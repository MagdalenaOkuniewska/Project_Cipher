import json
from buffer.buffer import Buffer


class FileHandler:
    """Handle file operations (save and load) for Buffer data in JSON format."""

    @staticmethod
    def buffer_to_dict(buffer: Buffer):
        """Convert buffer storage to a list of dictionaries for JSON format."""
        return [text.to_dict() for text in buffer.storage]

    @staticmethod
    def save_to_file(buffer: Buffer, filename: str):
        """Saving data from buffer to file."""

        data_to_save = FileHandler.buffer_to_dict(buffer)

        try:
            with open(filename, "a") as outfile:
                json.dump(data_to_save, outfile, indent=4)
                outfile.write("\n")
        except FileNotFoundError:
            pass

    @staticmethod
    def load_from_file(buffer: Buffer, filename: str):
        """Load data from file to the buffer."""
        pass
