def threesum(nums):
    length = len(nums)
    nums.sort()
    out = list()
    for i in range(length):
        
        if nums[i]>0: break

        # print(i>0,nums[i]==nums[i-1])
        if i>0 and nums[i] == nums[i-1]:
            # print("c")
            continue

        L = i+1
        R = length - 1

        # print(L,R)

        while (L<R):
            # print(L,R, nums[L],nums[R],-1 * nums[i])
            if L>i+1 and nums[L] == nums[L-1]: 
                L+=1
                # print("continue")
                continue

            if nums[L] + nums[R] == -1 * nums[i]:
                out.append([nums[i],nums[L],nums[R]])
                L+=1
                R-=1
                # print('Both')
            if nums[L] + nums[R] > -1 * nums[i]:
                R-=1
                # print('right! {} {}->{} {}'.format(L,R+1,L,R))
            if nums[L] + nums[R] < -1 * nums[i]:
                L+=1
            # print(L,R)
            
    return out

nums = [-3,-5,1,2,4,7]
nums = [-3,-3,1,2]
print(threesum(nums))
            