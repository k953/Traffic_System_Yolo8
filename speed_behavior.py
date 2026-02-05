import time
import math

class SpeedBehavior:
    def __init__(self):
        self.prev = {}

    def compute(self, track_id, world_pt):
        speed = 0.0
        event = None
        now = time.time()

        if track_id in self.prev:
            x0, y0, t0 = self.prev[track_id]
            dist = math.hypot(world_pt[0] - x0, world_pt[1] - y0)
            dt = now - t0

            if dt > 0:
                speed = (dist / dt) * 3.6  # km/h
                if speed > 80:
                    event = "OVER SPEED"

        self.prev[track_id] = (world_pt[0], world_pt[1], now)
        return speed, event

