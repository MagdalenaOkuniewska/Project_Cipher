from typing import List
from text import Text


class Buffer:
    """Buffer holding a list of Text objects."""

    def __init__(self):
        self.storage: List[Text] = []

    def __str__(self):
        if not self.storage:
            return "Buffer empty"

        buffer_content = "\n".join(str(text) for text in self.storage)
        return f"Buffer content:\n{buffer_content}"

    def add(self, content: str, rot_type: str, status: str) -> None:
        """Add the text to the buffer with specified status."""

        text = Text(content=content, rot_type=rot_type, status=status)
        self.storage.append(text)

    def add_bulk(self, data: list[dict[str, str]]) -> None:
        """Add multiple texts to the buffer from a list of dictionaries."""

        for item in data:
            data = Text(**item)
            self.storage.append(data)

    def clear_all(self):
        """Clear the buffer."""

        self.storage.clear()

    def display(self):
        """Display the content of the buffer."""

        if not self.storage:
            print("Buffer empty")
            return

        print("Buffer content:")
        for i, item in enumerate(self.storage, 1):
            print(f"{i}. ROT:[{item.rot_type}], STATUS[{item.status}]: {item.content}")
