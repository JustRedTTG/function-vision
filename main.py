import pygameextra as pe
pe.init()
pe.display.make((600, 600), "function visualize")

function = "abs(x)+x*2"
range_of_check = (-5, 5)
quarter = 5
increment = .01
line_size = 2
line_color = pe.colors.white


def get_point(x):
    #problem = function.replace('x', str(x))
    return eval(function, {'x': x})

draggable = pe.mouse.Draggable(pe.math.center((0,0, *pe.display.get_size())))

while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    pe.fill.full(pe.colors.verydarkgray)
    ok, center  = draggable.check()

    pe.draw.line(pe.colors.darkgray, (center[0]-150, center[1]), (center[0]+150, center[1]), 1)
    pe.draw.line(pe.colors.darkgray, (center[0], center[1]-150), (center[0], center[1]+100), 1)

    for x in range(int(range_of_check[0]*100), int(range_of_check[1]*100), int(increment*100)):
        y = get_point(x*.01)
        pe.draw.circle(line_color, (center[0] + x * quarter * .01, center[1] - y * quarter), line_size)

    pe.display.update(60)


