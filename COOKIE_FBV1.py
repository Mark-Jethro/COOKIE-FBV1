import os,sys,re,time
try:import requests,mechanize
except:os.system('pip install requests');os.system('pip install mechanize')
browser=mechanize.Browser()
def run(a):
	for A in a+'\n':sys.stdout.write(A);sys.stdout.flush();time.sleep(0.02)
def logo():os.system('clear');run('\n  \x1b[1;97m - Copyright By : Huỳnh Mai Nhật Minh \x1b[00m\n  \n  \x1b[1;96m        ███╗   ███╗██╗███╗   ██╗██╗  ██╗\n          ████╗ ████║██║████╗  ██║██║  ██║\n          ██╔████╔██║██║██╔██╗ ██║███████║\n          ██║╚██╔╝██║██║██║╚██╗██║██╔══██║\n          ██║ ╚═╝ ██║██║██║ ╚████║██║  ██║\n          ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝\n  \x1b[0m                                \x1b[1;95m[\x1b[1;93m 𝟮𝟬𝟬𝟱 \x1b[1;95m]\x1b[0m\n                            ')
def main():
	E='c_user';C=True;logo();F=input('\n\x1b[1;92m[+] Account Facebook : ');G=input('\n\x1b[1;92m[+] Password Facebook : ');A=input('\n\x1b[1;92m[+] User-Agent : ')
	if A=='':sys.exit()
	elif'Android'in A:H=re.findall('Mozilla([^"]*)Chrome/',A)[0];A='Mozilla'+H+'Chrome/'+'69.0.3497.86'+' Mobile Safari/537.36'
	elif'iPhone'in A:A='Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
	else:sys.exit()
	browser.addheaders=[('User-Agent',A)];browser.set_handle_equiv(C);browser.set_handle_gzip(C);browser.set_handle_redirect(C);browser.set_handle_referer(C);browser.set_handle_robots(False);D=mechanize.CookieJar();browser.set_cookiejar(D);I='https://www.facebook.com/login.php';browser.open(I);browser._factory.is_html=C;browser.select_form(nr=0);browser.form['email']=F;browser.form['pass']=G;browser.submit();B=requests.utils.dict_from_cookiejar(D)
	if E in B:J=B['datr'];K=B['sb'];L=B[E];M=B['xs'];N=B['fr'];O='datr='+J+';sb='+K+';c_user='+L+';xs='+M+';fr='+N+';m_pixel_ratio=3;wd=360×649';run('\n\x1b[1;93m==> Get Cookie Success');print('\n\x1b[1;97m'+O)
	else:run('\n\x1b[1;91m==> Error! An error occurred. Please try again later');sys.exit()
if __name__=='__main__':main()