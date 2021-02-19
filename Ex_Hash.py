
class ExtindableHashing:
    
    ## X should be a list of list with 0th column to hash
    def __init__(self,X,hash_function,SSM):
        self.global_depth = 0
        self.directory = []
        self.hash_function = hash_function
        self.SSM = SSM
        self.insert(X,hash_function,SSM)
        self.is_directory_epanded = False
        self.directory_length = 1

        if len(self.directory) == 0:
            key = self.hash_function(0)
            self.directory.append(self.SSM.getRecordBucket())

    def insert(self,x):

        key = self.hash_function(x[0])

        bin_key = format(key, '016b')

        if self.global_depth == 0:
            final_key = 0
        else:
            final_key = int(bin_key(-self.global_depth:),2)
            
        bucket_index = self.directory[final_key]

        bucket = self.SSM.getBucket(bucket_index)

        ## bucket is free 
        if bucket.free_spaces > 0:
            bucket.insert(x)
        elif bucket.free_spaces == 0 and bucket.local_depth == self.global_depth:
            if not self.is_directory_epanded:
                self.directory_expansion()
                insert(self,x)
                self.is_directory_epanded = False
            else:
                ##overflow bucket code
                Overflow_bucket = self.SSM.getOverflowBucket()
                bucket.is_last = False
                bucket.link = Overflow_bucket
        
        elif bucket.free_spaces == 0 and bucket.local_depth < self.global_depth:
            self.split_bucket(final_key,bucket_index)

    def directory_expansion(self):

        current_length = 2**self.global_depth

        i = 0

        while i < current_length:

            top = self.directory.pop(0)

            if    

    def split_bucket(bucket_index):



            




