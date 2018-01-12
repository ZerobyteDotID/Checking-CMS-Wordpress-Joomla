# Auto checking CMS Wordpress & Joomla
# Coded by xSuxHaxDax a.k.a DayWalker
# Special thx : Budi - Coy Rap - Koko
# Zerobyte.id - Backbox Indonesian
#
import urllib2

def liat():
	try: 
		u = urllib2.urlopen('%s' % site)
	except: 
		print "[BAD] %s" % site, 
		return
	get = u.getcode()
	if get == 200:
		mulai()
def mulai():
	req = urllib2.Request('%s' %site, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36' })
	html = urllib2.urlopen(req).read()
	jom = '<meta name="generator" content="Joomla!' in html
	word = '<meta name="generator" content="WordPress' in html
	if (jom == True):
		#print "CHECKING %s" %site,
		print "[OK] CMS JOOMLA => %s" %site,
		f = open('Result_Joomla.txt','w')
		f.write("%s" %site,) 
		f.close()
	elif (word == True):
		print "[OK] CMS WORDPRESS => %s" %site,
		f = open('Result_Wordpress.txt','w')
		f.write("%s" %site,) 
		f.close()
	else:
		print "[UNKNOWN] %s" %site,
bnyak = raw_input("Masukan list : ")
with open('%s' % bnyak)  as input_file:
	for a,site in enumerate(input_file):
		liat()