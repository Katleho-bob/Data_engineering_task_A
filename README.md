# Data_engineering_task_A

---

# Timestamp Difference Calculator

This Python application calculates the time difference between two given timestamps in seconds. It takes multiple test cases, where each test case contains two timestamps. The app computes the absolute difference between the timestamps and returns the result in seconds.

## Features

- Parses timestamps in the format: `Sun 10 May 2015 13:54:36 -0700`
- Supports multiple test cases
- Outputs the absolute difference between two timestamps in seconds

## Requirements

- Python 3.x

## Installation

1. Ensure that Python 3.x is installed on your system.
2. Download or clone the repository to your local machine.
3. Navigate to the directory where the script is located.

## Usage

1. Run the script in your terminal:
   ```bash
   python timestamp_difference.py
   ```

2. Follow the on-screen instructions:
   - First, input the number of test cases (T).
   - Then, for each test case, input two timestamps (t1 and t2) in the following format:
     ```
     Sun 10 May 2015 13:54:36 -0700
     Sun 10 May 2015 13:54:36 -0000
     ```

3. The application will output the absolute difference in seconds for each pair of timestamps.

### Sample Input:
```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```

### Sample Output:
```
25200
88200
```

## Functions

- **`parse_datetime(dt_str)`**: Converts the timestamp string into a `datetime` object.
- **`calculate_difference(t1, t2)`**: Computes the absolute time difference between two timestamp strings in seconds.

