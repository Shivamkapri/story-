from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
from utils import recommend_similar_images

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if 'image' not in request.files:
            error = 'No file part'
            return render_template('index.html', error=error)
        file = request.files['image']
        if file.filename == '':
            error = 'No selected file'
            return render_template('index.html', error=error)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Get top-5 similar images
        recommendations = recommend_similar_images(filepath)

        return render_template(
            'results.html',
            uploaded_image=url_for('static', filename=f'uploads/{filename}'),
            recommendations=[url_for('static', filename=path.split('static/')[1]) for path in recommendations]
        )
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)