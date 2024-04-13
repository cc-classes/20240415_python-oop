FROM ubuntu:22.04

WORKDIR /home/

COPY . .

RUN apt-get update
RUN apt-get install -y \
  curl \
  git \
  gnupg2 \
  jq \
  sudo \
  zsh \
  vim \
  build-essential \
  openssl \
  python3 \
  python3-venv \
  python3-pip \
  python-is-python3

RUN /usr/bin/python3 -m pip install --upgrade pip mypy ruff