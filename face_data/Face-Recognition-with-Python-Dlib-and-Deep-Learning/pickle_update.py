import pickle

def load_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return None

print(load_data('encodings.pickle').keys())
# print(load_data('encodings.pickle').values())
print(type(load_data('encodings.pickle')))