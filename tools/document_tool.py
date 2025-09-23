
from agents.document_agent import query_pdf
from camel.toolkits import FunctionTool

def _document_func(query: str) -> str:
    """
    Queries PDF/document embeddings for relevant answers.
    """
    return query_pdf(query)

def document_tool():
    return FunctionTool(_document_func)
