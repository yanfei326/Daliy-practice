#0、两个数合并后比较大小
class Solution:
    def merge(self,nums1:list[int],m:int,nums2:list[int],n:int)->None:
        i=m-1
        j=n-1
        p=m+n-1
        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[p]=nums1[i]
                i-=1
            else:
                nums1[p]=nums2[j]
               j-=1
            p-=1
                