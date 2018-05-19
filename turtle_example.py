# source: https://github.com/hulaloop/Introduction-to-Python/blob/master/Advanced-Turtle-Examples.md
import turtle

t = turtle.Turtle()
t.color("#FFFFFF")
t.setpos(-120, 140)
t.speed(0)
t.color("#bada55")
t.hideturtle()

def koch(length):
	if length < 5:
		t.forward(length)
		t.left(60)
		t.forward(length)
		t.right(120)
		t.forward(length)
		t.left(60)
		t.forward(length)
	else:
		koch(length / 2)
		t.left(60)
		koch(length / 2)
		t.right(120)
		koch(length / 2)
		t.left(60)
		koch(length / 2)

for _ in range(1, 51):
	koch(24.0)
	t.right(90)
