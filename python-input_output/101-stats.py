#!/usr/bin/python3
"""Script to compute metrics from stdin"""

import sys


def print_stats(total_size, status_counts):
    """Print the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Main function to process stdin line by line"""
    total_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Try to extract status code and file size
            try:
                if len(parts) >= 2:
                    file_size = int(parts[-1])
                    total_size += file_size

                    status_code = int(parts[-2])
                    if status_code in status_counts:
                        status_counts[status_code] += 1

            except (IndexError, ValueError):
                # Skip malformed lines for status counting
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
