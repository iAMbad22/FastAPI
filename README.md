FastAPI Transcription Service
This is a FastAPI application that provides endpoints for audio file transcription and saving transcripts to a MongoDB database.

Features
User Authentication: Secure endpoints using OAuth2 JWT authentication.
File Transcription: Transcribe audio files uploaded by users using Deepgram API.
Transcript Storage: Save transcripts along with user information to MongoDB.
Error Handling: Detailed error messages for better debugging.
Installation
Prerequisites
Python 3.7+
MongoDB (or MongoDB Atlas for cloud deployment)
Deepgram API Key
Setup
Clone the repository:

bash
Copy code
git clone <repository-url>
cd fastapi-transcription-service
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory with the following:

makefile
Copy code
DATABASE_URL=<mongodb-uri>
DG_API_KEY=<deepgram-api-key>
Replace <mongodb-uri> with your MongoDB connection URI and <deepgram-api-key> with your Deepgram API key.

Run the application:

bash
Copy code
uvicorn main:app --reload
The API will start running locally at http://localhost:8000.

Usage
Endpoints
GET /: Root endpoint with a welcome message.
POST /token: Obtain JWT token for authentication.
POST /register: Register a new user.
POST /transcribe: Upload an audio file to transcribe.
POST /save_transcript: Save a transcript to the database.
Example
To transcribe an audio file using the /transcribe endpoint:

Obtain a JWT token using /token endpoint.
Use Postman or curl to send a POST request to /transcribe with the audio file.
The server will transcribe the file using Deepgram API and return the transcript.
Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.