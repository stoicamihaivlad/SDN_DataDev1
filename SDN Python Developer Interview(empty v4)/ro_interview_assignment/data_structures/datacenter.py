from dataclasses import dataclass
#from pydantic import validate_arguments


#@validate_arguments
@dataclass
class Datacenter:
    name: str
    cluster_list:list
    def __init__(self, name:str, cluster_list:list):
        """
        Constructor for Datacenter data structure.
        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.cluster_list = cluster_list
        

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.

        I have tested each case separately 
        """
        #I presumed that the parent Datecenter is stored in the name 

        for i in range(len(self.cluster_list)):
            if len(self.cluster_list[i]) > 7 :
                self.cluster_list.pop(i)
                continue
            if self.name[0:3] != self.cluster_list[i][0:3]:
                self.cluster_list.pop(i)
                continue
            if self.cluster_list[i][3] != '-':
                self.cluster_list.pop(i)
                continue
            if not self.cluster_list[i][4:].isnumeric():
                self.cluster_list.pop(i)
                continue
            
        print (self.cluster_list)
        pass

# A = Datacenter('PAR',['PAR-1','ABC-4567'])
# print(A.cluster_list)
# A.remove_invalid_clusters()

# B=Datacenter(5,(1,2))
# print(B)