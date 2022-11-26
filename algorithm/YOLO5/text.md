input - 
DEEPSORT:
  REID_CKPT: "deep_sort_pytorch/deep_sort/deep/checkpoint/ckpt.t7"
  MAX_DIST: 0.2
  MIN_CONFIDENCE: 0.3
  NMS_MAX_OVERLAP: 0.5
  MAX_IOU_DISTANCE: 0.7
  MAX_AGE: 20
  N_INIT: 8
  NN_BUDGET: 30

python track2.py --yolo_weights yolov5/runs/train/yolov5m-32/weights/last.pt --source input3.mp4 --save-vid --save-txt --save-upa --show-vid --conf-thres 0.8

output

DEEPSORT:
  REID_CKPT: "deep_sort_pytorch/deep_sort/deep/checkpoint/ckpt.t7"
  MAX_DIST: 0.2
  MIN_CONFIDENCE: 0.3
  NMS_MAX_OVERLAP: 0.5
  MAX_IOU_DISTANCE: 0.7
  MAX_AGE: 65
  N_INIT: 3
  NN_BUDGET: 85

python track3.py --yolo_weights yolov5/runs/train/yolov5m-32/weights/last.pt --source input3.mp4 --save-vid --save-txt --save-upa --show-vid --conf-thres 0.9