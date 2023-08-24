import socket
import requests
from urllib.parse import urlparse

def extract_ip_and_info(url):
    # Parse the URL to extract the host address
    parsed_url = urlparse(url)
    host = parsed_url.netloc

    try:
        # Convert the host address to an IP address
        ip_address = socket.gethostbyname(host)

        # Send a request to retrieve IP address information
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")

        # Parse the JSON response
        ip_info = response.json()

        return ip_info
    except socket.gaierror:
        return "Unable to find IP address"
    except requests.RequestException:
        return "Unable to fetch IP information"

if __name__ == "__main__":
    url = input("Enter a URL (e.g., https://201580ag.github.io/): ")
    ip_info = extract_ip_and_info(url)

    if isinstance(ip_info, dict):
        print("IP Address Information:")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
    else:
        print(ip_info)
