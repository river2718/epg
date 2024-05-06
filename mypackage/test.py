if __name__ == '__main__':
    import sys,os
    sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","epg.settings")
    import django
    django.setup()

import json
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
        print('time out')
        return None
    if result.returncode != 0:
        print(result.stdout.decode())
        return None
    else:
        print(result.stdout.decode())
        return True
    
def main():
    for channel in Channel.objects.all():
        print(channel.name)
        print(get_video_info(channel.live_url))

if __name__ == '__main__':
    main()