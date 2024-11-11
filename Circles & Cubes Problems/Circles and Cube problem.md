
## Problem setup

A cube contains a circle of diameter equal to its side length. Between the circles perimeter and the square's are 3 circles of the same size the maximum without overlapping.

![[Projects/Completed/Puzzles and Problems/Circles & Cubes Problems/Assets/Circles and Cube Problem full diagram.excalidraw]]
Zooming into one corner.
![[Projects/Completed/Puzzles and Problems/Circles & Cubes Problems/Assets/CIrcles cube problem zoom.excalidraw]]

![[Projects/Completed/Puzzles and Problems/Circles & Cubes Problems/Assets/CIrcles cube problem zoom small diamiters.excalidraw]]

### Useful Equations

### Formula for a circle


## [[2024-06-08]] @ 04:05 
Can I model this situation?
The problem is defined by the intersection of points on the perimeter of a circle ($x^{2}+y^{2} = r^{2} + O_{3x}i + O_{3y}j$) with:
- x axis ($y=0$) at only one point
	- Therefore: $x^{2} = r^{2} + O_{3x}i + O_{3y}j$
- y axis ($x = 0$) at only one point
	- Therefore: $y^{2} = r^{2} + O_{3x}i + O_{3y}j$
- the two smaller circles (at only one point each)
	- Circle 1 $C_{1}$
		- Perimeter $P_{1}$ given by $x^{2}+y^{2} = \frac{1}{2\pi}^{2} + \frac{3}{2}d_{s} \ i+ \frac{1}{2}d_{s} \ j$
		- Centre $O_{1}$ displaced by $\frac{3}{2}d_{s} \ i+ \frac{1}{2}d_{s} \ j$
	- Circle 2 $C_{2}$
		- Perimeter $P_{2}$ given by $x^{2}+y^{2} = \frac{1}{2\pi}^{2} + \frac{1}{2}d_{s} \ i+ \frac{3}{2}d_{s} \ j$
		- Centre $O_{2}$ displaced by $\frac{1}{2}d_{s} \ i+ \frac{3}{2}d_{s} \ j$

