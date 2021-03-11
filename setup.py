#!/usr/bin/env python3
# coding:utf-8
from setuptools import setup, find_packages
from pkg_resources import Requirement, resource_filename
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements=[
    'flask==1.1.2',
    'pycrypto==2.6.1',
]

setup(
    name='zabbixwechatwork',
    version='1.05',
    author="Traveller",
    author_email="admin@mytlu.cn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Send zabbix alert to wechat user",
    url="https://github.com/TravellerXi/Zabbix-WechatWork",
    #package_dir={'/tmp/Zabbix-WechatWork'},
    package_data={'': ['*.py','*.ini','*.md','*.sh','*.conf','*.wsgi']},#'':['*.ini'],'':['*.md']},
    #packages=find_packages(),
    packages=['zabbix-wechatwork','zabbix-wechatwork/Functions','zabbix-wechatwork/WeChatAPI','zabbix-wechatwork/ZabbixSendMessageScript'],
    #packages=find_packages(),
    #packages=find_packages(where='.',exclude=(),include=('*',)),
    ## 文件依然在该目录下，所以没意义。https://stackoverflow.com/questions/10456279/python-setuptools-how-to-include-a-config-file-for-distribution-into-prefix-e
    # data_files=[('etc/zabbixwechatwork',['Zabbix-WechatWork/Configure.ini'])],
    install_requires=requirements,
    scripts=['zabbix-wechatwork/zabbix-wechatwork'],
    #include_package_data=True,
    #zip_safe=False,
    python_requires=">=3",
)
