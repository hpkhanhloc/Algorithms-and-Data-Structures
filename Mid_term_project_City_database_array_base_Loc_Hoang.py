import math
import timeit
import ctypes
#Array based implementation
class UnorderedList:
    def __init__(self):
        self.item_count = 0
        self.array_capacity = 1
        self.primary_array = self._create_array(self.array_capacity)

    def _create_array(self, array_capacity):
        # return new array with input capacity
        return (array_capacity * ctypes.py_object)()
    
    def isEmpty(self):
        return self.item_count == 0

    def insert(self, item_name, item_latitude, item_longitude):
        # create new array with input capacity and copy content of old to new array
        if self.item_count == self.array_capacity:
            temp_array = self._create_array(self.array_capacity + 1)
            for i in range(self.item_count):
                temp_array[i] = self.primary_array[i]
            self.primary_array = temp_array
            self.array_capacity = self.array_capacity + 1
        
        self.primary_array[self.item_count] = {"name": item_name, "latitude": item_latitude, "longitude": item_longitude}
        self.item_count += 1

    def delete_by_name(self, item_name):
        item_index = None
        for i in range(self.item_count):
            if self.primary_array[i]["name"] == item_name:
                item_index = i
                break
        
        if item_index == None:
            return f"There is not record matching name: {item_name} for deleting"
        
        while 0 <= item_index < self.item_count - 1:
            self.primary_array[item_index] = self.primary_array[item_index + 1]
            item_index += 1
        
        self.item_count -= 1

    def delete_by_coordinates(self, item_latitude, item_longitude):
        item_index = None
        for i in range(self.item_count):
            if self.primary_array[i]["latitude"] == item_latitude and self.primary_array[i]["longitude"] == item_longitude:
                item_index = i
                break

        if item_index == None:
            return f"There is not record matching coordinates ({item_latitude}, {item_longitude}) for deleting"
        
        while 0 <= item_index < self.item_count - 1:
            self.primary_array[item_index] = self.primary_array[item_index + 1]
            item_index += 1
        
        self.item_count -= 1
            

    def search_by_name(self, item_name):
        item_index = None
        for i in range(self.item_count):
            if self.primary_array[i]["name"] == item_name:
                item_index = i
                break
        
        if item_index == None:
            return f"There is not record matching name: {item_name}"

        return self.primary_array[item_index]["latitude"], self.primary_array[item_index]["longitude"]

    def search_by_coordinates(self, item_latitude, item_longitude):
        item_index = None
        for i in range(self.item_count):
             if self.primary_array[i]["latitude"] == item_latitude and self.primary_array[i]["longitude"] == item_longitude:
                item_index = i
                break
        
        if item_index == None:
            return  f"There is not record matching coordinates ({item_latitude}, {item_longitude})"

        return self.primary_array[item_index]["name"]

    def search_in_distance(self, item_name, distance):
        records = ""
        city_latitude, city_longitude = self.search_by_name(item_name)
        for i in range(self.item_count):
            current_latitude = self.primary_array[i]["latitude"]
            current_longitude = self.primary_array[i]["longitude"]
            distance_between_cities = math.sqrt((current_latitude - city_latitude)**2 + (current_longitude - city_longitude)**2)
            if 0 < distance_between_cities <= distance:
                records = records + f'city: {self.primary_array[i]["name"]}, coordinates: {self.primary_array[i]["latitude"]}, {self.primary_array[i]["longitude"]}\n'

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