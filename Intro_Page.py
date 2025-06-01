
import gradio as gr

with gr.Blocks() as Intro:
    gr.Markdown(
        """
<h1 style="text-align: center;">✨ <strong>BookSage</strong> – <em>Your Smart Book Companion</em></h1>

## 📚 Discover Books That Truly Resonate With You
<h3>Tired of generic book lists and endless scrolling? **BookSage** uses cutting-edge AI to understand your emotions and preferences—recommending books that match your mood, interests, and the way you think.</h3>

---
<h2> 💬 Just Say What You're In the Mood For</h2>
**Whether you're feeling nostalgic, curious, inspired, or just looking for a thrilling escape, BookSage listens.**

    “I want a heartwarming story about self-discovery”
    “Something dark, suspenseful, and unforgettable”

<h2> 🧠 Powered by Modern AI (LLM)</h2> 
<ul style="list-style-type: none; padding-left: 0;">
   <li>✔️ <b>Natural Language Input</b>: You speak like a human. Our AI listens like one</li>  
   <li>✔️ <b>Deep Semantic Understanding</b>: Using advanced text embeddings (all-MiniLM-L6-v2), we analyze the true meaning of your query</li>  
   <li>✔️ <b>Emotion-Aware Matching</b>: With emotion recognition (j-hartmann/emotion-english-distilroberta-base), we detect the emotional tone behind your words</li>
   <li>✔️ <b>Personalized Book Recommendations</b>:Instantly get book suggestions that resonate—with your mind and mood</li> 
</ul>
<h2> 💡 Why You’ll Love It</h2> 
<ul style="list-style-type: none; padding-left: 0;">
   <li>🎯 <b>Emotionally aligned, deeply relevant, never boring. Not just “similar books,” but emotionally relevant stories</li>
   <li>⚡ Fast & Seamless: Results in seconds, no signup required</li>
   <li>📚 Curated With Care: Powered by real AI, not random lists</li>
   <li>🌟 Great for Everyone – From casual readers to bookworms</li>
 </ul>  
   
---
<p style="text-align">
  <a href="https://github.com/LakhanGitHub/Book-Recommendation" target="_blank" style="text-decoration:none;">
    &nbsp;<strong>👉 View the code on GitHub</strong>
  </a>  
</p>
"""
    )
    gr.Markdown("Made with ❤️ by Lakhan", elem_id="footer", elem_classes="footer-note")

if __name__ == "__main__":
    Intro.launch()

