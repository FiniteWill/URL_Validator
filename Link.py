from enum import Enum

class Status(Enum):
    GOOD = "Good"
    BAD = "Bad"
    MODIFIED = "Mod"
    UNKNOWN = "?"
    
class Link:
    
    link = ""
    status = Status(Status.UNKNOWN)
    
    def __init__(self, txt : str) -> str:
        self.link = txt
        self.status = Status(Status.UNKNOWN)
