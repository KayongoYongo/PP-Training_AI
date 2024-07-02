from load_file import load_pdf
from split_text import split_text
from create_embedding import GeminiEmbeddingFunction
from create_db import create_chroma_db


# load the pdf
pdf_text = load_pdf(file_path="pdf/Investments.pdf")

# split the text into chunks
chunked_text = split_text(text=pdf_text)

# create the chroma_db
name = create_chroma_db(documents=chunked_text,
                            path="./Chroma",
                            name="rag_experiment")