import yaml
import os

# Python function to automatically create data.yaml config file
# 1. Reads "classes.txt" file to get list of class names
# 2. Creates data dictionary with correct paths to folders, number of classes, and names of classes
# 3. Writes data in YAML format to data.yaml

DATA_PATH = "./data/"
CLASSES_PATH = os.path.join(DATA_PATH, "classes.txt")
DATA_YML_PATH = os.path.join(DATA_PATH, "data.yml")


def create_data_yaml(path_to_classes_txt = CLASSES_PATH, path_to_data_yaml = DATA_YML_PATH):

    # Read class.txt to get class names
    if not os.path.exists(path_to_classes_txt):
        print(f'classes.txt file not found! Please create a classes.txt labelmap and move it to {path_to_classes_txt}')
        return
    with open(path_to_classes_txt, 'r') as f:
        classes = []
        for line in f.readlines():
            if len(line.strip()) == 0: 
                continue
            classes.append(line.strip())
    number_of_classes = len(classes)

    # Create data dictionary
    data = {
        'path': 'data',
        'train': 'images',
        'val': 'validation',
        'nc': number_of_classes,
        'names': classes
    }

    # Write data to YAML file
    with open(path_to_data_yaml, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    print(f'Created config file at {path_to_data_yaml}')

    return

create_data_yaml()