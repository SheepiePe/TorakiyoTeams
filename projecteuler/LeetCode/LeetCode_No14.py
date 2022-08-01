"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

def longestCommonPrefix():
    strs = ["flower","flower","flower","flower"]

    firstStr = list(strs[0])
    targeStr = ''
        
    if len(strs) == 1:
        return strs[0]
        
    for i in range(len(firstStr) + 1):
        targeStr = ''
        for a in range(i):
            targeStr += firstStr[a]
            
        for j in range(len(strs)):
            if targeStr in strs[j]:
                continue
            else:
                targeStr = ''
                for b in range(i - 1):
                    targeStr += firstStr[b]
                    return targeStr
        
    return targeStr



def main():
    print(longestCommonPrefix())


main()