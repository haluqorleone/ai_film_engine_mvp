def build_timeline(duration: float, fps: int):
    total_frames = int(duration * fps)
    return [i / total_frames for i in range(total_frames)]
