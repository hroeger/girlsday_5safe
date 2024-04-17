from fivesafe.utilities import run
from fivesafe.object_detection import find_detector_class
from fivesafe.bev import PositionEstimation, draw_world_positions, draw_vehicle_baseplates
from fivesafe.image_tracking import Tracker as ImageTracker, draw_tracks
from fivesafe.world_tracking import Tracker as WorldTracker
from fivesafe.decision_module import decision_making as dm
from ultralytics import YOLO
import cv2
import girls_day
import argparse

dm_model = "empty_model.pkl"

def start(cap, cfg):
    # Initialization
    _, frame = cap.read()
    height, width, _ = frame.shape
    model = YOLO(cfg.detection.model)
    DetectorClass = find_detector_class(cfg.detection.model)
    detector = DetectorClass(
        model=model,
        classes_of_interest=cfg.detection.classes_of_interest
    )
    position_estimator = PositionEstimation(cfg.bev.homography, cfg.bev.scalefactor)
    image_tracker = ImageTracker(width, height)
    world_tracker = WorldTracker()  
    top_view_org = cv2.imread(cfg.bev.top_view)
   # cv2.namedWindow("top_view", cv2.WINDOW_NORMAL) 
    cv2.namedWindow("perspective_view", cv2.WINDOW_NORMAL)

    if cfg.dm.is_used:
        contours_int_path = dm.get_contours(cfg.dm.not_intended_paths.points) 
        contours_turning_right = dm.get_contours(cfg.dm.turning_right.points) 
        dm.draw_polylines_in_top_view(top_view_org, contours_int_path, color=cfg.dm.not_intended_paths.color)
        dm.draw_polylines_in_top_view(top_view_org, contours_turning_right, color=cfg.dm.turning_right.color)

    
 #   girls_day_model = girls_day.GirlsDayModel('empty_model.pkl')
    print(f'"initialize dm with model: {dm_model}')
    girls_day_model = girls_day.GirlsDayModel(dm_model)
    girls_day_messenger = girls_day.GDMessageHandler()

    # start flask server. - no! flask server is a second, different application. then store in model and thats it.
    # somehow need to refresh the model.
    
    
    # Main Loop
    while True:
        top_view = top_view_org.copy()
        detections = detector.detect(frame)
        print(detections, flush=True)

        #detections ist eine list von "detection" objekten

        detecion_array = [d.label() for d in detections] 

        # verify against model.
        dangerous_situation = girls_day_model.test_frame(detecion_array)
        print(dangerous_situation, flush=True)
        girls_day_messenger.q.put(dangerous_situation) #True / False
        # send warnings if necessary

        image_tracks = image_tracker.track(detections)
     #   image_tracks_transformed = position_estimator.transform(image_tracks, detections)
     #   world_tracks_vrus, world_tracks_vehicles = world_tracker.track(image_tracks_transformed)
       # top_view = draw_world_positions(top_view, world_tracks_vrus, cfg.colors)
       # top_view = draw_vehicle_baseplates(top_view, world_tracks_vehicles, cfg.bev.scalefactor, cfg.colors, 3)
        frame = draw_tracks(frame, image_tracks, cfg.colors, draw_detection_id=False)
        # Decision Making
      #  not_intended_path_vrus, turn_right_vrus = dm.get_vrus_in_zones(world_tracks_vrus, contours_int_path, contours_turning_right)
       # top_view = draw_world_positions(top_view, not_intended_path_vrus, cfg.colors, fixed_color=[0, 255, 0])
       # top_view = draw_world_positions(top_view, turn_right_vrus, cfg.colors, fixed_color=[0, 255, 0])

        cv2.imshow("perspective_view", frame)
     #   cv2.imshow("top_view", top_view)
        if cv2.waitKey(1) == ord('q'):
            break
        _, frame = cap.read()
    cv2.destroyAllWindows

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("dm_model", help="path to model used")
    args = parser.parse_args()
    print(args)
    dm_model = args.dm_model

    print(f'starting with model: {dm_model}')
    run('conf/video_LUMPI.yaml', start, bufferless=False)