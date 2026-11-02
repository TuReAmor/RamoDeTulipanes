
import turtle
import math
import random

# ==========================================
# PARA MI AMOR ❤️
# Un ramo de tulipanes delicados
# ==========================================

screen = turtle.Screen()
screen.setup(width=1000, height=680)
screen.title("Para mi re amor ❤️")
screen.bgcolor("#10101F")
screen.tracer(1)

# ==========================================
# PALETA DE COLORES
# ==========================================

ROSA = "#F58EB5"
ROSA_CLARO = "#FFD0E1"
ROSA_OSCURO = "#CE638C"
ROSA_SOMBRA = "#B94F7D"
ROSA_LUZ = "#FFE4ED"
VERDE = "#367B52"
VERDE_CLARO = "#69B783"
VERDE_BRILLO = "#B4E2B8"
DORADO = "#FFDFA0"
TEXTO = "#FFE0EC"

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def curva(p0, p1, p2, p3, pasos=30):
    puntos = []

    for i in range(pasos + 1):
        u = i / pasos
        v = 1 - u

        x = (
            v**3 * p0[0]
            + 3 * v**2 * u * p1[0]
            + 3 * v * u**2 * p2[0]
            + u**3 * p3[0]
        )

        y = (
            v**3 * p0[1]
            + 3 * v**2 * u * p1[1]
            + 3 * v * u**2 * p2[1]
            + u**3 * p3[1]
        )

        puntos.append((x, y))

    return puntos


def dibujar_curva(puntos, color, grosor=2):
    t.penup()
    t.goto(puntos[0])
    t.pencolor(color)
    t.pensize(grosor)
    t.pendown()

    for p in puntos[1:]:
        t.goto(p)

    t.penup()


def poligono(puntos, relleno, borde):
    t.penup()
    t.goto(puntos[0])
    t.color(borde)
    t.fillcolor(relleno)
    t.pensize(2)
    t.pendown()
    t.begin_fill()

    for p in puntos[1:]:
        t.goto(p)

    t.goto(puntos[0])
    t.end_fill()
    t.penup()


def escribir(x, y, mensaje, tamano, color,
             estilo="normal"):
    t.penup()
    t.goto(x, y)
    t.color(color)

    t.write(
        mensaje,
        align="center",
        font=("Georgia", tamano, estilo)
    )


def dibujar_forma(segmentos, relleno, borde, escala):
    puntos = []

    for segmento in segmentos:
        parte = curva(*segmento, pasos=24)

        if puntos:
            puntos.extend(parte[1:])
        else:
            puntos.extend(parte)

    poligono(puntos, relleno, borde)


# ==========================================
# FONDO ESTRELLADO
# ==========================================

def corazon(x, y, escala, color):
    puntos = []

    for i in range(101):
        a = 2 * math.pi * i / 100

        hx = 16 * math.sin(a)**3

        hy = (
            13 * math.cos(a)
            - 5 * math.cos(2*a)
            - 2 * math.cos(3*a)
            - math.cos(4*a)
        )

        puntos.append((
            x + hx * escala / 32,
            y + hy * escala / 32
        ))

    poligono(puntos, color, color)


def fondo():
    random.seed(20)

    for _ in range(75):
        x = random.randint(-480, 480)
        y = random.randint(-320, 320)

        t.penup()
        t.goto(x, y)
        t.dot(random.randint(2, 4), "#514B69")

    corazon(-430, 270, 22, "#74385E")
    corazon(430, 270, 22, "#74385E")
    corazon(-430, -130, 18, "#74385E")
    corazon(430, -130, 18, "#74385E")

    for x, y in [
        (-330, 190),
        (330, 210),
        (-370, -200),
        (370, -210)
    ]:
        t.penup()
        t.goto(x, y)
        t.dot(7, DORADO)


# ==========================================
# TALLOS
# ==========================================

def tallo(x, y):
    puntos = curva(
        (x, y - 20),
        (x, y - 100),
        (x * 0.4, -145),
        (0, -205)
    )

    dibujar_curva(puntos, VERDE, 6)

    # Reflejo fino del tallo
    dibujar_curva(
        curva(
            (x - 1, y - 25),
            (x - 1, y - 100),
            (x * 0.4 - 1, -145),
            (-1, -205)
        ),
        "#78A982",
        1
    )


# ==========================================
# HOJAS BOTÁNICAS
# ==========================================

def hoja(x, y, direccion, tamano=1):

    inicio = (x, y)

    punta = (
        x + direccion * 100 * tamano,
        y + 75 * tamano
    )

    superior = curva(
        inicio,
        (x + direccion*20*tamano,
         y + 65*tamano),
        (x + direccion*75*tamano,
         y + 110*tamano),
        punta
    )

    inferior = curva(
        punta,
        (x + direccion*75*tamano,
         y + 15*tamano),
        (x + direccion*25*tamano,
         y - 20*tamano),
        inicio
    )

    poligono(
        superior + inferior[1:],
        VERDE_CLARO,
        VERDE
    )

    # Nervadura central
    dibujar_curva(
        curva(
            inicio,
            (x + direccion*35*tamano,
             y + 35*tamano),
            (x + direccion*65*tamano,
             y + 55*tamano),
            punta
        ),
        VERDE_BRILLO,
        2
    )


# ==========================================
# TULIPANES DELICADOS 🌷
# ==========================================

def tulipan(x, y, escala=1):

    def P(px, py):
        return (
            x + px * escala,
            y + py * escala
        )

    # --------------------------------------
    # PÉTALO TRASERO IZQUIERDO
    # --------------------------------------

    izquierdo = [
        (
            P(-29, -22),
            P(-37, 5),
            P(-39, 43),
            P(-27, 62)
        ),
        (
            P(-27, 62),
            P(-19, 72),
            P(-9, 57),
            P(-7, 43)
        ),
        (
            P(-7, 43),
            P(-8, 20),
            P(-9, -5),
            P(-10, -22)
        ),
        (
            P(-10, -22),
            P(-17, -26),
            P(-23, -25),
            P(-29, -22)
        )
    ]

    dibujar_forma(
        izquierdo,
        ROSA_CLARO,
        ROSA_OSCURO,
        escala
    )

    # --------------------------------------
    # PÉTALO TRASERO DERECHO
    # --------------------------------------

    derecho = [
        (
            P(10, -22),
            P(9, -5),
            P(8, 20),
            P(7, 43)
        ),
        (
            P(7, 43),
            P(9, 57),
            P(19, 72),
            P(27, 62)
        ),
        (
            P(27, 62),
            P(39, 43),
            P(37, 5),
            P(29, -22)
        ),
        (
            P(29, -22),
            P(23, -25),
            P(17, -26),
            P(10, -22)
        )
    ]

    dibujar_forma(
        derecho,
        ROSA,
        ROSA_OSCURO,
        escala
    )

    # --------------------------------------
    # PÉTALO CENTRAL PRINCIPAL
    # --------------------------------------

    central = [
        (
            P(-12, -22),
            P(-14, 5),
            P(-15, 43),
            P(-9, 61)
        ),
        (
            P(-9, 61),
            P(-5, 76),
            P(-1, 84),
            P(0, 84)
        ),
        (
            P(0, 84),
            P(5, 76),
            P(9, 61),
            P(9, 48)
        ),
        (
            P(9, 48),
            P(15, 25),
            P(14, 0),
            P(12, -22)
        ),
        (
            P(12, -22),
            P(4, -26),
            P(-4, -26),
            P(-12, -22)
        )
    ]

    dibujar_forma(
        central,
        ROSA_CLARO,
        ROSA_OSCURO,
        escala
    )

    # --------------------------------------
    # SOMBRAS SUAVES ENTRE PÉTALOS
    # --------------------------------------

    dibujar_curva(
        curva(
            P(-9, -10),
            P(-17, 15),
            P(-16, 43),
            P(-9, 61)
        ),
        ROSA_OSCURO,
        max(1, int(escala * 1.5))
    )

    dibujar_curva(
        curva(
            P(9, -10),
            P(17, 15),
            P(16, 43),
            P(9, 61)
        ),
        ROSA_OSCURO,
        max(1, int(escala * 1.5))
    )

    # --------------------------------------
    # NERVADURAS DELICADAS
    # --------------------------------------

    dibujar_curva(
        curva(
            P(-3, -12),
            P(-5, 15),
            P(-4, 48),
            P(0, 73)
        ),
        "#FFF0F5",
        1
    )

    dibujar_curva(
        curva(
            P(3, -12),
            P(5, 15),
            P(4, 48),
            P(0, 73)
        ),
        "#FFF0F5",
        1
    )

    # --------------------------------------
    # REFLEJOS
    # --------------------------------------

    t.penup()
    t.goto(*P(-21, 28))
    t.dot(5 * escala, "#FFFFFF")

    t.penup()
    t.goto(*P(20, 36))
    t.dot(3 * escala, "#FFF0F5")

    t.penup()
    t.goto(*P(0, 66))
    t.dot(3 * escala, "#FFFFFF")


# ==========================================
# ENVOLTORIO
# ==========================================

def envoltorio():

    poligono([
        (-250, -105),
        (250, -105),
        (95, -265),
        (-95, -265)
    ], "#542D50", "#DA6C9C")

    dibujar_curva(
        curva(
            (-250, -105),
            (-180, -170),
            (-70, -235),
            (0, -265)
        ),
        "#A95783",
        2
    )

    dibujar_curva(
        curva(
            (250, -105),
            (180, -170),
            (70, -235),
            (0, -265)
        ),
        "#A95783",
        2
    )


# ==========================================
# LAZO
# ==========================================

def lazo():

    poligono([
        (-5, -205),
        (-42, -185),
        (-80, -205),
        (-55, -240),
        (-10, -225)
    ], ROSA_CLARO, ROSA_OSCURO)

    poligono([
        (5, -205),
        (42, -185),
        (80, -205),
        (55, -240),
        (10, -225)
    ], ROSA, ROSA_OSCURO)

    poligono([
        (-8, -220),
        (-30, -275),
        (-5, -265),
        (8, -220)
    ], ROSA_CLARO, ROSA_OSCURO)

    t.penup()
    t.goto(0, -210)
    t.dot(17, ROSA_OSCURO)

    # Brillo del nudo
    t.goto(-2, -207)
    t.dot(5, ROSA_LUZ)


# ==========================================
# DEDICATORIA ANIMADA ❤️
# ==========================================

mensaje = (
    "Gracias por estos maravillosos tres meses "
    "a tu lado, mi princesita."
)

texto = turtle.Turtle()
texto.hideturtle()
texto.speed(0)
texto.penup()
texto.color(TEXTO)


def escribir_animado(indice=0):

    texto.clear()
    texto.goto(0, -295)

    texto.write(
        mensaje[:indice],
        align="center",
        font=("Georgia", 17, "italic")
    )

    if indice < len(mensaje):
        screen.ontimer(
            lambda: escribir_animado(indice + 1),
            65
        )
    else:
        screen.ontimer(final, 500)


def final():

    corazon(0, -318, 27, ROSA)

    escribir(
        0, -335,
        "TE AMO PARA SIEMPRE",
        10,
        ROSA_CLARO,
        "italic"
    )


# ==========================================
# CONSTRUCCIÓN DEL RAMO
# ==========================================

def crear_ramo():

    fondo()

    flores = [
        (-220, 30, 0.85),
        (-110, 105, 0.95),
        (0, 155, 1.10),
        (110, 105, 0.95),
        (220, 30, 0.85)
    ]

    # Envoltorio
    envoltorio()

    # Tallos
    for x, y, escala in flores:
        tallo(x, y)

    # Hojas
    hoja(-65, -100, -1, 0.85)
    hoja(-35, -145, -1, 0.70)

    hoja(65, -100, 1, 0.85)
    hoja(35, -145, 1, 0.70)

    # Tulipanes
    for x, y, escala in flores:
        tulipan(x, y, escala)

    # Lazo
    lazo()

    # Dedicatoria
    screen.ontimer(escribir_animado, 1000)


# ==========================================
# INICIO
# ==========================================

crear_ramo()

screen.mainloop()
