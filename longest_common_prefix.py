# 14. Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lower-case English letters.

from typing import List


class LongestCommonPrefix:
    
    def longest_common_prefix(self, strs: List) -> str:
        result = ""
        if not strs or not strs[0]:
            return result

        result = strs[0]

        for s in strs[1:]:
            while s.find(result) != 0:
                result = result[:-1]     
        return result

if __name__ == '__main__':
    obj = LongestCommonPrefix()
    print(obj.longest_common_prefix(strs=["flow", "flower","plight"]))