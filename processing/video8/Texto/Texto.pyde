def setup():
    fullScreen()
    global f
    f = createFont("Ubuntu", 15, True)
    background(126)
    
def draw():
    global f
    textFont(f, 20)
    s = "me gusta\nusar processing"
    fill(255)
    rect(0, 500, width, 200)
    fill(255, 41, 41)
    textAlign(CENTER)
    textSize(30)
    textLeading(50)
    text(s, width//2, 500 + 30)
    line(width//2, 0, width//2, height)
