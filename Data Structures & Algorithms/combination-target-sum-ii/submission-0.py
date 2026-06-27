class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            prev = -1

            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue

                if total + candidates[j] > target:
                    break

                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()

                prev = candidates[j]

        dfs(0, [], 0)

        return res