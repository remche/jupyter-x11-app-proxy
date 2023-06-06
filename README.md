# Jupyter X11 APP Proxy

Run your X11 applications on Jupyter.

This is heavily inspired by [Jupyter Remote Desktop Proxy](https://github.com/jupyterhub/jupyter-remote-desktop-proxy/).

- Easily configure (name, icon...) several applications ;
- Run on notebook or browser window ;
- Auto-fit window size ;
- Auto restart applications on crash.

## How it works

Jupyter X11 App Proxy is using [Jupyter Server Proxy](https://jupyter-server-proxy.readthedocs.io/) to run X11 applications.
It runs a VNC server, Xorg server and Matchbox Window manager for each configured applications.

## Usage

The easiest way is to use Docker image embedding dependencies listed above as your base image.

```Dockerfile
FROM remche/jupyter-x11-app-proxy
```

You can find a dummy example in the `examples` folder.
