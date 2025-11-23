!/bin/bash

echo "CPU Usage:"
top -bn1 | head -5

echo ""
echo "Memory Usage:"
free -h
