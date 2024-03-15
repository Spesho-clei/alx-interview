#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    # Initialize a set to keep track of opened boxes
    opened = set()
    opened.add(0)  # The first box is always unlocked initially

    # Initialize a queue for BFS
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        # Check all the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and we haven't opened it yet
            if key < len(boxes) and key not in opened:
                opened.add(key)
                queue.append(key)

    # If all boxes have been opened, return True
    return len(opened) == len(boxes)
