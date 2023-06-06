import jupyter_core

import jupyter_x11_app_proxy

c.ServerProxy.servers = jupyter_x11_app_proxy.setup_apps(
    [
        {
            "name": "Xeyes",
            "app": "xeyes",
            "icon": f"{jupyter_core.paths.jupyter_config_dir()}/X11.svg",
        },
        {
            "name": "Oclock",
            "app": "oclock",
            "icon": f"{jupyter_core.paths.jupyter_config_dir()}/X11.svg",
            "new_tab": True,
        },
        {
            "name": "Xcalc",
            "app": "xcalc",
            "icon": f"{jupyter_core.paths.jupyter_config_dir()}/X11.svg",
        },
        {
            "name": "XLogo",
            "app": "xlogo",
            "icon": f"{jupyter_core.paths.jupyter_config_dir()}/X11.svg",
        },
        {
            "name": "Xedit",
            "app": "xedit",
            "icon": f"{jupyter_core.paths.jupyter_config_dir()}/X11.svg",
        },
        {
            "name": "Xcalc2",
            "app": "xcalc",
            "icon": f"{jupyter_core.paths.jupyter_config_dir()}/X11.svg",
        },
    ]
)
