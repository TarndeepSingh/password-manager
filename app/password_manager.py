from app.exceptions import EmptyFieldError, CredentialNotFoundError
from app.storage import StorageHandler


class PasswordManager:
    """
    Core business logic for managing credentials.
    """

    def __init__(self, storage: StorageHandler):
        self.storage = storage

    def add_credential(self, website: str, email: str, password: str) -> None:
        """
        Adds or updates credentials for a website.
        """
        if not website or not email or not password:
            raise EmptyFieldError("Website, email, and password are required.")

        data = self.storage.load_data()
        data[website] = {
            "email": email,
            "password": password
        }
        self.storage.save_data(data)

    def find_credential(self, website: str) -> dict:
        """
        Retrieves stored credentials for a website.
        """
        data = self.storage.load_data()
        if website not in data:
            raise CredentialNotFoundError("No credentials found for this website.")
        return data[website]
