import os
from uuid import uuid4


UPLOAD_DIR = "app/static/uploads"


def save_file(file):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    filename = f"{uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path