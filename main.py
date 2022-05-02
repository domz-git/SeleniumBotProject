from booking.booking import Booking

inst = Booking()
inst.land_page()
inst.accept_cookies()
inst.change_currency(currency='GBP')
inst.destination(destination='New York')
inst.dates(date_check_in='2022-05-17', date_check_out='2022-06-18')
inst.sleep()