#!/usr/bin/env python3
# coding:utf-8
from WeChatAPI.WXBizMsgCrypt3 import WXBizMsgCrypt
from Functions.CorpInfo import *
import xml.etree.cElementTree as ET

def HandleCallback(msg_signature,timestamp,nonce,echostr):
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
    ret, sEchoStr = wxcpt.VerifyURL(msg_signature, timestamp, nonce, echostr)
    #if (ret != 0):
    #    return("ERR: VerifyURL ret: " + str(ret))
    if ret !=0:
        return -1
    # 验证URL成功，将sEchoStr返回给企业号
    # HttpUtils.SetResponse(sEchoStr)
    return (sEchoStr.decode())

def DecodeMessage(msg_signature,timestamp,nonce,ReqData):
   wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
   ret, sMsg = wxcpt.DecryptMsg(ReqData, msg_signature, timestamp, nonce)
   if (ret != 0):
      #return ("ERR: DecryptMsg ret: " + str(ret))
      return -1
   # 解密成功，sMsg即为xml格式的明文
   # TODO: 对明文的处理
   # For example:
   # print(sMsg)
   # print(type(sMsg))
   xml_tree = ET.fromstring(sMsg)
   # print(xml_tree)
   # print(type(xml_tree))
   # print xml_tree.find('Content')
   # print(type (xml_tree.find('Content')))
   MsgType = xml_tree.find('MsgType').text
   if MsgType == 'text':
      Content = xml_tree.find('Content')
      FromUserName = xml_tree.find('FromUserName')
      MsgId = xml_tree.find('MsgId')
      ToUserName = xml_tree.find('ToUserName')
      print(Content.text + ',' + FromUserName.text + ',' + MsgType + ',' + ToUserName.text)
      return(Content.text + ',' + FromUserName.text + ',' + MsgType + ',' + ToUserName.text)
   elif MsgType == 'event':
      EventKey = xml_tree.find('EventKey')
      try:
         TaskId = xml_tree.find('TaskId')
         FromUserName = xml_tree.find('FromUserName')
         MsgId = '0'
         ToUserName = xml_tree.find('ToUserName')
         print(EventKey.text + ',' + FromUserName.text + ',' + MsgType + ',' + TaskId.text)
         return(EventKey.text + ',' + FromUserName.text + ',' + MsgType + ',' + TaskId.text)
      except:
         FromUserName = xml_tree.find('FromUserName')
         ToUserName = xml_tree.find('ToUserName')
         print(EventKey.text + ',' + FromUserName.text + ',' + MsgType + ',' + 'myproblem')
         return(EventKey.text + ',' + FromUserName.text + ',' + MsgType + ',' + 'myproblem')