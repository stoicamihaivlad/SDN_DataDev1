from dataclasses import dataclass
from datetime import datetime
# from pydantic import validate_arguments


#@validate_arguments
@dataclass
class Entry:
    address: str
    available: bool
    last_used: str
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

    def __lt__(self,obj):
        return ((self.address) < (self.address))

    def __gt__(self,obj):
        return ((self.address) > (self.address))

    def __le__(self,obj):
        return ((self.address) <= (self.address))

    def __ge__(self,obj):
        return ((self.address) >= (self.address))

    def __eq__(self,obj):
        return ((self.address) == (self.address))

