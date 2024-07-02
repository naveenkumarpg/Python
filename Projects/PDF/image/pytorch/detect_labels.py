import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def load_image(image_path):
    image = Image.open(image_path).convert("RGB")
    transform = T.Compose([T.ToTensor()])
    image = transform(image)
    return image

def get_prediction(image, threshold=0.5):
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    with torch.no_grad():
        prediction = model([image])
    # Filter results with low scores
    pred_labels = prediction[0]['labels'].tolist()
    pred_boxes = [[(i[0], i[1]), i[2]-i[0], i[3]-i[1]] for i in prediction[0]['boxes'].tolist()]
    pred_scores = prediction[0]['scores'].tolist()
    # Keep predictions above the threshold
    qualified_predictions = [(box, label) for box, label, score in zip(pred_boxes, pred_labels, pred_scores) if score > threshold]
    return qualified_predictions

def show_image(image, predictions):
    fig, ax = plt.subplots(1, figsize=(12,9))
    ax.imshow(image.permute(1, 2, 0))
    for box, label in predictions:
        rect = patches.Rectangle((box[0][0], box[0][1]), box[1], box[2], linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        plt.text(box[0][0], box[0][1], s=str(label), color='white', verticalalignment='top', bbox={'color': 'red', 'pad': 0})
    plt.show()

def detect_labels_pytorch(path):
    image = load_image(path)
    predictions = get_prediction(image)
    print(predictions)
