import pathlib
import yaml

class CameraConfig:
    def __init__(self, configuration_file: pathlib.Path):
        self.configuration_file = configuration_file
        self.config: dict = {}
        self.load_config()

    def load_config(self):
        with open(self.configuration_file, 'r') as file:
            self.config= yaml.safe_load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config_dict[key] = value
