from crio.ds.Tree.TreeNode import *
from Solution import countTreePathsThatSumsToK





def main():


    root = readTreeReturnRoot()
    k = int(input())
    print(countTreePathsThatSumsToK(root, k))

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)
    main()
