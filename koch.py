# Koch snowflake

import turtle # graphics

def koch_curve(t, iterations, length, short_fac, angle):

    if iterations == 0:
        t.forward(length)
    else:
        iterations = iterations - 1
        length = length / short_fac

        koch_curve(t, iterations, length, short_fac, angle)
        t.left(angle)
        koch_curve(t, iterations, length, short_fac, angle)
        t.right(angle * 2)
        koch_curve(t, iterations, length, short_fac, angle)
        t.left(angle)
        koch_curve(t, iterations, length, short_fac, angle)


t = turtle.Turtle()
t.hideturtle()


for i in range(3):
    koch_curve(t, 4, 200, 3, 60)
    t.right(120)



trutle.mainloop() # stops the turtle screen (comment this to see the image after completion)


