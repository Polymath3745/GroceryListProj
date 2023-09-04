import cv2
import os

def take_pic():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        exit()

    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not capture frame")
        cap.release()
        exit()

    # Define the relative path to the "data" folder (sibling to the "utils" folder)
    data_folder = "data"

    # Specify the filename and path for the saved image
    image_filename = os.path.join(data_folder, "captured_image.jpg")

    # Save the captured frame as an image in the "data" folder
    cv2.imwrite(image_filename, frame)

    # Release the webcam
    cap.release()

    print("Image captured and saved successfully!")