class Solution:
    def isValid(self, s: str) -> bool:
        paren_pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        closers = list(paren_pairs.values())

        stack = []
        for c in s:
            if len(stack) == 0:
                # If the stack is empty and a closer is encountered, return
                # False.
                if c in closers:
                    return False

                # Otherwise, push the expected closer to the stack. The prompt
                # said that s consists of only openers and closers. Because c
                # is not a closer, we can assume it is an opener.
                stack.append(paren_pairs[c])
                continue

            if c in closers:
                # The next character is a closer. Get the expected closer.
                exp = stack.pop()
                if c != exp:
                    # The current closer did not match the expected closer.
                    return False

                # Continue to the next character.
                continue

            # The next character is an opener. Push the expected closer onto
            # the stack.
            stack.append(paren_pairs[c])

        # By this point, no errors have occurred. Therefore, return True if the
        # stack is empty.
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()

    for input, exp, name in [
        ("()", True, "()"),
        ("()[]{}", True, "()[]{}"),
        ("(]", False, "(]"),
        ("([)]", False, "([)]"),
        ("{[]}", True, "{[]}"),
    ]:
        res = s.isValid(input)
        if res != exp:
            print(f"{name}, exp: {exp}, res: {res}")
        else:
            print(f"passed: {name}")
