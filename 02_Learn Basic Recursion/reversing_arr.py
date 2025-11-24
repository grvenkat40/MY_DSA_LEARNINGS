class reverse_arr:
    def reversing(self,i,j,arr):
    # Recursion method
        if i>j:
            return
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
            self.reversing(i,j,arr)
        return arr
    # Normal method
        # i=0
        # j=len(arr)-1
        # while i<j:
        #     arr[i],arr[j]=arr[j],arr[i]
        #     i+=1
        #     j-=1
        # return arr

arr=[83,6,3,2,1,4]
print("Before Reversing :",arr)
obj=reverse_arr()
result=obj.reversing(0,len(arr)-1,arr)
for i in result:
    print(i,end=' ')