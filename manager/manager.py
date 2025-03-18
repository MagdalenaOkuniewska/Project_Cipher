from cipher.cipher import CipherFacade, CipherNotFoundError
from buffer.buffer import Buffer
from files_service.file_handler import FileHandler
from menu.menu_items import MainMenu


class Manager:
    """Manager class that acts as a Facade for the application.
    Coordinates interactions between Cipher, Buffer, FileHandler and Menu components."""

    def __init__(
        self,
        cipher_facade: CipherFacade,
        buffer: Buffer,
        file_handler: FileHandler,
        menu: MainMenu,
    ) -> None:

        self.cipher_facade = cipher_facade
        self.buffer = buffer
        self.file_handler = file_handler
        self.menu = menu

    def encrypt_text(self):
        """Handle encryption and stores in a buffer."""

        print("\n=== Encrypt text ===")

        text = input("Enter text to encrypt: ")
        cipher_type = input("Enter the cipher type: ")

        try:
            cipher = self.cipher_facade.check_cipher_type(cipher_type)
            encrypted_text = cipher.encrypt(text)
            self.buffer.add(
                content=encrypted_text, rot_type=cipher_type, status="encrypted"
            )

            print(f"Text encrypted successfully: {encrypted_text}")
            print("Added to buffer with status 'encrypted'")

        except CipherNotFoundError as e:
            print(f"Cipher error: {str(e)}")
        except Exception as e:
            print(f"Error during encryption: {str(e)}")

    def decrypt_text(self):
        """Handle decryption and stores in a buffer."""

        print("\n=== Decrypt text ===")

        text = input("Enter text to decrypt: ")
        cipher_type = input("Enter the cipher type: ")

        try:
            cipher = self.cipher_facade.check_cipher_type(cipher_type)
            decrypted_text = cipher.decrypt(text)
            self.buffer.add(
                content=decrypted_text, rot_type=cipher_type, status="decrypted"
            )

            print(f"Text decrypted successfully: {decrypted_text}")
            print("Added to buffer with status 'decrypted'")

        except CipherNotFoundError as e:
            print(f"Cipher error: {str(e)}")
        except Exception as e:
            print(f"Error during decryption: {str(e)}")

    # def display_buffer(self):
    #     pass
    #
    # def clear_buffer(self):
    #     pass
    #
    # def save_to_file(self):
    #     pass
    #
    # def load_from_file(self):
    #     pass
    #
    # def exit_program(self):
    #     pass
    #
    # def menu_choice(self):
    #     pass
