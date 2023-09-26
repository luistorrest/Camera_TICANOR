# Sequoia Multispectral Camera ROS Node

This Python code provides a ROS (Robot Operating System) node for interfacing with a Sequoia Multispectral Camera. It subscribes to raw image messages from the camera and allows you to recognize and display individual spectral bands in real-time.

## Prerequisites

Before running this code, make sure you have the following dependencies installed:

- [ROS (Robot Operating System)](http://wiki.ros.org/ROS/Installation): Install ROS on your system.

- [OpenCV](https://opencv.org/): You need OpenCV to work with image data. You can install it using pip:

- [sensor_msgs](http://wiki.ros.org/sensor_msgs): ROS package for sensor messages.

## Usage

1. Clone this repository to your ROS workspace.

2. Build your ROS workspace using `catkin_make`.

3. Launch the ROS node:

4. The code will subscribe to the `/sequoia/image_raw` topic, where the camera publishes raw image data.

5. The code will recognize the individual spectral bands (Red, Green, Blue, NIR) and display them in separate windows.

6. Press 'q' in any of the windows to exit the program.

## Customization

You can customize the code to work with your specific camera or color scheme by modifying the `band_colors` array in the `recognize_bands` method.

```python
# Define the colors of the four bands
band_colors = np.array([ [0, 0, 255],  # Red
 [0, 255, 0],  # Green
 [255, 0, 0],  # Blue
 [255, 255, 0]  # NIR
])


