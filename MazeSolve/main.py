from pyamaze import maze, agent, textLabel
from solver import *
import sys

sys.setrecursionlimit(10000)

sizex = 50
sizey = 50
m = maze(sizex, sizey)
start = (sizex, sizey)
end = (1, 1)
m.CreateMaze(end[0], end[1])


#Graph Making
mazeGraph = graph.generateGraph(m.maze_map)

#Pointer
a=agent(m,start[0],start[1], filled=True, footprints=True,color='red')
r=agent(m,start[0],start[1], filled=True, footprints=True,color='green')

#Path Making
path = solver.dfsCaller(mazeGraph, start, end)

#Counters
cellsChecked = textLabel(m, 'Cells Checked', len(solver.cPath))
cellsOnPath = textLabel(m, 'Path Cells', len(path))

#Path Drawing
m.tracePath({a:solver.cPath},delay=10)
m.tracePath({r:path},delay=10)

#Run
m.run()