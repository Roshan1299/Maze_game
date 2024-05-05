import os
from copy import deepcopy 

MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'

os.system("")       # Enables ANSI escape codes in terminal
    
def clear_screen():
    """
    Clears the terminal screen.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def print_location(x, y, text):
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{1};{0}H{2}".format(x, y, text)) 
    
def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')
    
    

def load_map(map_file) :
    with open(map_file,'r') as file :
        map = file.readlines()                      #reading the file
        for x in range(len(map)) :              
            map[x] = map[x].replace('\n','')        #replacing all the'\n' by ''
        
        
        x = []
        for i in range(len(map)) :
            a = []
            for j in range(len(map[i])) :
                a.append(map[i][j])
            x.append(a)                             #you get a nested list of the map
            
        #print(x)                         
             
        return x
    
def find_start(grid) :
    for i in grid :
        if 'S' in i :
                                                    #if 'S' is in the grid, it returns the coordinates of it
            return [grid.index(i),i.index('S')]
    
def get_command(a) :
    done = False
    while not done :
        
        if a == 'escape' :
            exit()
        else : 
            print('I do not understand')
            done = False
            
def display_map(grid,player_position):
    dup_grid = deepcopy(grid)
    dup_grid[player_position[0]][player_position[1]] = '@'      #puts "@" wherever is te player
    
    for x in range(len(dup_grid)) :
        for y in range(len(dup_grid[x])):
            dup_grid[x][y] = dup_grid[x][y].replace('S','🏠')    #replacing the letters with emojis
            dup_grid[x][y] = dup_grid[x][y].replace('-','🧱')
            dup_grid[x][y] = dup_grid[x][y].replace('*','🟢')
            dup_grid[x][y] = dup_grid[x][y].replace('F','🏺')
            dup_grid[x][y] = dup_grid[x][y].replace('@','🧝')
            
    for z in range(len(dup_grid)):
        a = ''
        for f in range(len(dup_grid[z])):
            a += dup_grid[z][f]
        print(a)
        

    
def get_grid_size(grid) :
    x = len(grid)
    y = len(grid[0])

    return [x,y]

def is_inside_grid(grid, list) :
    grid_rows,grid_cols = get_grid_size(grid)
    giv_rows,giv_cols = list[0],list[1]                           #given rows and given columns
    if giv_rows >= 0 and giv_cols >= 0 and giv_rows < grid_rows and giv_cols < grid_cols: #cant be negative, if it is neg, then it will be an error since the player with be going above the map(prev row)
        return True
    else : 
        return False 
    
def look_around(grid,player_position) :     #this function tells us, all the suitable directions we can go
    allowed_objects = ('S','F','*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    
    if is_inside_grid(grid,[row - 1,col]) and grid[row - 1][col] in allowed_objects :   #north would mean, the row would go up, so row-1, and the column would be same
        directions.append('north')
    if is_inside_grid(grid,[row + 1,col]) and grid[row + 1][col] in allowed_objects :   #south would mean, the row would go down, so row+1, and the column would be same
        directions.append('south')
    if is_inside_grid(grid,[row,col-1]) and grid[row][col-1] in allowed_objects :   #west would mean, col would go left, so col-1, and the row would be same
        directions.append('west')
    if is_inside_grid(grid,[row,col+1]) and grid[row][col+1] in allowed_objects :   #east would mean, col would go right, so col+1, and the row would be same
        directions.append('east')
    
    return directions
        
def move(direction,player_position,grid) :      #this fucntion is used for moving around
    if direction in look_around(grid,player_position) :
        if direction == 'west' :
            player_position = [player_position[0],player_position[1]-1]         #changes position of @, by going left (col - 1)
           
            
        if direction == 'east' :
            player_position = [player_position[0],player_position[1]+1]         #changes position of @, by going right (col + 1)
            
            
        if direction == 'north' :
            player_position = [player_position[0]-1,player_position[1]]         #changes position of @, by going up (row - 1)
            
            
        if direction == 'south' :
            player_position = [player_position[0]+1,player_position[1]]         #changes position of @, by going down (row + 1)
            
            
        return True , player_position       #returns bool and current player position
    else :
        return False , player_position
        
def check_finish(grid,player_position) :
    for i in grid :
        if 'F' in i :
            finish = [grid.index(i),i.index('F')]   #gives us the position of the "F"
                                                    
    if player_position == finish :                  #if player position is same as the finish position, it returns True
        return True
    else :
        return False
        
def display_help(file):
    with open(file,'r') as file :
        return (file.read())
        
def main() :
    game_over = False
    grid = load_map(MAP_FILE)
    player = find_start(grid)
    clear_screen()
    print_location(0,1,"Maze Game")
    print_location(0,3,display_help(HELP_FILE))
    av = ''.join(look_around(grid,player))
    print_location(0,6,"You can go "+av)
    move_cursor(0,8)
    display_map(grid,player)
    #user = input()   
    while not game_over :
        # grid = load_map(MAP_FILE)
        # player = find_start(grid)
        # clear_screen()
        # print_location(0,1,"Maze Game")
        # print_location(0,2,display_help(HELP_FILE))
        # av = ''.join(look_around(grid,player))
        # print_location(0,4,"You can go "+av)
        # display_map(grid,player)
        user = input()
        #if user == "show map" :
        #    display_map(grid,player)
        #    print('You can go',', '.join(look_around(grid,player)))
        #    game_over = False
        if user.startswith('go ') :
            # clear_screen()
            # print_location(0,1,"Maze Game")
            # print_location(0,3,display_help(HELP_FILE))
            # av = ''.join(look_around(grid,player))
            # print_location(0,6,"You can go "+av)
            # move_cursor(0,8)
            # display_map(grid,player)
            direction = user.split()[1]                 #split fucntion, makes it into 2 objects in a list, and then accesses the index 1, which is direction 
            success , player = move(direction,player,grid)   #here bool as well as the current player position will be returned                   
            if check_finish(grid,player) :
                print('Congratulations! You have reached the exit!')    #when player reaches finish, this is displayed
                game_over = True 
            elif success :
                clear_screen()
                print_location(0,7,'you moved '+direction)
                print_location(0,6,'You can go '+', '.join(look_around(grid,player))) #it shows all the suitable directions we can go
                print_location(0,1,"Maze Game")
                print_location(0,3,display_help(HELP_FILE))
                av = ''.join(look_around(grid,player))
                #print_location(0,6,"You can go "+av)
                move_cursor(0,9)
                display_map(grid,player)
                game_over = False
            else :
                clear_screen()
                print_location(0,7,'There is no way there.')
                print_location(0,6,'You can go '+', '.join(look_around(grid,player)))
                print_location(0,1,"Maze Game")
                print_location(0,3,display_help(HELP_FILE))
                av = ''.join(look_around(grid,player))
                #print_location(0,6,"You can go "+av)
                move_cursor(0,9)
                display_map(grid,player)
                game_over = False
                
   
        elif user == 'escape' :
            game_over = True
        
             
if __name__ ==  '__main__' :
    main()