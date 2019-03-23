s1 = "ABAZDCasdffasdfFDSGRSVFHDFSFSDfdsfFDSFgfsdggf"
s2 = "DCas123sdfFVF123HDSD123fds33fFD444SFg"

def sub_Seq(s1, s2):
    l = []
    search_from = 0
    for char in s1:
        if char in s2[search_from:]:
            l.append([char, search_from + s2[search_from:].index(char)])
            search_from = s2[search_from:].index(char)

    sub_seq = ""
    # print(l)
    l = [element for (i, element) in enumerate(l[:-1]) if l[i][1] < l[i+1][1]]

    for element in l:
        sub_seq += element[0]

    return sub_seq

def wrapper(s1, s2):
    if len(s1) == len(s2):
        seq_1 = sub_Seq(s1, s2)
        seq_2 = sub_Seq(s2, s1)
        return seq_1 if len(seq_1) > len(seq_2) else seq_2
    else:
        return sub_Seq(s1, s2) if len(s1) < len(s2) else sub_Seq(s2, s1)


print(wrapper(s1,s2))
print(wrapper(s2,s1))