import xml.etree.ElementTree as ET
import math

RADIUS = 100.0

# ---------- Route laden ----------
route_tree = ET.parse("linie1.rou.xml")
route_root = route_tree.getroot()

route_edges = set()

for route in route_root.findall("route"):
    edges = route.get("edges")
    if edges:
        route_edges.update(edges.split())

print(f"Route edges: {len(route_edges)}")

# ---------- Netz laden ----------
net_tree = ET.parse("osmnew.net.xml")
net_root = net_tree.getroot()

edge_points = {}

for edge in net_root.findall("edge"):
    edge_id = edge.get("id")

    if edge_id is None:
        continue

    if edge_id.startswith(":"):
        continue

    shape = edge.get("shape")

    if shape is None:
        lane = edge.find("lane")
        if lane is not None:
            shape = lane.get("shape")

    if not shape:
        continue

    pts = []

    for p in shape.split():
        x, y = p.split(",")
        pts.append((float(x), float(y)))

    edge_points[edge_id] = pts

print(f"Edges im Netz: {len(edge_points)}")

# ---------- Route-Geometrie sammeln ----------
route_geometry = []

for edge in route_edges:
    if edge in edge_points:
        route_geometry.extend(edge_points[edge])

print(f"Route-Geometriepunkte: {len(route_geometry)}")


# ---------- Distanz ----------
def min_dist(points_a, points_b):
    dmin = float("inf")

    for x1, y1 in points_a:
        for x2, y2 in points_b:
            d = math.hypot(x1 - x2, y1 - y2)

            if d < dmin:
                dmin = d

            if dmin <= RADIUS:
                return dmin

    return dmin


# ---------- Korridor erzeugen ----------
keep_edges = set(route_edges)

counter = 0

for edge_id, pts in edge_points.items():

    if edge_id in keep_edges:
        continue

    d = min_dist(pts, route_geometry)

    if d <= RADIUS:
        keep_edges.add(edge_id)

    counter += 1

    if counter % 1000 == 0:
        print(counter)

print(f"Keep edges: {len(keep_edges)}")

with open("keep_edges_100m.txt", "w") as f:
    for e in sorted(keep_edges):
        f.write(e + "\n")

print("keep_edges_100m.txt geschrieben")