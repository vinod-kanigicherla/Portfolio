#!/bin/bash

# Variables
URL="http://127.0.0.1:5000/api/timeline_post"
NAME="User1"
EMAIL="user1@example.com"
CONTENT="Example timeline post."
ID=""

# Creating a random timeline post:
create_post() {
    echo "Creating a new timeline post -"
    RESPONSE=$(curl -s -X POST $URL \
    --data "name=$NAME" \
    --data "email=$EMAIL" \
    --data "content=$CONTENT")
    echo "$RESPONSE"
    ID=$(echo $RESPONSE | jq -r '.id')
}

# Get all timeline posts:
get_posts() {
    echo "Getting all timeline posts -"
    RESPONSE=$(curl -s -X GET $URL)
    echo "$RESPONSE"
}

# Delete a timeline post
delete_post() {
    echo "Deleting post with ID: $ID -"
    RESPONSE=$(curl -s -X DELETE $URL/$ID)
    echo "$RESPONSE"
}

# Call Functions
create_post
get_posts
delete_post
get_posts

