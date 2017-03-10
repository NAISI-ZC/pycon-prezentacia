In all previous examples, we've used RF static API. This means that robot
framework will list methods of our library and use them as a keywords.

In Dynamic API, we implement only 3 methods that will dynamically supply
information about our keywords. This is good approach if we have lot of 
helper methods, classes and we need to specify which methods should be imported
as keywords (in order to prevent keyword collisions)

There is going on lot of meta programming, so comments are included inline
with source code. Please check out `PyCoffee/src/Espresso/jar.py` for more.

