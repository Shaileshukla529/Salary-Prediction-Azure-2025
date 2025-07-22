from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import traceback
import os

app = Flask(__name__)

# --- Global Variables ---
model = None
scaler = None
target_encoder = None
feature_encoders = {}
training_columns = None

# --- Model and Dependency Loading ---
def load_dependencies():
    """Load model, scaler, and pre-fitted encoders from disk."""
    global model, scaler, target_encoder, feature_encoders, training_columns
    
    models_dir = 'models'
    
    # Debug: Print current working directory and check if models directory exists
    print(f"Current working directory: {os.getcwd()}")
    print(f"Models directory exists: {os.path.exists(models_dir)}")
    if os.path.exists(models_dir):
        print(f"Files in models directory: {os.listdir(models_dir)}")
    
    try:
        model_path = os.path.join(models_dir, 'best_gradient_boosting_model.pkl')
        scaler_path = os.path.join(models_dir, 'scaler.pkl')
        encoder_path = os.path.join(models_dir, 'label_encoder.pkl')
        
        print(f"Trying to load model from: {model_path}")
        print(f"Model file exists: {os.path.exists(model_path)}")
        
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        target_encoder = joblib.load(encoder_path)

        # Define the exact categories for each feature based on the notebook.
        # This ensures the encoding is stable and matches the training phase.
        feature_encoders['workclass'] = LabelEncoder().fit(['Private', 'Self-emp-not-inc', 'Local-gov', 'State-gov', 'Self-emp-inc', 'Federal-gov', 'Without-pay', 'Others', 'Never-worked'])
        feature_encoders['marital-status'] = LabelEncoder().fit(['Married-civ-spouse', 'Never-married', 'Divorced', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'])
        feature_encoders['occupation'] = LabelEncoder().fit(['Prof-specialty', 'Craft-repair', 'Exec-managerial', 'Adm-clerical', 'Sales', 'Other-service', 'Machine-op-inspct', 'Transport-moving', 'Handlers-cleaners', 'Farming-fishing', 'Tech-support', 'Protective-serv', 'Priv-house-serv', 'Armed-Forces', 'Others'])
        feature_encoders['relationship'] = LabelEncoder().fit(['Husband', 'Not-in-family', 'Own-child', 'Unmarried', 'Wife', 'Other-relative'])
        feature_encoders['race'] = LabelEncoder().fit(['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])
        feature_encoders['gender'] = LabelEncoder().fit(['Male', 'Female'])
        
        # A simplified list for native-country to keep it manageable
        country_classes = ['United-States', 'Mexico', 'Philippines', 'Germany', 'Puerto-Rico', 'Canada', 'El-Salvador', 'India', 'Cuba', 'England', 'Jamaica', 'South', 'China', 'Italy', 'Dominican-Republic', 'Vietnam', 'Guatemala', 'Japan', 'Poland', 'Columbia', 'Taiwan', 'Haiti', 'Iran', 'Portugal', 'Nicaragua', 'Peru', 'France', 'Ecuador', 'Ireland', 'Hong', 'Cambodia', 'Trinadad&Tobago', 'Laos', 'Thailand', 'Yugoslavia', 'Outlying-US(Guam-USVI-etc)', 'Honduras', 'Hungary', 'Scotland', 'Holand-Netherlands']
        feature_encoders['native-country'] = LabelEncoder().fit(country_classes)

        # Define the final column order the model expects
        training_columns = [
            'age', 'workclass', 'fnlwgt', 'educational-num', 'marital-status',
            'occupation', 'relationship', 'race', 'gender', 'capital-gain',
            'capital-loss', 'hours-per-week', 'native-country'
        ]
        
        print("✅ Model and dependencies loaded successfully.")
        return True
    except FileNotFoundError as e:
        print(f"❌ Error loading dependencies: {e}. Make sure model files are in the 'models' directory.")
        return False

# --- Flask Routes ---
@app.route('/')
def home():
    """Render the main prediction page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle the prediction request."""
    if not model:
        return jsonify({'error': 'Model is not loaded!', 'success': False}), 500

    try:
        data = request.get_json()
        input_df = pd.DataFrame(data, index=[0])

        # --- Replicate Preprocessing from Notebook ---

        # 1. Map 'education' text to 'educational-num'
        education_map = {
            'HS-grad': 9, 'Some-college': 10, 'Bachelors': 13, 'Masters': 14, 'Assoc-voc': 11, '11th': 7, 'Assoc-acdm': 12, '10th': 6, '7th-8th': 4, 'Prof-school': 15, '9th': 5, '12th': 8, 'Doctorate': 16, '5th-6th': 3, '1st-4th': 2, 'Preschool': 1
        }
        input_df['educational-num'] = input_df['education'].map(education_map)
        
        # Add 'fnlwgt' which is missing from the form, using a typical value
        input_df['fnlwgt'] = 180000

        # 2. Apply the pre-fitted LabelEncoders to categorical features
        for col, encoder in feature_encoders.items():
            if col in input_df.columns:
                # Handle unseen values by mapping them to the first known class
                input_df[col] = input_df[col].apply(lambda x: x if x in encoder.classes_ else encoder.classes_[0])
                input_df[col] = encoder.transform(input_df[col])

        # 3. Ensure all columns are numeric and in the correct training order
        processed_df = input_df.reindex(columns=training_columns, fill_value=0)
        for col in processed_df.columns:
            processed_df[col] = pd.to_numeric(processed_df[col])

        # 4. Scale the features using the loaded scaler
        scaled_features = scaler.transform(processed_df)

        # 5. Make the prediction
        prediction_encoded = model.predict(scaled_features)
        prediction_proba = model.predict_proba(scaled_features)
        
        # 6. Decode the prediction (e.g., 0 -> '<=50K')
        prediction_text = target_encoder.inverse_transform(prediction_encoded)
        
        return jsonify({
            'prediction': prediction_text[0],
            'probability': prediction_proba[0].tolist(),
            'success': True
        })

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e), 'success': False}), 400

# --- Application Entry Point ---
# Load dependencies on application startup
load_dependencies()

if __name__ == '__main__':
    # The app is already configured, just run it for local debugging
    app.run(debug=True, port=5000)
