---
services: app-service\web,app-service
platforms: python
author: cephalin
---

# Django and PostgreSQL sample for Azure App Service

This is a sample application that you can use to follow along with the tutorial at 
[Build a Python and PostgreSQL web app in Azure App Service](https://docs.microsoft.com/azure/app-service/containers/tutorial-python-postgresql-app). 

The sample is a simple Python Django application that connects to a PostgreSQL database.

The database connection information is specified via environment variables `DBHOST`, `DBPASS`, `DBUSER`, and `DBNAME`. This app always uses the default PostgreSQL port.

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.