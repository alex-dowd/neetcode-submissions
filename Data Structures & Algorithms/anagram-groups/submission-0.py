class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_counts = []

        for word in strs:
            temp = {}

            for i in word:
                if i in temp:
                    temp[i] += 1
                else:
                    temp[i] = 1

            key = tuple(sorted(temp.items()))
            word_counts.append((word, key))

        out = {}

        for word, key in word_counts:
            if key in out:
                out[key].append(word)
            else:
                out[key] = [word]

        output = []

        for i in out:
            output.append(out[i])

        return output