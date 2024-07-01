# test_transcription.py

import os
from transcribe import transcribe_audio

if __name__ == "__main__":
    # Adjust the path to the real audio file you have for testing
    test_file_path = "recording.mp3"  # Assuming the file is in the same directory

    try:
        with open(test_file_path, "rb") as f:
            file_content = f.read()
        format = test_file_path.split(".")[-1]
        transcript = transcribe_audio(file_content, format)
        print("Transcription successful:")
        print(transcript)
    except Exception as e:
        print(f"Error: {e}")
