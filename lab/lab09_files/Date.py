days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
class Date:
    def __init__(self, year, month=1, day=1):
       self.year=year
       self.month=month
       self.day=day
    def __str__(self):
       self.month = str(self.month)
       return "{0},{1},{2}".format(str(self.year).rjust(4,'0'),str(self.month).rjust(2,'0'),str(self.day).rjust(2,'0'))
    def same_day_in_year(self, arg):
       if str(self)==str(arg):
           return True
       return False
    def is_leap_year(self):
       if self.year%4==0:
           return True
       return False
    
    def __lt__(d1,d2):
      if d1.year > d2.year:
       return False 
      elif d1.year == d2.year and d1.month > d2.month:
       return False 
      elif d1.year == d2.year and d1.month == d2.month and d1.day >= d2.day:
       return False 
      else:
       return True



if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()
