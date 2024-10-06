
from pydantic import BaseModel
from datetime import datetime


class ProblematicInputBase(BaseModel):
    problematic_id: int
    dataJson: str
    timestamp: datetime

class ProblematicInputResponse(ProblematicInputBase):
    id: int
