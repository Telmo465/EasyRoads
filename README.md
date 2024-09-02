# EasyRoads

EasyRoads is a specialized tool designed to streamline the process of creating road scenarios with all the essential features required by the SILAB software. EasyRoads provides an intuitive interface for defining cross-sections, routes, and landscapes, which are fundamental for scenario creation in SILAB.

In addition to these core functionalities, EasyRoads introduces the ability to include traffic participants, enhancing the overall scenario setup. A standout feature of EasyRoads is its capability to generate road layouts directly from GPS coordinates, simplifying the process of road design.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.x**: Download from the [official Python website](https://www.python.org/downloads/).
- **pip**: Python's package manager (typically included with Python).

## Installation

1. **Clone the Repository**: 

    ```bash
    git clone https://github.com/Telmo465/EasyRoads.git
    cd EasyRoads
    ```

2. **Create a Virtual Environment** (Optional but recommended):

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**:

    Install the required packages listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

To run the application, execute the following command:

```bash
python3 main.py
