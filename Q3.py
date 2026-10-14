from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        groups = defaultdict(list)
        for i, v in enumerate(arr):
            groups[v].append(i)

        visited = [False] * n
        visited[0] = True
        q = deque([0])
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1:
                    return steps

                for j in groups[arr[i]]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
                groups[arr[i]].clear()  # never scan this value group again

                for j in (i - 1, i + 1):
                    if 0 <= j < n and not visited[j]:
                        visited[j] = True
                        q.append(j)
            steps += 1

        return -1
      
