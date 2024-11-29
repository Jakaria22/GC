import cv2
import numpy as np

def bresenham_line(x1, y1, x2, y2):
    points, dx, dy = [], abs(x2 - x1), abs(y2 - y1)
    sx, sy, err = (1 if x1 < x2 else -1), (1 if y1 < y2 else -1), dx - dy
    while True:
        points.append((x1, y1))
        if (x1, y1) == (x2, y2): break
        e2 = 2 * err
        if e2 > -dy: err, x1 = err - dy, x1 + sx
        if e2 < dx: err, y1 = err + dx, y1 + sy
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
    size = 501  
    canvas = np.zeros((size, size, 3), dtype=np.uint8)
    draw_grid_and_labels(canvas, size)
    mid = size // 2

    try:
        x1, y1 = map(int, input("Enter start point (x1, y1): ").split())
        x2, y2 = map(int, input("Enter end point (x2, y2): ").split())
        
        line_points = bresenham_line(x1 + mid, mid - y1, x2 + mid, mid - y2)
        
        for x, y in line_points:
            if 0 <= x < size and 0 <= y < size:
                canvas[y, x] = (255, 0, 255)

        cv2.imshow("Bresenham's Line with Graph Paper", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError:
        print("Invalid input! Please enter valid integers for the points.")