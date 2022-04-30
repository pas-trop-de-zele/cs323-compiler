OPERATIONS = '+-*/'
TERMINAL_CHAR = '$'


def is_valid(string):
    for c in string:
        if not c.isalnum() and c not in OPERATIONS and c != TERMINAL_CHAR:
            print(f"INVALID CHAR: {c}")
            return False
    return True


def remove_space(string):
    no_space_string = ""
    for char in string:
        if char.isspace():
            continue
        no_space_string += char
    return no_space_string


def get_chars(string):
    # We dont want duplicate but we also want to
    # keep chars relative order
    chars = []
    chars_set = set()
    for c in string:
        if c not in OPERATIONS and c != TERMINAL_CHAR and c not in chars_set:
            chars.append(c)
            chars_set.add(c)
    return chars


def replace_with_digit(string, lookup):
    res = []
    for c in string:
        res.append(c if c not in lookup else str(lookup[c]))
    return ''.join(res)


while True:
    string = input("\nPlease enter string with $ ending: ")
    if string.lower() == "Q":
        break

    # Remove all spaces
    string = remove_space(string)
    if not is_valid(string):
        continue

    chars = get_chars(string)
    lookup = {}
    for c in chars:
        val = input(f"Enter the value for {c}: ")
        lookup[c] = val

    string = replace_with_digit(string, lookup)

    stack = []
    for c in string:
        if c not in OPERATIONS:
            stack.append(c)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if c == '+':
                stack.append(str(a + b))
            elif c == '-':
                stack.append(str(a - b))
            elif c == '*':
                stack.append(str(a * b))
            elif c == '/':
                stack.append(str(a // b))
            elif c == '$':
                break
    print(stack[0])
