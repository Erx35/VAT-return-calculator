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
    Calculate the vat value for the product
    """
    def get_vat_value(self):
        vat_cats = SHEET.worksheet("vat_cat_list").get_all_values()[1:6] 
        new_dict = {vat_cats[i][0]: vat_cats[i][1] for i in range(len(vat_cats))}
        vat_price = self.price * float(new_dict[self.vat_class])
        return vat_price


def main():
    print("welcome to Vat calculator")
    vat_item = input("Pleae enter your item data:\n")
    data_str = vat_item.split(",")
    print(data_str)
    lsist_item = VatListItem(data_str[0], float(data_str[1]), data_str[2])
    print(lsist_item)
    print(lsist_item.get_vat_value())
    worksheet_to_update = SHEET.worksheet("item_list")
    worksheet_to_update.append_row(data_str)


main()
#radio = VatListItem("Radio", 125.63, "2")

#print(datetime.now())
