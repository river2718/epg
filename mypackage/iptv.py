import re

class Channel:
    def __init__(self,id,name,logo,group,catchup,catchup_source,catchup_days,name_display,url):
        self.id = id
        self.name = name
        self.logo = logo
        self.group = group
        self.catchup = catchup
        self.catchup_source = catchup_source
        self.catchup_days = catchup_days
        self.name_display = name_display
        self.url = url
    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.id,self.name,self.logo,self.group,self.catchup,self.catchup_source,self.catchup_days,self.name_display,self.url)
    
class IptvList:
    def __init__(self,header='',channels=[]):
        self.header = header
        self.channels = channels
    def loadf(self,filepath):
        self.channels = []
        with open(filepath,'r',encoding='utf8') as f:
            fileline = f.readline()
            while fileline:
                fileline = fileline.strip(' \n\t')
                m = re.search(r'^#EXTM3U (.*)',fileline)
                if m is not None:
                    self.header = m.group(1)
                if re.search(r'^#EXTINF',fileline) is not None:
                    m = re.search(r'tvg-id="([^"]*)"',fileline)
                    ch_id = m.group(1) if m else ""
                    m = re.search(r'tvg-name="([^"]*)"',fileline)
                    ch_name = m.group(1) if m else ""
                    m = re.search(r'tvg-logo="([^"]*)"',fileline)
                    ch_logo = m.group(1) if m else ""
                    m = re.search(r'group-title="([^"]*)"',fileline)
                    ch_group = m.group(1) if m else ""
                    m = re.search(r'catchup="([^"]*)"',fileline)
                    ch_catchup = m.group(1) if m else ""
                    m = re.search(r'catchup-source="([^"]*)"',fileline)
                    ch_catchup_source = m.group(1) if m else ""
                    m = re.search(r'catchup-days="([^"]*)"',fileline)
                    ch_catchup_days = m.group(1) if m else ""
                    m = re.search(r',([^,]*$)',fileline)
                    ch_name_display = m.group(1).strip(' ') if m else ""
                    ch_url = f.readline().strip(' \n')
                    self.channels.append(Channel(ch_id,ch_name,ch_logo,ch_group,ch_catchup,ch_catchup_source,ch_catchup_days,ch_name_display,ch_url))
                fileline = f.readline()
    
    def dump(self,filepath):
        with open(filepath,'w',encoding='utf8') as f:
            if self.header != '':
                f.write('#EXTM3U {}\n'.format(self.header))
            else:
                f.write('#EXTM3U\n')
            for channel in self.channels:
                txt = '#EXTINF:-1 tvg-id="{}" tvg-name="{}" tvg-logo="{}" group-title="{}"'\
                    .format(channel.id,channel.name,channel.logo,channel.group)
                if channel.catchup != '':
                    txt = txt + ' catchup="{}"'.format(channel.catchup)
                if channel.catchup_source != '':
                    txt = txt + ' catchup-source="{}"'.format(channel.catchup_source)
                if channel.catchup_days != '':
                    txt = txt + ' catchup-days="{}"'.format(channel.catchup_days)
                txt = txt + ',{}\n'.format(channel.name_display)
                f.write(txt)
                f.write('{}\n'.format(channel.url))

if __name__ == '__main__':
    # playlist = IptvList()
    # playlist.loadf('./in.m3u')
    # playlist.dump('./out.m3u')
    pass