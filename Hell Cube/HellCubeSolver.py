
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

