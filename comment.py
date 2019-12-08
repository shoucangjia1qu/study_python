# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:23:32 2019

@author: ecupl
"""

import os
os.chdir(r"C:\Users\ecupl\Desktop\sina\comment_sina")
from weibo import APIClient
import webbrowser
import urllib
import time
from random import choice

class sina_comments(object):
    def __init__(self):
        self.APP_KEY = '1924965216'                 #自己的APP信息
        self.APP_SECRET = '3257d1f93917cf1e59773003dda5d7e4'    #自己的APPsecret
        self.CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'     #自己定义的回调授权页面
        self.url = 0
        self.client = 0
        self.code = 0                               #code值
        self.token_result = 0                       #Oauth授权后返回的结果        
        self.access_token = 0                       #access_token
        self.expires_in = 0                         #expires_in时间戳
        self.commentsList = []                      #评论列表，直接保存json格式
        self.userList = []                          #评论用户列表，直接保存json格式
        self.since_id = 0                           #上一次开始的微博id
        self.replyList = []                         #回复列表，以weiboID_commentID列表格式保存
        
        
    #1、申请获取Oauth2授权方式的code
    def Get_Oauth2Code(self):
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
        url = client.get_authorize_url()
        webbrowser.open_new(url)
        self.url = url
        self.code = input("复制粘贴code，并按回车确认。")
        self.client = client
        return
    
    #2、获取token值等信息，并设置回client
    def Get_token(self):
        self.token_result = self.client.request_access_token(self.code)
        self.access_token = self.token_result.access_token
        self.expires_in = self.token_result.expires_in
        self.client.set_access_token(self.access_token, self.expires_in)
        return
    
    #3、获取接收到的评论列表
    def Get_CommentsToMe(self, sinceID):
        page = 1
        comments = []
        #按顺序获取最新的评论
        while True:
            print("获取第%d页评论"%page)
            comment_recv = self.client.comments__to_me(since_id = sinceID, count=50, page=page).comments
            if len(comment_recv)==0:
                break
            comments.extend(comment_recv)
            page += 1
        #提取最新评论的所有信息，包括评论、用户、最新的评论id
        if len(comments) != 0:
            users = [cs.user for cs in comments]
            self.commentsList.extend(comments)
            self.userList.extend(users)
            self.since_id = comments[0].id
        return comments
    
    #4、展示收到的评论列表,并收集需要回复的微博id，评论id
    def Show_CommentsToMe(self, comments):
        for idx, c in enumerate(comments):
            print("第%d条评论"%idx)
            #区分是回复微博还是回复评论
            if "reply_comment" in c.keys():
                print("【 类  型 】  他人回复你的评论")
                print("【你的评论】\t\"%s\""%c.reply_comment.text)
            else:
                print("【 类  型 】  他人评论你的微博")
            print("【微博原文】\t\"%s\"\n"%c.status.text)
            GMTstr = c.created_at
            t_struct = time.strptime(GMTstr, "%a %b %d %H:%M:%S "+GMTstr.split()[-2]+" %Y")
            print("【评论时间】\t",time.strftime("%Y-%m-%d %H:%M:%S", t_struct))
            print("【评 论 人】\t",c.user.name)
            print("【评论内容】\t",c.text)
            print("--------------------------------------------------------------\n")
        noReplystr = input("Q1:请输入不需要自动回复的评论编号，并以英文\",\"隔开，按回车结束：")
        #未输入数字
        if noReplystr.strip() == "":
            noReply = []
        else:
            noReply = [int(i.strip()) for i in noReplystr.split(",")]
        weibo_comments = self.Collect_AutoReplyID(comments, noReply)
        return weibo_comments        
    
    #5、收集评论中需要自动回复的微博id和评论id，并以dict形式储存
    def Collect_AutoReplyID(self, comments, noReplyID):
        weibo_comments = dict()
        for idx, c in enumerate(comments):
            #评论index在不自动回复的列表中，则直接跳过，不收集ID
            if idx in noReplyID:
                continue
            weibo_id = c.status.id
            if weibo_id not in weibo_comments.keys():
                weibo_comments[weibo_id] = []
            weibo_comments[weibo_id].append(c.id)
        self.replyList.append(weibo_comments)
        return weibo_comments

    #6、开始自动回复
    def AutoReply(self, IDdict):
        reply_mes = input("Q2:请输入自动回复的内容，并以\"/\"隔开，按回车结束：")
        reply_mes_list = [mes.strip() for mes in reply_mes.split("/")]
        for weiboID, commentID_list in IDdict.items():
            for commentID in commentID_list:
                #随机选取一条既定评论回复用户
                reply_mes_random = choice(reply_mes_list)
                values ={'access_token':self.access_token,
                         'cid':commentID,
                         'id':weiboID,
                         'comment':reply_mes_random}
                url_reply = 'https://api.weibo.com/2/comments/reply.json'
                data = urllib.parse.urlencode(values)
                data =data.encode('UTF-8')
                url =urllib.request.Request(url_reply,data)
                html = urllib.request.urlopen(url)
                print("*回复成功，【回复内容】\t%s"%reply_mes_random)
        print("完成本次自动回复工作！",time.ctime())
        return
    
    #7、获取最新的未回复的since_id，以最晚发出的评论id为since_id
    def Get_sinceID(self):
        comment_send = self.client.comments__by_me().comments
        print("since_id为0，使用最晚发出的评论id：",comment_send[0].id)
        return comment_send[0].id
    
    #8、主程序开始运行
    def comments_train(self):
        flag = True         #是否运行标识
        #先尝试获取token，若授权过期，则需要重新授权
        try:
            while flag:
                if self.since_id == 0:
                    self.since_id = self.Get_sinceID()
                comments = self.Get_CommentsToMe(self.since_id)
                if len(comments) == 0:
                    print("^^^^^^^^^^^^\n暂无更新评论！")
                    print("最新的since_id是：",self.since_id)
                else:
                    print("^^^^^^^^^^^^\n有%d条更新评论！"%len(comments))
                    print("最新的since_id是：",self.since_id)
                    weibo_comments = self.Show_CommentsToMe(comments)
                    self.AutoReply(weibo_comments)
                flag = int(input("是否刷新评论并自动回复？\"是\"输入1，\"否\"输入0"))
        except:
            print("授权过期，重新申请授权！")
            self.Get_Oauth2Code()
            self.Get_token()
            print("获取授权成功！")
            #循环跑最新的评论和回复评论
            while flag:
                if self.since_id == 0:
                    self.since_id = self.Get_sinceID()
                comments = self.Get_CommentsToMe(self.since_id)
                if len(comments) == 0:
                    print("^^^^^^^^^^^^\n暂无更新评论！")
                    print("最新的since_id是：",self.since_id)
                else:
                    print("^^^^^^^^^^^^\n有%d条更新评论！"%len(comments))
                    print("最新的since_id是：",self.since_id)
                    weibo_comments = self.Show_CommentsToMe(comments)
                    self.AutoReply(weibo_comments)
                flag = int(input("是否刷新评论并自动回复？\"是\"输入1，\"否\"输入0\n"))
        return
                
                
sina = sina_comments()
sina.comments_train()

