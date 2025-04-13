import json

class DataStorage:
    def __init__(self, filename="data.json"):
        """
        Initialize the data storage with a filename.
        :param filename: str
        """
        self.filename = filename

    def save_data(self, data):
        """
        Save data to a JSON file.
        :param data: dict
        """
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        """
        Load data from a JSON file.
        :return: dict
        """
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file doesn't exist
        except json.JSONDecodeError:
            return {}  # Return an empty dictionary if the file is corrupted