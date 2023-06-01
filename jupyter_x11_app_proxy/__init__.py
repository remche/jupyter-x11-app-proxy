import os
import shlex

HERE = os.path.dirname(os.path.abspath(__file__))


def setup_insarviz():
    return setup_app(app="ts_viz", icon='/opt/install/insarviz/icon.svg',
                     display=1)


def setup_insarviz2():
    return setup_app(app="ts_viz", icon='/opt/install/insarviz/icon.svg',
                     display=2)


def setup_app(app, icon, display=1):
    vnc_command = ' '.join(
        shlex.quote(p)
        for p in (
            ['vncserver']
            + [
                '-verbose',
                '-xstartup',
                os.path.join(HERE, 'share/xstartup'),
                '-nohttpd',
                # '-geometry',
                # '1680x1050',
                '-SecurityTypes',
                'None',
                '-fg',
                f':{display}',
            ]
        )
    )
    return {
        'command': [
            'websockify',
            '-v',
            '--web',
            os.path.join(HERE, 'share/web/noVNC-1.2.0'),
            '--heartbeat',
            '30',
            f'{5900+display}',
        ]
        + ['--', '/bin/sh', '-c', f'cd {os.getcwd()} && {vnc_command}'],
        'environment': {'APP': app},
        'port': 5900+display,
        'timeout': 30,
        'mappath': {'/': '/vnc_lite.html'},
        'launcher_entry': {'icon_path': icon},
        'new_browser_tab': False,
    }
