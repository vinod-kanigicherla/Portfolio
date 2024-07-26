#!/bin/bash

# Change to the project directory
cd /path/to/your/project

# Fetch the latest changes from the main branch
git fetch && git reset origin/main --hard

# Spin down the containers 
docker-compose -f docker-compose.prod.yml down

# Build and spin up the containers
docker-compose -f docker-compose.prod.yml up -d --build

