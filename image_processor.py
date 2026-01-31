import cv2


class ImageProcessor:
    """
    This class contains static methods or instance methods for image processing logic.
    """

    @staticmethod
    def to_grayscale(image):
        """Converts BGR image to Grayscale."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def apply_blur(image, kernel_size):
        """
        Applies Gaussian Blur.
        kernel_size: Must be an odd number (checked internally).
        """
        k = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
        return cv2.GaussianBlur(image, (k, k), 0)

    @staticmethod
    def detect_edges(image):
        """Applies Canny Edge Detection."""
        # Convert to gray first for better edge detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Using standard threshold values
        edges = cv2.Canny(gray, 100, 200)
        # Convert back to BGR so it displays correctly in the app
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def adjust_brightness(image, value):
        """
        Adjusts brightness.
        value: Integer shift (positive or negative).
        """
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v = cv2.add(v, value)  # Prevents overflow using cv2.add
        final_hsv = cv2.merge((h, s, v))
        return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    @staticmethod
    def adjust_contrast(image, factor):
        """
        Adjusts contrast.
        factor: Float (1.0 is original).
        """
        return cv2.convertScaleAbs(image, alpha=factor, beta=0)

    @staticmethod
    def rotate_image(image, angle):
        """
        Rotates image by 90, 180, or 270 degrees.
        angle: 90, 180, or 270.
        """
        if angle == 90:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            return cv2.rotate(image, cv2.ROTATE_180)
        elif angle == 270:
            return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return image

    @staticmethod
    def flip_image(image, mode):
        """
        Flips image.
        mode: 0 for vertical, 1 for horizontal.
        """
        return cv2.flip(image, mode)

    @staticmethod
    def resize_image(image, width, height):
        """Resizes the image to specific dimensions."""
        return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
