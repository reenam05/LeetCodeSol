class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        while i != len(nums1):
            if nums2 == []:
                i+=1
            elif nums1[i] <= nums2[j] and i <= m - 1:
                i+=1
            elif nums1[i] <= nums2[j] and i > m - 1:
                nums1[i] = nums2[j]
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                if nums1[i] <= nums2[j+1]:
                    tmp = nums1[i]
                    nums1[i] = nums2[j]
                    nums2[j] = tmp
                    i+=1
                else:
                    nums1[m] = nums2[j]
                    j+=1
                    m+=1 