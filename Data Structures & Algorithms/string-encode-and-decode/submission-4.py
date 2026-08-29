class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += f'{len(s)}|{s}'
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        # print(s)
        while i < len(s):
            num = ''
            while s[i] != '|':
                num += s[i]
                i += 1
            n = int(num)

            ans.append(s[i + 1:i + 1 + n])
            # print(i, ans)
            i += n + 1
        return ans
        
