class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxarea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, d = stack.pop()
                w = i - d
                area = h * w
                maxarea = max(maxarea, area)
                start = d
            stack.append([height, start])

        while stack:
            h, d = stack.pop()
            w = n - d
            area = w * h
            maxarea = max(maxarea, area)

        return maxarea
        