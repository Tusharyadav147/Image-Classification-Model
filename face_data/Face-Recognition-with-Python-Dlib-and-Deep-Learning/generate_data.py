import cv2
import os

def create_dataset(camera_index=0, max_images=30):
    # Get user's name
    user_name = input("Enter your name: ")

    # Create output folder based on user's name
    output_folder = os.path.join("dataset", user_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open camera
    cap = cv2.VideoCapture(camera_index)

    # Set the resolution of the camera (adjust as needed)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Counter for the number of captured images
    count = 0

    while count < max_images:
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow("Capture", frame)

        # Save the image with a unique filename
        img_filename = os.path.join(output_folder, f"{user_name}_{count}.jpg")
        cv2.imwrite(img_filename, frame)

        # Increment the counter
        count += 1

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create the dataset
    create_dataset()
