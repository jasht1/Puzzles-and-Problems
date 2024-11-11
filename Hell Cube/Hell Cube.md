# Hell Cube

## Project Proposal
%%[[2024-09-13]] @ 10:57%%

I was given a [[Hell Cube]] to solve by my long time friend [[Rosemary]]. Over a weekend I spent what probably amounts to several hours trying to solve it intuitively with what feels like negligible progress. 

%%[[2024-09-13]] @ 11:00%%

I think it should be possible to write a simple python script to find the solution.

I wonder if wave function collapse would be useful.

## Constraints
%%[[2024-09-13]] @ 11:10%%

I must begin by defining the constraints to the problem.

### Solution space

Blocks have 1 of 2 forms differentiated by whether their connected faces are opposite or perpendicular.

blocks may be in one of 4 rational states.

### Continuity

Block faces that are connected must be facing each other.

The relative positions of a given blocks connected faces are immutable.

The order of blocks is immutable.

Blocks cannot exist 2ce.

### Targets

All blocks must exist within $\left[\begin{matrix} 0 \pm 1 \\  0 \pm 1 \\ 0 \pm 1 \end{matrix}\right]$ 

## Preliminary assumptions
%%[[2024-09-13]] @ 11:51%%

The second block will be the centre 

therefore the first block will be the centre of the top face by arbitrary definition.



## Possible Approaches
%%[[2024-09-13]] @ 12:08%%

### Path finding inside a cube
%%[[2024-09-13]] @ 12:09%%

[[HellCubeSolver.py]]

#### Codifying paths
%%[[2024-09-13]] @ 19:14%%

Points $P$ in the space will be stored in len 3 int arrays storing coordinates `[x,y,z]` each of which can take on values $x,y,z \in -1,0,1$.

Paths are simply then a list of points.

#### Assumptions
%%[[2024-09-13]] @ 12:09%%

A path through a $3*3*3$ space must be found that visits every point only once. 

Apart from steps `[6,8,20,22]`, it must move in a different direction than in its previous step.

The path will begin centre left, dead centre, centre bottom. 

When it reaches 26 steps the solution is found.

```python
connected_face_is_parralell = [5,7,19,21];
path = [[-1,0,0],[0,0,0],[0,-1,0]];
step = 2;
```
#### Core logical loop
%%[[2024-09-13]] @ 12:11%%

At any step with multiple remaining viable next steps is treated as a checkpoint.
From this checkpoint it will make an arbitrary decision and follow it until reaching a point were there are no possible next steps at which point it returns to the previous checkpoint and takes a different decision. 

```python
checkpoints = []
while step < 26 :
    if step in connected_face_is_parralell:  # Check if on a parralell block
        next_steps = parralellStep(path)
    else:
        next_steps = perpendicularSteps(path)

    if len(next_steps) > 1:
        checkpoints.append([path.copy(),next_steps[1:].copy()])
    if len(next_steps) >= 1:
        path.append(next_steps[0])
        step = step + 1 
    elif len(next_steps) == 0:
        path = checkpoints[-1][0].copy()
        step = len(path)
        path.append(checkpoints[-1][1][0])
        del checkpoints[-1][1]
        if len(checkpoints[-1]) == 1:
            del checkpoints[-1]
```

#### Determining possible next steps (perpendicular)
%%[[2024-09-13]] @ 19:14%%

The relevant [[#Constraints]] for this step are:

- It must move only 1 step and in only 1 direction.
- It must move in a different direction than in its previous step.
- It must not visit the same point 2ce
- It must not leave the bounds $P \begin{pmatrix} x\\y\\z \end{pmatrix} = \left[\begin{matrix} 0 \pm 1 \\  0 \pm 1 \\ 0 \pm 1 \end{matrix}\right]$ 

Steps can be found as the previous point - the current point, this will give a len 3 array for `[x,y,z]` where 2 entries will always be 0 and one will be $\pm 1$. 

The list of all reachable points in the next step can be found as the points in the solution space $P \begin{pmatrix} x\\y\\z \end{pmatrix} = \left[\begin{matrix} 0 \pm 1 \\  0 \pm 1 \\ 0 \pm 1 \end{matrix}\right]$ bordering the current point $P(i)$ in the 2 dimensions not changed in the previous step in other words $\text{for 0s in } P(i)-P(i-1)$ 

```python
def perpendicularSteps(path):
    current_point = path[-1]
    previous_point = path[-2]

    previous_step = list(map(lambda a,b:a-b, current_point,previous_point))

    reachable_points = []

    for dimension in range (3):  # Consider the 3 avaliable dimensions
        if previous_step[dimension] != 0:  # The dimension of travel of the previous step will not change
            continue

        else:
            if current_point[dimension] == 0:  # if it is in the centre it could move to either edge
                point_up = []
                point_down = []

                for point_coordinate in range(3):
                    if point_coordinate == dimension:
                        point_up.append(1)
                        point_down.append(-1)
                    else:
                        point_up.append(current_point[point_coordinate])
                        point_down.append(current_point[point_coordinate])

                reachable_points.append(point_up)
                reachable_points.append(point_down)

            elif current_point[dimension] != 0:  # if it is on the edge it can only move to the centre
                point = []
                for point_coordinate in range(3):
                    if point_coordinate == dimension:
                        point.append(0)
                    else:
                        point.append(current_point[point_coordinate])

                reachable_points.append(point)


    next_steps = []

    for point in reachable_points:
        if point not in path:  # If the point has already been visited it is not a viable next step
            next_steps.append(point)

    return next_steps
```

#### Parallel steps
%%[[2024-09-13]] @ 19:32%%

Parallel steps are simply a repeat of the previous step.

```python
def parralellStep(path):
        current_point = path[-1]
        previous_point = path[-2]

        previous_step = list(map(lambda a,b:a-b, current_point,previous_point))

        next_point = list(map(lambda a,b:a+b, current_point,previous_step))

        if all(coordinates in [-1,0,1] for coordinates in next_point) and (next_point not in path):  # if viable allow step
            next_steps = [next_point]
        else:
            next_steps = []

        return next_steps
```

#### Changes
%%[[2024-09-15]] @ 14:03%%

One of the issues that kept biting me during this was my miss understanding of the append function. I assumed it would copy the contents of the list from it's pointer but it instead appends the pointer to the list which of course changes if the list is updated down the line. A simple fix using the `copy()` method.

I also tried a few different methods for the small vector math operations, It didn't seem worth using something like numpy for such a short vector I settled on a [[Lambda Calculus]] implementation based on [this post](https://stackoverflow.com/a/68597489).

The assumptions I made in [[#Preliminary assumptions]]:
![[#Preliminary assumptions]]

That gave me the initial path mentioned in [[#Assumptions]]:
![[#Hell Cube#Possible Approaches#Path finding inside a cube#Assumptions]]

must have been wrong as the program would just run into a dead end. I tried some different starting path assumptions and the second one I tried:
	`path = [[-1,1,-1],[-1,1,0]];`
worked a treat.

#### Conclusions
%%[[2024-09-15]] @ 14:17%%

![[Hell Cube Solved.png|300]]
In total the program explores 1331 branches and tries 4003 steps. 

It could certainly be allot more elegant, I would be interested in seeing if an A** or depth first search algorithm would be more effective. I was also hoping to give a wave function collapse method a go. 

This method has given me an/the answer and was a good exercise in and of itself.

![[Hell Cube solution.png]]

#### full code

```python
def perpendicularSteps(path):
    current_point = path[-1]
    previous_point = path[-2]

    previous_step = list(map(lambda a,b:a-b, current_point,previous_point))

    reachable_points = []

    for dimension in range (3):  # Consider the 3 avaliable dimensions
        if previous_step[dimension] != 0:  # The dimension of travel of the previous step will not change
            continue

        else:
            if current_point[dimension] == 0:  # if it is in the centre it could move to either edge
                point_up = []
                point_down = []

                for point_coordinate in range(3):
                    if point_coordinate == dimension:
                        point_up.append(1)
                        point_down.append(-1)
                    else:
                        point_up.append(current_point[point_coordinate])
                        point_down.append(current_point[point_coordinate])

                reachable_points.append(point_up)
                reachable_points.append(point_down)

            elif current_point[dimension] != 0:  # if it is on the edge it can only move to the centre
                point = []
                for point_coordinate in range(3):
                    if point_coordinate == dimension:
                        point.append(0)
                    else:
                        point.append(current_point[point_coordinate])

                reachable_points.append(point)


    next_steps = []

    for point in reachable_points:
        if point not in path:  # If the point has already been visited it is not a viable next step
            next_steps.append(point)

    return next_steps

def parralellStep(path):
        current_point = path[-1]
        previous_point = path[-2]

        previous_step = list(map(lambda a,b:a-b, current_point,previous_point))

        next_point = list(map(lambda a,b:a+b, current_point,previous_step))

        if all(coordinates in [-1,0,1] for coordinates in next_point) and (next_point not in path):  # if viable allow step
            next_steps = [next_point]
        else:
            next_steps = []

        return next_steps

connected_face_is_parralell = [5,7,19,21];

path = [[-1,1,-1],[-1,1,0]];
step = 1;

iters = 0;
branches = 0;

checkpoints = []
while step < 26 :
    iters = iters +1
    if step in connected_face_is_parralell:  # Check if on a parralell block
        next_steps = parralellStep(path)
    else:
        next_steps = perpendicularSteps(path)

    if len(next_steps) > 1:
        checkpoints.append([path.copy(),next_steps[1:].copy()])
    if len(next_steps) >= 1:
        path.append(next_steps[0])
        step = step + 1 
    elif len(next_steps) == 0:
        path = checkpoints[-1][0].copy()
        step = len(path)
        path.append(checkpoints[-1][1][0])
        branches = branches+1
        del checkpoints[-1][1]
        if len(checkpoints[-1]) == 1:
            del checkpoints[-1]

for point in path:
    print (point)
```
