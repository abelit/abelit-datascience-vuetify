# --------------------------
# Docker file
# --------------------------
FROM python:3.6

MAINTAINER Abelit <ychenid@live.com>


# Set TimeZone
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install  Python and Flask requirement
COPY ../backend/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn 
RUN pip install --timeout 600 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn -r /tmp/requirements.txt

# Create webapp directory
RUN mkdir -p /data/webapp
COPY ../backend /data/webapp/
WORKDIR /data/webapp

# ENV PORT 5000
EXPOSE 5000

CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", ":5000", "manage:app"]