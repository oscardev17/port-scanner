# Port Scanner

A simple Python-based port scanner that detects open ports on a specified IP address. The tool uses multithreading to perform fast scans and provides colored output for better readability.

## Features

- Multithreading with `ThreadPoolExecutor` for faster scanning.
- Uses the `socket` library to attempt connections on specified ports.
- Colorful terminal output with the `pystyle` library.

## Prerequisites

Make sure you have Python installed on your machine. This project requires the following Python packages:

- `pystyle`

You can install the required package using pip:

```bash
pip install pystyle
