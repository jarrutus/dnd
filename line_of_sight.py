def check_if_visible(map, initiator, target):
    """Takes in the current map, initiator and target. Checks if person at initiator coordinates can see target, calculated from center to center."""
    initiator[0] = int(initiator[0])
    initiator[1] = int(initiator[1])
    target[0] = int(target[0])
    target[1] = int(target[1])
    diff_x = abs(target[0] - initiator[0])
    diff_y = abs(target[1] - initiator[1])
    direction = check_direction(initiator, target, diff_x, diff_y)
    angle = calculate_angle(diff_x, diff_y)
    path = get_path(map, initiator, target, direction, angle)
    print(path) # For testing purposes
    confirmation = check_path(path)
    return confirmation

def check_direction(initiator, target, diff_x, diff_y):
    """Takes the location of initiator and target, returns a (integer) value between 0 and 15 for further use in check_if_visible."""
    if target[0] > initiator[0]: #If target is to the east of initiator.
        if target[1] == initiator[1]: #Both are on same row.
            direction = 0
        elif target[1] > initiator[1]: #Target is SE.
            if diff_x == diff_y: #Directly SE.
                direction = 2
            elif diff_x > diff_y: #SEE
                direction = 1
            elif diff_y > diff_x: #SSE
                direction = 3
        elif target[1] < initiator[1]: #NE
            if diff_x == diff_y: #Directly SE
                direction = 14
            elif diff_x > diff_y: #NEE
                direction = 15
            elif diff_y > diff_x: #NNE
                direction = 13
    elif target[0] < initiator[0]: #If target is to the west of initiator.
        if target[1] == initiator[1]: #Both are on same row.
            direction = 8
        elif target[1] > initiator[1]: #Target is SW.
            if diff_x == diff_y: #Directly SE.
                direction = 6
            elif diff_x > diff_y: #SWW
                direction = 7
            elif diff_y > diff_x: #SSW
                direction = 5
        elif target[1] < initiator[1]: #NW
            if diff_x == diff_y: #Directly NW
                direction = 10
            elif diff_x > diff_y: #NWW
                direction = 9
            elif diff_y > diff_x: #NNW
                direction = 11
    elif target[0] == initiator[0]: #Both in same column
        if target[1] > initiator[1]: #Target is South
            direction = 4
        elif target[1] < initiator[1]: #Target is North
            direction = 12
    else:
        print("Something went wrong.")
        direction = 0
        
    return direction

def calculate_angle(diff_x, diff_y):
    """Calculates the value of angle multiplier between two points."""
    x = diff_x
    y = diff_y
    angle = min(x, y) / max(x, y)
    return angle

def get_path(map, initiator, target, direction, angle):
    """Takes the battleground map, initiator and target coordinates, direction and angle of the line. Returns an array of tiles to check."""
    path = []
    #Starting coordinates for the path
    added_x = initiator[0]
    added_y = initiator[1]
    # Calculate what tiles need to be added to the array
    if direction in [0,4,8,12]: # One of the cardinal directions
        if direction == 0: #Direct line to East
            while added_x < target[0]:
                added_x += 1
                tile = map[added_y][added_x]
                path.append(tile)
        elif direction == 8: #Direct line to West
            while added_x > target[0]:
                added_x -= 1
                tile = map[added_y][added_x]
                path.append(tile)
        elif direction == 4: #Direct line to South
            while added_y < target[1]:
                added_y += 1
                tile = map[added_y][added_x]
                path.append(tile)
        elif direction == 12: #Direct line to North
            while added_y > target[1]:
                added_y -= 1
                tile = map[added_y][added_x]
                path.append(tile)
    elif direction in [2,6,10,14]: #NE,NW,SW or SE
        if direction == 2: #SE
            while added_x < target[0]:
                added_x += 1
                added_y += 1
                tile = map[added_y][added_x]
                path.append(tile)
        elif direction == 6: #SW
            while added_x > target[0]:
                added_x -= 1
                added_y += 1
                tile = map[added_y][added_x]
                path.append(tile)
        elif direction == 10: #NW
            while added_x > target[0]:
                added_x -= 1
                added_y -= 1
                tile = map[added_y][added_x]
                path.append(tile)
        elif direction == 14: #NE
            while added_x < target[0]:
                added_x += 1
                added_y -= 1
                tile = map[added_y][added_x]
                path.append(tile)
    elif direction in [1,3,5,7,9,11,13,15]: #The remaining directions, could have gone with else: but went with this in case there's an error.
        if direction in [1,3,9,11]:
            up_or_down = 1 # up_or_down is a way for the code to hande wheter the resulting mathematical function is growing or not.
        elif direction in [5,7,13,15]:
            up_or_down = 0
        if direction == 1: #SEE
            origo = get_origo(added_x,added_y,angle,up_or_down)
            while added_x < target[0]:
                added_x += 1
                values = calculate_line(added_x, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[values[0]][added_x]
                    path.append(tile)
                else:
                    tile1 = map[values[0]][added_x]
                    path.append(tile1)
                    tile2 = map[values[1]][added_x]
                    path.append(tile2)
        elif direction == 3: #SSE
            origo = get_origo(added_y,added_x,angle,up_or_down)
            while added_y < target[1]:
                added_y += 1
                values = calculate_line(added_y, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[added_y][values[0]]
                    path.append(tile)
                else:
                    tile1 = map[added_y][values[0]]
                    path.append(tile1)
                    tile2 = map[added_y][values[1]]
                    path.append(tile2)
        elif direction == 5: #SSW
            origo = get_origo(added_y,added_x,angle,up_or_down)
            while added_y < target[1]:
                added_y += 1
                values = calculate_line(added_y, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[added_y][values[0]]
                    path.append(tile)
                else:
                    tile1 = map[added_y][values[0]]
                    path.append(tile1)
                    tile2 = map[added_y][values[1]]
                    path.append(tile2)
        elif direction == 7: #SWW
            origo = get_origo(added_x,added_y,angle,up_or_down)
            while added_x > target[0]:
                added_x -= 1
                values = calculate_line(added_x, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[values[0]][added_x]
                    path.append(tile)
                else:
                    tile1 = map[values[0]][added_x]
                    path.append(tile1)
                    tile2 = map[values[1]][added_x]
                    path.append(tile2)
        elif direction == 9: #NWW
            origo = get_origo(added_x,added_y,angle,up_or_down)
            while added_x > target[0]:
                added_x -= 1
                values = calculate_line(added_x, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[values[0]][added_x]
                    path.append(tile)
                else:
                    tile1 = map[values[0]][added_x]
                    path.append(tile1)
                    tile2 = map[values[1]][added_x]
                    path.append(tile2)
        elif direction == 11: #NNW
            origo = get_origo(added_y,added_x,angle,up_or_down)
            while added_y > target[1]:
                added_y -= 1
                values = calculate_line(added_y, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[added_y][values[0]]
                    path.append(tile)
                else:
                    tile1 = map[added_y][values[0]]
                    path.append(tile1)
                    tile2 = map[added_y][values[1]]
                    path.append(tile2)
        elif direction == 13: #NNE
            origo = get_origo(added_y,added_x,angle,up_or_down)
            while added_y > target[1]:
                added_y -= 1
                values = calculate_line(added_y, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[added_y][values[0]]
                    path.append(tile)
                else:
                    tile1 = map[added_y][values[0]]
                    path.append(tile1)
                    tile2 = map[added_y][values[1]]
                    path.append(tile2)
        elif direction == 15: #NEE
            origo = get_origo(added_x,added_y,angle,up_or_down)
            while added_x < target[0]:
                added_x += 1
                values = calculate_line(added_x, angle, origo, up_or_down)
                if values[0] == values[1]: # If the two points are same, only add once to the array.
                    tile = map[values[0]][added_x]
                    path.append(tile)
                else:
                    tile1 = map[values[0]][added_x]
                    path.append(tile1)
                    tile2 = map[values[1]][added_x]
                    path.append(tile2)
    return path

def calculate_line(reference, angle, origo, up_or_down):
    """A sub-funtion of 'get path'. Takes in a reference point on the primary axis and the angle, returns  values A & B to check for walls."""
    point_a = reference - 0.4
    point_b = reference + 0.4
    if up_or_down == 1:
        value_a = int(round(origo + point_a * angle))
        value_b = int(round(origo + point_b * angle))
    elif up_or_down == 0:
        value_a = int(round(origo - point_a * angle))
        value_b = int(round(origo - point_b * angle))
    values = [value_a,value_b]
    return values

def get_origo(main, secondary, angle, up_or_down):
    zero = main * angle
    if up_or_down == 1: #going up
        origo = secondary - zero
    elif up_or_down == 0: #going down
        origo = secondary + zero
    return origo

def check_path(path):
    """Takes a list of tiles to check, returns 0 or 1"""
    # Later on, add a bit to take out the target tile in case target is a walls
    confirmation = 1
    while len(path) > 0:
        a = path.pop(0)
        if a == "W":
            confirmation = 0
            break
    return confirmation