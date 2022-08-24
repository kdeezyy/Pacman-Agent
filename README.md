# Pacman Ai

An implementation of UC Berkeley's Pacman AI project from their CS188 AI Learning class. The game/pacman
gui was given by the class but the features implemented by me are listed below.

### Features Implemented in Project:

Depth First Search

Breadth First Search

A-Star Search



# Screenshots
### Depth First Search
![pacman image 1](https://user-images.githubusercontent.com/39201070/186384779-2ceeae6b-1f1c-4995-80be-c1dbf9c92647.PNG)
### Breadth First Search
![pacman image 2](https://user-images.githubusercontent.com/39201070/186385044-3dde07ac-6a1d-4846-a97f-976b5b43cee4.PNG)

### A* Search 
![pacman image 3](https://user-images.githubusercontent.com/39201070/186385475-846dd077-9ec2-4b7b-a91f-f2b7b75a5bdb.PNG)

### A* Search for a four corners problem
![image](https://user-images.githubusercontent.com/39201070/186385601-9b1a3912-7697-43f8-8224-1679a2bef211.png)


# Getting Started
```
git clone https://github.com/kdeezyy/Pacman-Agent.git
cd Pacman-Agent
```

# Running Tests

### DFS
```
python pacman.py -l tinyMaze -p SearchAgent

python pacman.py -l mediumMaze -p SearchAgent

python pacman.py -l bigMaze -z .5 -p SearchAgent
```

### BFS
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

### A* Search
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### A* Search 4-Corners
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

# Implemented With
#### Python
