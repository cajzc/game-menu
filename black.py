import os
import random
import time
import curses

win=False

# Players stdscr.getchs
def blackjack(stdscr):

    # AI stdscr.getchs
    ai_first_card=random.randint(1,10)
    ai_second_card=random.randint(1,10)
    ai_total=ai_first_card+ai_second_card



    # Assign first card
    first_card=random.randint(1,10)

    # Assign second card
    second_card=random.randint(1,10)

    stdscr.addstr(f"Player: {first_card}")
    # stdscr.addstr combo of first and second card
    new_cards= first_card+second_card
    stdscr.addstr(f"\nPlayer: {new_cards}")

    # Check if blackjack/21
    if new_cards==21:
        stdscr.addstr("WIN!")

    # Check if bust 
    elif new_cards>21:
        stdscr.addstr("BUST!")

    # If cards <21, does player want to hit again?   
    elif new_cards<21:
        stdscr.addstr("\nHit or Stand?")
        hit_or_stand=(stdscr.getstr())
        third_card=random.randint(0,11)
        final_card=new_cards+third_card

        # Player selects stand
        if hit_or_stand =='stand':
            final_card=new_cards
            stdscr.addstr(f"Player: {final_card}")

        # Player selects hit
        elif hit_or_stand=='hit':  
            stdscr.addstr(f"Player: {final_card}")
        
        # Compare with AI
        if ai_total>final_card:
            stdscr.addstr(f"House: {ai_total}")
            stdscr.addstr("LOSE!")

        elif ai_total<final_card:
            stdscr.addstr(f"House: {ai_total}")
            stdscr.addstr("WIN!")
        else:
            stdscr.addstr("House: {ai_total}")
            stdscr.addstr("DRAW, NO WINNERS!")

            # Check if blackjack/21
            if new_cards==21:
                stdscr.addstr("BLACKJACK!")

            # Check if bust    
            elif new_cards>21:
                stdscr.addstr("BUST!")
    curses.nocbreak()
    curses.echo()
