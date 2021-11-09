class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        highest_seen = None
        sum = 0
        for c in reversed(s):
            current_value = symbols[c]
            if highest_seen:
                highest_value = symbols[highest_seen]
                if current_value < highest_value:
                    sum -= current_value
                    continue
            sum += current_value
            highest_seen = c
        return sum


if __name__ == '__main__':
    s = Solution()

    for roman, exp, name in [
        ("III", 3, "3"),
        ("IV",  4, "4"),
        ("IX",  9, "9"),
        ("LVIII", 58, "58"),
        ("MCMXCIV", 1994, "1994"),
    ]:
        res = s.romanToInt(roman)
        if res != exp:
            print(f"{name}, exp: {exp}, res: {res}")
        else:
            print(f"passed: {name}")
