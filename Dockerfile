FROM artifact-registry.mercedes-benz.com.cn/baselibrary/python:3.6-alpine

ADD . /app
WORKDIR /app
USER 1000

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --user

ENV PATH "$PATH:/app/.local/bin/"
ENV PYTHONUNBUFFERED=0
EXPOSE 9000

CMD chmod -R 777 bin/
ENTRYPOINT ["sh", "bin/Entrypoint.sh"]
