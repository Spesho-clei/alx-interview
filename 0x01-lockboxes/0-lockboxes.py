#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked
    """
    if not boxes or not boxes[0]:
        return False

    n1 = len(boxes)
    visited = [False] * n1
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        print("Visiting box:", current_box)

        for key in boxes[current_box]:
            if 0 <= key < n1 and not visited[key]:
                print("Found key to box:", key)
                visited[key] = True
                queue.append(key)
            else:
                print("Skipping key to box:", key)

    return all(visited)
