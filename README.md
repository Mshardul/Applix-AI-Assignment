# Applix-AI-Assignment
- Assignment for Applix AI - Time Series Analysis Full stack App

## Objective
- Create a web application that allows users to upload time-series data in Excel or CSV format, parse and clean the data, store it in a database, analyze it, and display interactive charts with time delta selection functionality.

## Requirements

### Frontend:
- Technology Stack: React (or Angular/Vue.js) for the web portal. ✅
- Features: ❌
    - File Upload Component: Allow users to upload Excel/CSV files. ✅
    - Data Table: Display the cleaned data. ✅
    - Interactive Charts: ❌
        - Line chart for trends over time. ✅
        - Other visualizations (e.g., bar or scatter plots) for insights. ❌
    - Time Delta Selection: ✅
        - Dropdown or date-picker range to filter the displayed data by a specific time range. ✅

### Backend:
- Technology Stack: Python (FastAP| / Flask / Django). ✅
- Features: ❌
    - Parse and Validate Uploaded Files: ✅
        - Use libraries like pandas (Python) for parsing. ✅
    - Data Cleaning: ✅
        - Remove null anxd empty values. ✅
        - Apply regularization (e.g., standardizing date formats, normalizing numerical values). ✅
    - Store Data in Database: ✅
        - Use PostgreSQL/MySQL for relational data or MongoDB for flexible schema. ✅
    - Perform Analysis: ✅
        - Calculate summary statistics (mean, median, trends). ✅
        - Perform time-based aggregations (daily, weekly, monthly).
    - API Endpoints:
        - Endpoint to upload and process data. ✅
        - Endpoint to fetch cleaned and analyzed data for frontend charts. ✅
        - Endpoint to filter data based on time delta. ✅
### Database:
- Schema: ✅
    - Raw Data Table:
        - Store raw data for reference.
    - Cleaned Data Table: ✅
        - Store cleaned and transformed data. ✅
    - Analysis Results Table: 
        - Store computed metrics like trends, averages, etc.

### Deliverables:
1. Web portal with an intuitive UI for uploading, filtering, and visualizing data. ✅
2. Clean and modular code for frontend and backend. ✅
3. Documentation explaining:
    a. System design and architecture.
    b. Steps to setup and run the application.
4. Screenshots or video demo of the application.

### Additional Mandatory Features:
- Export cleaned or analyzed data to CSV/Excel. ✅
- Use advanced analysis techniques (e.g., clustering, forecasting).
- Deploy the application on a cloud platform like AWS/GCP/Azure or a hosting service like Heroku/Netlify

# Steps to be Taken

## Dependencies
- **Frontend:** `React`, `Material UI`, `Axios`
- **Backend:** `FastAPI`, `Pandas`, `Motor` (`MongoDB` client for Python), and `Uvicorn`.

## Frontend Development

### Flow
- Update Data
    - Upload the file
    - Send file to Backend API
    - Show upload proogress
- Visualize Data
    - Fetch cleaned data from the backend.
    - Show cleaned data in tabular form
    - Visualize data in an Interactive Chart
        - Date-picker to filter data dynamically.
- Export Data
    - Implement a CSV/Excel download button.
    - In case of any filter, just download the Filtered data. Otherwise, download the entire data.

### Components
- File Upload Component
    - Accept only .csv/.xlsx files.
    - Enforce 10MB file size limit.
    - Send the file to the backend API.
- Data Table Component
    - Use `Material UI` Table to display the parsed data.
- Interactive Chart Component
    - Use `Chart.js` to create
        - `Line chart` (trends over time).
        - `Bar chart` or scatter plot for insights.

## Backend Development

### APIs
- POST /upload
    - Receive a csv/xlsx file.
    - Use Pandas to parse the files.
    - Save files temporarily in local storage.
    - Read, clean, and convert to JSON format.
    - Store raw and cleaned data in MongoDB.
- GET /get-data
- GET /get-stats
- POST /get-filtered-data
- GET /export

### Data Processing
- Clean null/empty values.
- Normalize date formats.

### Auto-Refresh
- Implement WebSockets (or polling) to notify the frontend when new data is available.

## Database Setup

## Hosting
- **Frontend:** `Netlify`
- **Backend:** `PythonAnywhere`
- **Database:** `MongoDB Atlas`


