from dataclasses import dataclass


@dataclass
class Text:
    """Stores a single text element with encryption information"""

    content: str
    rot_type: str
    status: str

    def to_dict(self) -> dict:
        """Converts the Text object to a dictionary"""
        return {
            "content": self.content,
            "rot_type": self.rot_type,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Text":
        """Converts the dictionary to an instance of Text"""
        return Text(
            content=data["content"], rot_type=data["rot_type"], status=data["status"]
        )
