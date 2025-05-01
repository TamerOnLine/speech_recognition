import os
import whisper


def transcribe_video_to_text(file_path: str, model_size: str = "base") -> str:
    """
    Transcribes Arabic speech from a video file using OpenAI's Whisper model.

    Args:
        file_path (str): The path to the video file.
        model_size (str): The size of the Whisper model to use (e.g., "base", "small", "medium", "large").

    Returns:
        str: The transcribed text from the video.
    """
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return ""

    # Load the Whisper model
    model = whisper.load_model(model_size)

    # Transcribe audio to text
    result = model.transcribe(file_path, language="ar")

    # Print and return the transcribed text
    print("Extracted text:\n", result["text"])
    return result["text"]


# Example usage
transcribe_video_to_text("video.mp4")
