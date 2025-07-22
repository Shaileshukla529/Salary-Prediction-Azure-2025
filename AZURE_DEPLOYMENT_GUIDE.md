# Step-by-Step Azure App Service Deployment Guide
*Following Microsoft Azure Standard Conventions*

## 📋 Prerequisites

Before starting the deployment, ensure you have:

- ✅ **Azure Account**: Active Azure subscription
- ✅ **Azure CLI**: Installed and configured (optional but recommended)
- ✅ **GitHub Account**: Repository access
- ✅ **Repository URL**: `https://github.com/Shaileshukla529/Salary-prediction-Edunet.git`

## 🚀 Step 1: Access Azure Portal

1. **Navigate to Azure Portal**
   ```
   URL: https://portal.azure.com
   ```

2. **Sign In**
   - Use your Azure account credentials
   - Select the appropriate subscription if you have multiple

3. **Verify Subscription**
   - Check that you have an active subscription
   - Note the subscription name for resource creation

---

## 🏗️ Step 2: Create Resource Group (Best Practice)

1. **Navigate to Resource Groups**
   - Click "Resource groups" in the left sidebar
   - Or search "Resource groups" in the top search bar

2. **Create New Resource Group**
   - Click "+ Create"
   - Fill in the details:
     ```
     Subscription: [Your subscription]
     Resource group name: rg-salary-prediction-app
     Region: East US 2 (or your preferred region)
     ```

3. **Review and Create**
   - Click "Review + create"
   - Click "Create"

---

## 🌐 Step 3: Create Azure App Service

### 3.1 Navigate to App Services
- Click "App Services" in the left sidebar
- Or search "App Services" in the top search bar
- Click "+ Create"

### 3.2 Configure Basic Settings
```
Subscription: [Your subscription]
Resource Group: rg-salary-prediction-app
Name: salary-prediction-app-[unique-suffix]
Publish: Code
Runtime stack: Python 3.11
Operating System: Linux
Region: East US 2 (same as resource group)
```

### 3.3 Configure App Service Plan
**For Development/Testing:**
```
Linux Plan: Create new
Name: ASP-salary-prediction
Sku and size: F1 (Free)
```

**For Production:**
```
Linux Plan: Create new
Name: ASP-salary-prediction-prod
Sku and size: B1 (Basic)
```

### 3.4 Review Configuration
- Review all settings
- Click "Review + create"
- Click "Create"
- Wait for deployment to complete (2-3 minutes)

---

## 🔧 Step 4: Configure Deployment Settings

### 4.1 Access Deployment Center
1. Go to your newly created App Service
2. In the left sidebar, click "Deployment Center"

### 4.2 Configure Source Control
```
Source: GitHub
GitHub account: [Authorize if needed]
Organization: Shaileshukla529
Repository: Salary-prediction-Edunet
Branch: main
```

### 4.3 Configure Build Settings
```
Build provider: App Service build service
Runtime stack: Python 3.11
Runtime version: Python 3.11
```

### 4.4 Save Configuration
- Click "Save" at the top
- Azure will automatically trigger the first deployment

---

## ⚙️ Step 5: Configure Application Settings

### 5.1 Navigate to Configuration
- In your App Service, click "Configuration" in the left sidebar

### 5.2 Add Application Settings (if needed)
Click "New application setting" and add:

```
Name: SCM_DO_BUILD_DURING_DEPLOYMENT
Value: true
```

```
Name: ENABLE_ORYX_BUILD
Value: true
```

```
Name: WEBSITE_RUN_FROM_PACKAGE
Value: 1
```

### 5.3 Configure General Settings
- Click "General settings" tab
- **Startup Command**: Leave empty (will use Procfile)
- **Stack**: Python
- **Major version**: 3.11
- **Minor version**: 3.11

### 5.4 Save Configuration
- Click "Save" at the top
- Click "Continue" when prompted about restart

---

## 📦 Step 6: Monitor Deployment Process

### 6.1 Check Deployment Logs
1. Go to "Deployment Center"
2. Click on the latest deployment entry
3. Monitor the build process in real-time

### 6.2 Expected Build Steps
```
1. Setting up build environment
2. Installing Python 3.11
3. Installing pip dependencies from requirements.txt
4. Collecting static files (if any)
5. Starting application with gunicorn
```

### 6.3 Verify Successful Deployment
Look for these success indicators:
- ✅ "Deployment successful" message
- ✅ Green checkmark next to deployment
- ✅ No error messages in logs

---

## 🧪 Step 7: Test the Application

### 7.1 Get Application URL
- Go to App Service "Overview" page
- Copy the URL (format: `https://salary-prediction-app-[suffix].azurewebsites.net`)

### 7.2 Test Application Access
1. Click the URL or open in new browser tab
2. Verify the salary prediction form loads
3. Fill out a test form with sample data
4. Submit and verify prediction results

### 7.3 Test API Endpoints
- **Home Page**: `GET /`
- **Prediction**: `POST /predict`
- **Health Check**: Browse to root URL

---

## 🔍 Step 8: Configure Monitoring (Optional but Recommended)

### 8.1 Enable Application Insights
1. In App Service, click "Application Insights"
2. Click "Enable Application Insights"
3. Select "Create new resource" or use existing
4. Click "Apply"

### 8.2 Configure Log Stream
1. Click "Log stream" in the left sidebar
2. Enable to see real-time application logs

---

## 🛡️ Step 9: Configure Custom Domain (Optional)

### 9.1 Add Custom Domain
1. Click "Custom domains" in left sidebar
2. Click "Add custom domain"
3. Follow the verification process

### 9.2 Configure SSL Certificate
1. Click "TLS/SSL settings"
2. Choose "Private Key Certificates"
3. Upload certificate or use App Service Managed Certificate

---

## 📊 Step 10: Performance and Scaling Configuration

### 10.1 Configure Scaling
1. Click "Scale up (App Service plan)"
2. Choose appropriate pricing tier based on needs:
   - **F1 (Free)**: Development/Testing
   - **B1 (Basic)**: Small production workloads
   - **S1 (Standard)**: Production with custom domains
   - **P1V2 (Premium)**: High-performance production

### 10.2 Configure Auto-scaling (Premium tiers)
1. Click "Scale out (App Service plan)"
2. Enable auto-scaling based on metrics
3. Set minimum and maximum instances

---

## 🔐 Step 11: Security Configuration

### 11.1 Configure Authentication (Optional)
1. Click "Authentication" in left sidebar
2. Configure identity providers if needed

### 11.2 Configure CORS (if needed)
1. Click "CORS" in left sidebar
2. Add allowed origins for API access

---

## 📝 Step 12: Final Verification Checklist

### ✅ Deployment Verification
- [ ] Application builds successfully
- [ ] No deployment errors in logs
- [ ] Application starts without errors
- [ ] Web interface is accessible
- [ ] Form submission works correctly
- [ ] Predictions are generated successfully
- [ ] Model files are loaded properly

### ✅ Performance Verification
- [ ] Application loads within acceptable time
- [ ] Predictions complete quickly
- [ ] No memory or CPU issues

### ✅ Configuration Verification
- [ ] Correct Python version (3.11)
- [ ] All required packages installed
- [ ] Environment variables set correctly
- [ ] Startup command working (gunicorn)

---

## 🚨 Troubleshooting Common Issues

### Issue 1: Build Failures
**Symptoms**: Deployment fails during package installation
**Solution**: 
1. Check requirements.txt format
2. Verify Python version compatibility
3. Check build logs for specific error messages

### Issue 2: Application Won't Start
**Symptoms**: "Application Error" or 502 Bad Gateway
**Solution**:
1. Check startup command configuration
2. Verify Procfile exists and is correct
3. Check application logs for Python errors

### Issue 3: Module Import Errors
**Symptoms**: ImportError or ModuleNotFoundError
**Solution**:
1. Verify all packages in requirements.txt
2. Check package version compatibility
3. Ensure model files are in repository

### Issue 4: Static Files Not Loading
**Symptoms**: CSS/JS files not found
**Solution**:
1. Configure static files collection
2. Check static file paths in templates

---

## 📋 Post-Deployment Maintenance

### Regular Tasks
1. **Monitor Application Performance**
   - Check Application Insights metrics
   - Review error logs regularly

2. **Update Dependencies**
   - Keep Python packages updated
   - Monitor security vulnerabilities

3. **Backup Strategy**
   - Regular database backups (if applicable)
   - Code repository maintenance

4. **Scaling Monitoring**
   - Monitor CPU and memory usage
   - Adjust scaling settings as needed

---

## 🎯 Success Metrics

Your deployment is successful when:
- ✅ Application URL responds with status 200
- ✅ Salary prediction form works correctly
- ✅ Model makes accurate predictions
- ✅ No errors in application logs
- ✅ Performance meets requirements

## 📞 Support Resources

- **Azure Documentation**: [Azure App Service Python](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python)
- **Azure Support**: Available through Azure Portal
- **Community Support**: Stack Overflow, Azure Forums
- **Repository Issues**: GitHub repository issues section

---

**🎉 Congratulations! Your Salary Prediction Application is now successfully deployed on Azure App Service following Microsoft's standard conventions.**
