class Solution:
    def inversionCount(self, arr):
        return self.merge_sort(arr, 0, len(arr) - 1)
    
    def merge_sort(self, arr, left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            
            count += self.merge_sort(arr, left, mid)
            count += self.merge_sort(arr, mid + 1, right)
            count += self.merge(arr, left, mid, right)
            
        return count
    
    def merge(self, arr, left, mid, right):
        temp = []
        i, j = left, mid + 1
        count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                count += (mid - i + 1)   # 🔥 inversion logic
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
            
        while j <= right:
            temp.append(arr[j])
            j += 1
        
        for k in range(len(temp)):
            arr[left + k] = temp[k]
        
        return count
