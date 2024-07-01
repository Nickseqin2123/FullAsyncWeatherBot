from aiogram import Router
from UserOperations.get_weath import router as weath_router


router = Router(name=__name__)

router.include_routers(
    weath_router
)