def find_ones(mat):
    index=0
    max_cnt=-1
    for row in range(len(mat)):
        cnt=0                               #TC : O(row*col)
        for col in range(len(mat)):
            cnt+=mat[row][col]
        if cnt>max_cnt:
            max_cnt=cnt
            index=row
    return index
mat = [ [1, 0, 0], [0, 1, 1], [0, 0, 0] ]
print(find_ones(mat))
print()

class BS_find_one():
    def lower_bound(self,nums,x):
        i=0
        j=len(nums)
        # ans=0
        while i<=j:
            mid=(i+j)//2
            if nums[mid]>=x:
                j=mid-1
                # ans=mid
            else:
                i=mid+1
        return i


    def find_ones_BS(self,mat):
        n=len(mat)  #row
        m=len(mat[0])   #col
        index=0
        max_cnt=-1
        for row in range(n):
            pos = self.lower_bound(mat[row], 1)   # ✅ only 2 args
            cnt = m - pos                             #TC : O(row*col)
            if cnt>max_cnt:
                max_cnt=cnt
                index=row
        return index

mat = [ [1, 0, 0], [0, 1, 1], [0, 0, 0] ]
obj=BS_find_one()
print(obj.find_ones_BS(mat))