class Rectangle:
    """
    Represents a rectangle.

    Attributes:
    - width (float): Width of the rectangle.
    - height (float): Height of the rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
        float: The area of the rectangle.
        """
        return self.width * self.height
