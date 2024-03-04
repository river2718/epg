if __name__ == '__main__':
    import sys,os
    sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","epg.settings")
    import django
    django.setup()

from datetime import date,timedelta
from web.models import Channel,Channel_list
from mypackage.iptv import IptvList

base_dir = os.path.dirname(__file__)
playlist = IptvList()
playlist.loadf(os.path.join(base_dir,'iptv.m3u'))
for channel0 in playlist.channels:
    channs = Channel_list.objects.filter(out_name=channel0.name_display)
    if channs.count() == 0:
        # print(channel.name_display)
        pass
    if channs.count() >1:
        print(channel0.name_display)
        channel,created = Channel.objects.update_or_create(name=channel0.name_display,\
            defaults={'channel_id':'<{}:{}>'.format(channs[0].source,channs[0].out_channel_id),
                      'source':channs[0].source,
                      'has_epg':1,
                      'ineed':1,
                      'tvg_name':channel0.name,
                      'logo':'https://river2718.github.io/logos/{}.png'.format(channel0.name),
                      'last_program_date':date.today()-timedelta(days=1)})

# channels = Channel_list.objects.all()
# for channel in channels:
#     print(channel.out_name)