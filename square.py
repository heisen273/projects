import turtle

def square(cursor):
	num=0
	while num<4:
		cursor.forward(100)
		cursor.right(75)
		num=num+1

def draw():
	window=turtle.Screen()
        window.bgcolor("red")
        flower=turtle.Turtle()#kvadrat
	flower.shape("turtle")
	flower.speed(444400)
	for i in range(1,30):
		square(flower)
		flower.right(-90)
	flower.right(160)
	flower.fd(400)
	#krug=turtle.Turtle()#circle
	#krug.shape("arrow")
	#krug.circle(100)
	
	window.exitonclick()
draw()


