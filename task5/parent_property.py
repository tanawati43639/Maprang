# Copy and paste the Property class from the previous task
from abc import ABC, abstractmethod
from typing import Tuple, List, Union
from amenity import Amenity
import math
from pprint import pprint


class Property(ABC):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_area: int,
                        price: int, 
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
            
        self.prop_id = prop_id
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms 
        self.parking_spaces = parking_spaces 
        self.full_address = full_address
        self.floor_area = floor_area
        self.price = price
        self.property_features = property_features
        self.coordinates = coordinates

    def get_prop_id(self) -> str:
        return self.prop_id

    def get_full_address(self) -> str:
        return self.full_address

    def get_suburb(self) -> str:
        self.suburb = self.full_address.split(' ')[-3]
        return self.suburb
     
    @abstractmethod
    def get_prop_type(self) -> str:
        pass
    
    def set_bedrooms(self, bedrooms: int) -> None:
        #validation 
        if self.bedrooms.isdigit():
            self.bedrooms = bedrooms
        else:
            print ("Bedroom must be a digit")
    
    def get_bedrooms(self) -> int:
        return self.bedrooms
    
    def set_bathrooms(self, bathrooms: int) -> None:
        #validation
        if self.bathrooms.isdigit():
            self.bathrooms = bathrooms
        else:
            print ("Bathroom must be a digit")
    
    def get_bathrooms(self) -> int:
        return self.bathrooms
    
    def set_parking_spaces(self, parking_spaces: int) -> None:
        #validation
        if self.parking_spaces.isdigit():
            self.parking_spaces = parking_spaces
        else:
            print ("Parking space must be a digit")

    def get_parking_spaces(self) -> int:
        return self.parking_spaces
    
    def get_coordinates(self) -> Tuple[float, float]:
        return self.coordinates
    
    @abstractmethod
    def set_floor_number(self, floor_number: int) -> None:
        pass
        
    @abstractmethod
    def get_floor_number(self) -> Union[int,None]:
        pass
    
    @abstractmethod
    def set_land_area(self, land_area: int) -> None:
        pass

    @abstractmethod
    def get_land_area(self) -> Union[int,None]:
        pass

    def set_floor_area(self, floor_area: int) -> None:
        if self.floor_area.isdigit():
            self.floor_area = floor_area
        else:
            print ("Floor area must be a number")            
    
    def get_floor_area(self) -> int:
        return self.floor_area

    def set_price(self, price: int) -> None:
        if self.price.isdigit():
            self.price = price
        else:
            print ("Price must be a number")
    
    def get_price(self) -> int:
        return self.price
    
    def set_property_features(self, property_features: List[str]) -> None:
        self.property_features = property_features
    
    def get_property_features(self) -> List[str]:
        return self.property_features
    
    def add_feature(self, feature: str) -> None:
        if feature not in self.property_features:
            self.property_features.append(feature)
    
    def remove_feature(self, feature: str) -> None:
        if feature in self.property_features:
            self.property_features.remove(feature)

    def nearest_amenity(self, amenities: List[Amenity],amenity_type: str, amenity_subtype: str = None) -> Tuple[Amenity, float]:
        # distance_2 = 100
        # nearest_amenity = None
        list_amenity = []   #Add
        prop_lat = self.coordinates[0]
        prop_long = self.coordinates[1]

        for amenity in amenities:
            if amenity.amenity_type == amenity_type:
                #if amenity is not None:
                amen_lat, amen_long = amenity.get_amenity_coords()
                distance = (self.__haversine_distance(prop_lat, prop_long, amen_lat, amen_long))
                list_amenity.append({'amenity':amenity, 'distance':distance})
                # if distance_1 < distance_2:
                #     distance_2 = distance_1
                #     nearest_amenity = amenity
    

        list_amenity.sort(key=lambda element: element['distance'])
        pprint(list_amenity)
        return list_amenity[0]['amenity'], list_amenity[0]['distance']
        #return nearest_amenity, distance_2
    
    

    def __haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        radius_of_earth = 6371  # Radius of the earth in kilometers.
        distance = radius_of_earth * c

        return distance
    

if __name__ == '__main__':
    pass




