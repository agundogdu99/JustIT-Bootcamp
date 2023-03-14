print("hi")

# # Nested dictionary
# myFamily = {
#     "firstChild": {"name": "Alice", "age": 24},
#     "secondChild": {"name": "Paul", "age": 19},
# }


# ####################
# for aList, items in enumerate(myFamily.items()):
#     print(f"\nThis is child {aList} and list items: {items}")
#     for indexPos, anItem in enumerate(items):
#         print(f"This is index {indexPos} : item: {anItem}")

# for aList, items in myFamily.items():
#     print(f"\nThis is child {aList} and list items: {items}")
#     for indexPos, anItem in enumerate(items):
#         print(f"This is index {indexPos} : item: {anItem}")


# def count_bits(n):
#     bit_value = list(bin(n))
#     return bit_value.count('1')

# count_bits(5)

import sys
import math
# import numpy as np
# import pandas as pd
# from sklearn import ...

#for line in sys.stdin:
    
  #  print(line, end="")
    


import sys
import math
# import numpy as np
# import pandas as pd
# from sklearn import ...

  


for line in sys.stdin:
    # SPlitting and mapping out values to respective variables
    mib_size, seconds = map(int, line.split())
    #print(mib_size)
    #print(seconds)

    # Converting mebibytes to bits - Got help with formula from https://www.dataunitconverter.com/mebibyte-to-bit/400
    bits_size = mib_size * (8*1024**2)
    # print(bits_size)

    # Getting the Network bandwidth in bits
    network_bandwidth_bits = bits_size / seconds
    # Converting the bits bandwidth to megabits bandwidth, and rounding up
    # 1,000,000 bits in 1 megabit
    network_bandwidth_mb = math.ceil(network_bandwidth_bits / 1000000)

 
    print(network_bandwidth_mb)













import math
def rgb(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    r_split = math.modf(r / 16)
    g_split = math.modf(g / 16)
    b_split = math.modf(b / 16)

    r_calculated_list = []
    r_calculated_list.append(int(r_split[1]))
    r_calculated_list.append(int(r_split[0] * 16))

    g_calculated_list = []
    g_calculated_list.append(int(g_split[1]))
    g_calculated_list.append(int(g_split[0] * 16))

    b_calculated_list = []
    b_calculated_list.append(int(b_split[1]))
    b_calculated_list.append(int(b_split[0] * 16))

    for i, value in enumerate(r_calculated_list):
        if value == 10:
            r_calculated_list[i] = "A"
        elif value == 11:
            r_calculated_list[i] = "B"
        elif value == 12:
            r_calculated_list[i] = "C"
        elif value == 13:
            r_calculated_list[i] = "D"
        elif value == 14:
            r_calculated_list[i] = "E"
        elif value == 15:
            r_calculated_list[i] = "F"


    for i, value in enumerate(g_calculated_list):
        if value == 10:
            g_calculated_list[i] = "A"
        elif value == 11:
            g_calculated_list[i] = "B"
        elif value == 12:
            g_calculated_list[i] = "C"
        elif value == 13:
            g_calculated_list[i] = "D"
        elif value == 14:
            g_calculated_list[i] = "E"
        elif value == 15:
            g_calculated_list[i] = "F"



    for i, value in enumerate(b_calculated_list):
        if value == 10:
            b_calculated_list[i] = "A"
        elif value == 11:
            b_calculated_list[i] = "B"
        elif value == 12:
            b_calculated_list[i] = "C"
        elif value == 13:
            b_calculated_list[i] = "D"
        elif value == 14:
            b_calculated_list[i] = "E"
        elif value == 15:
            b_calculated_list[i] = "F"


    hex_list = r_calculated_list + g_calculated_list + b_calculated_list

    return ''.join([str(elem) for elem in hex_list])
