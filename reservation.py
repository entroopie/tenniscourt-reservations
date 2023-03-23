import pandas as pd
from datetime import datetime, timedelta

class Reservation:
    
    def __init__(self):
        self.name = None
        self.start_time = None
        self.end_time = None
    
    def set_starttime(self):
        while True:
            try:
                self.start_time = pd.to_datetime(input('When would you like to book? {DD.MM.YYYY HH:MM}\n'), dayfirst = True)
            except:
                print('Invalid date. Try again.')
                continue
            now = datetime.now()
            if ((self.start_time - now).total_seconds() / 3600) < 1:
                print('The chosen time is less than one hour from now. Try again.')
            elif self.start_time.hour >= 20 or self.start_time.hour < 9:
                print('The tennis court is closed at this time. Try again.')
            else: 
                break
      
    def set_endtime(self, manager, start_time):
        if manager.sch.get_duration(start_time):
            duration = 90
        else:
            ind = manager.sch.get_closest_start(start_time)
            duration = (ind - start_time).total_seconds() / 60
        if duration >= 90:
            close_time = start_time
            close_time = close_time.replace(hour = 20, minute = 0)
            duration = (close_time - start_time).total_seconds() / 60
        time = manager.choose_booking(duration)
        self.end_time = start_time + timedelta(minutes = time)
    
    def set_name(self):
        self.name = input('Whats your name? { Name Surname }\n')
        
    def get_cancel_time(self):
        while True:
            try:
                self.set_name()
                cancel_time = pd.to_datetime(input('Enter the date which you want to cancel. { DD.MM.YYYY HH:MM }\n'), dayfirst = True)
            except:
                print('Invalid date. Try again.')
                continue
            now = datetime.now()
            if ((cancel_time - now).total_seconds() / 3600) < 1:
                print('The chosen time is less than one hour from now. Cannot cancel the reservation.')
                return None
            else: break
        return cancel_time
        
    def get_starttime(self):
        return self.start_time
    
    def get_endtime(self):
        return self.end_time   
        
    def get_name(self):
        return self.name