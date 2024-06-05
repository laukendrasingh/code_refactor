# Use an official python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /code_refactor_app

# Install python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the application source code into the container
COPY . .

# Expose the streamlit port
EXPOSE 8501

# Run the streamlit app when the container starts
CMD ["streamlit", "run", "src/main.py"]
