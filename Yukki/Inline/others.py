from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="❰𝙎𝙚𝙖𝙧𝙘𝙝 𝙇𝙮𝙧𝙞𝙘𝙨❱",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝙔𝙤𝙪𝙧 𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩❱",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥 𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩❱",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❰𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝘼𝙪𝙙𝙞𝙤/𝙑𝙞𝙙𝙚𝙤❱",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝙂𝙤 𝘽𝙖𝙘𝙠❱",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❰🗑 𝗖𝗹𝗼𝘀𝗲❱",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰𝙂𝙚𝙩 𝘼𝙪𝙙𝙞𝙤❱",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❰𝙂𝙚𝙩 𝙑𝙞𝙙𝙚𝙤❱",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❰𝙂𝙤 𝘽𝙖𝙘𝙠❱", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="❰🗑 𝗖𝗹𝗼𝘀𝗲❱", callback_data=f"close"),
        ],
    ]
    return buttons
