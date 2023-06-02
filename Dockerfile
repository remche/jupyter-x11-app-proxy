FROM docker.io/jupyter/base-notebook:2023-05-08
LABEL maintainer="OSUG"

RUN jupyter labextension disable "@jupyterlab/apputils-extension:announcements"

USER root

RUN apt-get -y -q update \
 && apt-get -y -q upgrade \
 && apt-get -y -q install \
	git \
	matchbox-window-manager \
	mesa-utils \
	xorg \
# chown $HOME to workaround that the xorg installation creates a
# /home/jovyan/.cache directory owned by root
 && chown -R $NB_UID:$NB_GID $HOME

ARG VIRTUALGL_VERSION=3.1
RUN wget -q "https://sourceforge.net/projects/virtualgl/files/${VIRTUALGL_VERSION}/virtualgl_${VIRTUALGL_VERSION}_amd64.deb/download" -O virtualgl.deb \
 && apt-get install -y -q ./virtualgl.deb \
 && rm ./virtualgl.deb \
 && ln -s /opt/VirtualGL/bin/* /usr/local/bin/
RUN /opt/VirtualGL/bin/vglserver_config +glx +egl +s +f +t

ARG TURBOVNC_VERSION=2.2.6
RUN wget -q "https://sourceforge.net/projects/turbovnc/files/${TURBOVNC_VERSION}/turbovnc_${TURBOVNC_VERSION}_amd64.deb/download" -O turbovnc.deb \
 && apt-get install -y -q ./turbovnc.deb \
    # remove light-locker to prevent screen lock
 && apt-get remove -y -q light-locker \
 && rm ./turbovnc.deb \
 && ln -s /opt/TurboVNC/bin/* /usr/local/bin/

RUN rm -rf /var/lib/apt/lists/*

COPY jupyter_x11_app_proxy/ /opt/install/jupyter-x11-app-proxy/jupyter_x11_app_proxy/
COPY setup.py MANIFEST.in README.md LICENSE /opt/install/jupyter-x11-app-proxy/

USER $NB_USER
RUN cd /opt/install/jupyter-x11-app-proxy \
 && mamba install -y websockify \
 && pip install -e .
