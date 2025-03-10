from dataclasses import dataclass


@dataclass
class Text:
    """Stores a single text element with encryption information"""

    content: str
    rot_type: str
    status: str
