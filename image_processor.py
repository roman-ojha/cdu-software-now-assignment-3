import cv2


class ImageProcessor:
    """
    This class contains static methods or instance methods for image processing logic.
    """

    @staticmethod
    def to_grayscale(image):
        """This method will convert the input image to grayscale."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def apply_blur(image, kernel_size):
        """
        This method will apply a Gaussian blur to the input image.
        and kernel size will be a odd number and it will be checked internally.
        """
        k = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
        return cv2.GaussianBlur(image, (k, k), 0)

    @staticmethod
    def detect_edges(image):
        """This method will apply Canny edge detection to the input image."""
        # Convert to gray first for better edge detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Using standard threshold values
        edges = cv2.Canny(gray, 100, 200)
        # Convert back to BGR so it displays correctly in the app
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def adjust_brightness(image, value):
        """This method will adjust the brightness of the input image."""
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v = cv2.add(v, value)  # Prevents overflow using cv2.add
        final_hsv = cv2.merge((h, s, v))
        return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    @staticmethod
    def adjust_contrast(image, factor):
        "This method will adjust the contrast of the input image."
        return cv2.convertScaleAbs(image, alpha=factor, beta=0)

    @staticmethod
    def rotate_image(image, angle):
        """This method will rotate the input image by a specified angle (90, 180, or 270 degrees)."""
        if angle == 90:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            return cv2.rotate(image, cv2.ROTATE_180)
        elif angle == 270:
            return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return image

    @staticmethod
    def flip_image(image, mode):
        """This method will flip the input image either vertically or horizontally based on the mode parameter. if mode is 0, it will flip vertically; if mode is 1, it will flip horizontally."""
        return cv2.flip(image, mode)

    @staticmethod
    def resize_image(image, width, height):
        """This method will resize the input image to the specified width and height using cv2.resize with INTER_AREA interpolation for better quality when reducing size."""
        return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
