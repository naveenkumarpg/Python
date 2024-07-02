import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'image/google/secure-stone-427110-v8-b5c5ce8beb84.json'

# Detect details from the file.
def detect_labels_google(path):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels:")

    for label in labels:
        print(label.description)

    if response.error.message:
        print("There is some error")
