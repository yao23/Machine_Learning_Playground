class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=6lH4nO3JfLk&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=27

        https://github.com/neetcode-gh/leetcode/blob/main/python/0909-snakes-and-ladders.py
        
        beats 75.21%
        """
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c 
            return [r, c]

        q = deque()
        q.append([1,0]) # [square, moves]
        visit = set()
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1
