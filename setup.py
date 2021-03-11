#!/usr/bin/env python3
# coding:utf-8
from setuptools import find_packages, setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='Zabbix-WechatWork',
    version='1.0.4',
    author="Traveller",
    author_email="admin@mytlu.cn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Send zabbix alert to wechat user",
    url="https://github.com/TravellerXi/Zabbix-WechatWork",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask==1.1.2',
        'pycrypto==2.6.1',
    ],
python_requires=">=3",
)