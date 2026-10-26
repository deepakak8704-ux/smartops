import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="SmartOps Dashboard",
    page_icon="🛠️",
    layout="wide"
)


st.title("🛠️ SmartOps")
st.subheader(
    "Intelligent IT Operations & Service Management Platform"
)


def get_data(endpoint):

    try:

        response = requests.get(
            f"{API_URL}{endpoint}",
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        st.error(
            f"Unable to connect to SmartOps API: {error}"
        )

        return []


# -------------------------------------------------
# EMPLOYEE DATA
# -------------------------------------------------

employees = get_data(
    "/employees/"
)

employee_count = len(employees)


# -------------------------------------------------
# LOG DATA
# -------------------------------------------------

logs = get_data(
    "/logs/"
)

error_logs = [
    log
    for log in logs
    if log["level"] == "ERROR"
]


warning_logs = [
    log
    for log in logs
    if log["level"] == "WARNING"
]


# -------------------------------------------------
# API MONITORING DATA
# -------------------------------------------------

api_results = get_data(
    "/monitor/"
)

successful_apis = [
    result
    for result in api_results
    if result["status"] == "SUCCESS"
]

failed_apis = [
    result
    for result in api_results
    if result["status"] == "FAILED"
]


# -------------------------------------------------
# SERVICE REQUEST DATA
# -------------------------------------------------

service_requests = get_data(
    "/service-requests/"
)


open_requests = [
    request
    for request in service_requests
    if request["status"] == "Open"
]


in_progress_requests = [
    request
    for request in service_requests
    if request["status"] == "In Progress"
]


resolved_requests = [
    request
    for request in service_requests
    if request["status"] == "Resolved"
]


# -------------------------------------------------
# DASHBOARD METRICS
# -------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "👥 Employees",
        employee_count
    )


with col2:

    st.metric(
        "🔴 Errors",
        len(error_logs)
    )


with col3:

    st.metric(
        "🌐 API Success",
        len(successful_apis)
    )


with col4:

    st.metric(
        "🎫 Open Requests",
        len(open_requests)
    )


with col5:

    st.metric(
        "✅ Resolved Requests",
        len(resolved_requests)
    )


# -------------------------------------------------
# APPLICATION ERRORS
# -------------------------------------------------

st.header(
    "🔴 Recent Application Errors"
)


if error_logs:

    for error in error_logs[:10]:

        st.error(
            f"{error['timestamp']} — "
            f"{error['message']}"
        )

else:

    st.success(
        "No application errors found."
    )


# -------------------------------------------------
# API MONITORING
# -------------------------------------------------

st.header(
    "🌐 API Monitoring Status"
)


if api_results:

    for result in api_results[:10]:

        if result["status"] == "SUCCESS":

            st.success(
                f"✅ {result['endpoint']} | "
                f"HTTP {result['status_code']} | "
                f"Response: {result['response_time']}"
            )

        else:

            st.error(
                f"❌ {result['endpoint']} | "
                f"HTTP {result['status_code']} | "
                f"Error: {result['error_message']} | "
                f"Response: {result['response_time']}"
            )

else:

    st.info(
        "No API monitoring results found."
    )

# -------------------------------------------------
# SERVICE REQUESTS
# -------------------------------------------------

st.header(
    "🎫 Service Requests"
)


if service_requests:

    status_filter = st.selectbox(
        "Filter by status",
        [
            "All",
            "Open",
            "In Progress",
            "Resolved",
            "Closed"
        ]
    )


    filtered_requests = service_requests


    if status_filter != "All":

        filtered_requests = [
            request
            for request in service_requests
            if request["status"] == status_filter
        ]


    for request in filtered_requests:

        with st.expander(
            f"#{request['id']} — "
            f"{request['title']}"
        ):

            st.write(
                f"**Description:** "
                f"{request['description']}"
            )

            st.write(
                f"**Priority:** "
                f"{request['priority']}"
            )

            st.write(
                f"**Status:** "
                f"{request['status']}"
            )

            st.write(
                f"**Assigned Employee:** "
                f"{request['assigned_employee_id']}"
            )

            st.write(
                f"**Source:** "
                f"{request['source']}"
            )

            st.write(
                f"**Related Error:** "
                f"{request['related_error']}"
            )

else:

    st.info(
        "No service requests found."
    )


# -------------------------------------------------
# WARNING SUMMARY
# -------------------------------------------------

st.header(
    "⚠️ Warning Summary"
)


st.metric(
    "Warning Log Entries",
    len(warning_logs)
)


st.divider()


st.caption(
    "SmartOps — Python Development Internship "
    "Capstone Project"
)