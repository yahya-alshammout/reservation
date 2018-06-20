from controllers.hotel import *
from controllers.customer import *
from controllers.reservations import *
from controllers.notification import *
from controllers.main import *
from controllers.tester import *
from django.http import HttpResponse


def InitializeData(request):
    return HttpResponse("Welcome to My program Hotels_Reservation")
def HotelList(request):
    start_app()
    hotel_list = Hotel.hotels
    hotel_list_output = "<ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + h[1] + "</li>"
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output)


def HotelInCity(request):
    start_app()
    hotel_list = Hotel.list_hotels_in_city()
    hotel_list_output = "<ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + h[0] + "</li>" + "<li>" + str(h[1]) + "</li>"
    hotel_list_output += "/ul"
    return HttpResponse(hotel_list_output)

def ReservationList(request):
    reserv = Reservation()
    reservation_list = reserv.reservation_list_in_hotel()
    reservation_list_output = "<ul>"
    for h in reservation_list:
        reservation_list_output += "<li>" + h[0] + "<li>"
    return HttpResponse(reservation_list_output)





