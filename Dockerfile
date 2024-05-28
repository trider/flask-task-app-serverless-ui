FROM python:3.12
COPY requirements.txt ./
RUN pip install -r requirements.txt
ADD app.py .
COPY . .
EXPOSE 5001
CMD ["python", "./app.py"]
