class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs: # Iterate through each word in the input list
            sorted_word = ''.join(sorted(word)) # Sort the characters in the word to create a key
            result[sorted_word].append(word) # Append the original word to the list corresponding to the sorted key

        return list(result.values())