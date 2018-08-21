# Water Jug Problem

## Problem Statement:

A Water Jug Problem: You are given two jugs, a 4-gallon one and a 3-gallon
one, a pump which has unlimited water which you can use to fill the jug, and
the ground on which water may be poured. Neither jug has any measuring
markings on it. How can you get exactly 2 gallons of water in the 4-gallon jug?
State Representation and Initial State – we will represent a state of the problem as a
tuple (x, y) where x represents the amount of water in the 4-gallon jug and y
represents the amount of water in the 3-gallon jug. Note 0 ≤ x ≤ 4, and 0 ≤ y ≤ 3.
<br>
Our initial state: (0,0)
<br>
### Goal Predicate – state = (2,y) where 0 ≤ y ≤ 3.
### Operators – we must define a set of operators that will take us from one state to another:

1. Fill 4-gal jug (x,y) → (4,y)
x < 4
2. Fill 3-gal jug (x,y) → (x,3)
y < 3
3. Empty 4-gal jug on ground (x,y) → (0,y)
x > 0
4. Empty 3-gal jug on ground (x,y) → (x,0)
y > 0
5. Pour water from 3-gal jug (x,y) → (4, y - (4 - x))
to fill 4-gal jug 0 < x+y ≥ 4 and y > 0
6. Pour water from 4-gal jug (x,y) → (x - (3-y), 3)
to fill 3-gal-jug 0 < x+y ≥ 3 and x > 0
7. Pour all of water from 3-gal jug (x,y) → (x+y, 0)
into 4-gal jug 0 < x+y ≤ 4 and y ≥ 0
8. Pour all of water from 4-gal jug (x,y) → (0, x+y)
into 3-gal jug 0 < x+y ≤ 3 and x ≥ 0
<br>
Through Graph Search, the following solution is found :
<br>
capacityA = 5
<br>
capacityB = 7
<br>
Measure = 4
<br>
Jug 1 | Jug 2
----- | -----
5 | 0
0 | 0
0 | 5
5 | 5
3 | 7
0 | 3
5 | 3
1 | 7
0 | 1
5 | 1
5 | 6
0 | 6
4 | 7
0 | 4

## Additional Resources for Water jug Problem:
* [An Arithmetic Approach to the General Two Water Jugs Problem - Yiu-Kwong Man](http://www.iaeng.org/publication/WCE2013/WCE2013_pp145-147.pdf)
* [Water Jug Problem using BFS](https://www.geeksforgeeks.org/water-jug-problem-using-bfs/)