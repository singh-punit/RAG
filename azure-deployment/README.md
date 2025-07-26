# Azure Deployment

Azure deployment configurations, scripts, and documentation for various applications.

## Files

### 📋 Documentation

- `azure-deployment-options.md` - Comprehensive guide to Azure hosting options for MCP servers and web applications

### 🚀 Deployment Scripts

- `azure-deploy.yml` - GitHub Actions workflow for automated Azure deployment
- `startup.sh` - Startup script for Azure App Service
- `web.config` - IIS configuration for Azure App Service

## Deployment Options

### 1. Azure App Service

**Best for:** Production web applications and APIs
**Cost:** ~$13-55/month for basic plans

```bash
# Create App Service
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myApp --runtime "PYTHON|3.9"

# Deploy
az webapp up --name myApp --resource-group myResourceGroup
```

### 2. Azure Functions

**Best for:** Serverless applications and APIs
**Cost:** Pay per execution (very cost-effective)

```bash
# Deploy function app
func azure functionapp publish myFunctionApp
```

### 3. Azure Container Instances

**Best for:** Containerized applications, development/testing
**Cost:** Pay per second of usage

```bash
# Deploy container
az container create --resource-group myResourceGroup --name myContainer --image myregistry/myapp:latest
```

### 4. Azure Static Web Apps

**Best for:** Static websites and SPAs
**Cost:** Free tier available

```bash
# Deploy via GitHub Actions (automatic)
# Or use Azure CLI
az staticwebapp create --name myStaticApp --resource-group myResourceGroup --source https://github.com/user/repo
```

## GitHub Actions Deployment

1. **Setup:** Add `azure-deploy.yml` to `.github/workflows/`
2. **Secrets:** Add `AZURE_WEBAPP_PUBLISH_PROFILE` to GitHub secrets
3. **Deploy:** Push to main branch triggers automatic deployment

## Configuration Files

### `startup.sh`

Configures the application startup for Azure App Service:

- Sets up Gunicorn with optimal settings
- Configures workers and timeout
- Binds to correct port

### `web.config`

IIS configuration for Windows-based Azure App Service:

- Python path configuration
- Request handling setup
- Logging configuration

### `azure-deploy.yml`

GitHub Actions workflow:

- Automated testing
- Dependency installation
- Azure deployment
- Environment configuration

## Best Practices

1. **Environment Variables:** Use Azure App Settings for configuration
2. **Scaling:** Configure auto-scaling based on demand
3. **Monitoring:** Enable Application Insights
4. **Security:** Use managed identities and Key Vault
5. **Cost Optimization:** Choose appropriate pricing tiers

## Troubleshooting

### Common Issues

- **Startup failures:** Check startup.sh permissions and Python path
- **Deployment errors:** Verify publish profile and resource names
- **Performance issues:** Adjust worker count and timeout settings

### Monitoring

- Use Azure Monitor for performance metrics
- Enable diagnostic logging
- Set up alerts for critical issues

## Cost Optimization

- **Development:** Use Azure Container Instances or Functions
- **Production:** Azure App Service with appropriate tier
- **Static sites:** Azure Static Web Apps (free tier)
- **APIs:** Azure Functions for sporadic usage
