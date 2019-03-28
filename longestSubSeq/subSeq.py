"""
ABAZDC
BACBAD
"""

"""
ABBA
ABCABA
"""

"""
AGGTAB
GXTXAYB
"""

s1 = "ABAZDC"
s2 = "BACBAD"

def sub_Seq(s1, s2):
    # print(s1)
    # print(s2)
    table = {}
    l = []
    for char in s1:
        # print(char)
        # print(char, table)
        if char in table:
            search_from = table[char]
            if char in s2[search_from:]:
                if char in s2[search_from + 1:]:
                    new_index = s2[search_from + 1:].index(char)
                    if new_index != 0:
                        table[char] = search_from + 1 + new_index
                l.append([char, table[char]])
        else:
            if char in s2:
                table[char] = s2.index(char)
                l.append([char, table[char]])
    print(l)
    cleaned = []
    if (len(l) > 1 and l[0][1] <= l[1][1]):
        cleaned.append(l[0][0])

    for i in range(1, len(l) - 1):
        if l[i][1] < l[i + 1][1]:
            cleaned.append(l[i][0])
    cleaned.append(l[-1][0])

    max_length = len(s1) if len(s1) < len(s2) else len(s2)

    for i in range(len(cleaned) - max_length):
        cleaned.pop()
    # print(cleaned)
    return "".join(cleaned)

def wrapper(s1, s2):
    # if len(s1) == len(s2):
    #     seq_1 = sub_Seq(s1, s2)
    #     seq_2 = sub_Seq(s2, s1)
    #     return seq_1 if len(seq_1) > len(seq_2) else seq_2
    # else:
    #     return sub_Seq(s1, s2) if len(s1) > len(s2) else sub_Seq(s2, s1)
    seq_1 = sub_Seq(s1, s2)
    seq_2 = sub_Seq(s2, s1)
    return seq_1 if len(seq_1) > len(seq_2) else seq_2

print(wrapper(s1,s2))
# print(sub_Seq(s2, s1))


# print("BACBAD".index("B"))s