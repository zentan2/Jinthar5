# Use an official Python runtime as a parent image.
FROM python:3.10.0
# Create an /app folder inside the container.
RUN mkdir /App
# Set the working directory inside the container to /app.
WORKDIR /App
# Port issues
# Copy files from the current directory into the container's /app directory.
COPY . /App
# Install any needed packages specified in requirements.txt.
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN chmod a+rw app.db
# Make port 8090 available to the world outside this container.
EXPOSE 8090
# Run main.py when the container launches.
ENTRYPOINT ["python", "run.py"]
