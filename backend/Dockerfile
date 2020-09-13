FROM python:3
USER root
ENV TZ=Asia/Shanghai
WORKDIR /app
COPY . /app
RUN sed -i 's/security.debian.org/mirrors.aliyun.com/' /etc/apt/sources.list
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/' /etc/apt/sources.list
RUN apt-get update && apt-get clean
RUN pip install -r requirements.txt -i "https://pypi.doubanio.com/simple/"
CMD python3 run.py