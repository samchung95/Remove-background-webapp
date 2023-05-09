from rembg import remove, new_session
from PIL import Image

class Remover:
    '''
    u2net (download, source): A pre-trained model for general use cases.
    u2netp (download, source): A lightweight version of u2net model.
    u2net_human_seg (download, source): A pre-trained model for human segmentation.
    u2net_cloth_seg (download, source): A pre-trained model for Cloths Parsing from human portrait. Here clothes are parsed into 3 category: Upper body, Lower body and Full body.
    silueta (download, source): Same as u2net but the size is reduced to 43Mb.
    isnet-general-use (download, source): A new pre-trained model for general use cases.
    sam (download encoder, download decoder, source): A pre-trained model for any use cases.
    '''

    def __init__(self) -> None:
        pass

    def remove_bg(b:bytes):
        sess = new_session("isnet-general-use")
        image = Image.open(b)
        output = remove(image,session=sess)
        # output = output.convert('RGBA')

        return output

if __name__ == "__main__":
    sess = new_session("u2net")
    image = Image.open("photo/test1.jpg")
    output = remove(image,session=sess)
    output.save("photo/output.png")

# output.save(output_path)