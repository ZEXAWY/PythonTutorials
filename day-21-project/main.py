from graph import create_chart
from data_storage import read_columns, header_picker

menu_prompt = """Please select one of the following options:
- 'a' to draw a chart.
- 'q' to quite.

What will you do? """

charting_menu = "Please select one of these options: "
filename_prompt = "what you like to name your chart? "


def handling_chart():
    try:
        column = int(input(charting_menu))
        x = read_columns(-1)
        y = [float(n) for n in read_columns(column)]

        filename = input(filename_prompt).strip()
        create_chart(x, y, filename)
    except (IndexError, ValueError):
        print("please choose one of the previous option again.")


while True:
    user_selection = input(menu_prompt)
    if user_selection == 'q':
        break
    elif user_selection == 'a':
        header_picker()
        handling_chart()
    else:
        print("Sorry, I didn't get what you mean by that.")
