import math
import timeit
# Linked list implementation
class Node:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.next = None

    def getName(self):
        return self.name

    def getCoordinates(self):
        return self.latitude, self.longitude

    def setCoordinates(self, newLatitude, newLongitude):
        self.latitude = newLatitude
        self.longitude = newLongitude

    def setNext(self, newNext):
        self.next = newNext

    def getNext(self):
        return self.next


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insert(self, item_name, item_latitude, item_longitude):
        temp = Node(item_name, item_latitude, item_longitude)
        temp.setNext(self.head)
        self.head = temp
        
    def delete_by_name(self, item_name):
        current = self.head
        previous = None
        found = False

        # Search
        while current != None:
            if current.getName() == item_name:
                break       
            else:
                previous = current
                current = current.getNext()

        # Remove
        if previous == None:
            self.head = current.getNext()
        elif current == None:
            print(f"There is not record match city name: {item_name} for deleting")
        else:
            previous.setNext(current.getNext())

    def delete_by_coordinates(self, item_latitude, item_longitude):
        current = self.head
        previous = None

        # Search
        while current != None:
            if current.getCoordinates() == (item_latitude, item_longitude):
                break
            else:
                previous = current
                current = current.getNext()

        # Remove
        if previous == None:
            self.head = current.getNext()
        elif current == None:
            print(f"There is not record match coordinates ({item_latitude}, {item_longitude}) for deleting")
        else:
            previous.setNext(current.getNext())

    def search_by_name(self, item_name):
        current = self.head
        while current != None:
            if current.getName() == item_name:
                break
            else:
                current = current.getNext()
        
        if current == None:
            return f"There is not record for city: {item_name}"
        return current.getCoordinates()

    def search_by_coordinates(self, item_latitude, item_longitude):
        current = self.head
        while current != None:
            if current.getCoordinates() == (item_latitude, item_longitude):
                break
            else:
                current = current.getNext()
        
        if current == None:
            return f"There is not record for coordinates: ({item_latitude}, {item_longitude})"
        return current.getName()

    def search_in_distance(self, item_name, distance):
        city_latitude, city_longitude = self.search_by_name(item_name)
        current = self.head
        records = ""
        while current != None:
            current_latitude, current_longitude = current.getCoordinates()
            distance_between_cities = math.sqrt((current_latitude - city_latitude)**2 + (current_longitude - city_longitude)**2)
            if 0 < distance_between_cities <= distance:
                records = records + f"city: {current.getName()}, coordinates: {current.getCoordinates()}\n"
            current = current.getNext()
        
        # remove last newline
        return records.rstrip()

def insert_time():
    SETUP_CODE = '''
from __main__ import UnorderedList
city_database = UnorderedList()'''
    TEST_CODE = '''city_database.insert("Hue", 16, 107)'''
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10)
    print(f"Insert time: {min(times)}")

def delete_by_name_time():
    SETUP_CODE = '''
from __main__ import UnorderedList
city_database = UnorderedList()
city_database.insert("Hue", 16, 107)
'''
    TEST_CODE = '''city_database.delete_by_name("Hue")'''
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=1)
    print(f"Delete by name time: {min(times)}")

def delete_by_coordinates_time():
    SETUP_CODE = '''
from __main__ import UnorderedList
city_database = UnorderedList()
city_database.insert("Hue", 16, 107)
'''
    TEST_CODE = '''city_database.delete_by_coordinates(16, 107)'''
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=1)
    print(f"Delete by coordinates time: {min(times)}")

def search_by_name_time():
    SETUP_CODE = '''
from __main__ import UnorderedList
city_database = UnorderedList()
city_database.insert("Hue", 16, 107)
'''
    TEST_CODE = '''city_database.search_by_name("Hue")'''
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
    print(f"Search by name time: {min(times)}")

def search_by_coordinates_time():
    SETUP_CODE = '''
from __main__ import UnorderedList
city_database = UnorderedList()
city_database.insert("Hue", 16, 107)
'''
    TEST_CODE = '''city_database.search_by_coordinates(16, 107)'''
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
    print(f"Search by coordinates time: {min(times)}")

def search_in_distance_time():
    SETUP_CODE = '''
from __main__ import UnorderedList
city_database = UnorderedList()
city_database.insert("Hue", 16, 107)
city_database.insert("Hochiminh city", 11, 106)
city_database.insert("Hanoi", 21, 105)
'''
    TEST_CODE = '''city_database.search_in_distance("Hue", 50)'''
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10000)
    print(f"Search in distance time: {min(times)}")

if __name__ == "__main__":
    # Test
    city_database = UnorderedList()
    print(f"Is city database empty: {city_database.isEmpty()}")

    # Insert
    city_database.insert("Helsinki", 60, 24)
    city_database.insert("Kokkola", 63, 23)
    city_database.insert("Tampere", 61, 23)
    city_database.insert("Hochiminh city", 11, 106)
    city_database.insert("Hanoi", 21, 105)
    city_database.insert("Hue", 16, 107)
    insert_time()
    print(f"Is city database empty: {city_database.isEmpty()}")

    # Search by name
    search_by_name_time()
    print(f"Coordinates of Helsinki is: {city_database.search_by_name('Helsinki')}")

    # Search by coordinates
    search_by_coordinates_time()
    print(f"Search by coordinates of (11,106): {city_database.search_by_coordinates(11, 106)}")

    # Delete by name
    delete_by_name_time()
    city_database.delete_by_name("Tampere")
    print(city_database.search_by_name("Tampere"))
    city_database.delete_by_name("Tampere")

    # Delete by coordinates
    delete_by_coordinates_time()
    city_database.delete_by_coordinates(63, 23)
    print(city_database.search_by_name("Kokkola"))
    city_database.delete_by_coordinates(63, 23)

    # Print all records within a given distance from a specific city
    search_in_distance_time()
    records = city_database.search_in_distance("Hue", 50)
    print("List of cities from Hue in disance of 50:")
    print(records)