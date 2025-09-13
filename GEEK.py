class Solution:
    def binarysearch(self, arr, k):
   
        low = 0
        high = len(arr) - 1
        while low <= high:
            print(k)
            mid = (high - low) // 2
            if k > high:
               print("Element is too high")
               break
            # Check if x is present at mid
            if arr[mid] == k:
                return mid
    
            # If x is greater, ignore left half
            elif arr[mid] < k:
                low = mid + 1
    
            # If x is smaller, ignore right half
            else:
                high = mid - 1
           
        # If we reach here, then the element
        # was not present
        return -1
    
 
solution = Solution()
solution.binarysearch([1, 2, 5, 7, 8], )