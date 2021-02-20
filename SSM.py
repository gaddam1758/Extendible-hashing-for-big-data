import numpy as np
from Bucket import Bucket

class SimulatedSecondaryMemory:

    def __init__(self,size, record_bucket_size, directory_bucket_size):
        self.size = size
        self.Memory = np.empty(size,dtype=Bucket)
        self.start_index = 0
        self.end_index = size-1
        self.record_bucket_size = record_bucket_size
        self.directory_bucket_size = directory_bucket_size
    
    def getBucket(self,index):
        return self.Memory[index]
    
    def getSize(self):
        return self.size
    
    ##returns index
    def getRecordBucket(self):
        b = Bucket(self.record_bucket_size)
        self.Memory[self.start_index] = b
        self.start_index+=1
        return self.start_index-1
    
    def getDirectoryBucket(self):
        b = Bucket(self.directory_bucket_size)
        self.Memory[self.end_index] = b
        self.end_index-=1

        return self.end_index+1



    def getOverflowBucket(self):
        b  = Bucket(self.record_bucket_size)
        self.Memory[self.end_index] = b
        self.end_index-=1
    
