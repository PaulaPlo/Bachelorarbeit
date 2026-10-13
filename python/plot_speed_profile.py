import pandas as pd
import matplotlib.pyplot as plt

# CSV einlesen
data = pd.read_csv("vehicle_data.csv")

# Diagramm erzeugen
plt.figure(figsize=(12, 6))

plt.plot(
    data["time"],
    data["speed"]
)

plt.title("Geschwindigkeit-Zeit-Diagramm")
plt.xlabel("Zeit [s]")
plt.ylabel("Geschwindigkeit [m/s]")

plt.grid(True)

plt.show()