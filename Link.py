from enum import Enum

class Status(Enum):
    GOOD = 0
    BAD = -100
    MODIFIED = 100
    UNKNOWN = 200
    
class Link:
    __link = ""
    __status = Status.UNKNOWN
    def __init__(txt : str = "") -> str:
        __link = txt
        __status = Status.UNKOWN
    


