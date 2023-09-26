import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image

class SequoiaMultispectralCamera:
    def __init__(self):
        """
        Initializes the SequoiaMultispectralCamera class.

        This class interfaces with a multispectral camera, subscribes to image messages,
        and provides methods for recognizing the individual spectral bands.

        Attributes:
            bridge: CvBridge object for image message conversion.
            image_sub: ROS subscriber for the raw image topic.
            image: Current image received from the camera.
        """
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/sequoia/image_raw", Image, self.image_callback)
        self.image = None

    def image_callback(self, msg):
        """
        Callback function for handling incoming image messages.

        Args:
            msg (sensor_msgs.msg.Image): The raw image message.
        """
        self.image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

    def recognize_bands(self):
        """
        Recognizes and separates the spectral bands from the captured image.

        This method splits the input image into its constituent spectral bands based on
        predefined colors and returns them as separate masks.

        Returns:
            list: A list of numpy arrays representing the spectral band masks.
        """
        # Split the image into the four bands
        bands = np.split(self.image, 4, axis=2)

        # Define the colors of the four bands
        band_colors = np.array([
            [0, 0, 255],  # Red
            [0, 255, 0],  # Green
            [255, 0, 0],  # Blue
            [255, 255, 0]  # NIR
        ])

        # Create a mask for each band
        band_masks = []
        for i in range(4):
            band_mask = np.zeros((self.image.shape[0], self.image.shape[1]), dtype=np.uint8)
            band_mask[np.where(np.all(bands[i] == band_colors[i], axis=2))] = 255
            band_masks.append(band_mask)

        # Return the band masks
        return band_masks

if __name__ == "__main__":
    rospy.init_node("sequoia_multispectral_camera_node")

    camera = SequoiaMultispectralCamera()

    while not rospy.is_shutdown():
        # Get the image from the camera
        camera.image_callback()

        # Recognize the bands
        band_masks = camera.recognize_bands()

        # Display the band masks
        for i in range(4):
            cv2.imshow("Band {}".format(i), band_masks[i])
            cv2.waitKey(1)

        # If the user presses 'q', quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all windows
    cv2.destroyAllWindows()

