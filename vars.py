{
    "name": "𝐀𝐉 𝐓𝐄𝐗𝐓 𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐑",
    "description": "𝑻𝒆𝒙𝒕 𝑳𝒆𝒆𝒄𝒉 𝑽𝒊𝒅𝒆𝒐 𝑬𝒙𝒕𝒓𝒂𝒄𝒕𝒐𝒓 𝑭𝒐𝒓 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎",
    "logo": "http://envs.sh/ten.jpg",
    "keywords": [
        "text-video",
        "video-extract",
        "pyrogram"
    ],
    "repository": "https://github.com/AJ-PYTHON",
    "success_url": "https://t.me/AJ_TECH_WORLD",
    "stack": "container",
    "env": {
        "api_id": {
            "description": "𝑬𝒏𝒕𝒆𝒓 𝒀𝒐𝒖𝒓 𝑨𝒑𝒊 𝑰𝑫",28225971
            "required": true
        },
        "api_hash": {
            "description": "𝑬𝒏𝒕𝒆𝒓 𝒀𝒐𝒖𝒓 𝑨𝒑𝒊 𝑯𝒂𝒔𝒉",d5de247a7d8b865b48d1bb5944058315
            "required": true
        },
        "bot_token": {
            "description": "𝑬𝒏𝒕𝒆𝒓 𝒀𝒐𝒖𝒓 𝑩𝒐𝒕 𝑻𝒐𝒌𝒆𝒏",
            "required": true
        },
        "pwtoken": {
            "description": "𝑬𝒏𝒕𝒆𝒓 𝒀𝒐𝒖𝒓 𝑻𝒐𝒌𝒆𝒏",
            "required": true
        }
    },
    "addons": [],
    "buildpacks": [
        {
            "url": "heroku/python"
        },
        {
            "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git"
        }
    ]
}
