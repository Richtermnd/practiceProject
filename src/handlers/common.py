import enum
from typing import Any

import aiogram
from aiogram import types, filters
from aiogram.fsm import context

import logger


class Command(enum.Enum):
    START = "start"
    ABOUT = "about"

answers: dict[Command, dict[str, Any]] = {
    Command.START: {
        "text": "greeting message"
    },
    Command.ABOUT: {
        "text": "about message"
    }
}

router = aiogram.Router()

@router.message(filters.Command(commands=[Command.START.value]))
async def cmd_start(message: types.Message, state: context.FSMContext):
    log = logger.get_logger("command start")
    log.withAttrs(from_user_id=message.from_user.id)  # type: ignore
    log.debug("command received")
    await message.answer(**answers[Command.START])
    log.debug("handled")


@router.message(filters.Command(commands=[Command.ABOUT.value]))
async def cmd_about(message: types.Message, state: context.FSMContext):
    log = logger.get_logger("command about")
    log.withAttrs(from_user_id=message.from_user.id)  # type: ignore
    log.debug("command received")
    await message.answer(**answers[Command.ABOUT])
    log.debug("handled")


