open_set = [[int(random(0, 600)), int(random(0, 600))]]
closed_set = []
direction = ['r', 'd', 'l', 'u']
r = 255
g = 0
b = 0
cobj = {
    'r': 'h',
    'g': 'i',
    'b': 'h'
}

def setup():
    size(600, 600)
    background(0)

def draw():
    global open_set, r, g, b, cobj
    if len(open_set) != 0:
        test_node = open_set[int(random(len(open_set)))]
        closed_set.append(test_node)
        stroke(r, g, b)
        strokeWeight(4)
        point(test_node[0], test_node[1])
        for dir in direction:
            if dir == 'r':
                x = test_node[0] + 4
                y = test_node[1]
            elif dir == 'd':
                x = test_node[0]
                y = test_node[1] + 4
            elif dir == 'l':
                x = test_node[0] - 4
                y = test_node[1]
            elif dir == 'u':
                x = test_node[0]
                y = test_node[1] - 4

            if x < 0 or x > width or y < 0 or y > height or [x, y] in closed_set or [x, y] in open_set:
                continue
            open_set.append([x, y])
        del open_set[open_set.index(test_node)]
        if cobj['r'] == 'i':
            if r < 255:
                r += 1
            else:
                cobj['r'] = 'h'
                cobj['b'] = 'd'
        elif cobj['r'] == 'd':
            if r > 0:
                r -= 1
            else:
                cobj['r'] = 'h'
                cobj['b'] = 'i'
        elif cobj['g'] == 'i':
            if g < 255:
                g += 1
            else:
                cobj['r'] = 'd'
                cobj['g'] = 'h'
        elif cobj['g'] == 'd':
            if g > 0:
                g -= 1
            else:
                cobj['g'] = 'h'
                cobj['r'] = 'i'
        elif cobj['b'] == 'i':
            if b < 255:
                b += 1
            else:
                cobj['b'] = 'h'
                cobj['g'] = 'd'
        elif cobj['b'] == 'd':
            if b > 0:
                b -= 1
            else:
                cobj['b'] = 'h'
                cobj['g'] = 'i'
        print(test_node, r, g, b)
