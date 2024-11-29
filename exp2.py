import cv2
import os
from datetime import datetime

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Get frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Ask user if they want to save the video
    save_video = input("Do you want to save the video? (yes/no): ").strip().lower() == 'yes'
    out = None
    
    if save_video:
        # Create 'videos' directory if it doesn't exist
        if not os.path.exists('videos'):
            os.makedirs('videos')
        
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"videos/output_{timestamp}.mp4"
        
        # Define codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (frame_width, frame_height))
        
        if not out.isOpened():
            print("Error: Could not create video file.")
            return
        
        print(f"Saving video to {filename}")

    print("Press 'q' to stop the camera feed.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Save the frame if saving is enabled
        if save_video:
            out.write(frame)

        # Check for 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            choice = input("Do you want to quit? (yes/no): ").strip().lower()
            if choice == 'yes':
                break

    # Release the camera and video writer, and close the display window
    cap.release()
    if save_video:
        out.release()
    cv2.destroyAllWindows()

    if save_video:
        print(f"Video saved to {filename}")

if __name__ == "__main__":
    main()