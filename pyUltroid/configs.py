# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", "29981514" =6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", "8f913218d44ff822f6c85a8622a15b36")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", "1BVtsOHUBu34FURBx2h2mkN4svUOcarnrgP5r5-71rmBgkZHm1LJiMJBElG-sJFGc3P2LY34_G-7wKKththq3X-RTgHeahx5KzvhnRpIoF5jXBsDe7vNogLSM7NL2UOkwgtDYPCVkPgSBrhJ3HxRo3hX9KIfqFNqDZyB_mlWQAA9YwYxv45EWpCrCmGapuMnjM7G0KuMJTfx7Jxdshoh8j3sOTHIxFcBFW-mI1syAghpWeC3RisFlo_ZBcHq28ysmLi5bmpzIcigkKlQG9TxDg6QlBuFn6DtMnZImiEsNBP1uONbtWS01i550cS5RIj6Xzhb_oUaGSK6V-2cCjzSw3wYhTFZpEk8")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", "redis-13227.c299.asia-northeast1-1.gce.cloud.redislabs.com:13227"))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", "JiPZPKbGUTZInzOlSMmfJubWniGk3CEy")
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
