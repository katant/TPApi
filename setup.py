import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TPApi",
    version="1.0.0",
    author="Katant",
    author_email="katant.savelev@yandex.ru",
    description="Temp-mail.org API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/katant/TPApi",
    packages=["TPApi"],
    install_requires=['requests', 'passgen'],
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
