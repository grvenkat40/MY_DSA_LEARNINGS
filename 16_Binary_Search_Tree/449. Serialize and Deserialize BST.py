# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root) -> str:
        nums = []
        def preorder(node):
            if node is None:
                return
            nums.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return " ".join(nums)

    def deserialize(self, data: str):
        if not data:
            return None
        nums = [int(n) for n in data.split()]
        def BuildBST(lower, upper):
            if not nums or not(lower < nums[0] < upper):
                return None
            value = nums.pop(0)
            node = TreeNode(value)
            node.left = BuildBST(lower, value)
            node.right = BuildBST(value, upper)
            return node
        return BuildBST(float("-inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

tree = ser.serialize(root)
ans = deser.deserialize(tree)

def showBST(node, l):
    if node is None:
        return
    showBST(node.left, l+1)
    print("     "*l, node.val)
    showBST(node.right, l+1)
showBST(ans, 0)