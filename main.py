from booking.booking import Booking
from booking.filtration import Filtration

booking = Booking()
filtration = Filtration()
booking.land_page()
booking.accept_cookies()
booking.change_currency(currency='GBP')
booking.destination(destination='New York')
booking.dates(date_check_in='2022-05-17', date_check_out='2022-06-18')
booking.adults(count=3)
booking.search()
booking.filtration()
booking.sleep()