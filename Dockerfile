# Use a smaller base image
FROM python:3.10-alpine

SHELL ["/bin/sh", "-xo", "pipefail", "-c"]

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8

# Install dependencies and wkhtmltopdf
RUN apk --no-cache add \
    ca-certificates \
    curl \
    dirmngr \
    fonts-noto-cjk \
    gnupg \
    libssl1.1 \
    nodejs \
    python3 \
    python3-dev \
    py3-pip \
    py3-magic \
    py3-num2words \
    py3-odf \
    py3-pdfminer \
    py3-phonenumbers \
    py3-pyldap \
    py3-qrcode \
    py3-renderpm \
    py3-setuptools \
    py3-slugify \
    py3-vobject \
    py3-watchdog \
    py3-xlrd \
    py3-xlwt \
    xz && \
    curl -o wkhtmltox.deb -sSL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb && \
    echo 'ea8277df4297afc507c61122f3c349af142f31e5 wkhtmltox.deb' | sha1sum -c - && \
    apk add --no-cache wkhtmltopdf && \
    rm -rf /var/cache/apk/* wkhtmltox.deb

# Install Odoo
ARG ODOO_VERSION=16.0
ARG ODOO_RELEASE=20231010
ARG ODOO_SHA=4a03ec31713364f570a8c49d39a5c1393d609feb

ENV ODOO_VERSION=${ODOO_VERSION}

RUN curl -o odoo.deb -sSL "http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb" && \
    echo "${ODOO_SHA} odoo.deb" | sha1sum -c - && \
    apk --no-cache add ./odoo.deb && \
    rm -rf /var/cache/apk/* odoo.deb

# Expose Odoo services
EXPOSE 8069 8071 8072

