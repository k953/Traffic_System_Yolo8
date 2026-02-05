import cv2
from detector import Detector
from tracker_module import Tracker
from mapper import WorldMapper
from speed_behavior import SpeedBehavior
from analytics import TrafficAnalytics

cap = cv2.VideoCapture("highway.mp4")

detector = Detector()
tracker = Tracker()
mapper = WorldMapper()
speed_engine = SpeedBehavior()
analytics = TrafficAnalytics()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detector.detect(frame)
    tracks = tracker.update(detections, frame)

    for x1,y1,x2,y2,track_id in tracks:
        cx = (x1+x2)//2
        cy = (y1+y2)//2

        world_pt = mapper.map_point(cx, cy)
        speed, event = speed_engine.compute(track_id, world_pt)
        analytics.update(track_id)

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        text = f"ID:{track_id} {speed:.1f} km/h"
        if event:
            text += f" {event}"

        cv2.putText(frame,text,(x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

    cv2.putText(frame,
                f"Vehicle Count: {analytics.count()}",
                (30,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("Traffic System", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
