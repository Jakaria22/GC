import cv2 
import numpy as np 
# A black canvas with a size of 500x500 pixels and 3 color channels (RGB) image 
image=np.zeros((500, 500, 4), dtype=np.uint8)
# Drawing a simple line (start point, end point, color, thickness) 

cv2.line(image, (50, 50), (450, 50), (0, 255, 0), 3) # Green line
cv2.arrowedLine(image, (50, 100), (450, 100), (255, 0, 0), 2) 

cv2.rectangle(image, (50, 150), (450, 250), (0, 0, 255), 2) #  # 
cv2.circle(image, (250, 350), 50, (255, 25, 255), -1) 

cv2.putText(image, 'OpenCV Shapes', (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 
255, 255), 2, cv2.LINE_AA) 



# Show the final image 
cv2.imshow("Image", image) 

# Wait for a key press and close the window 
cv2.waitKey(0) 
cv2.destroyAllWindows() 


