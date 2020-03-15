# REFERENCES
# http://paulbourke.net/fractals/lorenz/

x = 0.01
y = 0
z = 0

# contants sigma=a, ro=b, and beta=c
A = 10
B = 28
C = 8 / 3

points = PVector(x, y, z)


def setup():
    size(500, 500, P3D)
    background(0)

def draw():

    # for handlling time
    dt = 0.01

    # formulas
    global x, y, z
    dx = (A * (y - x)) * dt
    dy = (x * (B - z) - y) * dt
    dz = (x * y - C * z) * dt
    x += dx
    y += dy
    z += dz
    # print(x, y, z)

    points.add(x, y, z)
    print(points)

    translate(width / 2, height / 2)
    scale(5)
    stroke(255)

    for v in points:
        point(x,y,z)
