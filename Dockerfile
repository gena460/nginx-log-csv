FROM python:3.11-slim
WORKDIR /app
COPY convert_nginx_log.py run.sh nginx.log ./
RUN chmod +x run.sh
CMD ["./run.sh", "nginx.log", "nginx.csv"]
