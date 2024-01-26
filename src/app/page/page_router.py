from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.auth.base_config import current_active_verified_user, current_admin
from app.models.models import User

templates = Jinja2Templates(directory="./front/templates")
router = APIRouter(
    tags=["Pages"]
)


# @router.get("/viewing-save", response_class=HTMLResponse)
# def protected_route(request: Request, user: User = Depends(current_admin)):
#     return templates.TemplateResponse("viewing_save.html", {"request": request})
#
#
# @router.get("/viewing/", response_class=HTMLResponse)
# async def read_item(request: Request, id: str, user: User = Depends(current_active_verified_user)):
#     return templates.TemplateResponse("viewing.html", {"request": request, "id": id})
#
#
# @router.get("/material-save", response_class=HTMLResponse)
# async def read_item(request: Request, user: User = Depends(current_admin)):
#     return templates.TemplateResponse("material-save.html", {"request": request})
#
#
# @router.get("/material/", response_class=HTMLResponse)
# async def read_item(request: Request, id: str, user: User = Depends(current_active_verified_user)):
#     return templates.TemplateResponse("material.html", {"request": request, "id": id})


@router.get("/sign-in", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("sign-in.html", {"request": request})


@router.get("/auth", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})
