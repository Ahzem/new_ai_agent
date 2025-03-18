from phi.agent import Agent
from phi.agent import Agent
from phi.model.google import Gemini
from knowledge_base import knowledge_base
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector
from phi.embedder.google import GeminiEmbedder
import os
from dotenv import load_dotenv
load_dotenv()

# Create a knowledge base from a PDF
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # Use LanceDB as the vector database
    vector_db=PgVector(
        table_name="recipes",
        # uri="tmp/lancedb",
        db_url=os.getenv("DATABASE_URL"),
        # search_type=SearchType.vector,
        # embedder=OpenAIEmbedder(model="text-embedding-3-small"),
        embedder=GeminiEmbedder(id="gemini-2.0-flash"),
    ),
    # vector_db=PgVector(
    # ),
)
# Comment out after first run as the knowledge base is loaded
knowledge_base.load(recreate=False)

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    # Add the knowledge base to the agent
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)