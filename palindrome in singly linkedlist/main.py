import string
from random import randrange

class node(object):
    def __init__(self, char):
        self._data = char
        self._next = None
        
    def get_next(self):
        return self._next
    
    def append(self, char):
        self._next = node(char)
        return self._next
    
    def get_data(self):
        return self._data
    
    
def generate_palindrome(length):
    rand_char = string.ascii_lowercase[randrange(26)]
    head = node(rand_char)
    used_chars = [rand_char]
    itt = head
    
    for i in range(length // 2 - 1):
        rand_char = string.ascii_lowercase[randrange(26)]
        itt = itt.append(rand_char)
        used_chars.append(rand_char)
    
    if length & 1:
        middle_char = string.ascii_lowercase[randrange(26)]
        itt = itt.append(middle_char)
    
    for char in reversed(used_chars):
            itt = itt.append(char)

    return head
        
def print_list(head):
    itt = head
    while itt:
        print(itt.get_data(), end="")
        itt = itt.get_next()

    print()


def check_palindrome(head):
    value = check_palindrome_rec(head, head)
    return value != None


def check_palindrome_rec(curr, head):
    if curr.get_next():
        return_value = check_palindrome_rec(curr.get_next(), head)
        if return_value:
            if not return_value.get_next():
                if curr.get_data() == return_value.get_data():
                    return node("T")
                else:
                    return None
            else:
                return return_value.get_next()
        else:
            return None
    else:
        if curr.get_data() == head.get_data():
            return head.get_next()
        else:
            return None





def main():
    head = generate_palindrome(5)
    print_list(head)
    print(check_palindrome(head))
    
    
    


if __name__ == "__main__":
    main()
        