import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'<iframe[^>]*src="([^"]+)"', s)
    if match:
        url = match.group(1)
        vid = re.search(r"^https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)$", url)
        if vid:
            return f"https://youtu.be/{vid.group(1)}"
    return None

if __name__ == "__main__":
    main()
