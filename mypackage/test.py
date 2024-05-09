if __name__ == '__main__':
    import sys,os
    sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","epg.settings")
    import django
    django.setup()

import json,requests,shutil
from ipytv import playlist
from web.models import Channel
from subprocess import run,Popen,PIPE,STDOUT,TimeoutExpired
# ffmpeg_folder = '/home/pi/Programs/ffmpeg-5.0.1-arm64-static'
ffmpeg_folder ='/bin'

def get_video_info(fullname):
    cmd = os.path.join(ffmpeg_folder,'ffprobe')
    args = [cmd,'-hide_banner',
                # '-v','panic',
                # '-print_format','json',
                # '-show_streams',
                # '-select_streams','v',
                '-i',fullname]
    try:
        result = run(args,stdin=PIPE,stdout=PIPE,stderr=STDOUT,timeout=10)
    except TimeoutExpired:
        # print('Time out')
        return False
    if result.returncode != 0:
        # print(result.stdout.decode())
        return False
    else:
        # print(result.stdout.decode())
        return True

def get_channel_urls():
    # url = 'https://live.fanmingming.com/tv/m3u/ipv6.m3u'
    # pl = playlist.loadu(url)
    pl = playlist.loadf('/home/pi/PythonProjects/epg/mypackage/iptv_old.m3u')
    # attributes = pl.get_attributes()
    # for k,v in attributes.items():
    #     print(f'"{k}":"{v}"')
    for chan in pl:
        tvg_name = chan.attributes['tvg-name']
        # print(tvg_name)
        try:
            channel = Channel.objects.get(tvg_name=tvg_name)
        #     if not channel.is_valid:
        #         print(tvg_name)
        #         channel.live_url = chan.url
        #         channel.save()
        except Channel.DoesNotExist:
            # channel = Channel.objects.create(**{
            #             'name':tvg_name,
            #             'tvg_name':tvg_name,
            #             'tvg_id':tvg_name,
            #             'sort':'NewTV系列',
            #             'logo':'https://river2718.github.io/logos/{}.png'.format(tvg_name),
            #             'catchup':'append',
            #             'catchup_source':'?playseek={utc:YmdHMS}-{utcend:YmdHMS}',
            #             'catchup_days':'7',
            #             'live_url':chan.url
            #             })
            print(tvg_name)
            # pass
        # print(channel.name,channel.url,channel.duration)
        # print(channel.attributes)
        # print(channel.extras)

def main():
    # check_validity_of_urls()
    update_invalid_urls()
    update_m3u()

def check_validity_of_urls():
    for channel in Channel.objects.all():
        if not get_video_info(channel.live_url):
            if channel.is_valid:
                print('Warning: url of "{}" is not valid. Change is_valid to "False".'.format(channel.tvg_name))
            channel.is_valid = False
        else:
            if not channel.is_valid:
                print('Warning: url of "{}" is valid. Change is_valid to "True".'.format(channel.tvg_name))
            channel.is_valid = True
        channel.save()

def update_invalid_urls():
    url = 'https://live.fanmingming.com/tv/m3u/ipv6.m3u'
    pl = playlist.loadu(url)
    for chan in pl:
        tvg_name = chan.attributes['tvg-name']
        try:
            channel = Channel.objects.get(tvg_name=tvg_name)
            if not channel.is_valid:
                if get_video_info(chan.url):
                    print('Info: url of channel {} is updated.'.format(tvg_name))
                    channel.live_url = chan.url
                    channel.is_valid = True
                    channel.save()
        except Channel.DoesNotExist:
            print('Info: channel {} is not in database.'.format(tvg_name))
            pass

def update_m3u():
    Channel.create_m3u()
    dir_base = os.path.dirname(__file__)
    file_path = os.path.join(dir_base,'iptv_new.m3u')
    dir_base_new = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(dir_base))),'river2718.github.io')
    file_path_new = os.path.join(dir_base_new,'iptv.m3u')
    shutil.move(file_path,file_path_new)

if __name__ == '__main__':
    main()