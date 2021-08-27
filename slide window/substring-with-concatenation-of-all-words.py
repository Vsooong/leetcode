from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = len(words[0])
        if len(s) < d * len(words):
            return []
        starts = []
        word_Counter = Counter(words)
        end = len(s) - d * len(words)
        cur_Counter = Counter()
        for i in range(end + 1):
            for j in range(len(words)):
                substr = s[i + d * j : i + d * (j + 1)]
                if substr in words:
                    cur_Counter[substr] += 1
                else:
                    cur_Counter.clear()
                    break
            # print(cur_Counter)

            if cur_Counter == word_Counter:
                starts.append(i)
            cur_Counter.clear()
        return starts


solution = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
s = "aaa"
words = ["a", "a"]
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
s= "bcabbcaabbccacacbabccacaababcbb"
words = ["c","b","a","c","a","a","a","b","c"]
print(solution.findSubstring(s, words))


# def findSubstring(self, s: str, words: List[str]) -> List[int]:
#     d = len(words[0])
#     if len(s) < d * len(words):
#         return []
#     starts = []
#     not_finds = list(words)
#     end = len(s) - d * len(words)
#     for i in range(end+1):
#         for j in range(len(words)):
#             substr = s[i + d * j : i + d * (j + 1)]
#             if substr in not_finds:
#                 not_finds.remove(substr)
#                 # print(substr, not_finds)
#             else:
#                 not_finds = list(words)
#                 break
#         if len(not_finds) == 0:
#             starts.append(i)
#             not_finds = list(words)
#     return starts
