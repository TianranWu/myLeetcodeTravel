class Solution(object):
    def numRescueBoats(self, people, limit):
        
        people.sort()

        left = 0
        right = len(people) - 1
        count = 0
        while(left <= right):
            # print(count, people,left, right)
            
            if right == left:
                count += 1
                break
            if people[left] + people[right] > limit:
                right -= 1
                count += 1
            else:
                right -= 1
                left += 1
                count += 1

            # print(people)

        return count
        




class Solution_timelimit(object):
    def numRescueBoats(self, people, limit):
        
        people.sort()

        left = 0
        right = len(people) - 1
        count = 0
        while(len(people)>0):
            right = len(people) - 1
            if len(people) == 1:
                count+=1
                break
            if people[left] + people[right] > limit:
                people = people[:-1]
                count+=1
            else:
                people = people[1:-1]
                count+=1

            print(people)

        return count


class Solution_time_limit2(object):
    def remove(self,alist,aindex):
        if aindex == -1:
            return alist[:-1]
        if aindex == 0:
            return alist[1:]
        else:
            return alist[:aindex] + alist[aindex+1:]

    def find_index(self, blist, bther):
        head = 0
        end = len(blist)
        alist = blist.copy()
        print(blist, alist[head:end])
        while len(blist) > 1:
            length = len(blist)
            
            if blist[round(length/2)] > bther:
                end = end - round(length/2) 
                blist = blist[:round(length/2)]

            else:
                head = round(length/2) + head 
                blist = blist[round(length/2):]
                
            
            # print(blist)
            # print(alist[head:end]) 

        # assert head==end-1 or head==end
            
        return head


    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        if people[-1] > limit:
            return 0
        
        count = 0
        while not len(people) == 0:

            print('####')
            print(people)
            count+=1
            ther = limit - people[0]
            people = people[1:]
        
            if people == []:
                break

            # for i in range(len(people)):
            #     if ther >= people[-i-1]:
            #         index = -i-1
            #         people = self.remove(people, index)
            #         break
            if ther >= people[0]:
                index = self.find_index(people, ther)
                print(index)
                people = self.remove(people, index)
            print(people)

        return count

people = [2,2,4,3]
limit = 6

# people = [1,2]
# limit = 3
# people = [3,2,2,1]
# limit = 3
# people = [3,5,3,4]
# limit = 5
# people = [5,1,4,2]
# limit = 6
solu = Solution()
print(solu.numRescueBoats(people,limit))
# solu.find_index([1, 2, 4, 5],5)