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

def longest_sub_seq_rec(s1, s2, index_1, index_2, result):
    if index_1 == len(s1) or index_2 == len(s2):
        return result

    if s1[index_1] == s2[index_2]:
        result = "{}{}".format(result, s1[index_1])
        return longest_sub_seq_rec(s1, s2, index_1 + 1, index_2 + 1, result)
    
    partial_1 = longest_sub_seq_rec(s1, s2, index_1 + 1, index_2, result)
    partial_2 = longest_sub_seq_rec(s1, s2, index_1, index_2 + 1, result)
    return partial_1 if len(partial_1) > len(partial_2) else partial_2



def longest_sub_seq(s1, s2):
    return longest_sub_seq_rec(s1, s2, 0, 0, "")    

def main():
    s1 = "ABAZDC"
    s2 = "BACBAD"
    sub_seq = longest_sub_seq(s1, s2)
    print(sub_seq)
    correct = "ABAD"
    print(correct)
    print(sub_seq == correct)


if __name__ == "__main__":
    main()