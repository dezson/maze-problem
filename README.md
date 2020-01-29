# maze-problem
:question: Maze solving algorithm using DFS


# How do you solve a maze?

DFS is a common way to approach solving maze-like problems. First we selec a path in the maze and we follow it until we hit a dead end or reach the finishing point of the maze. If a given path
doesn't work, we backtrack and take an alternative path from a past junction, and try that path.

Analysis:
Time complexity: O(|V| + |E|)
Space complexity: O(|V|)
