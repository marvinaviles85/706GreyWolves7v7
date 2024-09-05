from rembg import remove
from PIL import Image

input_path = ".venv/Scripts/Images/706gw.jpg"
output_path = ".venv/Scripts/Images/706gw_no_bg.png"

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
