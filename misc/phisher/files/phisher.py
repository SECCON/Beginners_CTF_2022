import os
import pyocr
import random
import string
import cv2 as cv
import numpy as np
from PIL import ImageFont, ImageDraw, Image


flag = os.getenv("CTF4B_FLAG")

fqdn = "www.example.com"

# TEXT to PNG
def text2png(text:str) -> str:
    os.makedirs("phish", exist_ok=True)
    filename = "".join([random.choice(string.ascii_letters) for i in range(15)])
    png = f"phish/{filename}.png"
    img = np.full((100, 600, 3), 0, dtype=np.uint8)
    font = ImageFont.truetype("font/Murecho-Black.ttf", 64)
    img_pil = Image.fromarray(img)
    ImageDraw.Draw(img_pil).text((10, 0), text[:15], font=font, fill=(255, 255, 255)) # text[:15] :)
    img = np.array(img_pil)
    cv.imwrite(png, img)
    return png

# PNG to TEXT (OCR-English)
def ocr(image:str) -> str:
    tool = pyocr.get_available_tools()[0]
    text = tool.image_to_string(Image.open(image), lang="eng")
    os.remove(image)
    if not text:
        text = "???????????????"
    return text

# Can you deceive the OCR?
# Give me "www.example.com" without using "www.example.com" !!!
def phishing() -> None:
    input_fqdn = input("FQDN: ")[:15]
    ocr_fqdn = ocr(text2png(input_fqdn))
    if ocr_fqdn == fqdn: # [OCR] OK !!!
        for c in input_fqdn:
            if c in fqdn:
                global flag
                flag = f"\"{c}\" is included in \"www.example.com\" ;("
                break
        print(flag)
    else: # [OCR] NG
        print(f"\"{ocr_fqdn}\" is not \"www.example.com\" !!!!")

if __name__ == "__main__":
    print("""       _     _     _                  ____    __
 _ __ | |__ (_)___| |__   ___ _ __   / /\ \  / /
| '_ \| '_ \| / __| '_ \ / _ \ '__| / /  \ \/ /
| |_) | | | | \__ \ | | |  __/ |    \ \  / /\ \\
| .__/|_| |_|_|___/_| |_|\___|_|     \_\/_/  \_\\
|_|
""")
    phishing()
