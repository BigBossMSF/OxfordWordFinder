from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text="Приветствую! Отправьте слово на английском, которое вы хотите получить из оксфордского словаря")
