import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def simulate_data_stream(n_points=1):
    """
    Simulates a data stream with regular patterns, noise, and random anomalies.
    :param n_points: Number of data points to simulate
    :return: A numpy array containing the simulated data
    """
    # Time sequence for our simulated data
    time = np.arange(n_points)
    
    # Regular pattern (sine wave) with random noise
    data = np.sin(0.1 * time) + np.random.normal(0, 0.1, size=n_points)
    
    # Introduce some anomalies (random spikes)
    anomalies = np.random.choice([False, True], size=n_points, p=[0.95, 0.05])
    data[anomalies] += np.random.uniform(5, 10, size=anomalies.sum())  # random spikes
    
    return data

def detect_anomalies(data, threshold=3, window_size=100):
    """
    Detects anomalies in the latest segment of the data stream.
    :param data: The data stream as a numpy array
    :param threshold: Z-score threshold for identifying anomalies
    :param window_size: Number of latest data points to analyze
    :return: Indices of anomalies within the current window
    """
    
    # Check if window_size is valid
    if window_size > len(data):
        window_size = len(data)  # Set window to data length if data is shorter than the window  
          
    # Use only the last 'window_size' points for Z-score calculation
    recent_data = data[-window_size:]
    z_scores = zscore(recent_data)
    
    # Find anomalies within the window
    anomalies = np.where(np.abs(z_scores) > threshold)[0] + len(data) - window_size
    
    return anomalies

def update_plot(ax, line, scatter, data_stream, anomalies):
    """Updates the plot with the current data stream and detected anomalies."""

    # Update plot data
    line.set_data(range(len(data_stream)), data_stream)

    # Check if anomalies exist and update scatter plot
    if len(anomalies) > 0:
        anomaly_values = [data_stream[j] for j in anomalies if j < len(data_stream)]  # Ensure valid indices
        scatter.set_offsets(np.c_[anomalies, anomaly_values])
    else:
        # Clear scatter if no anomalies by passing an empty 2D array
        scatter.set_offsets(np.empty((0, 2)))

    # Dynamically adjust y-axis based on current data range
    ax.set_ylim(min(data_stream) - 1, max(data_stream) + 1)
    ax.set_xlim(0, len(data_stream))

    # Render and pause briefly to simulate real-time updates
    plt.pause(0.05)  # Use plt.pause to simulate real-time updates    


def run_simulation(num_points=1000, threshold=3, window_size=100):
    # Initialize plot for the data stream and anomalies
    fig, ax = plt.subplots()
    line, = ax.plot([], [], label="Data Stream")  # Line for the data stream
    scatter = ax.scatter([], [], color='red', label="Anomalies", marker='x')  # Scatter plot for anomalies
    ax.set_xlim(0, 100)
    ax.set_ylim(-2, 12)
    ax.set_title("Real-Time Data Stream with Anomalies")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()
    
    # Initialize an empty data stream list
    data_stream = []

    for i in range(num_points):  # Loop to simulate specified number of data points
        # Simulate the next data point
        data_point = simulate_data_stream(1)[0]

        # Validate that data_point is a real number
        if np.isnan(data_point) or np.isinf(data_point):
            print("Warning: Invalid data point detected; skipping.")
            continue  # Skip this iteration if data is invalid
    
        data_stream.append(data_point)

        # Detect anomalies in the current data stream
        if len(data_stream) >= window_size:
            anomalies = detect_anomalies(np.array(data_stream), threshold, window_size)
        else:
            anomalies = []
        
        # Update every 10th data point for smoother performance
        if i % 10 == 0:
            update_plot(ax, line, scatter, data_stream, anomalies)

    plt.show()  # Show the final plot  
    
# Run the simulation
run_simulation()