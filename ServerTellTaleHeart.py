'''
Created on Mar 22, 2014
[YStart,BlockCount] 
[[0,1],[1,1],[2,1],[1,1],[0,1],[0,1],[0,1],[-1,1],[-2,1],[-1,5],[4,5],[9,5],[4,5],[-2,6]]
@author: chris
'''
import curses
import time
class CursesWindow(object):
    def __enter__(self):
        screen = curses.initscr()
        #curses.beep()
        curses.initscr()
        curses.noecho()
        return screen
    def __exit__(self, type, value, traceback):
        curses.echo()
        curses.endwin()
        print("Exit")
def DrawBeat(objScreen,Xcoord,LineHeight):
    heartPattern = [0,1,1,-1,-1,0,0,0,-1,-1,5,5,5,-5,-7,0,1,1,1,0,0,1,1,1,0,0,-1,-1,-1,0,0]
    Xcoord += 1
    i = 0
    LastCoord = LineHeight
    while i < len(heartPattern):
        if Xcoord >= objScreen.getmaxyx()[1]:
            Xcoord = 0
            objScreen.erase()
            objScreen.refresh()
        if heartPattern[i]==0:
            objScreen.addstr(LastCoord,Xcoord,'#')
            objScreen.refresh()
            time.sleep(.030)
        else:
            a = 0
            while a < (abs(heartPattern[i])):
                start = 0
                if heartPattern[i] > 0:
                    start= LastCoord -1
                else:
                    if((i != 0 and heartPattern[i-1] < 0) or a != 0 or (i != 0 and heartPattern[i-1] == 0)):
                        start = LastCoord + 1
                    else:
                        start = LastCoord + abs(heartPattern[i-1])
                objScreen.addstr(start,Xcoord,'#')
                objScreen.refresh()
                LastCoord = start
                a+=1
        i += 1
        Xcoord += 1
    return Xcoord
def main():
    with CursesWindow() as stdscr:
        Xcoord = 0
        LineHeight = int((stdscr.getmaxyx()[0]-1)/2)
        stdscr.addstr(LineHeight,Xcoord,"@")
        stdscr.refresh()
        while 1:
            Xcoord = DrawBeat(stdscr,(Xcoord+1),LineHeight)
        
if __name__ == '__main__':
    main()

