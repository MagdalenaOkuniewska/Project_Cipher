from dataclasses import asdict
import json
from buffer.buffer import Buffer


class FileHandler:
    """Handle file operations (save and load) for Buffer data in JSON format."""

    @staticmethod
    def buffer_to_dict(buffer: Buffer) -> list[dict[str, str]]:
        """Convert buffer storage to a list of dictionaries for JSON format."""

        list_of_dicts = [asdict(text) for text in buffer.storage]
        return list_of_dicts

    @staticmethod
    def get_filename(filename: str | None) -> str:
        """Get filename from user input and ensure it has a .json extension."""

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
            with open(filename, mode, encoding="utf-8") as outfile:
                json.dump(data_to_save, outfile, indent=4)
                outfile.write("\n")
            print(f"Data successfully saved to {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    @staticmethod
    def load_from_file(buffer: Buffer, filename: str) -> None:
        """Load data from file to the buffer."""

        filename = FileHandler.get_filename(filename)

        try:
            with open(filename, mode="r", encoding="utf-8") as infile:
                data_to_load = json.load(infile)

                buffer.add_bulk(data_to_load)

        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.decoder.JSONDecodeError:
            print(f"File {filename} is not valid JSON.")
