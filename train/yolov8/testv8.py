from ultralytics import YOLO

# Load a model
model = YOLO('../runs/yolov8x-seg/weights/best.pt')  # load a custom model

# Validate the model
metrics = model.val(data='./data.yaml', device='cpu')  # no arguments needed, dataset and settings remembered
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category