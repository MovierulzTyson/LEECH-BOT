"""ThumbNail utilities, © @AnyDLBot"""


import os

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image
from tobrot import DOWNLOAD_LOCATION


async def save_thumb_nail(client, message):
    thumbnail_location = os.path.join(DOWNLOAD_LOCATION, "thumbnails")
    thumb_image_path = os.path.join(
        thumbnail_location, str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("𝙋𝙍𝙊𝘾𝙀𝙎𝙎𝙄𝙉𝙂.....")
    if message.reply_to_message is not None:
        if not os.path.isdir(thumbnail_location):
            os.makedirs(thumbnail_location)
        download_location = thumbnail_location + "/"
        downloaded_file_name = await client.download_media(
            message=message.reply_to_message, file_name=download_location
        )
        # https://stackoverflow.com/a/21669827/4723940
        Image.open(downloaded_file_name).convert("RGB").save(downloaded_file_name)
        metadata = extractMetadata(createParser(downloaded_file_name))
        height = 0
        if metadata.has("height"):
            height = metadata.get("height")
        # resize image
        # ref: https://t.me/PyrogramChat/44663
        img = Image.open(downloaded_file_name)
        # https://stackoverflow.com/a/37631799/4723940
        # img.thumbnail((320, 320))
        img.resize((320, height))
        img.save(thumb_image_path, "JPEG")
        # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
        os.remove(downloaded_file_name)
        await ismgs.edit(
            "✅ 𝘾𝙐𝙎𝙏𝙊𝙈 𝙁𝙄𝙇𝙀/𝙑𝙄𝘿𝙀𝙊 𝙏𝙃𝙐𝙈𝘽𝙉𝘼𝙄𝙇 𝙎𝘼𝙑𝙀𝘿. "
            + "𝙏𝙃𝙄𝙎 𝙄𝙈𝘼𝙂𝙀 𝙒𝙄𝙇𝙇 𝘽𝙀 𝙐𝙎𝙀𝘿 𝙊𝙉 𝙐𝙋𝙇𝙊𝘼𝘿, 𝙏𝙄𝙇𝙇 /clearthumbnail."
        )
    else:
        await ismgs.edit("❌ 𝙍𝙀𝙋𝙇𝙔 𝙏𝙊 𝘼 𝙋𝙃𝙊𝙏𝙊 𝙏𝙊 𝙎𝘼𝙑𝙀 𝙏𝙃𝙐𝙈𝘽𝙉𝘼𝙄𝙇")


async def clear_thumb_nail(client, message):
    thumbnail_location = os.path.join(DOWNLOAD_LOCATION, "thumbnails")
    thumb_image_path = os.path.join(
        thumbnail_location, str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("💠𝙋𝙍𝙊𝘾𝙀𝙎𝙎𝙄𝙉𝙂 ...")
    if os.path.exists(thumb_image_path):
        os.remove(thumb_image_path)
        await ismgs.edit("✅ 𝘾𝙐𝙎𝙏𝙊𝙈 𝙏𝙃𝙐𝙈𝘽𝙉𝘼𝙄𝙇 𝘾𝙇𝙀𝘼𝙍𝙀𝘿 𝙎𝙐𝘾𝘾𝙀𝙎𝙁𝙐𝙇𝙇𝙔.")
    else:
        await ismgs.edit("❌ 𝙉𝙊𝙏𝙃𝙄𝙉𝙂 𝙏𝙊 𝘾𝙇𝙀𝘼𝙍 .")
