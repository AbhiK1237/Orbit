import os
import requests
from dotenv import load_dotenv
load_dotenv()
# os.makedirs('local_data', exist_ok=True)
# url = "https://arxiv.org/pdf/2303.17760.pdf"
# response = requests.get(url)
# with open('local_data/camel_paper.pdf', 'wb') as file:
#      file.write(response.content)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from camel.embeddings import GeminiEmbedding
from camel.types import EmbeddingModelType
from camel.storages import QdrantStorage
from camel.retrievers import VectorRetriever
from camel.loaders import UnstructuredIO
embedding_instance = GeminiEmbedding(model_type=EmbeddingModelType.GEMINI_EMBEDDING_EXP)
from camel.configs import GeminiConfig
from camel.toolkits import FunctionTool

from dotenv import load_dotenv
load_dotenv()
import os
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_5_PRO,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)

storage_instance = QdrantStorage(
    vector_dim=embedding_instance.get_output_dim(),
    url_and_api_key=("http://localhost:6333", None),
    collection_name="camel_paper",
    prefer_grpc=False,
)

vector_retriever = VectorRetriever(embedding_model=embedding_instance,
                                   storage=storage_instance)


loader = UnstructuredIO()
elements = loader.parse_file_or_url("local_data/Abhijith_Resume.pdf")
doc_text = " ".join([el.text for el in elements if el.text])

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,    # ~300-500 tokens works well
    chunk_overlap=100
)

chunks = splitter.split_text(doc_text)

print(f"📄 Extracted {len(chunks)} chunks from PDF")
for idx, chunk in enumerate(chunks):
    vector_retriever.process(content=chunk)

# print("✅ Document embedded and stored in Qdrant")
# retrieved_info = vector_retriever.query(
#     query="what are my technical skills?",
#     top_k=2,
#     similarity_threshold=0.4
# )
# print(retrieved_info)

def query_pdf(query: str) -> str:
    """Retrieve answers from your embedded PDF."""
    results = vector_retriever.query(query=query, top_k=3, similarity_threshold=0.3)
    if not results:
        return "No relevant information found in the document."
    return "\n".join([r.content for r in results])

pdf_tool = FunctionTool(query_pdf)

# retrieved_info_irrevelant = vector_retriever.query(
#     query="Compared with dumpling and rice, which should I take for dinner?",
#     top_k=2,
#     similarity_threshold=0.4
# )

# print(retrieved_info_irrevelant)
# from qdrant_client import QdrantClient

# client = QdrantClient(url="http://localhost:6333")
# print(client.get_collections())