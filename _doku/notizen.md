======= STAND DER TECHNIK ===================================================================================
======= AUFBAU DER VERKEHRSSIUMLATION =======================================================================
 
TraCI: Traffic COntrol Interface
Programmierschnittstelle zwischen Python und Sumo

simulation.sumocfg:
- zentrale Konfigurationsdatei der Simulation
- verbindet Straßennetz, Fahrzeugrouten, den zu simulierenden Zeitraum

net.net.xml:
- Informationen zu:
    - Straßenabschnitte (Edges)
    - Fahrstreifen (Lanes)
    - Knotenpunktek (Junctions)
    - zulässige Fahrbeziehungen
    - Geschwindigkeiten
    - gegebenenfalls Lichtsignalanlagen
- Erzeugung aus map.osm durch netconvert
- Kommandozeile: sumo-gui -n net.net.xml

route-files:
- mehrere Routendatei für eine Simulation zulässig
- Bedeutung:
    - vehicle: definiert ein Fahrzeug
    - id = "0" gibt dem Fahrzeug eine eindeutige Kennung
    - depart = "0.00" legt den gewünschten Abfahrtszeitpunkt fest
    - route beschreibt die zu befahrende Strecke
    - edges = "..." ehthält die Folge der Straßenabschnitte
- Fahrzeuge müssen nach ihren Abfahrtrs- oder Beginnzeiten sortiert sein, weil Sumo Routendateien schrittweise einliest.
- Beschreibt nicht das Straßennetz, sondern die Nutzung des Netzes durch Verkehrsteilnehmende

Ordnerstruktur:
configuration --> sumocfg & Startdateien
corridor --> Netzreduktion
demand --> Hintergrundverkehr
infrastructure --> Haltestellen, Detektoren, Additional Files
net --> Straßennetz
output --> Simulationsergebnisse

======= FAHRERMODELLENTWICKLUNG =============================================================================

Relevante Größen für das Fahrermodell:
- Zeit
- Geschwindigkeit
- Position/Streckenfortschritt
- Höhenprofil?
daraus ergibt sich:
- Beschleunigung
- Leistungsbedarf
- Drehmomentbedarf

======= IMPLEMENTIERUNG IN STEUERGERÄT ======================================================================