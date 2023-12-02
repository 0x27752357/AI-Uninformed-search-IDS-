import turtle, sys, math, random, time

grid = []

with open("Test Case/test_case_3.txt", 'r') as file:
    first_line = file.readline().strip()

    for line in file:
        line = list(line)
        if '\n' in line: 
            line.pop()
        grid.append(line)
    
    print(grid)

file.close()

first_line = first_line.split(',')
rows = int(first_line[0])
cols = int(first_line[1])

grid = grid[:rows]


t = turtle.Turtle()
cellHeight = 10
cellWidth = 10
print("Rows", rows)
print("Columns", cols)
goal = None
start = None
neighbors = {}
visited = []
t.speed(0)
path = []


def main(visited):
    colorgrid()
    for l in range(100):
        start_time = time.time()
        val = DLS(start, goal, l, visited)
        if val is not False:
            print(l + 1, " Steps")
            draw_path(val)
            break
        else:
            visited = []
    print("Time:", time.time() - start_time)
    turtle.mainloop()
    print("END---------------------------------------------")

main_way = []

def colorgrid():
    for x in range(rows):
        for y in range(cols):
            add_neighbors(x, y)

            if (x, y) == start:
                draw_filled_rect(x, y, "blue")  # Start point in blue
            elif (x, y) == goal:
                draw_filled_rect(x, y, "green")  # Goal point in green
            elif grid[x][y] == '-':
                draw_filled_rect(x, y, "white")  # Ways in white
            elif grid[x][y] == '%':
                draw_filled_rect(x, y, "black")  # Walls in black


def add_neighbors(x, y):
    curr_key = (x, y)
    list_of_neighbors = []

    if y < cols - 1 and grid[x][y + 1] != '%':
        list_of_neighbors.append((x, y + 1))
    if x < rows - 1 and grid[x + 1][y] != '%':
        list_of_neighbors.append((x + 1, y))
    if y > 0 and grid[x][y - 1] != '%':
        list_of_neighbors.append((x, y - 1))
    if x > 0 and grid[x - 1][y] != '%':
        list_of_neighbors.append((x - 1, y))

    copy = []
    for neighbor in list_of_neighbors:
        if curr_key in neighbors:
            neighbors.setdefault(curr_key, []).append(neighbor)
        else:
            neighbors[curr_key] = [neighbor]
            copy.extend(neighbors[curr_key])


def draw_filled_rect(x, y, color):
    t.up()
    t.goto(y * cellWidth, -x * cellHeight)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(4):
        t.forward(cellWidth)
        t.left(90)
    t.end_fill()
    t.up()
    
    
def draw_path(val):
    current = start
    t.pensize(2)
    t.pencolor("red")
    t.speed(1)

    movements = val.split(',')
    for move in movements:
        x, y = map(int, move.split(':'))
        if current[0] < x:
            t.goto((current[1] + 1) * cellWidth, -current[0] * cellHeight)
            t.pendown()
            t.goto((y + 1) * cellWidth, -x * cellHeight)
            t.penup()
        elif current[0] > x:
            t.goto((current[1] + 1) * cellWidth, -current[0] * cellHeight)
            t.pendown()
            t.goto((y + 1) * cellWidth, -x * cellHeight)
            t.penup()
        elif current[1] < y:
            t.goto((current[1] + 1) * cellWidth, -current[0] * cellHeight)
            t.pendown()
            t.goto((y + 1) * cellWidth, -x * cellHeight)
            t.penup()
        elif current[1] > y:
            t.goto((current[1] + 1) * cellWidth, -current[0] * cellHeight)
            t.pendown()
            t.goto((y + 1) * cellWidth, -x * cellHeight)
            t.penup()

        current = (x, y)

    t.hideturtle()



def DLS(start_state, goal, depth, visited):
    visited.append(start_state)
    draw_filled_rect(start_state[0], start_state[1], "blue")

    if start_state == goal:
        print(depth)
        draw_filled_rect(goal[0], goal[1], "green")
        print("End can be reached")
        return str(start_state[0]) + ":" + str(start_state[1])
    elif depth == 0:
        return False
    else:
        val = False
        for neighbor in neighbors[start_state]:
            if neighbor not in visited and val is False:
                val = DLS(neighbor, goal, depth - 1, visited)
        if val is not False:
            draw_filled_rect(start_state[0], start_state[1], "green")
            main_way.append([start_state[0], start_state[1]])
            return val + "," + str(start_state[0]) + ":" + str(start_state[1])
        return False

def correct_way(main_way): 
    main_way = main_way[::-1]
    print(main_way)
    ways = []
    for tp in range(len(main_way) - 1) : 
        if main_way[tp][0] < main_way[tp+1][0] : 
            ways.append("D")
        elif main_way[tp][0] > main_way[tp+1][0] : 
            ways.append("U")
        elif main_way[tp][1] > main_way[tp+1][1] :
            ways.append("L")
        elif main_way[tp][1] < main_way[tp+1][1] : 
            ways.append("R")  
    return ways
        
             

if __name__ == "__main__":
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    main(visited)
    ways = correct_way(main_way)
    print(ways)
