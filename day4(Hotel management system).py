#  Hotel Management Mini Project

#  Tuple (Fixed hotel information)
hotel_info = ("Royal Palace Hotel", "Lahore", 5)
print("Hotel Info:", hotel_info)

#  List (Available room numbers)
available_rooms = [101, 102, 103, 104]
print("\nAvailable Rooms:", available_rooms)

#  Dictionary (Guest records)
guests = {}

#  Set (Unique services offered)
services = {"WiFi", "Breakfast", "Parking", "WiFi"}
print("\nHotel Services:", services)

# ---- Booking Process ----
print("\n--- Room Booking ---")

name = input("Enter guest name: ")
room = int(input("Enter room number to book: "))

if room in available_rooms:
    guests[name] = {
        "room": room,
        "services": list(services)
    }
    available_rooms.remove(room)
    print("Room booked successfully!")
else:
    print("Room not available!")

# ---- Show Final Records ----
print("\nUpdated Available Rooms:", available_rooms)
print("\nGuest Records:")
print(guests)
