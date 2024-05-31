# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials
from os import system
import keyboard

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('VatDataTable')


class VatListItem:
    """
    Create vat list item objects
    """
    def __init__(self, name, price, vat_class):
        self.name = name
        self.price = price
        self.vat_class = vat_class
    """
    Calculate the vat value for the current product
    """
    def get_vat_value(self):
        print("Calculating total VAT return")
        vat_cats = SHEET.worksheet("vat_cat_list").get_all_values()[1:6]
        new_dict = {vat_cats[i][0]: vat_cats[i][1] for i in range(len(vat_cats))}
        vat_price = self.price * float(new_dict[self.vat_class])
        return vat_price
    """
    Add user entered data to the database
    """
    def add_item_to_db(self):
        print("Adding item to the VAT database")
        worksheet_to_update = SHEET.worksheet("item_list")
        worksheet_to_update.append_row([self.name, self.price, self.vat_class, str(datetime.now())])


"""
Clear the terminal after user presses enter
"""


def input_and_clear():
    input("Press enter to continue\n")
    system('cls||clear')


"""
Print out the database entries
"""


def print_db_content(sheet):
    all_items = SHEET.worksheet(sheet).get_all_values()[1:]
    [print(item) for item in all_items]


"""
Calculate VAT for the whole DB entriwes
"""


def calculate_vat_return():
    print("Calculating VAT return for items in the database")
    items_list = SHEET.worksheet("item_list").get_all_values()[1:]
    vat_return = 0
    if items_list != []:
        vat_cats = SHEET.worksheet("vat_cat_list").get_all_values()[1:6]
        new_dict = {vat_cats[i][0]: vat_cats[i][1] for i in range(len(vat_cats))}

        for item in items_list:
            vat_return += float(item[1]) * float(new_dict[item[2]])

        print("Removing calculated items from active database to backup database")
        worksheet_to_update = SHEET.worksheet("registred_item_list")

        for row in items_list:
            worksheet_to_update.append_row(row)

        worksheet_to_delete = SHEET.worksheet("item_list")
        worksheet_to_delete.delete_rows(2, 99)
    return vat_return


"""
Add calculated VAT return to the database
"""


def add_vat_return_to_db(vat_return):
    if vat_return != 0:
        print("Adding calculated VAT return to the database")
        data_str = [str(vat_return), str(datetime.now())]
        worksheet_to_update = SHEET.worksheet("vat_report")
        worksheet_to_update.append_row(data_str)


"""
Check that the VAT data input is valid
"""


def validate_data_input(data):
    try:
        if len(data) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(data)}"
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again!\n')


"""
Main function
"""


def main():
    print("Welcome to Vat calculator\n")
    selection = ""

    while True:

        print("Please select from the following menu")
        print("1. Enter VAT item")
        print("2. Calculate VAT for the items in the database")
        print("3. See items in the current database")
        print("4. See items in archived database")
        print("5. See VAT reports and their date")
        print("6. Exit")

        selection = input("Please eneter your selection:\n")

        system('cls||clear')

        if selection == '1':
            print(f'Format of the VAT item entry is "item_name,price,vat_category"')
            vat_item = input("Pleae enter your item data:\n")
            data_str = vat_item.split(",")
            validate_data_input(data_str)

            try:
                list_item = VatListItem(data_str[0], float(data_str[1]), data_str[2])
                list_item.add_item_to_db()
                vat_value = list_item.get_vat_value()
                print(f'{list_item.name} has been entered to the database. VAT on the item is: {vat_value}')
            except ValueError as e:
                print(f'Could not add data to the database.')
            except IndexError as e:
                print(f'Not enough data entered for the VAT item.')
            input_and_clear()
        elif selection == '2':
            vat_return_total = calculate_vat_return()
            if vat_return_total == 0:
                print(f'No data in the active database, please enter more data')
            else:
                print(f'Calculated vat return is: {vat_return_total}')
            add_vat_return_to_db(vat_return_total)
            input_and_clear()
        elif selection == '3':
            print_db_content("item_list")
            input_and_clear()
        elif selection == '4':
            print_db_content("registred_item_list")
            input_and_clear()
        elif selection == '5':
            print_db_content("vat_report")
            input_and_clear()
        elif selection == '6':
            print("Thank you for using VAT calculator")
            input_and_clear()
            break
        else:
            print(f'Please enter correct selection! You entered {selection}')
            input_and_clear()


main()
