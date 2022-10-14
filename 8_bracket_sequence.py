def is_correct_bracket_seq(seq: str) -> bool:
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in seq:
        if i in brackets:
            if len(stack) == 0 or brackets[i] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(i)
    return len(stack) == 0


if __name__ == '__main__':
    sequence = input()
    print(is_correct_bracket_seq(sequence))
