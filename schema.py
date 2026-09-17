from datetime import date
from pydantic import BaseModel, Field



class AddUserResponse(BaseModel):
    status : bool
    message: str
 
class AddUserSchema(BaseModel):
    user_name: str
    user_age : int
