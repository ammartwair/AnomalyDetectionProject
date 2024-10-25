# Anomaly Detection Project

## Overview

This project simulates a real-time data stream with added anomalies and implements a Z-score-based anomaly detection algorithm. The primary goal is to identify unusual patterns in a continuous flow of data, which can represent various metrics such as financial transactions or system metrics.

## Features

- Simulates a data stream with a sine wave pattern, noise, and random anomalies.
- Real-time visualization of the data stream and detected anomalies.
- Utilizes the Z-score method for anomaly detection.
- Adjustable parameters for data simulation and anomaly detection.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)

## Installation

To run this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ammartwair/AnomalyDetectionProject.git
   cd AnomalyDetectionProject
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:

- On Windows:
   ```bash
   env\Scripts\activate
   ```

- On macOS/Linux:
   ```bash
   source env/bin/activate
   ```

4. **Install the required packages**: 
   ```bash
   pip install -r requirements.txt
   ```
## Usage

To run the anomaly detection simulation, execute the following command:
   ```bash
   python anomaly_detection.py
   ```

The simulation will display a real-time plot of the data stream, highlighting any detected anomalies in red.

## Algorithm Explanation

This code simulates a real-time data stream, where each data point follows a sine wave pattern with added random noise.
At random points, anomalies are introduced as sudden spikes in the data.
Anomaly detection is based on the Z-score method, which measures how far each data point is from the mean in terms of standard deviations.
Points with a Z-score exceeding a threshold (3 by default) are flagged as anomalies.

### Why Z-score Method

This method is straightforward and effective for normally distributed data with noise.
Z-scores help differentiate typical noise from unusual spikes.

## Limitations

The Z-score method may not work as effectively for non-normal or heavily seasonal data.
For such cases, alternative methods like seasonal decomposition or machine learning models could be considered.

## Future Improvements 

- Implement additional anomaly detection algorithms (e.g., Isolation Forest, Local Outlier Factor).
- Enhance the model to adapt to concept drift.
- Include performance metrics to evaluate the effectiveness of the anomaly detection.
- Add unit tests to ensure code robustness and reliability.