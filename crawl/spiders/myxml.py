import datetime
from lxml import etree
from requests import Session
from dateutil import tz

with Session() as s:
    s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36)'})
    r = s.get('https://live.fanmingming.com/e.xml')
    r.raise_for_status()
xml_data = etree.XML(r.content)

tz_sh = tz.gettz('Asia/Shanghai')

def get_epgs_xml(channel, channel_id, dt, func_arg):
    success = 1
    epgs = []
    progs = xml_data.xpath('//programme[@channel="{}" and starts-with(@start,{})]'.format(channel_id,dt.strftime('%Y%m%d')))
    for prog in progs:
        starttime = datetime.datetime.strptime(prog.get('start'),'%Y%m%d%H%M%S +0800').astimezone(tz=tz_sh)
        endtime = datetime.datetime.strptime(prog.get('stop'),'%Y%m%d%H%M%S +0800').astimezone(tz=tz_sh)
        title = prog.find('title').text
        descr = prog.find('desc')
        epg = {'channel_id': channel.id,
                'starttime': starttime,
                'endtime': endtime,
                'title': title,
                'desc': descr,
                'program_date': dt,
                } 
        epgs.append(epg)
    msg = ''
    ret = {
        'success': success,
        'epgs': epgs,
        'msg': msg,
        'last_program_date': dt,
        'ban':0,
    }
    return ret

if __name__ == '__main__':
    dt = datetime.date.today()
    class Channel:
        pass
    channel = Channel()
    channel.id = 1
    ret = get_epgs_xml(channel, 'CCTV1', dt, 0)
    print(ret)