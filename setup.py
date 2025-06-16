from distutils.core import setup

setup(
    name="Asterisk",
    py_modules=["asterisk"],
    entry_points={"console_scripts": ["asterisk=asterisk:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool. Asterisk rewrite in Python.",
    author="Jaydatt Khodave",
    author_email="support@itisuniqueofficial.com",
    url="https://github.com/itisuniqueofficial/asterisk",
    keywords=["dos", "http", "asterisk"],
    license="MIT",
)
