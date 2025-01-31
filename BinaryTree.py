"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from queue import Queue

class BinaryTree:
    def build_binary_tree(self):
        x = int(input("Enter the root element: "))  # hamne yaha pe ak value liya jo hamlog root ka value hoga
        root = Node(x)  # hamne root ke node ka create kiya

        q = Queue()  # queue data structure instialise kiya hamne Queue isiye use kiya kyuki hame pahle root ke left ko dkehna hai phir right ko yani ki ham node pe aynge and uske left me add right me add karnge and wo newley aaded nodes back se add hote rahnge 
        q.put(root)  # queue me root ke adres ko bheja

        while not q.empty():  # q emepty yani sare ka hamne create kar diya
            temp = q.get()  # hamlog queue ke first value ko fetch kange and usle left and right child add karnge 
            
            # Left Node
            first = int(input(f"Enter the left value of {temp.data} (-1 for no left child): "))
            if first != -1:
                temp.left = Node(first)
                q.put(temp.left)  # queue ke andar left child ko add kiya
            
            # Right Node
            second = int(input(f"Enter the right value of {temp.data} (-1 for no right child): "))
            if second != -1:
                temp.right = Node(second)
                q.put(temp.right)  # queue ke andar right child ko add kiya

        return root  # pura binary tree create ho chuka hai, isliye root ko return kar rahe hain

# Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    root = bt.build_binary_tree()



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_binary_tree():
    x = int(input("Enter node value (-1 for NULL): "))  # Input the node value
    if x == -1:  # If input is -1, return None (NULL)
        return None

    temp = Node(x)  # Create a new node with the input value
    print(f"Enter left child of {x}:")  # Prompt for the left child
    temp.left = build_binary_tree()  # Recursively build the left subtree
    print(f"Enter right child of {x}:")  # Prompt for the right child
    temp.right = build_binary_tree()  # Recursively build the right subtree

    return temp  # Return the created node


# Example usage
if __name__ == "__main__":
    print("Build the binary tree:")
    root = build_binary_tree()




class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def build():
    x=int(input("Enter node value (-1 for NULL): "))  # Input the node value
    if x==-1:
        return None
    temp=Node(x)
    print(f"Enter left child of {x}:")  # Prompt for the left child
    temp.left=build()
    print(f"Enter right child of {x}:")  # Prompt for the right child
    temp.right=build()
    return  temp


####Dekho main khela yaha pe recursion ka  hai and wo  kasie hai dekho sbase pahle aisa samjho ki jab bhi function return karta hai to apne previous pass jata hai bus ye main concept hai to dekho
## isme kya hoga pahle 1 let say mera root node hoga thik hai uske badh promt ayega phir ki left wala dalo and phir se ham function ko call kar denge and phir se same hoga
#uske badh jab ham -1 enter karnge to kya hoga dekho tab dekho ye phir right side 

"""
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count=0

    def build_binary_tree(self):
        try:
            x = int(input("Enter node value (-1 for NULL): "))  # Input the node value
            if x == -1:  # If input is -1, return None (NULL)
                return None

            temp = Node(x)  # Create a new node with the input value
            print(f"Enter left child of {x}:")  # Prompt for the left child
            temp.left = self.build_binary_tree()  # Recursively build the left subtree
            print(f"Enter right child of {x}:")  # Prompt for the right child
            temp.right = self.build_binary_tree()  # Recursively build the right subtree

            return temp  # Return the created node
        except ValueError:
            print("Invalid input! Please enter integers only.")
            return None

    def preorder_traversal(self, root):
        if root is None:
            return []
        return [root.data] + self.preorder_traversal(root.left) + self.preorder_traversal(root.right)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.data] + self.inorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root is None:
            return []
        return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.data]
    ''''
    def level_order(self, root):
        if root is None:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            temp = q.popleft()
            ans.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return ans
    '''
    def level_order(self, root):
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        ans = []

        while q:
            level_size = len(q)  # Number of nodes at the current level
            level = []  # To store nodes at this level

            for _ in range(level_size):
                temp = q.popleft()
                level.append(temp.data)
                
                # Enqueue children of the current node
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            
            ans.append(level)  # Add current level to the answer
        
        return ans
    def getSize(self,root):
        ###THis is recursive approach of solving the problem
        if root is None:
            return 0
        left_side=self.getSize(root.left) 
        right_side=self.getSize(root.right)
        return left_side+right_side+1

    #This is iterative method for the same     
    def getSizeItretive(self,root):
        if root is None:
            return 0
        q=deque()
        q.append(root)
        count=0
        while q:
            count+=1
            temp=q.popleft()
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return count            

    def sumBT(self,root):
        if root is None:
            return 0  # we can also solve this using preorder concepts
        return self.sumBT(root.left)+self.sumBT(root.right)+root.data    

    def countLeafNode(self,root):
        #iterative ways
        count=0
        q=deque()
        q.append(root)
        while q:
            temp=q.popleft()
            if not temp.left and not temp.right:
                count+=1
            else:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        
       
        return count  

    def countLeafNode_Recursive(self,root):
        #Recursive way
        if root is None:
            return 
        if root.left is None and root.right is None:
            return 1
        return self.countLeafNode_Recursive(root.left)+self.countLeafNode_Recursive(root.right) 


    def countNonLeafNodes(self, root): #using preorder approach 
        if root is None:
            return 0
        if root.left or root.right:
            self.count+=1
        self.countNonLeafNodes(root.left)
        self.countNonLeafNodes(root.right)
        return self.count

    def countNonLeafNodes1(self, root): ### using 1+left+right approach
        if root is None:
            return 0
        if not root.left and not root.right:
            return 0
        return self.countNonLeafNodes1(root.left)+self.countNonLeafNodes1(root.right)+1      

    def largestAteachLevel(self,root):
        q=deque()
        q.append(root)
        y=[]
        while q:
            res=[]
            x=len(q)
            for i in range(x):    
                temp=q.popleft()
                res.append(temp.data)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            y.append(max(res))
        return y     

# Example usage
if __name__ == "__main__":
    print("Build the binary tree:")
    bt = BinaryTree()
    bt.root = bt.build_binary_tree()

    if bt.root:
        print("Preorder Traversal:", bt.preorder_traversal(bt.root))
        print("Inorder Traversal:", bt.inorder_traversal(bt.root))
        print("Postorder Traversal:", bt.postorder_traversal(bt.root))
        print("Level Order Traversal:", bt.level_order(bt.root))
        print("The size of the Tree is ",bt.getSize(bt.root))
    else:
        print("The tree is empty.")
