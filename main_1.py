from generate import generate_answer
from load_db import load_chroma_collection
from prompt import make_rag_prompt
from relevant import get_relevant_passage

# start wit this file
def generate_final_answer(db,query):
    relevant_text = get_relevant_passage(query, db, n_results=3)
    prompt = make_rag_prompt(query,
                             relevant_passage="".join(relevant_text))
    
    answer = generate_answer(prompt)

    return answer

# load the chroma db
db = load_chroma_collection(path="./Chroma", name="rag_experiment")

# Convert this with Django

answer = generate_final_answer(db,query="what are the benefits of borrowing from saccos?")

# finl answer
print(answer)