#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBOt/blob/main/LICENSE > .

from decouple import config


class Var:
    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASS = config("REDIS_PASS", default=None)
    API_ID = config("API_ID", default=19099900, cast=int)
    API_HASH = config("API_HASH", default="2b445de78e5baf012a0793e60bd4fbf5")
    BOT_TOKEN = config("BOT_TOKEN", default="6142266368:AAGfkcM2QMoXNJJVGV6qdZpTZ3JYBAzzLbU")
    BACKUP = config("BACKUP", default=0, cast=int)
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CHAT = config("CHAT", cast=int)
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/37d9d0657d51e01a71f26.jpg"
    )
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    CLOUD = config("CLOUD", cast=int)
    GDRIVE_FOLDER_ID = config("GDRIVE_FOLDER_ID", default=None)
    TOKEN_FILE_LINK = config("TOKEN_FILE_LINK", default=None)
    INDEX_LINK = config("INDEX_LINK", default="https://github.com/")
    OWNERS = config("OWNERS", default="")
    GDRIVE_UPLOAD = config("GDRIVE_UPLOAD", default=False, cast=bool)
