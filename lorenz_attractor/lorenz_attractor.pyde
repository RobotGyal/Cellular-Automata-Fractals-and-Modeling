x = 0
y = 0
z = 0

# contants theta=a, __=b, and beta=c
A = 1
B = 1
C = 1

def setup():
    size(300, 300)
    background(0)

def draw():
    # for handlling time 
    dt = 1
    
    # formulas 
    global x, y, z
    dx = (A * (y - x)) * dt
    dy = (x * (B - z) - y) * dt
    dz = (x * y - C * z) * dt
    x += dx
    y += dy
    z += dz
