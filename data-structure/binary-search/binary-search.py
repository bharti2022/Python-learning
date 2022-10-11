class binary_search:
    def __init__(self,listt):
        self.listt = listt
        
    def binary_search(self,start,end,find):
        if start > end :
            return False
        else :
            mid = (start + end) // 2
            if find == self.listt[mid]:
                return True
            elif find > listt[mid]:
               return self.binary_search(mid+1,len(listt)-1,find)
            elif find < listt[mid]:
               return self.binary_search(0,mid-1,find)
        
            return False


listt = [1,2,3,4,5,6]

obj1 = binary_search(listt)

print(obj1.binary_search(0,len(listt),1))            
                
                   
                