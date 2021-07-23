
# 序言
这是我想了解CTF开始看的书，分别为反欺骗三艺术、反入侵的艺术、反黑客三艺术,我称它们为反黑三部曲。它们没有阅读的先后顺序，个人比较推荐只看反黑客三艺术，这三者中比较好的，其余两本是凯文-米特尼克所写，描述的社工的方法，如同故事一般，他的第二部反入侵的艺术比其第一步反欺骗的艺术好看。而这里所写的笔记主要是对反黑客的艺术中的各种链接和人物传记中的博客进行记录。    
## 反欺骗的艺术
Author: **Kevin D.Mitnick** 
### Note
**邮件落点(mail drop)** 社交工程师对租来的邮箱的称呼。通常是用假名租来的，其用途是接收受害者上当后寄来的文件或包裹。    

**糖果式的安全：** 贝尔实验室的**Bellovin** 和**Cheswick** 发明的一个术语，用来描述一种安全情形：虽然外围安全设施（比如防火墙）很强大，但内部的基础设施却很脆弱。此术语源于M&M糖果，这种糖外壳硬而内核软。    

**地下酒吧式的安全：** 这种安全性依赖于知道所要的信息在何处，使用某个词或名字来访问该信息或计算机系统    

**基于隐匿度的安全：** 一种不太有效的计算机安全方法，它依赖于对system运行的细节情况（协议、算法和内部系统）进行保密。基于隐匿度的安全，它错误地假设了在可信任的一群人以外，其他人无法进入系统。    

**RAT** 远程访问的特洛伊木马，可以让攻击者完全访问你的计算机，就像他坐在你的键盘前面一样。    

**MALWARE** 恶意软件的俗称，指像病毒、蠕虫或特洛伊木马这一类能执行破坏性任务的计算机程序。    

**后门** 一个可在用户浑然不知的情况下秘密地进入其计算机的隐藏入口点。程序员在开发软件程序时也可能会使用后门技术，这样他们可以进入到程序中改正错误。

**安全套接字层** Netscape开发的一个安全协议。在因特网上的安全通信中，它可以提供客户和服务器的身份认证    

[clearlogs日志软件](www.ntsecurity.nu)    

**哑终端** 没有微处理器的终端。哑终端只能接受简单的命令并以文本方式显示字符和数字。
 
[列举的单词列表](http://www.outpost9.com/files/WordLists.html) 

**密码破解** L0phtcrack 如今已经到7了    

[密码恢复工具](http://www.elcomsoft.com) 

[世界安全博览](http://www.secureworldexpo.com) 

--------

## 反入侵的艺术
Author: **Kevin D.Mitnick** 
Author: **William L. Simon** 

这是他写的第二部
### Note
**IDA Pro** Interactive Disassembler(www.ccso.com有出售是个逆向软件)

[反向DNS查询](www.samspade.org) 
 
到这就没有可记录了的。


## 反黑客的艺术
Author: Roger A. Grimes
### Note
本次学习收获最大的就是这本书了，三本之中最好的一本。
作者采用一个章节引出一个相关的人物接着科普他的人物事迹

[Kevin Mitnick](https://www.secureworldexpo.com) 
 
[Robert T. Morris](https://en.wikipedia.org/wiki/Morris_worm) 后来成为了[ACM的研究员](http://awards.acm.org/award_winners/morris_4169967.cfm) 

**指纹采集**(fingerprinting)
[Nmap](https://nmap.org/) 

[Nikto2](https://cirt.net/Nikto2) 

黑客用来破解目标的不同技术：   
- 零日攻击(Zero-Days)
- 未打补丁的软件(Unpatched Software)
- 恶意软件(Malware)
- 社会工程(Social Engineering)
- 密码问题(Password Issues)
- 窃听/中间人攻击(Eavesdropping/MitM)
- 数据泄露(Data Leaks)
- 错误配置(Misconfiguration)
- 拒绝服务(Denial of Service)
- 内部人员/合作伙伴/顾问/供应商/第三方(Insider/Partner/Consultant/Vendor/Third Party)
- 用户错误(User Error)
- 物理访问(Physical Access)
- 权限升级(Privilege Escalation)    

[Verizon的数据泄露年度报告](http://www.verizonenterprise.com/verizon-insights-lab/dbir/) 
 
**Bruce Schneier** 布鲁斯.施乃尔    
他的书籍：
- [《应用密码学：用C语言实现的协议、算法和源代码》](https://www.amazon.com/Applied-Cryptography-Protocols-Algorithms-Source/dp/) 
 
- [《机密和谎言：网络世界中的数字安全》](https://www.amazon.com/Secrets-Lies-Digital-Security-Networked/dp/0471453803) 
 
- [《超越恐惧：在不确定的世界中理智地思考安全》](https://www.amazon.com/Beyond-Fear-Thinking-Sensibly-Uncertain/dp/0387026207) 
 
- [《骗子和异常：社会生存需要信任》](https://www.amazon.com/Liars-Outliers-Enabling-Society-Thrive/dp/1118143302/)

- [《数据和歌利亚：搜集你的数据、控制你的世界的隐藏战争》](https://www.amazon.com/Data-Goliath-Battles-Collect-Control/dp/039335217X/)     


     
[Schneier的个人博客](https://www.schneier.com/) 

[每月密码简报](https://www.schneier.com/crypto-gram/) 
 
 **扩展验证** Extended Validation, EV **[数字证书](https://en.wikipedia.org/wiki/Extended_Validation_certificate) 

[扩展验证的网站通常以某种方式突出显示（通常是绿色的地址栏或高亮显示的绿色名称）](https://www.bankofamerica.com) 
 
**Kevin Mitnick**    
 
[kevin的网站](https://mitnicksecurity.com/) 

- [《网络的幽灵》](https://www.amazon.com/Ghost-Wires-Adventures-Worlds-Wanted/dp/03160377729/) 
 
- [《隐形的艺术》](https://www.amazon.com/Art-Invisibility-Worlds-Teaches-Brother/dp/0316380504/)

- [kevin在KnowBe4网站上的安全意识培训：](https://www.knowbe4.com/products/kevin-mitnick-security-awareness-training/) 

- [在Slashdot网站上的问答](https://news.slashdot.org/story/11/09/12/1234252/Kevin-Mitnick-Answers)     

[通用漏洞与披露（Common Vulnerabilities and Exposures, CVE](http://cve.mitre.org) 

[微软安全智能报告](http://www.microsoft.com/sir) 
 
[Metasploit](https://www.metasploit.com/) 
 
现在通常把尽力减少软件漏洞数量的过程称为**安全开发生命周期(Security Development Liftcycle,SDL)**     

[SDL免费工具](https:www.microsoft.com/sdl) 
 
[Daniel J. Bernstein博士](https://en.wikipedia.org/wiki/Daniel_J.__Bernstein)     

**Michael Howard** 

[其著作](https://www.amazon.com/Michael-Howard/e/B001H6GDPW/ref=dp__byline_cont_book_1) 

[Michael Howard的博客](https://blogs.msdn.microsoft.com/michael_howard/) 
 
[他的推特](https://twitter.com/michael_howard) 
 
**Gary McGraw** 加里.麦格劳

[早期加入的公司Cigital](https://www.cigital.com/) 
 
[与Ed Felten合著](https://www.amazon.com/Gary-McGraw/e/B000APFZ2S/ref=sr_tc_2_0?qid=1484584085&sr=1-2-ent) 
  
[Ross Anderson撰写的Security Engineering](https://www.amazon.com/Security-Engineering-Building-Dependable-Distributed/dp/0471389226/) 
 
[McGraw在他的月度银弹安全播客](https://www.garymcgraw.com/technology/silver-bullet-podcast/) 
 [其著作](https://www.amazon.com/Gary-McGraw/e/B000APFZ2S/) 
  
[Gary McGraw的网站](https://www.garymcgraw.com/) 

[其播客](https://www.garymcgraw.com/technology/silver-bullet-podcast/) 
 
[2003 SQL Slammer蠕虫](https://en.wikipedia.org/wiki/SQL_Slammer) 
 
 **Susan Bradley** 

[参与的Window Secrets简报](http://windowssecrets.com/) 
 
[开发的勒索防护工具箱](http://www.thirdtier.net/ransomware-prevention-kit/) 

[Susan Bradley的Microsoft MVP播客](http://blogs.msmvps.com/bradley/) 

[Susan Bradley的Windows Secrets简报](http://windowssecrets.com/author/susan-bradley) 

**Mark Russinovich** 

[其创建的优秀工具](http://www.sysinternals.com) 
 
[Docker](https://www.docker.com/) 
 
[Mark Russinovich的维基百科入口](https://en.wikipedia.org/wiki/Mark_Russinovich) 
  
[Mark Russinovich的著作](https://www.amazon.com/Mark-E.-Russinovich/e/B001IGNICC/) 
 
[Mark Russinovich的网站](http://www.trojanhorsethebook.com/) 

[Mark Russinovich的优秀Sysinternals实用工具](http://www.sysinternals.com) 
 
[NIST美国国家标准与技术研究所](http://www.nist.gov) 

[NSA美国国家安全局](http://www.nsa.gov) 

**Martin Hellman** 

[Martin Hellman在斯坦福大学的经历](http://www-ee.stanford.edu/~hellman/crypto.html) 

[其著作](http://www-ee.stanford.edu/~hellman/crypto.html) 

[James P. Anderson在1980年发表其开创性论文“计算机安全威胁监视与监控”(Computer Security Threat Monitoring and Surveillance)](http://csrc.nist.gov/publications/history/ande80.pdf) 
 
[Verizon的数据泄露年度报告 ](http://www.verizonenterprise.com/verizon-insights-lab/dbir/) 

**高级持续性威胁(Advanced Persistent Threats, APT)** 

[Dorothy E. Denning博士发表了关于异常检测的里程碑式论文](https://users.ece.cmu.edu/~adrian/731-sp04/readings/denning-ids.pdf) 

**入侵检测系统(IDS)** 

**入侵防御系统(IPS)** 

[第一个广泛使用的HIDS可追溯到Tripwire](https://en.wikipedia.org/wiki/Tripwire_(company))    

[一个被广泛使用的NIDS是开源的Snort](https://www.snort.org/) 
 
[NISt的特殊出版物SP800-92"计算机安全日志管理指南"](http://csrc.nist.gov/publicantions/nistpubs/800-92/SP800-92.pdf) 
 
 **检测高级持续性威胁(APT)** 

[微软的高级持续性威胁服务](https://www.microsoft.com/en-us/cloud-platform/advanced-threat-analytics) 
 
[高级持续性保护](https://www.microsoft.com/en-us/WindowsForBusiness/windows-atp) 
 
[CrowdStrike](https://www.crowdstrike.com) 

[Alien Vault](https://www.alienvault.com) 
 
[长期以来作为防恶意软件供应商的TrendMicro](http://www.trendmicro.com) 

**Michael Dubinsky** 

**Advanced Threat Analytics, ATA** 

[pass-the-hash攻击](https://en.wikipedia.org/wiki/Pass_the_hash) 

[golden ticket攻击](http://www.infoworld.com/article/2608877/security/fear-the-golden-ticket-attack-.html) 

**远程控制木马(Remote Access Trojans,RAT)** 

[SubSeven](https://en.wikipedia.org/wiki/Sub7) 
 
[Michael Dubinsky的推特](https://twitter.com/michaeldubinsky) 
 
[Jeffery C. Mogul](https://research.google.com/pubs/JefferyMogul.html) 

[Morris Internet蠕虫](https://en.wikipedia.org/wiki/Morris_worm) 
 
**Cheswick将防火墙命名为proxyd** 

**William Cheswick** 现代防火墙得到创始人之一

[防火墙的经典著作Firewalls and Internet Security:Repelling the Wily Hacker](https://www.amazon.com/Firewalls-Internet-Security-Repelling-Hacker/dp/020163466X) 
 
[其著名的蜜罐An Evening with Berferd in which a Cracker Is Lured, Endured, and Studied](http://www.cheswick.com/ches/papers/berferd.pdf) 
 
[其网络地图项目](http://cheswick.com/ches/map/) 
 
[DYN DDoS攻击](http://dyn.com/blog/dyn-analysis-summary-of-friday-october-21-attack/) 
 
[William Cheswick的个人网站](http://www.checwick.com/ches/index.html) 
 
[Clifford Stoll撰写的蜜罐The Cuckoo's Egg](https://www.amazon.com/Cuckoos-Egg-Tracking-Computer-Espionage/dp/1416507777787) 

[作者写的Honeypots for Windows](https://www.amazon.com/Honeypots-Windows-Books-Professionals/dp/1590593359/) 

[蜜网项目](http://www.honeynet.org)是蜜罐信息和取证的最佳选择
 
[Honeywall CD-ROM映像](http://www.honeynet.org/project/HoneywallCDROM) 
 
[Honeyd](http://www.honeyd.org)是一个开源的蜜罐软件
 
[作者喜欢的蜜罐软件Kfsensor](http://www.keyfocus.net)其仅适用window
 
**Lance Spitzner** 其是作者遇到的一个蜜罐倡导者

现在大多数人认为**Spitzner**是现代计算机蜜罐之父

[Spitzner的经典](https://www.amazon.com/Honeypots-Tracking-Hackers-Lance-Spitzner/dp/0321108957) 
 
[作者写的关于蜜罐带书籍](https://www.amazon.com/Honeypots-Windows-Books-Professionals/dp/1590593359) 
 
他读的三篇让他从防火墙到蜜罐的兴趣转变
- 计算机病毒防御之父Fred Cohen的一篇[论文](https://en.wikipedia.org/wiki/Fred_Cohen) 

- Clifford Stoll的TheCuckoo's Egg

- Bill Cheswick的白皮书    


[SANS Institute](http://www.sans.org) 现在改为了[SANS Securing the Human](https://securingthehuman.sans.org/) 
 
[Lance Spitzner的推特](https://twitter.com/lspitzner) 

[Know Your Enemy白皮书](http://old.honeynet.org/papers/enemy/) 
 
[Know Your Enemy系列白皮书](http://www.honeynet.org/papers) 
 
[开源工具John the Ripper](http://www.openwall.com/john/)这是一个非常好的学习平台PS：作者说的
 
[FIDO联盟](https://fidoalliance.org/)通过互联网来消除用户对密码的依赖的势头正持续增加 
 
[Cormac Herley博士的网站](http://cormac.herley.org/) 

[Cormac Herley博士的推特](https://twitter.com/cormacherley) 
 
[Cormac Herley博士的Microsoft个人资料](https:www.microsoft.com/en-us/research/people/cormac/) 
 
[Wireshark](http://www.wireshark.com/) 
 
[Ethereal](https://sourceforge.net/project/ethereal/) 
 
**Aircrack-ng** 无线攻击工具，kali自带

[Kismet](https://www.kismetwireless.net) 

[Fern Wi-Fi Hacker](https://github.com/savio-code/fern-wifi-cracker) 
 
[Firesheep](http://codebutler.com/firesheep) 

**电磁屏蔽(又称EMI屏蔽)**、射频屏蔽或法拉第笼(Faraday cage)

**Thomas d'Otreppe de Bouvette** Aircrack-ng的创建者 

[Bouvette的无线入侵检测程序OpenWIPS-ng](http://www.openwips-ng.org/) 

[Bouvette和Rick Farina在DEF CON演示无线黑客的视频](https://www.youtube.com/watch?v=XqPPqqV_884) 

[上面的pdf](https://defcon.org/images/defcon-16/dc16-presentations/defcon-16-de_bouvette-farina.pdf) 

**CISSP认证** 
[国际信息系统安全认证联盟(ISC)^2](https://www.isc2.org/) 

**SANS学院的认证** 
[GIAC](http://www.giac.org/certifications/get-certified/roadmap) 
 
**CEH认证** 
[首席信息安全官](https://cert.eccouncil.org/certified-chief-information-security-officer.html) 

还有其他认证例如cisco的

**Aaron Higbee** 

[PhishMe](https://phishme.com/) 
 
[Aaron Higbee的推特](https://twitter.com/higbee) 
 
[Aaron Higbee在LinkedIn上的个人资料](https://www.linkedin.com/in/aaron-higbee-6098781) 

[Aaron Higbee的PhishMe博客](https://phishme.com/author/aaronh/) 

**Benild Joseph** 

[Benild Joseph在LinkedIn上的个人资料](https://www.linkedin.com/in/benild) 
 
[Benild Joseph的Google+站点](https://plus.google.com/1076000977183424443394) 

[Benild Joseph的关于和Hacker5项目的YouTube视频](http://www.youtube.com/watch?v=BH_BNXfj0pQ) 

**分布式拒绝服务(Distributed Denial of Service,DDoS)** 

[了解DNS放大攻击的更多信息](http://technet.microsoft.com/en-us/security/hh9772393.aspx) 

了解DDoS攻击的详细信息
- [incapsula.com](https://www.incapsula.com/ddos/ddos-attack/) 

- [ddos-types](https://javapipe.com/ddos-types/) 
 
- [Denial-of-service_attack](https://en.wikipedia.org/wiki/Denial-of-service_attack) 

[Low Orbit Ion Cannon](https://sourceforge.net/project/loic0/) 

[DLR](https://sourceforge.net/projects/dlr/) 

[Hulk](https://packetstormsecurity.com/files/112856/HULK-Http-Unbearable-Load-King.html) 

**抗DDoS服务** 
[Imperva](https://www.incapsula.com/) 

[Prolexic/Akamai](http://www.prolexic.com/) 
 
**Brian Krebs** 
[Brian Krebs的个人博客](https://krebsonsecurity.com/) 

**操作系统** 

[OpenBSD](http://www.openbsd.org/) 

[Qubes](https://www.qubes-or.org/) 
 
[行业联盟：可信计算组织](https://trustedcomputinggroup.org/) 

[FIDO联盟](https://fidoalliance.org/) 

**Joanna Rutkowska** 

[2006年发布一个终极版恶意Rootkit程序](http://theinvisiblethings.blogspot.com/2006/06/introducing-blue-pill.html) 
 
[Invisible Things Lab网站](http://Invisiblethingslab.com) 
 
[Rutkowska的博客](https://blog.invisiblethings.org) 

**Aaron Margosis** 

[OpenBSD](https://www.freebsd.org/) 

[CIS(Center for Internet Security)](https://www.cisecurity.org/) 

[Aaron Margosis的Non-Admin，App-Compat and Sysinternals Weblog:](https://blogs.msdn.microsoft.com/Aaron_Margosis) 

[Aaron Margosis的US Government Configuration Baseline(USGCB)技术博客：](https://blogs.technet.microsoft.com/fdcc) 

[Aaron Margosis的Microsoft Security Guidance的博客:](https://blogs.technet.microsoft.com/SecGuide) 

**Laura Chappell** 

[Chappell大学:](https://www.chappellu.com/) 

[Chappell推特:](https://twitter.com/LauraChappell) 

[Laura Chappell实验室博客(已过时，但仍有价值)](http://laura-chappell.blogspot.com/) 

下面是一些公开分享IoT攻击的例子，内容十分有趣：
- [avast](https://www.avast.com/2015/11/11/the-anatonmy-of-an-iot-hack/) 

- [rapid7](https://www.rapid7.com/docs/Hacking-IoT-A-Case-Study-on-Baby-Monitor-Exposures-and-Vulnerabilities.pdf) 

- [securelist](https://securelist.com/analysis/publications/66207/iot-how-i-hacked-my-home/) 

- [infosecinsitute](http://resources.infosecinstitute.com/hardware-hacking-iot-devices-offensive-iot-exploitation/) 


[IoT Village](https://www.iotvillage.org/) 

[San Francisco IoT Hacking Meetup](https://www.meetup.com) 

**Charlie Miller博士** 

[Miller和Valasek写了一篇详细的白皮书“汽车网络的控制单元的探险”](http://illmatics.com/car_hacking.pdf) 
 
[Pwn2Own黑客竞赛](https://en.wikipedia.org/wiki/Pwn2Own) 

[黑帽大会](http://blackhat.com/) 
 
[微软的模糊测试](https://www.microsoft.com/en-us/springfield/) 

[Charlie Miller博士的推特](https://twitter.com/0xcharlie) 

[Charlie Miller博士的著作](https://www.amazon.com/Charlie-Miller/e/B0085NZ1PS/) 

[Adventures in Automotive Networks and Control Units白皮书：](http://illmatics.com/car_hacking.pdf) 

[Car Hacking:For Poories白皮书：](http://illmatics.com/car_hacking_poories.pdf) 

[NIST网络安全框架](https://www.nist.gov/cyberframework) 

**Jine de Jong-Chen** 

[Jine de Jong-Chen的Microsoft博客](http://blogs.microsoft.com/microsoftsecure/author/jingdejongchen/) 

**SDL(Security Development Lifecycle, 安全开发生命周期)**  

**Adam Shostack** 

[飞客蠕虫病毒(Conficker)](https://en.wikipedia.org/wiki/Conficker) 

[Adam Shostack的网站](https://adam.shostack.org/) 

**Stephen Northcutt** 

[Tenable](http://www.tenable.com) 和SourceFire

[SANS协会](http://www.sans.org) 

[SANS的网上简报](https://www.sans.org/newsletters/) 

[EFF(电子前沿基金会)](https://www.eff.org/) 

[EPIC(电子隐私信息中心)](https://epic.org/) 

[Bruce Schneier ](https://www.schneier.com/) 

[Tor](https://www.torproject.org/) 

[DuckDuckGo互联网搜索引擎](https://duckduckgo.com/) 

**Window Snyder** 

[Window Snyder在推特上的主页](https://twitter.com/window) 
 
[WordPress搭建个人博客](http://www.wordpress.com) 

[Mark Minasi 是个IT作家](http://www.minasi.com) 

**Fahmida Y. Rashid** 

[Fahmida Y. Rashid在InfoWorld发表的文章](http://www.infoworld.com/author/Fahmida-Y.-Rashid/) 

["攻击我吧"网站](https://www.hackthissite.org/) 

["HackerSpaces网站"](http://hackerspaces.org/wiki) 
 
**漏洞赏金计划(Bug Bounty Programs)** 

[Microsoft的漏洞赏金计划:](https://technet.microsoft.com/en-us/library/dn425036.aspx) 
[Google的漏洞赏金计划:](https://www.google.com/about/appsecurity/reward-program/) 

[Mozilla的漏洞赏金计划:](https://www.mozilla.org/en-US/security/bug-bounty/) 

[HackerOne](https://www.hackerone.com) 
 
[树莓派硬件入侵工具包](https://www.raspberrypi.org) 

[Arduino](https://www.arduino.cc) 

[RoboRealm](http://www.roborealm.com/clubs/list.php) 

[Arrick Robotics](http://arrickrobotics.com/clubs.html) 

[CTF](https://ctftime.org/) 

--------
**ENDING!** 

