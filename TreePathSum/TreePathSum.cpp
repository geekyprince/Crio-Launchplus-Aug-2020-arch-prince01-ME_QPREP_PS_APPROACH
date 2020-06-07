#include <bits/stdc++.h>
#include "Solution.cpp"
using namespace std;



int main()
{

    TreeNode* root  = TreeNode().readTreeReturnRoot();
    int k;
    cin >> k;
    printf("%lld\n", CountTreePathSumToK(root, k));
    return 0;
}
