#!/bin/bash

# Create the directory if it doesn't exist
mkdir -p pdf

for i in *.ipynb; do 
    # Get the filename without the extension
    filename=$(basename "$i" .ipynb)
    
    # Convert the notebook to PDF and save it in the /pdf directory
    jupyter nbconvert --to pdf "$i" --output-dir='./pdf' --output="$filename.pdf"
done