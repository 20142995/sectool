
## 近7天release更新记录
| 类型| 项目名称 | 更新时间 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- | :---- |

## 近7天commit提交记录
| 类型| 项目名称 | 提交时间 | 更新内容 |
| :---- | :---- | :---- | :---- |
| 半自动漏洞扫描 | [afrog](https://github.com/zan8in/afrog) | 2022-11-27 03:38:42 | update CVE-2022-36883 |
| 子域名收集 | [OneForAll](https://github.com/shmilylty/OneForAll) | 2022-11-26 02:32:16 | 解决#286 |
| 目录扫描 | [dirsearch](https://github.com/maurosoria/dirsearch) | 2022-11-23 13:31:50 | Merge pull request #1248 from drego85/patch-12<br><br>Useful Files and Directory for the SIMOGEO FileManager exploit |
| Burpsuite插件 | [BurpSuite-collections](https://github.com/Mr-xn/BurpSuite-collections) | 2022-11-25 14:53:59 | add BpScan<br><br>一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件(SpringSpiderScan、Log4jScan和FastJsonScan) |
| Burpsuite插件 | [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | 2022-11-20 10:24:53 | Update DomainManager.java<br><br>CopyOnWriteArraySet 用iterator的remove反而会出错 |
## 所有项目
### 漏洞发现&利用
#### 半自动漏洞扫描
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [xray](https://github.com/chaitin/xray) | chaitin | 2019-06-10 07:16:37 | 2022-10-31 02:32:49 | 1.9.3 | 一款完善的安全评估工具，支持常见 web 安全问题扫描和自定义 poc | 使用之前务必先阅读文档 |
| [nuclei](https://github.com/projectdiscovery/nuclei) | projectdiscovery | 2020-04-03 18:47:11 | 2022-11-17 10:29:05 | v2.7.9 | Fast and customizable vulnerability scanner based on simple YAML based DSL. |
| [Fvuln](https://github.com/d3ckx1/Fvuln) | d3ckx1 | 2021-09-26 14:05:11 | 2022-09-18 11:14:42 | Fvuln_v1.4.8 | F-vuln（全称：Find-Vulnerability）是为了自己工作方便专门编写的一款自动化工具，主要适用于日常安全服务、渗透测试人员和RedTeam红队人员，它集合的功能包括：存活IP探测、开放端口探测、web服务探测、web漏洞扫描、smb爆破、ssh爆破、ftp爆破、mssql爆破等其他数据库爆破工作以及大量web漏洞检测模块。 |
| [afrog](https://github.com/zan8in/afrog) | zan8in | 2022-02-24 06:00:32 | 2022-11-27 03:38:42 | v2.0.0 | afrog 是一款性能卓越、快速稳定、PoC 可定制化的漏洞扫描工具 - A tool for finding vulnerabilities |
| [vulmap](https://github.com/zhzyker/vulmap) | zhzyker | 2020-10-09 06:34:36 | 2022-04-13 13:23:54 | v0.9 | Vulmap 是一款 web 漏洞扫描和验证工具, 可对 webapps 进行漏洞扫描, 并且具备漏洞验证功能 |
#### 半自动化漏洞利用
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [railgun](https://github.com/lz520520/railgun) | lz520520 | 2020-08-31 00:52:43 | 2022-08-22 05:20:08 | v1.4.6 |  |
| [Goby](https://github.com/gobysec/Goby) | gobysec | 2019-06-03 07:56:11 | 2021-11-22 11:19:16 | Beta1.9.325 | Attack surface mapping |
#### 数据库利用
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [MDUT](https://github.com/SafeGroceryStore/MDUT) | SafeGroceryStore | 2020-12-30 02:49:31 | 2022-10-13 05:34:29 | v2.1.1 | MDUT - Multiple Database Utilization Tools |
| [LiqunKit_](https://github.com/Liqunkit/LiqunKit_) | Liqunkit | 2021-08-21 11:40:23 | 2022-01-21 08:11:55 |  | 下架 |
| [SharpSQLTools](https://github.com/uknowsec/SharpSQLTools) | uknowsec | 2019-10-18 01:55:23 | 2021-08-05 12:39:51 | 41 | SharpSQLTools 和@Rcoil一起写的小工具，可上传下载文件，xp_cmdshell与sp_oacreate执行命令回显和clr加载程序集执行相应操作。 |
| [mssqlproxy](https://github.com/blackarrowsec/mssqlproxy) | blackarrowsec | 2020-02-12 08:44:28 | 2020-08-13 11:53:38 | 0.1 | mssqlproxy is a toolkit aimed to perform lateral movement in restricted environments through a compromised Microsoft SQL Server via socket reuse |
| [odat](https://github.com/quentinhardy/odat) | quentinhardy | 2014-02-28 12:55:51 | 2022-06-20 08:09:48 | 5.1.1 | ODAT: Oracle Database Attacking Tool |
| [redis-rogue-server](https://github.com/n0b0dyCN/redis-rogue-server) | n0b0dyCN | 2019-07-07 17:39:37 | 2022-10-13 03:29:51 |  | Redis(<=5.0.5) RCE |
| [redis-rce](https://github.com/Ridter/redis-rce) | Ridter | 2019-07-08 14:05:30 | 2021-11-30 14:55:59 |  | Redis 4.x/5.x RCE |
| [RedisEXP](https://github.com/yuyan-sec/RedisEXP) | yuyan-sec | 2022-03-19 14:41:00 | 2022-09-10 06:47:57 |  | Redis 漏洞利用工具 |
| [redis_rce](https://github.com/zyylhn/redis_rce) | zyylhn | 2022-03-16 15:02:08 | 2022-04-18 02:32:09 | v0.1.0 | Redis primary/secondary replication RCE |
#### Shell管理
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [Behinder](https://github.com/rebeyond/Behinder) | rebeyond | 2018-09-26 01:11:17 | 2022-08-23 02:50:39 | Behinder_v4.0.5 | “冰蝎”动态二进制加密网站管理客户端 |
| [Godzilla](https://github.com/BeichenDream/Godzilla) | BeichenDream | 2020-08-17 17:27:56 | 2021-11-01 08:57:30 | v4.0.1-godzilla | 哥斯拉 |
#### 中间件&框架漏洞利用
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [AttackTomcat](https://github.com/tpt11fb/AttackTomcat) | tpt11fb | 2022-11-13 11:01:41 | 2022-11-15 09:05:50 | V1 | Tomcat漏洞利用工具 |
| [SpringExploit](https://github.com/SummerSec/SpringExploit) | SummerSec | 2022-04-19 03:48:27 | 2022-06-14 12:28:15 | 0.1.9 | 🚀 一款为了学习go而诞生的漏洞利用工具 |
| [shiro_rce_tool](https://github.com/wyzxxz/shiro_rce_tool) | wyzxxz | 2020-01-07 10:47:41 | 2022-08-17 09:35:07 |  | shiro 反序列 命令执行辅助检测工具 |
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2) | SummerSec | 2021-06-13 03:44:13 | 2022-08-31 15:54:01 | 4.5.6 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原版中NoCC的问题 https://github.com/j1anFen/shiro_attack |
| [shiro_attack](https://github.com/j1anFen/shiro_attack) | j1anFen | 2020-11-08 06:28:38 | 2021-06-22 01:51:08 | 2.2 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马） |
| [FastjsonExploit](https://github.com/c0ny1/FastjsonExploit) | c0ny1 | 2019-07-20 04:55:57 | 2020-03-06 07:48:16 |  | Fastjson vulnerability quickly exploits the framework（fastjson漏洞快速利用框架） |
| [fastjson_rec_exploit](https://github.com/mrknow001/fastjson_rec_exploit) | mrknow001 | 2020-07-10 08:02:48 | 2020-07-21 13:50:22 |  | fastjson一键命令执行 |
| [jexboss](https://github.com/joaomatosf/jexboss) | joaomatosf | 2014-11-30 16:56:15 | 2017-03-28 01:34:04 |  | JexBoss: Jboss (and Java Deserialization Vulnerabilities) verify and EXploitation Tool |
| [dubbo-exp](https://github.com/threedr3am/dubbo-exp) | threedr3am | 2021-12-26 04:52:47 | 2022-10-12 08:48:36 |  | dubbo学习demo，之前删了，重新上传。 |
| [Struts2-Scan](https://github.com/HatBoy/Struts2-Scan) | HatBoy | 2018-07-12 15:04:44 | 2020-12-23 09:04:37 |  | Struts2全漏洞扫描利用工具 |
| [log4j-shell-poc](https://github.com/kozmer/log4j-shell-poc) | kozmer | 2021-12-10 23:19:28 | 2022-01-22 14:55:02 |  | A Proof-Of-Concept for the CVE-2021-44228 vulnerability.  |
#### 中间件&框架漏洞扫描
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [WeblogicScan](https://github.com/rabbitmask/WeblogicScan) | rabbitmask | 2019-03-05 00:57:22 | 2022-01-26 02:56:25 |  | Weblogic一键漏洞检测工具，V1.5，更新时间：20200730 |
| [weblogic-infodetector](https://github.com/woodpecker-appstore/weblogic-infodetector) | woodpecker-appstore | 2021-04-01 04:32:50 | 2022-03-23 08:33:43 | 0.2.4 | woodpecker框架weblogic信息探测插件 |
| [Jiraffe](https://github.com/0x48piraj/Jiraffe) | 0x48piraj | 2020-02-07 13:26:33 | 2021-05-08 12:37:38 | v2.0.6 | One stop place for exploiting Jira instances in your proximity |
| [Artillery](https://github.com/Weik1/Artillery) | Weik1 | 2022-05-12 06:36:18 | 2022-08-08 00:39:34 | v1.0_20220519 | JAVA 插件化漏洞扫描器，Gui基于javafx。POC 目前集成 Weblogic、Tomcat、Shiro、Spring等。 |
#### 重点CMS利用
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL) | LittleBear4 | 2022-10-13 12:31:21 | 2022-11-17 09:28:39 | v0.6 | OA综合利用工具，集合将近20款OA漏洞批量扫描 |
| [seeyon_exp](https://github.com/Summer177/seeyon_exp) | Summer177 | 2021-06-03 07:22:37 | 2021-06-03 08:03:40 |  | 致远OA综合利用工具 |
| [SeeyonExploit-GUI](https://github.com/God-Ok/SeeyonExploit-GUI) | God-Ok | 2021-07-20 14:42:05 | 2021-07-07 15:01:16 |  | 致远OA综合利用工具V1.0 |
| [TDOA_RCE](https://github.com/xinyu2428/TDOA_RCE) | xinyu2428 | 2021-03-01 07:18:29 | 2021-03-17 08:51:32 | v1.0 | 通达OA综合利用工具 |
| [LandrayExploit](https://github.com/yuanhaiGreg/LandrayExploit) | yuanhaiGreg | 2021-06-29 09:48:21 | 2021-07-27 08:20:41 | 1.1 | 蓝凌OA漏洞利用工具/前台无条件RCE/文件写入 |
| [weaver_exp](https://github.com/z1un/weaver_exp) | z1un | 2021-06-27 17:15:41 | 2021-06-28 19:02:37 |  | 泛微OA漏洞综合利用脚本 |
| [EgGateWayGetShell](https://github.com/Tas9er/EgGateWayGetShell) | Tas9er | 2021-01-14 01:04:48 | 2021-01-14 01:05:29 |  | Code By:Tas9er |
| [CMSmap](https://github.com/Dionach/CMSmap) | Dionach | 2018-09-20 06:55:41 | 2018-10-26 18:45:03 |  | CMSmap is a python open source CMS scanner that automates the process of detecting security flaws of the most popular CMSs.  |
| [wordpress-exploit-framework](https://github.com/rastating/wordpress-exploit-framework) | rastating | 2015-11-27 22:13:52 | 2019-11-24 19:04:43 | v2.0.1 | A Ruby framework designed to aid in the penetration testing of WordPress systems.  |
| [wpscan](https://github.com/wpscanteam/wpscan) | wpscanteam | 2012-07-11 20:27:47 | 2022-11-17 14:27:09 | v3.8.22 | WPScan WordPress security scanner. Written for security professionals and blog maintainers to test the security of their WordPress websites. |
| [WPForce](https://github.com/n00py/WPForce) | n00py | 2016-03-17 21:20:14 | 2021-02-16 23:47:36 | v.1.0.0 | Wordpress Attack Suite |
| [ThinkphpGUI](https://github.com/Lotus6/ThinkphpGUI) | Lotus6 | 2021-06-22 15:01:04 | 2022-06-01 18:48:29 | 1.3 | Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，getshell。 |
| [thinkphp_gui_tools](https://github.com/bewhale/thinkphp_gui_tools) | bewhale | 2021-04-26 13:32:23 | 2022-07-02 09:01:52 | v2.4.2 | ThinkPHP漏洞综合利用工具, 图形化界面, 命令执行, 一键getshell, 批量检测, 日志遍历, session包含,宝塔绕过 |
#### 信息泄露利用
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [Cloud-Bucket-Leak-Detection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | UzJu | 2022-02-22 10:07:49 | 2022-08-25 09:31:28 | v0.4.0 | 六大云存储，泄露利用检测工具 |
| [aksk_tool](https://github.com/wyzxxz/aksk_tool) | wyzxxz | 2021-07-05 10:21:36 | 2022-11-08 06:43:32 |  | AK资源管理工具，阿里云/腾讯云/华为云/AWS/UCLOUD/京东云/七牛云存储  AccessKey AccessKeySecret，利用AK获取资源信息和操作资源，ECS/CVM/E2/UHOST/ECI执行命令，OSS/COS/S3管理，RDS/DB管理，域名管理，添加RAM/CAM/IAM账号等 |
| [swagger-exp](https://github.com/lijiejie/swagger-exp) | lijiejie | 2021-03-23 06:46:21 | 2022-08-08 07:07:03 |  | A Swagger API Exploit |
| [swagger-hack](https://github.com/jayus0821/swagger-hack) | jayus0821 | 2021-02-01 11:49:51 | 2021-08-02 05:39:49 |  | 自动化爬取并自动测试所有swagger接口 |
| [heapdump_tool](https://github.com/wyzxxz/heapdump_tool) | wyzxxz | 2021-08-06 02:48:31 | 2022-08-17 09:34:10 |  | heapdump敏感信息查询工具，例如查找 spring heapdump中的密码明文，AK,SK等 |
| [Packer-Fuzzer](https://github.com/rtcatc/Packer-Fuzzer) | rtcatc | 2020-09-30 20:21:15 | 2022-11-11 14:18:43 | v1.4 | Packer Fuzzer is a fast and efficient scanner for security detection of websites constructed by javascript module bundler such as Webpack.  |
| [GitHack](https://github.com/BugScanTeam/GitHack) | BugScanTeam | 2017-02-24 02:58:50 | 2020-02-25 10:15:10 |  | .git 泄漏利用工具，可还原历史版本 |
| [ds_store_exp](https://github.com/lijiejie/ds_store_exp) | lijiejie | 2017-01-24 11:48:50 | 2022-06-16 02:22:00 |  | A .DS_Store file disclosure exploit.   It parses .DS_Store file and downloads files recursively. |
| [svnExploit](https://github.com/admintony/svnExploit) | admintony | 2018-02-06 09:43:26 | 2019-10-17 01:09:21 |  | SvnExploit支持SVN源代码泄露全版本Dump源码 |
| [git-dumper](https://github.com/arthaud/git-dumper) | arthaud | 2017-03-31 03:39:53 | 2022-05-07 04:39:31 |  | A tool to dump a git repository from a website |
| [GitDorker](https://github.com/obheda12/GitDorker) | obheda12 | 2020-07-13 01:11:46 | 2021-05-07 06:11:57 |  | A Python program to scrape secrets from GitHub through usage of a large repository of dorks. |
| [SecretFinder](https://github.com/m4ll0k/SecretFinder) | m4ll0k | 2020-06-08 10:50:12 | 2021-06-26 07:43:14 |  | SecretFinder - A python script for find sensitive data (apikeys, accesstoken,jwt,..) and search anything on javascript files  |
| [JSFScan.sh](https://github.com/KathanP19/JSFScan.sh) | KathanP19 | 2020-06-30 06:05:32 | 2022-11-04 03:20:29 |  | Automation for javascript recon in bug bounty.  |
| [SubOver](https://github.com/Ice3man543/SubOver) | Ice3man543 | 2018-02-04 09:49:46 | 2018-08-30 00:38:45 | v1.2 | A Powerful Subdomain Takeover Tool |
#### 口令爆破
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [goon](https://github.com/i11us0ry/goon) | i11us0ry | 2021-06-28 15:31:50 | 2022-08-23 16:20:26 | v3.5 | goon,集合了fscan和kscan等优秀工具功能的扫描爆破工具。功能包含：ip探活、port扫描、web指纹扫描、title扫描、压缩文件扫描、fofa获取、ms17010、mssql、mysql、postgres、redis、ssh、smb、rdp、telnet、tomcat等爆破以及如netbios探测等功能。 |
| [SNETCracker](https://github.com/shack2/SNETCracker) | shack2 | 2018-09-13 09:31:04 | 2019-08-01 05:56:13 | 1.0.20190715 | 超级弱口令检查工具是一款Windows平台的弱口令审计工具，支持批量多线程检查，可快速发现弱密码、弱口令账号，密码支持和用户名结合进行检查，大大提高成功率，支持自定义服务端口和字典。 |
| [web-brutator](https://github.com/koutto/web-brutator) | koutto | 2019-04-11 15:02:03 | 2021-11-16 14:29:28 |  | Fast Modular Web Interfaces Bruteforcer |
| [WebCrack](https://github.com/yzddmr6/WebCrack) | yzddmr6 | 2019-08-20 03:39:16 | 2021-09-07 12:19:54 |  | WebCrack是一款web后台弱口令/万能密码批量检测工具，在工具中导入后台地址即可进行自动化检测。 |
#### 漏洞检测利用仓库
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [poc-hub](https://github.com/ybdt/poc-hub) | ybdt | 2020-09-03 04:47:40 | 2022-10-24 16:38:39 |  | 漏洞检测、漏洞利用 |
| [Awesome-Exploit](https://github.com/Threekiii/Awesome-Exploit) | Threekiii | 2022-04-22 02:08:08 | 2022-10-11 03:03:21 |  | 一个漏洞利用工具仓库 |
### 信息收集
#### 资产测绘采集
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll) | ExpLangcn | 2022-06-09 10:09:47 | 2022-10-26 08:28:16 | V1.2 | 为了方便安全从业人员在使用网络测绘平台进行信息搜集时的效率，本程序集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并且合并展示及导出。 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | xzajyjs | 2022-01-14 14:53:32 | 2022-11-08 12:25:49 | v2.3.2 | 【支持Fofa、Zoomeye、Quake等网络空间搜索引擎】闪电搜索器；GUI图形化渗透测试信息搜集工具；资产搜集引擎 |
#### 子域名收集
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [subfinder](https://github.com/projectdiscovery/subfinder) | projectdiscovery | 2018-03-31 09:44:57 | 2022-11-17 14:37:23 | v2.5.5 | Subfinder is a subdomain discovery tool that discovers valid subdomains for websites. Designed as a passive framework to be useful for bug bounties and safe for penetration testing. |
| [ksubdomain](https://github.com/knownsec/ksubdomain) | knownsec | 2020-08-21 07:29:04 | 2022-02-07 06:18:30 | v0.7 | 无状态子域名爆破工具 |
| [OneForAll](https://github.com/shmilylty/OneForAll) | shmilylty | 2018-12-10 09:43:37 | 2022-11-26 02:32:16 | v0.4.5 | OneForAll是一款功能强大的子域收集工具 |
| [LangSrcCurise](https://github.com/LangziFun/LangSrcCurise) | LangziFun | 2019-08-23 02:07:53 | 2021-01-14 04:32:06 |  | SRC子域名资产监控 |
| [github-subdomains](https://github.com/gwen001/github-subdomains) | gwen001 | 2020-07-24 06:54:29 | 2022-11-17 20:37:34 |  | Find subdomains on GitHub. |
| [LayerDomainFinder](https://github.com/euphrat1ca/LayerDomainFinder) | euphrat1ca | 2019-07-17 07:34:49 | 2019-07-17 07:46:03 | 3 | Layer子域名挖掘机 |
| [dnsub](https://github.com/yunxu1/dnsub) | yunxu1 | 2020-03-21 12:06:52 | 2021-04-08 07:06:24 | v2.1 | dnsub一款好用且强大的子域名扫描工具 |
#### 目录扫描
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [dirsearch](https://github.com/maurosoria/dirsearch) | maurosoria | 2013-04-30 15:57:40 | 2022-11-23 13:31:50 | v0.4.3 | Web path scanner |
| [URLFinder](https://github.com/pingc0y/URLFinder) | pingc0y | 2022-06-06 10:17:00 | 2022-10-25 05:55:08 |  | 类似JSFinder的golang实现，一款用于快速提取检测页面中JS与URL的工具，更快更全更舒服 |
| [feroxbuster](https://github.com/epi052/feroxbuster) | epi052 | 2020-08-22 15:36:19 | 2022-11-16 22:53:02 | v2.7.2 | A fast, simple, recursive content discovery tool written in Rust. |
| [ffuf](https://github.com/ffuf/ffuf) | ffuf | 2018-11-08 09:25:49 | 2022-05-19 06:33:57 | v1.5.0 | Fast web fuzzer written in Go |
| [dirmap](https://github.com/H4ckForJob/dirmap) | H4ckForJob | 2019-04-11 12:10:16 | 2022-06-01 08:21:11 |  | An advanced web directory & file scanning tool that will be more powerful than DirBuster, Dirsearch, cansina, and Yu Jian.一个高级web目录、文件扫描工具，功能将会强于DirBuster、Dirsearch、cansina、御剑。 |
| [cansina](https://github.com/deibit/cansina) | deibit | 2013-02-21 19:52:13 | 2022-10-04 09:10:02 | 1.0.0 | Web Content Discovery Tool |
| [urlbrute](https://github.com/ReddyyZ/urlbrute) | ReddyyZ | 2020-12-04 22:09:05 | 2020-12-05 15:54:27 | v1.0.2 | Directory/Subdomain scanner developed in GoLang. |
| [yjdirscan](https://github.com/foryujian/yjdirscan) | foryujian | 2020-10-05 15:37:28 | 2020-10-25 03:14:19 | yjdirscan | 御剑目录扫描专业版，简单实用的命令行网站目录扫描工具，支持爬虫、fuzz、自定义字典、字典变量、UA修改、假404自动过滤、扫描控速等功能。 |
| [yuhScan](https://github.com/hunyaio/yuhScan) | hunyaio | 2021-06-23 07:04:13 | 2021-07-19 06:45:00 | v1.0 | web目录快速扫描工具 |
| [gospider](https://github.com/jaeles-project/gospider) | jaeles-project | 2020-01-22 05:13:57 | 2022-05-17 11:00:12 | v1.1.6 | Gospider - Fast web spider written in Go |
#### 指纹识别
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [EHole](https://github.com/EdgeSecurityTeam/EHole) | EdgeSecurityTeam | 2021-01-15 05:51:57 | 2022-07-11 08:43:07 | 3.0 | EHole(棱洞)3.0 重构版-红队重点攻击系统指纹探测工具 |
#### 端口扫描
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [TXPortMap](https://github.com/4dogs-cn/TXPortMap) | 4dogs-cn | 2021-03-29 02:43:30 | 2021-12-10 11:35:55 | v1.1.2 | Port Scanner & Banner Identify From TianXiang |
| [naabu](https://github.com/projectdiscovery/naabu) | projectdiscovery | 2020-01-21 10:56:32 | 2022-10-25 21:40:41 | v2.1.1 | A fast port scanner written in go with a focus on reliability and simplicity. Designed to be used in combination with other tools for attack surface discovery in bug bounties and pentests |
### 内网渗透
#### 密码提取
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [getIntrInfo](https://github.com/Potato-py/getIntrInfo) | Potato-py | 2021-09-29 03:00:32 | 2022-10-08 07:32:58 |  | 收集内部网信息。包括：浏览器书签、密码和浏览历史记录、cookie。Wifi信息和密码。主机信息。 |
| [FinalShell-Decoder](https://github.com/passer-W/FinalShell-Decoder) | passer-W | 2022-04-06 07:11:25 | 2022-04-11 11:34:42 | V1.0 | FinallShell 密码解密GUI工具 |
### 相关资源
#### 工具集成环境
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [penetration-suite-toolkit](https://github.com/makoto56/penetration-suite-toolkit) | makoto56 | 2021-09-03 00:47:14 | 2022-05-26 03:24:23 | v3.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先利其器。 |
#### 知识库
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [penetration-suite-toolkit](https://github.com/makoto56/penetration-suite-toolkit) | makoto56 | 2021-09-03 00:47:14 | 2022-05-26 03:24:23 | v3.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先利其器。 |
| [Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam) | Threekiii | 2022-02-08 00:45:03 | 2022-11-16 01:59:50 |  | 一个红队知识仓库 |
### 工具&插件
#### Burpsuite插件
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [PowerScanner](https://github.com/NeoTheCapt/PowerScanner) | NeoTheCapt | 2021-01-23 19:00:16 | 2021-12-16 07:53:45 | 1.1.3 | 面向HW的红队半自动扫描器 |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | F6JO | 2022-06-01 07:07:38 | 2022-11-16 03:49:31 | RouteVulScan1.3 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的burp插件 |
| [SpringScan](https://github.com/metaStor/SpringScan) | metaStor | 2022-04-09 04:51:10 | 2022-06-22 05:17:06 | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [BurpSuite-collections](https://github.com/Mr-xn/BurpSuite-collections) | Mr-xn | 2020-01-25 02:07:37 | 2022-11-25 14:53:59 |  | 有关burpsuite的插件(非商店),文章以及使用技巧的收集(此项目不再提供burpsuite破解文件,如需要请在博客mrxn.net下载)---Collection of burpsuite plugins (non-stores), articles and tips for using Burpsuite, no crack version file |
| [BurpShiroPassiveScan](https://github.com/pmiaowu/BurpShiroPassiveScan) | pmiaowu | 2020-07-15 07:12:16 | 2022-06-30 02:35:20 | BurpShiroPassiveScan-2.0.0 | 一款基于BurpSuite的被动式shiro检测插件 |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | pmiaowu | 2020-12-15 02:22:42 | 2022-06-26 17:02:17 | BurpFastJsonScan-2.2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [HaE](https://github.com/gh0stkey/HaE) | gh0stkey | 2020-03-24 10:12:50 | 2022-09-26 10:49:35 | 2.4.4 | HaE - Highlighter and Extractor, 赋能白帽 高效作战 |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | bit4woo | 2019-01-18 07:15:15 | 2022-11-20 10:24:53 | v1.9-alpha | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集；快速Title获取；外部工具联动；等等 |
| [Sylas](https://github.com/Acmesec/Sylas) | Acmesec | 2022-01-05 10:16:09 | 2022-10-09 11:06:28 | 1.1.1 | 新一代子域名主/被动收集工具 - Subdomain automatic/passive collection tool |
| [GadgetProbe](https://github.com/BishopFox/GadgetProbe) | BishopFox | 2020-01-21 19:45:18 | 2021-02-19 18:47:05 | v1.0 | Probe endpoints consuming Java serialized objects to identify classes, libraries, and library versions on remote Java classpaths. |
| [HopLa](https://github.com/synacktiv/HopLa) | synacktiv | 2021-05-06 11:01:23 | 2021-05-12 16:21:29 | 1.2 |  HopLa Burp Suite Extender plugin -  Adds autocompletion support and useful payloads in Burp Suite |
| [captcha-killer-modified](https://github.com/f0ng/captcha-killer-modified) | f0ng | 2022-03-18 12:41:58 | 2022-11-18 07:59:12 | 0.16 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免费ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) | whwlsfb | 2020-05-29 02:59:15 | 2022-06-21 03:48:18 |  | BurpCrypto is a collection of burpsuite encryption plug-ins, support AES/RSA/DES/ExecJs(execute JS encryption code in burpsuite). 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSuite插件 |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | f0ng | 2022-03-26 10:13:56 | 2022-11-15 05:41:53 | 0.19.0 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等），类似mitmproxy，不同点在于经过了burp中转 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | TheKingOfDuck | 2019-06-05 07:24:35 | 2022-09-29 09:12:23 | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [AutoRepeater](https://github.com/nccgroup/AutoRepeater) | nccgroup | 2017-12-15 21:09:41 | 2020-10-08 21:22:46 |  | Automated HTTP Request Repeating With Burp Suite |
| [http-request-smuggler](https://github.com/portswigger/http-request-smuggler) | portswigger | 2019-07-30 14:41:18 | 2022-11-18 14:26:29 |  |  |
#### xray
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [yarx](https://github.com/zema1/yarx) | zema1 | 2021-11-11 09:43:21 | 2021-11-30 08:37:42 | v0.2.0 | An awesome reverse engine for xray poc. | 一个自动化根据 xray poc 生成对应 server 的工具 |
| [xray-poc-generation](https://github.com/phith0n/xray-poc-generation) | phith0n | 2019-07-06 21:45:57 | 2019-08-23 08:21:38 |  | 🧬 辅助生成 XRay YAML POC |
#### pocsuite3
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [ExpToPocsuite3](https://github.com/smallfox233/ExpToPocsuite3) | smallfox233 | 2022-09-30 15:47:25 | 2022-10-04 05:59:18 | v0.1 | goby exp批量转换为pocsuite3 exp脚本 |
#### 浏览器扩展
| 项目名称 | 作者 | 创建时间| 最近提交时间 | 版本 | 项目描述 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [Hack-Tools](https://github.com/LasCC/Hack-Tools) | LasCC | 2020-06-22 21:42:16 | 2022-10-21 19:39:12 | 0.4.0 | The all-in-one Red Team extension for Web Pentester 🛠 |
| [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega) | FelisCatus | 2012-06-08 15:32:30 | 2022-11-16 09:05:15 | v2.5.20 | Manage and switch between multiple proxies quickly & easily. |
| [untrusted-types](https://github.com/filedescriptor/untrusted-types) | filedescriptor | 2020-11-15 09:49:44 | 2021-10-12 17:37:56 | 1.1.1 |  |
| [fofa_view](https://github.com/fofapro/fofa_view) | fofapro | 2019-12-28 17:11:26 | 2022-02-16 17:26:12 | v0.0.5 | FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件，目前兼容  Chrome、Firefox、Opera。 |
| [mitaka](https://github.com/ninoseki/mitaka) | ninoseki | 2018-02-09 00:13:30 | 2022-09-23 07:03:14 | v0.93.0 | A browser extension for OSINT search |
| [anti-honeypot](https://github.com/cnrstar/anti-honeypot) | cnrstar | 2020-08-16 14:24:29 | 2020-10-30 02:59:02 |  | 一款可以检测WEB蜜罐并阻断请求的Chrome插件 |
| [Chromium-based-XSS-Taint-Tracking](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) | v8blink | 2022-04-30 01:01:32 | 2022-06-05 23:43:51 | v0.3 | Cyclops 是一款具有 XSS 检测功能的浏览器 |
