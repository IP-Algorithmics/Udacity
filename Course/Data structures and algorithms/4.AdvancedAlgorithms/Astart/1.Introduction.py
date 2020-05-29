'''
https://youtu.be/pHySYq-wghU
What Is A Problem? https://youtu.be/gepUYmWERZA
Example: Route Finding https://youtu.be/5lrkPKQwOFE
Note here that we're only looking at how many "steps", or nodes visited, we have to take to go from one node to another. The paths also show a cost value, but we're ignoring those for now.

Uniform Cost Search https://youtu.be/oPe45CJ_o0k
Uniform Cost Search 1 https://youtu.be/rTddvJ0qd6c
Uniform Cost Search 2 https://youtu.be/QSjh-ypUhto
Uniform Cost Search 3 https://youtu.be/bEfXeDfoIY8
Uniform Cost Search 4 https://youtu.be/zpOf15umlkE
Uniform Cost Search 5 https://youtu.be/MoyBcrw-n_M
Now that we've added quite a few paths to our map, it can be a bit difficult to follow which paths are being checked at each step.
Starting at 1:30, we are checking the path coming into Craiova from Rimnicu Vilcea, and heading toward either Drobeta (366+120 = 486) or Pitesti (366+318 = 504), both of which are worse than our current best of 418.
After that, we already know the path to get to Drobeta was worse than the path to get to Craiova, so there cannot be a more beneficial path heading to that already explored location.


On Uniform Cost https://youtu.be/8xH-3WtswDs
Uniform Cost search - expands out equally in all directions, may expend additional effort getting to a fairly direct path to the goal.
Greedy best-first search - expands outward toward locations estimated as closer to the goal. If a direct path is available, expends much less effort than Uniform Cost; however, it does not consider any routes in which it may need to temporarily take a further away path in order to arrive at an overall shorter path.
A* Search - utilizes both of these - will try to optimize with both the shortest path and the goal in mind. We'll see how this works in the next video.

A* Search https://youtu.be/HNdOFYCtfu4 https://youtu.be/_cPSOQ-sC2k
A* Search 1 https://youtu.be/yMUqkCzFXts https://youtu.be/pfSya9ScozE
A* Search 2 https://youtu.be/gYKBDz2kQJ8 https://youtu.be/kvDVL4G_njI
A* Search 3 https://youtu.be/DRreaZXn72E https://youtu.be/Njd5k_I6Sqo
A* Search 4 https://youtu.be/B_rOIxwLzr8
A* Search 5 https://youtu.be/7d4iHfJXPso
'''
