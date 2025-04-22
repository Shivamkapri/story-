#  FashionFinder AI 
A Deep Learning based Fashion Recommender System using the ResNET50

This project is a content-based image recommender system that suggests visually similar fashion items based on an uploaded image. It is built using  TensorFlow, Keras,flask and scikit-learn.

## Features
- Upload an image of a fashion item
- Extract visual features using a pre-trained ResNet50 model
- Recommend top 5 similar items from the dataset
- Web interface

## Project 

├── static/
│   ├── uploads/              Uploaded images
│   └── images/               Fashion dataset images
├── templates/               HTML pages
├── model/                   Pickled embeddings and filenames
├── app.py                   Main Flask app
├── utils.py                 Feature extraction and recommendation
├── requirements.txt         Dependencies
└── README.md               


# Setup Instructions
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. <<Ensure your dataset images are in `static/images/`>>
4. Run the app: `python app.py`
5. Open browser at: `http://localhost:5000`

## Dataset Preprocessing
<<<Before running the app, make sure `embeddings.pkl` and `filenames.pkl` are generated using ResNet50 features.>>>
dataset link :- 1. https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small
                2. https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset


