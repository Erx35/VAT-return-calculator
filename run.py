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
        headings = SHEET.worksheet("vat_cat_list").get_all_values()[1:6] 
        new_dict = {headings[i][0]: headings[i][1] for i in range(0,5)}
        vat_price = self.price * float(new_dict[self.vat_class])
        return vat_price


def get_column_names():
    headings = SHEET.worksheet("vat_cat_list").get_all_values()[1:6] 
    new_dict = {headings[i][0]: headings[i][1] for i in range(0,5)}
    new_dict['2']


    return headings


#radio = VatListItem("Radio", 125.63, "2")

print(datetime.now())
