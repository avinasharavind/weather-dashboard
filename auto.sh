#!/bin/bash
MESSAGE="Forecast Update (Automatic): $(date)"
REPO_PATH="/Users/avinasharavind/Documents/Weather_Projects/NWS_Forecast_Page"

git -C "$REPO_PATH" add .
git -C "$REPO_PATH" commit -m "$MESSAGE"
