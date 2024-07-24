import openrouteservice as ors
import folium
import operator
from functools import reduce
import numpy as np 
import matplotlib.pyplot as plt 
from geopy.distance import geodesic
import math
from openrouteservice import convert
import random

#calc raio final

def calculate_radius_from_chord_and_arc(chord_length, arc_length):
    # Ensure valid input values
    if chord_length <= 0 or arc_length <= 0:
        raise ValueError("Chord length and arc length must be positive values.")

    # Calculate the central angle in radians
    arg_asin = chord_length / (2 * arc_length)

    # Ensure the argument falls within the valid range [-1, 1]
    if not -1 <= arg_asin <= 1:
        raise ValueError("Invalid argument for arcsin. Check chord and arc lengths.")

    theta = 2 * math.asin(arg_asin)

    # Calculate the radius
    radius = arc_length / theta

    return radius

#calc dist

def calculate_distance(coord2, coord1):
    return geodesic(coord2, coord1).meters

#calc bearing

def get_bearing(lat1, long1, lat2, long2):
    dLon = (long2 - long1)
    x = math.cos(math.radians(lat2)) * math.sin(math.radians(dLon))
    y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(dLon))
    brng = np.arctan2(x,y)
    brng = np.degrees(brng)
    if brng < 0:
        brng += 360
        

    return brng

def group_coordinates_by_segments(coordinates):
    segments = []
    

    for i in range(len(coordinates) - 1):
        
        segment = [tuple(coordinates[i]), tuple(coordinates[i + 1]), calculate_distance(coordinates[i], coordinates[i + 1]), get_bearing(coordinates[i][1],coordinates[i][0],coordinates[i+1][1],coordinates[i+1][0])]
        segments.append(segment)

    for i in range(0, len(segments)):
        if i == 0:
            bearing_change=0
            curvature = 1
            radius = 1
        else:
            bearing_change = segments[i][3] - segments[i - 1][3]
            curvature = (bearing_change/segments[i][2]) * 1000
            radius = 1/(curvature/1000)

        # Adjust for changes across 0/360 degrees
        if bearing_change < -180:
            bearing_change += 360
        elif bearing_change > 180:
            bearing_change -= 360

            #segments[i].append(abs(bearing_change))
        segments[i].append(bearing_change)
        segments[i].append(curvature)
        segments[i].append(radius)

    return segments

def merge_segments(segments, max_length_difference=20):
    merged_segments = []
    size = 0
    total = len(segments)-1
    while size <= total:
        #print("estamos aqui", size)
        if segments[size][2] <= max_length_difference and size<total:
            merged_segments.append([segments[size][0], segments[size + 1][1]] + [segments[size][2] + segments[size+1][2]] + segments[size + 1][3:])
            #print(segments[i][1])
            size += 2
            #print("saltou", size)
        else:
            # Add a new segment
            merged_segments.append(segments[size])
            size += 1


    return merged_segments  

def re_coordinates(merged_segments):

    new_coordinates = []

    for segment in merged_segments:
        new_coordinates.append(segment[0])

    new_coordinates.append(merged_segments[-1][1])

    #print(new_coordinates)

    result = (group_coordinates_by_segments(new_coordinates))
    return result

def merge_by_bearing(segments, max_bearing_difference=3):
    merged_segments = []
    total = len(segments)

    if total > 0:
        merged_segments.append(segments[0])

        for size in range(1, total):
            current_segment = segments[size]

            # Check if the bearing change is less than the threshold
            if abs(current_segment[4]) <= max_bearing_difference:
                # Merge the current segment with the last one
                merged_segments[-1] = [merged_segments[-1][0], current_segment[1]] + [merged_segments[-1][2] + current_segment[2]] + current_segment[3:]
            else:
                # Add a new segment
                merged_segments.append(current_segment)

    return merged_segments

def add_straigth(segments, max_curvature=15):
    merged_segments = []
    for segment in segments:
        if len(segment) <= 7:
            if abs(segment[5]) < max_curvature:
                segment.append("Straight")
                merged_segments.append(segment)
            else:
                segment.append("Curve")
                merged_segments.append(segment)
        else:
            if abs(segment[5]) < max_curvature:
                segment[7] = "Straight"
                merged_segments.append(segment)
            else:
                segment[7] = "Curve"
                merged_segments.append(segment)

    return merged_segments

def merge_by_curve(segments, max_bearing_difference=10):
    merged_segments = []
    total = len(segments)

    if total > 0:
        merged_segments.append(segments[0])

        for size in range(1, total):
            current_segment = segments[size]
            previous_segment = merged_segments[-1]

            # Check if the conditions for merging are met
            # Check if the conditions for merging are met
            if (previous_segment[7] == "Curve" and current_segment[7] == "Curve" and
                    abs(current_segment[4]) <= max_bearing_difference and
                    previous_segment[4] * current_segment[4] > 0):
                # Merge the current segment with the last one
                merged_radius = (previous_segment[6] + current_segment[6]) / 2.0
                new_bearchange = (current_segment[4] + previous_segment[4])
                new_length = (previous_segment[2] + current_segment[2])
                merged_segments[-1] = [previous_segment[0], current_segment[1]] + \
                                      [new_length] + [current_segment[3]] + [new_bearchange] + \
                                      [current_segment[5]] + [merged_radius] + \
                                      [current_segment[7]]
            elif (previous_segment[7] == "Straight" and current_segment[7] == "Straight"):
                new_length = (previous_segment[2] + current_segment[2])
                new_bearchange = (current_segment[4] + previous_segment[4])
                merged_segments[-1] = [previous_segment[0], current_segment[1]] + \
                                      [new_length] + [current_segment[3]] + [new_bearchange] + \
                                      current_segment[5:]
            else:
                # Add a new segment
                merged_segments.append(current_segment[0:5] + [1.0] + [1.0] + [current_segment[7]])

    return merged_segments

def final_segments(segments):
    merged_segments = []

    for segment in segments:
        if segment[7] == "Curve":
            curvature = (segment[4]/segment[2])*1000
            radius = 1/(curvature/1000)
            merged_segments.append(segment[0:5] + [curvature] + [radius] + segment[7:])
        else:
            merged_segments.append(segment)
    
    return merged_segments

def calc_radius_certo(segments_straith, segments_arc):
    new_segments=[]
    for i in range(len(segments_arc)):
        curva = "Straight"
        raio = 1.0
        if segments_arc[i][7] == "Curve":
            if (segments_arc[i][5]*(-1)>0):
                curva = "Curva_esq"
                raio = calculate_radius_from_chord_and_arc(segments_straith[i][2], segments_arc[i][2])
        if segments_arc[i][7] == "Curve":
            if (segments_arc[i][5]*(-1)<0):
                curva = "Curva_dir"
                raio = calculate_radius_from_chord_and_arc(segments_straith[i][2], segments_arc[i][2])
        
        new_segments.append(segments_arc[i][0:3] + [raio] + [curva] )


    return new_segments

def transcript(raio_certo):
    total = []
    for segment in raio_certo:
        if segment[4] == "Straight":
            total.append("Straight(%d)" % segment[2])
            #total += (math.floor(segment[2]))
        elif segment[4] == "Curva_dir":
            total.append("Bend(%d, %d)" % (segment[2],segment[3]))
            #total += (math.floor(segment[2]))
        elif segment[4] == "Curva_esq":
            total.append("Bend(%d, %d)" % (segment[2],-segment[3]))
            #total += (math.floor(segment[2]))
    return total

def random_division(total_length):
    min_segment_length = 100  # Minimum segment length in meters
    max_segment_length = 1000  # Maximum segment length in meters
    num_segments = max(1, 2*round(total_length / max_segment_length))  # Calculate the number of segments
    segments = []
    remaining_length = total_length
    for _ in range(num_segments - 1):
        # Generate a random length for the segment, ensuring it's at least 50 meters and does not exceed the maximum length
        segment_length = random.randint(min_segment_length, min(max_segment_length, remaining_length - min_segment_length * (num_segments - len(segments) - 1)))
        segments.append(segment_length)
        remaining_length -= segment_length
    
    # The last segment takes the remaining length
    segments.append(remaining_length)
    
    return segments

def generate_normal_distribution(num_samples, max_tilt, mean=0, std_deviation=0.7):
    # Generate samples from a normal distribution with mean=0 and std deviation=1
    samples = np.random.normal(loc=0, scale=std_deviation, size=num_samples)
    # Scale the samples to the desired range [-x, x]
    scaled_samples = samples * std_deviation * max_tilt  # Adjusted for standard deviation
    # Clip the scaled samples to ensure they are within the range [-x, x]
    clipped_samples = np.clip(scaled_samples, -max_tilt, max_tilt)
    clipped_samples[0] = 0  # Set the first item to 0
    clipped_samples[-1] = 0
    samples_list = [round(sample, 1) for sample in clipped_samples]
    return samples_list

def height_profile(total,max_tilt_abs=3):
    divisions = random_division(total)
    n_samples = len(divisions)
    tilt = generate_normal_distribution(n_samples,max_tilt_abs)
    height = []
    for x in range(n_samples):
        if x == n_samples-1:
            height.append("(%.2f, %.2f, 1000)" % (tilt[x],divisions[x]))
        else:
            height.append("(%.2f, %.2f, 1000)," % (tilt[x],divisions[x]))
    return height

# client =  ors.Client(key='5b3ce3597851110001cf6248673af3d65161476698e39eba4b28fc12')
# coords =  [[-8.567732098809747,40.92098933956433], [-8.49826520133499,40.42342860557837]]
# geometry = client.directions(coords)['routes'][0]['geometry']
# decoded = convert.decode_polyline(geometry)
# points_list = decoded.get('coordinates')
# coordinates_array = points_list

def calc_gps_sections(points_list):
    result_segments = group_coordinates_by_segments(points_list)
    merged_segments = merge_segments(result_segments)
    new_points =  re_coordinates(merged_segments)
    new_segments = merge_by_bearing(new_points)
    new_points_bearing = re_coordinates(new_segments)
    segments_type = add_straigth(new_points_bearing)
    new_segments_curves = merge_by_curve(segments_type)
    final_final = final_segments(new_segments_curves)
    final = re_coordinates(new_segments_curves)
    raio_certo = calc_radius_certo(final, final_final)
    return (transcript(raio_certo))
