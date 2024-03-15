#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    keys = set(boxes[0])
    opened = {0}

    # Perform BFS starting from the first box
    queue = [0]
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in opened:
                keys |= set(boxes[key])
                opened.add(key)
                queue.append(key)

    return len(opened) == n
