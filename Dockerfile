FROM python:3.8-slim
RUN mkdir /api
WORKDIR /api
ADD requirements.txt /api
RUN pip3 install -r requirements.txt
ADD . /api
EXPOSE 3000
CMD coverage run --source='.' -m behave ./features && coverage report