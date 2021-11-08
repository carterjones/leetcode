from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. Choose a string with the longest length. It doesn't matter which
        #    one if there are multiple strings with the longest length.
        longest = sorted(strs, key=len)[-1]

        # 2. Generate a list of substrings starting with the full string,
        #    followed by the full string without the last letter, followed by
        #    one with one more letter removed from the end, etc. until there is
        #    the empty string.
        combinations = []
        for i in range(len(longest), -1, -1):
            combinations.append(longest[:i])

        # 3. Search through all the other strings for each of those strings.
        #    Return the first string that matches the prefix of all other
        #    strings, which could be the empty string.
        for combination in combinations:
            is_match = True
            for str in strs:
                if str == longest:
                    continue
                if not str.startswith(combination):
                    is_match = False
                    break
            if is_match:
                return combination

        # If my logic is correct, this should never be reached, but this is
        # here just in case I messed up.
        return ''


if __name__ == '__main__':
    s = Solution()

    for input, exp, name in [
        (["flower", "fowl", "flight"], "f", "f"),
        (["flower", "flow", "flight"], "fl", "fl"),
        (["tow", "tower", "town", "toward"], "tow", "tow"),
        (["dog", "racecar", "car"], "", "No common prefix"),
    ]:
        res = s.longestCommonPrefix(input)
        if res != exp:
            print(f"{name}, exp: {exp}, res: {res}")
        else:
            print(f"passed: {name}")
