FROM remche/jupyter-x11-app-proxy:2023-06-06

USER root

RUN apt-get -y -q update \
 && apt-get -y -q upgrade \
 && apt-get -y -q install \
	x11-apps \
 && rm -rf /var/lib/apt/lists/*

USER $NB_USER

COPY --chown=${NB_UID} X11.svg jupyter_server_config.py /tmp/
RUN mv /tmp/jupyter_server_config.py /tmp/X11.svg $(jupyter --conf)
