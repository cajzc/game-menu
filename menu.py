import curses
import os
import random
import time

from black import blackjack
from tictactoe import full_tictactoe

# Define menu items
menu_items = [
    {"title": "Games", "options": ["Blackjack", "Tic-Tac-Toe"]},
    {"title": "Leaderboard", "options": ["Options"]},
]

# Initialize curses
stdscr = curses.initscr()

# Turn off cursor blinking
curses.curs_set(0)

# Set up colors
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
highlight_color = curses.color_pair(1)

# Set up the menu window
menu_window = curses.newwin(len(menu_items) + 2, 40, 4, 4)
menu_window.keypad(1)

# Blackjack function
# Players stdscr.getchs

# Define a function to print the menu
def print_menu(options, current_option):
    menu_window.clear()
    menu_window.border(0)
    menu_window.addstr(0, 15, " MAIN MENU ")
    for i, option in enumerate(options):
        if i == current_option:
            menu_window.addstr(i+1, 2, f"> {option}", highlight_color)
        else:
            menu_window.addstr(i+1, 2, f"  {option}")
    menu_window.refresh()

# Define a function to handle keyboard input
def get_user_input():
    current_option = 0
    while True:
        print_menu([item['title'] for item in menu_items], current_option)
        key = menu_window.getch()
        if key == curses.KEY_UP:
            current_option = (current_option - 1) % len(menu_items)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(menu_items)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected_item = menu_items[current_option]
            if selected_item['title'] == 'Games':
                # Display the game options sub-menu
                sub_menu_window = curses.newwin(len(selected_item['options']) + 2, 40, 4, 4)
                sub_menu_window.keypad(1)
                sub_menu_current_option = 0
                while True:
                    print_menu(selected_item['options'], sub_menu_current_option)
                    sub_menu_key = sub_menu_window.getch()
                    if sub_menu_key == curses.KEY_UP:
                        sub_menu_current_option = (sub_menu_current_option - 1) % len(selected_item['options'])
                    elif sub_menu_key == curses.KEY_DOWN:
                        sub_menu_current_option = (sub_menu_current_option + 1) % len(selected_item['options'])
                    elif sub_menu_key == curses.KEY_ENTER or sub_menu_key in [10, 13]:
                        # Do something with the selected game option
                        if selected_item['options'][sub_menu_current_option] == 'Blackjack':
                            blackjack(stdscr)
                            stdscr.refresh()
                            stdscr.getch()
                        elif selected_item['options'][sub_menu_current_option]=='Tic-Tac-Toe':
                            curses.wrapper(full_tictactoe)
                            stdscr.refresh()
                            stdscr.getch()
                        sub_menu_window.clear()
                        sub_menu_window.refresh()
                        curses.endwin()
                        return
                    
                    print_menu(selected_item['options'], sub_menu_current_option)

            # Display the score
            elif selected_item['title'] == 'Leaderboard':
                pass
            else:
                curses.endwin()
                return
        print_menu([item['title'] for item in menu_items], current_option)

# Call the function to start the menu
get_user_input()
