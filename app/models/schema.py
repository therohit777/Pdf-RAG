from pydantic import BaseModel
from typing import List, Optional,Union

class ApiResponse(BaseModel):
    status_code: int
    message: str
    data: Union[list, dict, None]

class LinkQueryModel(BaseModel):
    link_data: List[dict]