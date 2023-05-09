from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
import io
import os
from remover import Remover

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files.get('image')

    if image:
        removed = Remover.remove_bg(image)
        # removed.save(os.path.join('images', image.filename))
        img_io = io.BytesIO()
        removed.save(img_io, 'png')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png'), 200
    else:
        return jsonify({'message': 'No image provided.'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)