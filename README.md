---
services: app-service\web,app-service
platforms: python
author: cephalin
---

# Django and PostgreSQL sample for Azure App Service

This samples is a simple Django app that connects to a PostgreSQL database. The sample is used in the tutorial https://learn.microsoft.com/azure/postgresql/flexible-server/tutorial-django-app-service-postgres](Deploy Django app with App Service and Azure Database for PostgreSQL - Flexible Server).

When deployed to Azure App Service, the database connection information is specified via environment variables `DBHOST`, `DBPASS`, `DBUSER`, and `DBNAME`. This app always uses the default PostgreSQL port. See the tutorials for more information.

## Change log

- 27 Oct 2020: Possible breaking change: removed use of the `DJANGO_ENV` environment variable to switch between local and production settings. The code instead triggers the selection using the `WEBSITE_HOSTNAME` environment variable, which is defined when the code is running inside the the Azure App Service container. See manage.py and azuresite/wsgi.py.

- 12 Oct 2020: **BREAKING CHANGE**: The `DBHOST` environment variable is expected to contain *only* the server name, not the full URL, which is constructed at run time (see azuresite/production.py). Similarly, `DBUSER` is expected to contain only the user name, not username@servername as before, because using the simpler `DBHOST` the code can also construct the correct login form at run time (again in azuresite/production.py), avoiding failures that arise when `DBUSER` lacks the @servername portion.  

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
