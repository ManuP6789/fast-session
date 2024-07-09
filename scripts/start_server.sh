#!/bin/bash
# Start Flask server
cd /var/www/backend
nohup python app.py &

# Restart Nginx to serve the frontend
systemctl restart nginx
