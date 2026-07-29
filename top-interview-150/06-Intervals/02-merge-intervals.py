class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []
        if len(intervals) == 0:
            return []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > end :
                merged_intervals += [[start, end]]
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(intervals[i][1], end)
        end = max(intervals[-1][1], end)
        merged_intervals += [[start, end]]
        return merged_intervals
