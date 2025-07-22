# Step-by-Step Azure Deployment Guide

## 🚀 Deploy Salary Prediction App to Azure

### Prerequisites
- Azure account with active subscription
- GitHub repository: `https://github.com/Shaileshukla529/Edunet-Salary-Prediction.git`

### Step 1: Create Azure Web App

1. **Login to Azure Portal**
   - Go to [Azure Portal](https://portal.azure.com)
   - Sign in with your Azure account

2. **Create Web App**
   - Click "Create a resource"
   - Search for "Web App"
   - Click "Create"

3. **Configure Basic Settings**
   ```
   Resource Group: Create new or select existing
   Name: salary-prediction-app (or any unique name)
   Publish: Code
   Runtime stack: Python 3.11
   Operating System: Linux
   Region: East US (or preferred region)
   ```

4. **Select Pricing Plan**
   - Choose F1 (Free) for testing
   - Or B1 (Basic) for production use

### Step 2: Configure Deployment

1. **Go to Deployment Center**
   - After Web App creation, go to your Web App
   - Navigate to "Deployment Center" in the left sidebar

2. **Configure GitHub Integration**
   ```
   Source: GitHub
   Organization: Shaileshukla529
   Repository: Edunet-Salary-Prediction
   Branch: main
   ```

3. **Build Configuration**
   ```
   Build provider: App Service build service
   Runtime stack: Python 3.11
   ```

### Step 3: Application Configuration

1. **Set Application Settings**
   - Go to "Configuration" → "Application settings"
   - Add these if needed:
   ```
   SCM_DO_BUILD_DURING_DEPLOYMENT = true
   ENABLE_ORYX_BUILD = true
   ```

2. **Startup Command** (Optional)
   - Go to "Configuration" → "General settings"
   - Startup command: `gunicorn app:app`
   - (This should auto-detect from Procfile)

### Step 4: Deploy the Application

1. **Trigger Deployment**
   - Save the configuration in Deployment Center
   - Azure will automatically trigger the build

2. **Monitor Build Process**
   - Go to "Deployment Center" → "Logs"
   - Watch the build and deployment progress

### Step 5: Verify Deployment

1. **Check Application Status**
   - Go to "Overview" page of your Web App
   - Click the URL to access your application

2. **Test the Application**
   - Your app should be available at:
     `https://salary-prediction-app.azurewebsites.net`
   - Fill out the form to test predictions

### Deployment Files Ready ✅

The repository now contains all necessary files for Azure deployment:

- ✅ **Procfile**: `web: gunicorn app:app`
- ✅ **runtime.txt**: `python-3.11`
- ✅ **requirements.txt**: Optimized with essential packages
- ✅ **app.py**: Production-ready Flask application
- ✅ **models/**: Pre-trained ML models included
- ✅ **templates/**: HTML interface ready

### Expected Build Output

```bash
# Azure build process will:
1. Detect Python 3.11 from runtime.txt
2. Install packages from requirements.txt
3. Use Procfile for startup command
4. Deploy the application
```

### Troubleshooting

If deployment fails:
1. Check build logs in Deployment Center
2. Verify all files are in the repository
3. Ensure Python version compatibility
4. Check that model files are included

### Application Features After Deployment

- 🤖 **ML Model**: Gradient Boosting Classifier
- 📊 **Accuracy**: ~87.3%
- 🌐 **Web Interface**: User-friendly HTML form
- 📈 **Real-time Predictions**: Instant salary classification
- 🔒 **Production Ready**: Using gunicorn WSGI server

Your salary prediction application is now ready for Azure deployment!
