class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_pairs = sorted(boxTypes, key = lambda x : x[1])
        
        ans = 0
        while truckSize and sorted_pairs:
            num_boxes, num_units = sorted_pairs.pop()
            if num_boxes < truckSize:
                truckSize -= num_boxes
                ans += num_boxes * num_units
            else:
                ans += truckSize * num_units
                break
            
        return ans