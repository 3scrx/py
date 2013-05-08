class TreeNode:
    def __init__(self,key,val,parent=None,left=None,right=None):
        self.key=key
        self.payload=val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def put (self,key,val):
        if key < self.key:
            if self.leftChild:
                self.leftChild.put(key,val)
            else:
                self.leftChild = TreeNode(key,val,self)
        else:
            if self.rightChild:
                self.rightChild.put(key,val)
            else:
                self.rightChild = TreeNode(key,val,self)
    def get(self,key):
        if key == self.key:
            return self.payload
        elif key < self.key:
            if self.leftChild:
                return self.leftChild.get(key)
            else:
                return None
        elif key > self.key:
            if self.rightChild:
                return self.rightChild.get(key)
            else:
                return None
        else:
            print "error:tihs line should never be executed"
    def delete_key(self,key):
        if self.key == key:
            if not(self.leftChild or self.rightChild):
                if self == self.parent.leftChild:
                    self.parent.leftChild = None
                else:
                    self.parent.rightChild = None
            
   
    def __setitem__(self,k,v):
        self.put(k,v)
    def __getitem__(self,key):
        return self.get(key)
