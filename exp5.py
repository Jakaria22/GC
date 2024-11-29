import cv2
import numpy as np

def dda_line(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))  
    
    x_increment = dx / steps  
    y_increment = dy / steps
    
    x, y = x1, y1  # Start point
    for _ in range(steps + 1):
        points.append((round(x), round(y)))  
        x += x_increment
        y += y_increment
    
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

        # Calculate the line points using DDA algorithm
        line_points = dda_line(x_start, y_start, x_end, y_end)

        # Draw the line on the canvas
        for x, y in line_points:
            canvas_x = x + mid
            canvas_y = mid - y
            if 0 <= canvas_x < canvas_size and 0 <= canvas_y < canvas_size:
                canvas[canvas_y, canvas_x] = (0, 255, 255)

        # Display the canvas
        cv2.imshow("DDA Line", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError:
        print("Invalid input! Please enter valid integers for the points.")
