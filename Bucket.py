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
    
    def insert(record):
        spaces[idx] = record

        free_spaces-=1
        idx+=1
        


