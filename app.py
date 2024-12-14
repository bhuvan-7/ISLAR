from flask import Flask, request, render_template, send_file
import os
from PIL import Image
import tensorflow as tf
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load your trained model (update path as needed)
model = tf.keras.models.load_model(r"E:\ISL\models\indian_sign_language_model.h5")

# Mapping of text to ISL sign images (update paths accordingly)
text_to_sign_mapping = {
    "A": r"E:\dataset\alphabets\A\1.jpg",
    "B": r"E:\dataset\alphabets\B\1.jpg",
    "C": r"E:\dataset\alphabets\C\1.jpg",
    "D": r"E:\dataset\alphabets\D\1.jpg",
    "E": r"E:\dataset\alphabets\E\1.jpg",
    "F": r"E:\dataset\alphabets\F\1.jpg",
    "G": r"E:\dataset\alphabets\G\1.jpg",
    "H": r"E:\dataset\alphabets\H\1.jpg",
    "I": r"E:\dataset\alphabets\I\1.jpg",
    "J": r"E:\dataset\alphabets\J\1.jpg",
    "K": r"E:\dataset\alphabets\K\1.jpg",
    "L": r"E:\dataset\alphabets\L\1.jpg",
    "M": r"E:\dataset\alphabets\M\1.jpg",
    "N": r"E:\dataset\alphabets\N\1.jpg",
    "O": r"E:\dataset\alphabets\O\1.jpg",
    "P": r"E:\dataset\alphabets\P\1.jpg",
    "Q": r"E:\dataset\alphabets\Q\1.jpg",
    "R": r"E:\dataset\alphabets\R\1.jpg",
    "S": r"E:\dataset\alphabets\S\1.jpg",
    "T": r"E:\dataset\alphabets\T\1.jpg",
    "U": r"E:\dataset\alphabets\U\1.jpg",
    "V": r"E:\dataset\alphabets\V\1.jpg",
    "W": r"E:\dataset\alphabets\W\1.jpg",
    "X": r"E:\dataset\alphabets\X\1.jpg",
    "Y": r"E:\dataset\alphabets\Y\1.jpg",
    "Z": r"E:\dataset\alphabets\Z\1.jpg",
    "1": r"E:\dataset\numericals\1\14.jpg",
    "2": r"E:\dataset\numericals\2\14.jpg",
    "3": r"E:\dataset\numericals\3\14.jpg",
    "4": r"E:\dataset\numericals\4\14.jpg",
    "5": r"E:\dataset\numericals\5\14.jpg",
    "6": r"E:\dataset\numericals\6\14.jpg",
    "7": r"E:\dataset\numericals\7\14.jpg",
    "8": r"E:\dataset\numericals\8\14.jpg",
    "9": r"E:\dataset\numericals\9\14.jpg"
}

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle text-to-ISL conversion
@app.route('/convert', methods=['POST'])
def convert_text():
    text = request.form.get('text', '').strip()
    if text:
        # Convert the entered text to corresponding ISL images
        images_folder = "static/converted_images/"
        os.makedirs(images_folder, exist_ok=True)
        
        image_files = []
        for char in text.upper():
            if char in text_to_sign_mapping:
                img_path = text_to_sign_mapping[char]
                img = Image.open(img_path)
                output_path = os.path.join(images_folder, f"{char}.jpg")
                img.save(output_path)
                # Save path relative to static directory
                image_files.append(f"converted_images/{char}.jpg")
        
        return render_template('show_images.html', images=image_files)
    else:
        return "No text entered. Please enter text to convert.", 400

# Route to serve the generated images (if needed)
@app.route('/static/<filename>')
def serve_image(filename):
    return send_file(os.path.join('static/converted_images', filename))

if __name__ == '__main__':
    app.run(debug=True)
