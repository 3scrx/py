from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def put(self,key,val):
        if self.root:
            self.root.put(key,val)
        else:
            self.root = TreeNode(key,val)
        self.size +=1
    def get(self,key):
        if self.root:
            return self.root.get(key)
        else:
            return None
    def __setitem__(self,k,v):
        self.put(k,v)
    def __getitem__(self,key):
        return self.get(key)

    
    def hash_key(self,key):
        if self.root.get(key):
            return True
        else:
            return False
    
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def delete_key(self,key):
        if self.size > 1:
            nodeToRemove = self.get(key)
            nodeToRemove.delete_key(key)
            self.size-=1
        elif self.root.key == key:
            self.root = None
            self.size = self.size-1
        else:
            print "error ,bad key"
    
            


#test
bst=BinarySearchTree()
bst[70]=70
bst[31]=31
bst[93]=93
bst[94]=94
bst[14]=14
bst[23]=23
bst[73]=73

