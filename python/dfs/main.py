class linkedlist:

    def __init__(self,c,v):
        self.child=c
        self.val=v
        self.visited=0

    def get_child(self):
        return self.child

    def get_val(self):
        return self.val

    def get_visited(self):
        return self.visited

    def set_visited(self):
        self.visited=1

    def add_child(self,child):
        self.child.append(child)

def dfs(root):
    if root.get_visited()==1:
        print(root.val)
        return

    root.set_visited()


    for node in root.get_child():
        dfs(node)

    print(root.val)

def node_exists(val,nodes):
    for n in nodes:
        if n.get_val()==val:
            return n
    return None


print("HERE IS AN APP TO RUN DFS ALGORITHM !")
print("==============================================")
print("enter the number od nodes")
num=int(input())
print("start entering edges . enter the edges between the ith elemnt and other nodes in the ith line . ")

nodes=[]
for counter in range(1,num+1):
    tmp = input()
    children=[]
    if tmp.__contains__(" "):
        children = map(int, tmp.split(" "))
    elif tmp!="":
        children.append(int(tmp))

    current = node_exists(counter,nodes)
    if current==None :
        current=linkedlist([],counter)
        nodes.append(current)


    for cc in children:
        child=node_exists(cc,nodes)
        if child==None:
            child = linkedlist([], cc)
            nodes.append(child)
        current.add_child(child)

print("enter start node for DFS")
start=int(input())
dfs(node_exists(start,nodes))

