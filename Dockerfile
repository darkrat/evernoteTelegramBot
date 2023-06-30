FROM python:3.9



COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py /app/

WORKDIR /app

CMD ["python", "bot.py"]