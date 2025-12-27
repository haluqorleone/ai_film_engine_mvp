import json

class SceneGraph:
    def __init__(self, scene_path: str):
        with open(scene_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def camera(self):
        return self.data["camera"]

    @property
    def events(self):
        return self.data.get("events", [])

    @property
    def scene_id(self):
        return self.data.get("scene_id", "scene")
