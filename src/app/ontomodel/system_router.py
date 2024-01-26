# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy import insert
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from app.auth.base_config import current_active_verified_user
# from app.database import get_async_session
# from app.models.models import System
# from app.ontomodel.utils import isComponentWithIdExist
#
# router = APIRouter(
#     prefix="/system",
#     tags=["System"],
#     dependencies=[Depends(current_active_verified_user)]
# )
#
#
# @router.get("/add/{component_id}")
# async def create_system_from_component_by_id(component_id: int, session: AsyncSession = Depends(get_async_session)):
#     if not await isComponentWithIdExist(component_id, session):
#         raise HTTPException(status_code=400, detail={
#             "status": "error",
#             "data": None,
#             "details": f"Component with id:{component_id} does not exist"
#         })
#     stmt = insert(System).values(parent_id=component_id)
#     await session.execute(stmt)
#     await session.commit()
#     return {
#         "status": "success",
#         "data": None,
#         "details": None
#     }
