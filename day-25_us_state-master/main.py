import turtle
import pandas
from messenger import Messenger

image = "blank_states_img.gif"
csv = "50_states.csv"
done = "states_done.csv"


def extract_and_display_state(row):
    """Extract data from the Pandas Series,
    and write the state name to the appropriate location on the screen"""
    # Reset the row index to zero (the old index is retained in a new Index column)
    row1 = row.reset_index()
    state_name = row1.at[0, "state"]
    state_x = int(row1.at[0, "x"])  # Convert numpy.int64 to int
    state_y = int(row1.at[0, "y"])
    state_msg.message_position(message=state_name, position=(state_x, state_y))


# Set up the Screen
# =================
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)  # Sets the actual window size
# screen.screensize(canvwidth=725, canvheight=491)  # Sets the size of the canvas the turtles are drawing on

screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)

# player_msg displays information to the player
player_msg = Messenger(
    fontcolor="red",
    fontsize=24,
    fonttype="bold italic",
)

# state_msg displays the state names on the map
state_msg = Messenger(
    fontcolor="black",
    fontsize=8,
    fonttype="normal",
)

# Read the CSV into a Pandas DataFrame
df = pandas.read_csv(csv)


# Game Loop
# =========
game_on = True
total = len(df.index)  # Total number of states
score = 0  # Number of correct answers given
correct_states = []

while game_on:
    # Get the player answer
    answer = screen.textinput(
        title=f"{score}/{total} States Correct", prompt="Name a U.S. state :")

    # Prevent .title() crash if cancelled or nothing is input
    if answer is None:
        player_msg.message_time("Please type a state name.\nTry Again.", 2)
    else:
        answer = answer.title()  # Convert to Title Case
        if answer == "Exit" or answer == "Quit":
            player_msg.pencolor("green")
            player_msg.message_time("Goodbye\nfor now.", 5)
            break

        # Extract the corresponding Series (row) from the DataFrame
        series = df[df["state"] == answer]

        # Check that the answer given is valid
        if series.empty:
            player_msg.message_time("Incorrect!\nTry Again.", 2)
        else:

            # Check if already answered
            if answer in correct_states:
                player_msg.message_time(
                    f"You already got\n{answer}.\nTry Again.", 2)
            else:
                score += 1
                correct_states.append(answer)
                extract_and_display_state(series)

                # End game
                if score == total:
                    game_on = False
                    player_msg.pencolor("green")
                    player_msg.message_time("Completed.\nWell Done!", 5)


turtle.mainloop()  # Keep the window open when the program ends
