import random
# import psycopg2 as pg2
from turtle import Turtle,Screen
#Database connection
# conn = pg2.connect(database='TURTLE_GAME', user='postgres',password='dip2000')
# cur = conn.cursor()

screen=Screen()
screen.setup(width=500,height=400)
def play():
    colors = ["red", "blue", "yellow", "purple", "orange", "green","pink"]
    y_position = [-150,-100,-50,0,50,100,150]
    all_turtles = []
    for turtel_index in range(0,7):
        tim=Turtle(shape="turtle")
        tim.penup()
        tim.color(colors[turtel_index])
        tim.goto(x=-300,y=y_position[turtel_index])
        all_turtles.append(tim)
    #Wining Line
    timmy = Turtle()
    timmy.penup()
    timmy.goto(x=200,y=-200)
    timmy.pendown()
    timmy.left(90)
    timmy.forward(400)
    timmy.hideturtle()
    user_id =[]
    user_bet = []
    no_of_user = screen.numinput(title = "Welcome to the game"  ,prompt="How many players want to play: ")
    for _ in range(0 , int(no_of_user) ):

        user_id.append(screen.textinput(title = "Welcome to the game"  ,prompt="Enter your name: "))
        user_bet.append(screen.textinput(title = "Make your bet"  ,prompt= "Which turtle will win the race ? Enter a color: " ))


    race_on = True
    while race_on :
        for turtle in all_turtles:
            if turtle.xcor() > 190 :
                race_on=False
                winning_color = turtle.pencolor()
                j=0

                for i in user_bet:
                    if winning_color== i:
                        win=True

                        winner = user_id[j]
                        user_id.remove(winner)
                        j += 1
                        print(f"{winner} Won! The {winning_color} turtle has Won")


                k= 0
                for _ in user_id:
                    # if winning_color !=i:
                    win= False
                    loser = user_id[k]
                    k +=1
                    print(f"{loser} lose! The {winning_color} turtle has Won")
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)
    output = screen.textinput(title=f"The {winning_color} turtle has Won", prompt="Do you want to play again? Yes?no")

    # Database
    # query = '''Insert into gamedata(player_name,colour,winner,winner_turtle_colour)
    # values('{}','{}',{},'{}')
    # '''.format(user_id, user_bet, win, winning_color)
    # cur.execute(query)
    # conn.commit()
    if output == 'y':
        screen.clear()
        play()

play()

screen.exitonclick()