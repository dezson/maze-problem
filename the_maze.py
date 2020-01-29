def the_maze(maze, start, dest):
    """
    :type maze: list(list)
    :type start: tuple(int, int)
    :type dest: tuple(int,int)
    """
    
    def dfs(maze, current_x, current_y, dest, visited):
        current = (current_x, current_y) 
        if current_x >= 0 and current_x < len(maze) and current_y >= 0 and current_y < len(maze[0]):
        
            if maze[current_x][current_y] == 1: return False
            if visited[current_x][current_y] == True: return False
            
            if current == dest:
                return True
                
            visited[current_x][current_y] = True
            
            return dfs(maze,current_x+1, current_y, dest, visited) or \
                     dfs(maze,current_x-1, current_y, dest, visited) or \
                     dfs(maze,current_x, current_y+1, dest, visited) or \
                     dfs(maze,current_x, current_y-1, dest, visited)    
                
        return False                                              
                    

    visited = [[False for i in range(len(maze[1]))] for j in range(len(maze))]
    curr_x, curr_y = start
        
    return dfs(maze, curr_x, curr_y, dest, visited)
    

# Example 1
maze_1 = [[0,0,1,0,0],
          [0,0,0,0,0],
          [0,0,0,1,0],
          [1,1,0,1,1],
          [0,0,0,0,0]]   

start_1= (0,0)
dest_1 = (4,4)
print(the_maze(maze_1, start_1, dest_1)) # -> True


# Example 2
maze_2 = [[0,1,1,0,0],
          [0,0,0,0,0],
          [1,1,1,1,0],
          [0,1,1,1,0],
          [0,0,0,0,0]]

start_2 = (0,0)
dest_2 = (3,0)
print(the_maze(maze_2, start_2, dest_2)) # -> True


# Example 3
maze_3 = [[0,1,1,0,0],
          [0,0,0,0,0],
          [1,1,1,1,0],
          [0,1,1,1,0],
          [1,0,0,0,0]]

start_3 = (0,0)
dest_3 = (3,0)
print(the_maze(maze_3, start_3, dest_3)) # -> False
