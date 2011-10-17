from os import system, path
from feedparser import parse
import ipdb;
aFeed = parse('http://blip.tv/djangocon/rss')
destFolder = '~/SharedFolder/DjangoCon/'
for item in aFeed['entries']:
	if (item.blip_datestamp.split('T')[0].split('-')[0] == '2011'):
		for media in item.media_content:
			if(media.has_key('blip:role') and (media['blip:role'].find('LD') >= 0)):
				filename = media['url'].split('/')[-1]

				print("Convertion of %s LD video file to mp3 started" % filename)
				print("---------------------------------------------")
				system('wget -P %s %s' % (destFolder,media['url']))
				system('ffmpeg -i "%s" -ab 256k -f mp3 "%s.mp3"' % (filename,path.splitext(filename)[0]))
				print("Removing %s" % (filename))
				system('rm -f %s' % (filename))
