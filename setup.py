from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()


setup(
    name="jupyter-x11-app-proxy",
    packages=find_packages(),
    version='1.0.0',
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    description="Run a desktop environments on Jupyter",
    entry_points={
        'jupyter_serverproxy_servers': [
            'InsarViz = jupyter_x11_app_proxy:setup_insarviz',
            'InsarVizTest = jupyter_x11_app_proxy:setup_insarviz2',
        ]
    },
    install_requires=[
        'jupyter-server-proxy>=1.4.0',
    ],
    include_package_data=True,
    keywords=["Interactive", "Desktop", "Jupyter"],
    license="BSD",
    long_description=readme,
    long_description_content_type="text/markdown",
    platforms="Linux",
    python_requires=">=3.6",
    url="https://jupyter.org",
    zip_safe=False,
)
