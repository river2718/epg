#-*- coding:utf-8 -*-
import time,re,os,unicodedata
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','epg.settings')
django.setup()
from web.models import Crawl_log
from web.models import Channel,Epg
##log(msg,level=1),日志写入数据库并打印
##gen_trans_m3u(上传文件目录，下载文件目录） 将已经上传的文件与频道名称匹配并保存
def log(msg,level = 1): #写日志 1正常 2错误
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) + ' '
    m = t + '\t' + str(msg)
    dbinfo = Crawl_log(msg=msg,level = level)
    dbinfo.save()
    print(m)
'''
获取生成HTML时需要的信息，频道列表、EPG统计
'''
def get_html_info(need_date):
    # channels = Channel.get_need_channels(Channel,'all')
    channels = Channel.objects.all()
    channels = [channels,channels.values_list('id')]
    epgs = Epg.get_epgs(channels[1], need_date)
    epg_no = epgs.count()
    return ({
        'epg_no':epg_no,
        'channels':channels[0],
    })


