# File Size Checker

This script checks the size of files before downloading them.

## Usage

1. **Add URLs**: Open `url.py` and add any URLs that you want to check. For example:

urls = [
"https://example.com/path/to/file1",
"https://example.com/path/to/file2",
]


2. **Run the Script**: Execute the following command in your terminal:

python check_file_size.py


## Requirements

Make sure you have the following installed:
- Python 3.x
- Required packages (install them using pip):

pip install requests


## Notes

- The script sends a HEAD request to each URL to retrieve file size and content type without downloading the files.
- Ensure that your virtual environment is activated before running the script.

## License

This project is open-source. Feel free to modify and use it as needed.

