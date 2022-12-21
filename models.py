from pydantic import BaseModel
from enum import Enum
from typing import List

class Languages(str, Enum):
  c = "c"
  python = "python"
  javascript = "javascript"

class Programmer(BaseModel):
  id: int
  name: str
  languages: List[Languages]

