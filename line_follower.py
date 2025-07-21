class GreedyLineFollower:
    """
    Implements a greedy algorithm to trace a dark line in an image starting from a user-defined pixel.
    """
    

    def __init__(self, color_threshold):
        """
        Initialize the line follower.
        Args:
            color_threshold (int): Grayscale threshold to consider a pixel part of the path (0 = black, 255 = white).
                                   Pixels below this value are treated as "dark".
        """
        self.color_threshold = color_threshold
    

    def is_dark_pixel(self, pixel_value):
        """
        Check if a given pixel value is considered dark.
        Args:
            pixel_value (int): Grayscale pixel intensity (0-255).
        Returns:
            bool: True if pixel is dark, False otherwise.
        """
        return pixel_value < self.color_threshold
    

    def get_neighbors(self, pixel, image):
        """
        Get all 8-connected neighboring pixels within the image bounds.
        Args:
            pixel (tuple): (x, y) coordinates of the current pixel.
            image (np.ndarray): 2D grayscale image.
        Returns:
            list: List of (x, y) coordinates of valid neighbors.
        """
        x, y = pixel
        height, width = image.shape
        neighbors = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    neighbors.append((nx, ny))

        return neighbors
    

    def follow_line(self, start_pixel, image):
        """
        Trace the darkest connected path in the image using greedy search.
        Args:
            start_pixel (tuple): (x, y) coordinates to start from.
            image (np.ndarray): 2D grayscale image.
        Returns:
            list: List of (x, y) coordinates that represent the traced path.
        """
        path = [start_pixel]
        visited = set()
        dark_neighbors = set()
        current_pixel = start_pixel

        while True:
            visited.add(current_pixel)
            neighbors = self.get_neighbors(current_pixel, image)

            # Collect unvisited dark neighbors
            for p in neighbors:
                if p not in visited and self.is_dark_pixel(image[p[1], p[0]]):
                    dark_neighbors.add(p)

            if not dark_neighbors:
                break  # End of path

            # Greedy choice: pick the next pixel with lowest (x, y) by default
            next_pixel = min(dark_neighbors)

            path.append(next_pixel)
            dark_neighbors.remove(next_pixel)
            current_pixel = next_pixel
        
        return path