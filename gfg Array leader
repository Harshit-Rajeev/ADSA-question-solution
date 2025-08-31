class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders = []
        max_val = arr[-1]
        leaders.append(max_val)

        for i in range(n - 2, -1, -1):
            if arr[i] >= max_val:
                leaders.append(arr[i])
                max_val = arr[i]

        leaders.reverse()
        return leaders

