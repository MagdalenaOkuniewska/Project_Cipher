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

        text: str = input("Enter text to encrypt: ")
        cipher_type: str = input("Enter the cipher type: ")

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

        text: str = input("Enter text to decrypt: ")
        cipher_type: str = input("Enter the cipher type: ")

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

    def display_buffer(self):
        """Display current buffer content"""

        print("\n=== Buffer content ===")
        self.buffer.display()

    def clear_buffer(self):
        """Clears current buffer content"""

        self.buffer.clear_all()
        print("Buffer content cleared.")

    def save_to_file(self):
        """Save current buffer content to a JSON file"""

        print("\n=== Save to JSON file ===")

        if not self.buffer.storage:
            print("Buffer is empty. Nothing to save.")
            return

        filename: str = input("Enter filename to save to: ")
        mode: str = input("Enter mode ('w' for write, 'a' for append): ")

        try:
            self.file_handler.save_to_file(self.buffer, filename, mode)
            print(f"Buffer content successfully saved to {filename} in {mode} mode.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self):
        """Load data from JSON file to a buffer"""

        print("\n=== Load from JSON file ===")

        filename: str = input("Enter filename to load from: ")

        try:
            self.file_handler.load_from_file(self.buffer, filename)
            print(f"Data successfully loaded from {filename}.")
        except Exception as e:
            print(f"An error occurred while loading from file: {e}")

    def exit_program(self):
        """Exit the application."""

        print("\nExiting application. Goodbye!")
        exit()

    def menu_choice(self):
        """Map the menu choice to the appropriate function."""

        self.menu.display_menu()

        choice = self.menu.get_choice()

        actions = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.display_buffer,
            4: self.clear_buffer,
            5: self.save_to_file,
            6: self.load_from_file,
            7: self.exit_program,
        }

        if choice in actions:
            return actions[choice]()
        else:
            print(f"Invalid choice: {choice}")
