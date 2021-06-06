# simpleAStarImplementationPathFinding
This is a simple Path Finding Algorithm
I am not sure if this is exactly A* because I never looked up any A* implementations
This path finding is entirely based on my interpretation of Computerphile's video on A* so I mighth have missed a few important aspects of the real A* algorithm
but this implementation seems to do its job pretty well as it finds the best path (or one of the best paths) from start to finish with a random map.
I am most proud of this project because I have not at all used any help on the path finding algorithm and its completely based on my understanding of computerphile's
video so I am very very very very very proud of that.

A few key notes:

My "random" map is not really a proper map. I have just used a random number generator to give a probability (0.3) for each cell to be a wall. So basically 30%
of the map (roughly) will be a wall and randomly placed so it does NOT ensure a path is possible from start to finish. To overcome this, I just made a while loop which
re-makes a map if a path is not possible and basically just re-runs the whole program. So if you windows opens and closes quickly its because there was no path form 
start to finish and its re-making the map and it will run again until it finds a map that has a possible path.

Diagonals are not vaible neighbours. A next edition to this project would be to add diagonals with the path cost of roughly Sqrt(2) instead of the path length 1 I am
using right now.

The method called gridPrint() is absolete now that I have added a gui but initially it was my way of checking if the program worked. Its still in there for when
I make tweaks so that I can check my work

I am relatively new to python and did not realize that somehow my variables in my main method seem to be accesable from any of the other methods for some reason, but
even still I supplied them as parameters for the functions just for my sake and keeping my sanity. 

The Node class has unnecessary getter methods since I can just access the objects values but I just did that also for my own sanity

The random location of the ending spot is limited to outside a rectangle of width 20 and heigh 10 just so that the path isnt too short. So the end particle will
always be outside that rectangular region

For a denser map, just increase the probability of having a 1 on the board (currenlty at 30%). 

When running be careful not to click on the gui too much because it might freeze it. I used tkinter in a way that was just convinient and ignored all proper ways of
doing gui stuff. I do not know exactly how the gui works so its just a hot mess and all over the place.

I also realize now that I have quite a few redunduncies but I cannot bother going back to fix them because I don't care too much for wasted memory as it gets cleared 
soon enough. 

I do not know if python has a nice way of using a Priority Queue, I do not quite know what a Priority Queue really is, but it just sounds like a sorted list
for the most part so that is what I have been using and it seems to work just fine. 

In the distance function, there might seem to be a random factor of 10 which is multiplied by the euclideian distance. This factor is to prioritize searching in the direction of the end goal. The more you increase this scalar constant, the more it prioritizes the direction rather than the raw path length. If you make this constant 0, you will just get an undirected search which is the same as dijkstra's algorithm. For a randomly generated map like this one, it is probably better to have a large constant (10 works well enough). If you really want to see the difference, make that constant 0 or 1 and then compare it to when the constant in 10 or higher. There is a significant difference in the runtime. Now there are certain graphs where a low constant value is desired but that can be a future avenue to explore. 
