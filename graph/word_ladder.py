from typing import List
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)

        # Creating adjacency list
        for word in wordList:
            for i in range(len(word)):
                # hot
                # i = 0
                # [] -> ["*"] + o : t -> *ot
                pattern = word[:i] + "*" + word[i + 1 :]
                neighbors[pattern].append(word)

        visited = set([beginWord])
        q = collections.deque([beginWord])

        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neighborWord in neighbors[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            q.append(neighborWord)

            res += 1
        return 0


s = Solution()
print(
    s.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
)
