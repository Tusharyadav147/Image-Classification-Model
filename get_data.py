import requests
import os

# Replace this URL with your actual camera IP
api_url = 'http://46.11.254.195/GetSnapshot'

# Replace 'your_username' and 'your_password' with your actual credentials
username = 'admin'
password = 'ispy8191'

# Number of images to download
num_images = 50

# Directory to save the images
save_directory = 'new_data_left'

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Loop to download multiple images
for i in range(num_images):
    try:
        # Make a GET request to the API with authentication
        response = requests.get(api_url, auth=(username, password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the image to the specified directory
            image_filename = f'image_{i+1}.jpg'
            image_path = os.path.join(save_directory, image_filename)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Image {i+1} downloaded successfully.")
        else:
            print(f"Failed to download image {i+1}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

print("Image download process completed.")
