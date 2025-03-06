from abc import ABC, abstractmethod
from typing import List, Dict, Any


class CipherNotFoundError(Exception):
    """Exception raised when the specified cipher type is not found."""

    pass


class Cipher(ABC):
    """Abstract base class for ciphers."""

    @abstractmethod
    def encrypt(self, text: str) -> str:
        """Encrypts the provided text."""
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        """Decrypts the provided text."""
        pass

    @abstractmethod
    def perform_shift(self, text: str, shift: int) -> str:
        """Calculating the shift to encrypt and decrypt the text."""
        pass


class CipherROT13(Cipher):
    """ROT13 cipher implementation."""

    def encrypt(self, text: str) -> str:
        return self.perform_shift(text, shift=13)

    def decrypt(self, text: str) -> str:
        return self.perform_shift(text, shift=13)

    def perform_shift(self, text: str, shift: int) -> str:
        """Calculate shift for text according to ROT13 cipher.
        Works on only alphabetic characters."""

        rot13_txt = ""

        for char in text:
            if char.isalpha():
                ascii_offset = ord("a") if char.islower() else ord("A")
                alphabet_position = (ord(char) - ascii_offset + shift) % 26
                shifted_char = chr(alphabet_position + ascii_offset)
                rot13_txt += shifted_char
            else:
                rot13_txt += char
        return rot13_txt


class CipherROT47(Cipher):
    """ROT47 cipher implementation."""

    def encrypt(self, text: str) -> str:
        return self.perform_shift(text, shift=47)

    def decrypt(self, text: str) -> str:
        return self.perform_shift(text, shift=47)

    def perform_shift(self, text: str, shift: int) -> str:
        """Calculate shift for text according to ROT47 cipher.
        Works on ASCII characters from '!' (33) to '~' (126)."""

        rot47_txt = ""

        for char in text:
            if 33 <= ord(char) <= 126:
                char_position = (ord(char) - 33 + shift) % 94
                shifted_char = chr(char_position + 33)
                rot47_txt += shifted_char
            else:
                rot47_txt += char
        return rot47_txt


class CipherFacade:
    """Facade for encryption operations."""

    def __init__(self):
        self.ciphers: dict[str, Cipher] = {
            "rot13": CipherROT13(),
            "rot47": CipherROT47(),
        }

    def check_cipher_type(self, cipher_type: str) -> Cipher:
        """Validates the cipher type and returns the corresponding cipher."""

        cipher_type = cipher_type.lower()
        available_ciphers = ", ".join(self.ciphers.keys())

        try:
            return self.ciphers[cipher_type]
        except KeyError:
            raise CipherNotFoundError(
                f"Cipher type {cipher_type} not found. Available ciphers: {available_ciphers}."
            )

    def encrypt(self, text: str, cipher_type: str) -> str:
        """Encrypts the text using the provided cipher type."""

        return self.check_cipher_type(cipher_type).encrypt(text)

    def decrypt(self, text: str, cipher_type: str) -> str:
        """Decrypts the text using the provided cipher type."""

        return self.check_cipher_type(cipher_type).decrypt(text)
