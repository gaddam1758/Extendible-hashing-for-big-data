import numpy as np
import Bucket

class SSM:

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
        self.Memory[start_index] = b
        start_index+=1
        return start_index-1
    
    def getDirectoryBucket(self):
        b = Bucket(self.directory_bucket_size)
        self.Memory[end_index] = b
        end_index-=1

        return end_index+1



    def getOverflowBucket(self):
        b  = bucket(self.record_bucket_size)
        self.Memory[end_index] = b
        end_index-=1
    

