def isValidSudoku(self, board: List[List[str]]) -> bool:
    hashmap = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                continue
            if board[i][j] not in hashmap:
                hashmap[board[i][j]] = [(i,j)]
            else:
                if not valid(hashmap[board[i][j]], i, j):
                    return False
                hashmap[board[i][j]].append((i,j))
    return True

def valid(prev_occurences, i, j):
    for x, y in prev_occurences:
        if x == i or y == j:
            return False
        if checkforboxes(x, y, i, j):
            return False
    return True

def checkforboxes(x, y, i, j):
    if not ((0 <= abs(x - i) < 3) and (0 <= abs(y - j) < 3)):
        return False
    if ((x - 3) * (i - 3) < 0) or ((x - 6) * (i - 6) < 0):
        return False
    if (x == 3 and i < 3) or (x < 3 and i == 3):
        return False
    if (x == 6 and i < 6) or (x < 6 and i == 6):
        return False
    if ((y - 3) * (j - 3) < 0) or ((y - 6) * (j - 6) < 0):
        return False
    if (y == 3 and j < 3) or (y < 3 and j == 3):
        return False
    if (y == 6 and j < 6) or (y < 6 and j == 6):
        return False
    return True
