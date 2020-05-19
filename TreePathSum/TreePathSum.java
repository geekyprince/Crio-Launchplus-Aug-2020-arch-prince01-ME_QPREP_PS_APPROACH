import java.util.*;
import crio.ds.Tree.TreeNode;

class TreePathSum {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		TreeNode root  = TreeNode.readTreeReturnRoot(sc);
		int k = sc.nextInt();
		Long answer = Solution.CountTreePathSumToK(root, k);
		System.out.print(answer);
	}
}
