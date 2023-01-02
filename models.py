from pydantic import BaseModel
from enum import Enum

class Languages(str, Enum):
  b = "b"
  c = "c"
  java = "java"
  javascript = "javascript"
  python = "python"

class Programmer(BaseModel):
  id: int
  name: str
  languages: list[Languages]

