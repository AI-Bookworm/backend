from flask import Flask, request, jsonify
import api

app = Flask(__name__)
logger = app.logger

@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    test_mode = request.args.get('test')
    
    if test_mode == None:
        # The "real" code will go here.
        if 'image' not in request.files:
            return jsonify({'message': 'No image part in the request'}), 400
        
        image = request.files['image']
        return api.get_book_data(image)
    
    if test_mode == 'notfound':
        return jsonify({'message': 'Test 404 invoked!'}), 404
    
    if test_mode == 'error':
        return jsonify({'message': 'Test 500 invoked!'}), 500
    
    if test_mode == 'success':
        if 'image' not in request.files:
            return jsonify({'message': 'No image part in the request'}), 400
    
        return jsonify({
            'title': 'Book Title',
            'subtitle': 'Book Subtitle',
	        'author':'Author' ,
	        'rating': 3.5,
	        'length': '271',
	        'categories': ['Category 1', 'Category 2'],
	        'description': 'Book Description. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
        }), 200

# Use this API to sanity test your local connection
@app.route('/', methods=['GET'])
def test_post():
    logger.info(f'Connection success!')
    return jsonify({'message' : 'Test Works!'}), 200

if __name__ == '__main__':
    app.run(debug=True)