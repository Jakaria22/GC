import cv2
import os

def process_image(file_path: str):
    """Load, display, and save an image."""
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Unable to load image at {file_path}")
    
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    file_name, file_ext = os.path.splitext(file_path)
    save_path = f"{file_name}_saved{file_ext}"
    cv2.imwrite(save_path, image)
    print(f"Image saved to {save_path}")


if __name__ == "__main__":
    try:
        image_path = input("Enter the path to the image file: ").strip()
        process_image(image_path)
    except FileNotFoundError as e:
        print(e)
