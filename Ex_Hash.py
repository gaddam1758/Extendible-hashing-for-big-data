
import DirectoryEntry 
import numpy as np

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
        self.directory_overflow = None

        if len(self.directory) == 0:
            key = self.hash_function(0)
            entry = DirectoryEntry(key, self.SSM.getRecordBucket() )
            self.directory.append(entry)

    def insert(self,x):

        key = self.hash_function(x[0])

        bin_key = format(key, '016b')

        if self.global_depth == 0:
            final_key = 0
        else:
            final_key = int(bin_key(-self.global_depth:),2)
            
        bucket_index = self.directory[final_key].bucket_index

        bucket = self.SSM.getBucket(bucket_index)

        ## bucket is free 
        if bucket.free_spaces > 0:
            bucket.insert(x)
        elif bucket.free_spaces == 0 and bucket.local_depth == self.global_depth:
            if not self.is_directory_epanded:
                self.directory_expansion()
                self.global_depth+=1
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

            self.directory_length+=1

            if self.directory_length > 1024:
                if self.directory_overflow is None:
                    self.directory_overflow = self.SSM.getDirectoryBucket()
                
                self.insert_directory_overflow(self.directory_overflow, top)

                
    def insert_directory_overflow(self, cur_dir, directory_item):

        if cur_dir.is_last is not True:
            self.insert_directory_overflow(cur_dir.overflow_link,directory_item)
        
        else:
            cur_dir.insert(top)
            cur_dir.insert(top)

        


    def getRecords(self,bucket_index):

        ls = []
        b = self.SSM.getBucket(bucket_index)

        while b.is_last is not true:
            ls += b.getRecords()
            b = b.link
        
        ls+= b.getRecords()

    def getEntries(self, bucket_index):

        ls = []
        for i, entry in enumerate(self.directory):
            
            if entry == bucket_index:
                ls.append(i)
        cur_dir = self.directory_overflow
        
        if cur_dir is not None:
            while cur_dir.is_last is not true:

        
        


    def split_bucket(self,key,bucket_index):

        bucket = self.SSM.getBucket(bucket_index)
        new_bucket_idx = self.SSM.getRecordBucket()
        new_bucket = self.SSM.getBucket(new_bucket_idx)

        ##collecting records to hash
        list_to_hash = self.getRecords(bucket_index)

        bucket.clean()

        entries_pointing_to_this_bucket = self.getEntries(bucket_index)



            




