import time
import logging 
import platform

import pyrogram
from config import Config
from telegraph import Telegraph
from pyrogram import __version__ as pyrogram_version
from main.core.database import Database
from main.core.helpers import Helpers
from main.core.newpyrogram import Methods






class ClassManager(Config, Helpers, Database, Methods):
    # versions /
    python_version = str(platform.python_version())
    pyrogram_version = str(pyrogram_version)

    # assistant /
    assistant_name = "Toxic"
    assistant_version = "v.0.0.3"

    # userbot /
    userbot_name = "ToxicUserBot"
    userbot_version = "v.0.1.0"

    # containers /
    CMD_HELP = {}

    # owner details /
    owner_name = "❥❥≛⃝❤️🥀【𓆩🇲 𝕣𓆪】 ͢ ̶ͥ ̶ ̶ͣ ͓ ̶ͫ➳🇫𝕒𝕚𝕫𝕒𝕟𓆪🥀𝄗⃝𓆩≛⃝🖤"
    owner_id = 5085606047
    owner_username = "@Faisu_xd"

    # other /
    message_ids = {}
    PIC = "https://telegra.ph/file/38eec8a079706b8c19eae.mp4"
    Repo = "https://github.com/ITZ-FAIZAN/ToxicUserBot.git"
    StartTime = time.time()
    utube_object = object
    callback_user = None
    whisper_ids = {}

    # debugging /
    
   
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logging.getLogger("pyrogram.session.session").setLevel(logging.WARNING) 
    logging.getLogger("pyrogram.session.internals.msg_id").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.dispatcher").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.connection.connection").setLevel(logging.WARNING)
    log = logging.getLogger()

    # telegraph /
    telegraph = Telegraph()
    telegraph.create_account(short_name=Config.TL_NAME if Config.TL_NAME else "Toxic userbot")

