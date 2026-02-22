from flask import Flask, render_template_string, request
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    story = ""
    if request.method == 'POST':
        topic = request.form.get('topic')
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        try:
            response = model.generate_content(f"Cerita horor pendek tentang {topic}")
            story = response.text
        except Exception as e:
            story = f"Error: {str(e)}"

    return render_template_string('''
        <html>
            <body style="font-family:sans-serif; text-align:center; padding-top:50px;">
                <h1>🎬 Video AI (No-Streamlit Mode)</h1>
                <form method="post">
                    <input type="text" name="topic" placeholder="Topik apa?" style="padding:10px; width:300px;">
                    <button type="submit" style="padding:10px;">Bikin Cerita</button>
                </form>
                <div style="margin-top:20px; padding:20px; border:1px solid #ccc; display:inline-block; max-width:500px;">
                    <strong>Hasil:</strong> <p>{{ story }}</p>
                </div>
            </body>
        </html>
    ''', story=story)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
