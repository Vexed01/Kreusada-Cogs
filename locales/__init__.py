import json
import pathlib

from .locales import Locales

with open(pathlib.Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]

async def setup(bot):
    cog = Locales(bot)
    await cog.initialize()
    bot.add_cog(cog)