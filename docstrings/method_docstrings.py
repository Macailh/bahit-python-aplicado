class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        """
        Compute the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return 2 * 3.14159 * self.radius
