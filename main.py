import manager as mng

system = mng.Manager()

options = {
    'Make a reservation': system.start_reservation,
    'Cancel reservation': system.cancel_reservation,
    'Print schedule': system.print_schedule,
    'Save schedule to a file': system.save_schedule
}

while True:
    opt = input("What you want to do: \n1) Make a reservation \n2) Cancel reservation \n3) Print schedule\n4) Save schedule to a file\n5) Exit\n")
    if opt == 'Exit':
        exit()
    else:
        try:
            options.get(opt)()
        except:
            print('Invalid option. Try again.')
        