import secrets
import string


class SecurityUtils:
    """Utility class for security-related operations."""

    @staticmethod
    def generate_password(length: int = 16) -> str:
        """
        Generates a cryptographically secure random password.

        :param length: Length of the password
        :return: Secure random password string
        """
        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )
        return ''.join(secrets.choice(characters) for _ in range(length))
