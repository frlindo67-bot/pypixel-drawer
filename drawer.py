import turtle as t

LEBAR = 10
TINGGI = 10

def set_pixel_size(lebar, tinggi=None):
    global LEBAR, TINGGI
    LEBAR = lebar
    TINGGI = tinggi or lebar

def pixel(x, y, warna):
    t.penup()
    t.goto(x, y)
    t.color(warna)
    t.begin_fill()

    for _ in range(2):
        t.forward(LEBAR)
        t.right(90)
        t.forward(TINGGI)
        t.right(90)

    t.end_fill()
    t.penup()