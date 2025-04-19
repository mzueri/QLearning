import json
import os

def save_Q_as_json(Q, dir_file): 
    assert dir_file.endswith('.json'), "Make sure the file path points to a JSON file. "

    Q=[[elem[0],elem[1],elem[2]] for elem in Q]

    with open(dir_file, 'w') as f:
        json.dump(Q, f)


def read_json_as_Q(dir_file):
    assert os.path.exists(dir_file), "File path is not valid. "
    assert os.path.isfile(dir_file), "The given path is not a file. "
    assert dir_file.endswith('.json'), "The file is not a JSON file. "
    
    # Load the data from the JSON file
    with open(dir_file, 'r') as f:
        Q = json.load(f)

    Q=[[elem[0],{"entry":tuple(elem[1]["entry"]),"mark":elem[1]["mark"]},elem[2]] for elem in Q]

    return Q
