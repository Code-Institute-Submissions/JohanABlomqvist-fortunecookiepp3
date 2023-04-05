import gspread
import random
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fortunecookiepp3')

worksheet = SHEET.sheet1

# Fetch fortunes from the Google Sheet (assuming they're in column A)
fortunes = worksheet.col_values(1)

def get_fortune():
    return random.choice(fortunes)

def print_fortune_cookie():
    print("  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("  ┃                             ┃")
    print("  ┃       Fortune Cookie        ┃")
    print("  ┃                             ┃")
    print("  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def save_fortune(name, fortune):
    with open("saved_fortunes.txt", "a") as f:
        f.write(f"{name}: {fortune}\n")

def get_valid_input(prompt, valid_choices):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please try again.")

print_fortune_cookie()
print("Hello, please enter your name to get your fortune:")
name = input()

while True:
    fortune = get_fortune()
    print(f"\n{name}, your fortune is:\n")
    print(fortune)

    save_choice = get_valid_input("Would you like to save your fortune? (y/n): ", ["y", "n"])
    if save_choice == "y":
        save_fortune(name, fortune)
        print("Your fortune has been saved.")
    else:
        print("Your fortune has not been saved.")

    another_fortune = get_valid_input("Do you want to get another fortune? (y/n): ", ["y", "n"])
    if another_fortune != "y":
        break