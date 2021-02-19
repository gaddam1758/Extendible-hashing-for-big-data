import numpy as np


class Bucket:

    def __init__(self,bucket_size):
        self.spaces = np.empty(bucket_size,dtype='O') 
        self.overflow_link = None
        self.is_last = True
        self.free_spaces = bucket_size
        self.local_depth = 0
        self.size = bucket_size
        self.idx = 0
    
    def insert(self,record):
        self.spaces[idx] = record

        self.free_spaces-=1
        self.idx+=1
    
    def pop(self):
        self.free_spaces+=1
        self.idx-=1

        temp  = self.spaces[0]
        np.delete(self.spaces,0)

        return temp
    
    def clean(self):
        self.is_last = True
        self.free_spaces = self.size
        self.overflow_link = None
    
    def getRecords(self):

        ls = []
        for i in range(self.size - self.free_spaces):
            ls.append(spaces[i])
        
        


