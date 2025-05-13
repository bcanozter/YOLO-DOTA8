from ultralytics import YOLO
from PIL import Image
model = YOLO("best.pt")

# Train the model on the DOTAv1 dataset
image = Image.open("harbour.jpg")
results = model(source=image)
for result in results:
    # Save as image
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    obb = result.obb
    result.save(filename="result.jpg")
