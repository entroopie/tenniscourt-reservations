import pandas as pd
from datetime import datetime, timedelta

class Schedule:
      
    def __init__(self):
        try:
            self.data = pd.read_csv('local_storage.csv', sep = ',')
        except:
            self.data = pd.DataFrame(columns = ['name', 'start_time', 'end_time'])
        self.data['start_time'] = pd.to_datetime(self.data['start_time'])
        self.data['end_time'] = pd.to_datetime(self.data['end_time'])
      
    def append_reservation(self, name, start, end):
        new_row = {'name': name, 'start_time': start, 'end_time': end}
        self.data = self.data.append(new_row, ignore_index = True)
        print('Reservation succesfully added!')
        self.data.sort_values('start_time').to_csv('local_storage.csv', index = False)
        
    def delete_reservation(self, user_time, user_name):
        if self.data[self.data['start_time'] == user_time].empty:
            print('No reservation on given date.')
        else:
            self.data = self.data.drop(labels = self.data.index[(self.data['start_time'] == user_time) & (self.data['name'] == user_name)])
            print('Reservation succesfully cancelled!')
            self.data.sort_values('start_time').to_csv('local_storage.csv', index = False)
                
    def print_reservations(self, start, end):
        for day in range(0, (end.day - start.day) + 1):
            tmp = self.data[self.data['start_time'].dt.date == (start + timedelta(days = day))]
            self.print_day(tmp, start, day)
            if tmp.empty:
                print('No reservations')
        print()
        
    def save_to_file(self, choice):
        name = input('Enter the name of the file:\n')
        if choice == 'CSV':
            self.data.to_csv(name, index = False)
        else:
            self.data.to_json(name)
        print('Schedule succesfully saved!')
    
    def check_name(self, name, start_time):
        start_week = (start_time - timedelta(days = start_time.weekday()))
        end_week = (start_time + timedelta(days = 6 - start_time.weekday()))
        tmp = self.data[(self.data['start_time'] >= start_week) & (self.data['start_time'] <= end_week) & (self.data['name'] == name)]
        if tmp.shape[0] > 1:
            return True
        else: 
            return False
    
    def validate_date(self, tmp):
        return self.data[(self.data['start_time'] <= tmp) & (self.data['end_time'] > tmp)].empty
    
    def get_duration(self, tmp):
        return self.data[self.data['start_time'] > tmp].empty
    
    def get_closest_start(self, tmp):
        return self.data['start_time'].iloc[self.data['start_time'].searchsorted(tmp)]
    
    def get_closest_end(self, tmp):
        return self.data['end_time'].iloc[self.data['end_time'].searchsorted(tmp)]
    
    def print_day(self, data, start, day):
        now = datetime.now()
        if (start + timedelta(days = day)).date() == now.date():
            print('\nToday:')
        elif (start + timedelta(days = day)).date() == (now + timedelta(days = 1)).date():
            print('\nTomorrow')
        else:
            print('\n' + (start + timedelta(days = day)).strftime('%A') + ':')
        for ind in data.index:
            print('* ' + str(data['name'][ind]) + ' ' + str(data['start_time'][ind]) + ' - ' + str(data['end_time'][ind]))