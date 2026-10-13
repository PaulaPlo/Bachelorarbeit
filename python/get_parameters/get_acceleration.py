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

        acceleration = traci.vehicle.getAcceleration(firstVehicle)

        print(
            f"Schritt {step}: "
            f"Fahrzeug {firstVehicle} "
            f"beschleunigt {acceleration:.2f} m/s^2"
        )

traci.close()