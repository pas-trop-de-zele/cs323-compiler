VALID_CHARS = "ab+-*/()$="

lookup = {
    "S":    {"a": "a=E", "b": "",   "+": "",        "-": "",        "*": "",    "/": "",     "(": "",       ")": "",        "$": ""},
    "E":    {"a": "TQ",  "b": "TQ", "+": "",        "-": "",        "*": "",    "/": "",     "(": "TQ",     ")": "",        "$": ""},
    "Q":    {"a": "",    "b": "",   "+": "+TQ",     "-": "-TQ",     "*": "",    "/": "",     "(": "",       ")": "EPSILON", "$": "EPSILON"},
    "T":    {"a": "FR",  "b": "FR", "+": "",        "-": "",        "*": "",    "/": "",     "(": "FR",     ")": "",        "$": ""},
    "R":    {"a": "",    "b": "",   "+": "EPSILON", "-": "EPSILON", "*": "*FR", "/": "/FR",  "(": "",       ")": "EPSILON", "$": "EPSILON"},
    "F":    {"a": "a",   "b": "b",  "+": "",        "-": "",        "*": "",    "/": "",     "(": "(E)",    ")": "",        "$": ""},
}


def is_valid(string):
    for c in string:
        if c not in VALID_CHARS:
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


while True:
    string = input("\nPlease enter string with $ ending: ")
    if string == "Q":
        break

    # Remove all spaces
    string = remove_space(string)
    if not is_valid(string):
        continue

    print(f"--------------------CHECKING {string}--------------------")
    STARTING_STATE = "S"
    stack = [STARTING_STATE]

    while stack:
        current_state = stack[-1]
        removal = False

        if current_state == string[0]:
            removal = True
            action = f"Remove {current_state}"
        else:
            next_state = lookup[current_state][string[0]]
            action = f"{current_state} -> {next_state}"

            if not next_state:
                print(('$' + ''.join(stack)).ljust(10),
                      string.ljust(10), action.ljust(10))
                print("INVALID INPUT")
                print(
                    f"There is no next state for the {current_state} at {string[0]}")
                break

        print(('$' + ''.join(stack)).ljust(10),
              string.ljust(10), action.ljust(10))

        stack.pop()

        if removal:
            string = string[1:]
        else:
            # We appending nothing for EPSILON
            if next_state != "EPSILON":
                for char in reversed(next_state):
                    stack.append(char)

print("\texit...")
