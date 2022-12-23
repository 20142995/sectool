# 更新于 2022-12-23 09:02:20

## 近30天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
|2022-12-21 09:25:38|[afrog](https://github.com/zan8in/afrog)|v2.1.1|- Fixed a bug with high false positives<br> in fingerprint- Added optional -json op<br>tion for write output in JSON format, eg<br>: -json result.json|
|2022-12-18 08:14:24|[HaE](https://github.com/gh0stkey/HaE)|2.4.5|HaE 2.4.5 更新内容：1. 在线更新配置信息<br>功能添加提示框，防止用户误触导致配置被更<br>新：#91；2. 数据聚合查询面板添加支持通配<br>符域名查找：#88；3. 数据聚合查询面板添加<br>清空数据功能，便于用户查看最新数据；4. 新<br>增规则作用域：any header（请求与响应头）<br>、any body（请求与响应主体）。|
|2022-12-15 11:47:23|[super-xray](https://github.com/4ra1n/super-xray)|0.9|## 0.9一个bug修复版本，目前功能基本完善<br>Bugs:- [important] [bug] showMessageDial<br>og多屏情况下的位置问题 #76- [important] <br>[bug] 反连平台应该自动配置client属性否则<br>会失效 #72- [important] [bug] 当reverse配<br>置为空但确认配置后无法正常启动 #71- [bug]<br> 高级配置的某个ui绑定错误 #79- [bug] 在<br>线生成的翻译问题 #75 (另外修复多处翻译问<br>题)Others:- [feat] 不输入端口情况下不应该<br>允许开启被动扫描 #77- 构建的System JRE EX<br>E应该对JRE版本进行限制 #73- 打开扫描结果<br>为空时应该给一个提示 #78- 添加一个按钮允<br>许用户清除PoC的设置 #80|
|2022-12-14 01:54:06|[captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified)|0.19|【2022-12-14】 0.191. 增加URL解码、过滤<br>图片编码中的.，#20 感谢@yinanzhaobaima 师<br>傅反馈|
|2022-12-13 03:32:05|[pocsuite3](https://github.com/knownsec/pocsuite3)|v2.0.2|* 修复 _check 方法中 url 重定向的问题 #<br>337* 修复 console 模式下 use 命令使用绝<br>对路径的问题 #341，thanks @S2eTo* 修复 bu<br>ild_url 兼容 ipv6 的问题 #347，thanks @H<br>omerQing* 优化 nuclei DSL 表达式执行 #34<br>8----------------* fix url redirect prob<br>lem in _check method #337* fix use comma<br>nd in console mode can't use absolute pa<br>th #341, thanks @S2eTo* fix ipv6 compati<br>bility issue in build_url #347, thanks @<br>HomerQing* optimize dsl expression execu<br>tion #348|
|2022-12-11 13:04:41|[nuclei](https://github.com/projectdiscovery/nuclei)|v2.8.3|## What's Changed* Fixed bug to conside<br>r clustering with automatic http probing<br> by @Ice3man543 in https://github.com/pr<br>ojectdiscovery/nuclei/pull/3019* Fixed b<br>ug to remove blank protocol name by @vza<br>manillo in https://github.com/projectdis<br>covery/nuclei/pull/2993* Added option to<br> disable request clustering by @Ice3man5<br>43in https://github.com/projectdiscovery<br>/nuclei/pull/3019* Added custom ip to pr<br>otocol-generated variables by @Mzack9999<br> in https://github.com/projectdiscovery/<br>nuclei/pull/3011**Full Changelog**: http<br>s://github.com/projectdiscovery/nuclei/c<br>ompare/v2.8.2...v2.8.3|
|2022-12-09 01:31:39|[log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner)|0.21.0|# 0.21.0 更新## 2022-12-91. 增加参数 pr<br>efixparam前缀可控，可输入如%84$，造成一<br>些数据库组件解析错误，从而进行log4j2的报<br>错触发2. 增加自定义header头获取响应结果请<br>求(支持了dnslog.cn等，但是dnslog.cn有PHPS<br>ESSID默认过期时间，暂不推荐使用)，举例如<br> privatednsResponseurl 框内填入以下字段<br>：HEADERhttp://dnslog.cn/getrecords.phpCo<br>okie:PHPSESSID=bmekedlvumo1e9onr6qsd1j2u<br>63. 修复dnsparam参数初始化问题，感谢微信<br>群@啊哈师傅反馈|
|2022-12-02 08:08:53|[github-subdomains](https://github.com/gwen001/github-subdomains)|v1.2.0||
|2022-11-30 19:12:53|[faker](https://github.com/joke2k/faker)|v15.3.4|See [CHANGELOG.md](https://github.com/j<br>oke2k/faker/blob/refs/tags/v15.3.4/CHANG<br>ELOG.md).|
|2022-11-28 17:47:44|[Behinder](https://github.com/rebeyond/Behinder)|Behinder_<br>v4.0.6|### 2022.11.28 v4.0.6 更新日志1.修复了T<br>omcat10中内存马植入无法连接的问题；2.修<br>复了asp版本内置传输协议的连接问题；3.修复<br>了传输协议在恢复默认时会出现错误的问题；4<br>.内置了Javafx库，修复了各类因为Javafx环<br>境无法运行的问题；5.修复了客户端兼容性问<br>题，客户端兼容Java8至Java19；6.新增“默认<br>”连接模式，兼容冰蝎3默认服务端；7.其他的<br>一些优化。|
|2022-11-28 08:58:17|[RequestTemplate](https://github.com/1n7erface/RequestTemplate)|v1.1.0|2022.11.28 17:00这一次更新时隔一个月,我<br>还是只更新了Golang的扫描端。我觉得这次更<br>新是我迄今为止最满意的一次更新，因为我将<br>程序的架构进行了翻新重构。解决了很多在以<br>往我觉得是"bug"的细节，虽然在运行时不会出<br>现异常，但是架构始终让我不太满意。这次我<br>在爆破模块与端口扫描增加了“调度中心“的<br>角色。详细的细节我可能会发文章叙述。各位<br>及时给出评价。注：mac在更新13之后不能使用<br>压缩过后的文件，不知道为啥，在此我提供未<br>压缩的文件。见：App-arm64darwin-noupx、Ap<br>p-am d64darwin-noupx|
|2022-11-23 03:58:28|[BpScan](https://github.com/EASY233/BpScan)|1.0.0|1、修复log4j poc编码问题2、修复dnslog平<br>台请求错误的问题3、其他bug修复|
## 近30天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
|2022-12-23 01:00:16|[NucleiTP](https://github.com/ExpLangcn/NucleiTP)|更新啦❤️|
|2022-12-22 20:47:31|[PocOrExp_in_Github](https://github.com/ycdxsb/PocOrExp_in_Github)|update 2022-12-23 04:47:30|
|2022-12-22 03:22:36|[afrog](https://github.com/zan8in/afrog)|afrog-pocs 1.7.8|
|2022-12-21 21:23:19|[RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)|Update logging.StreamHandler to use sys.stderr instead<br> of sys.stdout|
|2022-12-21 20:15:18|[wpscan](https://github.com/wpscanteam/wpscan)|Updates DFs|
|2022-12-21 11:49:36|[super-xray](https://github.com/4ra1n/super-xray)|UI BUG|
|2022-12-21 02:53:43|[All-Defense-Tool](https://github.com/guchangan1/All-Defense-Tool)|更新v2.1|
|2022-12-20 09:22:50|[svnExploit](https://github.com/admintony/svnExploit)|Do not verify the certificate取消对https证书的校验，防<br>止一些https自签名证书dump失败|
|2022-12-19 06:40:20|[404StarLink](https://github.com/knownsec/404StarLink)|weekly update at 2022-12-19|
|2022-12-18 08:12:16|[HaE](https://github.com/gh0stkey/HaE)|Version: 2.4.5 Update|
|2022-12-18 06:06:34|[Threathunting-book](https://github.com/12306Bro/Threathunting-book)|Update README.md|
|2022-12-17 09:57:34|[poc-hub](https://github.com/ybdt/poc-hub)|Update .gitignore|
|2022-12-14 12:09:50|[feroxbuster](https://github.com/epi052/feroxbuster)|Merge pull request #734 from epi052/all-contributors/a<br>dd-kmancdocs: add kmanc as a contributor for bug, and c<br>ode|
|2022-12-14 05:55:42|[vulnerability](https://github.com/lal0ne/vulnerability)|CVE-2022-46169|
|2022-12-14 03:27:29|[captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified)|Update FAQ.md|
|2022-12-13 07:14:54|[Library-POC](https://github.com/luck-ying/Library-POC)|Update README.md|
|2022-12-13 03:25:37|[pocsuite3](https://github.com/knownsec/pocsuite3)|Merge pull request #349 from 13ph03nix/masterchore: bu<br>mp version to 2.0.2|
|2022-12-11 13:00:15|[nuclei](https://github.com/projectdiscovery/nuclei)|Merge pull request #3021 from projectdiscovery/devBugf<br>ix release|
|2022-12-11 11:22:06|[penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit)|Update README.md|
|2022-12-11 11:22:06|[penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit)|Update README.md|
|2022-12-09 11:22:09|[dirsearch](https://github.com/maurosoria/dirsearch)|Merge pull request #1255 from kylincodelab/masterUpdat<br>e dicc.txt|
|2022-12-09 07:10:04|[log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner)|Update FAQ-zh-CN.md|
|2022-12-09 02:48:45|[Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki)|更新漏洞|
|2022-12-09 02:47:17|[Awesome-POC](https://github.com/Threekiii/Awesome-POC)|更新漏洞|
|2022-12-08 13:37:18|[InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll)|Update README.md|
|2022-12-07 21:02:53|[ffuf](https://github.com/ffuf/ffuf)|Fix the ac for good now (#615)|
|2022-12-06 07:29:11|[OneForAll](https://github.com/shmilylty/OneForAll)|回退|
|2022-12-05 16:15:52|[OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL)|Update README.md|
|2022-12-05 09:54:29|[Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam)|图片本地化|
|2022-12-05 03:27:07|[Vulhub-Reproduce](https://github.com/Threekiii/Vulhub-Reproduce)|更新README.md|
|2022-12-03 07:13:38|[RedisEXP](https://github.com/yuyan-sec/RedisEXP)|Update tools.go|
|2022-12-02 08:08:51|[github-subdomains](https://github.com/gwen001/github-subdomains)|v1.2.0|
|2022-12-02 06:41:15|[TomatoTools](https://github.com/ht0Ruial/TomatoTools)|fix #7|
|2022-12-01 14:41:27|[BurpSuite-collectio<br>ns](https://github.com/Mr-xn/BurpSuite-collections)|add passive-scan-client 维护分支|
|2022-12-01 07:55:41|[RequestTemplate](https://github.com/1n7erface/RequestTemplate)|Update README.md|
|2022-11-30 19:12:19|[faker](https://github.com/joke2k/faker)|Bump version: 15.3.3 → 15.3.4|
|2022-11-29 10:47:06|[QingTing](https://github.com/StarCrossPortal/QingTing)|蜻蜓v2|
|2022-11-29 02:41:57|[aksk_tool](https://github.com/wyzxxz/aksk_tool)|Update README.md|
|2022-11-27 07:02:42|[knife](https://github.com/bit4woo/knife)|update|
|2022-11-25 11:42:34|[BpScan](https://github.com/EASY233/BpScan)|update|## 所有项目
### 信息收集
#### 资产测绘采集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll) | V1.2 | 为了方便安全从业人员在使用网络测绘平台进行信息搜集时的效率，本程<br>序集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并且合<br>并展示及导出。 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | v2.3.2 | 【支持Fofa、Zoomeye、Quake等网络空间搜索引擎】闪电搜索器；GUI图<br>形化渗透测试信息搜集工具；资产搜集引擎 |
#### 子域名收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [subfinder](https://github.com/projectdiscovery/subfinder) | v2.5.5 | Subfinder is a subdomain discovery tool that discovers valid sub<br>domains for websites. Designed as a passive framework to be usefu<br>l for bug bounties and safe for penetration testing. |
| [ksubdomain](https://github.com/knownsec/ksubdomain) | v0.7 | 无状态子域名爆破工具 |
| [OneForAll](https://github.com/shmilylty/OneForAll) | v0.4.5 | OneForAll是一款功能强大的子域收集工具 |
| [LangSrcCurise](https://github.com/LangziFun/LangSrcCurise) |  | SRC子域名资产监控 |
| [github-subdomains](https://github.com/gwen001/github-subdomains) | v1.2.0 | Find subdomains on GitHub. |
| [LayerDomainFinder](https://github.com/euphrat1ca/LayerDomainFinder) | 3 | Layer子域名挖掘机 |
| [dnsub](https://github.com/yunxu1/dnsub) | v2.1 | dnsub一款好用且强大的子域名扫描工具 |
#### 目录扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dirsearch](https://github.com/maurosoria/dirsearch) | v0.4.3 | Web path scanner |
| [URLFinder](https://github.com/pingc0y/URLFinder) |  | 类似JSFinder的golang实现，一款用于快速提取检测页面中JS与URL的工<br>具，更快更全更舒服 |
| [feroxbuster](https://github.com/epi052/feroxbuster) | v2.7.2 | A fast, simple, recursive content discovery tool written in Rust<br>. |
| [ffuf](https://github.com/ffuf/ffuf) | v1.5.0 | Fast web fuzzer written in Go |
| [dirmap](https://github.com/H4ckForJob/dirmap) |  | An advanced web directory & file scanning tool that will be more<br> powerful than DirBuster, Dirsearch, cansina, and Yu Jian.一个高<br>级web目录、文件扫描工具，功能将会强于DirBuster、Dirsearch、cansina<br>、御剑。 |
| [cansina](https://github.com/deibit/cansina) | 1.0.0 | Web Content Discovery Tool |
| [urlbrute](https://github.com/ReddyyZ/urlbrute) | v1.0.2 | Directory/Subdomain scanner developed in GoLang. |
| [yjdirscan](https://github.com/foryujian/yjdirscan) | yjdirscan | 御剑目录扫描专业版，简单实用的命令行网站目录扫描工具，支持爬虫、<br>fuzz、自定义字典、字典变量、UA修改、假404自动过滤、扫描控速等功能<br>。 |
| [yuhScan](https://github.com/hunyaio/yuhScan) | v1.0 | web目录快速扫描工具 |
| [gospider](https://github.com/jaeles-project/gospider) | v1.1.6 | Gospider - Fast web spider written in Go |
| [rad](https://github.com/chaitin/rad) | 0.4 |  |
#### 指纹识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EHole](https://github.com/EdgeSecurityTeam/EHole) | 3.0 | EHole(棱洞)3.0 重构版-红队重点攻击系统指纹探测工具 |
#### 端口扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [TXPortMap](https://github.com/4dogs-cn/TXPortMap) | v1.1.2 | Port Scanner & Banner Identify From TianXiang |
| [naabu](https://github.com/projectdiscovery/naabu) | v2.1.1 | A fast port scanner written in go with a focus on reliability an<br>d simplicity. Designed to be used in combination with other tools<br> for attack surface discovery in bug bounties and pentests |
#### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dismap](https://github.com/zhzyker/dismap) | v0.4 | Asset discovery and identification tools 快速识别 Web 指纹信息，<br>定位资产类型。辅助红队快速定位目标资产信息，辅助蓝队发现疑似脆弱点 |
### 漏洞发现&利用
#### 半自动化漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [railgun](https://github.com/lz520520/railgun) | v1.4.6 |  |
| [Goby](https://github.com/gobysec/Goby) | Beta1.9.3<br>25 | Attack surface mapping |
#### 半自动漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EasyPen](https://github.com/lijiejie/EasyPen) |  | EasyPen is a GUI program which helps pentesters do target discov<br>ery, vulnerability scan and exploitation |
| [xray](https://github.com/chaitin/xray) | 1.9.3 | 一款完善的安全评估工具，支持常见 web 安全问题扫描和自定义 poc | <br>使用之前务必先阅读文档 |
| [w13scan](https://github.com/w-digital-scanner/w13scan) |  | Passive Security Scanner (被动式安全扫描器) |
| [Fvuln](https://github.com/d3ckx1/Fvuln) | Fvuln_v1.<br>4.8 | F-vuln（全称：Find-Vulnerability）是为了自己工作方便专门编写的一<br>款自动化工具，主要适用于日常安全服务、渗透测试人员和RedTeam红队人<br>员，它集合的功能包括：存活IP探测、开放端口探测、web服务探测、web漏<br>洞扫描、smb爆破、ssh爆破、ftp爆破、mssql爆破等其他数据库爆破工作以<br>及大量web漏洞检测模块。 |
| [nuclei](https://github.com/projectdiscovery/nuclei) | v2.8.3 | Fast and customizable vulnerability scanner based on simple YAML<br> based DSL. |
| [afrog](https://github.com/zan8in/afrog) | v2.1.1 | A Vulnerability Scanning Tools For Penetration Testing |
| [vulmap](https://github.com/zhzyker/vulmap) | v0.9 | Vulmap 是一款 web 漏洞扫描和验证工具, 可对 webapps 进行漏洞扫描,<br> 并且具备漏洞验证功能 |
| [POC-bomber](https://github.com/tr0uble-mAker/POC-bomber) | v2.0.2-PO<br>C-bomber | 利用大量高威胁poc/exp快速获取目标权限，用于渗透和红队快速打点 |
| [QingTing](https://github.com/StarCrossPortal/QingTing) | v0.3 | 蜻蜓安全一个安全工具编排平台,可以自由编排你的工具流,集成108款工<br>具,包括xray、nmap、awvs等;你可以将喜欢的工具编排成一个场景，快速打<br>造适合自己的安全工作台~ |
#### 漏洞扫描框架
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pocsuite3](https://github.com/knownsec/pocsuite3) | v2.0.2 | pocsuite3 is an open-sourced remote vulnerability testing framew<br>ork developed by the Knownsec 404 Team. |
| [Godscan](https://github.com/Guoke324/Godscan) | Godscan | Godscan 是一款python编写的具有图形化界面的漏洞检测框架，可以之定<br>义漏洞检测 poc ，主要是帮助安全测试者，更好的去记录和整理历史漏洞<br>，以便更好的进行漏洞检测，提高工作效率！ |
| [FrameScan-GUI](https://github.com/qianxiao996/FrameScan-GUI) | v1.4.2 | FrameScan-GUI 一款python3和Pyqt编写的具有图形化界面的cms漏洞检测<br>框架。 |
#### 数据库利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [MDUT](https://github.com/SafeGroceryStore/MDUT) | v2.1.1 | MDUT - Multiple Database Utilization Tools |
| [SharpSQLTools](https://github.com/uknowsec/SharpSQLTools) | 41 | SharpSQLTools 和@Rcoil一起写的小工具，可上传下载文件，xp_cmdshel<br>l与sp_oacreate执行命令回显和clr加载程序集执行相应操作。 |
| [mssqlproxy](https://github.com/blackarrowsec/mssqlproxy) | 0.1 | mssqlproxy is a toolkit aimed to perform lateral movement in res<br>tricted environments through a compromised Microsoft SQL Server v<br>ia socket reuse |
| [odat](https://github.com/quentinhardy/odat) | 5.1.1 | ODAT: Oracle Database Attacking Tool |
| [redis-rogue-server](https://github.com/n0b0dyCN/redis-rogue-server) |  | Redis(<=5.0.5) RCE |
| [redis-rce](https://github.com/Ridter/redis-rce) |  | Redis 4.x/5.x RCE |
| [RedisEXP](https://github.com/yuyan-sec/RedisEXP) |  | Redis 漏洞利用工具 |
| [redis_rce](https://github.com/zyylhn/redis_rce) | v0.1.0 | Redis primary/secondary replication RCE |
| [RequestTemplate](https://github.com/1n7erface/RequestTemplate) | v1.1.0 | 双语双端内网扫描以及验证工具 |
#### Shell管理
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Behinder](https://github.com/rebeyond/Behinder) | Behinder_<br>v4.0.6 | “冰蝎”动态二进制加密网站管理客户端 |
| [Godzilla](https://github.com/BeichenDream/Godzilla) | v4.0.1-go<br>dzilla | 哥斯拉 |
#### 中间件&框架漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [AttackTomcat](https://github.com/tpt11fb/AttackTomcat) | V1 | Tomcat漏洞利用工具 |
| [SpringExploit](https://github.com/SummerSec/SpringExploit) | 0.1.9 | 🚀 一款为了学习go而诞生的漏洞利用工具 |
| [shiro_rce_tool](https://github.com/wyzxxz/shiro_rce_tool) |  | shiro 反序列 命令执行辅助检测工具 |
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2) | 4.5.6 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原<br>版中NoCC的问题 https://github.com/j1anFen/shiro_attack |
| [shiro_attack](https://github.com/j1anFen/shiro_attack) | 2.2 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马） |
| [FastjsonExploit](https://github.com/c0ny1/FastjsonExploit) |  | Fastjson vulnerability quickly exploits the framework（fastjson<br>漏洞快速利用框架） |
| [fastjson_rec_exploi<br>t](https://github.com/mrknow001/fastjson_rec_exploit) |  | fastjson一键命令执行 |
| [jexboss](https://github.com/joaomatosf/jexboss) |  | JexBoss: Jboss (and Java Deserialization Vulnerabilities) verify<br> and EXploitation Tool |
| [weblogic-framework](https://github.com/dream0x01/weblogic-framework) | v0.2.3 | weblogic-framework is the best tool for detecting weblogic vulne<br>rabilities. |
| [dubbo-exp](https://github.com/threedr3am/dubbo-exp) |  | dubbo学习demo，之前删了，重新上传。 |
| [STS2G](https://github.com/xfiftyone/STS2G) | 1.0 | Struts2漏洞扫描利用工具 - Golang版. Struts2 Scanner Written in G<br>olang |
| [Struts2-Scan](https://github.com/HatBoy/Struts2-Scan) |  | Struts2全漏洞扫描利用工具 |
| [log4j-shell-poc](https://github.com/kozmer/log4j-shell-poc) |  | A Proof-Of-Concept for the CVE-2021-44228 vulnerability.  |
| [SpringBootExploit](https://github.com/0x727/SpringBootExploit) | 1.3 | 项目是根据LandGrey/SpringBootVulExploit清单编写，目的hvv期间快速<br>利用漏洞、降低漏洞利用门槛。 |
#### 中间件&框架漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WeblogicScan](https://github.com/rabbitmask/WeblogicScan) |  | Weblogic一键漏洞检测工具，V1.5，更新时间：20200730 |
| [weblogic-infodetect<br>or](https://github.com/woodpecker-appstore/weblogic-infodetector) | 0.2.4 | woodpecker框架weblogic信息探测插件 |
| [Jiraffe](https://github.com/0x48piraj/Jiraffe) | v2.0.6 | One stop place for exploiting Jira instances in your proximity |
| [Artillery](https://github.com/Weik1/Artillery) | v1.0_2022<br>0519 | JAVA 插件化漏洞扫描器，Gui基于javafx。POC 目前集成 Weblogic、Tom<br>cat、Shiro、Spring等。 |
#### 漏洞利用辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jndi_tool](https://github.com/wyzxxz/jndi_tool) |  | JNDI服务利用工具 RMI/LDAP，支持部分场景回显、内存shell，高版本JD<br>K场景下利用等，fastjson rce命令执行，log4j rce命令执行 漏洞检测辅<br>助工具 |
| [ysoserial](https://github.com/frohoff/ysoserial) | v0.0.6 | A proof-of-concept tool for generating payloads that exploit uns<br>afe Java object deserialization. |
| [Gopherus](https://github.com/tarunkant/Gopherus) |  | This tool generates gopher link for exploiting SSRF and gaining <br>RCE in various servers |
#### 重点CMS利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL) | v0.6 | OA综合利用工具，集合将近20款OA漏洞批量扫描 |
| [seeyon_exp](https://github.com/Summer177/seeyon_exp) |  | 致远OA综合利用工具 |
| [SeeyonExploit-GUI](https://github.com/God-Ok/SeeyonExploit-GUI) |  | 致远OA综合利用工具V1.0 |
| [TDOA_RCE](https://github.com/xinyu2428/TDOA_RCE) | v1.0 | 通达OA综合利用工具 |
| [LandrayExploit](https://github.com/yuanhaiGreg/LandrayExploit) | 1.1 | 蓝凌OA漏洞利用工具/前台无条件RCE/文件写入 |
| [weaver_exp](https://github.com/z1un/weaver_exp) |  | 泛微OA漏洞综合利用脚本 |
| [EgGateWayGetShell](https://github.com/Tas9er/EgGateWayGetShell) |  | Code By:Tas9er |
| [CMSmap](https://github.com/Dionach/CMSmap) |  | CMSmap is a python open source CMS scanner that automates the pr<br>ocess of detecting security flaws of the most popular CMSs.  |
| [wprecon](https://github.com/blackbinn/wprecon) |  |  |
| [wordpress-exploit-f<br>ramework](https://github.com/rastating/wordpress-exploit-framework) | v2.0.1 | A Ruby framework designed to aid in the penetration testing of W<br>ordPress systems.  |
| [wpscan](https://github.com/wpscanteam/wpscan) | v3.8.22 | WPScan WordPress security scanner. Written for security professi<br>onals and blog maintainers to test the security of their WordPres<br>s websites. |
| [wprecon](https://github.com/AngraTeam/wprecon) | 2.4.5 | WPRecon, is a tool for the recognition of vulnerabilities and bl<br>ackbox information for wordpress. |
| [Aazhen-RexHa](https://github.com/zangcc/Aazhen-RexHa) | Aazhen-Re<br>xHa_Scanne<br>r | 自研JavaFX图形化漏洞扫描工具，支持扫描的漏洞分别是： ThinkPHP-2.<br>x-RCE， ThinkPHP-5.0.23-RCE， ThinkPHP5.0.x-5.0.23通杀RCE， Think<br>PHP5-SQL注入&敏感信息泄露， ThinkPHP 3.x 日志泄露NO.1， ThinkPHP <br>3.x 日志泄露NO.2， ThinkPHP 5.x 数据库信息泄露的漏洞检测，以及批<br>量检测的功能。漏洞POC基本适用ThinkPHP全版本漏洞。 |
| [ThinkphpGUI](https://github.com/Lotus6/ThinkphpGUI) | 1.3 | Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，getsh<br>ell。 |
| [thinkphp_gui_tools](https://github.com/bewhale/thinkphp_gui_tools) | v2.4.2 | ThinkPHP漏洞综合利用工具, 图形化界面, 命令执行, 一键getshell, 批<br>量检测, 日志遍历, session包含,宝塔绕过 |
#### 信息泄露利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Cloud-Bucket-Leak-D<br>etection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | v0.4.0 | 六大云存储，泄露利用检测工具 |
| [aksk_tool](https://github.com/wyzxxz/aksk_tool) |  | AK资源管理工具，阿里云/腾讯云/华为云/AWS/UCLOUD/京东云/七牛云存<br>储AccessKey AccessKeySecret，利用AK获取资源信息和操作资源，ECS/CVM<br>/E2/UHOST/ECI执行命令，OSS/COS/S3管理，RDS/DB管理，域名管理，添加<br>RAM/CAM/IAM账号等 |
| [swagger-exp](https://github.com/lijiejie/swagger-exp) |  | A Swagger API Exploit |
| [swagger-hack](https://github.com/jayus0821/swagger-hack) |  | 自动化爬取并自动测试所有swagger接口 |
| [heapdump_tool](https://github.com/wyzxxz/heapdump_tool) |  | heapdump敏感信息查询工具，例如查找 spring heapdump中的密码明文，<br>AK,SK等 |
| [Packer-Fuzzer](https://github.com/rtcatc/Packer-Fuzzer) | v1.4 | Packer Fuzzer is a fast and efficient scanner for security detec<br>tion of websites constructed by javascript module bundler such as<br> Webpack.  |
| [GitHack](https://github.com/BugScanTeam/GitHack) |  | .git 泄漏利用工具，可还原历史版本 |
| [dvcs-ripper](https://github.com/kost/dvcs-ripper) |  | Rip web accessible (distributed) version control systems: SVN/GI<br>T/HG... |
| [ds_store_exp](https://github.com/lijiejie/ds_store_exp) |  | A .DS_Store file disclosure exploit.It parses .DS_Store file and<br> downloads files recursively. |
| [svnExploit](https://github.com/admintony/svnExploit) |  | SvnExploit支持SVN源代码泄露全版本Dump源码 |
| [git-dumper](https://github.com/arthaud/git-dumper) |  | A tool to dump a git repository from a website |
| [GitDorker](https://github.com/obheda12/GitDorker) |  | A Python program to scrape secrets from GitHub through usage of <br>a large repository of dorks. |
| [SecretFinder](https://github.com/m4ll0k/SecretFinder) |  | SecretFinder - A python script for find sensitive data (apikeys,<br> accesstoken,jwt,..) and search anything on javascript files  |
| [JSFScan.sh](https://github.com/KathanP19/JSFScan.sh) |  | Automation for javascript recon in bug bounty.  |
| [SubOver](https://github.com/Ice3man543/SubOver) | v1.2 | A Powerful Subdomain Takeover Tool |
| [JDumpSpider](https://github.com/whwlsfb/JDumpSpider) |  | HeapDump敏感信息提取工具 |
#### 口令爆破
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [goon](https://github.com/i11us0ry/goon) | v3.5 | goon,集合了fscan和kscan等优秀工具功能的扫描爆破工具。功能包含：i<br>p探活、port扫描、web指纹扫描、title扫描、压缩文件扫描、fofa获取、<br>ms17010、mssql、mysql、postgres、redis、ssh、smb、rdp、telnet、to<br>mcat等爆破以及如netbios探测等功能。 |
| [SNETCracker](https://github.com/shack2/SNETCracker) | 1.0.20190<br>715 | 超级弱口令检查工具是一款Windows平台的弱口令审计工具，支持批量多<br>线程检查，可快速发现弱密码、弱口令账号，密码支持和用户名结合进行检<br>查，大大提高成功率，支持自定义服务端口和字典。 |
| [web-brutator](https://github.com/koutto/web-brutator) |  | Fast Modular Web Interfaces Bruteforcer |
| [WebCrack](https://github.com/yzddmr6/WebCrack) |  | WebCrack是一款web后台弱口令/万能密码批量检测工具，在工具中导入后<br>台地址即可进行自动化检测。 |
| [ssb](https://github.com/pwnesia/ssb) | v0.1.1 | Secure Shell Bruteforcer — A faster & simpler way to bruteforce<br> SSH server |
#### 漏洞检测利用仓库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [poc-hub](https://github.com/ybdt/poc-hub) |  | 漏洞复现、漏洞检测 |
| [Awesome-Exploit](https://github.com/Threekiii/Awesome-Exploit) |  | 一个漏洞利用工具仓库 |
| [exphub](https://github.com/zhzyker/exphub) |  | Exphub[漏洞利用脚本库] 包括Webloigc、Struts2、Tomcat、Nexus、Sol<br>r、Jboss、Drupal的漏洞利用脚本，最新添加CVE-2020-14882、CVE-2020-<br>11444、CVE-2020-10204、CVE-2020-10199、CVE-2020-1938、CVE-2020-25<br>51、CVE-2020-2555、CVE-2020-2883、CVE-2019-17558、CVE-2019-6340 |
| [CVE-Master](https://github.com/wjl110/CVE-Master) | v1.0.1 | 收集本人自接触渗透测试用于漏洞验证的所有热门CVE、POC、CNVD攻击有<br>效载荷+测试工具+FUZZ,一个仓库满足许多攻击测试场景,开箱即用. |
| [0day](https://github.com/helloexp/0day) |  | 各种CMS、各种平台、各种系统、各种软件漏洞的EXP、POC ,该项目将持<br>续更新 |
| [PocList](https://github.com/1n7erface/PocList) |  | Alibaba-Nacos-Unauthorized/ApacheDruid-RCE_CVE-2021-25646/MS-Exc<br>hange-SSRF-CVE-2021-26885/Oracle-WebLogic-CVE-2021-2109_RCE/RG-CN<br>VD-2021-14536/RJ-SSL-VPN-UltraVires/Redis-Unauthorized-RCE/TDOA-V<br>11.7-GetOnlineCookie/VMware-vCenter-GetAnyFile/yongyou-GRP-U8-XXE<br>/Oracle-WebLogic-CVE-2020-14883/Oracle-WebLogic-CVE-2020-14882/Ap<br>ache-Solr-GetAnyFile/F5-BIG-IP-CVE-2021-22986/Sonicwall-SSL-VPN-R<br>CE/GitLab-Graphql-CNVD-2021-14193/D-Link-DCS-CVE-2020-25078/WLAN-<br>AP-WEA453e-RCE/360TianQing-Unauthorized/360TianQing-SQLinjection/<br>FanWeiOA-V8-SQLinjection/QiZhiBaoLeiJi-AnyUserLogin/QiAnXin-WangK<br>angFirewall-RCE/金山-V8-终端安全系统/NCCloud-SQLinjection/ShowDoc<br>-RCE |
| [vulnerability](https://github.com/lal0ne/vulnerability) |  | 收集、整理、修改互联网上公开的漏洞POC |
| [Some-PoC-oR-ExP](https://github.com/coffeehb/Some-PoC-oR-ExP) |  | 各种漏洞poc、Exp的收集或编写 |
| [POChouse](https://github.com/DawnFlame/POChouse) |  | POC&EXP仓库、hvv弹药库、Nday、1day |
| [PocOrExp_in_Github](https://github.com/ycdxsb/PocOrExp_in_Github) |  | 聚合Github上已有的Poc或者Exp，CVE信息来自CVE官网。Auto Collect P<br>oc Or Exp from Github by CVE ID. |
#### 漏洞文库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [bylibrary](https://github.com/BaizeSec/bylibrary) |  | 白阁文库是白泽Sec安全团队维护的一个漏洞POC和EXP公开项目 |
| [PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book) | PeiQi-WIK<br>I-Book-202<br>2-03-20 | 面向网络安全从业者的知识文库🍃 |
| [VulWiki](https://github.com/Ares-X/VulWiki) |  | VulWiki |
| [vulbase](https://github.com/cckuailong/vulbase) |  | 各大漏洞文库合集 |
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC) |  | 一个各类漏洞POC知识库 |
| [Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki) | v1.0 | 一个综合漏洞知识库，集成了Vulhub、Peiqi、Edge、0sec、Wooyun等开<br>源漏洞库 |
| [yougar0.github.io](https://github.com/heise5yuetian/yougar0.github.io) |  | 漏洞知识库 |
| [Vulhub-Reproduce](https://github.com/Threekiii/Vulhub-Reproduce) |  | 一个Vulhub漏洞复现知识库 |
| [Report_Public](https://github.com/DVPNET/Report_Public) |  |  DVPNET 公开漏洞知识库 |
| [BUG-Pocket](https://github.com/light-Life/BUG-Pocket) |  | 小型漏洞库，提供FOFA语法及批量脚本，具体利用法请参考别的漏洞库，<br>共4种类型47项 |
| [WiKi](https://github.com/ScarecrowSec/WiKi) |  | 稻草人安全团队漏洞库 |
| [PoC-ExP](https://github.com/Cuerz/PoC-ExP) |  | 【漏洞Poc知识库】一个网络安全爱好者对网络上一些已知漏洞payload的<br>收录，持续更新。并编写了利用脚本，可用于日常学习或批量的src漏洞挖<br>掘 |
### 内网渗透
#### 密码提取
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [getIntrInfo](https://github.com/Potato-py/getIntrInfo) |  | 收集内部网信息。包括：浏览器书签、密码和浏览历史记录、cookie。Wi<br>fi信息和密码。主机信息。 |
| [FinalShell-Decoder](https://github.com/passer-W/FinalShell-Decoder) | V1.0 | FinallShell 密码解密GUI工具 |
| [Xdecrypt](https://github.com/dzxs/Xdecrypt) |  | Xshell Xftp password decrypt |
### 相关资源
#### 工具集成环境
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先<br>利其器。 |
#### 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先<br>利其器。 |
| [Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam) |  | 一个红队知识仓库 |
| [Threathunting-book](https://github.com/12306Bro/Threathunting-book) |  | Threat hunting Web Windows AD linux ATT&CK TTPs |
| [PenetrationTesttips](https://github.com/CYJoe-Cyclone/PenetrationTesttips) |  | 渗透测试Tips - Version1.3 |
| [Intranet_Penetratio<br>n_Tips](https://github.com/Ridter/Intranet_Penetration_Tips) |  | 2018年初整理的一些内网渗透TIPS，后面更新的慢，所以整理出来希望跟<br>小伙伴们一起更新维护~ |
#### 优秀项目集合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [404StarLink](https://github.com/knownsec/404StarLink) |  | 404StarLink - 推荐优质、有意义、有趣、坚持维护的安全开源项目 |
| [Scanners-Box](https://github.com/We5ter/Scanners-Box) |  | A powerful and open-source toolkit for hackers and security auto<br>mation - 安全行业从业者自研开源扫描器合辑 |
| [All-Defense-Tool](https://github.com/guchangan1/All-Defense-Tool) |  | 本项目集成了全网优秀的攻防武器工具项目，包含自动化利用，子域名、<br>目录扫描、端口扫描等信息收集工具，各大中间件、cms漏洞利用工具，爆<br>破工具、内网横向及免杀、社工钓鱼以及应急响应等资料。 |
| [About-Attack](https://github.com/lintstar/About-Attack) |  | 一个旨在通过应用场景 / 标签对 Github 红队向工具 / 资源进行分类收<br>集，降低红队技术门槛的手册【持续更新】 |
| [RedTeamTools](https://github.com/FiveAourThe/RedTeamTools) |  | 分享红队常用的工具 |
### 工具&插件
#### Burpsuite
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [PowerScanner](https://github.com/NeoTheCapt/PowerScanner) | 1.1.3 | 面向HW的红队半自动扫描器 |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | RouteVulS<br>can1.3 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的bu<br>rp插件 |
| [SpringScan](https://github.com/metaStor/SpringScan) | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [BurpSuite-collectio<br>ns](https://github.com/Mr-xn/BurpSuite-collections) |  | 有关burpsuite的插件(非商店),文章以及使用技巧的收集(此项目不再提<br>供burpsuite破解文件,如需要请在博客mrxn.net下载)---Collection of bu<br>rpsuite plugins (non-stores), articles and tips for using Burpsui<br>te, no crack version file |
| [BurpShiroPassiveSca<br>n](https://github.com/pmiaowu/BurpShiroPassiveScan) | BurpShiro<br>PassiveSca<br>n-2.0.0 | 一款基于BurpSuite的被动式shiro检测插件 |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | BurpFastJ<br>sonScan-2.<br>2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [HaE](https://github.com/gh0stkey/HaE) | 2.4.5 | HaE - Highlighter and Extractor, 赋能白帽 高效作战 |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9-alph<br>a | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集；<br>快速Title获取；外部工具联动；等等 |
| [Sylas](https://github.com/Acmesec/Sylas) | 1.1.1 | 新一代子域名主/被动收集工具 - Subdomain automatic/passive collec<br>tion tool |
| [GadgetProbe](https://github.com/BishopFox/GadgetProbe) | v1.0 | Probe endpoints consuming Java serialized objects to identify cl<br>asses, libraries, and library versions on remote Java classpaths. |
| [HopLa](https://github.com/synacktiv/HopLa) | 1.2 |  HopLa Burp Suite Extender plugin -Adds autocompletion support a<br>nd useful payloads in Burp Suite |
| [captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified) | 0.19 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免费<br>ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, sup<br>port AES/RSA/DES/ExecJs(execute JS encryption code in burpsuite).<br> 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSuite插<br>件 |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.19.0 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等）<br>，类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础上，<br>不影响APP、网站加解密正常逻辑等。 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [AutoRepeater](https://github.com/nccgroup/AutoRepeater) |  | Automated HTTP Request Repeating With Burp Suite |
| [http-request-smuggl<br>er](https://github.com/portswigger/http-request-smuggler) |  |  |
| [burp-requests](https://github.com/silentsignal/burp-requests) | v0.2.4 | Copy as requests plugin for Burp Suite |
| [CORSScanner](https://github.com/zzzskd/CORSScanner) |  | CORS 跨域漏洞 burp 插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) | v1.0.0 | fastjson利用，支持tomcat、spring回显，哥斯拉内存马；回显利用链为<br>dhcp、ibatis、c3p0。 |
| [HostHeaderAttack](https://github.com/weujieytt/HostHeaderAttack) | 0.1 | 检测host头攻击的Burpsuite被动扫描插件，Burpsuite passive scannin<br>g plugin responsible for detecting host header attack |
| [knife](https://github.com/bit4woo/knife) | v2.1 | A burp extension that add some useful function toContext Menu 添<br>加一些右键菜单让burp用起来更顺畅 |
| [log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner) | 0.21.0 | CVE-2021-44228 Log4j2 BurpSuite Scanner,Customize ceye.io api or<br> other apis,including internal networks |
| [passive-scan-client](https://github.com/c0ny1/passive-scan-client) | 0.3.0 | Burp被动扫描流量转发插件 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpSuiteCn](https://github.com/funkyoummp/BurpSuiteCn) | V2.0 | Burp Suite汉化 中文 |
#### xray
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [yarx](https://github.com/zema1/yarx) | v0.2.0 | An awesome reverse engine for xray poc. | 一个自动化根据 xray po<br>c 生成对应 server 的工具 |
| [xray-poc-generation](https://github.com/phith0n/xray-poc-generation) |  | 🧬 辅助生成 XRay YAML POC |
| [super-xray](https://github.com/4ra1n/super-xray) | 0.9 | XRAY GUI Starter (Web Vulnerability Scanner) |
#### pocsuite3
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ExpToPocsuite3](https://github.com/smallfox233/ExpToPocsuite3) | v0.1 | goby exp批量转换为pocsuite3 exp脚本 |
#### 浏览器扩展
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Hack-Tools](https://github.com/LasCC/Hack-Tools) | 0.4.0 | The all-in-one Red Team extension for Web Pentester 🛠 |
| [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega) | v2.5.20 | Manage and switch between multiple proxies quickly & easily. |
| [untrusted-types](https://github.com/filedescriptor/untrusted-types) | 1.1.1 |  |
| [fofa_view](https://github.com/fofapro/fofa_view) | v0.0.5 | FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件，目前兼容Chrome<br>、Firefox、Opera。 |
| [mitaka](https://github.com/ninoseki/mitaka) | v0.93.0 | A browser extension for OSINT search |
| [anti-honeypot](https://github.com/cnrstar/anti-honeypot) |  | 一款可以检测WEB蜜罐并阻断请求的Chrome插件 |
| [Chromium-based-XSS-<br>Taint-Tracking](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) | v0.3 | Cyclops 是一款具有 XSS 检测功能的浏览器 |
#### pocassist
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pocassistdb](https://github.com/jweny/pocassistdb) | 1.0.2 | database of pocassist（漏洞库） |
#### goby
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Library-POC](https://github.com/luck-ying/Library-POC) |  | 基于Pocsuite3、goby编写的漏洞poc&exp存档 |
#### volatility
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [tool-for-CTF](https://github.com/ruokeqx/tool-for-CTF) |  | Virtual machine configuration for CTF |
#### nuclei
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [NucleiTP](https://github.com/ExpLangcn/NucleiTP) |  | 自动整合全网Nuclei的漏洞POC，实时同步更新最新POC！ |
### CTF杂项
#### 图片隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegsolve](https://github.com/Giotino/stegsolve) | v1.4 |  |
| [BlindWatermark](https://github.com/ww23/BlindWatermark) | v0.0.3 | Java 盲水印 |
| [cloacked-pixel](https://github.com/livz/cloacked-pixel) |  | LSB steganography and detection |
#### 流量分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [UsbMiceDataHacker](https://github.com/WangYihang/UsbMiceDataHacker) |  | USB鼠标流量包取证工具 , 主要用于绘制鼠标移动以及拖动轨迹 |
| [UsbKeyboardDataHack<br>er](https://github.com/WangYihang/UsbKeyboardDataHacker) |  | USB键盘流量包取证工具 , 用于恢复用户的击键信息 |
#### 编码解码
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [TomatoTools](https://github.com/ht0Ruial/TomatoTools) | v1.0.2 | TomatoTools 一款CTF杂项利器，支持36种常见编码和密码算法的加密和<br>解密，31种密文的分析和识别，支持自动提取flag，自定义插件等。 |
#### 取证分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pyvmx-cracker](https://github.com/axcheron/pyvmx-cracker) |  | Simple tool to crack VMware VMX encryption passwords |
| [chatViewTool](https://github.com/Ormicron/chatViewTool) | BEAT | 基于Java实现的图形化微信聊天记录解密查看器 |
| [Sharp-dumpkey](https://github.com/Ormicron/Sharp-dumpkey) | 1 | 基于C#实现的获取微信数据库密钥的小工具 |
| [Sunflower_get_Passw<br>ord](https://github.com/wafinfo/Sunflower_get_Password) |  | 一款针对向日葵的识别码和验证码提取工具 |
#### 音频隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dtmf-decoder](https://github.com/ribt/dtmf-decoder) |  | Extract phone numbers from an audio recording of the dial tones. |
#### 文件分离
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BlindWaterMark](https://github.com/chishaxie/BlindWaterMark) |  | 盲水印 by python |
#### 压缩文件分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CRC32-Tools](https://github.com/AabyssZG/CRC32-Tools) | 2.2 | Easy CRC32 Tools，so easy！！！ |
### CTF综合
#### 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CTF-Note](https://github.com/kitezzzGrim/CTF-Note) |  | CTF笔记：该项目主要记录CTF知识、刷题记录、工具等。 |
### CTF逆向
#### pyc逆向
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegosaurus](https://github.com/AngelKitty/stegosaurus) | 1.0 | A steganography tool for embedding payloads within Python byteco<br>de. |
### CTFWEB
#### 敏感目录
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ctf-wscan](https://github.com/OrangeWatermelon/ctf-wscan) |  | 在kingkaki的项目上进行了修改，改为单线程，可以在任意目录下执行，<br>对重复的请求进行了过滤 |
| [scrabble](https://github.com/denny0223/scrabble) |  | Simple tool to recover .git folder from remote server |
### CTF密码学
#### RSA
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [rsa-wiener-attack](https://github.com/pablocelayes/rsa-wiener-attack) |  | A Python implementation of the Wiener attack on RSA public-key e<br>ncryption scheme. |
| [RSA](https://github.com/Mr-Aur0ra/RSA) |  |  |
| [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) |  | RSA attack tool (mainly for ctf) - retreive private key from wea<br>k public key and/or uncipher data |
### 应急响应
#### web日志分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [DecodeSomeJSPWebshe<br>ll](https://github.com/minhangxiaohui/DecodeSomeJSPWebshell) | v1.2 | 冰蝎、哥斯拉 jsp webshell通信流量解密器 |
### 其他
#### 其他
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [faker](https://github.com/joke2k/faker) | v15.3.4 | Faker is a Python package that generates fake data for you. |
| [SmsForwarder](https://github.com/pppscn/SmsForwarder) | v3.1.1 | 短信转发器——监控Android手机短信、来电、APP通知，并根据指定规则<br>转发到其他手机：钉钉群自定义机器人、钉钉企业内机器人、企业微信群机<br>器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram<br>机器人、Server酱、PushPlus、手机短信等。包括主动控制服务端与客户端<br>，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。（V3.0 新<br>增）PS.这个APK主要是学习与自用，如有BUG请提ISSUE，同时欢迎大家提PR<br>指正 |
