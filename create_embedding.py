from chromadb import Documents, EmbeddingFunction, Embeddings
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environmental variables from a .env file
load_dotenv()

class GeminiEmbeddingFunction(EmbeddingFunction):
    """
    Custom embedding function using the Gemini AI API for document retrieval.

    This class extends the EmbeddingFunction class and implements the __call__ method
    to generate embeddings for a given set of documents using the Gemini AI API.

    Parameters:
    - input (Documents): A collection of documents to be embedded.

    Returns:
    - Embeddings: Embeddings generated for the input documents.
    """

    def __call__(self, input: Documents) -> Embeddings:
        
        # Access the Google API key from the loaded environment variables
        API_KEY = os.getenv("GOOGLE_API_KEY")

        # Configure the generative AI client with the API key
        genai.configure(api_key=API_KEY)

        model = "models/embedding-001"
        title = "Custom query"

        return genai.embed_content(model=model,
                                content=input,
                                task_type="retrieval_document",
                                title=title)["embedding"]