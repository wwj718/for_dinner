#!/usr/bin/env python
# encoding: utf-8

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler,FileSystemEventHandler

from send_emails import send_mail
import commands
from os import system
from config import watchdir,watch_file_type,remotedir

def notice2download(sub=u"下载视频",content=u"请登录百度网盘"):
    send_mail(sub,content)

def upload_watch_file(file):
    pass

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if (event.src_path).endswith(watch_file_type):
            print event.src_path
            #上传到云盘
            mycommands = "bypy.py upload " + event.src_path + " " + remotedir
            output = commands.getoutput(mycommands)
            print output
            #发送邮件
            content = u"新建文件："+event.src_path
            notice2download(content=content)
            time.sleep(60*10) #十分钟后关机
            system('halt')

    def on_modified(self, event):
        if (event.src_path).endswith(watch_file_type):     #监控指定文件内容、权限等变化
            print "log file %s changed!" % event.src_path

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else watchdir
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

