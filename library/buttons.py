
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Buttons used

home_button = [
    [InlineKeyboardButton("๐ Source", "source_btn"),
     InlineKeyboardButton("โฌ๏ธ  Fr. Id", "from_btn"),
     InlineKeyboardButton("โ Help", url="https://telegra.ph/4-UI-Help-05-30")],
    [InlineKeyboardButton("๐ฏ Target", "target_btn"),
     InlineKeyboardButton("โฌ๏ธ  To Id", "up_to_btn"),
     InlineKeyboardButton("Types  โก", "types_btn")],
    [InlineKeyboardButton("Delayed", "delay_btn"),
     InlineKeyboardButton("Caption", "caption_btn"),
     InlineKeyboardButton("FNAC", "f_caption_btn")],
    [InlineKeyboardButton("๐๏ธ  View", "view_btn"),
     InlineKeyboardButton("๐ฎ  Reset", "rst_btn"),
     InlineKeyboardButton("โ  Close", "close_btn")],
    [InlineKeyboardButton("๐ฆ Clone Medias ๐ฆ", "clone_btn")]
]


start_button = [
    [InlineKeyboardButton("๐ GitHub ๐", url="github.com/4/4"),
     InlineKeyboardButton("โ๏ธSettings โ", "start_btn")]
]


types_button = [
    [InlineKeyboardButton(" โบ Docs", "docs_btn"),
     InlineKeyboardButton(" โบ Video", "video_btn"),
     InlineKeyboardButton(" โบ Audio", "audio_btn")],
    [InlineKeyboardButton(" โบ Photo", "photo_btn"),
     InlineKeyboardButton(" โบ Voice", "voice_btn"),
     InlineKeyboardButton("โ๏ธ View", "view_types")],
    [InlineKeyboardButton("โฌ๏ธ Back", "start_btn")]
]


stop_button = [
    [InlineKeyboardButton("๐ซ STOP ๐ซ", "stop_clone")]
]


finished_button = [
    [InlineKeyboardButton("๐   HOME", "start_btn"),
     InlineKeyboardButton("โ  CLOSE", "close_btn")]
]


terminate_btn = [
    [InlineKeyboardButton("๐งธ Updates", url="https://github.com/m4mallu/clonebot-ui"),
     InlineKeyboardButton("โ Usage", url="https://telegra.ph/Clonebot-UI-Help-05-30")],
    [InlineKeyboardButton("๐ซ Terminate", "terminate_btn"),
     InlineKeyboardButton("๐  Home", "start_btn")]
]

indexing_skip_button = [
        [
            InlineKeyboardButton("๐น Skip", "index_skip_btn")
        ]
    ]

purging_skip_button = [
        [
            InlineKeyboardButton("๐น Skip", "purge_skip_btn")
        ]
    ]

purge_button = [
    [
        InlineKeyboardButton("Nop", "purge_no_btn"),
        InlineKeyboardButton("Purge it ๐", "purge_yes_btn")
    ]
]

# markups used

reply_markup_purge = InlineKeyboardMarkup(purge_button)

reply_markup_skip_index = InlineKeyboardMarkup(indexing_skip_button)

reply_markup_skip_purge = InlineKeyboardMarkup(purging_skip_button)

reply_markup_stop = InlineKeyboardMarkup(stop_button)

reply_markup_home = InlineKeyboardMarkup(home_button)

reply_markup_start = InlineKeyboardMarkup(start_button)

reply_markup_terminate = InlineKeyboardMarkup(terminate_btn)

reply_markup_finished = InlineKeyboardMarkup(finished_button)

reply_markup_types_button = InlineKeyboardMarkup(types_button)
