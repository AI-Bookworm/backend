from flask import Flask, request, jsonify

app = Flask(__name__)
logger = app.logger

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No image part in the request'}), 400
    
    image = request.files['image']
    
    if image.filename == '':
        return jsonify({'message': 'No image selected for uploading'}), 400
    
    # Here you can add code to save the image or process it as needed
    
    print('Image successfully sent')
    return jsonify({'message': 'Image successfully sent'}), 200

# Use this API to test your local connection
@app.route('/test', methods=['GET'])
def test_post():
    logger.info(f'Received test!')
    return jsonify({'message' : 'Test Works!'}), 200

if __name__ == '__main__':
    app.run(debug=True)