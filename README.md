# Azure_Custom_Tasks

## Step 1: Define the Task in JSON
Create a task.json file that defines the metadata and inputs for your task. This file specifies the task's name, description, inputs (such as URLs and directories), and the script to be executed. For Python, ensure the execution block points to your Python script.

# Step 2

Create a download_and_extract.py script to implement the task's logic. This script uses Python libraries to download a file from a URL and extract it to a specified directory.

# step 3 

## Step 3: Package and Publish the Task
Package your task into a .vsix file using the tfx-cli tool and a manifest file (vss-extension.json). This package includes your task.json and Python script.

# Create the package:

tfx extension create --manifest-globs vss-extension.json


