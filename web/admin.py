from django.contrib import admin
from .models import Channel,Epg,Crawl_log,Channel_list
admin.site.site_header = '我的EPG--频道配置'
admin.site.site_title = "我的EPG"
admin.site.index_title = "后台首页"
# Register your models here.
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'tvg_name', 'sort', 'source', 'ineed', 'last_program_date')
    #list_per_page设置每页显示多少条记录
    list_per_page = 100
    #ordering设置默认排序字段
    ordering = ('id',)
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('id','name',)
    #筛选器
    list_filter =('sort','source','ineed') #过滤器
    search_fields =('tvg_name','name','channel_id' ) #搜索字段
admin.site.register(Channel,ChannelAdmin)

class EpgAdmin(admin.ModelAdmin):
    list_display = ('channel', 'starttime', 'title','program_date','source')
    list_display_links = ('title',)
    date_hierarchy = 'program_date'
    search_fields =('channel__name', 'title') #搜索字段
admin.site.register(Epg,EpgAdmin)
class Crawl_logAdmin(admin.ModelAdmin):
    list_display = ('dt', 'msg', 'level')
admin.site.register(Crawl_log,Crawl_logAdmin)
class Channel_listAdmin(admin.ModelAdmin):
    list_display = ('out_name','out_channel_id','source')
    list_filter =('source',) #过滤器
    list_display_links = ('out_name',)
    search_fields = ('out_name',)
admin.site.register(Channel_list,Channel_listAdmin)
