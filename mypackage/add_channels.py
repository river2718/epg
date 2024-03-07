if __name__ == '__main__':
    import sys,os
    sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","epg.settings")
    import django
    django.setup()

from datetime import date,timedelta
from web.models import Channel,Channel_list,Epg
from mypackage.iptv import IptvList

# base_dir = os.path.dirname(__file__)
# playlist = IptvList()
# playlist.loadf(os.path.join(base_dir,'iptv.m3u'))
# for channel0 in playlist.channels:
    # channs = Channel_list.objects.filter(out_name=channel0.name_display)
    # if channs.count() == 0:
    #     # print(channel.name_display)
    #     pass
    # if channs.count() >1:
    #     print(channel0.name_display)
    #     channel,created = Channel.objects.update_or_create(name=channel0.name_display,\
    #         defaults={'channel_id':'<{}:{}>'.format(channs[0].source,channs[0].out_channel_id),
    #                   'source':channs[0].source,
    #                   'has_epg':1,
    #                   'ineed':1,
    #                   'tvg_name':channel0.name,
    #                   'logo':'https://river2718.github.io/logos/{}.png'.format(channel0.name),
    #                   'last_program_date':date.today()-timedelta(days=1)})

    # channel,created = Channel.objects.update_or_create(name=channel0.name_display,\
    #     defaults={
    #               'tvg_name':channel0.name,
    #               'tvg_id':channel0.id,
    #               'sort':channel0.group,
    #               'logo':channel0.logo,
    #               'catchup':channel0.catchup,
    #               'catchup_source':channel0.catchup_source,
    #               'catchup_days':channel0.catchup_days,
    #               'live_url':channel0.url
    #               })

# channels = Channel_list.objects.all()
# for channel in channels:
#     print(channel.out_name)

# channels = Channel.objects.filter(ineed=0)
# for channel in channels:
#     tvg_name = channel.name
#     # if 'CGTN' in tvg_name:
#     #     tvg_name = tvg_name.replace('CGTN','CGTN ')
#     chans = Channel_list.objects.filter(source='tvmao',out_name=tvg_name)
#     if chans.count() == 1:
#         print(channel.name)
#         channel.channel_id = '<{}:{}>'.format(chans[0].source,chans[0].out_channel_id)
#         channel.source = chans[0].source
#         channel.ineed=1
#         channel.save()

from lxml import etree
def test():
    dir_base = os.path.dirname(__file__)
    file_path = os.path.join(dir_base,'pp.xml')
    root = etree.parse(file_path)
    chan_ids = root.xpath('//channel/@id')
    channels = Channel.objects.all()
    for channel in channels:
        if channel.tvg_id in chan_ids:
            print(channel.tvg_id)
            progs = root.xpath('//programme[@channel="{}"]'.format(channel.tvg_id))
            for prog in progs:
                print(prog[0].text)
            break
         
    # for chan in chans:
    #     print(chan.get('id'))
        
def test2():
    Channel.create_m3u()

def test3():
    for epg in Epg.objects.all():
        if epg.chan.id != int(epg.channel_id):
            print(epg.chan.id,epg.channel_id)
            epg.chan = Channel.objects.get(id=epg.channel_id)
            epg.save()

def test4():
    Epg.save_to_dbs_from_xml(repl=False)

def test5():
    Epg.objects.all().delete()
    Channel.objects.update(last_program_date=None)
if __name__ == '__main__':
    test5()