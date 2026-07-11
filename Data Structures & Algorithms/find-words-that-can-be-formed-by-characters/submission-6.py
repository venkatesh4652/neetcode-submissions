class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars = Counter(chars)
        res = 0
        for w in words:
            count_words = Counter(w)
            good = True
            for c in count_words:
                if count_words[c] > count_chars[c]:
                    good = False
                    break
            if good:
                res += len(w)
        return res



