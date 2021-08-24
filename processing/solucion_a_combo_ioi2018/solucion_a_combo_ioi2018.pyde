s = ""
i = 0
l = ["\nS\nlen(S)\n","\nS+S\nlen(S)\n","\nS+SB+SX+SY\nlen(S)+1\n","\nS+SB+SX\nlen(S) len(S)+1\n"]
l.append("\nSBX+SBY\nlen(S)+2\n")
l.append("\nSBX+SBY+SX\nlen(S) len(S)+1 len(S)+2\n")
l.append("\nAB\n0 1 2\n")
l.append("\nsi 0 --> X\n0 1\n")
l.append("\nSB+SX\nlen(S) len(S)+1\n")
l.append("\nsi len(S)+1 --> SB\nlen(S) len(S)+1\n")

def setup():
    global f, s, l
    fullScreen()
    background(0)
    f = createFont("Ubuntu Bold", 30, True)
    
def draw():
    global f, i, s
    background(0)
    textFont(f)
    s = ""
    copia = i
    for j in range(5):
        if (copia == 0): break
        s += l[j]
        copia -= 1
    fill(255)
    text(s, 300, 30)
    s = ""
    for j in range(5, 10):
        if (copia == 0): break
        s += l[j]
        copia -= 1
    fill(255)
    text(s, 1000, 30)
    s = ""
    for j in range(5, 10):
        if (copia == 0): break
        s += l[j]
        copia -= 1
    fill(255)
    text(s, 1500, 30)

def keyPressed():
    global i, l, f
    fill(255)
    if (keyCode == RIGHT):
        if (i < len(l)):
            i += 1
    if (keyCode == LEFT):
        if (i > 0):
            i -= 1
