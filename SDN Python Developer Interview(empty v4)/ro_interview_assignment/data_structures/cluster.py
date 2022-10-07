from dataclasses import dataclass
# from pydantic import validate_arguments


# @validate_arguments
@dataclass
class Cluster:
    name: str
    security_level: int
    network_list: list
    def __init__(self, name, network_list, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        self.name = name
        self.security_level = security_level
        self.network_list = network_list
        
        # def __setattr__(self,name,value):
        #     if name == 'name' and not isinstance(value, str):
        #         raise TypeError ('Cluster.name must be string')
        #     super().__setattr__(name,value)

