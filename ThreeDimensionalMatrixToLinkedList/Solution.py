class SpecialNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.front = None
        self.back = None

    def extract_neightbors(self):
        lst = []#[self.val] 
        if self.front != None:
           lst.append(self.front.val)
        if self.back != None:
           lst.append(self.back.val)
        if self.left != None:
           lst.append(self.left.val)
        if self.right != None:
           lst.append(self.right.val)
        if self.up != None:
           lst.append(self.up.val)
        if self.down != None:
           lst.append(self.down.val)
        return lst


num_layers, num_rows, num_cols = 0, 0, 0

def create_nodes(mat):
   global num_layers, num_rows, num_cols
   for layer in range(num_layers):
      for row in range(num_rows):
         for col in range(num_cols):
            mat[layer][row][col] = SpecialNode(mat[layer][row][col])


def define_neighbours(mat, layer, row, col):
   global num_layers, num_rows, num_cols
   node = mat[layer][row][col]
   node.front = mat[layer - 1][row][col]
   node.back = mat[(layer + 1) % num_layers][row][col]
   node.left = mat[layer][row][col - 1]
   node.right = mat[layer][row][(col + 1) % num_cols]
   node.up = mat[layer][row - 1][col]
   node.down = mat[layer][(row + 1) % num_rows][col]


def matrix_to_linked_list(mat):
   global num_layers, num_rows, num_cols
   num_layers = len(mat)
   num_rows = len(mat[0])
   num_cols = len(mat[0][0])
   create_nodes(mat)
   for layer in range(num_layers):
      for row in range(num_rows):
         for col in range(num_cols):
            define_neighbours(mat, layer, row, col)
   return mat[0][0][0]
   
   

