# System Health Monitor

A Python-based system monitoring tool that tracks CPU, RAM, and disk usage.

## Features

- Monitors CPU usage
- Monitors RAM usage
- Monitors disk usage
- Displays warning messages when usage exceeds defined thresholds
- Shows the date and time of each check
- Automatically checks system health every 60 seconds


## Installation

Make sure Python is installed on your computer.

Install the required library:

```bash
python -m pip install psutil
```

## Usage

Run the Python script using the following command:

```bash
python system_monitor.py
```

The program will display CPU, RAM, and disk usage every 60 seconds.

Press Ctrl + C to stop the monitoring process.