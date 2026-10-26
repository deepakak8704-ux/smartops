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

### 2. Application Log Analysis

- Process application log files
- Identify INFO, WARNING, and ERROR entries
- Detect malformed log entries
- Count log entries by severity
- Identify frequently occurring error messages
- Store analyzed log entries in the database
- Retrieve stored log information through the API

### 3. API Monitoring

- Monitor external REST APIs
- Record API request status
- Measure response time
- Handle failed API requests
- Handle HTTP errors
- Automatically identify external API failures
- Create service requests for API failures

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

### 6. Testing and Reliability

The project includes automated tests using pytest and FastAPI TestClient.

The final test suite contains:

```text
12 tests passed
0 failed
0 warnings

### 7. Technology Stack

Technology                 Purpose
Python	                Core programming language
FastAPI	                Backend REST API
Pydantic	            Data validation
SQLAlchemy	            Database ORM
SQLite	                Database
Requests	            External API communication
Streamlit	            Dashboard
pytest	                Automated testing
HTTPX/httpx2	        API testing support
Git	                    Version control
GitHub	                Source code hosting


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
├── screenshots/01-2_fastapi_swagger.png       
|     |--01-3_fastapi_swagger.png       
|     |--01_fastapi_swagger.png         
|     |--02_employee_list.png           
|     |--03-2_employee_csv_import.png   
|     |--03_employee_csv_import.png     
|     |--04-2_employee_json_import.png  
|     |--04_employee_json_import.png    
|     |--05-2_log_analysis.png          
|     |--05-3_log_analysis.png          
|     |--05-4_log_analysis.png          
|     |--05_log_analysis.png            
|     |--06-2_api_monitoring.png        
|     |--06_api_monitoring.png          
|     |--07-2_create_service_request.png
|     |--07_create_service_request.png  
|     |--08-2_update_service_request.png
|     |--08_update_service_request.png  
|     |--09-2_streamlit_dashboard.png   
|     |--09-3_streamlit_dashboard.png   
|     |--09_streamlit_dashboard.png     
|     |__10_all_tests_passed.png    
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


### 9. System Architecture

                    ┌──────────────────────────┐
                    │      Streamlit UI        │
                    │       Dashboard          │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │       FastAPI API        │
                    └────────────┬─────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
   Employee Module        Log Analyzer            API Monitor
          │                      │                      │
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Service Request Mgmt   │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │        SQLite DB         │
                    └──────────────────────────┘


### 10. Installation

1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project:
cd smartops

2. Create a virtual environment
Windows:
python -m venv venv

Activate it using PowerShell:
.\venv\Scripts\Activate.ps1

If PowerShell execution policy prevents activation, use:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then:
.\venv\Scripts\Activate.ps1

Alternatively, Command Prompt can be used:
venv\Scripts\activate

Install Dependencies
Install the project dependencies:
pip install -r requirements.txt

Database
SmartOps uses SQLite for persistent data storage.

The database is created automatically when the application starts.

The main database file is:
smartops.db

The database stores information such as:
- Employees
- Application log entries
- Service requests
- API monitoring/service information
The database file is intentionally excluded from GitHub using .gitignore.
Run the FastAPI Backend
From the SmartOps root directory:
uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

FastAPI interactive documentation:
http://127.0.0.1:8000/docs

Run the Streamlit Dashboard
Keep the FastAPI server running.

Open another terminal and activate the virtual environment.

Then run:
streamlit run dashboard/dashboard.py

The Streamlit dashboard will open in the browser.

The dashboard communicates with the FastAPI backend at:
http://127.0.0.1:8000

Sample Data
Sample employee data is available in:
data/employees.csv
data/employees.json

Sample application logs are available in:
data/application.log

These files can be used to demonstrate the employee import and log analysis features.
Employee Management
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

Application Log Analysis
The log analyzer processes application log files and identifies:
INFO
WARNING
ERROR

It also detects malformed records and calculates error frequency.

Example log processing flow:
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

API Monitoring
The monitoring module communicates with external REST APIs.

It records information including:
- Request status
- Response time
- Successful requests
- Failed requests
- HTTP failures
- External API errors
API failures can also result in service requests being created for operational tracking.
Service Request Management
Service requests provide centralized tracking of operational issues.

A service request can contain information such as:
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

API Documentation
FastAPI automatically provides interactive API documentation.

Open:
http://127.0.0.1:8000/docs

The Swagger UI can be used to:
- Test API endpoints
- Upload employee files
- Create service requests
- Update service requests
- Search employees
- Retrieve log information
- View monitoring results
Testing
SmartOps uses pytest for automated testing.

Run the complete test suite:
python -m pytest -v

Final test result:
12 passed in 1.22s

Test areas include:
General API
Employee Management
Application Log Analysis
API Monitoring
Service Request Management

The final test suite completed successfully with:
12 passed
0 failed
0 warnings

Screenshots
Screenshots demonstrating the SmartOps application are stored in:
screenshots/

Recommended screenshots include:
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

Project Validation
The following major components have been implemented and tested:
Requirement	Status
Employee CSV import	✅
Employee JSON import	✅
Employee validation	✅
Duplicate detection	✅
Employee search	✅
Log analysis	✅
INFO/WARNING/ERROR detection	✅
Error frequency analysis	✅
API monitoring	✅
HTTP/API failure handling	✅
Service request creation	✅
Service request retrieval	✅
Service request update	✅
Employee assignment	✅
Priority tracking	✅
Status tracking	✅
SQLite persistence	✅
FastAPI backend	✅
Streamlit dashboard	✅
Automated testing	✅
12 automated tests	✅


Future Enhancements
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
Internship Project
Project: SmartOps — Intelligent IT Operations & Service Management Platform

Organization: SkyCurve Technologies

Internship: Python Development Internship

Project Type: Final Capstone Project
Author
Deepak

Python Development Intern
License
This project was developed as part of an internship capstone project for educational and demonstration purposes.

### Save the file.

Then run:

```powershell
Get-Item README.md