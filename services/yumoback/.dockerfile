FROM python:3.12

LABEL author=yumo name=yumoviews version=1.0.0

ENV BASEDIR=/yumoback

WORKDIR $BASEDIR

# 部署项目环境
# 导入工具库，环境索引
COPY lib .
COPY requirements.txt .

# 安装python依赖库
RUN pip install -r requirements.txt
