import csv
import traci
import sumolib

sumoBinary = sumolib.checkBinary("sumo")

simulationConfig = "../sumo/simulation.sumocfg"

traci.start([
    sumoBinary,
    "-c",
    simulationConfig
])

# Öffnen der CSV-Datei
with open(
    "vehicle_data.csv",
    # w steht für write: Datei neu schreiben
    mode = "w",
    newline=""
) as file:

    # erzeugt ein Objekt, das Daten zeilenweise in die CSV schreiben kann
    writer  = csv.writer(file)

    # Kopfzeile der CSV-Datei
    writer.writerow([
        "time",
        "speed",
        "acceleration",
        "pos_x",
        "pos_y"
    ])
    step = 0
    
    while traci.simulation.getMinExpectedNumber() > 0:


        step += 1

        traci.simulationStep()

        vehicles = traci.vehicle.getIDList()

        if len(vehicles) > 0:

            vehicle = vehicles[0]

            speed = traci.vehicle.getSpeed(vehicle)

            acceleration = traci.vehicle.getAcceleration(vehicle)

            pos_x, pos_y = traci.vehicle.getPosition(vehicle)

            # Befüllen der Datenzeilen
            writer.writerow([
                step,
                speed,
                acceleration,
                pos_x,
                pos_y
            ])

traci.close()