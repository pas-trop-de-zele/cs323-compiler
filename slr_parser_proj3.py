table = {      
    0:	{"i":"S5"	,"+":""	    ,"-":""	    ,"*":""	    ,"/":""	    ,"(":"S4"	,")":""	    ,"$":""     },     
    1:	{"i":""	    ,"+":"S6"	,"-":"S7"	,"*":""	    ,"/":""	    ,"(":""	    ,")":""	    ,"$":"ACC"  },
    2:	{"i":""	    ,"+":"R3"	,"-":"R3"	,"*":"S8"	,"/":"S9"	,"(":""	    ,")":"R3"	,"$":"R3"   },
    3:	{"i":""	    ,"+":"R6"	,"-":"R6"	,"*":"R6"	,"/":"R6"	,"(":""	    ,")":"R6"	,"$":"R6"   },
    4:	{"i":"S5"	,"+":""	    ,"-":""	    ,"*":""	    ,"/":""	    ,"(":"S4"	,")":""	    ,"$":""     },
    5:	{"i":""	    ,"+":"R8"	,"-":"R8"	,"*":"R8"	,"/":"R8"	,"(":""	    ,")":"R8"	,"$":"R8"   },
    6:	{"i":"S5"	,"+":""	    ,"-":""	    ,"*":""	    ,"/":""	    ,"(":"S4"	,")":""	    ,"$":""     },
    7:	{"i":"S5"	,"+":""	    ,"-":""	    ,"*":""	    ,"/":""	    ,"(":"S4"	,")":""	    ,"$":""     },
    8:	{"i":"S5"	,"+":""	    ,"-":""	    ,"*":""	    ,"/":""	    ,"(":"S4"	,")":""	    ,"$":""     },
    9:	{"i":"S5"	,"+":""	    ,"-":""	    ,"*":""	    ,"/":""	    ,"(":"S4"	,")":""	    ,"$":""     },
    10:	{"i":""	    ,"+":"S6"	,"-":"S7"	,"*":""	    ,"/":""	    ,"(":""	    ,")":"S15"	,"$":""     },
    11:	{"i":""	    ,"+":"R1"	,"-":"R1"	,"*":"S8"	,"/":"S9"	,"(":""	    ,")":"R1"	,"$":"R1"   },
    12:	{"i":""	    ,"+":"R2"	,"-":"R2"	,"*":"S8"	,"/":"S9"	,"(":""	    ,")":"R2"	,"$":"R2"   },
    13:	{"i":""	    ,"+":"R4"	,"-":"R4"	,"*":"R4"	,"/":"R4"	,"(":""	    ,")":"R4"	,"$":"R4"   },
    14:	{"i":""	    ,"+":"R5"	,"-":"R5"	,"*":"R5"	,"/":"R5"	,"(":""	    ,")":"R5"	,"$":"R5"   },
    15:	{"i":""	    ,"+":"R7"	,"-":"R7"	,"*":"R7"	,"/":"R7"	,"(":""	    ,")":"R7"	,"$":"R7"   }
}

goto = {
    0:	{"E":1	,"T":2	,"F":3  },
    1:	{"E":""	,"T":""	,"F":"" },
    2:	{"E":""	,"T":""	,"F":"" },
    3:	{"E":""	,"T":""	,"F":"" },
    4:	{"E":10	,"T":2	,"F":3  },
    5:	{"E":""	,"T":""	,"F":"" },
    6:	{"E":""	,"T":11	,"F":3  },
    7:	{"E":""	,"T":12	,"F":3  },
    8:	{"E":""	,"T":""	,"F":13 },
    9:	{"E":""	,"T":""	,"F":14 },
    10:	{"E":""	,"T":""	,"F":"" },
    11:	{"E":""	,"T":""	,"F":"" },
    12:	{"E":""	,"T":""	,"F":"" },
    13:	{"E":""	,"T":""	,"F":"" },
    14:	{"E":""	,"T":""	,"F":"" },
    15:	{"E":""	,"T":""	,"F":"" }
}

cfg = {
    'E+T':  'E',
    'E-T':  'E',
    'T'  :  'E',
    'T*F':  'T',
    'T/F':  'T',
    'F'  :  'T',
    '(E)':  'F',
    'i'  :  'F'
}

VALID_CHARS = "i+-*/()$"


def is_valid(string):
    for c in string:
        if c not in VALID_CHARS:
            return False
    return len(string) != 0


def remove_space(string):
    no_space_string = ""
    for char in string:
        if char.isspace():
            continue
        no_space_string += char
    return no_space_string

def display(stack_char, stack_no, string, entry, action):
    stack = ""
    for char, num in zip(stack_char, stack_no):
        stack += char
        stack += str(num)
    print(stack.ljust(20), string.rjust(10), entry.rjust(10), action.rjust(25))

def replace(string):
    while string and string not in cfg:
        string = string[1:]
    # NEED TO THROW EXCEPTION HERE IN CASE NOTHING FOUND
    return string, cfg[string]
    

while True:
    string = input("\nPlease enter string with $ ending: ")
    if string == "Q":
        break

    # Remove all spaces
    string = remove_space(string)
    if not is_valid(string):
        print("INVALID INPUT")
        continue
    
    if string and string[-1] != '$':
        string += '$'

    # Example: "(i/i)$"
    print(f"--------------------CHECKING {string}--------------------")
    print(("Stack").ljust(20), ("Input").rjust(10), ("Entry").rjust(10), ("Action").rjust(25))

    stack_char = ['$']
    stack_no = [0]
    entry = ''
    
    while True:
        entry = table[stack_no[-1]][string[0]]

        if entry == 'ACC':
            break

        if not entry:
            print(f"INVALID TABLE ENTRY [{stack_no[-1]}, {string[0]}]")
            break

        action = ''
        is_shift = entry[0] == 'S'

        if is_shift:
            display(stack_char, stack_no, string, entry, action)
            stack_char.append(string[0])
            string = string[1:]

            next_state = int(entry[1:])
            stack_no.append(next_state)
        else:
            found_entry, replacement = replace(''.join(stack_char))
            
            prev_state = stack_no[- (1 + len(found_entry))]
            next_state = goto[prev_state][replacement]
            action += f"{replacement}->{found_entry}; [{prev_state},{replacement}]={next_state}"

            display(stack_char, stack_no, string, entry, action)
            
            stack_char = stack_char[:-len(found_entry)]
            stack_no = stack_no[:-len(found_entry)]
            stack_char.append(replacement)
            stack_no.append(next_state)
    
    if (entry == 'ACC'):    
        display(stack_char, stack_no, string, entry, '')


    