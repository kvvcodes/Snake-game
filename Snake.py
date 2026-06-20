# first project in python, a snake game using turtle module 2026.06.15

import turtle
import time
import random

delay = 0.1

#Score system
score = 0
high_score = 0

#setting up the screen
sc = turtle.Screen()
sc.title("Snake Game by @kvvcodes")
sc.bgcolor("black")
sc.setup(width=600, height=600)
sc.tracer(0)   # turns off the screen updates,This is useful in games because you can perform many moves and drawing operations off-screen, then render one complete frame with sc.update() — resulting in much smoother motion, less flicker, and better performance.

# creating the snake head
head = turtle.Turtle()
head.speed(0)   
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)   
food.shape("circle")
food.color("red")
food.penup() # so i first used the penup after goto line and the problem with that was there was a line connecting the head and food thats cuz in turtle the drawing happens with goto since i placed the penup after goto what it did was it stopped the drawing after it already drew so i just had move the penup command a line higher and it fixed.
food.goto(0, 200)

segments = []  # this list will hold the segments of the snake's body, which will grow as the snake eats food. Each time the snake eats food, a new segment will be added to this list and positioned accordingly to create the appearance of a growing snake.

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High score: 0", align= "center", font=("Courier", 24, "normal"))


# functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) # i could also write head.sety(head.ycor() - 20) instead of creating those new variable y(or x) but i just think this way is more cleaner and understandable.

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
def go_up():
    if head.direction != "down": # this is to prevent the snake from directly moving in opposite direction cuz that would make it collide and end the agme
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right" 

#keybindings
sc.listen()
sc.onkeypress(go_up, 'Up') # so i first used up or w in a single and the w didnt work, thats because or first checks up and if up is true the code doesnt check for the next w key it travels to the next line. So basically or isnt really an either function. 
sc.onkeypress(go_up, 'w')
sc.onkeypress(go_down, 'Down')
sc.onkeypress(go_down, 's')
sc.onkeypress(go_left, 'Left')
sc.onkeypress(go_left, 'a')
sc.onkeypress(go_right, 'Right')
sc.onkeypress(go_right, 'd')


#main game loop

while True:
    sc.update()  # since we turned off the screen updates, we need to manually update the screen in each iteration of the game loop to reflect any changes made to the game state.
    
    if head.distance(food) < 20: #this checks if the head and food has collided i came to know that a shape in turtle is 20 pixels and since 10 from head and 10 from food is 20 pixels thats how i came with the number 20.
        # moving the food to a random spot on the screen using the random module
        x = random.randint(-290,290) 
        y = random.randint(-290,290) # i used -290 and 290 cuz the screen is 600x600 and the center is 0,0 so the max x and y can be 300 and min can be -300 but since the shape is 20 pixels i subtracted 10 from both sides to make sure the food doesnt go out of bounds.
        food.goto(x, y) # again i could just remove the x and y and directly put the random.randint in the goto function but i think this way makes it more understandable.
        
        #adding the new segments to the snake
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square")
        new_segments.color("grey")
        new_segments.penup()
        segments.append(new_segments)
        delay -= 0.001 #this makes the snake faster as it eats because in turtle as the snake grows longer it slows the snake down so to counter that and to make the game more challenging i have done this. Theres no real way to remove this slowing down other than do this or use pygame.

        #score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear() # this is to clear the previous score before writing the new score, if we dont clear it the new score will just be written on top of the old score and it will look messy.
        pen.write("Score: {}  High score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
        

    #moving the end segments first in reverse order so that they follow the head. I'm gonna do this in reverse order because if i do it in normal order the segments will just stack on top of each other and not follow the head properly. By doing it in reverse order, each segment will move to the position of the segment in front of it, creating a smooth following effect.
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #moving segment 0 to follow the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    #collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop" 

        #resetting the delay
        delay = 0.1
        
        #score reset
        score = 0
        pen.clear()
        pen.write("Score: 0  High score: {}".format(high_score), align = "center", font = ("Courier", 24, "normal"))

        #the thing with the turtle module is that individual lines or "segments" arent managed as seperate entities so you cant just delete these segments once they are drawn they kinda permanent but for that what we can is hide them i hid them by making them go off the screen but you can make their color the same as bgcolor but its kind of a bad idea cuz its gonna kinda like erase the border if you get what i mean.
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

        
    move()

    #collision with the body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            #resetting the delay
            delay = 0.1
            
            #score reset
            score = 0
            pen.clear()
            pen.write("Score: 0  High score: {}".format(high_score), align = "center", font = ("Courier", 24, "normal"))



    time.sleep(delay) 





sc.mainloop()  # This line starts the event loop, allowing the window to remain open and responsive to user interactions until it is closed.    
#finished 2026.06.18