# Nginx Log to CSV Converter

## Description

This project parses nginx access logs, converts them to CSV format, and stores the result in Git.


## Features

•	Parse nginx access log: IP, datetime, method, url, protocol, status, size, referer, user_agent
•	Output CSV for analytics or integration
•	Optionally filter by IP or HTTP status, or sort by datetime
•	Commit the CSV export automatically to your Git repo
•	Docker support for portable packaging

## Usage

# Build and run in Docker

# With Docker
docker build -t nginx-log-csv .
# Run the container
docker run --rm -v $(pwd):/app nginx-log-csv

# Or, run locally:

```bash
chmod +x run.sh
./run.sh nginx.log nginx.csv –sort
```


# Script Options

•	--filter-ip <ip>: Filter logs by IP address.
•	--filter-status <code>: Filter by status code (e.g., 404).
•	--sort: Sort results by date/time.


# Output CSV Columns

remote_addr | datetime | method | url | protocol | status | size | referer | user_agent |

# Requirements

•	Python 3
•	Git (for auto-commit)
•	Docker (optional)


# Git Integration

Initialize your Git repository (if needed)
git init
The resulting CSV file is automatically added and committed to the repo.


## License

Apache License 2.0
