from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    images_dir = os.path.join(app.static_folder, 'images')
    images = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith('.png')]
    random_image = random.choice(images)
    return render_template('index.html', image=random_image)

if __name__ == '__main__':
    app.run(debug=True)
