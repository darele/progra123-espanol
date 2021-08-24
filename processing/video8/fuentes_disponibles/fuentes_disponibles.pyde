def setup():
    global f
    #size(1500, 800)
    fullScreen()
    background(255)
    f = createFont("DejaVu Sans", 15, True)
    textFont(f, 20)
    x = 0
    y = 20
    mayor = 0
    l = PFont.list()
    fill(0)
    for i in l:
        text(str(i), x, y)
        y += 20
        mayor = mayor if textWidth(i) <= mayor else textWidth(i) 
        if (y + 20 > height):
            x += mayor
            x += 5
            y = 20
            mayor = 0
            
