from pinecone import Pinecone, ServerlessSpec
from keys import api_key

def insert_data_pinecone(embeddings):
    # Initialize Pinecone
    pc = Pinecone(api_key=api_key)

    # Check if initialization is successful
    print(pc.list_indexes().names())

    # Define index name and dimension
    index_name = 'index-pdf-data-1'
    dimension = 4096  # Replace with the actual dimension of your embeddings

    # Create a new index (if it doesn't exist already)
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name, 
            dimension=dimension, 
            metric='euclidean',
            spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
            ) 
        )

    # Connect to the index
    index = pc.Index(index_name)

    # Example pre-computed embeddings
    embeddings = [
        {"id": "1", "values": embeddings},  # Replace with actual embeddings
    ]

    # Prepare embeddings for Pinecone
    vectors_to_upsert = [(embedding["id"], embedding["values"]) for embedding in embeddings]

    # Insert embeddings into Pinecone index
    index.upsert(vectors_to_upsert)

    # Check the number of vectors in the index
    print(index.describe_index_stats())
