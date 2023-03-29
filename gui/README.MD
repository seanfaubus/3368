Welcome to our final project for CIS 3368.
Team members: Sean Faubus(16230) and Aryan Dham(15369)

-----------------
PHASE II
-----------------
Login Credentials are:

username: admin
password: password

Once you login, flights page will render.
You can then add/delete a flight.

You can navigate to the Planes/Airports page.
There you can add/delete/update a plane/airport.


Make sure main.py is running in the backend.


-----------------------
HOW TO USE APP PHASE 1
-----------------------
Run main.py in backend directory

In order to login, navigate to /login.
*You will need to add two headers: 'username' and 'password'
Then enter the following credentials
username: admin
password: password

If you login succesfully, the flights info will display. 


-----------------------
General API Information
-----------------------
*** GET ***
For all the different tables: flights, planes, and airports, in order to return one item, navigate 
to /api/(desired table) ex. /api/plane
in the parameters, enter 'id' and the id of the plane you want to return.
However, if you want all the planes, navigate to /api/planes. Same goes for flights and airports.

*** POST ***
For all the tables, to input a record, navigate to /api/plane or flight, or airport. 
Add all necessary column names and information in the body (json format)
To enter a date: "YYYY-MM-DD" with quotes

*** PUT ***
YOU CAN ONLY UPDATE THE AIRPORTS AND PLANES TABLES.
You can update any and all information desired in those tables. except of course the id's.

*** DELETE ***
You can delete any record as long as its not a foreign key being used in the flights table. 

