FROM continuumio/miniconda3

ENV NERDART_PARENT_DIR="/opt"
ENV NERDART_ENV_DIR="${NERDART_PARENT_DIR}/env"
ENV INSIDE_CONTAINER=true

RUN apt-get update
RUN apt-get install -y uvicorn

WORKDIR $NERDART_PARENT_DIR
ADD app app
ADD nerdart nerdart
COPY .bashrc.nerdart \
     environment.yaml \
     README.md \
     setup.py \
     ./
RUN set -e \
    && conda update -n base -c defaults conda \
    && conda env create --file environment.yaml --prefix "${NERDART_ENV_DIR}" \
    && echo Conda environment successfully created \
    && cat .bashrc.nerdart >> $HOME/.bashrc

WORKDIR /
COPY dockerd-entrypoint.sh \
     LICENSE \
     ./
ENTRYPOINT ["bash", "dockerd-entrypoint.sh"]
