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
    head = node(string.ascii_lowercase[randrange(26)])
    itt = head
    used_chars = []
    for i in range(length // 2 - 1):
        



def main():
    pass
    
    


if __name__ == "__main__":
    main()
        