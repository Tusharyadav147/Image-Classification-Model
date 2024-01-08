import pickle
import cv2
import os
import shutil

from utils import get_image_paths
from utils import face_encodings


root_dir = "dataset"
class_names = os.listdir(root_dir)

def load_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        data = {}
        return data

def save_data(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
    
def update_pickle(file_path, new_data):
    existing_data = load_data(file_path)

    if existing_data is not None:
        # Update the existing data with new_data
        existing_data.update(new_data)
    else:
        # If the file doesn't exist, create it with the new_data
        existing_data = new_data

    # Save the updated data back to the pickle file
    save_data(file_path, existing_data)


if class_names:  

    pickle_file_path = "encodings.pickle"
            
    # get the paths to the images
    image_paths = get_image_paths(root_dir, class_names)
    # initialize a dictionary to store the name of each person and the corresponding encodings
    name_encondings_dict = {}

    # initialize the number of images processed
    nb_current_image = 1
    # now we can loop over the image paths, locate the faces, and encode them
    for image_path in image_paths:
        print(f"Image processed {nb_current_image}/{len(image_paths)}")
        # load the image
        image = cv2.imread(image_path)
        # get the face embeddings
        encodings = face_encodings(image)
        # get the name from the image path
        name = image_path.split(os.path.sep)[-2]
        # get the encodings for the current name
        e = name_encondings_dict.get(name, [])
        # update the list of encodings for the current name
        e.extend(encodings)
        # update the list of encodings for the current name
        name_encondings_dict[name] = e
        nb_current_image += 1

    # save the name encodings dictionary to disk
    # with open("encodings.pickle", "wb") as f:
    #     pickle.dump(name_encondings_dict, f)
        
    update_pickle(pickle_file_path, name_encondings_dict)

    sub_folder = os.listdir('dataset')
    for i in sub_folder:
        source_folder = f'dataset/{i}'
        destination_folder = f'encoded_dataset'
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.move(source_folder, destination_folder)

else:
    print("Model is updated with the DataSet!")