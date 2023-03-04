#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT

nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT)
# nonebot.load_builtin_plugins("echo")
# nonebot.load_plugin("nonebot_plugin_gocqhttp")
# nonebot.load_plugin("nonebot_plugin_status")
# nonebot.load_plugin('nonebot_plugin_picsearcher')
# nonebot.load_plugin('nonebot_plugin_help')
# nonebot.load_plugin('nonebot_plugin_simplemusic')
# nonebot.load_plugin('nonebot_plugin_code')
# nonebot.load_plugin('nonebot_plugin_petpet')
# nonebot.load_plugin('nonebot_plugin_crazy_thursday')
# nonebot.load_plugin('nonebot_plugin_smart_reply')

nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")