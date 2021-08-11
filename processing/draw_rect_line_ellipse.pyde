x = 0

def setup():
    size(1000, 900)
    strokeWeight(10)
    background(255)

def draw():
    delay(100)
    global x
    background(255)
    point(x, 500)
    x += 20
    if (x > width):
        x %= width