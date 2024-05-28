# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

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
    def __init__(self,name, price, vat_class):
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
Calculate VAT for the whole DB entriwes
"""
def calculate_vat_return():
    print("Calculating VAT return for items in the database")
    items_list = SHEET.worksheet("item_list").get_all_values()[1:]
    vat_cats = SHEET.worksheet("vat_cat_list").get_all_values()[1:6]
    new_dict = {vat_cats[i][0]: vat_cats[i][1] for i in range(len(vat_cats))}

    vat_return = 0
    for item in items_list:
        vat_return += float(item[1]) * float(new_dict[item[2]])

    print("Removing calculated items from active database to backup database")
    worksheet_to_update = SHEET.worksheet("registred_item_list")

    for row in items_list:
        worksheet_to_update.append_row(row)

    worksheet_to_delete = SHEET.worksheet("item_list")
    worksheet_to_delete.delete_rows(2,99)
    
    return vat_return

"""
Add calculated VAT return to the database
"""
def add_vat_return_to_db(vat_return):
    print("Adding calculated VAT return to the database")
    data_str = [str(vat_return), str(datetime.now())]
    worksheet_to_update = SHEET.worksheet("vat_report")
    worksheet_to_update.append_row(data_str)



def main():
    print("welcome to Vat calculator")
    print(f'Format of the VAT item entry is "item name,price,vat category')
    vat_item = input("Pleae enter your item data:\n")
    data_str = vat_item.split(",")
    lsist_item = VatListItem(data_str[0], float(data_str[1]), data_str[2])
    lsist_item.add_item_to_db()



#main()
calculate_vat_return()
