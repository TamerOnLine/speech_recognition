
# 🎙️ Speech Recognition (Arabic) using OpenAI Whisper

This is a simple yet professional Python project for transcribing **Arabic speech from video files** using OpenAI's [Whisper](https://github.com/openai/whisper) model.

---

## 📁 Project Structure

```
tameronline-speech_recognition/
├── app.py               # Main script for transcription
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🔧 What It Does

- Loads a Whisper model (base, small, medium, etc.)
- Extracts audio from the given video file
- Transcribes Arabic speech to text with high accuracy
- Displays the result in the terminal
- Can be extended to save the result in a `.txt` file

---

## 📋 Requirements

- Python 3.8+
- `ffmpeg` installed and added to system PATH
- Internet connection (for the first-time model download)

---

## 🚀 Setup & Usage

1. **Clone the repository** (or download it as a ZIP):
   ```bash
   git clone https://github.com/your-username/speech_recognition.git
   cd speech_recognition
   ```

2. **(Optional)** Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

---

## 📦 Example Code

```python
from app import transcribe_video_to_text

text = transcribe_video_to_text("video.mp4", model_size="base")
```

---

## ⚠️ FFMPEG Required

Please make sure [`ffmpeg`](https://ffmpeg.org/download.html) is installed on your system and available in your environment `PATH`.

If not available, the script will fail to read video/audio files.

---

## 🖥️ GUI Alternative (No Coding)

For non-programmers or quick use, try this free and open-source desktop app:

### 🔗 [Whisper Desktop GUI](https://github.com/Const-me/Whisper)

- No Python needed
- Works directly on Windows
- Supports Arabic speech recognition
- Drag-and-drop interface

---

## 📄 License & Credits

- Uses OpenAI's [Whisper](https://github.com/openai/whisper)
- Free to use, modify, and extend

---

## 🙋‍♂️ Author

**TamerOnLine**  
🔗 [GitHub](https://github.com/TamerOnLine) | [LinkedIn](https://www.linkedin.com/in/tameronline) | [YouTube](https://www.youtube.com/@TamerOnPi)
