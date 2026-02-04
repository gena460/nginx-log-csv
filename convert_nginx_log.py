import argparse
import csv
import re

LOG_PATTERN = re.compile(
    r'(?P<remote_addr>\S+) - (?P<remote_user>\S+) \[(?P<time_local>[^\]]+)\] '
    r'"(?P<request>[^"]*)" (?P<status>\d+) (?P<body_bytes_sent>\d+) "(?P<http_referer>[^"]*)" "(?P<http_user_agent>[^"]*)"'
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    return match.groupdict() if match else None

def main(log_file, csv_file, filter_ip=None, sort_by_time=False, filter_status=None):
    entries = []
    with open(log_file) as lf:
        for line in lf:
            data = parse_log_line(line)
            if not data:
                continue
            if filter_ip and data['remote_addr'] != filter_ip:
                continue
            if filter_status and data['status'] != filter_status:
                continue
            entries.append(data)
    if sort_by_time:
        entries.sort(key=lambda x: x['time_local'])
    with open(csv_file, 'w', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=entries[0].keys())
        writer.writeheader()
        for e in entries:
            writer.writerow(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Nginx log to CSV')
    parser.add_argument('logfile', help='Path to nginx log file')
    parser.add_argument('csvfile', help='Path to output csv file')
    parser.add_argument('--filter-ip', help='Filter by IP address')
    parser.add_argument('--sort', action='store_true', help='Sort by time')
    parser.add_argument('--filter-status', help='Filter by status code')
    args = parser.parse_args()
    main(args.logfile, args.csvfile, args.filter_ip, args.sort, args.filter_status)
