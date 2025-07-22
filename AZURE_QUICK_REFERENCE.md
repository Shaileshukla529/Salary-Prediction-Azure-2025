# Azure Deployment Quick Reference Card

## 🚀 Essential Commands & Settings

### Resource Creation
```bash
# Resource Group
Name: rg-salary-prediction-app
Region: East US 2

# App Service
Name: salary-prediction-app-[unique]
Runtime: Python 3.11
OS: Linux
Plan: F1 (Free) or B1 (Basic)
```

### GitHub Configuration
```
Repository: Shaileshukla529/Salary-prediction-Edunet
Branch: main
Build Provider: App Service build service
```

### Required Files in Repository
- ✅ `Procfile`: `web: gunicorn app:app`
- ✅ `runtime.txt`: `python-3.11`
- ✅ `requirements.txt`: Essential packages only
- ✅ `app.py`: Main Flask application
- ✅ `models/`: ML model files
- ✅ `templates/`: HTML templates

### Application Settings
```
SCM_DO_BUILD_DURING_DEPLOYMENT = true
ENABLE_ORYX_BUILD = true
WEBSITE_RUN_FROM_PACKAGE = 1
```

### URLs After Deployment
```
Application: https://[app-name].azurewebsites.net
Health Check: https://[app-name].azurewebsites.net/
API Endpoint: https://[app-name].azurewebsites.net/predict
```

## ⚡ Quick Deployment Steps

1. **Create Resource Group** → Resource groups → Create
2. **Create App Service** → App Services → Create → Configure basic settings
3. **Configure Deployment** → Deployment Center → GitHub → Configure
4. **Monitor Build** → Deployment Center → Logs
5. **Test Application** → Browse to URL → Test functionality

## 🔧 Standard Azure Conventions Used

- **Naming Convention**: `rg-[project]-[environment]` for resource groups
- **Location Consistency**: Same region for all resources
- **Security**: HTTPS enabled by default
- **Monitoring**: Application Insights integration
- **Scaling**: Auto-scaling capable configuration
- **CI/CD**: GitHub Actions integration
- **Runtime**: Latest stable Python version (3.11)
- **Server**: Gunicorn WSGI server for production

## 🚨 Critical Success Factors

- ✅ Python 3.11 compatibility
- ✅ Minimal requirements.txt (avoid conflicts)
- ✅ Correct Procfile format
- ✅ Model files included in repository
- ✅ Flask app production configuration
- ✅ No debug mode in production
- ✅ Proper error handling
