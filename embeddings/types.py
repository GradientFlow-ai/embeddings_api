from pydantic import BaseModel

class Text(BaseModel):
    document: str

