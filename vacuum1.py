rooms = {"A": "Dirty", "B": "Dirty"}

location = input("Enter starting room (A/B): ").upper()

if location not in rooms:
    location = "A"

while "Dirty" in rooms.values():

    print("\nAgent is in room:", location)
    print("Room status:", rooms[location])

    if rooms[location] == "Dirty":
        print("Action: SUCK")
        rooms[location] = "Clean"

    elif location == "A":
        print("Action: MOVE RIGHT")
        location = "B"

    else:
        print("Action: MOVE LEFT")
        location = "A"

print("\nBoth rooms are clean.")
print("Final status:", rooms)