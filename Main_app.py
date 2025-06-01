import gradio as gr
import Intro_Page, Books_Page, app

mainApp = gr.Blocks()

with mainApp:                         # home page
    Intro_Page.Intro.render()

with mainApp.route("Recommendation"): # recommendation page
    app.dashboard.render()

with mainApp.route("Books"):
    Books_Page.books_page.render()


if __name__ == "__main__":
    mainApp.launch()
