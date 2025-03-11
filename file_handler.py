import json
from buffer.buffer import Buffer


class FileHandler:
    """Handle file operations (save and load) for Buffer data in JSON format."""

    @staticmethod
    def buffer_to_dict(buffer: Buffer):
        """Convert buffer storage to a list of dictionaries for JSON format."""
        return [text.to_dict() for text in buffer.storage]

    @staticmethod
    def get_filename(filename: str | None) -> str:
        """Get filename from user input if not provided, and ensure it has a .json extension."""

        if filename is None:
            filename = input("Enter a filename: ")

        if not filename.lower().endswith(".json"):
            filename += ".json"

        return filename

    @staticmethod
    def save_to_file(buffer: Buffer, filename: str, mode: str = "a") -> None:
        """Saving data from buffer to file."""

        data_to_save = FileHandler.buffer_to_dict(buffer)
        filename = FileHandler.get_filename(filename)

        if mode not in ["w", "a"]:
            print("Invalid mode. Setting up to default 'append' mode.")
            mode = "a"

        try:
            with open(filename, mode) as outfile:
                json.dump(data_to_save, outfile, indent=4)
                outfile.write("\n")
            print(f"Data successfully saved to {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    @staticmethod
    def load_from_file(buffer: Buffer, filename: str):
        """Load data from file to the buffer."""
        pass
