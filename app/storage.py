import json
from pathlib import Path
from app.exceptions import StorageError


class StorageHandler:
    """
    Handles reading and writing credential data to JSON storage.
    """

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)

    def load_data(self) -> dict:
        """
        Loads credentials from JSON file.

        :return: Dictionary of stored credentials
        """
        if not self.filepath.exists():
            return {}

        try:
            with open(self.filepath, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise StorageError("Data file is corrupted.")
        except IOError as error:
            raise StorageError(f"File read error: {error}")

    def save_data(self, data: dict) -> None:
        """
        Saves credentials to JSON file.

        :param data: Dictionary containing credentials
        """
        try:
            self.filepath.parent.mkdir(exist_ok=True)
            with open(self.filepath, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            raise StorageError(f"File write error: {error}")
