import gradio as gr
import Intro_Page, Books_Page, Recommend_page

mainApp = gr.Blocks()

with mainApp:                         # home page
    Intro_Page.Intro.render()

with mainApp.route("AI Recommendation"): # recommendation page
    Recommend_page.dashboard.render()

with mainApp.route("Book Store"):
    Books_Page.books_page.render()


if __name__ == "__main__":
    mainApp.launch()
