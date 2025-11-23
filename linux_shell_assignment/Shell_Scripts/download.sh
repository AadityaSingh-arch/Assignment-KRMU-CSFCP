!/bin/bash

echo "Enter the URL to download:"
read url

wget "$url"

echo "Download completed."
