# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Expose port for Streamlit app
EXPOSE 8503

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
