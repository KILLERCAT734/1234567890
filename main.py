from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
    types.BotCommand(command='/start', description='команда для того, чтобы запустить бота'),
    types.BotCommand(command='/help', description='команда для того, чтобы узнать, с чем может помочь ваш бот')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('привет!')

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('я могу тебе помочь!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup())