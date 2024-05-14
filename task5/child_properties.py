# Copy and Paste the House and Apartment classes from the previous task
from typing import Tuple, List, Union
from parent_property import Property

class House(Property):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        land_area: int, 
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        
        super().__init__(prop_id, bedrooms, 
                         bathrooms, 
                         parking_spaces, 
                         full_address, 
                         floor_area, 
                         price, 
                         property_features,
                         coordinates
                         )
        
        self.land_area = land_area

    def get_prop_type(self) -> str:
        return "house"

    def set_floor_number(self, floor_number: int) -> None:
        pass

    def get_floor_number(self) -> Union[int, None]:
        return None
    
    def set_land_area(self, land_area: int) -> None:
        self.land_area = land_area
        
    def get_land_area(self) -> Union[int, None]:
        return self.land_area
    
class Apartment(Property):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_number: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        
        super().__init__(prop_id, bedrooms, 
                         bathrooms, 
                         parking_spaces, 
                         full_address, 
                         floor_area, 
                         price, 
                         property_features,
                         coordinates
                         )
        
        self.floor_number = floor_number

    def get_prop_type(self) -> str:
        return "apartment"
        
    def set_floor_number(self, floor_number: int) -> None:
        self.floor_number = floor_number
    def get_floor_number(self) -> Union[int,None]:
        return self.floor_number 

    def set_land_area(self, land_area: int) -> None:
        pass
    def get_land_area(self) -> Union[int, None]:
        return None

if __name__ == '__main__':
    pass


