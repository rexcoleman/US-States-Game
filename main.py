import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data)
all_states = data["state"].to_list()
# print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another State's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        #
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        print(state_data)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

#states_to_learn.csv

screen.exitonclick()

#
# else:
#     print("no")


# print(states_data)



# state_count = len(states_data[states_data[title_case_answer] == title_case_answer])
# print(state_count)



# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

#
# match_search = False
# while match_search == False:
#     for state in states:
#         if state == title_case_answer:
#             match_search = True
#         else:
#             match_search = False
#     print(match_search)

# print(match_search)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


#Convert the guess to titla case
#Check if the guess is among the 50 states
#Write correct guesses onto the map
#Use a loop to allow the user to keep guessing
#Record the correct guesses in a list
#Keep track of the score





def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


