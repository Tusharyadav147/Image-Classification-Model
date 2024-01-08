import cv2
import os

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Set the directory to save the face data
data_dir = 'face_data'

# Create the data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Counter for the number of face samples
sample_count = 0

# Loop to capture frames and detect faces
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Flip the frame horizontally to prevent mirroring
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the faces and save the samples
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Save the face region as an image file
        face_roi = gray[y:y+h, x:x+w]
        sample_count += 1
        # file_name = os.path.join(data_dir, f'face_{sample_count}.png')
        # cv2.imwrite(file_name, face_roi)

        print(f"Face {sample_count} captured!")

    # Display the resulting frame
    cv2.imshow('Face Data Collection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
