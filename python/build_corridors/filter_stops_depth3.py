import xml.etree.ElementTree as ET
import copy

NET = "../../sumo/linie1/corridor/corridor_depth3.net.xml"
STOPS = "../../sumo/linie1/infrastructure/osm_stops.add.xml"
OUT = "../../sumo/linie1/infrastructure/corridor_depth3_stops.add.xml"

# existierende Lanes sammeln
net_tree = ET.parse(NET)
net_root = net_tree.getroot()

lanes = set()

for lane in net_root.iter("lane"):
    lane_id = lane.get("id")
    if lane_id:
        lanes.add(lane_id)

print("Lanes:", len(lanes))

# Stops laden
stop_tree = ET.parse(STOPS)
stop_root = stop_tree.getroot()

new_root = ET.Element("additional")

kept = 0
removed = 0

for elem in stop_root:

    if elem.tag != "busStop":
        continue

    lane = elem.get("lane")

    if lane in lanes:

        new_elem = copy.deepcopy(elem)

        for acc in list(new_elem.findall("access")):

            acc_lane = acc.get("lane")

            if acc_lane not in lanes:
                new_elem.remove(acc)

        new_root.append(new_elem)
        kept += 1

    else:
        removed += 1


ET.ElementTree(new_root).write(
    OUT,
    encoding="utf-8",
    xml_declaration=True
)

print("Kept:", kept)
print("Removed:", removed)