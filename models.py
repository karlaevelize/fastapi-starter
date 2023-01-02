from pydantic import BaseModel
from enum import Enum
from typing import List

class Languages(str, Enum):
  b = "b"
  c = "c"
  java = "java"
  javascript = "javascript"
  python = "python"

class Programmer(BaseModel):
  id: int
  name: str
  languages: List[Languages]

