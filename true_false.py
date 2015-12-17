def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475
def rental_car_cost(days):
    car_cost=days*40
    if days>=7:
         car_cost-=50
    elif days>=3:
        car_cost-=20
    return car_cost
    
def trip_cost(city,days):
    def add(rental_car_cost, hotel_cost,plane_ride_cost):
        return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)
trip_cost("Los Angeles",4)
