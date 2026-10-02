class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # condition 1
        for horizontal in range(3):
            for vertical in range(3):
                seen = set()

                for row in range(3):
                    for col in range(3):
                        if board[(3*horizontal) + row][(3*vertical) + col] == ".":
                            continue
                        if board[(3*horizontal) + row][(3*vertical) + col] in seen:
                            return False
                        seen.add(board[(3*horizontal) + row][(3*vertical) + col])
        
        # condition 2
        for horizontal in range(9):
            x_seen = set()
            for vertical in range(9):
                if board[horizontal][vertical] == ".":
                    continue
                if board[horizontal][vertical] in x_seen:
                    return False
                x_seen.add(board[horizontal][vertical])
        
        # condition 3
        for vertical in range(9):
            y_seen = set()
            for horizontal in range(9):
                if board[horizontal][vertical] == ".":
                    continue
                if board[horizontal][vertical] in y_seen:
                    return False
                y_seen.add(board[horizontal][vertical])
        
        return True

        