FROM python:3.12
RUN pip install flask 
WORKDIR /myapp 
COPY main.py ./main.py 
CMD ["python","./main.py"]