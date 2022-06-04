FROM python:3.10

WORKDIR /app

COPY . /app

# RUN pip --no-cache-dir install -r requirements.txt
# RUN pip3 install flask 
# CMD ["python3","src/app.py"]

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "./src/app.py"]