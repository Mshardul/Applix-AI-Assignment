# Applix-AI-Assignment
- Assignment for Applix AI - Time Series Analysis Full stack App

## Objective
- Create a web application that allows users to upload time-series data in Excel or CSV format, parse and clean the data, store it in a database, analyze it, and display interactive charts with time delta selection functionality.

## Requirements

### Frontend:
- Technology Stack: React (or Angular/Vue.js) for the web portal. ✅
- Features: ✅
    - File Upload Component: Allow users to upload Excel/CSV files. ✅
    - Data Table: Display the cleaned data. ✅
    - Interactive Charts: ✅
        - Line chart for trends over time. ✅
        - Other visualizations (e.g., bar or scatter plots) for insights. ✅
    - Time Delta Selection: ✅
        - Dropdown or date-picker range to filter the displayed data by a specific time range. ✅

### Backend:
- Technology Stack: Python (FastAP| / Flask / Django). ✅
- Features: ✅
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
    - API Endpoints: ✅
        - Endpoint to upload and process data. ✅
        - Endpoint to fetch cleaned and analyzed data for frontend charts. ✅
        - Endpoint to filter data based on time delta. ✅
### Database:
- Schema: ❌
    - Raw Data Table: ✅
        - Store raw data for reference. ✅
    - Cleaned Data Table: ✅
        - Store cleaned and transformed data. ✅
    - Analysis Results Table: ❌
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
- **Backend:** `FastAPI`, `Pandas`, `PyMongo` (`MongoDB` client for Python), and `Uvicorn`.

## Frontend Development

### Actions
- Update Data
    - Upload the file
    - Send file to Backend API
    - Show upload status - Success / Failed
- Visualize Data
    - Fetch cleaned data from the backend.
    - Show cleaned data as follows
      - Chart Visualization (Line, Bar, Radar)
      - Values Table (Cleaned Value Individually)
      - Statistics Table (`Mean`, `Median`, `Mode`, `Min`, `Max`, `Trend`)
- Filter Data
    - Data can be filtered based on a DateTime picker Modal.
    - The data in all 3 components, updates based on the filter applied.
- Auto-Refresh Data
    - Auto-Refresh Data for the given time frame every 60 seconds.
    - Displays the number of seconds left for next auto-refresh.
    - Refreshes the data in all 3 visualization components (1 chart and 2 tables).

### Components
- Data Filter Component
    - `Start Date Time Picker` and `End Date Time Picker`.
    - Filters data based on the dates provided.
- File Upload Component
    - Accept only .csv/.xlsx files.
    - Enforce 10MB file size limit.
    - Send the file to the backend API.
- Chart Component
    - Use `Chart.js` to create
        - `Line chart`
        - `Bar chart`
        - `Radar fhart`
- Data Table Component
    - `Material UI Table` to display the parsed data.
- Statistics Table Component
    - `Material UI Table` to display the Statistics

## Backend Development

### APIs
- POST /upload
    - Receive a csv/xlsx file.
    - Use Pandas to parse the files.
    - Save files temporarily in local storage.
    - Read, clean, and convert to JSON format.
    - Store raw and cleaned data in Database.
- GET /dummy_data
    - Generates 50 random temperature entries.
    - Store these entries in a csv file.
    - These files can be used to upload as dummy data.
- GET /retrieve
    - Retrieve procesed data from Database.
    - This data is structured for 3 different components
        - Chart Visualization
        - Values Table
        - Statistics Table

### Data Processing
- Clean null/empty values.
- Normalize date formats.

### Auto-Refresh
- Implement WebSockets (or polling) to notify the frontend when new data is available.

## Database Setup

### Database & Collections
- `TemperatureMonitoring`
    - `temperature_data`: stores processed data. each temperature reading as an entry.
    ```
    _id | time | temperature | location | created_at |
    ```
    - `temperature_data_raw`
    ```
    | _id | filename | created_at | uploaded_at | raw_data
    ```

# Hosting
- **Frontend:** `Netlify`
- **Backend:** `Railway.com`
- **Database:** `MongoDB Atlas`

# Run the App
## Over the Internet
- visit: [this link](https://afflix-ai-assessment-by-shardul.netlify.app)
## Locally
- Backend
  ```bash
  uvicorn main:app --host 127.0.0.1 --port 8000 --reload
  ```
- Frontend
  ```bash
  npm start
  ```
