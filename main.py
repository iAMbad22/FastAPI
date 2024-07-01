# main.py

from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta
from database import get_mongo_db, Transcript, create_user_in_db, get_user_from_db
from auth import Token, authenticate_user, create_access_token, get_current_active_user
from transcribe import transcribe_audio

# Define your FastAPI application
app = FastAPI()

ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserCreate(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, 
            detail="Incorrect username or password"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register", response_model=UserCreate)
async def register_user(user: UserCreate):
    db = get_mongo_db()
    if get_user_from_db(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    create_user_in_db(user.username, user.password)
    return user

@app.post("/transcribe")
async def transcribe_audio_file(file: UploadFile = File(...), current_user: str = Depends(get_current_active_user)):
    try:
        format = file.filename.split(".")[-1]
        file_content = await file.read()
        transcript = transcribe_audio(file_content, format)
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error transcribing audio: {str(e)}")

@app.post("/save_transcript")
async def save_transcript(transcript: Transcript, current_user: str = Depends(get_current_active_user)):
    db = get_mongo_db()
    try:
        transcript_dict = transcript.dict()
        transcript_dict["user"] = current_user
        transcript_dict["timestamp"] = datetime.now().isoformat()
        result = db.transcripts.insert_one(transcript_dict)
        return {"message": "Transcript saved successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving transcript: {str(e)}")