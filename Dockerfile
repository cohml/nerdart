FROM continuumio/miniconda3

ENV NERDART_PARENT_DIR="/opt"
ENV NERDART_ENV_DIR="${NERDART_PARENT_DIR}/env"
ENV INSIDE_CONTAINER=true

COPY nerdart "${NERDART_PARENT_DIR}/nerdart/"

WORKDIR $NERDART_PARENT_DIR
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
