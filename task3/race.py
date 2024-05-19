from custom_errors import *
from abc import ABC, abstractmethod
from runner import Runner
import math

class Race(ABC):
    def __init__(self, distance, runners = None):

        # if runners is not None:
        #     raise CustomTypeError('Runners must be none')
        self.runners = []
        
        self.race_type = self.race_type
        if type(self.race_type) is not str:
            raise CustomTypeError('Race Type must be string')

        if type(distance) is not float: 
            raise CustomTypeError('Distance must be float')
        if distance < 0:
            raise CustomValueError('Distanct less than 0')    
        self.distance = distance

        if type(self.maximum_participants) is not int:
            raise CustomTypeError('Maximum participants Type must be integer')
        self.maximum_participants = self.maximum_participants
            
    def add_runner(self, runner):
        if runner in self.runners:
            raise RunnerAlreadyExistsError('This runner already existed')
        
        self.runners.append(runner)
        if len(self.runners) > self.maximum_participants:
            raise RaceIsFullError('A race is full, cannot add new runner')

    def remove_runner(self, runner):
        if runner not in self.runners:
            raise RunnerDoesntExistError('This runner does not exist in the list')
        else:
            self.runners.remove(runner)
    
    def conduct_race(self):
        result = []
        if self.race_type == "short":
            for i, runner in enumerate(self.runners):
                time_taken = runner.run_race("short", 1.0) * 1.2
                result.append((runner, time_taken))
        elif self.race_type == "long":
            for i, runner in enumerate(self.runners):
                time_taken = 0
                for km in range(math.ceil(self.distance)):
                    if runner.energy > 0:
                        time_taken += runner.run_race("long", self.distance)
                        runner.drain_energy(100)
                    else:
                        time_taken = 'DNF'
                        break
                result.append((runner, time_taken))
        return result

class ShortRace(Race):
    race_type = "short"
    maximum_participants = 8
    time_multiplier = 1.2

class MarathonRace(Race):
    race_type = "long"
    maximum_participants = 16
    energy_per_km = 100

      
if __name__ == '__main__':
    short_race = ShortRace(0.5)
    long_race = MarathonRace(5.0)

    # Add a Runner
    eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    rup = Runner('Rupert', 23, 'Australia', 2.3, 1.9)

    long_race.add_runner(eli)
    long_race.add_runner(rup)

    results = long_race.conduct_race()
    for runner, time in results:
        print(runner.name, int(time+0.5)) 

