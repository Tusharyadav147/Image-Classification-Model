import dlib
import cv2

# Load the pre-trained face detector and facial landmark predictor
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks/shape_predictor_68_face_landmarks.dat")  # You need to download this file from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

# Load the image
image_path = "./new_data_left/image_13.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_detector(gray_image)

# Iterate through each detected face
for face in faces:
    # Predict facial landmarks
    landmarks = landmark_predictor(gray_image, face)

    # Draw landmarks on the image
    for i in range(68):  # Assuming you are using the 68-point facial landmark model
        x, y = landmarks.part(i).x, landmarks.part(i).y
        cv2.circle(image, (x, y), 1, (0, 0, 255), -1)  # Draw a red circle at each landmark point

# Display the result
cv2.imshow("Facial Landmarks", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
