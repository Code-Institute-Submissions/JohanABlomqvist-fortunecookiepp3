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

worksheet = SHEET.worksheet("fortunecookiepp3")

fortunes = worksheet.col_values(1)

def get_fortune():
    return random.choice(fortunes)

def print_fortune_cookie():
    print("  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("  ┃                             ┃")
    print("  ┃       Fortune Cookie        ┃")
    print("  ┃                             ┃")
    print("  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

print_fortune_cookie()
print("Hello, please enter your name to get your fortune:")
name = input()

print(f"\n{name}, your fortune is:\n")
print(get_fortune())