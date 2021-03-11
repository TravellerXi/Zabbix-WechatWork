# 打通Zabbix告警与企业微信

>Env : Python3 Flask
主程序以Python3编写，使用Flask框架。
> 系统环境依赖：
> 1. 因为pycrypto，所以需要gcc gcc-c++ python3-devel, centos 下可以通过以下命令解决yum install gcc gcc-c++ python3-devel
> 2. 对外发布采用mod_wsgi，因此需要预先配置mod_wsgi
> 3. 只支持Linux

>使用：
> 安装后，linux下键入“zabbix-wechatwork -h “ 以获取帮助

## 支持：
>1. zabbix消息推送企业微信
>2. 企业微信上ack或者close zabbix问题
>3. 查询系统主机信息
>4. 更多功能开发中

### 系统所有配置信息在Configure.ini

#### 请将文件夹ZabbixSendMessageScript下的WeChatMessage.py和wechat.ini放置到zabbix告警脚本目录，一般为/usr/lib/zabbix/alertscripts/
