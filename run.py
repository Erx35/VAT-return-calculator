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

    def add_item_to_db(self):
        worksheet_to_update = SHEET.worksheet("item_list")
        worksheet_to_update.append_row([self.name, self.price, self.vat_class, str(datetime.now())])


def calculate_vat_return():
    items_list = SHEET.worksheet("item_list").get_all_values()[1:]
    vat_cats = SHEET.worksheet("vat_cat_list").get_all_values()[1:6]
    new_dict = {vat_cats[i][0]: vat_cats[i][1] for i in range(len(vat_cats))}
    vat_return = 0
    for item in items_list:
        vat_return += float(item[1]) * float(new_dict[item[2]])
    return vat_return

def add_vat_return_to_db(vat_return):
    data_str = [str(vat_return), str(datetime.now())]
    worksheet_to_update = SHEET.worksheet("vat_report")
    worksheet_to_update.append_row(data_str)



def main():
    print("welcome to Vat calculator")
    vat_item = input("Pleae enter your item data:\n")
    data_str = vat_item.split(",")
    lsist_item = VatListItem(data_str[0], float(data_str[1]), data_str[2])
    lsist_item.add_item_to_db()


#add_vat_return_to_db(calculate_vat_return())

main()
#radio = VatListItem("Radio", 125.63, "2")

#print(datetime.now())
