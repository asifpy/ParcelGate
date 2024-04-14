# Broker Builder

FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_ROOT /app
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1


# RUN echo "deb http://ftp.fr.debian.org/debian bullseye main" > /etc/apt/sources.list \
#   echo "deb http://ftp.fr.debian.org/debian-security bullseye-security main" > /etc/apt/sources.list \
#   echo "deb http://ftp.fr.debian.org/debian bullseye-updates main" > /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y \
  build-essential \
  python-dev \
  libpq-dev \
  zlib1g \
  zlib1g-dev \
  libev4 \
  libev-dev \
  linux-libc-dev \
  libpcre3 \
  libssl-dev \
  libffi-dev \
  libldap2-dev \
  libsasl2-dev \
  wget \
  && rm -rf /var/lib/apt/lists/*

ADD requirements.txt ${APP_ROOT}/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r ${APP_ROOT}/requirements.txt

WORKDIR "${APP_ROOT}"
ADD ./ ${APP_ROOT}


CMD ["./entrypoint.sh"]