import cv2
import face_recognition
import pickle
import os

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    imgList.append(img)
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img_rgb)
        
        if len(face_locations) > 0:
            encode = face_recognition.face_encodings(img_rgb, face_locations)[0]
            encodeList.append(encode)
            
            # Draw rectangle and display encoding on the image
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, f'Encoding: {encode}', (left, bottom + 25), font, 0.6, (255, 255, 255), 1)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save the images with encodings drawn on them
for i, img in enumerate(imgList):
    file_name = os.path.join("Sample_data", f'face_{i}.png')
    print(file_name)
    cv2.imwrite(f'face_{i}.png', img)

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
