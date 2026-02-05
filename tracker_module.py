from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        self.tracker = DeepSort(
            max_age=30,
            n_init=3,
            max_iou_distance=0.7
        )

    def update(self, detections, frame):
        tracks = self.tracker.update_tracks(detections, frame=frame)
        outputs = []

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            x1, y1, x2, y2 = map(int, track.to_ltrb())
            outputs.append([x1, y1, x2, y2, track_id])

        return outputs
