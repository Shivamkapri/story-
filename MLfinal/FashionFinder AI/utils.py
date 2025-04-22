import os
import numpy as np
import pickle
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from keras.layers import GlobalMaxPooling2D
from keras.models import Model
from sklearn.neighbors import NearestNeighbors

# Load and prepare ResNet50 model
resnet = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model = Model(inputs=resnet.input, outputs=GlobalMaxPooling2D()(resnet.output))

# Load embeddings and filenames
with open(os.path.join('model', 'embeddings.pkl'), 'rb') as f:
    embeddings = pickle.load(f)
with open(os.path.join('model', 'filenames.pkl'), 'rb') as f:
    filenames = pickle.load(f)

# Build full image paths
IMAGE_DIR = os.path.join('static', 'images')
image_paths = [os.path.join(IMAGE_DIR, fname) for fname in filenames]

# Fit Nearest Neighbors on embeddings
neighbors = NearestNeighbors(n_neighbors=5, metric='cosine', algorithm='brute')
neighbors.fit(embeddings)

def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded = np.expand_dims(img_array, axis=0)
    preprocessed = preprocess_input(expanded)
    features = model.predict(preprocessed)
    return features.flatten()

def recommend_similar_images(img_path):
    query_features = extract_features(img_path)
    distances, indices = neighbors.kneighbors([query_features])
    return [image_paths[idx] for idx in indices[0]]