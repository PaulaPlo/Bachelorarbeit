import traci
import sumolib

sumoBinary = sumolib.checkBinary("sumo")

traci.start([
    sumoBinary,
    "-c",
    "simulation.sumocfg"
])

for step in range(10):

    traci.simulationStep()

    vehicles = traci.vehicle.getIDList()

    if len(vehicles) > 0:

        firstVehicle = vehicles[0]

        speed = traci.vehicle.getSpeed(firstVehicle)

        print(
            f"Schritt {step}: "
            f"Fahrzeug {firstVehicle} "
            f"fährt {speed:.2f} m/s"
        )

traci.close()