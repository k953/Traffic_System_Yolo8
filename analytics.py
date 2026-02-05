class TrafficAnalytics:
    def __init__(self):
        self.vehicle_ids = set()

    def update(self, track_id):
        self.vehicle_ids.add(track_id)

    def count(self):
        return len(self.vehicle_ids)
