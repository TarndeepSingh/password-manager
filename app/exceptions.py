class PasswordManagerError(Exception):
    """Base class for all MyPass related exceptions."""
    pass


class EmptyFieldError(PasswordManagerError):
    """Raised when input fields are left empty."""
    pass


class CredentialNotFoundError(PasswordManagerError):
    """Raised when a requested website is not found."""
    pass


class StorageError(PasswordManagerError):
    """Raised for file read/write or corruption issues."""
    pass
