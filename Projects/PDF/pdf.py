import pymupdf

from embeddings.openai import create_embedding_open_ai
from embeddings.ollama import create_embedding_ollama
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# from image.google.google_vision import detect_labels_google
# from image.pytorch.detect_labels import detect_labels_pytorch
# from image.opencv.detect_labels import detect_labels_open_cv
from image.tensorflow.detect_labels import detect_labels_tensorflow
from text_from_image.tesseract import detect_text_pytesseract
from text_clean.pymupdf import clean_text_file
from database.pinecone import insert_data_pinecone



doc = pymupdf.open("pdf/2022.pdf") # open a document
# doc = pymupdf.open("pdf/LittleHedge.pdf") # open a document

out = open("results/output.txt", "wb") # create a text output
for page in doc: # iterate the document pages
    text = page.get_text('text').encode("utf8") # get plain text (is in UTF-8)
    print(text)

    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    print('\n\n\n\n\nExtracted text is saved into the results results/output.txt \n\n\n\n\n')


total_images = 0

for page_index in range(len(doc)): # iterate over pdf pages
    page = doc[page_index] # get the page
    image_list = page.get_images()
    
    # print the number of images found on the page
    if image_list:
        print(f"Found {len(image_list)} images on page {page_index}")
    else:
        print("No images found on page", page_index)

    for image_index, img in enumerate(image_list, start=1): # enumerate the image list
        xref = img[0] # get the XREF of the image
        pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

        if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

        total_images = total_images +1
        image_name = f"results/image-{total_images}.png"
        pix.save(image_name)

        print("****************************************************************")
        # Extract objects from the image
        # imageData = detect_labels_google(f"results/image-{total_images}.png")
        # imageData = detect_labels_pytorch(f"results/image-{total_images}.png")
        # imageData = detect_labels_open_cv(f"results/image-{total_images}.png")
        imageData = detect_labels_tensorflow(f"results/image-{total_images}.png")
        text = imageData.encode("utf8") # get plain text (is in UTF-8)
        print(f'\n\n\n\n\n ${text} \n\n\n\n\n')

        out.write(text) # write text of page
        out.write(bytes((12,))) # write page delimiter (form feed 0x0C)

        # Extract text from the image
        #image_text =  detect_text_pytesseract(f"results/image-{total_images}.png")
        
        pix = None

out.close()


#clean the text file
clean_text_file('results/output.txt')

# Create Embeddings 
loader = TextLoader("results/cleaned_text.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
docs = text_splitter.split_documents(documents)
print(docs)

# Creating embeddings 
# embeddings = create_embedding_open_ai(content)
embeddings = create_embedding_ollama(docs)
print(embeddings)

# adding into vector store
status = insert_data_pinecone(embeddings)
print(status)
