#!/usr/bin/python3
'''
Write a script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
'''
import sys


if __name__ == '__main__':
    file_size, line_count = 0, 0
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status = {k: 0 for k in codes}

    def print_status(stats: dict, fileSize: int) -> None:
        print(f'File size: {file_size}')
        for key, value in sorted(stats.items()):
            if value:
                print(f'{key}: {value}')

    try:
        for line in sys.stdin:
            data = line.split()
            line_count += 1

            try:
                status_code = data[-2]
                if status_code in status:
                    status[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_status(status, file_size)
        print_status(status, file_size)
    except KeyboardInterrupt:
        print_status(status, file_size)
        raise
