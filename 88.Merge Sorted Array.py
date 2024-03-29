##88.Merge Sorted Array  Similar with 977: Squares of Sorted Array & 986. Interval list insections
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums2[j]>=nums1[i]:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            else:
                nums1[k]=nums1[i]
                i-=1
                k-=1
        if j>=0:
            nums1[:k+1]=nums2[:j+1]      #left element is not include so +1 is needed 
