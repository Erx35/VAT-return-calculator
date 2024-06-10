# Vat Calculator Application
This application was designed to have a method of checking how much VAT could a company claim back when purchasing goods for business needs. Application allows you to enter all your goods into a database, calculate the VAT return amount and save the goods processed and VAT calculations int separate databases. All the data in the databases can be seen through a menu selection.

![Image of a webpage on different screens][multiscreen]

[multiscreen]: media/project-3-main-screen.JPG

## Features
The program has many features that are accessible through a menu. All the features can be accessed by selecting a number in front of the menu feature.  

![Application menu][menu]

[menu]: media/menu.JPG

### Enter VAT item
Allows user to enter VAT item bought for a company in the format Item name, Item Price, Vat category

![Entry of VAT item][vatitem]

[vatitem]: media/vat-item.JPG

Once the item is entered, the quantity of VAT is displayed.

![VAT item added to the db][vatitemadded]

[vatitemadded]: media/vat-item.JPG

### Calculate VAT 
Calculates the total VAT on the items added to the active VAT database. Creates a report on the VAT that can be returned. Adds the report to the VAT database and moves calculated items to the backup database.

![Calculated VAT results][vatcalc]

[vatcalc]: media/vat-calc.JPG

### Menu options for preview
Selections 3, 4 and 5 allow the user to see the current status of the data in the databases. User cab see what is in the current active VAT item database, the calculated VAT in the VAT database and already calculated VAT items in the backup database.

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

### Exiting application
When exiting the application, greeting is displayed to the user.

![Exit greeting][exit]

[exit]: media/exit.JPG

## Data model
The VAT item was designed to be a class. Class has 3 member variables, name, price and VAT class. Clas has a two member functions that allow for adding the VAT item to the database and calculate individual VAT value.

## Testing
* Code has been manually tested and functionality confirmed
* PEP8 linter came back with no errors
* Exceptions for the VAT item input were confirmed
* Tested in Gitpod and Heroku terminals with no issues

## Resaearch
* Needed to research how to move, delete and transform data in the Google sheets. There are many websites that describe how Google sheets is used but most of them are not for Python. Had to test out many different methodologies to the the functionality working.

## Bugs
* Issue with data not being deleted from the main VAT item DB - Status Fixed

## Remaining Bugs
There are no remaining bugs

## Validator Testing
* PEP8
    * Using PEP8online.com returned no errors

## Deployment
Project was deployed on Heroku. Please follow the link below.
<br />
[VAT-return-calculator](https://vat-calculator-b6621b2925e2.herokuapp.com/)

Repository can be found on the link below.
<br />
[GitHub Repository](https://github.com/Erx35/VAT-return-calculator.git)

## Credits
* Code Institute for the class materials
* W3schools for the easy to follow tutorials


