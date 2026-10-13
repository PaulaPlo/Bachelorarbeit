import traci
import sumolib

sumoBinary = sumolib.checkBinary("sumo")
simulationConfig = "../sumo/simulation.sumocfg"

traci.start([
    sumoBinary,
    "-c",
    simulationConfig
])

for step in range(10):

    traci.simulationStep()

    vehicles = traci.vehicle.getIDList()

    if len(vehicles) > 0:

        firstVehicle = vehicles[0]

        position = traci.vehicle.getPosition(firstVehicle)

        print(
            f"Schritt {step}: "
            f"Fahrzeug {firstVehicle} "
            f"Position = {position}"
        )

traci.close()