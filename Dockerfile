FROM ubuntu:latest

# Timezoneを設定
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# Install Python PIP
RUN apt update -y && apt install -y python3-venv git libopencv-dev\
&& apt clean && rm -rf /var/lib/apt/lists/*

# 仮想環境を作成
RUN python3 -m venv /opt/venv

# 作業場所
WORKDIR /root/work/

# ローカルのディレクトリをコンテナにコピー
COPY ./ /root/work/SynthDoG

# synthtigerのインストール
RUN git clone https://github.com/takmin/synthtiger
RUN /opt/venv/bin/pip install --no-cache-dir ./synthtiger

# 仮想環境をパスに追加
ENV PATH="/opt/venv/bin:$PATH"

CMD ["/bin/bash"]
