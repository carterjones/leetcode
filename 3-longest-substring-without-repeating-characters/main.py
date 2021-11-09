class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = []
        current = 0
        maximum = 0
        for c in s:
            if c in used:
                i = used.index(c)
                used = used[i+1:] + [c]
                current = len(used)
                continue
            used.append(c)
            current += 1
            maximum = max(current, maximum)
        return maximum


if __name__ == '__main__':
    s = Solution()

    for input, exp, name in [
        ("abcabcbb", 3, "case 1"),
        ("bbbbb",    1, "case 2"),
        ("pwwkew",   3, "case 3"),
        ("",         0, "case 4"),
        ("dvdf",     3, "case 5"),
        ("nfpdmpi",  5, "case 6"),
    ]:
        res = s.lengthOfLongestSubstring(input)
        if res != exp:
            print(f"{name}, exp: {exp}, res: {res}")
        else:
            print(f"passed: {name}")
