# Salary Prediction Web Application

This project is a web application that predicts whether an individual's annual income is likely to be more or less than $50,000. It uses a machine learning model trained on the Adult Census Income dataset and provides an interactive user interface built with Flask.

## Project Structure

The repository is organized as follows:

```
.
├── data/
│   └── adult 3.csv         # The dataset used for training
├── models/                 # Saved model and preprocessing files
│   ├── best_gradient_boosting_model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
├── templates/
│   └── index.html          # The HTML frontend for the Flask app
├── .venv/                  # Virtual environment folder
├── flask_app.py            # The main Flask application file
├── salary_prediction_model.ipynb # Jupyter Notebook for model training
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Setup and Execution

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv .venv

# Activate it (Windows)
.\.venv\Scripts\activate

# Activate it (macOS/Linux)
source .venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Train the Model

Before you can run the web application, you need to train the machine learning model and generate the necessary model files. Open and run all the cells in the `salary_prediction_model.ipynb` Jupyter Notebook.

This notebook will:
- Preprocess the data from `data/adult 3.csv`.
- Train several classification models.
- Evaluate the models to find the best performer.
- Save the best model (`best_gradient_boosting_model.pkl`), a scaler (`scaler.pkl`), and a label encoder (`label_encoder.pkl`) into the `models/` directory.

**Note:** Ensure you have Jupyter Notebook or JupyterLab installed (`pip install notebook`) to run the `.ipynb` file.

### 5. Run the Flask Web Application

Once the model files are generated, you can start the Flask server.

```bash
python flask_app.py
```

The application will start, and you can access it by opening your web browser and navigating to:

**http://127.0.0.1:5000**

You can now input data into the form to get salary predictions in real-time.

## Model Information

-   **Algorithm**: Gradient Boosting Classifier
-   **Test Accuracy**: Approximately 87.3%
-   **Features**: The model uses 12 demographic and financial features from the census data.
-   **Dataset**: Adult Census Income Dataset from the UCI Machine Learning Repository.
