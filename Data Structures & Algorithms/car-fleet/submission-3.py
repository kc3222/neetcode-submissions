class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort the cars
        # Compare two cars, if the earlier car has a slower speed, calculate if they will meet before target
        # If they meet, calculate if they will meet for the next car
        position, speed = zip(*sorted(zip(position, speed), reverse=True))
        fleets = [(position[0], speed[0])]
        for i in range(1, len(position)):
            currentFleetPos, currentFleetSpeed = fleets.pop()
            currentFleetSteps = (target - currentFleetPos) / currentFleetSpeed
            currentCarSteps = (target - position[i]) / speed[i]
            if currentFleetSteps >= currentCarSteps:
                fleets.append((currentFleetPos, currentFleetSpeed)) # Same fleet
            else:
                fleets.append((currentFleetPos, currentFleetSpeed))
                fleets.append((position[i], speed[i]))
        return len(fleets)