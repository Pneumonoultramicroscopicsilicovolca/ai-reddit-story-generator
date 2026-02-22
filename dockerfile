FROM python:3.9-slim

# Instal tools video (FFmpeg)
RUN apt-get update && apt-get install -y ffmpeg imagemagick && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Instal library inti
RUN pip install --no-cache-dir google-generativeai edge-tts moviepy flask

# Port khusus Hugging Face
EXPOSE 7860

CMD ["python", "app.py"]
