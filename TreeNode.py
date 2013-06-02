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
            print "deger bulundu : ",self.payload
            return self
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
        if not (self.leftChild or self.rightChild):
            print "cocuksuz dugum"
            if self == self.parent.leftChild:
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif (self.leftChild or self.rightChild) and \
             (not (self.leftChild and self.rightChild)):
            if self.leftChild:
                if self == self.patern.leftChild:
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.leftChild = self.rightChild
            else:
                if self == self.patern.leftChild:
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.leftChild = self.rightChild
        else:
            print "iki cocuklu dugum"
            succ = self.findSuccessor()
            succ.spliceOut()
            if self == self.parent.leftChild:
                self.parent.leftChild = succ
            else:
                self.parent.rightChild = succ
        succ.leftChild = self.leftChild
        succ.rigthChild = self.rightChild
        
                    
                    
                        
            
   
    def __setitem__(self,k,v):
        self.put(k,v)
    def __getitem__(self,key):
        return self.get(key)

    def findSuccessor(self):
        succ = None
        if self.rightChild:
            succ = self.rightChild.findMin()
        else:
            if self.parent.leftChild == self:
                succ=self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
        return succ
    def findMin(self):
        n= self
        while n.leftChild:
            n = n.leftChild
        print "found min,key = ",n.key
        return n
    def spliceOut(self):
        if (not self.leftChild and not self.rightChild):
            if self == self.parent.leftChild:
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif (self.leftChild or self.rightChild):
            if self.leftChild:
                if self ==self.parent.leftChild:
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.leftChild = self.leftChild
            else:
                if self==self.parent.leftChild:
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                
