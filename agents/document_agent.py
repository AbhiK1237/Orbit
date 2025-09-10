import os
import requests
os.makedirs('local_data', exist_ok=True)
url = "https://arxiv.org/pdf/2303.17760.pdf"
with open('local_data/camel_paper.pdf', 'wb') as file:
     file.write(response.content)

from camel.embeddings import OpenAIEmbedding
from camel.types import EmbeddingModelType
from camel.storages import QdrantStorage
from camel.retrievers import VectorRetriever
embedding_instance = OpenAIEmbedding(model_type=EmbeddingModelType.TEXT_EMBEDDING_3_LARGE)

storage_instance = QdrantStorage(
    vector_dim=embedding_instance.get_output_dim(),
    path="local_data",
    collection_name="camel_paper",
)

vector_retriever = VectorRetriever(embedding_model=embedding_instance,
                                   storage=storage_instance)
vector_retriever.process(
    content="local_data/camel_paper.pdf",
)

retrieved_info = vector_retriever.query(
    query="To address the challenges of achieving autonomous cooperation, we propose a novel communicative agent framework named role-playing .",
    top_k=1
)
print(retrieved_info)
retrieved_info_irrevelant = vector_retriever.query(
    query="Compared with dumpling and rice, which should I take for dinner?",
    top_k=1,
)

print(retrieved_info_irrevelant)
