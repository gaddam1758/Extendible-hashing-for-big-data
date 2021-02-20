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
        self.spaces[self.idx] = record

        self.free_spaces-=1
        self.idx+=1
    
    def pop(self):
        self.free_spaces+=1
        self.idx-=1

        temp  = self.spaces[0]
        self.spaces = np.delete(self.spaces,0)
        self.spaces = np.append(self.spaces,None)

        return temp
    
    def clean(self):
        self.is_last = True
        self.free_spaces = self.size
        self.overflow_link = None
        self.idx = 0
    
    def print_bucket(self):
        for i in self.spaces:
            print(i)
        if self.is_last is not True:
            print('link ->')
            self.overflow_link.print_bucket()
        else:
            print('----------------------------------')
    def getRecords(self):

        ls = []
        for i in range(self.size - self.free_spaces):
            ls.append(self.spaces[i])
        return ls
        


