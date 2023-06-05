# Jupyter X11 APP Proxy

Run your X11 applications on Jupyter.

This is heavily inspired by [Jupyter Remote Desktop Proxy](Jupyter Remote Desktop Proxy).

## How it works

Jupyter X11 App Proxy is using [Jupyter Server Proxy](https://jupyter-server-proxy.readthedocs.io/) to run X11 applications.
It runs a VNC server, Xorg server and Matchbox Window manager for each configured applications.

## Usage

The easiest way is to use Docker image embedding dependencies listed above as your base image.

- on peut mettre plusieurs applications ;
- on peut mettre une icone/un nom ;
- on peut choisir un nouvel onglet notebook ou navigateur ;
- meilleure gestion de la fenêtre (plein écran/redimensionnement) ;
- l'application se relance en cas de plantage.
