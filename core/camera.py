import math

class Camera:
    def __init__(self, position, movement, shake=0.0):
        self.x, self.y, self.z = position
        self.movement = movement
        self.shake = shake

    def dolly_in(self, t_norm: float):
        """
        t_norm: 0.0 → 1.0
        """
        intensity = self.movement.get("intensity", 0.3)
        dz = intensity * t_norm
        # basit kamera sarsıntısı
        jitter = math.sin(t_norm * math.pi * 8) * self.shake
        return (self.x + jitter, self.y, self.z + dz)
