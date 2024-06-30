from PyPDF2 import PdfReader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.document_loaders import PDFLoader

# Path to the PDF document
pdf_path = "pdf/Investments.pdf"

# Open the PDF file in read-binary mode
with open(pdf_path, "rb") as file:
    reader = PdfReader(file)
    pdf_text = ""

    # Iterate through all the pages of the PDF and extract text
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()

# Initialize the loader with the extracted PDF text
loader = PDFLoader(pdf_text)

# Load the documents from the PDF text
docs = loader.load()

# Initialize a text splitter with a chunk size of 1000 characters and an overlap of 200 characters
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Split the loaded documents into smaller chunks
splits = text_splitter.split_documents(docs)

# Create a vector store from the split documents using OpenAI embeddings
# and persist the vector store in the specified directory
Chroma.from_documents(documents=splits,
                      embedding=OpenAIEmbeddings(),
                      persist_directory="./chroma_db")
