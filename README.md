# Daily Trend Tracker Bot for Telegram

## Overview
This project is a Python script designed to track daily trending topics on the Persian Wikipedia and share them on a specified Telegram channel. It's an excellent tool for keeping up-to-date with the most discussed topics in the Persian-speaking community.

## Features
- Fetches top trending topics from Wikimedia's pageview statistics.
- Posts the trends to a specified Telegram channel.
- Generates links to Google Trends for an in-depth view.
- Schedules daily updates.

## Requirements
- Python 3
- `requests`, `schedule`, `datetime`, `urllib3`, `jdatetime`, `urllib.parse` libraries.

## Setup
1. Install required Python libraries: `pip install requests schedule urllib3 jdatetime`.
2. Replace `TELEGRAM_TOKEN` and `TELEGRAM_CHANNEL` with your Telegram Bot Token and Channel ID.
3. Run the script to start tracking and posting trends.

## Usage
The script is scheduled to run every day at 07:00 server time. It can be modified to suit different scheduling needs.

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/AbwlfazlMousavi/Wikipedia-Tracker-Bot/issues) if you want to contribute.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Seyed Abolfazl Mousavi - Musavii.ab@gmail.com

