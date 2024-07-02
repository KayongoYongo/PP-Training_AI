from langchain.text_splitter import CharacterTextSplitter

def split_text(text: str):
    """
    Splits a text string into a list of non-empty substrings based on the specified pattern.
    The "\n \n" pattern will split the document para by para
    Parameters:
    - text (str): The input text to be split.

    Returns:
    - List[str]: A list containing non-empty substrings obtained by splitting the input text.

    """
    # Initialize a text splitter with a chunk size of 1000 characters and an overlap of 200 characters
    text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size=1000, 
    chunk_overlap=200,
    length_function=len
    )

    # Split the loaded documents into smaller chunks
    documents = text_splitter.split_text(text)

    return documents