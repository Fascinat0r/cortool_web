from datetime import datetime

from pydantic import BaseModel


# class componentCreate(BaseModel):
#     id: int
#     name: str
#     description: str
#     creator_id: int
#     date: datetime
#     names_of_parents: list
#     parents_postfixes: list
#     names_of_heirs: list
#     data: dict
#
#
# class componentUpdate(BaseModel):
#     id: int
#     name: str
#     description: str
#     data: dict
#
#
# class addComponentsConnection(BaseModel):
#     parent_id: int
#     child_id: int
