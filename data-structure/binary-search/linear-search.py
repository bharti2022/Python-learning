class search:
    listt=[]
    def __init__(self, listt):
        self.listt = listt
    
    def find(self,find_value):
        for i in range(len(self.listt)):
            if self.listt[i] == find_value:
                return True
        return False    
            
            
listt = [1,2,3,4,5]

obj = search(listt)

print(obj.find(2))        
        