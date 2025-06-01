import pandas as pd
import numpy as np
import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

import gradio as gr


books = pd.read_csv('books_with_emotions.csv')
books['large_thumbnail'] = books['thumbnail'] + "&fife=800"
books['large_thumbnail'] = np.where(
        books['large_thumbnail'].isnull(),
        'cover-not-found.jpg',
        books['large_thumbnail']
    )

# Define the path to persist/load Chroma DB
persist_path = os.path.join(os.getcwd())

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load or create vector store
db_books = Chroma(
    persist_directory=persist_path,
    embedding_function=embedding_model
)

def retrieve_semantic_recommendation(
        query : str,
        category:str = None,
        ton: str = None,
        initial_top_k: int = 50,
        final_top_k: int = 16

) -> pd.DataFrame:
    recs = db_books.similarity_search(query,initial_top_k)
    books_list = [int(rec.page_content.strip('"').split()[0]) for rec in recs]
    books_recs = books[books['isbn13'].isin(books_list)].head(final_top_k)

    if category != 'All':
        books_recs = books_recs[books_recs['simple_categories'] == category].head(final_top_k)
    else:
        books_recs = books_recs.head(final_top_k)

    if ton=='Happy':
        books_recs.sort_values(by='joy', ascending=False, inplace=True)
    if ton=='Anger':
        books_recs.sort_values(by='anger', ascending=False, inplace=True)
    if ton=='Suspenseful':
        books_recs.sort_values(by='fear', ascending=False, inplace=True)
    if ton=='Sad':
        books_recs.sort_values(by='sadness', ascending=False, inplace=True)
    if ton=='Surprising':
        books_recs.sort_values(by='surprise', ascending=False, inplace=True)

    return books_recs


def book_recommendations(
        query:str,
        category:str,
        ton:str):

    recommendations = retrieve_semantic_recommendation(query,category,ton)
    results=  []

    for _, row in recommendations.iterrows():
        description = row['description']
        truncate_description_split = description.split()
        truncated_description = ' '.join(truncate_description_split[:30]) + '...'

        author_split = str(row['authors']).split(';')
        if len(author_split) == 2:
            auther_st = f"{author_split[0] and author_split[1]}"
        elif len(author_split) > 2:
            auther_st = f"{' '.join(author_split[:-1])} and {author_split[-1]}"
        else:
            auther_st = row['authors']

        caption = f"{row['title']} by {auther_st}:{truncated_description}"
        results.append((row['large_thumbnail'], caption))
    return results

categories = ['All'] + sorted(books['simple_categories'].unique())
ton = ['All'] + ['Happy','Anger','Suspenseful','Sad','Surprising']

with gr.Blocks(theme = gr.themes.Glass()) as dashboard:
    gr.Markdown("<h1>Semantic Book Recommender (Powered by AI)</h1>") #for title

    with gr.Row():
        user_query = gr.Textbox(label = "Please enter a description of a book:",
                                        placeholder = "e.g., A story about joy and happiness")
        category_dropdown = gr.Dropdown(choices = categories, label = "Select a category:", value = "All")
        tone_dropdown = gr.Dropdown(choices = ton, label = "Select an emotional tone:", value = "All")
        submit_button = gr.Button("Find recommendations")

    gr.Markdown("## Recommendations")

    output = gr.Gallery(label = "Recommended books", columns = 8, rows = 2)

    submit_button.click(fn = book_recommendations,
                        inputs = [user_query, category_dropdown, tone_dropdown],
                        outputs = output)

    gr.Markdown("Made with ❤️ by Lakhan", elem_id="footer", elem_classes="footer-note")

if __name__ == "__main__":
    dashboard.launch()

