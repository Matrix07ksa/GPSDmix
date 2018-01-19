import os as matrix
import sys as n
import time as mm
from platform import system
import urllib 
from termcolor import colored
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
admin_path = ['admin.php','/admin/','/administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php','joomla/administrator','login.php',
              'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']


def clear():
    if system() == 'Linux':
        matrix.system("clear")
    if system() == 'Windows':
        matrix.system('cls')
        matrix.system('color a')
    else:
        pass

clear()

def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 100)

def matrix():
    slow(R+'\t\t\t\t\n\n\n {{insta:d7_nn}}\t\t\t\tfb:matrix.gov}}')
    slow(GR+'\t\n\n{{code py/matrix}}  \t\t\t\t{{code py/muhammed}}')                
    print(B+'''

__        __                      __                                              __     
/  |      /  |                    /  |                                            /  |    
$$ |____  $$ |  ______    _______ $$ |   __         ______    ______    ______   _$$ |_   
$$      \ $$ | /      \  /       |$$ |  /  |       /      \  /      \  /      \ / $$   |  
$$$$$$$  |$$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/       /$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$/   
$$ |  $$ |$$ | /    $$ |$$ |      $$   $$<        $$ |  $$/ $$ |  $$ |$$ |  $$ |  $$ | __ 
$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \       $$ |      $$ \__$$ |$$ \__$$ |  $$ |/  |
$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |      $$ |      $$    $$/ $$    $$/   $$  $$/ 
$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/       $$/        $$$$$$/   $$$$$$/     $$$$/                                 
 _____  ____    ______   _$$ |_     ______  $$/  __    __ 
/     \/    \  /      \ / $$   |   /      \ /  |/  \  /  |
$$$$$$ $$$$  | $$$$$$  |$$$$$$/   /$$$$$$  |$$ |$$  \/$$/ 
$$ | $$ | $$ | /    $$ |  $$ | __ $$ |  $$/ $$ | $$  $$<  
$$ | $$ | $$ |/$$$$$$$ |  $$ |/  |$$ |      $$ | /$$$$  \ 
$$ | $$ | $$ |$$    $$ |  $$  $$/ $$ |      $$ |/$$/ $$  |
$$/  $$/  $$/  $$$$$$$/    $$$$/  $$/       $$/ $$/   $$/                                                                                        
''')
    slow(G+'''
[1]}> Guess Plates
[2]}> Guess SHELL

[99]}> exit
		''')
    
    try:
        numper =input("enter your numper >>> ")
        if numper ==1:
            slow("""
[1]} Single web site
[2]} list web site

[99] Back""")
            numper1 = input("Enter the nemper >>> ")
            if numper1 ==1:
                w = raw_input("\t\tEnter the Web site >>[ ")
                for admin in admin_path:
                    if "\n" in w:
                        if "/" not in admin:
                            f = w.split("\n")[0]+admin
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('Plates.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                        elif "/" in admin:
                            f = w.split("\n")[0]+admin.lstrip("/")
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('Plates.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
            #############################################################################################################################################################
                    elif "\n" not in w:
                        if "/" not in admin:
                            f = w+admin
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('Plates.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                        elif "/" in admin:
                            f = w+admin.lstrip("/")
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('Plates.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
            ##############################################################################################################################################################
            elif numper1 ==2:
                web = raw_input("\twep seite list ={ ")
                m = open(web,'r')
                list0 = m.readlines()
                print(colored("\n\t\tweb sites\n","blue"))
                for admin in admin_path:
                    for w in list0:
        ###############################################################################################################################################################
                        if "\n" in w:
                            if "/" not in admin:
                                f = w.split("\n")+admin
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('Plates.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                            elif "/" in admin:
                                f = w.split("\n")[0]+admin.lstrip("/")
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('Plates.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
    #############################################################################################################################################################
                        elif "\n" not in w:
                            if "/" not in admin:
                                f = w+admin
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('Plates.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                            elif "/" in admin:
                                f = w+admin.lstrip("/")
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('Plates.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
            elif numper1 == 99:
                return matrix()
        ##############################################################################################################################################################
        shell1 =['WSO.php','dz.php','mailer.php','promailer.php','hexor.php','hb.php','fuck.php','xz.php','CaZaNoVa163.php','w.php','wp-content/plugins/akismet/akismet.php','images/stories/w.php','wp-content/plugins/google-sitemap-generator/Server.php', 'wp-content/plugins/google-sitemap-generator/tmp/uploads.php', 'wp-content/plugins/google-sitemap-generator/tmp/up.php', 'wp-content/plugins/google-sitemap-generator/Server/', 'wp-content/plugins/google-sitemap-generator/wp-admin/c99.php', 'wp-content/plugins/google-sitemap-generator/tmp/priv8.php', 'wp-content/plugins/google-sitemap-generator/priv8.php', 'wp-content/plugins/google-sitemap-generator/cgi.pl/', 'wp-content/plugins/google-sitemap-generator/tmp/cgi.pl', 'wp-content/plugins/google-sitemap-generator/downloads/dom.php', 'wp-content/plugins/google-sitemap-generator/webadmin.html', 'wp-content/plugins/google-sitemap-generator/admins.php', 'wp-content/plugins/google-sitemap-generator/bluff.php', 'wp-content/plugins/google-sitemap-generator/king.jeen', 'wp-content/plugins/google-sitemap-generator/admins/', 'wp-content/plugins/google-sitemap-generator/admins.asp', 'wp-content/plugins/google-sitemap-generator/admins.php', 'wp-content/plugins/google-sitemap-generator/wp.zip', 'wp-content/plugins/google-sitemap-generator/sitemap-core.php', '/templates/beez/WSO.php', '/templates/beez/dz.php', '/templates/beez/DZ.php', '/templates/beez/cpanel.php', '/templates/beez/cpn.php', '/templates/beez/sos.php', '/templates/beez/term.php', '/templates/beez/Sec-War.php', '/templates/beez/sql.php', '/templates/beez/ssl.php', '/templates/beez/mysql.php', '/templates/beez/WolF.php', '/templates/beez/madspot.php', '/templates/beez/Cgishell.pl', '/templates/beez/killer.php', '/templates/beez/changeall.php', '/templates/beez/2.php', '/templates/beez/Sh3ll.php', '/templates/beez/dz0.php', '/templates/beez/dam.php', '/templates/beez/user.php', '/templates/beez/dom.php', '/templates/beez/whmcs.php', '/templates/beez/vb.zip', '/templates/beez/r00t.php', '/templates/beez/c99.php', '/templates/beez/gaza.php', '/templates/beez/1.php', '/templates/beez/d0mains.php', '/templates/beez/madspotshell.php', '/templates/beez/info.php', '/templates/beez/egyshell.php', '/templates/beez/Sym.php', '/templates/beez/c22.php', '/templates/beez/c100.php', '/templates/beez/configuration.php', '/templates/beez/g.php', '/templates/beez/xx.pl', '/templates/beez/ls.php', '/templates/beez/Cpanel.php', '/templates/beez/k.php', '/templates/beez/zone-h.php', '/templates/beez/tmp/user.php', '/templates/beez/tmp/Sym.php', '/templates/beez/cp.php', '/templates/beez/tmp/madspotshell.php', '/templates/beez/tmp/root.php', '/templates/beez/tmp/whmcs.php', '/templates/beez/tmp/index.php', '/templates/beez/tmp/2.php', '/templates/beez/tmp/dz.php', '/templates/beez/tmp/cpn.php', '/templates/beez/tmp/changeall.php', '/templates/beez/tmp/Cgishell.pl', '/templates/beez/tmp/sql.php', '/templates/beez/0day.php', '/templates/beez/tmp/admin.php', '/templates/beez/L3b.php', '/templates/beez/d.php', '/templates/beez/tmp/d.php', '/templates/beez/tmp/L3b.php', '/templates/beez/sado.php', '/templates/beez/admin1.php', '/templates/beez/upload.php', '/templates/beez/up.php', '/templates/beez/vb.zip', '/templates/beez/vb.rar', '/templates/beez/admin2.asp', '/templates/beez/uploads.php', '/templates/beez/sa.php', '/templates/beez/sysadmins/', '/templates/beez/admin1/', '/templates/beez/sniper.php', '/templates/beez/images/Sym.php', '/templates/beez//r57.php', '/templates/beez/gzaa_spysl', '/templates/beez/sql-new.php', '/templates/beez//shell.php', '/templates/beez//sa.php', '/templates/beez//admin.php', '/templates/beez//sa2.php', '/templates/beez//2.php', '/templates/beez//gaza.php', '/templates/beez//up.php', '/templates/beez//upload.php', '/templates/beez//uploads.php', '/templates/beez/shell.php', '/templates/beez//amad.php', '/templates/beez//t00.php', '/templates/beez//dz.php', '/templates/beez//site.rar', '/templates/beez//Black.php', '/templates/beez//site.tar.gz', '/templates/beez//home.zip', '/templates/beez//home.rar', '/templates/beez//home.tar', '/templates/beez//home.tar.gz', '/templates/beez//forum.zip', '/templates/beez//forum.rar', '/templates/beez//forum.tar', '/templates/beez//forum.tar.gz', '/templates/beez//test.txt', '/templates/beez//ftp.txt', '/templates/beez//user.txt', '/templates/beez//site.txt', '/templates/beez//error_log', '/templates/beez//error', '/templates/beez//cpanel', '/templates/beez//awstats', '/templates/beez//site.sql', '/templates/beez//vb.sql', '/templates/beez//forum.sql', '/templates/beez/r00t-s3c.php', '/templates/beez/c.php', '/templates/beez//backup.sql', '/templates/beez//back.sql', '/templates/beez//data.sql', '/templates/beez/wp.rar/', '/templates/beez/asp.aspx', '/templates/beez/tmp/vaga.php', '/templates/beez/tmp/killer.php', '/templates/beez/whmcs.php', '/templates/beez/abuhlail.php', '/templates/beez/tmp/killer.php', '/templates/beez/tmp/domaine.pl', '/templates/beez/tmp/domaine.php', '/templates/beez/useradmin/', '/templates/beez/tmp/d0maine.php', '/templates/beez/d0maine.php', '/templates/beez/tmp/sql.php', '/templates/beez/X.php', '/templates/beez/123.php', '/templates/beez/m.php', '/templates/beez/b.php', '/templates/beez/up.php', '/templates/beez/tmp/dz1.php', '/templates/beez/dz1.php', '/templates/beez/forum.zip', '/templates/beez/Symlink.php', '/templates/beez/Symlink.pl', '/templates/beez/forum.rar', '/templates/beez/joomla.zip', '/templates/beez/joomla.rar', '/templates/beez/wp.php', '/templates/beez/buck.sql', '/templates/beez/sysadmin.php', '/templates/beez/images/c99.php', '/templates/beez/xd.php', '/templates/beez/c100.php', '/templates/beez/spy.aspx', '/templates/beez/xd.php', '/templates/beez/tmp/xd.php', '/templates/beez/sym/root/home/', '/templates/beez/billing/killer.php', '/templates/beez/tmp/upload.php', '/templates/beez/tmp/admin.php', '/templates/beez/Server.php', '/templates/beez/tmp/uploads.php', '/templates/beez/tmp/up.php', '/templates/beez/Server/', '/templates/beez/wp-admin/c99.php', '/templates/beez/tmp/priv8.php', '/templates/beez/priv8.php', '/templates/beez/cgi.pl/', '/templates/beez/tmp/cgi.pl', '/templates/beez/downloads/dom.php', '/templates/beez/webadmin.html', '/templates/beez/admins.php', '/templates/beez/bluff.php', '/templates/beez/king.jeen', '/templates/beez/admins/', '/templates/beez/admins.asp', '/templates/beez/admins.php', '/templates/beez/wp.zip', '/templates/beez/index.php','/images/WSO.php', '/images/dz.php', '/images/DZ.php', '/images/cpanel.php', '/images/cpn.php', '/images/sos.php', '/images/term.php', '/images/Sec-War.php', '/images/sql.php', '/images/ssl.php', '/images/mysql.php', '/images/WolF.php', '/images/madspot.php', '/images/Cgishell.pl', '/images/killer.php', '/images/changeall.php', '/images/2.php', '/images/Sh3ll.php', '/images/dz0.php', '/images/dam.php', '/images/user.php', '/images/dom.php', '/images/whmcs.php', '/images/vb.zip', '/images/r00t.php', '/images/c99.php', '/images/gaza.php', '/images/1.php', '/images/d0mains.php', '/images/madspotshell.php', '/images/info.php', '/images/egyshell.php', '/images/Sym.php', '/images/c22.php', '/images/c100.php', '/images/configuration.php', '/images/g.php', '/images/xx.pl', '/images/ls.php', '/images/Cpanel.php', '/images/k.php', '/images/zone-h.php', '/images/tmp/user.php', '/images/tmp/Sym.php', '/images/cp.php', '/images/tmp/madspotshell.php', '/images/tmp/root.php', '/images/tmp/whmcs.php', '/images/tmp/index.php', '/images/tmp/2.php', '/images/tmp/dz.php', '/images/tmp/cpn.php', '/images/tmp/changeall.php', '/images/tmp/Cgishell.pl', '/images/tmp/sql.php', '/images/0day.php', '/images/tmp/admin.php', '/images/L3b.php', '/images/d.php', '/images/tmp/d.php', '/images/tmp/L3b.php', '/images/sado.php', '/images/admin1.php', '/images/upload.php', '/images/up.php', '/images/vb.zip', '/images/vb.rar', '/images/admin2.asp', '/images/uploads.php', '/images/sa.php', '/images/sysadmins/', '/images/admin1/', '/images/sniper.php', '/images/images/Sym.php', '/images//r57.php', '/images/gzaa_spysl', '/images/sql-new.php', '/images//shell.php', '/images//sa.php', '/images//admin.php', '/images//sa2.php', '/images//2.php', '/images//gaza.php', '/images//up.php', '/images//upload.php', '/images//uploads.php', '/images/shell.php', '/images//amad.php', '/images//t00.php', '/images//dz.php', '/images//site.rar', '/images//Black.php', '/images//site.tar.gz', '/images//home.zip', '/images//home.rar', '/images//home.tar', '/images//home.tar.gz', '/images//forum.zip', '/images//forum.rar', '/images//forum.tar', '/images//forum.tar.gz', '/images//test.txt', '/images//ftp.txt', '/images//user.txt', '/images//site.txt', '/images//error_log', '/images//error', '/images//cpanel', '/images//awstats', '/images//site.sql', '/images//vb.sql', '/images//forum.sql', '/images/r00t-s3c.php', '/images/c.php', '/images//backup.sql', '/images//back.sql', '/images//data.sql', '/images/wp.rar/', '/images/asp.aspx', '/images/tmp/vaga.php', '/images/tmp/killer.php', '/images/whmcs.php', '/images/abuhlail.php', '/images/tmp/killer.php', '/images/tmp/domaine.pl', '/images/tmp/domaine.php', '/images/useradmin/', '/images/tmp/d0maine.php', '/images/d0maine.php', '/images/tmp/sql.php', '/images/X.php', '/images/123.php', '/images/m.php', '/images/b.php', '/images/up.php', '/images/tmp/dz1.php', '/images/dz1.php', '/images/forum.zip', '/images/Symlink.php', '/images/Symlink.pl', '/images/forum.rar', '/images/joomla.zip', '/images/joomla.rar', '/images/wp.php', '/images/buck.sql', '/includes/WSO.php', '/includes/dz.php', '/includes/DZ.php', '/includes/cpanel.php', '/includes/cpn.php', '/includes/sos.php', '/includes/term.php', '/includes/Sec-War.php', '/includes/sql.php', '/includes/ssl.php', '/includes/mysql.php', '/includes/WolF.php', '/includes/madspot.php', '/includes/Cgishell.pl', '/includes/killer.php', '/includes/changeall.php', '/includes/2.php', '/includes/Sh3ll.php', '/includes/dz0.php', '/includes/dam.php', '/includes/user.php', '/includes/dom.php', '/includes/whmcs.php', '/includes/vb.zip', '/includes/r00t.php', '/includes/c99.php', '/includes/gaza.php', '/includes/1.php', '/includes/d0mains.php', '/includes/madspotshell.php', '/includes/info.php', '/includes/egyshell.php', '/includes/Sym.php', '/includes/c22.php', '/includes/c100.php', '/includes/configuration.php', '/includes/g.php', '/includes/xx.pl', '/includes/ls.php', '/includes/Cpanel.php', '/includes/k.php', '/includes/zone-h.php', '/includes/tmp/user.php', '/includes/tmp/Sym.php', '/includes/cp.php', '/includes/tmp/madspotshell.php', '/includes/tmp/root.php', '/includes/tmp/whmcs.php', '/includes/tmp/index.php', '/includes/tmp/2.php', '/includes/tmp/dz.php', '/includes/tmp/cpn.php', '/includes/tmp/changeall.php', '/includes/tmp/Cgishell.pl', '/includes/tmp/sql.php', '/includes/0day.php', '/includes/tmp/admin.php', '/includes/L3b.php', '/includes/d.php', '/includes/tmp/d.php', '/includes/tmp/L3b.php', '/includes/sado.php', '/includes/admin1.php', '/includes/upload.php', '/includes/up.php', '/includes/vb.zip', '/includes/vb.rar', '/includes/admin2.asp', '/includes/uploads.php', '/includes/sa.php', '/includes/sysadmins/', '/includes/admin1/', '/includes/sniper.php', '/includes/images/Sym.php', '/includes//r57.php', '/includes/gzaa_spysl', '/includes/sql-new.php', '/includes//shell.php', '/includes//sa.php', '/includes//admin.php', '/includes//sa2.php', '/includes//2.php', '/includes//gaza.php', '/includes//up.php', '/includes//upload.php', '/includes//uploads.php', '/includes/shell.php', '/includes//amad.php', '/includes//t00.php', '/includes//dz.php', '/includes//site.rar', '/includes//Black.php', '/includes//site.tar.gz', '/includes//home.zip', '/includes//home.rar', '/includes//home.tar', '/includes//home.tar.gz', '/includes//forum.zip', '/includes//forum.rar', '/includes//forum.tar', '/includes//forum.tar.gz', '/includes//test.txt', '/includes//ftp.txt', '/includes//user.txt', '/includes//site.txt', '/includes//error_log', '/includes//error', '/includes//cpanel', '/includes//awstats', '/includes//site.sql', '/includes//vb.sql', '/includes//forum.sql', '/includes/r00t-s3c.php', '/includes/c.php', '/includes//backup.sql', '/includes//back.sql', '/includes//data.sql', '/includes/wp.rar/', '/includes/asp.aspx', '/includes/tmp/vaga.php', '/includes/tmp/killer.php', '/includes/whmcs.php', '/includes/abuhlail.php', '/includes/tmp/killer.php', '/includes/tmp/domaine.pl', '/includes/tmp/domaine.php', '/includes/useradmin/', '/includes/tmp/d0maine.php', '/includes/d0maine.php', '/includes/tmp/sql.php', '/includes/X.php', '/includes/123.php', '/includes/m.php', '/includes/b.php', '/includes/up.php', '/includes/tmp/dz1.php', '/includes/dz1.php', '/includes/forum.zip', '/includes/Symlink.php', '/includes/Symlink.pl', '/includes/forum.rar', '/includes/joomla.zip', '/includes/joomla.rar', '/includes/wp.php', '/includes/buck.sql', '/includes/sysadmin.php', '/includes/images/c99.php', '/includes/xd.php', '/includes/c100.php', '/includes/spy.aspx', '/includes/xd.php', '/includes/tmp/xd.php', '/includes/sym/root/home/', '/includes/billing/killer.php', '/includes/tmp/upload.php', '/includes/tmp/admin.php', '/includes/Server.php', '/includes/tmp/uploads.php', '/includes/tmp/up.php', '/includes/Server/', '/includes/wp-admin/c99.php', '/includes/tmp/priv8.php', '/includes/priv8.php', '/includes/cgi.pl/', '/includes/tmp/cgi.pl', '/includes/downloads/dom.php', '/includes/webadmin.html', '/includes/admins.php', '/includes/bluff.php', '/includes/king.jeen', '/includes/admins/', '/includes/admins.asp', '/includes/admins.php', '/includes/wp.zip', '/includes/', '/templates/rhuk_milkyway/WSO.php', '/templates/rhuk_milkyway/dz.php', '/templates/rhuk_milkyway/DZ.php', '/templates/rhuk_milkyway/cpanel.php', '/templates/rhuk_milkyway/cpn.php', '/templates/rhuk_milkyway/sos.php', '/templates/rhuk_milkyway/term.php', '/templates/rhuk_milkyway/Sec-War.php', '/templates/rhuk_milkyway/sql.php', '/templates/rhuk_milkyway/ssl.php', '/templates/rhuk_milkyway/mysql.php', '/templates/rhuk_milkyway/WolF.php', '/templates/rhuk_milkyway/madspot.php', '/templates/rhuk_milkyway/Cgishell.pl', '/templates/rhuk_milkyway/killer.php', '/templates/rhuk_milkyway/changeall.php', '/templates/rhuk_milkyway/2.php', '/templates/rhuk_milkyway/Sh3ll.php', '/templates/rhuk_milkyway/dz0.php', '/templates/rhuk_milkyway/dam.php', '/templates/rhuk_milkyway/user.php', '/templates/rhuk_milkyway/dom.php', '/templates/rhuk_milkyway/whmcs.php', '/templates/rhuk_milkyway/vb.zip', '/templates/rhuk_milkyway/r00t.php', '/templates/rhuk_milkyway/c99.php', '/templates/rhuk_milkyway/gaza.php', '/templates/rhuk_milkyway/1.php', '/templates/rhuk_milkyway/d0mains.php', '/templates/rhuk_milkyway/madspotshell.php', '/templates/rhuk_milkyway/info.php', '/templates/rhuk_milkyway/egyshell.php', '/templates/rhuk_milkyway/Sym.php', '/templates/rhuk_milkyway/c22.php', '/templates/rhuk_milkyway/c100.php', '/templates/rhuk_milkyway/configuration.php', '/templates/rhuk_milkyway/g.php', '/templates/rhuk_milkyway/xx.pl', '/templates/rhuk_milkyway/ls.php', '/templates/rhuk_milkyway/Cpanel.php', '/templates/rhuk_milkyway/k.php', '/templates/rhuk_milkyway/zone-h.php', '/templates/rhuk_milkyway/tmp/user.php', '/templates/rhuk_milkyway/tmp/Sym.php', '/templates/rhuk_milkyway/cp.php', '/templates/rhuk_milkyway/tmp/madspotshell.php', '/templates/rhuk_milkyway/tmp/root.php', '/templates/rhuk_milkyway/tmp/whmcs.php', '/templates/rhuk_milkyway/tmp/index.php', '/templates/rhuk_milkyway/tmp/2.php', '/templates/rhuk_milkyway/tmp/dz.php', '/templates/rhuk_milkyway/tmp/cpn.php', '/templates/rhuk_milkyway/tmp/changeall.php', '/templates/rhuk_milkyway/tmp/Cgishell.pl', '/templates/rhuk_milkyway/tmp/sql.php', '/templates/rhuk_milkyway/0day.php', '/templates/rhuk_milkyway/tmp/admin.php', '/templates/rhuk_milkyway/L3b.php', '/templates/rhuk_milkyway/d.php', '/templates/rhuk_milkyway/tmp/d.php', '/templates/rhuk_milkyway/tmp/L3b.php', '/templates/rhuk_milkyway/sado.php', '/templates/rhuk_milkyway/admin1.php', '/templates/rhuk_milkyway/upload.php', '/templates/rhuk_milkyway/up.php', '/templates/rhuk_milkyway/vb.zip', '/templates/rhuk_milkyway/vb.rar', '/templates/rhuk_milkyway/admin2.asp', '/templates/rhuk_milkyway/uploads.php', '/templates/rhuk_milkyway/sa.php', '/templates/rhuk_milkyway/sysadmins/', '/templates/rhuk_milkyway/admin1/', '/templates/rhuk_milkyway/sniper.php', '/templates/rhuk_milkyway/images/Sym.php', '/templates/rhuk_milkyway//r57.php', '/templates/rhuk_milkyway/gzaa_spysl', '/templates/rhuk_milkyway/sql-new.php', '/templates/rhuk_milkyway//shell.php', '/templates/rhuk_milkyway//sa.php', '/templates/rhuk_milkyway//admin.php', '/templates/rhuk_milkyway//sa2.php', '/templates/rhuk_milkyway//2.php', '/templates/rhuk_milkyway//gaza.php', '/templates/rhuk_milkyway//up.php', '/templates/rhuk_milkyway//upload.php', '/templates/rhuk_milkyway//uploads.php', '/templates/rhuk_milkyway/shell.php', '/templates/rhuk_milkyway//amad.php', '/templates/rhuk_milkyway//t00.php', '/templates/rhuk_milkyway//dz.php', '/templates/rhuk_milkyway//site.rar', '/templates/rhuk_milkyway//Black.php', '/templates/rhuk_milkyway//site.tar.gz', '/templates/rhuk_milkyway//home.zip', '/templates/rhuk_milkyway//home.rar', '/templates/rhuk_milkyway//home.tar', '/templates/rhuk_milkyway//home.tar.gz', '/templates/rhuk_milkyway//forum.zip', '/templates/rhuk_milkyway//forum.rar', '/templates/rhuk_milkyway//forum.tar', '/templates/rhuk_milkyway//forum.tar.gz', '/templates/rhuk_milkyway//test.txt', '/templates/rhuk_milkyway//ftp.txt', '/templates/rhuk_milkyway//user.txt', '/templates/rhuk_milkyway//site.txt', '/templates/rhuk_milkyway//error_log', '/templates/rhuk_milkyway//error', '/templates/rhuk_milkyway//cpanel', '/templates/rhuk_milkyway//awstats', '/templates/rhuk_milkyway//site.sql', '/templates/rhuk_milkyway//vb.sql', '/templates/rhuk_milkyway//forum.sql', '/templates/rhuk_milkyway/r00t-s3c.php', '/templates/rhuk_milkyway/c.php', '/templates/rhuk_milkyway//backup.sql', '/templates/rhuk_milkyway//back.sql', '/templates/rhuk_milkyway//data.sql', '/templates/rhuk_milkyway/wp.rar/', '/templates/rhuk_milkyway/asp.aspx', '/templates/rhuk_milkyway/tmp/vaga.php', '/templates/rhuk_milkyway/tmp/killer.php', '/templates/rhuk_milkyway/whmcs.php', '/templates/rhuk_milkyway/abuhlail.php', '/templates/rhuk_milkyway/tmp/killer.php', '/templates/rhuk_milkyway/tmp/domaine.pl', '/templates/rhuk_milkyway/tmp/domaine.php', '/templates/rhuk_milkyway/useradmin/', '/templates/rhuk_milkyway/tmp/d0maine.php', '/templates/rhuk_milkyway/d0maine.php', '/templates/rhuk_milkyway/tmp/sql.php', '/templates/rhuk_milkyway/X.php', '/templates/rhuk_milkyway/123.php', '/templates/rhuk_milkyway/m.php', '/templates/rhuk_milkyway/b.php', '/templates/rhuk_milkyway/up.php', '/templates/rhuk_milkyway/tmp/dz1.php', '/templates/rhuk_milkyway/dz1.php', '/templates/rhuk_milkyway/forum.zip', '/templates/rhuk_milkyway/Symlink.php', '/templates/rhuk_milkyway/Symlink.pl', '/templates/rhuk_milkyway/forum.rar', '/templates/rhuk_milkyway/joomla.zip', '/templates/rhuk_milkyway/joomla.rar', '/templates/rhuk_milkyway/wp.php', '/templates/rhuk_milkyway/buck.sql', '/templates/rhuk_milkyway/sysadmin.php', '/templates/rhuk_milkyway/images/c99.php', '/templates/rhuk_milkyway/xd.php', '/templates/rhuk_milkyway/c100.php', '/templates/rhuk_milkyway/spy.aspx', '/templates/rhuk_milkyway/xd.php', '/templates/rhuk_milkyway/tmp/xd.php', '/templates/rhuk_milkyway/sym/root/home/', '/templates/rhuk_milkyway/billing/killer.php', '/templates/rhuk_milkyway/tmp/upload.php', '/templates/rhuk_milkyway/tmp/admin.php', '/templates/rhuk_milkyway/Server.php', '/templates/rhuk_milkyway/tmp/uploads.php', '/templates/rhuk_milkyway/tmp/up.php', '/templates/rhuk_milkyway/Server/', '/templates/rhuk_milkyway/wp-admin/c99.php', '/templates/rhuk_milkyway/tmp/priv8.php', '/templates/rhuk_milkyway/priv8.php', '/templates/rhuk_milkyway/cgi.pl/', '/templates/rhuk_milkyway/tmp/cgi.pl', '/templates/rhuk_milkyway/downloads/dom.php', '/templates/rhuk_milkyway/webadmin.html', '/templates/rhuk_milkyway/admins.php', '/templates/rhuk_milkyway/bluff.php', '/templates/rhuk_milkyway/king.jeen', '/templates/rhuk_milkyway/admins/', '/templates/rhuk_milkyway/admins.asp', '/templates/rhuk_milkyway/admins.php', '/templates/rhuk_milkyway/wp.zip', '/templates/rhuk_milkyway/','WSO.php', 'a.php', 'z.php', 'e.php', 'r.php', 'xz.php', 'hhh.php', 'fuck.php', 'hb.php', 't.php', 'y.php', 'u.php', 'i.php', 'o.php', 'p.php', 'q.php', 's.php', 'd.php', 'f.php', 'g.php', 'h.php', 'j.php', 'k.php', 'l.php', 'm.php', 'w.php', 'x.php', 'c.php', 'v.php', 'b.php', 'n.php', '1.php', '2.php', '3.php', '4.php', '5.php', '6.php', '7.php', '8.php', '9.php', '10.php', '12.php', '11.php', '1234.php']
        if numper ==2:
            slow("""
[1]} Single web site
[2]} list web site

[99] Back""")
            numper1 = input("Enter the nemper >>> ")
            if numper1 ==1:
                w = raw_input("Enter the Web site >>[ ")
                for shell in shell1:
                    if "\n" in w:
                        if "/" not in shell:
                            f = w.split("\n")[0]+shell
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('shell.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                        elif "/" in shell:
                            f = w.split("\n")[0]+shell.lstrip("/")
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('shell.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
            #############################################################################################################################################################
                    elif "\n" not in w:
                        if "/" not in shell:
                            f = w+shell
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('shell.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                        elif "/" in shell:
                            f = w+shell.lstrip("/")
                            ur = urllib.urlopen(f)
                            if ur.getcode() == 200:
                                print(colored("[+]find => "+str(f),"blue"))
                                p = open('shell.txt','a').write(str(f)+"\n")
                            elif ur.getcode() == 404:
                                print(colored("[!] not find => "+str(f),"red"))
                            else:
                                print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
            ##############################################################################################################################################################
            elif numper1 ==2:
                web = raw_input("\twep seite list ={ ")
                m = open(web,'r')
                list0 = m.readlines()
                print(colored("\n\t\tweb sites\n","blue"))
                for shell in shell1:
                    for w in list0:
        ###############################################################################################################################################################
                        if "\n" in w:
                            if "/" not in shell:
                                f = w.split("\n")[0]+shell
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('shell.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                            elif "/" in shell:
                                f = w.split("\n")[0]+shell.lstrip("/")
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('shell.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
    #############################################################################################################################################################
                        elif "\n" not in w:
                            if "/" not in shell:
                                f = w+shell
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('shell.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
                            elif "/" in shell:
                                f = w+shell.lstrip("/")
                                ur = urllib.urlopen(f)
                                if ur.getcode() == 200:
                                    print(colored("[+]find => "+str(f),"blue"))
                                    list0.remove(str(w))
                                    p = open('shell.txt','a').write(str(f)+"\n")
                                elif ur.getcode() == 404:
                                    print(colored("[!] not find => "+str(f),"red"))
                                else:
                                    print(colored("[?] Error => "+str(f)+" status code => "+str(ur.getcode()),"red"))
            elif numper1 == 99:
                return matrix()
    except SyntaxError:
        print('False Enter')
    except AttributeError:
        print('FALSE Break ')
    except KeyboardInterrupt:
        print('FALSE ENTER CTRLS')
    except NameError:
        print('\nNO string FAlse exit\n')
if __name__ =='__main__':
    matrix()
    

