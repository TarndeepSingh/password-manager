from app.password_manager import PasswordManager
from app.storage import StorageHandler
import os


def test_add_and_find_credential():
    test_file = "data/test_data.json"
    storage = StorageHandler(test_file)
    manager = PasswordManager(storage)

    manager.add_credential("github", "test@mail.com", "12345")
    credential = manager.find_credential("github")

    assert credential["email"] == "test@mail.com"

    os.remove(test_file)
