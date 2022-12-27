from pyamaze import maze, agent, textLabel
from solver import *

m = maze()
m.CreateMaze()

#Counters
cellsChecked = textLabel(m, 'Cells Checked', 0)
cellsOnPath = textLabel(m, 'Path Cells', 0)

#Graph Making
mazeGraph = graph.generateGraph(m.maze_map)
print(mazeGraph)

#Path Making


#Pointer
a=agent(m, filled=True, footprints=True,color='red')

#Path Drawing
m.tracePath({a:m.path},delay=50)

#Run
m.run()