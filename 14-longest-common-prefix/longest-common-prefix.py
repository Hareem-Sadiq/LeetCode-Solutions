class Solution(object):
    def longestCommonPrefix(self, strs):
        len_str=len(strs)
        char_store=""
        if len_str==1:
            return(strs[0])
        for word in range(1, len_str):
            if word>1:
                strs[word-1]=char_store
                char_store=""
            if (len(strs[word-1])<len(strs[word])):
                string_limit=len(strs[word-1])
            else:
                string_limit=len(strs[word])
            for i in range(string_limit):
                char_1=strs[word-1][i]
                char_2=strs[word][i]
                if char_1==char_2:
                    char_store= char_store+char_1
                    continue
                else:
                    break
                break
        return(char_store)
        