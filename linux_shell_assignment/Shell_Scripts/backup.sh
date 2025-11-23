!/bin/bash

echo "Enter the folder to backup:"
read folder

cp -r "$folder" backup_copy

echo "Backup created with name: backup_copy"
