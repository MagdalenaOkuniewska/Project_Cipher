from dataclasses import dataclass


@dataclass
class Text:
    """Stores a single text element with encryption information"""

    content: str
    rot_type: str
    status: str

    def to_dict(self):
        return {
            "content": self.content,
            "rot_type": self.rot_type,
            "status": self.status,
        }
