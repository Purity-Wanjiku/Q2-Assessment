# QStn.5
# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        calculate_value = self.price * self.quantity
        return f"The Total Value of {self.name} is {calculate_value}"
    
product1 = Product(name="Banana",price=30,quantity=10)
result = product1.total_value()
print(result)

product2 = Product(name="Apple",price=100,quantity=5)
result2 = product2.total_value()
print(result2)

product3 = Product(name="Melon",price=24,quantity=9)
result3 = product3.total_value()
print(result)

product4 = Product(name="Grape",price=120,quantity=13)
result4 = product4.total_value()
print(result4)

product5 = Product(name="Orange",price=60,quantity=20)
result5 = product5.total_value()
print(result5)


# QStn. 8 
# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
      
      
library =[]
class LibraryCatalog:
    def __init__(self,title,author,copy):
        self.title = title
        self.author = author
        self.copy = copy
        # self.description = description

    def add_book(self):
        all_infor = f"{self.title}, {self.author},{self.copy}"
        library.append(all_infor)
        
    def search_book(self,book_title):
        for item in library:
         if (book_title == item.title):
             return item.author
         
   
book1 = LibraryCatalog(title="River",author="Margret Ogola",copy=30)
book1.add_book()
x = book1.search_book("Born")
print(x)
print(library)

book2 = LibraryCatalog("Born","Trevor Noah",300)
book2.add_book()
print(library)


# Qstn. 7
# Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.

class FlightBoooking:
    def __init__(self, passenger_name,destination,date,total_seats):
        self.passenger_name = passenger_name
        self.destination = destination
        self.date = date
        self.total_seats = total_seats
        
    def occupy_seat(self,occupied_seats):
            self.total_seats -= occupied_seats
            return f"The total seats available for booking are {self.total_seats}"
        
    def reserve_seat(self,seat_no):
        if seat_no <= self.total_seats:
            return f"{self.passenger_name} has booked {seat_no} seats"
        if seat_no >self.total_seats:
            return f"The passenger cannot book flight since {self.total_seats} seats are left for booking"
    
        
flight1 = FlightBoooking("Rita","Wajir",2,40)
results = flight1.occupy_seat(40)
results2 = flight1.reserve_seat(3)
print(results)
print(results2)
        
         
    
      