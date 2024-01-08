import cv2
import requests
from io import BytesIO
import numpy as np
import face_recognition
import cvzone
import pickle

# Replace these with your actual camera details

# http://46.11.254.195/GetTargetFace
api_url = 'http://46.11.254.195/GetSnapshot'
username = 'admin'
password = 'ispy8191'

print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded")

while True:
    try:
        # Fetch the image from the camera
        response = requests.get(api_url, auth=(username, password))
        response.raise_for_status()

        # Read the image into a numpy array
        image_array = cv2.imdecode(np.asarray(bytearray(response.content)), cv2.IMREAD_COLOR)

        imgS = cv2.resize(image_array, (0, 0), None, 1, 1)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

        # Display the image
        cv2.imshow('Camera Snapshot', image_array)
    
        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print("matches", matches)
                print("faceDis", faceDis)

                matchIndex = np.argmin(faceDis)
                print("Match Index", matchIndex)

                if matches[matchIndex]:
                    print("Known Face Detected")
                    print(studentIds[matchIndex])
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                    imgBackground = cvzone.cornerRect(image_array, bbox, rt=0)
                    id = studentIds[matchIndex]

        else:
            modeType = 0
            counter = 0
        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"Failed to fetch or display image: {e}")

# Close the OpenCV window
cv2.destroyAllWindows()
