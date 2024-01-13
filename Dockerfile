FROM qgis/qgis:final-3_28_7

ENV QT_QPA_PLATFORM=offscreen

RUN apt -y update && \
    apt -y install awscli && \
    apt -y install htop && \
    apt -y install nano && \
    apt -y install build-essential pkg-config python3-dev

COPY . /app

RUN pip3 --no-cache-dir install --upgrade pip
RUN pip3 install --upgrade -r /app/requirements.txt

WORKDIR /app

CMD ["python3", "-u", "/app/index.py"]
