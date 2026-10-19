import xml.etree.ElementTree as ET # Bibliothek zum Einlesen von XML-Dateien

# Route einlesen
route_file = "../../sumo/linie1/route/linie1.rou.xml"
net_file = "../../sumo/linie1/net/osmnew.net.xml"

# Route-Edges sammeln
route_tree = ET.parse(route_file) # Route-Datei öffnen
route_root = route_tree.getroot() # Hier holt man das oberstse XML-Element

route_edges = set()

for route in route_root.findall("route"): # es wird innerhalb von <routes> nach allen <route...> Elementen gesucht
    edges = route.get("edges")
    if edges:
        route_edges.update(edges.split()) # edges werden aufgelistet und dem set hinzugefügt


# Netz lesen
net_tree = ET.parse(net_file)
net_root = net_tree.getroot()

# Edge -> Nachbarn
incoming = {}
outgoing = {}

for conn in net_root.findall("connection"):
    fr = conn.get("from") # fr und to jeweils dann die dazugeörige EdgeIDs
    to = conn.get("to")

    if fr and to:
        outgoing.setdefault(fr, set()).add(to)
        incoming.setdefault(to, set()).add(fr)

# Tiefe 0
keep = set(route_edges)

# Tiefe 1
depth1 = set()

for e in route_edges:
    depth1.update(outgoing.get(e, []))
    depth1.update(incoming.get(e, []))

depth1 -= keep
keep.update(depth1)

depth2 = set()

for e in depth1:
    depth2.update(outgoing.get(e, []))
    depth2.update(incoming.get(e, []))

keep.update(depth2)

depth3 = set()

for e in depth2:
    depth3.update(outgoing.get(e, []))
    depth3.update(incoming.get(e, []))

keep.update(depth3)

print("Route:", len(route_edges))
print("Tiefe 1 neu:", len(depth1))
print("Tiefe 2 neu:", len(depth2))
print("Tiefe 3 neu:", len(depth3))
print("Gesamt:", len(keep))


with open("keep_edges_depth3.txt", "w") as f:
    for edge in sorted(keep):
        f.write(edge + "\n")

print("keep_edges_depth3.txt geschrieben")