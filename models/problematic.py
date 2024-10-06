from pydantic import BaseModel

class ProblematicBase(BaseModel):
    name: str

class ProblematicResponse(ProblematicBase):
    id: int
