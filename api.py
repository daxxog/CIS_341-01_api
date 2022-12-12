from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

class UserInformationItem(BaseModel):
    id: int
    # note: I commented this out because it doesn't make much sense
    # without implementing authentication and authorization
    # user_id: int = 2
    title: str
    details: str

app = FastAPI()
app.include_router(CRUDRouter(schema=UserInformationItem))
