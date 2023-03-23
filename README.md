# Tennis court reservation system

The aim of this program is to make, cancel or check current reservations for a tennis court.
There is also an option for saving the schedule to CSV or JSON.

## Third-party libraries

- pandas - for creating a DataFrame and making easy data manipulation, also for reading/saving files
- datetime - for date and time manipulations

## Comments

- The program is loading "local_storage.csv" which contains already some reservations (I used the example .csv file that you uploaded). When the local storage is not avaialable, it is creating an empty DataFrame object with defined columns.

- After adding or deleting a reservation, "local_storage.csv" is automatically updated.

- I do not have unit tests, but I provided some .txt files that can be copy-pasted into the console.

- The program is taking the current date and time for cheking the case "The date user gives is less than one hour from now" in deleting and adding a reservation.

- It is also taking the current day for showing "Today" or "Tomorrow" when printing the schedule.

- I have assumed that the tennis court is open between 9 a.m. and 20 p.m.

## How to use

### Example of "Make a reservation":
    
    $ Make a reservation
    
    What's your Name? { Name Surname }
    
    $ Marcel Boxberger
    
    When would you like to book? {DD.MM.YYYY HH:MM}
    
    $ 26.03.2023 13:30 
    
    The time you chose is unavailable, would you like to make a reservation for 14:00:00 instead? (yes/no)
    
    $ Yes
    
    How long would you like to book court?
    1) 30 Minutes
    2) 60 Minutes
    3) 90 Minutes
    
    $ 60
    
    Reservation succesfully added!
    
### Example of "Cancel reservation":
    
    $ Cancel reservation
    
    Whats your name? { Name Surname }
    
    $ Marcel Boxberger
    
    Enter the date which you want to cancel. { DD.MM.YYYY HH:MM }
    
    $ 26.03.2023 14:00
    
    Reservation succesfully cancelled!
    
### Example of "Print schedule":
    
    $ Print schedule
    
    Enter the start date { DD.MM.YYYY }:
    
    $ 23.03.2023
    
    Enter the end date { DD.MM.YYYY }:
    
    $ 24.03.2023

    Today:
    * Michał Najman 2023-03-23 14:00:00 - 2023-03-23 15:00:00
    * Marcin Wiśniewski 2023-03-23 17:00:00 - 2023-03-23 18:00:00

    Tomorrow:
    * Tadeusz Stockinger 2023-03-24 11:00:00 - 2023-03-24 12:30:00
    * Robert Brzozowski 2023-03-24 12:30:00 - 2023-03-24 14:00:00
    * Norman Dudziuk 2023-03-24 16:30:00 - 2023-03-24 17:00:00
    
### Example of "Save schedule to a file":
    
    $ Save schedule to a file

    In which format should it be saved? (Type CSV or JSON) 
    1) CSV
    2) JSON

    $ CSV

    Enter the name of the file:

    $ schedule1

    Schedule succesfully saved!
