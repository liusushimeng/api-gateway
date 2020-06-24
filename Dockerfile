FROM artifact-registry.mercedes-benz.com.cn/baselibrary/python:3.6-alpine

ADD . /app
WORKDIR /app
USER root

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN apk add libressl-dev gcc libffi-dev musl-dev
USER 1000

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --user

ENV PATH "$PATH:/app/.local/bin/"
EXPOSE 9000

CMD chmod -R 777 bin/
ENTRYPOINT ["sh", "bin/Entrypoint.sh"]
