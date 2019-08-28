FROM python:3.6.8
MAINTAINER Your Name "panji@alterra.id"
RUN mkdir -p /DockerEcommerce
COPY . /DockerEcommerce        
RUN pip install -r /DockerEcommerce/requirements.txt
WORKDIR /DockerEcommerce
ENTRYPOINT ["python"]
CMD ["app.py"]

