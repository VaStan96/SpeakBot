from aiogram.fsm.state import StatesGroup, State

class BotState(StatesGroup):
    Start = State()
    NatLang = State()
    ReadyForDialog = State()
    Dialog = State()
    Feedback = State()