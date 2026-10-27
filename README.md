# SmartOps — Intelligent IT Operations & Service Management Platform

SmartOps is a Python-based IT Operations and Service Management platform developed as the final capstone project for the SkyCurve Technologies Python Development Internship.

The platform integrates employee data management, application log analysis, external API monitoring, and service request management into a centralized FastAPI backend with a Streamlit dashboard.

---

## Project Objective

The objective of SmartOps is to provide a centralized system for identifying operational issues, monitoring application and API health, managing employees, and creating and tracking IT service requests.

The project integrates concepts and components developed during the previous internship assignments.

---

## Key Features

### 1. Employee Data Management

- Import employee records from CSV and JSON files
- Validate employee information
- Detect duplicate employee IDs
- Identify invalid or missing employee information
- Search employees using keywords
- Retrieve individual employee details
- Store employee records in SQLite
_______________________________________________________________________________________________

### 2. Application Log Analysis

- Process application log files
- Identify INFO, WARNING, and ERROR entries
- Detect malformed log entries
- Count log entries by severity
- Identify frequently occurring error messages
- Store analyzed log entries in the database
- Retrieve stored log information through the API
_______________________________________________________________________________________________

### 3. API Monitoring

- Monitor external REST APIs
- Record API request status
- Measure response time
- Handle failed API requests
- Handle HTTP errors
- Identify external API failures
- Create service requests for API failures
_______________________________________________________________________________________________

### 4. Service Request Management

- Create service requests
- Retrieve service requests
- Retrieve individual service requests
- Update service requests
- Assign requests to employees
- Track priority
- Track request status
- Associate requests with application errors
- Associate requests with API failures
- Store service requests in SQLite
_______________________________________________________________________________________________

### 5. Streamlit Dashboard

The SmartOps dashboard provides a centralized visual interface for operational information.

The dashboard displays:

- Employee statistics
- Application error information
- Warning log information
- API monitoring results
- Open service requests
- In-progress service requests
- Resolved service requests
_______________________________________________________________________________________________

### 6. Testing and Reliability

The project includes automated tests using pytest and FastAPI TestClient.

Final test result:

```text
12 passed
0 failed
0 warnings
_______________________________________________________________________________________________

### 7. Technology Stack
 _____________________________________________
| Technology     | Purpose                    |
|----------------|----------------------------|
| Python         | Core programming language  |
| FastAPI        | Backend REST API           |
| Pydantic       | Data validation            |
| SQLAlchemy     | Database ORM               |
| SQLite         | Database                   |
| Requests       | External API communication |
| Streamlit      | Dashboard                  |
| pytest         | Automated testing          |
| HTTPX / httpx2 | API testing support        |
| Git            | Version control            |
| GitHub         | Source code hosting        |
|________________|____________________________|

_______________________________________________________________________________________________

### 8. Project Structure

smartops/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── employees/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── service.py
│   │   └── validator.py
│   │
│   ├── logs/
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   ├── routes.py
│   │   └── service.py
│   │
│   ├── monitoring/
│   │   ├── __init__.py
│   │   ├── monitor.py
│   │   ├── routes.py
│   │   └── service.py
│   │
│   └── service_requests/
│       ├── __init__.py
│       ├── routes.py
│       └── service.py
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   ├── application.log
│   ├── employees.csv
│   └── employees.json
│
├── screenshots/
│   ├── 01_fastapi_swagger.png
│   ├── 02_employee_list.png
│   ├── 03_employee_csv_import.png
│   ├── 04_employee_json_import.png
│   ├── 05_log_analysis.png
│   ├── 06_api_monitoring.png
│   ├── 07_create_service_request.png
│   ├── 08_update_service_request.png
│   ├── 09_streamlit_dashboard.png
│   └── 10_all_tests_passed.png
│
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_employees.py
│   ├── test_logs.py
│   ├── test_monitoring.py
│   └── test_service_requests.py
│
├── .gitignore
├── requirements.txt
└── README.md
_______________________________________________________________________________________________

### 9. System Architecture

                    ┌─────────────────────────────┐
                    │      Streamlit Dashboard             │
                    │             UI                       │
                    └──────────────┬──────────────┘
                                       │
                                       ▼
                    ┌─────────────────────────────┐
                    │         FastAPI API                  │
                    └──────────────┬──────────────┘
                                        │
           ┌─────────────────────┼─────────────────────┐
           ▼                           ▼                           ▼
      ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
      │  Employees      │       │ Log Analyzer    │       │ API Monitor     │
      └──────┬──────┘       └──────┬──────┘       └──────┬──────┘
               │                         │                          │
               └───────────────────┼────────────────────┘
                                         ▼
                    ┌─────────────────────────────┐
                    │    Service Request Mgmt              │
                    └──────────────┬──────────────┘
                                        │
                                        ▼
                    ┌─────────────────────────────┐
                    │          SQLite DB                   │
                    └─────────────────────────────┘
_______________________________________________________________________________________________

### 10.Installation


  1. Clone the Repository
         git clone https://github.com/deepakak8704-ux/smartops.git
         cd smartops

  2. Create a Virtual Environment
        Windows:
           python -m venv venv

  3. Activate the Virtual Environment
        PowerShell:
           .\venv\Scripts\Activate.ps1

        If PowerShell execution policy prevents activation:
           Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

        Then:
           .\venv\Scripts\Activate.ps1

        Alternatively, use Command Prompt:
           venv\Scripts\activate

  4. Install Dependencies
        pip install -r requirements.txt
_______________________________________________________________________________________________

### 11. Database

    SmartOps uses SQLite for persistent data storage.

    The database is created automatically when the application starts.

    The main database file is:
               smartops.db

    The database stores information such as:
       - Employees
       - Application log entries
       - Service requests
       - API monitoring/service information

    Database files are intentionally excluded from GitHub using .gitignore.
_______________________________________________________________________________________________

### 12.Run the FastAPI Backend

    From the SmartOps root directory:
       uvicorn app.main:app --reload

    The API will be available at:
       http://127.0.0.1:8000

    FastAPI interactive documentation:
       http://127.0.0.1:8000/docs
_______________________________________________________________________________________________

### 13. Run the Streamlit Dashboard

    Keep the FastAPI server running.

    Open another terminal and activate the virtual environment.

    Then run:
        streamlit run dashboard/dashboard.py

    The Streamlit dashboard will open in the browser.

    The dashboard communicates with the FastAPI backend at:
              http://127.0.0.1:8000
_______________________________________________________________________________________________

### 14. Sample Data

    Sample employee data:
          data/employees.csv
          data/employees.json

    Sample application logs:
          data/application.log

    These files can be used to demonstrate employee import and log analysis functionality.
_______________________________________________________________________________________________

### 15. Employee Management

    The employee module supports:
       - Creating employees
       - Listing employees
       - Searching employees
       - Retrieving employees by employee ID
       - Importing CSV files
       - Importing JSON files
       - Validating employee records
       - Detecting duplicate employee IDs
    Example employee search:
         GET /employees/search?keyword=John
_______________________________________________________________________________________________

### 16. Application Log Analysis

    The log analyzer processes application log files and identifies:
       - INFO
       - WARNING
       - ERROR
    It also detects malformed records and calculates error frequency.

    Example processing flow:

       application.log
             │
             ▼
        Log Parser
             │
             ▼
         Validation
             │
             ▼
    Severity Classification
             │
             ▼
    Error Frequency Analysis
             │
             ▼
       SQLite Database
_______________________________________________________________________________________________

### 17. API Monitoring

    The monitoring module communicates with external REST APIs.

    It records information including:
       - Request status
       - Response time
       - Successful requests
       - Failed requests
       - HTTP failures
       - External API errors

    API failures can also result in service requests being created for operational tracking.
_______________________________________________________________________________________________

### 18. Service Request Management

    Service requests provide centralized tracking of operational issues.

    Example:
    {
        "title": "Database connection failure",
        "description": "Database connection failed multiple times in application logs.",
        "priority": "Critical",
        "assigned_employee_id": "EMP001",
        "source": "Application Log",
        "related_error": "Database connection failed"
    }

    Service requests can be:
        - Created
        - Retrieved
        - Updated
        - Assigned
        - Prioritized
        - Tracked by status

    Example statuses include:
        Open
        In Progress
        Resolved
_______________________________________________________________________________________________

### 19. API Documentation

    FastAPI automatically provides interactive API documentation.

    Open:
        http://127.0.0.1:8000/docs

    Swagger UI can be used to:
        - Test API endpoints
        - Upload employee files
        - Create service requests
        - Update service requests
        - Search employees
        - Retrieve log information
        - View monitoring results
_______________________________________________________________________________________________

### 20. Testing

    SmartOps uses pytest for automated testing.

    Run the complete test suite:
         python -m pytest -v

    Final test result:
         12 passed in 1.22s

    Test areas include:
        - General API
        - Employee Management
        - Application Log Analysis
        - API Monitoring
        - Service Request Management

    Final validation:
        12 passed
        0 failed
        0 warnings
_______________________________________________________________________________________________

### 21. Screenshots

    Screenshots demonstrating the SmartOps application are stored in:
      screenshots/

    The screenshots cover:
      1. FastAPI Swagger documentation
      2. Employee management
      3. Employee CSV import
      4. Employee JSON import
      5. Log analysis
      6. API monitoring
      7. Service request creation
      8. Service request update
      9. Streamlit dashboard
      10. Automated test results

    Running the Complete Application

      Terminal 1 — FastAPI
         .\venv\Scripts\Activate.ps1
         uvicorn app.main:app --reload

      Terminal 2 — Streamlit
          .\venv\Scripts\Activate.ps1
          streamlit run dashboard/dashboard.py

      Terminal 3 — Tests
          .\venv\Scripts\Activate.ps1
          python -m pytest -v
_______________________________________________________________________________________________

### 22. Project Validation

      ____________________________________________
     | Requirement                  |  Status     |
     |------------------------------|-------------|
     | Employee CSV import          | Completed   |
     | Employee JSON import         | Completed   |
     | Employee validation          | Completed   |
     | Duplicate detection          | Completed   |
     | Employee search              | Completed   |
     | Log analysis                 | Completed   |
     | INFO/WARNING/ERROR detection | Completed   |
     | Error frequency analysis     | Completed   |
     | API monitoring               | Completed   |
     | HTTP/API failure handling    | Completed   |
     | Service request creation     | Completed   |
     | Service request retrieval    | Completed   |
     | Service request update       | Completed   |
     | Employee assignment          | Completed   |
     | Priority tracking            | Completed   |
     | Status tracking              | Completed   |
     | SQLite persistence           | Completed   |
     | FastAPI backend              | Completed   |
     | Streamlit dashboard          | Completed   |
     | Automated testing            | Completed   |
     | 12 automated tests           | Passed      |
     |______________________________|_____________|
_______________________________________________________________________________________________

### 23. Future Enhancements

    Possible future improvements include:
       - User authentication and role-based access
       - Advanced dashboard charts
       - Email or notification alerts
       - Scheduled API monitoring
       - Advanced employee filtering
       - Service request comments and history
       - Pagination for large datasets
       - Production database support such as PostgreSQL
       - Docker deployment
       - Cloud deployment
_______________________________________________________________________________________________

### 24. Internship Project

    Project: SmartOps — Intelligent IT Operations & Service Management Platform

    Organization: SkyCurve Technologies

    Internship: Python Development Internship

    Project Type: Final Capstone Project

    Author
       Deepak
       Python Development Intern
_______________________________________________________________________________________________

### 25. License

    This project was developed as part of an internship capstone project for educational and demonstration purposes.