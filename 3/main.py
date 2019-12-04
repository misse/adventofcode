with open(r'3/input', 'r') as f:
    INPUT = f.read()

def calcPath(WIRE):
    PATH = {}
    X, Y, INDEX = 0, 0, 0

    DIRECTIONS = {
        'U':[0, 1],
        'D':[0, -1],
        'R':[1, 0],
        'L':[-1, 0]
    }
    for PART in WIRE:
        LENGTH = PART[1:]
        DIRECTION = PART[0]
        for STEP in range(int(LENGTH)):
            ADDITION = DIRECTIONS[DIRECTION]
            X += ADDITION[0]
            Y += ADDITION[1]
            INDEX += 1
            PATH[(X,Y)] = INDEX
        
    return PATH

def findShortestPath(INPUT):
    WIRES = [LINE.split(',') for LINE in INPUT.split('\n')]
    
    WIREPATHS = {}
    for INDEX, WIRE in enumerate(WIRES):
        WIREPATHS[INDEX] = calcPath(WIRE)
    
    INTERSECTIONS = WIREPATHS[0].keys() & WIREPATHS[1].keys()

    LEAST_STEPS = []
    CLOSEST = []
    for INTERSECTION in INTERSECTIONS:
        CLOSEST += [(abs(INTERSECTION[0]) + abs(INTERSECTION[1]))]
        LEAST_STEPS += [abs(WIREPATHS[0][INTERSECTION]) + abs(WIREPATHS[1][INTERSECTION])]

    CLOSEST = min(CLOSEST)
    STEPS = min(LEAST_STEPS)
    
    return (CLOSEST, STEPS)

print(findShortestPath(INPUT))