# Vat Calculator Application
This application was designed to have a method of checking how much VAT could a company claim back when purchesing goods for business needs. Application allows you to enter all your goods into a database, calculate the VAT return ammount and save the goods processed and VAT calculations int separate databases. All the data in the databases can be seen througth a menu selection.

![Image of a webpage on different screens][multiscreen]

[multiscreen]: media/project-3-main-screen.JPG

## Features
The program has mant features that are accessible througth a menu. All the features can be accessed by selecting a number infront of the menu feature.  

![Application menu][menu]

[menu]: media/menu.JPG

### Enter VAT item
Allows user to enter VAT item bought for a compani in the format Item name, Item Price, Vat category

![Entry of VAT item][vatitem]

[vatitem]: media/vat-item.JPG

Once the item is entere, the quantity of VAT is displaied.

![VAT item added to the db][vatitemadded]

[vatitemadded]: media/vat-item.JPG

### Calculate VAT 
Calculates the total VAT on the items added to the active VAT database. Creates a report on the VAT that can be returned. Adds the report to the VAT database and moves calculated items to the backup database.

![Calculated VAT results][vatcalc]

[vatcalc]: media/vat-calc.JPG

### Menu options for preview
Selections 3, 4 and 5 allow the user to see the current status of the data in the databases. User cab see what is in the current active VAT item database, the calculated VAT in the VAT databace and already calculated VAT items in the backup database.

![VAT item active DB][vatitemdb]

[vatitemdb]: media/vat-item-db.JPG

![Calculated VAT DB][vatreports]

[vatreports]: media/vat-reports.JPG

![VAT item backup DB][vatitembackupdb]

[vatitembackupdb]: media/items-backup-db.JPG

### VAT classes
VAT classes were taken from the Revenue webpage and converted into a DB page to be read by the application.

![VAT classes in the DB][vatclasses]

[vatclasses]: media/vat-classes.JPG

## Data model
The VAT item was designed to be a class. Class has 3 member variables, name, price and VAT class. Clas has a two member functions that allow for adding the VAT item to the database and calculate individual VAT value.

## Testing
* Code has been manually tested and functionality confirmed
* PEP8 linter came back with no errors
* Exeptions for the VAT item input were confirmed
* Tested in Gitpod and Heroku terminals with no issues
## Bugs
* Fixed issue with data not being deleted from the main VAT item DB. Needed to research how to delete data from Goodle sheets.

