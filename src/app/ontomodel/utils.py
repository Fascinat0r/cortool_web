# from sqlalchemy import select
#
# from app.models.models import *
#
#
# async def isComponentWithIdExist(component_id: int, session):
#     query = select(Component).where(Component.id == int(component_id)).limit(1)
#     components = await session.execute(query)
#     return len(list(components)) != 0
#
#
# async def isComponentWithNameExist(component_name: str, session):
#     query = select(Component.id).where(Component.name == component_name).limit(1)
#     components = await session.execute(query)
#     return len(list(components)) != 0
