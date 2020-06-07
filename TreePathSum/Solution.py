from crio.ds.Tree.TreeNode import TreeNode

'''Here we traverse the tree first left subtree then right subtree
and maintain two vector one for left subtree and other for right
subtree which store possible path for that tree and return to root.
after that we calculate the path value form each node to other
node of both left and right subtree and if their sum == k then
increase ans by 1 and follow above procedure far all subtree.
'''
ans = 0
def solve(root, k):
    global ans
    result = []
    #Base case
    if(root == None):       #No node in Tree
        return result
    
    #traverse Left and Right sub tree 
    left = solve(root.left, k)[1]
    right = solve(root.right, k)[1]
    
    if left or right: #check either subtree is not None
        if right: #right is not None
            for i in range(len(right)):
                path = right[i] + root.val 
                if path == k:
                    ans += 1
                result.append(path) 
        elif left: #left is not None
            for i in range(len(left)):
                path = left[i] + root.val 
                if path == k:
                    ans += 1
                result.append(path)
        else:
            #here both subtree, find possible 
            #path pattern from any node to any node
            for i in range(len(left)):
                #path1 indicate all path of left subtree
                path1 = left[i]
                for j in range(len(right)):
                    #path2 indicate right subtree till root
                    path2 = right[j] + root.val
                    
                    #check if left + root + right combine 
                    #sum to k but do not push to result
                    #as it is complete sub tree
                    if path1 + path2 == k:
                        ans += 1
                    
                    #ensure all path of right subtree
                    #evaluated only once
                    if i == 0:  
                        if path2 == k:
                            ans += 1
                        result.append(path2)
                
                #return left subtree till root
                if path1 + root.val == k:
                    ans += 1
                result.append(path1 + root.val)
    
    #Base case
    if root.val == k:       #value of node := k
        ans += 1
    result.append(root.val)
    
    return result

def countTreePathsThatSumsToK(root, k):
    global ans 
    ans = 0
    if(root == None):
        return 0
    solve(root, k)
    return ans
    
