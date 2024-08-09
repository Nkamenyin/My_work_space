#/usr/bin/python3

""" This API allows users to upload profile pictures. Use request files to handle image uploads and dependencies to validate image dimensions and formats, with error handling for invalid submissions."""

from fastapi import Depends, File, UploadFile, HTTPException
from PIL import Image

app = FastAPI()

def validate_image(file: UploadFile = File()):
    if image.width < 100 or image.height < 100:
        raise HTTPException(status_code=400, detail="Image dimensions must be at least 100x100")
    if image.format not in ["JPEG", "PNG"]:
        raise HTTPException(status_code=400, detail="Only JPEG and PNG formats are allowed")
    if not file.content_type.startswith("image/"):
    raise HTTPException(status_code=400, detail="images only")
    return file


@app.post("/profile_picture") #the endpoint
def profile_picture_upload(file: UploadFile = Depends(validate_image)):
    return {"message": "Upload successful"}
