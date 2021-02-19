
class ExtindableHashing:
    
    def __init__(self,X,y,hash_function,SSM):
        self.global_depth = 0
        self.directory = {}
        self.insert(X,y,hash_function,SSM)

    def insert(self,X,y,hash_function,SSM):

        if len(self.directory) == 0:
            key = hash_function(0)
            directory[key] = SSM.getBucketFromStart()
        
        
        