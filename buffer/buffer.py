from typing import List
from cls_txt import Text


class Buffer:
    """Buffer holding a list of Text objects."""

    def __init__(self):
        self.storage: List[Text] = []

    def __str__(self):
        if not self.storage:
            return "Buffer empty"

        buffer_content = "\n".join(str(text) for text in self.storage)
        return f"Buffer content:\n{buffer_content}"

    def add_encrypted(self, content: str, rot_type: str) -> None:
        """Add an encrypted text to the buffer."""

        text = Text(content=content, rot_type=rot_type, status="encrypted")
        self.storage.append(text)

    def add_decrypted(self, content: str, rot_type: str) -> None:
        """Add a decrypted text to the buffer."""

        text = Text(content=content, rot_type=rot_type, status="decrypted")
        self.storage.append(text)

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


# buffer = Buffer()
# buffer.add_encrypted(rot_type='rot13', content='sdf5f2')
# buffer.add_decrypted(rot_type='rot47', content='Testowa zawartość II')
# buffer.display()
# buffer.clear_all()
# buffer.display()
