# 💰 Salary Prediction Azure App - FRESH DEPLOYMENT

A production-ready machine learning web application that predicts whether an individual's annual income is above or below $50,000. Built with Flask and optimized for Microsoft Azure App Service deployment.

**🆕 This is a FRESH REPOSITORY setup to avoid any previous deployment conflicts.**

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.1-green.svg)
![Azure](https://img.shields.io/badge/azure-app%20service-blue.svg)
![ML](https://img.shields.io/badge/ML-Gradient%20Boosting-orange.svg)

## 🎯 Application Overview

- **Machine Learning Model**: Gradient Boosting Classifier with 87.3% accuracy
- **Real-time Predictions**: Instant salary predictions through web interface
- **Production Ready**: Optimized for Azure App Service deployment
- **Latest Python**: Built with Python 3.11 for maximum performance
- **Fresh Setup**: New repository to avoid deployment conflicts

---

## 📁 Repository Structure

```
Salary-Prediction-Azure-Fresh/
├── 📄 app.py                    # Main Flask application (production-ready)
├── 📄 Procfile                  # Azure startup: web: gunicorn app:app
├── 📄 requirements.txt          # Python dependencies (Azure optimized)
├── 📄 runtime.txt               # Python 3.11 specification
├── 📁 models/                   # Pre-trained ML models
│   ├── best_gradient_boosting_model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
├── 📁 templates/                # HTML web interface
│   └── index.html
├── 📁 data/                     # Dataset (Adult Census Income)
│   └── adult 3.csv
└── 📄 README.md                 # This file
```

---

## 🆕 FRESH AZURE DEPLOYMENT PROCESS

**Important**: This is a completely new repository setup to avoid any conflicts from previous deployments.

### **NEW REPOSITORY SETUP REQUIRED:**
1. Create a brand new GitHub repository (e.g., `Salary-Prediction-Fresh-2025`)
2. Push this clean codebase to the new repository
3. Use the new repository for Azure deployment

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.11 or higher
- Git

### 1. Clone Repository
```bash
git clone https://github.com/Shaileshukla529/Salary-prediction-Edunet.git
cd Salary-prediction-Edunet
```

### 2. Set Up Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
python app.py
```

### 5. Access Application
Open your browser and navigate to: `http://localhost:5000`

---

## ☁️ Azure Deployment Guide

### 📋 Prerequisites for Azure Deployment
- ✅ **Azure Account**: Active Azure subscription
- ✅ **GitHub Account**: Repository access
- ✅ **Repository URL**: `https://github.com/Shaileshukla529/Salary-prediction-Edunet.git`

---

## 🛠️ Complete Fresh Azure Deployment

### **Step 0: Create New GitHub Repository**
1. Go to [GitHub.com](https://github.com)
2. Click "**New Repository**"
3. Name: `Salary-Prediction-Fresh-2025` 
4. Select "**Public**"
5. Click "**Create repository**"

### **Step 1: Access Azure Portal**
1. Navigate to: `https://portal.azure.com`
2. Sign in with your Azure account
3. Select your subscription

### **Step 2: Create Resource Group**
1. Search "Resource Groups" → Click "**+ Create**"
2. Configure:
   ```
   Resource group name: rg-salary-app-fresh-2025
   Region: East US 2
   ```
3. Click "**Review + create**" → "**Create**"

### **Step 3: Create App Service**
1. Search "App Services" → Click "**+ Create**"
2. **Basic Settings:**
   ```
   Resource Group: rg-salary-app-fresh-2025
   Name: salary-fresh-app-2025
   Publish: Code
   Runtime stack: Python 3.11
   Operating System: Linux
   Region: East US 2
   ```
3. **App Service Plan:**
   ```
   Linux Plan: Create new
   Name: ASP-salary-fresh-2025
   Pricing tier: F1 (Free) or B1 (Basic)
   ```
4. Click "**Review + create**" → "**Create**"

### **Step 4: Setup GitHub Deployment**
1. In your App Service → "**Deployment Center**"
2. **Source Configuration:**
   ```
   Source: GitHub
   Authorize GitHub account
   Organization: [Your GitHub username]
   Repository: Salary-Prediction-Fresh-2025
   Branch: main
   ```
3. **Build Configuration:**
   ```
   Build provider: App Service build service
   Runtime: Python 3.11
   ```
4. Click "**Save**"

### **Step 5: Configure Application Settings**
1. Go to "**Configuration**" → "**Application settings**"
2. Add these settings:
   ```
   SCM_DO_BUILD_DURING_DEPLOYMENT = true
   ENABLE_ORYX_BUILD = true
   WEBSITE_RUN_FROM_PACKAGE = 1
   ```
3. **General Settings:**
   - Stack: Python 3.11
   - Startup Command: (leave empty - uses Procfile)
4. Click "**Save**"

### **Step 6: Monitor Deployment**
1. Go to "**Deployment Center**" → watch build logs
2. Wait for "**Deployment successful**" ✅
3. Check for any errors in build process

### **Step 7: Test Application**
1. Go to "**Overview**" → Copy URL
2. Expected URL: `https://salary-fresh-app-2025.azurewebsites.net`
3. Test the prediction form

---

## 🔧 Production Configuration Files

### `Procfile`
```
web: gunicorn app:app
```

### `runtime.txt`
```
python-3.11
```

### `requirements.txt`
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

---

## 🔍 Troubleshooting Common Issues

### ❌ Issue: Build Failures
**Symptoms**: Deployment fails during package installation
**Solutions**:
- Check requirements.txt formatting
- Verify Python version compatibility  
- Review build logs for specific errors

### ❌ Issue: Application Won't Start
**Symptoms**: "Application Error" or 502 Bad Gateway
**Solutions**:
- Verify Procfile exists: `web: gunicorn app:app`
- Check startup command in Configuration
- Review application logs in Log Stream

### ❌ Issue: Import Errors
**Symptoms**: ModuleNotFoundError
**Solutions**:
- Ensure all packages are in requirements.txt
- Verify model files are uploaded to repository
- Check file paths in application code

### ❌ Issue: Model Loading Errors
**Symptoms**: Model files not found
**Solutions**:
- Verify models/ directory exists in repository
- Check model file names match code references
- Ensure files are not in .gitignore

---

## 📊 Application Technical Details

### Machine Learning Model
- **Algorithm**: Gradient Boosting Classifier
- **Training Accuracy**: ~87.3%
- **Features**: 12 demographic and employment features
- **Dataset**: Adult Census Income Dataset (UCI ML Repository)
- **Target**: Binary classification (>$50K or ≤$50K)

### Input Features
1. Age
2. Work Class
3. Education
4. Education Number
5. Marital Status
6. Occupation
7. Relationship
8. Race
9. Sex
10. Capital Gain
11. Capital Loss
12. Hours per Week
13. Native Country

### Technology Stack
- **Backend**: Flask 3.1.1
- **ML Library**: Scikit-learn 1.7.1
- **Data Processing**: Pandas, NumPy
- **Production Server**: Gunicorn
- **Deployment**: Microsoft Azure App Service
- **Version Control**: Git/GitHub

---

## 🚨 Important Notes for Production

### Security Considerations
- The application runs with debug mode disabled in production
- Model files are loaded once at startup for better performance
- Input validation is implemented for all form fields

### Performance Optimizations
- Pre-trained models are cached in memory
- Minimal dependency requirements for faster deployment
- Optimized for Azure App Service Linux containers

### Scaling Considerations
- Application is stateless and can be scaled horizontally
- Consider upgrading to higher Azure pricing tiers for production loads
- Monitor memory usage with large datasets

---

## 🎯 Expected Deployment Outcome

After successful deployment, your application will be available at:
```
https://salary-prediction-app-2025.azurewebsites.net
```

### ✅ Success Indicators
- [ ] Application builds without errors
- [ ] Web interface loads correctly  
- [ ] Prediction form accepts input
- [ ] Model generates accurate predictions
- [ ] Results display properly
- [ ] No errors in Azure logs

---

## 📞 Support & Resources

### Documentation
- **Flask Documentation**: [flask.palletsprojects.com](https://flask.palletsprojects.com)
- **Azure App Service**: [docs.microsoft.com/azure/app-service](https://docs.microsoft.com/en-us/azure/app-service/)
- **Scikit-learn**: [scikit-learn.org](https://scikit-learn.org)

### Getting Help
- **Issues**: Create an issue in this GitHub repository
- **Azure Support**: Available through Azure Portal
- **Community**: Stack Overflow with tags `azure`, `flask`, `python`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Shailesh Shukla**
- GitHub: [@Shaileshukla529](https://github.com/Shaileshukla529)
- Repository: [Salary-prediction-Edunet](https://github.com/Shaileshukla529/Salary-prediction-Edunet)

---

**🎉 Ready for Azure Deployment!** Follow the step-by-step guide above to deploy your salary prediction application to Microsoft Azure App Service.
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
