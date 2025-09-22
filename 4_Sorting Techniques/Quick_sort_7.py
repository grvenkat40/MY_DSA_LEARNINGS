class Quick_sorting():
    def quick(self,arr,low,high):
        if low<high:
            partition=self.Quick_sort(arr,low,high)
            self.quick(arr,low,partition)
            self.quick(arr,partition+1,high)

    def Quick_sort(self,arr,low,high):
        pivot=arr[low]
        i=low
        j=high
        while(i < j):
            while(arr[i] <= pivot and i<=high-1):
                i+=1
            while(arr[j] > pivot and j>=low+1):
                j-=1
            if i < j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[j],arr[low]=arr[low],arr[j]
        return j


obj=Quick_sorting()
arr=[9,5,1,7,2,4]
print("Before sort : ",arr)
low=0
high=len(arr)-1
obj.quick(arr,low,high)
print("After sort : ",arr)
