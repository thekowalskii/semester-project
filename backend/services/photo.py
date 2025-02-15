import io
import binascii
import base64

from PIL import Image
from fastapi import HTTPException


def hex_to_image(hex_str: str) -> io.BytesIO:
    try:
        image_bytes = binascii.unhexlify(hex_str)

        image = Image.open(io.BytesIO(image_bytes))

        buf = io.BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)
        return buf
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid hex data: {str(e)}")


def hex_to_base64(hex_str: str):
    binary_data = bytes.fromhex(hex_str)

    # Кодування в Base64
    base64_encoded = base64.b64encode(binary_data).decode("utf-8")

    print(base64_encoded)


# async def get_photo(title: str)
