FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    apt-transport-https \
    software-properties-common \
    unixodbc-dev \
    build-essential \
    ca-certificates \
    apt-utils \
    && apt-get remove -y libodbc2 libodbccr2 libodbcinst2 unixodbc-common \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# (somewhere after COPY my_churn_pipeline/pipeline ...)
COPY my_churn_pipeline/pipeline/test_sql_connection.py ./test_sql_connection.py


COPY my_churn_pipeline/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY my_churn_pipeline/pipeline ./pipeline

CMD ["python", "pipeline/main.py"]
