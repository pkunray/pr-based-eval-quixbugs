from collections import deque as Queue

def breadth_first_search(startnode, goalnode):
    if startnode is None or goalnode is None:
        return False

    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            for successor in node.successors:
                if successor not in nodesseen:
                    queue.append(successor)
                    nodesseen.add(successor)

    return False


"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
