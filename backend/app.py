from rembg import remove, new_session
from PIL import Image

input_path = 'photo/test.jpeg'
output_path = 'photo/output1.png'


input = Image.open(input_path)
sess = new_session("isnet-general-use")
output = remove(input,session=sess)


output.save(output_path)