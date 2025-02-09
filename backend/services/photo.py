import io
import binascii

from PIL import Image
from fastapi import HTTPException


async def hex_to_image(hex_str: str) -> io.BytesIO:
    try:
        image_bytes = binascii.unhexlify(hex_str)

        image = Image.open(io.BytesIO(image_bytes))

        buf = io.BytesIO()
        image.save(buf, format="PNG")
        print(image.format)
        buf.seek(0)
        return buf
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid hex data: {str(e)}")
