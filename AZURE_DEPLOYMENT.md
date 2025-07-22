# Azure Web App Deployment Configuration

## Project Structure for Azure Deployment
```
Edunet-Salary-Prediction/
├── app.py                 # Main Flask application
├── Procfile              # Process file for startup command
├── requirements.txt      # Python dependencies
├── runtime.txt          # Python version specification
├── models/              # Pre-trained ML models
│   ├── best_gradient_boosting_model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
├── data/                # Dataset
│   └── adult 3.csv
├── templates/           # HTML templates
│   └── index.html
└── static/             # Static files (if any)
```

## Azure Deployment Configuration

### 1. Procfile
```
web: gunicorn app:app
```

### 2. runtime.txt
```
python-3.11
```

### 3. requirements.txt (Optimized for Azure)
```
Flask==3.1.1
gunicorn==23.0.0
pandas==2.3.1
numpy==2.3.1
scikit-learn==1.7.1
joblib==1.5.1
xgboost==3.0.2
Werkzeug==3.1.3
```

## Azure App Service Configuration

### Environment Variables (if needed)
- `SCM_DO_BUILD_DURING_DEPLOYMENT=true`
- `ENABLE_ORYX_BUILD=true`
- `PRE_BUILD_SCRIPT_PATH=` (if custom build script needed)

### Startup Command
The application will automatically use the Procfile command:
```
gunicorn app:app
```

### Port Configuration
Azure will automatically set the PORT environment variable. The app is configured to use this.

## Deployment Steps for Azure

1. **Create Azure Web App**
   - Runtime: Python 3.11
   - Region: Choose appropriate region
   - Pricing tier: F1 (Free) or higher

2. **Configure Deployment**
   - Deployment Center: GitHub
   - Repository: Shaileshukla529/Edunet-Salary-Prediction
   - Branch: main
   - Build provider: App Service build service

3. **Application Settings**
   - Ensure Python version is set to 3.11
   - Enable build automation
   - Set startup file if needed: `gunicorn app:app`

4. **Deploy**
   - Trigger deployment from GitHub
   - Monitor build logs
   - Access the deployed application

## Application Features
- **Machine Learning Model**: Gradient Boosting Classifier
- **Accuracy**: ~87.3%
- **Features**: 12 demographic and financial features
- **Dataset**: Adult Census Income Dataset
- **Prediction**: Whether income is above or below $50,000

## URLs After Deployment
- Application: `https://<your-app-name>.azurewebsites.net`
- Health Check: `https://<your-app-name>.azurewebsites.net/`
- Prediction API: `https://<your-app-name>.azurewebsites.net/predict`
