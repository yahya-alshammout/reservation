from hotel import Hotel
from customer import Customer
from reservations import Reservation
#from notification import Notification

class Tester():

	hotel1 = Hotel(1, "Rotana", "Amman", 300, 50)
	hotel12 = Hotel(2, "Royal", "Amman", 250, 35)
	print hotel1.add_hotel()
	print hotel1.list_hotels_in_city()

	customer1 = Customer("Yahya")
	print customer1.add_customer()

	reservation1 = Reservation("Rotana", "Yahya", "+962779148786")
	print reservation1.reservation_list_in_hotel()
	#messeag1 = Notification("confirmation", "+962779148786")
	#print reservation1.add_new_reservation()
	#print reservation1.reservation_list_in_hotel()
Tester()




