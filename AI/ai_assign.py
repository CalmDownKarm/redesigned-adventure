"""AI assignment 1 demonstrate dfs, bfs, iterative deepening search on an full tree"""
found = False
def gen_left_child(parent,max_nodes): 
    """Generates the left child of the parent node """
    return 2*parent if 2*parent<=max_nodes else -1 # 2*parent<max_nodes?2*parent:-1
    #Python3 Messed up ternary operators big time

def gen_right_child(parent,max_nodes):
    """Generates Right Child"""
    return 2*parent+1 if 2*parent+1<=max_nodes else -1

def dfs(start_node, goal_node, max_nodes):
    """Runs a dfs, hint hint, it's actually depth limited to max_nodes"""
    stack = []
    visited = []
    if goal_node<=0 or start_node <=0 or max_nodes<start_node:
        print("Error")
        return
    else:
        nodes_gen = 1
        stack.append(start_node)
        while(stack):
            top = stack.pop()
            nodes_gen +=1
            visited.append(top)
            if goal_node == top:
                global found
                found = True
                print("\n Found")
                return (visited,stack)
            else:
                if gen_left_child(top,max_nodes) >-1:
                    stack.append(gen_left_child(top,max_nodes))
                if gen_right_child(top,max_nodes) >-1:
                    stack.append(gen_right_child(top,max_nodes))
    print("\n Not Found")
    return (visited,stack)    

def bfs(start_node,goal_node,max_nodes):
    """Simple BFS, again depth limited"""
    from collections import deque
    queue = deque()
    visited = []
    if goal_node<=0 or start_node <=0 or max_nodes<=start_node:
        print("Error")
        return
    else:
        nodes_gen = 1
        queue.append(start_node)
        while(queue):
            top = queue.popleft()
            nodes_gen +=1
            visited.append(top)
            if goal_node == top:
                print(len(visited))
                print(len(queue))
                return visited
            else:
                if gen_left_child(top,max_nodes) >-1:
                    queue.append(gen_left_child(top,max_nodes))
                if gen_right_child(top,max_nodes) >-1:
                    queue.append(gen_right_child(top,max_nodes))
    
    print("\n Not Found")
    
    return (visited,queue)

def depth_limited_search(start_node,goal_node):
    """You never actually need to implement this function, just call dfs with different values of max nodes"""
    # Since we have an implicit tree, regular dfs will never terminate. 
    dlsvisited = dfs(start_node,goal_node,(2**3)-1)[0]
    dlsstack = dfs(start_node,goal_node,(2**3)-1)[1]
    print(dlsvisited)
    print("\n Visited: "+repr(len(dlsvisited)))
    print("Total Generated including visisted"+repr(len(dlsstack)+len(dlsvisited))) 
    return dfs(start_node,goal_node,(2**3)-1)

def iterative_deepening_search(start_node,goal_node):
    """Just call on all values of max_node"""
    global found
    found = False
    visitedstack = [dfs(start_node,goal_node,(2**max_node)-1)[0] for max_node in range(1,15) if not found]
    stacktotals = [dfs(start_node,goal_node,(2**max_node)-1)[1] for max_node in range(1,15) if not found]
    print(visitedstack)
    print(stacktotals)
    totalvisited = sum([len(x) for x in visitedstack])
    totalgenerated = sum([len(x) for x in stacktotals])+totalvisited
    print("\n Visited : "+repr(totalvisited))
    print("\n Total Generated including visited" + repr(totalgenerated))
    return visitedstack
# print("DFS")
# print(dfs(1,7,15))
# print("BFS")
# print(bfs(1,10,15))
print("DLS")
depth_limited_search(1,6)
# print(depth_limited_search(1,6))
import pprint
print("IDS")
iterative_deepening_search(1,7)
# pprint.pprint())