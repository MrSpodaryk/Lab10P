from park import Park

park1 = Park()
park2 = Park("Стрийський парк", 500, 666, 5000)
park3 = Park("Парк 700річчя Львова", 325.5, 13.2, 2300, 923, True)

print(park1)
print(park2)
print(park3)

print("\n", Park.counter)

Park.add_to_counter(3)

print("\n", Park.counter)
