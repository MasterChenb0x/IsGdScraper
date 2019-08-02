#!/usr/local/bin/python3

import itertools

# List components
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
upper_vow = ['A', 'E', 'I', 'O', 'U']
upper_cons = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
lower_vow = ['a', 'e', 'i', 'o', 'u']
lower_cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'] 


# Menu Selection
selection = ""
while selection == "":
    print('Select the list to generate.')
    print('----------------------------')
    print('1. Full characterset [A-Za-z0-9]')
    print('2. Lower-case characterset [a-z0-9]')
    print('3. Lower-case "pronounceable" ex: ababab')
    selection = input()

    if selection == '1':
        charset = nums + upper_vow + upper_cons + lower_vow + lower_cons
        with open("linkslugs.txt", "w") as slugs:
            for ch1, ch2, ch3, ch4, ch5, ch6 in itertools.product(charset, charset, charset, charset, charset, charset):
                slugs.write(ch1 + ch2 + ch3 + ch4 + ch5 + ch6)
                slugs.write("\n")
    elif selection == '2':
        charset = lower_cons + lower_vow + nums
        with open("linkslugs.txt", "w") as slugs:
            for ch1, ch2, ch3, ch4, ch5, ch6 in itertools.product(charset, charset, charset, charset, charset, charset):
                slugs.write(ch1 + ch2 + ch3 + ch4 + ch5 + ch6)
                slugs.write("\n")
    elif selection == '3':
        with open("linkslugs.txt", "w") as slugs:
            for c1, v1, c2, v2, c3, v3 in itertools.product(lower_cons, lower_vow, lower_cons, lower_vow, lower_cons, lower_vow):
                slugs.write(c1 + v1 + c2 + v2 + c3 + v3)
                slugs.write("\n")
            for v1, c1, c2, v2, c3, v3 in itertools.product(lower_vow, lower_cons, lower_vow, lower_cons, lower_vow, lower_cons):
                slugs.write(v1 + c1 + v2 + c2 + v3 + c3)
                slugs.write("\n")
    else:
        selection = ""

