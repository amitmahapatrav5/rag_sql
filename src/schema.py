from typing import List

from pydantic import BaseModel


class File(BaseModel):
    name: str

class RequestToInsertFile(BaseModel):
    file: File
    owner: str

class RequestToDeleteFile(RequestToInsertFile):
    pass

class ResponseForGettingFiles(BaseModel):
    files: List[File]