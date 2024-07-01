from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Path to the PDF document
pdf_reader = PdfReader("pdf/Investments.pdf")

# print(pdf_reader)
pdf_text = ""

# Iterate through all the pages of the PDF and extract text
for i, page in enumerate(pdf_reader.pages):
    text = page.extract_text()
    if text:
        pdf_text += text

# print(len(pdf_text))
# Initialize a text splitter with a chunk size of 1000 characters and an overlap of 200 characters
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size=1000, 
    chunk_overlap=200,
    length_function=len
)

# Split the loaded documents into smaller chunks
documents = text_splitter.split_text(pdf_text)

# Create a vector store from the split documents using OpenAI embeddings
# and persist the vector store in the specified directory
Chroma.from_documents(documents=documents,
                      embedding=OpenAIEmbeddings(),
                      persist_directory="./chroma_db")