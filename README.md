Nginx Log to CSV Converter
Description
This project parses nginx access logs, converts them to CSV format, and stores the result in Git.
Usage
Run with Docker:
# Build the image
docker build -t nginx-log-csv .
# Run the container
docker run -v $(pwd):/app nginx-log-csv
Run Locally:
# Convert log, filter by status, sort by time
./run.sh nginx.log nginx.csv --filter-status 200 --sort
Script Options
•	--filter-ip <ip>: Filter logs by IP address.
•	--filter-status <code>: Filter by status code (e.g., 404).
•	--sort: Sort results by date/time.
Git Integration
The resulting CSV file is automatically added and committed to the repo.
Requirements
•	Python 3
•	Docker (optional)
Example Output
remote_addr	remote_user	…	status	…
127.0.0.1	-	…	200	…
