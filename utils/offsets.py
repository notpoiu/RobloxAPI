import json, requests

OffsetsRequest = requests.get("https://offsets.ntgetwritewatch.workers.dev/offsets.json")
Offsets = OffsetsRequest.json()

for key in Offsets:
    try:
        Offsets[key] = int(Offsets[key], 16)
    except (ValueError, TypeError):
        pass

with open("data/offsets.json", "r") as f:
    LoadedOffsets = json.load(f)
    f.close()

for key in LoadedOffsets:
    Offsets[key] = int(LoadedOffsets[key], 16)

# CFrame Offsets
RotationMatriciesLengthBytes = 3 * 3 * 4

Offsets["CameraCFrame"] = Offsets["CameraPos"] - RotationMatriciesLengthBytes
Offsets["CFrame"] = Offsets["Position"] - RotationMatriciesLengthBytes