import numpy as np


class Bucket:

    def __init__(self,bucket_size):
        self.spaces = np.empty(bucket_size,dtype='O') 
        self.overflow_link = None
        self.is_last = False
        self.free_spaces = bucket_size

