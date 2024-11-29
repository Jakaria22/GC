import cv2
import numpy as np

def bresenham_circle(xc, yc, r):
    points = []
    x, y = 0, r
    d = 3 - 2 * r
    while x <= y:
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x), (xc + y, yc - x), (xc - y, yc - x)
        ])
        if d <= 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
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
    canvas_size = 1001
    canvas = np.zeros((canvas_size, canvas_size, 3), dtype=np.uint8)
    draw_grid_and_labels(canvas, canvas_size)
    mid = canvas_size // 2

    try:
        xc, yc = map(int, input("Enter the center of the circle (xc, yc): ").split())
        r = int(input("Enter the radius of the circle: "))

        # Get the circle points using Bresenham's algorithm
        circle_points = bresenham_circle(xc, yc, r)

        # Draw the circle on the canvas
        for x, y in circle_points:
            canvas_x = x + mid
            canvas_y = mid - y
            if 0 <= canvas_x < canvas_size and 0 <= canvas_y < canvas_size:
                canvas[canvas_y, canvas_x] = (0, 255, 0)

        # Display the canvas
        cv2.imshow("Bresenham's Circle with Grid", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError:
        print("Invalid input! Please enter valid integers for the center and radius.")

