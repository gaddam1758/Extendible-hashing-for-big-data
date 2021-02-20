
from DirectoryEntry import DirectoryEntry 
import numpy as np

class ExtendibleHashing:
    
    ## X should be a list of list with 0th column to hash
    def __init__(self,X,hash_function,SSM, directory_max_memory_size):
        self.global_depth = 0
        self.directory = []
        self.hash_function = hash_function
        self.SSM = SSM
        self.is_directory_epanded = False
        self.directory_length = 1
        self.directory_overflow = None
        self.directory_max_memory_size  = directory_max_memory_size

        if len(self.directory) == 0:
            key = self.hash_function(0)
            entry = DirectoryEntry(key, self.SSM.getRecordBucket() )
            self.directory.append(entry)
        
        for x in X:
            self.insert(x)

    def insert(self,x):
        
        
        key = self.hash_function(x[0])

        bin_key = format(key, '016b')

        if self.global_depth == 0:
            final_key = 0
        else:
            final_key = int(bin_key[:self.global_depth],2)
            
        #print(final_key)
        ##need to write final keey greater than 1024
        
        bucket_index = self.get_bucket_index(final_key)

        bucket = self.SSM.getBucket(bucket_index)

        ## bucket is free 
        if bucket.free_spaces > 0:
            bucket.insert(x)
        elif bucket.free_spaces == 0 and bucket.local_depth == self.global_depth:
            if not self.is_directory_epanded:
                self.directory_expansion()
                self.is_directory_epanded = True
                self.global_depth+=1
                self.insert(x)
                self.is_directory_epanded = False
            else:
                ##overflow bucket code
                self.insert_bucket_overflow(bucket_index,x)
        
        elif bucket.free_spaces == 0 and bucket.local_depth < self.global_depth:
            self.split_bucket(final_key,bucket_index)
            self.insert(x)


    
    def get_bucket_index(self,key):
        if key<self.directory_max_memory_size:
            return self.directory[key].bucket_index
        else:
            cur_dir = self.directory_overflow
            
            while cur_dir.is_last is not True:
                for entry in cur_dir.spaces:
                    if entry.hash == key:
                        return entry.bucket_index
                cur_dir = cur_dir.overflow_link
            
            for entry in cur_dir.spaces:
                if entry is not None and entry.hash == key:
                    return entry.bucket_index
        
        
    def insert_bucket_overflow(self,bucket_index,x):
        bucket = self.SSM.getBucket(bucket_index)
        
        while bucket.is_last is not True:
            bucket = bucket.overflow_link
        
        if bucket.free_spaces>0:
            bucket.insert(x)
        else:
            n_bucket_idx = self.SSM.getRecordBucket()
            n_bucket = self.SSM.getBucket(n_bucket_idx)
            n_bucket.insert(x)
            bucket.overflow_link = n_bucket
            bucket.is_last = False
            
            
        
        
    def directory_expansion(self):

        current_length = 2**self.global_depth

        i = 0

        while i < current_length:

            top = self.directory.pop(0)

            self.directory_length+=1

            if self.directory_length > self.directory_max_memory_size:
                if self.directory_overflow is None:
                    self.directory_overflow = self.SSM.getBucket(self.SSM.getDirectoryBucket())
                
                temp = self.insert_directory_overflow(self.directory_overflow, top)
                self.directory.append(temp)
            else:
                n_d_entry = DirectoryEntry((top.hash<<1)+1,top.bucket_index)
                top.hash = top.hash<<1
                self.directory.append(top)
                
                self.directory.append(n_d_entry)
            i+=1

                
    def insert_directory_overflow(self, cur_dir, directory_item):
        
        
        a = cur_dir.spaces[0]
        b = cur_dir.spaces[1]
        
        n_cur_dir = cur_dir
        if cur_dir.is_last is not True:
            temp = self.insert_directory_overflow(cur_dir.overflow_link,directory_item)
        
        elif cur_dir.free_spaces == 0:
            new_bucket = self.SSM.getDirectoryBucket()
            cur_dir.is_last = False
            cur_dir.overflow_link = self.SSM.getBucket(new_bucket)
            temp = self.insert_directory_overflow(cur_dir.overflow_link,directory_item)
        
        else:
            n_d_entry = DirectoryEntry((directory_item.hash<<1)+1,directory_item.bucket_index)
            directory_item.hash = directory_item.hash<<1
            cur_dir.insert(directory_item)
            top = cur_dir.pop()
            cur_dir.insert(n_d_entry)
            c = cur_dir.spaces[0]
            d = cur_dir.spaces[1]
            
            return top
        
        c = cur_dir.spaces[0]
        d = cur_dir.spaces[1]
        top = n_cur_dir.pop()
        n_cur_dir.insert(temp)
        return top
    
    
            
            
            
    def getRecords(self,bucket_index):
        ls = []
        b = self.SSM.getBucket(bucket_index)

        while b.is_last is not True:
            ls += b.getRecords()
            b = b.overflow_link
        
        ls+= b.getRecords()
        return ls

    def getEntries(self, bucket_index):

        ls = []
        for i, entry in enumerate(self.directory):
            
            if entry.bucket_index == bucket_index:
                ls.append(entry)
        cur_dir = self.directory_overflow
        
        if cur_dir is not None:
            while cur_dir.is_last is not True:
                for entry in cur_dir.spaces:
                    if entry.bucket_index == bucket_index:
                        ls.append(entry)
            
                cur_dir = cur_dir.overflow_link
            
            for entry in cur_dir.spaces:
                
                    if entry is not None and entry.bucket_index == bucket_index:
                        ls.append(entry)
        
        return ls


    def split_bucket(self,key,bucket_index):

        bucket = self.SSM.getBucket(bucket_index)
        new_bucket_idx = self.SSM.getRecordBucket()
        new_bucket = self.SSM.getBucket(new_bucket_idx)

        ##collecting records to hash
        list_to_hash = self.getRecords(bucket_index)


        entries_pointing_to_this_bucket = self.getEntries(bucket_index)
        bucket.clean()
        bucket.local_depth+=1
        new_bucket.local_depth+=1
        
        l = len(entries_pointing_to_this_bucket)
        
        
        for i in range(int(l/2)):
            entries_pointing_to_this_bucket[i].bucket_index = bucket_index
        
        for i in range(int(l/2), l):
            entries_pointing_to_this_bucket[i].bucket_index = new_bucket_idx
        
        for item in list_to_hash:
            self.insert(item)
    
    def visualize(self):
        print("directory lenght is ", 2**self.global_depth)
        print("global depth is ", self.global_depth)
         
        print('-------------------------------------------')
        print('-------------------------------------------')
        for entry in self.directory:
            print('key is ', entry.hash)
            print('bucket index in SSM is ', entry.bucket_index)
            
            bucket = self.SSM.getBucket(entry.bucket_index)
            bucket.print_bucket()
        
        cur_dir = self.directory_overflow
        
        if cur_dir is not None:
            while cur_dir.is_last is not True:
                for entry in cur_dir.spaces:
                    print('key is ', entry.hash)
                    print('bucket index in SSM is ', entry.bucket_index)
                    bucket = self.SSM.getBucket(entry.bucket_index)
                    bucket.print_bucket()
                cur_dir = cur_dir.overflow_link
            
            for entry in cur_dir.spaces:
                
                    if entry is not None:
                      bucket = self.SSM.getBucket(entry.bucket_index)
                      bucket.print_bucket()
        print("directory lenght is ", 2**self.global_depth)
        print("global depth is ", self.global_depth)
         
        print("total no of records buckets used is ", self.SSM.getRecordBucket()-1)
        print("total no of directory buckets used is ", self.SSM.size-self.SSM.getDirectoryBucket()-1)
        
        
        print('-------------------------------------------')
        print('-------------------------------------------')
        


            




