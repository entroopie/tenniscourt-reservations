import pandas as pd
from reservation import Reservation
from datetime import timedelta
from schedule import Schedule

class Manager:
    
    def __init__(self):
        self.sch = Schedule()
        self.rsv = Reservation()
       
    def start_reservation(self):
        self.rsv.set_name()
        self.make_reservation()
      
    def make_reservation(self):
        self.rsv.set_starttime()
        if self.sch.check_name(self.rsv.get_name(), self.rsv.get_starttime()):
            print('You cannot have more than 2 reservations this week.\n')
        else:
            if self.sch.validate_date(self.rsv.get_starttime()):
                self.rsv.set_endtime(self, self.rsv.get_starttime())
                self.sch.append_reservation(self.rsv.get_name(), self.rsv.get_starttime(), self.rsv.get_endtime())
            else:
                self.alternative_proposition(self.rsv.get_starttime())
     
    def cancel_reservation(self):
        cancel_time = self.rsv.get_cancel_time()
        if cancel_time != None:
            self.sch.delete_reservation(cancel_time, self.rsv.get_name())
    
    def print_schedule(self):
        while True:
            try:
                start = pd.to_datetime(input('Enter the start date { DD.MM.YYYY }:\n'), dayfirst = True)
                end = pd.to_datetime(input('Enter the end date { DD.MM.YYYY }:\n'), dayfirst = True)
                break
            except:
                print('Invalid date. Try again.')
        self.sch.print_reservations(start, end)
            
    def save_schedule(self):
        try:
            choice = input('In which format should it be saved? (Type CSV or JSON) \n1) CSV \n2) JSON\n')
            assert choice in ['CSV', 'JSON']
        except:
            print('Invalid choice.')
            return None
        self.sch.save_to_file(choice)
        
    def choose_booking(self, duration):
        while True:
            print('How long would you like to book court?')
            try:
                if duration < 59:
                    time = int(input('1) 30 Minutes\n'))
                elif duration < 89:
                    time = int(input('1) 30 Minutes\n2) 60 Minutes\n'))
                else:
                    time = int(input('1) 30 Minutes\n2) 60 Minutes\n3) 90 Minutes\n'))
                assert time in [30, 60, 90]
                return time
            except:
                print('Invalid number of minutes. Try again.')
                
    def alternative_proposition(self, tmp):
        while True:
            proposition = self.sch.get_closest_end(tmp)
            if self.sch.validate_date(proposition):
                decision = input('The time you chose is unavailable, would you like to make a reservation for {} instead? (yes/no)\n'.format(proposition.time()))
                if decision in ['yes', 'Yes']:
                    self.rsv.set_endtime(self, proposition)
                    self.sch.append_reservation(self.rsv.get_name(), proposition, self.rsv.get_endtime())
                    break
                else:
                    self.make_reservation()
                    break
            else:
                tmp = proposition + timedelta(minutes = 1)