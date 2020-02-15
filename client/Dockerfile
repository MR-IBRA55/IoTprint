# User an existing docker image as base
FROM python
# Specify work dir path inside the container
WORKDIR /usr/app
# Download and install depndancies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy project files inside container workdir directory
COPY . .
# Tell the image what to do when starts as a container
CMD ["gunicorn", "-b", "0.0.0.0:3000", "-w", "2", "run:app"]
