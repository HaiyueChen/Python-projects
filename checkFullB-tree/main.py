class TreeNode(object):
    
    def __init__(self, data):
        self._data = data
        self._left =self._right = None

    def get_data(self):
        return self._data

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def add(self, number):
        if number == 3.5:
            print(self._data)

        if number < self._data:
            if not self._left:
                self._left = TreeNode(number)
            else:
                self._left.add(number)
        else:
            if not self._right:
                self._right = TreeNode(number)
            else:
                self._right.add(number)


def check_full_tree(root):
    if not root:
        return False
    else:
        # return check_full_tree_dfs(root)
        return check_full_tree_bfs([root])

def check_full_tree_dfs(root):
    if not root.get_left() and not root.get_right():
        return True
    
    if not root.get_left() or not root.get_right():
        return False
    
    return check_full_tree_dfs(root.get_left()) and check_full_tree_dfs(root.get_right())
    

def check_full_tree_bfs(nodes_to_check):
    while nodes_to_check:
        checking = nodes_to_check.pop(0)
        left = checking.get_left()
        right = checking.get_right()
        if not left and not right:
            continue

        if not left or not right:
            return False
        else:
            nodes_to_check.append(left)
            nodes_to_check.append(right)
    return True

def main():
    root = TreeNode(5)
    root.add(4)
    root.add(6)
    root.add(2)
    root.add(4.5)
    # print(root.get_data())
    # print(root.get_left().get_data())
    # print(root.get_right().get_data())
    # print(root.get_left().get_left().get_data())
    # print(root.get_left().get_right().get_data())
    print(check_full_tree(root))



if __name__ == "__main__":
    main()