from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

import dotenv
import os

# Load environment variables from a .env file
dotenv.load_dotenv()

# Path to the PDF document
pdfreader = PdfReader("pdf/Investments.pdf")

# Open the PDF file in read-binary mode
with open(pdf_path, "rb") as file:
    reader = PdfReader(file)
    pdf_text = ""

    # Iterate through all the pages of the PDF and extract text
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        pdf_text += page.extractText()

# Initialize the loader with the extracted PDF text
loader = PDFBaseLoader(pdf_text)

# Load the documents from the PDF text
docs = loader.load()

# Initialize a text splitter with a chunk size of 1000 characters and an overlap of 200 characters
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Split the loaded documents into smaller chunks
splits = text_splitter.split_documents(docs)

# Create a vector store from the split documents using OpenAI embeddings
# and persist the vector store in the specified directory
Chroma.from_documents(documents=splits,
                      embedding=OpenAIEmbeddings(),
                      persist_directory="./chroma_db")
