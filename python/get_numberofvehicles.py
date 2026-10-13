import traci
import sumolib

# gibt quasi Pfad aus wo sumo.exe liegt
sumoBinary = sumolib.checkBinary("sumo")

# Befehl: Starte SUMO und verbinde Python mit der laufenden Simulation
traci.start([
    sumoBinary,
    "-c",
    "simulation.sumocfg"
])

print("Simulation gestartet\n")

for step in range(10):

    # Berechne genau einen Simulationsschritt
    traci.simulationStep()

    # Fragt sumo, welche Fahrzeuge sich gerade im Netz befinden
    vehicles = traci.vehicle.getIDList()

    print(
        f"Zeitschritt {step}: "
        # Zählt dann die Anzahl der ELemente in der IDList
        f"{len(vehicles)} Fahrzeuge aktiv"
    )