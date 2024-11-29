import matplotlib.pyplot as plt 
# Region codes 
INSIDE = 0  # 0000 
LEFT = 1    # 0001 
RIGHT = 2   # 0010

BOTTOM = 4  # 0100 
TOP = 8     # 1000 
# Function to compute region code 
def compute_code(x, y, x_min, y_min, x_max, y_max): 
    code = INSIDE 
    if x < x_min: 
        code |= LEFT 
    elif x > x_max: 
        code |= RIGHT 
    if y < y_min: 
        code |= BOTTOM 
    elif y > y_max: 
        code |= TOP 
    return code 
# Cohen-Sutherland Line Clipping Algorithm 
def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max): 
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max) 
    code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max) 
    accept = False 
    while True: 
        if code1 == 0 and code2 == 0:  # Trivially accept 
            accept = True 
            break 
        elif code1 & code2 != 0:  # Trivially reject 
            break 
        else: 
            # Calculate intersection 
            x, y = 0.0, 0.0
            code_out = code1 if code1 != 0 else code2 
            if code_out & TOP: 
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1) 
                y = y_max 
            elif code_out & BOTTOM: 
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1) 
                y = y_min 
            elif code_out & RIGHT: 
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1) 
                x = x_max 
            elif code_out & LEFT: 
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1) 
                x = x_min 
            if code_out == code1: 
                x1, y1 = x, y 
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max) 
            else: 
                x2, y2 = x, y 
                code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max) 
    if accept: 
        return (x1, y1, x2, y2) 
    else: 
        return None 
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
    clipped_line = cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max) 
    if clipped_line: 
        cx1, cy1, cx2, cy2 = clipped_line 
        plt.plot([cx1, cx2], [cy1, cy2], 'g-', label="Clipped Line") 
        print(f"Clipped Line: ({cx1}, {cy1}) to ({cx2}, {cy2})") 
    else: 
        print("The line is outside the clipping window and has been rejected.") 
    # Show plot 
    plt.xlabel("X-axis") 
    plt.ylabel("Y-axis") 
    plt.title("Cohen-Sutherland Line Clipping") 
    plt.legend() 
    plt.grid(True) 
    plt.show() 
if __name__ == "__main__": 
    main()