l = []

def setup():
    size(1000, 900)
    strokeWeight(5)
    background(255)

def draw():
    background(255)
    for i in l:
        line(i[0], i[1], i[2], i[3])
    line(width / 2, 0, mouseX, mouseY)
    line(width / 2, height, mouseX, mouseY)
    line(0, height / 2, mouseX, mouseY)
    line(width, height / 2, mouseX, mouseY)
    if (mousePressed):
        l.append([width / 2, 0, mouseX, mouseY])
        l.append([width / 2, height, mouseX, mouseY])
        l.append([0, height / 2, mouseX, mouseY])
        l.append([width, height / 2, mouseX, mouseY])
