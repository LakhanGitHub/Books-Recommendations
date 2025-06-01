# ------------- Books_Page.py -------------
import gradio as gr
import pandas as pd
import numpy as np

# ── Load & prep data ───────────────────────────────────────
books = pd.read_csv("books_with_emotions.csv")

# large thumbnail fallback
books["large_thumbnail"] = (
    books["thumbnail"].fillna("cover-not-found.jpg") + "&fife=800"
)

# ── Recommendation helper ─────────────────────────────────
def book_recommendations() -> list[tuple[str, str]]:
    """
    Returns a list of (img_url, caption) tuples for gr.Gallery.
    Currently: random 50 samples. Replace with real filter logic later.
    """
    sample = books.sample(n=50, random_state=None)
    results: list[tuple[str, str]] = []

    for _, row in sample.iterrows():
        # --- truncate description to 30 words
        desc_words = str(row["description"]).split()
        truncated_desc = " ".join(desc_words[:30]) + "..."

        # --- prettify author list
        authors = str(row["authors"])
        author_list = [a.strip() for a in authors.split(";") if a.strip()]
        if len(author_list) == 0:
            author_str = "Unknown Author"
        elif len(author_list) == 1:
            author_str = author_list[0]
        elif len(author_list) == 2:
            author_str = f"{author_list[0]} and {author_list[1]}"
        else:
            author_str = f"{', '.join(author_list[:-1])}, and {author_list[-1]}"

        caption = f"{row['title']} by {author_str}: {truncated_desc}"
        results.append((row["large_thumbnail"], caption))

    return results


# ── Build the Books page ───────────────────────────────────
with gr.Blocks(theme=gr.themes.Glass()) as books_page:
    gr.Markdown("## 📚 Discover Books You Love")

    with gr.Row():
        gallery = gr.Gallery(label="", columns=5, rows=10)


    refresh_btn = gr.Button("🔄 Refresh Books")

    # ── Populate gallery on page load
    books_page.load(fn=book_recommendations, outputs=gallery)

    # ── Refresh button logic
    refresh_btn.click(fn=book_recommendations, outputs=gallery)

    gr.Markdown("### Made with ❤️ by Lakhan", elem_id="footer", elem_classes="footer-note")



if __name__ == "__main__":
    books_page.launch()
