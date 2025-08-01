FROM node:latest

LABEL author=yumo name=yumoviews version=1.0.0

ENV BASEDIR=/yumoviews

WORKDIR $BASEDIR

COPY ./services/yumoviews .

# 添加系统环境
RUN npm install


