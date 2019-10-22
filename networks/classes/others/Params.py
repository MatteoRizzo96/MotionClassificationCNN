import json
import logging
import os


class Params:
    """
    Class that loads hyperparameters from a json file.

    Example:
    params = Params(json_path)
    print(params.learning_rate)
    params.learning_rate = 0.5  # change the value of learning_rate in params
    """

    def __init__(self, json_path):
        logging.getLogger('execution').info('Loading parameters from {}...\n'.format(json_path))
        assert os.path.isfile(json_path), 'ERR: No json config file found at {}'.format(json_path)

        self.__update(json_path)

    def save(self, json_path):
        """Saves parameters to json file"""
        with open(json_path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    def __update(self, json_path):
        """Loads parameters from json file"""
        with open(json_path) as f:
            params = json.load(f)
            self.__dict__.update(params)

    @property
    def dict(self):
        """Gives dict-like access to Params instance by `params.dict['learning_rate']`"""
        return self.__dict__
