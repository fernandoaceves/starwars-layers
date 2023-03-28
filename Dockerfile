FROM python:3.11.2-alpine

WORKDIR /app

ENV PORT=3000

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 3000

COPY presentation.py .

COPY business.py .

CMD ["python", "/app/presentation.py"]