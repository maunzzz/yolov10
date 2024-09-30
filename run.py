import cv2

from config import data_folder, model_folder
from ultralytics import YOLOv10

model = YOLOv10(model_folder() / 'yolov10x.pt')
vid_path = data_folder() / 'IMG_6999.MOV'
cap = cv2.VideoCapture(str(vid_path))

model.fuse()
pred = model.predict(str(vid_path), stream=True)

for result in pred:
    asd = 0
