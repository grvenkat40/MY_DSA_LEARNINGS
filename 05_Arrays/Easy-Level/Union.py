def Union(nums1,nums2):
    i=0
    j=0
    union=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i] < nums2[j]:
            if len(union)==0 or union[len(union)-1]!=nums1[i]:
                union.append(nums1[i])
            i+=1
        else:
            if len(union)==0 or union[len(union)-1]!=nums2[j]:
                union.append(nums2[j])
            j+=1
    while j<len(nums2):
        if union[len(union)-1]!=nums2[j]:
            union.append(nums2[j])
        j+=1
            
    while i<len(nums1):
        if union[len(union)-1]!=nums1[i]:
            union.append(nums1[i])
        i+=1
    print("After Union:\n",union)


nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]
print(nums1)
print(nums2)
Union(nums1,nums2)
