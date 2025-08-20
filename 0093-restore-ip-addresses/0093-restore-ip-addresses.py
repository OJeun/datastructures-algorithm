class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        OCTET_MAX_DIGITS = 3
        ips = []
        ip = []

        def dfs(left, right, octet):

            if octet == 5:
                if left == len(s):
                    ips.append(".".join(ip))
                return

            if left >= len(s):
                return
            

            for offset in range(OCTET_MAX_DIGITS):
                right = left + offset
                length = right - left + 1
                if length == 2 or length == 3:
                    if s[left] == "0" or not (0 <= int(s[left:right+1]) <= 255):
                        continue

                ip.append(s[left:right+1])
                dfs(right + 1, right + offset, octet+1)
                ip.pop()

        dfs(0, 0, 1)
        return ips  