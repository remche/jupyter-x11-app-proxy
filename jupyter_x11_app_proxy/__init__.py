import os
import shlex

HERE = os.path.dirname(os.path.abspath(__file__))


def setup_apps(apps):
    config = {}
    for index, app in enumerate(apps):
        config[app.get('name')] = setup_app(
            app.get('app'),
            app.get('icon'),
            new_tab=app.get('new_tab') or False,
            id=index + 1,
        )
    return config


def setup_app(app, icon, new_tab=False, id=1):
    vnc_command = ' '.join(
        shlex.quote(p)
        for p in (
            ['vncserver']
            + [
                '-verbose',
                '-xstartup',
                os.path.join(HERE, 'share/xstartup'),
                '-nohttpd',
                '-name',
                f'{app}-{id}',
                # '-geometry',
                # '1680x1050',
                '-rfbport',
                f'{5900+id}',
                '-SecurityTypes',
                'None',
                '-fg',
                # f':{display}',
            ]
        )
    )
    return {
        'command': [
            'websockify',
            '-v',
            '--web',
            os.path.join(HERE, 'share/web/noVNC'),
            '--heartbeat',
            '30',
            f'{5900+id}',
        ]
        + ['--', '/bin/sh', '-c', f'cd {os.getcwd()} && {vnc_command}'],
        'environment': {'APP': app},
        'port': 5900 + id,
        'timeout': 30,
        'mappath': {'/': '/vnc_lite_patched.html'},
        'launcher_entry': {'icon_path': icon},
        'new_browser_tab': new_tab,
    }
