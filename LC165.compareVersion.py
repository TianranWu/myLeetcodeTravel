class Solution:
    def compareVersion(self, version1: str, version2: str):
        vlist1 = version1.split('.')
        vlist2 = version2.split('.')

        if len(vlist1) > len(vlist2):
            for i in range(len(vlist1)-len(vlist2)):
                vlist2.append('0')
        elif len(vlist1) < len(vlist2):
            for i in range(len(vlist2)-len(vlist1)):
                vlist1.append('0')

        assert len(vlist1) == len(vlist2)

        for i in range(len(vlist1)):
            x = int(vlist1[i])
            y = int(vlist2[i])

            if x>y: return 1
            if x<y: return -1
            
        return 0

    def official_version(self, version1: str, version2: str):
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else -1
        return 0

version1 = "1.0.0"
version2 = "1.0.0"
solu = Solution()
print(solu.compareVersion(version1,version2))