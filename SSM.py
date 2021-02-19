import numpy as np
import Bucket

class SSM:

    def __init__(self,size):
        self.size = size
        self.Memory = np.empty(size,dtype=Bucket)
        self.start_index = 0
        self.end_index = size-1
    
    def getBucket(self,index):
        return self.Memory[index]
    
    def getSize(self):
        return self.size
    
    ##returns index
    def getBucketFromStart(self):
        
        start_index+=1
        return start_index-1
    
    def getBucketFromEnd(self):
        end_index-=1

        return end_index+1