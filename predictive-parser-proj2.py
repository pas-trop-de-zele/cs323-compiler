lookup = {
    "E":    {"i": "TQ",       "+": "INVALID", "*": "INVALID", "(": "TQ",       ")": "INVALID", "$": "INVALID"},
    "Q":   {"i": "INVALID'",  "+": "+TQ",    "*": "INVALID", "(": "INVALID'",  ")": "EPSILON", "$": "EPSILON"},
    "T":    {"i": "FR",       "+": "INVALID", "*": "INVALID", "(": "FR",       ")": "INVALID", "$": "INVALID"},
    "R":   {"i": "INVALID'",  "+": "EPSILON", "*": "*FR",    "(": "INVALID'",  ")": "EPSILON", "$": "EPSILON"},
    "F":    {"i": "i",         "+": "INVALID", "*": "INVALID", "(": "(E)",       ")": "INVALID", "$": "INVALID"},
}

STARTING_STATE = "E"
input = "i+i*i$"
stack = [STARTING_STATE]

while stack:
    current_state = stack[-1]
    removal = False

    if current_state == input[0]:
        removal = True
        action = f"Remove {current_state}"
    else:
        next_state = lookup[current_state][input[0]]
        action = f"{current_state} -> {next_state}"

        if next_state == "INVALID":
            print("INVALID INPUT")
            break

    print(('$' + ''.join(stack)).ljust(10), input.ljust(10), action.ljust(10))

    stack.pop()

    if removal:
        input = input[1:]
    else:
        if next_state != "EPSILON":
            for char in reversed(next_state):
                stack.append(char)

print("\texit...")
