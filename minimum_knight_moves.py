# 1197. Minimum Knight Moves
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

# Example 1:

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]

# Example 2:

# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

 

# Constraints:

#     -300 <= x, y <= 300
#     0 <= |x| + |y| <= 300



class MinimumKnightMoves:
    
    def minimum_knight_moves(self, x: int, y: int) -> int:
        if x==0 and y==0:
            return 0
        x = abs(x)
        y = abs(y)
        visited = set()
        possible_moves = [(-2, -1), (-2, 1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
        queue = [(0,0)]
        moves = 0
        
        while queue:
            size = len(queue)
            for i in range(size):
                newX, newY = queue.pop(0)
                if newX == x and newY == y:
                    return moves
                for x1, y1 in possible_moves:
                    move = (newX+x1, newY+y1)
                    if move not in visited and move[0] >= -2 and move[1] >= -2:
                        queue.append(move)
                        visited.add(move)
            moves += 1
        return -1


if __name__ == '__main__':
    obj = MinimumKnightMoves()
    print(obj.minimum_knight_moves(x=2, y=1))
        