from phi.agent import Agent
from phi.model.groq import Groq
from phi.knowledge.pdf import PDFKnowledgeBase
from phi.knowledge.pdf import PDFReader
from phi.vectordb.chroma import ChromaDb  # Changed from chromadb to Chroma

def create_knowledge_base_agent():
    # Create a knowledge base from local PDFs
    company_knowledge = PDFKnowledgeBase(
        path="data/pdfs",
        vector_db=ChromaDb(
            collection="company_documents",
            path="./data/chromadb",
        ),
        reader=PDFReader(chunk=True),
    )

    return Agent(
        name="company-knowledge-agent",
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        knowledge_base=company_knowledge,
        instructions="""
        You are a company information assistant. Use the provided knowledge base to:
        1. Answer questions about company policies, procedures, and information
        2. Provide accurate information from company documents
        3. If information is not in the knowledge base, clearly state that
        Always cite the source document when providing information.
        """,
        description="Company Knowledge Assistant",
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
    )