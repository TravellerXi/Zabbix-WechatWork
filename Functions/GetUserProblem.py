#!/usr/bin/env python3
# coding:utf-8
# 未来开发项。在目前版本不起任何作用。

'''
请预先通过企业微信api创建菜单，创建内容：
{
  "button": [{
    "type": "click",
    "name": "故障列表",
    "key": "myproblem"
  }]
}
'''
# TODO: 获取微信当前用户在zabbix里的所有问题
from pyzabbix import ZabbixAPI
import warnings
from Functions.CorpInfo import *


WeChatUserName='UserNameHere'
SurName=WeChatUserName[:1]
Name=WeChatUserName[1:]
url = URL  # 这里的URL在python2.CorpInfo 定义
zapi = ZabbixAPI(server=url)
warnings.filterwarnings('ignore')
zapi.login(user=UserName, password=PassWord)
UserInfo = zapi.user.get(search={'SurName':[SurName],'name':[Name]})
#search={'host':[HostName]}
UserID=UserInfo[0]['userid']
UserGroupInfo=zapi.usergroup.get(userids=UserID,output='extend')
# TODO :在测试如何通过用户组拿到hostgroupid
print(UserGroupInfo)
