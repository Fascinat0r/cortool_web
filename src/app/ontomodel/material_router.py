# from fastapi import APIRouter, Depends
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from app.auth.base_config import current_active_verified_user
# from app.database import get_async_session
# from app.models.models import Material
# from app.ontomodel.schemas import *
#
# router = APIRouter(
#     prefix="/mat",
#     tags=["Material"],
#     dependencies=[Depends(current_active_verified_user)]
# )
#
# @router.get("")
# async def get_components_by_id(material_id: int, session: AsyncSession = Depends(get_async_session)):
#     # try:
#     query = select(Material).where(Material.id == material_id)
#     result = await session.execute(query)
#     material = result.scalars().first()
#     return material
#     # except Exception:
#     #     raise HTTPException(status_code=500, detail={
#     #         "status": "error",
#     #         "data": None,
#     #         "details": None
#     #     })