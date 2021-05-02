from PIL import Image, ImageDraw, ImageFont


class Data2Image:
    def __init__(self, image_name) -> None:
        self.image_name = image_name

    def write_image(self, text: str, font_path: str,
                    font_size: int,
                    image_mode: str, image_size=None,
                    image_color=None,
                    text_color=None):
        img = Image.new(mode=image_mode, size=image_size,
                        color=image_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        draw.text((10, 10), text=text, fill=text_color, font=font)
        img.save(self.image_name)
