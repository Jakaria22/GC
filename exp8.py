import matplotlib.pyplot as plt 
# Midpoint Circle Drawing Algorithm 
def draw_circle_midpoint(center, radius): 
    x_center, y_center = center
    x = 0 
    y = radius 
    d = 1 - radius  # Initial decision parameter 
    points = []  # To store points to be plotted 
    points.extend(get_circle_points(x_center, y_center, x, y))  # Plot initial points 
    print_circle_points(x_center, y_center, x, y)  # Print initial points 
    while x < y: 
        if d < 0:  # Midpoint is inside the circle 
            d = d + 2 * x + 3 
        else:  # Midpoint is outside or on the circle 
            d = d + 2 * (x - y) + 5 
            y -= 1 
        x += 1 
        points.extend(get_circle_points(x_center, y_center, x, y)) 
        print_circle_points(x_center, y_center, x, y)  # Print calculated points 
    return points 


# Function to calculate symmetric points 
def get_circle_points(xc, yc, x, y): 
    return [ 
        (xc + x, yc + y), (xc - x, yc + y), 
        (xc + x, yc - y), (xc - x, yc - y), 
        (xc + y, yc + x), (xc - y, yc + x), 
        (xc + y, yc - x), (xc - y, yc - x) 
    ] 


# Function to print symmetric points 
def print_circle_points(xc, yc, x, y): 
    points = get_circle_points(xc, yc, x, y) 
    for point in points:
          print(f"Point: {point}") 


# Main program 
def main(): 
    center = (0, 0)  # Center of the circle 
    radius = 10  # Radius of the circle 
    # Get points using the Midpoint Circle Algorithm 
    circle_points = draw_circle_midpoint(center, radius) 
    # Separate x and y coordinates for plotting 
    x_coords, y_coords = zip(*circle_points) 
    # Plot the circle 
    plt.figure(figsize=(6, 6)) 
    plt.scatter(x_coords, y_coords, s=10, color="blue")  # Plot points 
    plt.gca().set_aspect('equal', adjustable='box')  # Keep aspect ratio 
    plt.title("Circle Drawn Using Midpoint Algorithm") 
    plt.xlabel("X") 
    plt.ylabel("Y") 
    plt.grid(True) 
    plt.show() 
if __name__ == "__main__": 
    main()