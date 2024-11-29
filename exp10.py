import matplotlib.pyplot as plt 
# Liang-Barsky Line Clipping Algorithm 
def liang_barsky_clip(x_min, y_min, x_max, y_max, x1, y1, x2, y2): 

    dx = x2 - x1 
    dy = y2 - y1 
    # Define the parameterized boundaries 
    p = [-dx, dx, -dy, dy] 
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1] 
    t_min, t_max = 0.0, 1.0  # Initialize parameter t 
    for i in range(4): 
        if p[i] == 0:  # Line is parallel to one of the clipping edges 
            if q[i] < 0:  # Line is outside 
                return None 
        else: 
            t = q[i] / p[i] 
            if p[i] < 0: 
                t_min = max(t_min, t)  # Update t_min 
            else: 
                t_max = min(t_max, t)  # Update t_max 
    if t_min > t_max:  # Line is outside the clipping window 
        return None 
    # Calculate the clipped line endpoints 
    clipped_x1 = x1 + t_min * dx 
    clipped_y1 = y1 + t_min * dy 
    clipped_x2 = x1 + t_max * dx 
    clipped_y2 = y1 + t_max * dy 
    return (clipped_x1, clipped_y1, clipped_x2, clipped_y2) 
# Visualization and Input Handling 
def main(): 
    # Take user inputs 
    print("Enter the clipping rectangle (x_min, y_min, x_max, y_max):")

    x_min, y_min, x_max, y_max = map(int, input().split()) 
    print("Enter the coordinates of the line (x1, y1, x2, y2):") 
    x1, y1, x2, y2 = map(int, input().split()) 
    # Plot clipping rectangle 
    plt.figure() 
    plt.plot([x_min, x_max, x_max, x_min, x_min], 
             [y_min, y_min, y_max, y_max, y_min], 'r-', label="Clipping Window") 
    # Plot the original line 
    plt.plot([x1, x2], [y1, y2], 'b--', label="Original Line") 
    # Perform clipping 
    clipped_line = liang_barsky_clip(x_min, y_min, x_max, y_max, x1, y1, x2, y2) 
    if clipped_line: 
        cx1, cy1, cx2, cy2 = clipped_line 
        plt.plot([cx1, cx2], [cy1, cy2], 'g-', label="Clipped Line") 
        print(f"Clipped Line: ({cx1}, {cy1}) to ({cx2}, {cy2})") 
    else: 
        print("The line is outside the clipping window and has been rejected.") 
    # Show plot 
    plt.xlabel("X-axis") 
    plt.ylabel("Y-axis") 
    plt.title("Liang-Barsky Line Clipping") 
    plt.legend() 
    plt.grid(True) 
    plt.show() 
if __name__ == "__main__": 
    main() 