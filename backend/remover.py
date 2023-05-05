from rembg import remove, new_session
from PIL import Image

class Remover:

    def __init__(self) -> None:
        pass

    def remove_bg(b:bytes):
        sess = new_session("isnet-general-use")
        image = Image.open(b)
        output = remove(image,session=sess)

        return output

# output.save(output_path)