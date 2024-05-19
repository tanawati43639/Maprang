from custom_errors import *
from abc import ABC, abstractmethod
from runner import Runner
import math

class Race(ABC):
    def __init__(self, distance, runners = None):
        
        # if (runners) is not None:
        #     raise CustomTypeError('runners Type must be string')
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
            
    def add_runner(self, runner):
        if runner in self.runners:
            raise RunnerAlreadyExistsError('This runner already existed')
        self.runners.append(runner)
        if len(self.runners) > 16:
            print('A race is full, cannot add new runner')
            #raise RaceIsFullError('A race is full, cannot add new runner')
        

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
    # short_race = ShortRace(0.5)
    long_race = MarathonRace(5.0,[])

    # # Add a Runner
    # eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    rup1 = Runner('Rupert1', 23, 'Australia', 2.3, 1.9)
    rup2 = Runner('Rupert2', 23, 'Australia', 2.3, 1.9)
    rup3 = Runner('Rupert3', 23, 'Australia', 2.3, 1.9)
    rup4 = Runner('Rupert4', 23, 'Australia', 2.3, 1.9)
    rup5 = Runner('Rupert5', 23, 'Australia', 2.3, 1.9)
    rup6 = Runner('Rupert6', 23, 'Australia', 2.3, 1.9)
    rup7 = Runner('Rupert7', 23, 'Australia', 2.3, 1.9)
    rup8 = Runner('Rupert8', 23, 'Australia', 2.3, 1.9)
    rup9 = Runner('Rupert9', 23, 'Australia', 2.3, 1.9)
    rup10 = Runner('Rupert10', 23, 'Australia', 2.3, 1.9)
    rup11 = Runner('Rupert11', 23, 'Australia', 2.3, 1.9)
    rup12 = Runner('Rupert12', 23, 'Australia', 2.3, 1.9)
    rup13 = Runner('Rupert13', 23, 'Australia', 2.3, 1.9)
    rup14 = Runner('Ruper14', 23, 'Australia', 2.3, 1.9)
    rup15 = Runner('Rupert15', 23, 'Australia', 2.3, 1.9)
    rup16 = Runner('Rupert16', 23, 'Australia', 2.3, 1.9)
    rup17 = Runner('Rupert16', 23, 'Australia', 2.3, 1.9)


    # long_race.add_runner(eli)
    long_race.add_runner(rup1)
    long_race.add_runner(rup2)
    long_race.add_runner(rup3)
    long_race.add_runner(rup4)
    long_race.add_runner(rup5)
    long_race.add_runner(rup6)
    long_race.add_runner(rup7)
    long_race.add_runner(rup8)
    long_race.add_runner(rup9)
    long_race.add_runner(rup10)
    long_race.add_runner(rup11)
    long_race.add_runner(rup12)
    long_race.add_runner(rup13)
    long_race.add_runner(rup14)
    long_race.add_runner(rup15)
    long_race.add_runner(rup16)
    long_race.add_runner(rup17)


    results = long_race.conduct_race()
    print(len(results),results[16][0].name)
    # for runner, time in results:
    #     print(runner.name, time) 


