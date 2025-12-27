from core.scene_graph import SceneGraph
from core.camera import Camera
from render.timeline import build_timeline

FPS = 12  # hafif ve yeterli

def main():
    scene = SceneGraph("scene.json")

    cam_cfg = scene.camera
    cam = Camera(
        position=cam_cfg["position"],
        movement=cam_cfg["movement"],
        shake=cam_cfg.get("shake", 0.0)
    )

    duration = cam_cfg["movement"]["duration"]
    timeline = build_timeline(duration, FPS)

    print(f"[DIRECTOR] Scene: {scene.scene_id}")
    print(f"[DIRECTOR] Frames: {len(timeline)}")

    frames = []
    for i, t in enumerate(timeline):
        pos = cam.dolly_in(t)
        frames.append({
            "frame": i,
            "time": round(t * duration, 3),
            "camera_position": tuple(round(v, 3) for v in pos)
        })

    # Şimdilik sadece zaman çizelgesini yazdırıyoruz
    for f in frames:
        print(f)

if __name__ == "__main__":
    main()
