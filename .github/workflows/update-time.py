from datetime import datetime
import pytz
import re

def get_formatted_time(timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    return current_time.strftime("%H:%M:%S %Z")

def update_readme():
    with open('README.md', 'r') as file:
        content = file.read()

    # Update UTC time
    utc_time = datetime.now(pytz.UTC)
    new_time = utc_time.strftime("%Y-%m-%d %H:%M:%S")
    content = re.sub(
        r'Current Time: `.*`',
        f'Current Time: `{new_time} UTC`',
        content
    )

    # Update time zones in ASCII art
    times = {
        'EST': get_formatted_time('America/New_York'),
        'GMT': get_formatted_time('Europe/London'),
        'JST': get_formatted_time('Asia/Tokyo'),
        'AEDT': get_formatted_time('Australia/Sydney'),
        'BST': get_formatted_time('Asia/Dhaka')
    }

    for tz, time in times.items():
        content = re.sub(
            f'{tz}.*\n',
            f'{tz}        │ {time}  │\n',
            content
        )

    with open('README.md', 'w') as file:
        file.write(content)

if __name__ == "__main__":
    update_readme()
