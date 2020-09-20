import curses
import random

curses.initscr()

win = curses.newwin(24,70,0,0)
win.border(0)
curses.noecho()
curses.curs_set(0)
win.keypad(1)
win.nodelay(1)
win.timeout(100)

score = 0

snake = [[12,13],[12,14],[12,15]]

food = [20,20]
win.addch(food[0],food[1],'$')

key = curses.KEY_LEFT

win.addstr(0, 30, 'Snake Game!!')

while True:
    win.addstr(0, 3, '点数: ' + str(score) + ' ')                                  
    win.timeout(100)

    newKey = win.getch()

    if newKey not in [curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_UP,curses.KEY_DOWN]:
        key = key

    else:
        key = newKey

    if snake[0][0] == 0 or snake[0][0] == 23 or snake[0][1] == 0 or snake[0][1] == 69:
        break

    if snake[0] in snake[1:]:
        break

    newHead = [snake[0][0],snake[0][1]]

    if key == curses.KEY_DOWN:
        newHead[0] += 1
    if key == curses.KEY_UP:
        newHead[0] -= 1
    if key == curses.KEY_LEFT:
        newHead[1] -= 1
    if key == curses.KEY_RIGHT:
        newHead[1] += 1

    snake.insert(0,newHead)

    if snake[0] == food:
        score += 1
        food = []
        food = [random.randint(1,22),random.randint(1,68)]
        win.addch(food[0],food[1],'$')

    else:
        tail = snake.pop()
        win.addch(tail[0],tail[1],' ')
    win.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)

print ('Score: '+str(score))
curses.endwin()