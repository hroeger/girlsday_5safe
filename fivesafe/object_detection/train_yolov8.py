from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8s.pt')
 
# Training.
results = model.train(
   #data='conf/dataset.yaml',
   data='/Users/A200158358/Desktop/5 safe/girlsday/git_girlsday/girlsday_5safe/conf/train.yaml',
   imgsz=640,
   epochs=8,
   name='finetuned'
)
results = model.val()