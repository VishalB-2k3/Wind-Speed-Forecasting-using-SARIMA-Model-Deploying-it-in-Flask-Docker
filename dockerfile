FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 5000 (or any other port your Flask app is running on)
EXPOSE 5000

CMD ["python", "app.py"]
