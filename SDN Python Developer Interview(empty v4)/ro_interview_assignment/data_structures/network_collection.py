from dataclasses import dataclass
from ipaddress import ip_address,IPv4Network
# from pydantic import validate_arguments


# @validate_arguments
@dataclass
class NetworkCollection:
    ipv4_network:str
    raw_entry_list:list
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = IPv4Network(ipv4_network)
        self.raw_entry_list = raw_entry_list
        # def __setattr__(self,name,value):
        #     if name == 'name' and not isinstance(value, ipaddress.IPv4Network):
        #         raise TypeError ("value must be an instance of ipaddress.IPv4Address)
        #     super().__setattr__(name,value)

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        net = IPv4Network(self.ipv4_network)
        for i in range(len(self.raw_entry_list)):
            try:
                ip_address(self.raw_entry_list[i]["address"])
            except:
                self.raw_entry_list.pop(i)
            if self.raw_entry_list[i]["address"] not in net:
                self.raw_entry_list.pop(i)



    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
