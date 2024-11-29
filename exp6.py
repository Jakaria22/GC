import cv2
import numpy as np

def midpoint_line(x1, y1, x2, y2):
    """Implements the Midpoint Line Drawing Algorithm."""
    points = []  # List to store the points of the line
    
    dx = x2 - x1
    dy = y2 - y1

    # Determine the slope direction
    sx = 1 if dx > 0 else -1
    sy = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        p = 2 * dy - dx
        x, y = x1, y1
        for _ in range(dx + 1):
            points.append((x, y))
            x += sx
            if p >= 0:
                y += sy
                p -= 2 * dx
            p += 2 * dy
    else:
        p = 2 * dx - dy
        x, y = x1, y1
        for _ in range(dy + 1):
            points.append((x, y))
            y += sy
            if p >= 0:
                x += sx
                p -= 2 * dy
            p += 2 * dx

    return points


def draw_grid_and_labels(canvas, size, spacing=50):
    mid = size // 2
    for i in range(0, size + 1, spacing):
        cv2.line(canvas, (i, 0), (i, size), (50, 50, 50), 1)
        cv2.line(canvas, (0, i), (size, i), (50, 50, 50), 1)
        if i != mid:
            cv2.putText(canvas, f"{i - mid}", (i, mid + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)
            cv2.putText(canvas, f"{mid - i}", (mid + 5, i + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)
    
    cv2.line(canvas, (mid, 0), (mid, size), (100, 100, 100), 1)
    cv2.line(canvas, (0, mid), (size, mid), (100, 100, 100), 1)
    cv2.putText(canvas, "O", (mid + 5, mid + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)



if __name__ == "__main__":
    # Create a black canvas
    canvas_size = 500
    canvas = np.zeros((canvas_size, canvas_size, 3), dtype=np.uint8)
    draw_grid_and_labels(canvas,canvas_size)
    mid = canvas_size // 2


    try:
        x_start, y_start = map(int, input("Enter start point (x1, y1): ").split())
        x_end, y_end = map(int, input("Enter end point (x2, y2): ").split())

        # Get the line points using the Midpoint algorithm
        line_points = midpoint_line(x_start, y_start, x_end, y_end)

        # Draw the line on the canvas
        for x, y in line_points:
            canvas_x = x + mid
            canvas_y = mid - y
            if 0 <= canvas_x < canvas_size and 0 <= canvas_y < canvas_size:
                canvas[canvas_y, canvas_x] = (0, 255, 255)

        # Display the canvas
        cv2.imshow("Midpoint Line", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError:
        print("Invalid input! Please enter valid integers for the points.")
