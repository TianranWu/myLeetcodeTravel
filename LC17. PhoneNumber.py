class Solution:
    def letterCombinations(self, digits: str):

        if not digits:
            return list()

        phoneMap = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        length = 1
        for i in range(len(digits)):
            length *= len(phoneMap[digits[i]])

        print('length in total %d !' % length)

        for i in range(length):
            
            last = i;
            j = len(digits)-1
            sb = ''
            while(j>=0):
                print(last)
                
                # c = digits[j] - '0'
                zimu_string = phoneMap[digits[j]]
                pos = last % len(zimu_string)
                sb = sb+ zimu_string[int(pos)]
                last = last/len(zimu_string)
                

                j-=1
            # for(int j = digits.length()-1; j>=0;j--){
            #     int c = digits.charAt(j)-'0';
            #     int pos = last%strs[c].length();
            #     sb.append(strs[c].charAt(pos));
            #     last = last/strs[c].length();
            # }
            # result.add(sb.reverse().toString());
            print(sb[::-1])
        
            
            
            # out.append()
        return 0

    def letterCombinations2(self, digits: str):
        
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations



digits = "23"
solu = Solution()
solu.letterCombinations(digits)