import hashlib
import logging
from aiogram import Bot, Dispatcher, types
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter
import config
import markup as nav
from functions import traslate,english_to_leetspeak,zalgo
import dictionaries as dic

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.BOT_TOKEN:
    exit("No token provided")

# init
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)


# States

class Form(StatesGroup):
    selector = State()
    translation = State()


# handlers
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, '3DpaCtBUiTE, {0.first_name}'.format(message.from_user), reply_markup= nav.mainMenu)

@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    """Allow user to cancel action via /cancel command"""
    current_state = await state.get_state()
    if current_state is None:
        # User is not in any state, ignoring
        return
    # Cancel state and inform user about it
    await state.finish()
    await message.reply('OTMEHEHO.',reply_markup= nav.mainMenu)

@dp.message_handler(commands=['translate'])
async def сommand_translate(message: types.Message):
    await Form.selector.set()
    await message.reply("BBeduTe CJlOBAp6", reply_markup=nav.dictionarySelector)


@dp.message_handler(state=Form.selector)
async def process_translation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dictionary'] = message.text
    await Form.next()
    await message.reply("BBeduTe TeKCT", reply_markup=nav.cancelMenu)


@dp.message_handler(state=Form.translation)
async def process_translation(message: types.Message, state: FSMContext):
    await Form.next()
    async with state.proxy() as data:
        data['text'] = message.text
    if data['dictionary'] == 'PyCCkUu':
        responce = traslate(data['text'], dic.first)
        await message.answer(responce, reply_markup=nav.mainMenu)
    elif data['dictionary'] == 'AnGLIySKIy':
        responce = traslate(data['text'], dic.second)
        await message.answer(responce, reply_markup=nav.mainMenu)
    elif data['dictionary'] == 'l33t':
        responce = english_to_leetspeak(data['text'])
        await message.answer(responce, reply_markup=nav.mainMenu)
    elif data['dictionary'] == 'zalgo':
        responce = zalgo().zalgofy(data['text'])
        await message.answer(responce, reply_markup=nav.mainMenu)
    else:
        await message.answer(('BBeDuTE KOPPEKTHbIu\' CJlOBAP6'), reply_markup=nav.mainMenu)
    await state.finish()

@dp.inline_handler()
async def inline_handler (query: types.InlineQuery):
    text = query.query or "BBeDuTe TEKCT"

    translation = {
        "russian": traslate(text, dic.first),
        "english": traslate(text, dic.second),
        "leet": english_to_leetspeak(text),
        "zalgo": zalgo().zalgofy(text),
    }

    article = [
        types.InlineQueryResultArticle(
            id=1,
            title='PyCCkUu',
            description=translation['russian'],
            input_message_content=types.InputTextMessageContent(
                message_text=translation['russian']
            )
        ),
        types.InlineQueryResultArticle(
            id=2,
            title='AnGLIySKIy',
            description=translation['english'],
            input_message_content=types.InputTextMessageContent(
                message_text=translation['english']
            )
        ),
        types.InlineQueryResultArticle(
            id=3,
            title='l33t',
            description=translation['leet'],
            input_message_content=types.InputTextMessageContent(
                message_text=translation['leet']
            )
        ),
        types.InlineQueryResultArticle(
            id=4,
            title='zalgo',
            description=translation['zalgo'],
            input_message_content=types.InputTextMessageContent(
                message_text=translation['zalgo']
            )
        ),
    ]
    await query.answer(article,cache_time=1,is_personal=True)

