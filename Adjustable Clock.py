# Parsa Vetry
# The purpose of this program is to have a clock that starts at 00:00:00 and the user is supposed to change the time accordingly.

class clock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    def print_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
    def change_time(self):
        try:
            hours = int(input("Enter hours:"))
            if not 0 <= hours < 24:
                raise ValueError("Invalid hour value (must be 0-23)")
            minutes = int(input("Enter minutes:"))
            if not 0 <= minutes < 60:
                raise ValueError("Invalid minute value (must be 0-59)")
            seconds = int(input("Enter seconds:"))
            if not 0 <= seconds <60:
                raise ValueError("Invalid second value (must be 0-59)")
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            print("The new time is ", end = '')
        except ValueError as excpt:
            print(excpt)
            print ("Could not change the time")
            
time = clock()
time.change_time()
time.print_time()
    

