from cipher.cipher import CipherFacade, CipherNotFoundError
from buffer.buffer import Buffer
from files_service.file_handler import FileHandler
from menu.menu_items import MainMenu
from settings import DEBUG


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
        self.is_running = True

    @property
    def actions(self):
        return {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.display_buffer,
            4: self.clear_buffer,
            5: self.save_to_file,
            6: self.load_from_file,
            7: self.exit_program,
        }

    def encrypt_text(self):
        """Handle encryption and stores in a buffer."""
        self.__make_cipher_operation(operation_type="encrypt")

    def decrypt_text(self):
        """Handle decryption and stores in a buffer."""
        self.__make_cipher_operation(operation_type="decrypt")

    def __make_cipher_operation(self, operation_type: str):
        """Helper method to perform encryption or decryption."""

        print(f"\n=== {operation_type.title()} text ===")

        text: str = input(f"Enter text to {operation_type}: ")
        cipher_type: str = input("Enter the cipher type: ")

        try:
            cipher = self.cipher_facade.check_cipher_type(cipher_type)

            if operation_type == "decrypt":
                text = cipher.decrypt(text)
                status = "decrypted"
            elif operation_type == "encrypt":
                text = cipher.encrypt(text)
                status = "encrypted"
            else:
                print(f"Invalid operation type: {operation_type}")
                return

            self.buffer.add(content=text, rot_type=cipher_type, status=status)

            print(f"Text {operation_type}ed successfully: {text}")
            print(f"Added to buffer with status '{status}'")

        except CipherNotFoundError as e:
            print(f"Cipher error: {str(e)}")
        except Exception as e:
            if DEBUG:
                print(f"Error: {e}")
            print(f"Error during {operation_type} operation try again.")

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
        self.is_running = False

    def run(self):
        """Map the menu choice to the appropriate function."""

        while self.is_running:
            self.menu.display_menu()

            choice = self.menu.get_choice()

            if choice in self.actions:
                self.actions[choice]()
            else:
                print(f"Invalid choice: {choice}")
