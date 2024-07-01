# transcribe.py

import os
import logging
from deepgram import DeepgramClient, PrerecordedOptions, FileSource
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Deepgram API key
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
if not DEEPGRAM_API_KEY:
    raise ValueError("DEEPGRAM_API_KEY environment variable is not set.")

# Initialize Deepgram client
deepgram = DeepgramClient(DEEPGRAM_API_KEY)

def transcribe_audio(file: bytes, format: str) -> str:
    try:
        logger.debug("Transcribing audio file")

        # Prepare the payload
        payload: FileSource = {
            "buffer": file,
        }

        # Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # Call the transcribe_file method with the payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        # Extract and return the transcript from the response
        return response
        # .to_json(indent=4)["results"]["channels"][0]["alternatives"][0]["transcript"]

    except Exception as e:
        logger.error(f"Error transcribing audio: {e}")
        raise
