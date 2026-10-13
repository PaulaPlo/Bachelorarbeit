import xml.etree.ElementTree as ET

# Route einlesen
route_file = "linie1.rou.xml"
net_file = "osmnew.net.xml"

# Route-Edges sammeln
route_tree = ET.parse(route_file)
route_root = route_tree.getroot()

route_edges = set()

for route in route_root.findall("route"):
    edges = route.get("edges")
    if edges:
        route_edges.update(edges.split())

print("Route edges:", len(route_edges))

# Netz lesen
net_tree = ET.parse(net_file)
net_root = net_tree.getroot()

# Edge -> Nachbarn
incoming = {}
outgoing = {}

for conn in net_root.findall("connection"):
    fr = conn.get("from")
    to = conn.get("to")

    if fr and to:
        outgoing.setdefault(fr, set()).add(to)
        incoming.setdefault(to, set()).add(fr)

# Tiefe 2
keep = set(route_edges)

depth1 = set()

for e in route_edges:
    depth1.update(outgoing.get(e, []))
    depth1.update(incoming.get(e, []))

keep.update(depth1)

depth2 = set()

for e in depth1:
    depth2.update(outgoing.get(e, []))
    depth2.update(incoming.get(e, []))

keep.update(depth2)

print("Corridor edges:", len(keep))

with open("keep_edges.txt", "w") as f:
    for edge in sorted(keep):
        f.write(edge + "\n")

print("keep_edges.txt geschrieben")