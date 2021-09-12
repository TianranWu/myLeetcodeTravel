class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # char_list = [chr(i) for i in range(33,48)]
        # print(char_list)
        
        # new_p = ''.join([ ' ' if c in char_list else c.lower() for c in paragraph])
        new_p = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
        word = new_p.split()
        print(word)
        
        dic = {}
        for this_word in word:
            if this_word in banned:
                continue

            if this_word in dic.keys():
                dic[this_word] +=1
            else:
                dic[this_word] = 1


        sort_result = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))
        # print(sort_result)
        return sort_result[-1][0]
