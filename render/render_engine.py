import os
import cv2
import numpy as np
from PIL import Image
# Eğer diffusers yüklü değilse: pip install diffusers transformers torch

class StableDiffusionRenderer:
    def __init__(self):
        # Placeholder: Basit renkli arka plan üretimi
        pass

    def generate_frame(self, scene, camera_pos, frame_index):
        # Basit renk geçişi ile frame oluşturuyoruz
        h, w = 512, 512
        img = np.zeros((h, w, 3), dtype=np.uint8)
        r = int((frame_index / scene['frames']) * 255)
        g = int(((scene['frames'] - frame_index) / scene['frames']) * 255)
        b = 128
        img[:, :, 0] = r
        img[:, :, 1] = g
        img[:, :, 2] = b
        return img

def build_video(scene, output_file="output/video.mp4"):
    renderer = StableDiffusionRenderer()
    frames = []
    for i in range(scene['frames']):
        frame = renderer.generate_frame(scene, scene['camera_positions'][i], i)
        frames.append(frame)

    h, w, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 4, (w, h))  # 4 fps, 12-16 frame → ~3 saniye

    for f in frames:
        out.write(f)
    out.release()
    print(f"[RENDER] Video çıktı: {output_file}")
