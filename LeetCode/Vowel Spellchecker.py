from collections import defaultdict
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        wl = set(wordlist)
        case_map = defaultdict(str)
        vowel_map = defaultdict(str)

        def devowel(s):
            return "".join("*" if ch in vowels else ch for ch in s)

        for word in wordlist:
            w = word.lower()
            if w not in case_map:
                case_map[w] = word

            s = devowel(word.lower())
            if s not in vowel_map:
                vowel_map[s] = word

        ans = []

        for q in queries:
            if q in wl:
                ans.append(q)
    
            elif q.lower() in case_map:
                ans.append(case_map[q.lower()])
                
            elif devowel(q.lower()) in vowel_map:
                ans.append(vowel_map[devowel(q.lower())])

            else:
                ans.append("")

        return ans
