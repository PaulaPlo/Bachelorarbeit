======= STAND DER TECHNIK ===================================================================================
======= AUFBAU DER VERKEHRSSIUMLATION ======================================================================
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


Corridor-Festlegung:
Tiefe 0: Linie 1 --> Tiefe 1: direkte Einmündungen/Nachbar-Edges --> Tiefe 2: Nachbarn dieser Edges --> Tiefe 3: nochmal deren Nachbarn
outgoing: alle Edges, auf die man von A weiterfahren kann
incomig: alle Edges, von denen man nach B fahren kann
- pyhton Datei ausführen
- txt in net convertieren: netconvert --sumo-net-file "../../net/osmnew.net.xml" --keep-edges.input-file "keep_edges_depth3.txt" -o "corridor_depth3.net.xml"

Einbezug des Höhenprofils/der Topographie:
Datengrundlage: Digitales Geländemogell (DGM/DEM), möglichst als GeoTIFF
- convert-Befehl: netconvert --sumo-net-file "corridor_depth3.net.xml" --heightmap.geotiff "passau_dgm1.tif" -o "corridor_depth3_elevation.net.xml"


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