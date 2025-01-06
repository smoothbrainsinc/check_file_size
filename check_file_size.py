import requests
from url import urls  # Importing the list of URLs

def check_file_size(url):
    try:
        response = requests.head(url)
        
        if response.status_code == 200:
            content_length = response.headers.get('Content-Length')
            content_type = response.headers.get('Content-Type')
            
            if content_length is not None:
                file_size = int(content_length)  # Size in bytes
                print(f"URL: {url} - File size: {file_size / (1024 * 1024):.2f} MB")
            else:
                print(f"URL: {url} - Content-Length header not found.")
            
            print(f"Content type: {content_type}\n")
        else:
            print(f"URL: {url} - Failed to retrieve headers. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred for URL {url}: {e}")

if __name__ == "__main__":
    for url in urls:
        check_file_size(url)

