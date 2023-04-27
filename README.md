# 更新于 2023-04-27 08:43:26

## 近15天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
|2023-04-27 00:26:10|[feroxbuster](https://github.com/epi052/feroxbuster)|v2.9.5|## What's Changed* 878 support raw urls<br> by @epi052 in https://github.com/epi052<br>/feroxbuster/pull/884special thanks to @<br>aroly for reporting the issue, @lavafrot<br>h for the workaround, and @aancw for fur<br>thering the discussion! :tada:**Full Cha<br>ngelog**: https://github.com/epi052/fero<br>xbuster/compare/v2.9.4...v2.9.5|
|2023-04-26 14:33:25|[log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner)|0.25.0|# 0.25.0 update## 2023-4-261. fix bugs_<br>________________________________________<br>____________________1. 修复bug，感谢A_Ad<br>am师傅反馈|
|2023-04-26 06:14:59|[Elkeid](https://github.com/bytedance/Elkeid)|v1.7.0.11<br>-driver-ko<br>-20230426||
|2023-04-25 17:18:33|[Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)|v1.3.4|### v1.3.4 主要更新：- 新功能：截图预览<br>窗口。需要在设置→快捷识图→截图预览窗口<br>里打开。效果见下图，可以调整透明度 并钉在<br>屏幕顶层。![1682442876719.png](https://tu<br>pian.li/images/2023/04/26/64480a815920a.<br>png)- 新功能：可用方向键微调截图框位置。<br>- 修Bug：修复了拖入图片时有几率卡退主窗<br>口的问题。- 优化了一些处理流程。- 优化了<br>打包方式，软件体积比上一代减少了15MB。###<br> 文件说明软件本体：Umi-OCR.v1.3.4.7z，内<br>置简体中文&英文通用识别库。多国语言扩展包<br>：Umi-OCR.v1.3_DLC_languages.7z，可额外导<br>入繁中,英,日,韩,俄,德,法 识别库。请按需下<br>载。|
|2023-04-25 14:39:32|[PEASS-ng](https://github.com/carlospolop/PEASS-ng)|20230425-<br>bd7331ea||
|2023-04-25 07:05:14|[autoDecoder](https://github.com/f0ng/autoDecoder)|0.25|## 2023.4.25 更新0.251. 增加二进制请求<br>体、响应体处理，原理为将请求包的内容base6<br>4编码后传入接口，需要对burp做以下设置，<br>否则获取到的编码为损坏的- 需要勾选User op<br>tions->Character Sets中的Use the platfor<br>m default(UTF-8)[MAC]，或者勾选Display a<br>s raw bytes[Windows]感谢微信群师傅Ronin<br>师傅反馈|
|2023-04-25 04:01:24|[veinmind-tools](https://github.com/chaitin/veinmind-tools)|v2.1.2|## Feature* feat(veinmind-weakpass): su<br>pport ftp @ek1ng in https://github.com/c<br>haitin/veinmind-tools/pull/226* feat(vei<br>nmind-iac): add dockerfile security dete<br>ction by @ek1ng in https://github.com/ch<br>aitin/veinmind-tools/pull/228## Fix* fix<br>(ai): ignore basic info analyzer by @DVK<br>union in https://github.com/chaitin/vein<br>mind-tools/pull/218* fix(Makefile): add <br>CGO_ENBALED && update(dependency): updat<br>e dependency version by @ek1ng in https:<br>//github.com/chaitin/veinmind-tools/pull<br>/221* fix(CI/CD): change goproxy setting<br>s by @ek1ng in https://github.com/chaiti<br>n/veinmind-tools/pull/222## Others* doc:<br> update README.md by @DVKunion in https:<br>//github.com/chaitin/veinmind-tools/pull<br>/219## New Contributors* @ek1ng made the<br>ir first contribution in https://github.<br>com/chaitin/veinmind-tools/pull/221**Ful<br>l Changelog**: https://github.com/chaiti<br>n/veinmind-tools/compare/v2.1.1...v2.1.2|
|2023-04-25 03:38:54|[knife](https://github.com/bit4woo/knife)|v2.2|更新“Find URL And Request”功能更新chi<br>nese中文显示面板逻辑，及时刷新避免有时显<br>示不一致的问题端口扫描逻辑优化，多个host<br>在同一个命令行中完成扫描，避免打开太多窗<br>口更新dismiss功能，规则更清晰也更容易自行<br>编辑处理。让proxy中的数据包编辑更改可视化<br>，更容易判断数据处理规则是否正确数据包修<br>改更新、丢弃转发的规则类型更丰富，适应更<br>多场景。|
|2023-04-24 15:55:52|[faker](https://github.com/joke2k/faker)|v18.5.1|See [CHANGELOG.md](https://github.com/j<br>oke2k/faker/blob/refs/tags/v18.5.1/CHANG<br>ELOG.md).|
|2023-04-24 13:58:59|[Ladon](https://github.com/k8gege/Ladon)|v10.10.4|### Ladon 10.10.420230422[u]LadonGUI文<br>本处理，功能全改成中文(Win8及以上英文系统<br>支持中文)[+]EXP-2022-36537	Zookeeper 未授<br>权文件读取EXP (默认/WEB-INF/web.xml)[+]CV<br>E-2022-36537	Server Backup Manager 未授<br>权RCE漏洞检测 (Zookeeper)[+]INI插件超时30<br>秒，自动结束进程，防批量PY卡死[+]TXT文件I<br>P、URL等自动去重，只有str.txt不去重[+]TX<br>T文件扫描TXT支持自定义线程数，不再默认10<br>0[u]SshScan修复ip.txt时重复扫N多密码的Bu<br>g[+]PortForward端口转发 端口中转[+]默认<br>信息显示OS版本识别小版本号、.NET最高版本[<br>+]INI插件支持$ip$、$url$、$tar$、$ip$:$p<br>ort$、$ip$ $port$参数，自动处理格式，如t<br>ar.txt中有IP和URL，$ip$会把url处理成IP[+<br>]INI插件支持参数处理，如INI里配置$ip$，<br>读取tar.txt内容为http://192.168.1.8:8099<br>，内容将处理成IP数据192.168.1.8，其他同理<br>[+]TXT文件新增tar.txt、target.txt一样，<br>传入参数为原始内容，如提供的是IP，Ladon不<br>会处理成url，除非INI里指定，或模块自行处<br>理[+]TXT文件修复读取url.txt host.txt 出现<br>不完整问题，如http://backup.xxx.org 变成 <br>http:ckup.xx.org 的BugEXP-2022-36537	Zoo<br>keeper 未授权文件读取EXP (默认/WEB-INF/w<br>eb.xml)![image](http://k8gege.org/k8img/<br>Ladon/exe/CVE-2022-36537_EXP.png)批量检<br>测CVE-2022-36537 Server Backup Manager 未<br>授权RCE漏洞 上传是否可用![image](http://k<br>8gege.org/k8img/Ladon/exe/CVE-2022-36537<br>_ISOK.png)端口转发![image](http://k8gege<br>.org/k8img/Ladon/exe/FortForward.png)多<br>个Potato在IIS下轻松提权![image](http://k8<br>gege.org/k8img/Ladon/exe/lpe_efspotato.p<br>ng)### Ladon 10.10.3 20230410[+]FtpServe<br>r	迷你FTP服务器，(支持windows/Linux自带f<br>tp命令实现文件上传下载)默认21 admin admi<br>n 可自定义端口自定义用户、密码[+]TcpServ<br>er	监听TCP发包数据 保存TXT和HEX 如SMB RD<br>P HTTP SSH LDAP FTP等协议[+]UdpServer	监<br>听UDP发包数据 保存TXT和HEX 如DNS、SNMP等<br>协议[+]ArpInfoARP协议探测存活主机IP和MAC<br>，仅支持同一子网[u]WebServer	迷你WEB服务<br>器[u]PortScan移除9100端口Ladon 10.10.2 20<br>230402[+]clsLog清除崩溃日志、UsageLog日<br>志、清除图标缓存、禁止UsageLog日志记录[u]<br>默认禁止基于.net程序UsageLog日志记录(如各<br>类工具、powershell等)防止蓝队或EDR通过日<br>志审计[u]RunPS无PowerShell.exe执行*.ps1脚<br>本 新增内存绕过AMSI反病毒查杀接口[+]默认B<br>ypassETW 绕过部分杀软和EDR监控[+]HPreboo<br>tSNMP重启HP打印机 .net>=4.0|
|2023-04-24 08:11:58|[kube-bench](https://github.com/aquasecurity/kube-bench)|v0.6.13|## Changelogc3b6871 Fix version in poli<br>cies.yaml (#1415)9e41099 build(deps): bu<br>mp github.com/aws/aws-sdk-go-v2/service/<br>securityhub (#1397)7aeb6c3 build(deps): <br>bump github.com/fatih/color from 1.13.0 <br>to 1.14.1 (#1363)96c6b38 chore: publish <br>ubi based image (#1412)b43f58d add darwi<br>n builds (#1428)|
|2023-04-24 07:05:15|[dbeaver](https://github.com/dbeaver/dbeaver)|23.0.3|- General UI:- Issue with zoom in and o<br>ut with Ctrl++ and Ctrl+- in SQL Editor <br>and Data gird was fixed- ER Diagram font<br> now depends on the Main font- A lot of <br>UI rendering improvements were made- SQL<br> Editor:- Moving with Ctrl+Right/Left no<br>w considers words with an underscore and<br> a dollar as a whole word (configurable)<br>- Autocomplete for mixed-case was improv<br>ed- Issue with crashing when closing the<br> SQL Editor tab was fixed- Order by pars<br>ing was improved- AI: issue with changin<br>g settings was fixed- Data Editor:- Data<br> filters support in the Grouping panel w<br>as added- Opening TXT, JSON, and XML fil<br>es in external editors was improved on m<br>acOS and Linux- Rendering of non-display<br> characters was improved- Issue with dis<br>appearing filter option, when a query re<br>turns nothing, was fixed- Microseconds e<br>poch transformer was added (thanks to @B<br>obrPetr)- Database Navigator: issue with<br> creating a new view was fixed- Data tra<br>nsfer:- Issue with set max column length<br> when exporting in TXT was fixed- Issue <br>with export JSON to TXT was fixed- Datab<br>ases:- Firebird: recognition of procedur<br>e parameter data types was improved- SQL<br>ite: issue with database synchronization<br> with the server was fixed- Redshift: is<br>sue with renaming a view in Database Nav<br>igator was fixed- MySQL: issue with the <br>empty privileges list was fixed- Snowfla<br>ke: displaying the creation time of Snow<br>flake views was added- TiDB Cloud: telem<br>etry support was added (thanks to @Icema<br>p)- PostgreSQL: array presentation was i<br>mproved- Localization of Brazilian Portu<br>guese was improved (thanks to @brlarini)|
|2023-04-24 03:23:34|[fofax](https://github.com/xiecat/fofax)|v0.1.44|## Changelog* 修复更新时如果网络有问题<br>可能引发异常问题 #29 。修改弃用函数|
|2023-04-23 07:32:04|[mitaka](https://github.com/ninoseki/mitaka)|v1.2.0|- Remove abandoned/no longer maintained<br> searchers (#723)- Revamp FortiGuard sea<br>rcher (#724)- Support ThreatBook as a se<br>archer (#725)- Change TS mapping paths t<br>o follow Plasmo's default settings (#727<br>)- Make it possible to disable/scanners <br>in the options view (#728, #713)|
|2023-04-23 06:08:32|[OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL)|OA-EXPTOO<br>L-0.72|最近更新日志：泛微前台sql注入的poc验证<br>，暂无exp万户OA_UploadServlet.py万户OA_xf<br>ire_xxe优化poc的验证功能|
|2023-04-23 03:24:47|[Xray_Cracked](https://github.com/NHPT/Xray_Cracked)|v1.9.8|Xray 1.9.8 COMMUNITY-ADVANCED Windows,L<br>inux and Mac OS Version.xray_windows_amd<br>64.exeSHA256: E9E94E026B203D6D2FA1E98E0B<br>34D448408F9EF442C2ADC94F378DB824DC7270xr<br>ay_windows_386.exeSHA256: 3E973484110535<br>0CDB85C7DEB19231FCD5D9D4413F245DA53448C3<br>C37665492Bxray_darwin_amd64SHA256: 1405C<br>522622FBE43DEC8D2468C4DEB5C496BD02370B0C<br>9573BF9116F5D340C38xray_darwin_arm64SHA2<br>56: DEBDC4C8FA6C9A180F554BC4D0FA95B06AFE<br>3461D5549EDCB9483E8A53A48D1Exray_linux_a<br>md64SHA256: 002E9C31659160B44D0AADFC6856<br>E47F39401CD4F26840AE1DF7E0C6A147D359xray<br>_linux_arm64SHA256: 693C6D6251711B644C56<br>3EA0D30053433747D51247EF08D746428E0195BB<br>AB15|
|2023-04-22 13:09:02|[afrog](https://github.com/zan8in/afrog)|v2.2.3|optimization:- Customizable html report<br> report generation directoryPoC:- Added <br>22 PoCs-----------------优化：- 可自定义<br> html report 报告生成目录PoC:- 新增 22 P<br>oC|
|2023-04-22 09:01:57|[OneScan](https://github.com/vaycore/OneScan)|v1.0.0|1.0.0 版本发布，版本更新内容如下### 升<br>级提醒！！！！新版配置与旧版本不兼容，更<br>新前需要自行备份配置；以免各位想回退版本<br>的时候，出现配置文件报错的情况### 新增- <br>新增过滤规则可视化，将过滤规则文本框放到 <br>Filter 按钮左边- 新增Fingerprint指纹模块<br>- 新增随机内网IP动态变量{{random.local-i<br>p}}- 新增字典管理，可定义一系列字典，便<br>捷切换- 更新辅助信息面板UI，新增指纹信息<br>展示### 优化- 使用Gson作为项目的Json解析<br>库- 将默认Header配置中的{{random.ip}}修改<br>为{{random.local-ip}}- 优化黑白名单匹配规<br>则，添加*号匹配（支持格式：www.google.com<br>、*.google.com、*.google.*、www.google.*<br>、www.*.com）- 主动扫描时不进行黑白名单检<br>测- 自带的默认白名单不包含任何内容### 修<br>复- 修复Payload Processing处理异常的问题|
|2023-04-21 17:14:17|[grype](https://github.com/anchore/grype)|v0.61.1|# Changelog## [v0.61.1](https://github.<br>com/anchore/grype/tree/v0.61.1) (2023-04<br>-21)[Full Changelog](https://github.com/<br>anchore/grype/compare/v0.61.0...v0.61.1)<br>### Bug Fixes- :grey_question: Parsing d<br>pkg status: extracting key-value from li<br>ne:usr/lib/os-release err: cannot parse <br>field [[Issue #1195](https://github.com/<br>anchore/grype/issues/1195)]
- Grype sugg<br>esting to upgrade to a version already u<br>sed.[[Issue #1209](https://github.com/an<br>chore/grype/issues/1209)]### Additional <br>Changes- feat: add timestamp to json out<br>put (#1170) [[PR #1249](https://github.c<br>om/anchore/grype/pull/1249)] [[jneate](h<br>ttps://github.com/jneate)]|
|2023-04-21 16:24:14|[syft](https://github.com/anchore/syft)|v0.79.0|# Changelog## [v0.79.0](https://github.<br>com/anchore/syft/tree/v0.79.0) (2023-04-<br>21)[Full Changelog](https://github.com/a<br>nchore/syft/compare/v0.78.0...v0.79.0)##<br># Added Features- Add ALPM Metadata to C<br>YCLONEDX and SPDX output formats [[Issue<br> #1037](https://github.com/anchore/syft/<br>issues/1037)] [[PR #1747](https://github<br>.com/anchore/syft/pull/1747)] [[Shanedel<br>l](https://github.com/Shanedell)]- consu<br>l binary classifier [[Issue #1590](https<br>://github.com/anchore/syft/issues/1590)]<br> [[PR #1738](https://github.com/anchore/<br>syft/pull/1738)] [[Shanedell](https://gi<br>thub.com/Shanedell)]### Bug Fixes- Syft <br>missing direct dependencies from the gem<br>file.lock [[Issue #1660](https://github.<br>com/anchore/syft/issues/1660)] [[PR #174<br>9](https://github.com/anchore/syft/pull/<br>1749)] [[Shanedell](https://github.com/S<br>hanedell)]### Additional Changes- chore:<br> bump stereoscope to latest version [[PR<br> #1741](https://github.com/anchore/syft/<br>pull/1741)] [[westonsteimel](https://git<br>hub.com/westonsteimel)]|
|2023-04-21 14:16:08|[xray](https://github.com/chaitin/xray)|1.9.8|### 版本介绍该版本为 泛微 Ecology OA SQ<br>L 注入漏洞 的应急版本，相较上个版本，除<br>了添加了一个POC外，未改动其他内容。### 更<br>新内容想要检测该漏洞的师傅，可以使用./xra<br>y ws --poc poc-yaml-weaver-ecology-oa-pl<br>ugin-checkserver-setting-sqli --url http<br>://example.com进行检测。相关参考链接：[C<br>T stack](https://stack.chaitin.com/techb<br>log/detail?id=81)|
|2023-04-21 09:45:23|[Antenna](https://github.com/wuba/Antenna)|v1.3.5|1. 修复HTTPS分块传输请求导致处理逻辑错<br>误(#105)的问题2. 废弃domain_in查询方式(#1<br>06)，后续多个域名查询可使用多个domain参<br>数查询，详情可看http://blog.antenna.cool/<br>docs/api_back3. 新增api查询用户token以及<br>查询当前项目使用版本接口，为下个版本SDK与<br>自动更新功能做准备|
|2023-04-20 12:22:04|[safeline](https://github.com/chaitin/safeline)|v1.1.0|### 新增- 默认开启高防模式- 支持根据 IP<br> 和 URL 特征配置黑白名单### 优化- 支持在<br>日志详情中展示响应报文- 服务器时间不准导<br>致 TOTP 无法登录时增加了提示语- 修复了上<br>游服务器填 HTTPS 时端口解析不正确的问题- <br>优化了 SSL 上传逻辑，体验更好|
|2023-04-19 22:48:02|[nuclei](https://github.com/projectdiscovery/nuclei)|v2.9.2|## What's Changed* **Added llm_prompt a<br>s dsl helper** by @Mzack9999 in https://<br>github.com/projectdiscovery/nuclei/issue<br>s/3480yamlllm_prompt("what tech this ser<br>ver is using? return idk if you dont kno<br>w" + header)* Added **azure blob storage<br>** support for custom template download <br>by @kchason in https://github.com/projec<br>tdiscovery/nuclei/pull/3542* Added **git<br>lab project** support for custom templat<br>e downloadby @kchason in https://github.<br>com/projectdiscovery/nuclei/pull/3570* *<br>*Added CPE / EPSS Score information to c<br>ve-annotation**by @sduc in https://githu<br>b.com/projectdiscovery/nuclei/pull/3486*<br> **Added variable evaluation support in <br>payloads & variables** by @ShubhamRasal <br>in https://github.com/projectdiscovery/n<br>uclei/pull/3503* **Added config manageme<br>nt + logic refactor** by @tarunKoyalwar <br>in https://github.com/projectdiscovery/n<br>uclei/pull/3567* Added JSONL(ine) Export<br> (#3504) by @kchason in https://github.c<br>om/projectdiscovery/nuclei/pull/3505cons<br>ole-je, -json-export stringfile to expor<br>t results in JSON format* Fixed bug in h<br>ttp race condition logic by @ShubhamRasa<br>l in https://github.com/projectdiscovery<br>/nuclei/pull/3533* Fixed s3 argument typ<br>os by @kchason in https://github.com/pro<br>jectdiscovery/nuclei/pull/3536* Fixed in<br>tegration test by @tarunKoyalwar in http<br>s://github.com/projectdiscovery/nuclei/p<br>ull/3506* Fixed rate limit options not w<br>orking with query fuzzing by @RamanaRedd<br>y0M in https://github.com/projectdiscove<br>ry/nuclei/pull/3532* Fixed panic crash i<br>n tlsx by @ehsandeep in https://github.c<br>om/projectdiscovery/nuclei/pull/3554* Fi<br>xed panic with proxy input by @tarunKoya<br>lwar in https://github.com/projectdiscov<br>ery/nuclei/pull/3526* Updated -nc option<br> by @dogancanbakir in https://github.com<br>/projectdiscovery/nuclei/pull/3539* Upda<br>ted ccache with generic gcache by @Mzack<br>9999 in https://github.com/projectdiscov<br>ery/nuclei/pull/3523* Updated -un option<br> to -up as a short flag of self-update o<br>ption by @ehsandeep in https://github.co<br>m/projectdiscovery/nuclei/pull/3573Issue<br>s closed in this release - https://githu<br>b.com/projectdiscovery/nuclei/milestone/<br>29?closed=1## New Contributors* @sduc ma<br>de their first contribution in https://g<br>ithub.com/projectdiscovery/nuclei/pull/3<br>486* @dogancanbakir made their first con<br>tribution in https://github.com/projectd<br>iscovery/nuclei/pull/3539**Full Changelo<br>g**: https://github.com/projectdiscovery<br>/nuclei/compare/v2.9.1...v2.9.2|
|2023-04-19 04:40:00|[noterce](https://github.com/xiao-zhu-zhu/noterce)|v1.2|修复被控端不能更改note地址的bug感谢Expl<br>o1t师傅反馈|
|2023-04-18 00:34:58|[domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro)|v1.9|全局：多个bug修复布局模式优化基础方法实<br>现逻辑优化右键菜单：“Do Search”提供主动<br>在制定请求中进行搜索的能力，比如在某企业<br>邮箱的流量中搜索以提取邮箱地址“Add Reque<br>st And Comment”右键菜单添逻辑优化，修复<br>一个bug“Send To Tool Panel”右键菜单处理<br>逻辑优化，可合并发送多个数据包内容Domain<br>面板：root domain的comments逻辑更新提供多<br>个网络搜索引擎的后台自动搜索功能root doma<br>in双击，自动在浏览器中访问修改目标根域名<br>删除失败的bug显示序号，以便在排序后恢复原<br>始顺序Tool面板：重写JTextArea的paste函数<br>，避免大内容导致程序卡死JTextArea支持输入<br>文件，而程序处理其内容。文本取提供简单的<br>历史记录功能JSON提取逻辑优化新增多个功能<br>，比如排序优化URL提取逻辑，避免遗漏没有以<br>/开头的pathTitle面板中：端口扫描命令生成<br>逻辑优化备注和IP内容的显示优化，显示前排<br>序备注添加逻辑优化给手动添加的记录添加已<br>知的IP和CNAME、CertInfo搜索功能增强，支持<br>对数字型字段进行大于、小于、等于等搜索添<br>加多个搜索实例，以便用户熟悉搜索语法新增<br>“Do Request Item Again”菜单，对DNS记录<br>或无响应的数据包进行再次请求|
|2023-04-17 01:16:06|[AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool)|20230417|1. 效果优化|
|2023-04-16 22:40:19|[SSTImap](https://github.com/vladko312/SSTImap)|v1.1|- Crawler and form detection (by @fante<br>sykikachu)- New template engine added: C<br>heetah- Automatic import for engine modu<br>les- Interactive module reloading capabi<br>lity- Full support for Python 3.11- Repl<br>aced telnetlib with a custom TCP client|
|2023-04-16 13:30:59|[trivy](https://github.com/aquasecurity/trivy)|v0.40.0|## ⚡Release highlights and summary⚡👉<br> https://github.com/aquasecurity/trivy/d<br>iscussions/4074## Changelog* b43b19ba5 f<br>eat(flag): Support globstar for --skip-f<br>iles and --skip-directories (#4026)* 148<br>05002d chore(deps): bump actions/stale f<br>rom 7 to 8 (#3955)* 83bb97ab1 fix: retur<br>n insecure option to download javadb (#4<br>064)* 79a1ba32d fix(nodejs): don't stop <br>parsing when unsupported yarn.lock proto<br>cols are found (#4052)* ff1c43a79 ci: ad<br>d gpg signing for RPM packages (#4056)* <br>b608b116c fix(k8s): current context titl<br>e (#4055)* 2c3b60f4c fix(k8s): quit supp<br>ort on k8s progress bar (#4021)* a6b8642<br>13 chore: add a note about Dockerfile.ca<br>nary (#4050)* 90b80662c ci: fix path to <br>canary binaries (#4045)* dcefc6bf3 fix(v<br>uln): report architecture for debian pac<br>kages (#4032)* 601e25fb2 feat: add suppo<br>rt for Chainguard's commercial distro (#<br>3641)* 0bebec19f ci: bump goreleaser for<br> Github Action from 1.4.1 to 1.16.2 (#39<br>79)* 707ea9423 fix(vuln): fix error mess<br>age for remote scanners (#4031)* 8e1fe76<br>9e feat(report): add image metadata to S<br>ARIF (#4020)* 4b36e97dc docs: fix broken<br> cache link on Installation page (#3999)<br>* f0df725c5 fix: lock downloading polici<br>es and database (#4017)* 009675c82 fix: <br>avoid concurrent access to the global ma<br>p (#4014)* 3ed86aa3d feat(rust): add Car<br>go.lock v3 support (#4012)* f31dea4bd fe<br>at: auth support oci download server sub<br>command (#4008)* d37c50a2b chore(deps): <br>bump github.com/docker/docker (#4009)* 6<br>93d20516 chore: install.sh support for a<br>rmv7 (#3985)* 65d89b99d chore(deps): bum<br>p github.com/Azure/go-autorest/autorest/<br>adal (#3961)|
|2023-04-16 12:00:25|[WeblogicTool](https://github.com/KimJun1010/WeblogicTool)|v1.0||
|2023-04-15 01:34:31|[nemo_go](https://github.com/hanc00l/nemo_go)|v2.9.2|### Updated- 首页登录及后台更改密码时，<br>采用RSA加密传输（每次server启动生成随机RS<br>A密钥对）；- WEB页面修改XSCAN的默认配置<br>；优化XSCAN的选项，增加Nuclei漏洞扫描；- <br>增加输入任务参数长度校验（目标Targets不超<br>过5000个字符，输入参数总长度不超过6000个<br>字符）；- 增加WebServer API接口和Swagger<br>调试页面（为前后端分离提供支持）；- 将子<br>域名被动收集（Subfinder）及指纹获取（Http<br>x）功能由原通过源代码集成改用调用二进制<br>文件（解决和降低内存泄露、协程异常导致内<br>存和CPU占用异常的bug）；- 增加IP与资产的<br>黑名单功能及一键拉黑功能，对黑名单的资产<br>忽略指纹及漏洞任务、结果不会进行存储；- <br>更新纯真数据库；- ChangeLog；### Fix- 子<br>域名被动枚举（Subfinder）配置的provider-c<br>onfig.yaml未生效|
|2023-04-13 18:29:02|[clair](https://github.com/quay/clair)|v4.6.1|
## [Unreleased]## [v4.6.1] - 2023-04-1<br>3
### Airgap
- [e02aba27](https://github<br>.com/quay/clair/commit/e02aba27de01cb461<br>f79bee9644aac80c2f9bd65): Remove libinde<br>x Airgap option
### Chore
- [36990912](h<br>ttps://github.com/quay/clair/commit/3699<br>0912450fba2ccbef260a4829f1d9f69f45c6): v<br>4.6.1 changelog bump
- [e676671c](https:<br>//github.com/quay/clair/commit/e676671c1<br>7d2612470cd8de05aa668312fbb3036): Bump C<br>laircore to v1.4.21
### Go.Mod
- [36de97<br>cc](https://github.com/quay/clair/commit<br>/36de97ccf619113b1ef4dff6bfd0e0c69225254<br>4): update json (de)serializer
### Httpt<br>ransport
- [922f33d1](https://github.com<br>/quay/clair/commit/922f33d18919578049fbf<br>2ccb756e6990b66f280): fix request_id log<br>ging
### Httputil
- [9e8eacf5](https://g<br>ithub.com/quay/clair/commit/9e8eacf51b2a<br>45f967036396b3dc14a52edc480d): fix Parse<br>IP usage-[#1689](https://github.com/quay<br>/clair/issues/1689)### Notifier
- [ffa45<br>56d](https://github.com/quay/clair/commi<br>t/ffa4556d0f251cc984ed34594356625b9b7477<br>44): Avoid double reference[Unreleased]:<br> https://github.com/quay/clair/compare/v<br>4.6.1...HEAD
[v4.6.1]: https://github.co<br>m/quay/clair/compare/v4.6.0...v4.6.1
|
|2023-04-13 01:59:30|[captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified)|0.23-beta<br>5|【2023-4-13】 0.23-beta5- 修复验证码获<br>取接口中请求头字段置空无法获取验证码的问<br>题感谢微信群师傅 _隔壁老钱 反馈|
|2023-04-12 08:22:22|[ZoomEye-python](https://github.com/knownsec/ZoomEye-python)|v2.2.0|### update- remove username and passwor<br>d authenticate method, only support API-<br>KEY authenticate.### 更新- 移除用户名和<br>密码的认证方式，仅支持 API- KEY 认证。|
|2023-04-12 07:54:54|[RequestTemplate](https://github.com/1n7erface/RequestTemplate)|v1.1.5|2023.4.12 16:001.解决了一个并发时线程抢<br>锁问题2.添加指纹，目前指纹900+3.添加ps,us<br>参数|
|2023-04-12 06:53:40|[iDefender](https://github.com/wecooperate/iDefender)|2.6.0|增强稳定性、易用性，建议更新（感谢很多<br>热心网友的建议）- **添加学习模式**- 在学<br>习模式下，只会旁路监控来学习、观察规则的<br>使用和设置，实际不会拦截任何事件- 可以用<br>这种方式来建立白名单- 增强信任列表- 支持<br>手动添加、编辑- 不是弹框拦截规则也支持添<br>加信任- 增强拦截记录交互- 支持右键添加信<br>任的目标- 优化性能- 优化系统启动过程的一<br>些规则设置- 去掉规则引擎执行线程所有的文<br>件操作- 优化UI线程被阻塞后，导致系统短暂<br>卡死的问题- 修复一些场景导致启动卡住的问<br>题- 模板更新-**添加快速模板（拦截模式）**<br>-**添加快速模板（信任模式）**- 添加拦截<br>进程启动子进程模板- 添加忽略系统初始化过<br>程的规则模板- 优化一些内置模板导致误报弹<br>框的- 其他- 调整模板更新逻辑- 修复启动到<br>托盘闪一下界面的问题- 高级模板的一些字段<br>命名做了中文翻译- 修复专家策略设置错误格<br>式导致崩溃的问题- 修复进程路径选择的时候<br>选择成进程名的问题- 优化自保护跟卡巴斯基<br>冲突的问题- 优化一些使用体验问题软件下载|
## 近15天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
|2023-04-27 00:35:58|[feroxbuster](https://github.com/epi052/feroxbuster)|Merge pull request #889 from epi052/all-contributors/a<br>dd-lavafrothdocs: add lavafroth as a contributor for co<br>de, and ideas|
|2023-04-27 00:30:16|[NucleiTP](https://github.com/ExpLangcn/NucleiTP)|更新啦❤️|
|2023-04-27 00:06:13|[neuvector](https://github.com/neuvector/neuvector)|Merge pull request #760 from jeffhuang4704/7731_add_im<br>agePullPolicy_for_customRuleNVSHAS-7731-add imagePullPo<br>licy for pod template|
|2023-04-26 23:12:50|[PocOrExp_in_Github](https://github.com/ycdxsb/PocOrExp_in_Github)|update 2023-04-27 07:12:50|
|2023-04-26 20:42:43|[syft](https://github.com/anchore/syft)|chore: update test redactor ordering (#1765)Signed-off<br>-by: Keith Zantow |
|2023-04-26 14:29:38|[log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner)|Update README.md|
|2023-04-26 13:18:52|[PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book)|漏洞相关:JeecgBoot,KubeOperator,KubePi|
|2023-04-26 13:10:06|[dbeaver](https://github.com/dbeaver/dbeaver)|dbeaver/pro#1551 update pg driver to 42.5.2 (#19716)|
|2023-04-26 10:32:11|[safeline](https://github.com/chaitin/safeline)|Merge pull request #43 from naocanmonster/main调整了文<br>档的目录结构|
|2023-04-26 10:21:08|[appshark](https://github.com/bytedance/appshark)|bugfix: profiler serve delay when CPU is overload.|
|2023-04-26 08:48:51|[RouteVulScan](https://github.com/F6JO/RouteVulScan)|Merge pull request #25 from No-Github/main优化规则,降<br>低误报|
|2023-04-25 21:26:26|[slowhttptest](https://github.com/shekyan/slowhttptest)|updated Dockerfile to use Alpine 3.17 from issue #80 (<br>#81)Co-authored-by: Brian Riffle |
|2023-04-25 19:16:43|[Stowaway](https://github.com/ph4ntonn/Stowaway)|Update README|
|2023-04-25 17:10:35|[Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)|update v1.3.4|
|2023-04-25 15:05:49|[PEASS-ng](https://github.com/carlospolop/PEASS-ng)|Merge pull request #350 from Donovoi/masterfix path to<br>o long|
|2023-04-25 11:47:25|[trivy](https://github.com/aquasecurity/trivy)|feat(sbom): add primary package purpose field for SPDX<br> (#4119)|
|2023-04-25 11:19:28|[domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro)|删除非目标记录 逻辑更新|
|2023-04-25 08:12:35|[Elkeid](https://github.com/bytedance/Elkeid)|update:driver CI wget|
|2023-04-25 07:10:09|[autoDecoder](https://github.com/f0ng/autoDecoder)|Update README.md|
|2023-04-25 06:23:58|[heapdump_tool](https://github.com/wyzxxz/heapdump_tool)|Update README.md|
|2023-04-25 04:00:29|[afrog](https://github.com/zan8in/afrog)|update contribute|
|2023-04-25 03:51:00|[veinmind-tools](https://github.com/chaitin/veinmind-tools)|feat(veinmind-iac): add dockerfile security detection <br>(#228)* feat(plugins): add ftp protocol support in plug<br>indocs(plugins): fix Readme table bug* docs(plugins): a<br>dd ftp protocol support in plugin* feat(plugins): updat<br>e dependency version* feat(plugins): add ftp protocol s<br>upport in weekpass plugin* Refactor(plugins-weakpass): <br>change Mod name to Service name mapping from one-to-one<br> to one-to-many* Test(plugins-weakpass): Add unit tests<br> for ftp service* Test(plugins-weakpass): Add unit test<br>s for ftp service* feat(veinmind-iac): add dockerfile s<br>ecurity detection* test(veinmind-iac): add dockerfile s<br>ecurity detection tests* fix(veinmind-iac): fix format <br>bug* Test(veinmind-iac): Add unit tests for dockerfile <br>detection|
|2023-04-25 03:38:19|[knife](https://github.com/bit4woo/knife)|v2.2|
|2023-04-25 03:10:33|[URLFinder](https://github.com/pingc0y/URLFinder)|Update result.go2023/4/25|
|2023-04-24 18:49:01|[grype](https://github.com/anchore/grype)|chore(deps): bump github/codeql-action from 2.2.12 to <br>2.3.0 (#1256)Bumps [github/codeql-action](https://githu<br>b.com/github/codeql-action) from 2.2.12 to 2.3.0.- [Rel<br>ease notes](https://github.com/github/codeql-action/rel<br>eases)- [Changelog](https://github.com/github/codeql-ac<br>tion/blob/main/CHANGELOG.md)- [Commits](https://github.<br>com/github/codeql-action/compare/7df0ce34898d659f95c0c4<br>a09eaa8d4e32ee64db...b2c19fb9a2a485599ccf4ed5d65527d94b<br>c57226)---updated-dependencies:- dependency-name: githu<br>b/codeql-actiondependency-type: direct:productionupdate<br>-type: version-update:semver-minor...Signed-off-by: dep<br>endabot[bot]Co-authored-by: dependabot[bot] |
|2023-04-24 18:29:30|[clair](https://github.com/quay/clair)|chore: Remove 1.19Updating the go version CI matrix as<br> we bumped the go.mod go directive
to 1.20 and are rely<br>ing on some 1.20 features for upcoming changes.Signed-o<br>ff-by: crozzy |
|2023-04-24 15:55:03|[faker](https://github.com/joke2k/faker)|Bump version: 18.5.0 → 18.5.1|
|2023-04-24 14:14:31|[K8tools](https://github.com/k8gege/K8tools)|Add files via upload|
|2023-04-24 14:03:52|[Ladon](https://github.com/k8gege/Ladon)|Add files via upload|
|2023-04-24 13:06:57|[sqlmap](https://github.com/sqlmapproject/sqlmap)|Disabled hostname and certificate validation for TLSv1<br>.3 support. (#5395)|
|2023-04-24 13:04:07|[Antenna](https://github.com/wuba/Antenna)|Merge pull request #117 from wuba/developDevelop|
|2023-04-24 09:21:41|[aksk_tool](https://github.com/wyzxxz/aksk_tool)|Update README.md|
|2023-04-24 09:07:59|[Komo](https://github.com/komomon/Komo)|Update sensitiveinfo_main.py|
|2023-04-24 08:43:59|[Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki)|更新漏洞|
|2023-04-24 08:40:43|[Awesome-POC](https://github.com/Threekiii/Awesome-POC)|更新漏洞|
|2023-04-24 08:02:19|[kube-bench](https://github.com/aquasecurity/kube-bench)|release: prepare v0.6.13 (#1429)Signed-off-by: chenk |
|2023-04-24 07:24:25|[FrameScan-GUI](https://github.com/qianxiao996/FrameScan-GUI)|Update config.ini|
|2023-04-24 06:48:58|[Xray_Cracked](https://github.com/NHPT/Xray_Cracked)|Update README.md|
|2023-04-24 03:20:26|[fofax](https://github.com/xiecat/fofax)|发布因网络导致的更新异常|
|2023-04-23 17:54:49|[CVE-2023-21839](https://github.com/4ra1n/CVE-2023-21839)|Update README.md|
|2023-04-23 08:52:16|[go_proxy_pool](https://github.com/pingc0y/go_proxy_pool)|Update README.md|
|2023-04-23 07:26:13|[mitaka](https://github.com/ninoseki/mitaka)|Merge pull request #729 from ninoseki/v1.2.0v1.2.0|
|2023-04-23 06:05:21|[OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL)|Add files via upload|
|2023-04-23 02:53:50|[dismap](https://github.com/zhzyker/dismap)|Merge pull request #33 from BigTree975/patch-1Update r<br>ule.go|
|2023-04-23 02:33:34|[404StarLink](https://github.com/knownsec/404StarLink)|weekly update at 2023-04-23|
|2023-04-22 09:47:26|[SmsForwarder](https://github.com/pppscn/SmsForwarder)|修复：CactusSave中SharedPreference的键值对应错误 #294|
|2023-04-22 08:34:27|[OneScan](https://github.com/vaycore/OneScan)|针对1.0.0版本更新README说明文档及截图|
|2023-04-21 15:19:18|[ffuf](https://github.com/ffuf/ffuf)|Fix md output format (#672)* Fix MD output* Add CHANGE<br>LOG.md entry|
|2023-04-21 07:09:50|[Pentest-Windows](https://github.com/arch3rPro/Pentest-Windows)|Update README.md|
|2023-04-21 06:44:01|[swagger-exp](https://github.com/lijiejie/swagger-exp)|Merge pull request #13 from lanyi1998/masterfeat:suppo<br>rt mac|
|2023-04-21 02:28:30|[HackBrowserData](https://github.com/moonD4rk/HackBrowserData)|Merge pull request #213 from liumingxing/masterSupport<br> SessionStorage export|
|2023-04-20 15:04:09|[BurpSuite-collectio<br>ns](https://github.com/Mr-xn/BurpSuite-collections)|add burpsuite_hack、BypassPro插件|
|2023-04-20 11:28:35|[Scanners-Box](https://github.com/We5ter/Scanners-Box)|[+]lijiejie/MisConfig_HTTP_Proxy_Scanner|
|2023-04-19 22:46:46|[nuclei](https://github.com/projectdiscovery/nuclei)|Merge pull request #3573 from projectdiscovery/devnucl<br>ei v2.9.2|
|2023-04-19 15:11:04|[fshzqSearch](https://github.com/Ifory885/fshzqSearch)|Update quake_search.py|
|2023-04-19 13:35:30|[koko-moni](https://github.com/burpheart/koko-moni)|Update readme.md|
|2023-04-19 12:00:21|[ysoserial](https://github.com/su18/ysoserial)|更新 Agent Filter 中间件 Hook 点|
|2023-04-19 07:07:20|[Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam)|更新README.md|
|2023-04-19 05:37:56|[0day](https://github.com/helloexp/0day)|add CVE-2023-23397 exp|
|2023-04-19 04:29:51|[noterce](https://github.com/xiao-zhu-zhu/noterce)|Update server.go1.2 修复被控端不能更改地址的bug|
|2023-04-18 10:06:15|[DecodeSomeJSPWebshe<br>ll](https://github.com/minhangxiaohui/DecodeSomeJSPWebshell)|Update README.md哥斯拉解密的时候的具体使用方法没有描述<br>清除，导致我自己很久没用这个工具之后也忘记使用方法了，所<br>以这里更新下描述文件，添加了哥斯拉的解密case样例|
|2023-04-18 09:05:55|[murphysec](https://github.com/murphysecurity/murphysec)|Revert "refactor: remove task id config"This reverts c<br>ommit 81b819f565c9da309b6b42c47815cd9607647862.|
|2023-04-18 07:17:13|[vulnerability](https://github.com/lal0ne/vulnerability)|CVE-2019-7609|
|2023-04-17 14:33:13|[WeblogicTool](https://github.com/KimJun1010/WeblogicTool)|Update README.md|
|2023-04-17 08:34:38|[v2rayA](https://github.com/v2rayA/v2rayA)|Merge pull request #917 from Gh0u1L5/feat_v5|
|2023-04-17 07:42:21|[ddddocr](https://github.com/sml2h3/ddddocr)|Update README.md|
|2023-04-17 07:04:15|[WebGoat](https://github.com/WebGoat/WebGoat)|Fix typo of HijackSession_content0.adoc|
|2023-04-17 01:34:19|[OneForAll](https://github.com/shmilylty/OneForAll)|Merge pull request #308 from mastomii/adding-massdns-l<br>inux-aarch64adding "massdns-linux-aarch64"|
|2023-04-17 01:17:36|[AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool)|Update README.md|
|2023-04-16 22:36:36|[SSTImap](https://github.com/vladko312/SSTImap)|Release of SSTImap version 1.1.0Crawler and form detec<br>tion (by @fantesykikachu)New template engine added: Che<br>etahAutomatic import for engine modulesInteractive modu<br>le reloading capabilityFull support for Python 3.11Repl<br>aced telnetlib with a custom TCP client---------Co-auth<br>ored-by: fantesykikachu |
|2023-04-15 11:44:52|[revsuit](https://github.com/Li4n0/revsuit)|ci: disable cgo|
|2023-04-15 01:26:43|[nemo_go](https://github.com/hanc00l/nemo_go)|Update: Release v2.9.2|
|2023-04-12 07:44:49|[ZoomEye-python](https://github.com/knownsec/ZoomEye-python)|Merge pull request #87 from knownsec/devupdate():remov<br>e username and password authenticate method|
|2023-04-12 07:23:36|[xray](https://github.com/chaitin/xray)|[update] POC贡献流程|
|2023-04-12 07:14:03|[About-Attack](https://github.com/lintstar/About-Attack)|Update README.md项目页面重构 https://red.lintstar.top/<br>Attack/|
|2023-04-12 06:08:21|[Library-POC](https://github.com/luck-ying/Library-POC)|Update README.md|
|2023-04-12 02:41:31|[rengine](https://github.com/yogeshojha/rengine)|Merge pull request #877 from AnonymousWP/fix-incorrect<br>-numbering-in-readmedocs(readme): fix numbered list|## 所有项目
# 渗透测试
## 信息收集
### 资产测绘采集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll) | V1.2 | 为了方便安全从业人员在使用网络测绘平台进行信息搜集时的效率，本程<br>序集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并且合<br>并展示及导出。 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | v2.3.3 | 【支持Fofa、Zoomeye、Quake等网络空间搜索引擎】闪电搜索器；GUI图<br>形化渗透测试信息搜集工具；资产搜集引擎 |
| [Search_Viewer](https://github.com/G3et/Search_Viewer) | v2.0 | 集Fofa、Hunter鹰图、Shodan、360 quake、Zoomeye 钟馗之眼为一体的g<br>ui图形界面化工具 |
| [koko-moni](https://github.com/burpheart/koko-moni) | v0.0.1 | 一个网络空间搜索引擎监控平台，可定时进行资产信息爬取，及时发现新<br>增资产，本项目聚合了 Fofa、Hunter、Quake、Zoomeye 和 Threatbook 的<br>数据源，并对获取到的数据进行去重与清洗 |
| [AsamF](https://github.com/Kento-Sec/AsamF) | v0.1.10 | AsamF是集成Fofa、Quake、Hunter、Shodan、Zoomeye、Chinaz、0.zone<br>及爱企查的一站式企业信息资产收集、网络资产测绘工具。 |
| [fshzqSearch](https://github.com/Ifory885/fshzqSearch) |  | fofa、shodan、hunter、zoomeye、quake网络空间搜索引擎及github聚合<br>搜索，并对结果进行finger指纹识别。 |
### 子域名收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [subfinder](https://github.com/projectdiscovery/subfinder) | v2.5.7 | Fast passive subdomain enumeration tool. |
| [ksubdomain](https://github.com/knownsec/ksubdomain) | v0.7 | 无状态子域名爆破工具 |
| [OneForAll](https://github.com/shmilylty/OneForAll) | v0.4.5 | OneForAll是一款功能强大的子域收集工具 |
| [LangSrcCurise](https://github.com/LangziFun/LangSrcCurise) |  | SRC子域名资产监控 |
| [github-subdomains](https://github.com/gwen001/github-subdomains) | v1.2.2 | Find subdomains on GitHub. |
| [LayerDomainFinder](https://github.com/euphrat1ca/LayerDomainFinder) | 3 | Layer子域名挖掘机 |
| [dnsub](https://github.com/yunxu1/dnsub) | v2.1 | dnsub一款好用且强大的子域名扫描工具 |
| [ksubdomain](https://github.com/boy-hack/ksubdomain) | v1.9.5 | Subdomain enumeration tool, asynchronous dns packets, use pcap t<br>o scan 1600,000 subdomains in 1 second |
| [ct](https://github.com/knownsec/ct) | v1.0.9 | 简单易用的域名爆破工具 |
| [subDomainsBrute](https://github.com/lijiejie/subDomainsBrute) | v1.4 | A fast sub domain brute tool for pentesters |
### 目录扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dirsearch](https://github.com/maurosoria/dirsearch) | v0.4.3 | Web path scanner |
| [feroxbuster](https://github.com/epi052/feroxbuster) | v2.9.5 | A fast, simple, recursive content discovery tool written in Rust<br>. |
| [ffuf](https://github.com/ffuf/ffuf) | v2.0.0 | Fast web fuzzer written in Go |
| [dirmap](https://github.com/H4ckForJob/dirmap) |  | An advanced web directory & file scanning tool that will be more<br> powerful than DirBuster, Dirsearch, cansina, and Yu Jian.一个高<br>级web目录、文件扫描工具，功能将会强于DirBuster、Dirsearch、cansina<br>、御剑。 |
| [cansina](https://github.com/deibit/cansina) | 1.0.0 | Web Content Discovery Tool |
| [urlbrute](https://github.com/ReddyyZ/urlbrute) | v1.0.2 | Directory/Subdomain scanner developed in GoLang. |
| [yjdirscan](https://github.com/foryujian/yjdirscan) | yjdirscan | 御剑目录扫描专业版，简单实用的命令行网站目录扫描工具，支持爬虫、<br>fuzz、自定义字典、字典变量、UA修改、假404自动过滤、扫描控速等功能<br>。 |
| [SWebScan](https://github.com/shack2/SWebScan) | 5.0.2018.<br>08.21 | SWebScan是一款基于C#的Web目录扫描器。 |
| [yuhScan](https://github.com/hunyaio/yuhScan) | v1.0 | web目录快速扫描工具 |
| [gospider](https://github.com/jaeles-project/gospider) | v1.1.6 | Gospider - Fast web spider written in Go |
| [rad](https://github.com/chaitin/rad) | 0.4 |  |
| [URLFinder](https://github.com/pingc0y/URLFinder) | 2023.2.21 | 一款快速、全面、易用的页面信息提取工具，可快速发现和提取页面中的<br>JS、URL和敏感信息。 |
| [JSFinder](https://github.com/Threezh1/JSFinder) |  | JSFinder is a tool for quickly extracting URLs and subdomains fr<br>om JS files on a website. |
| [BBScan](https://github.com/lijiejie/BBScan) | v1.5 | A fast vulnerability scanner |
### 指纹识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EHole](https://github.com/EdgeSecurityTeam/EHole) | 3.0 | EHole(棱洞)3.0 重构版-红队重点攻击系统指纹探测工具 |
| [Glass](https://github.com/s7ckTeam/Glass) |  | Glass是一款针对资产列表的快速指纹识别工具，通过调用Fofa/ZoomEye/<br>Shodan/360等api接口快速查询资产信息并识别重点资产的指纹，也可针对<br>IP/IP段或资产列表进行快速的指纹识别。 |
| [Finger](https://github.com/EASY233/Finger) |  | 一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具 |
### WAF识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [identYwaf](https://github.com/stamparm/identYwaf) |  | Blind WAF identification tool |
### 端口扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [webfinder-next](https://github.com/Liqunkit/webfinder-next) |  | 对小米范webfinder http://www.cnblogs.com/SEC-fsq/p/5610981.html <br>进行了小修改 |
| [yujianportscan](https://github.com/foryujian/yujianportscan) |  | 一个基于VB.NET + IOCP模型开发的高效端口扫描工具，支持IP区间合并<br>，端口区间合并，端口指纹深度探测 |
| [TXPortMap](https://github.com/4dogs-cn/TXPortMap) | v1.1.2 | Port Scanner & Banner Identify From TianXiang |
| [naabu](https://github.com/projectdiscovery/naabu) | v2.1.5 | A fast port scanner written in go with a focus on reliability an<br>d simplicity. Designed to be used in combination with other tools<br> for attack surface discovery in bug bounties and pentests |
| [scaninfo](https://github.com/redtoolskobe/scaninfo) | v1.1.0 | fast scan for redtools |
| [portscan](https://github.com/20142995/portscan) |  |  |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dismap](https://github.com/zhzyker/dismap) | v0.4 | Asset discovery and identification tools 快速识别 Web 指纹信息，<br>定位资产类型。辅助红队快速定位目标资产信息，辅助蓝队发现疑似脆弱点 |
| [AssetsHunter](https://github.com/rabbitmask/AssetsHunter) |  | 资产狩猎框架-AssetsHunter，信息收集是一项艺术~ |
| [TScan](https://github.com/dyboy2017/TScan) |  | TScan 提供了CMS指纹识别、端口扫描、旁站信息、信息泄漏等功能，期<br>许在最短的时间辅助安全人员在渗透前做好充分的信息搜集 |
### 自动化信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [H](https://github.com/SiJiDo/H) |  | H是一款强大的资产收集管理平台 |
| [X-Marshal](https://github.com/XTeam-Wing/X-Marshal) |  | Golang-分布式资产探测&漏洞扫描&外部攻击面管理 |
| [heartsk_community](https://github.com/yqcs/heartsk_community) | LOWBUG@La<br>test | Hearts K-企业资产发现与脆弱性检查工具，自动化资产信息收集与漏洞<br>扫描 |
| [AnScan](https://github.com/Arbor01/AnScan) |  | AnScan是一款集合信息收集、分布式漏洞扫描、漏洞POC管理等为一体的<br>红队扫描工具 |
| [nemo_go](https://github.com/hanc00l/nemo_go) | v2.9.2 | Nemo是用来进行自动化信息收集的一个简单平台，通过集成常用的信息收<br>集工具和技术，实现对内网及互联网资产信息的自动收集，提高隐患排查和<br>渗透测试的工作效率。 |
| [rengine](https://github.com/yogeshojha/rengine) | v1.3.6 | reNgine is an automated reconnaissance framework for web applica<br>tions with a focus on highly configurable streamlined recon proce<br>ss via Engines, recon data correlation and organization, continuo<br>us monitoring, backed by a database, and simple yet intuitive Use<br>r Interface. reNgine makes it easy for penetration testers to gat<br>her reconnaissance with minimal configuration and with the help o<br>f reNgine's correlation, it just makes recon effortless. |
| [ShuiZe_0x727](https://github.com/0x727/ShuiZe_0x727) | v1.0 | 信息收集自动化工具 |
| [DBJ](https://github.com/wgpsec/DBJ) |  | 大宝剑-边界资产梳理工具（红队、蓝队、企业组织架构、子域名、Web资<br>产梳理、Web指纹识别、ICON_Hash资产匹配） |
| [Voyager](https://github.com/xundididi/Voyager) |  | 一个安全工具集合平台，用来提高乙方安全人员的工作效率，请勿用于非<br>法项目 |
| [GoScan](https://github.com/CTF-MissFeng/GoScan) |  | GoScan是采用Golang语言编写的一款分布式综合资产管理系统，适合红队<br>、SRC等使用 |
| [Autoscanner](https://github.com/zongdeiqianxing/Autoscanner) | v1.2.1 | 输入域名>爆破子域名>扫描子域名端口>发现扫描web服务>集成报告的全<br>流程全自动扫描器。集成oneforall、masscan、nmap、dirsearch、crawler<br>go、xray等工具，另支持cdn识别、网页截图、站点定位；动态识别域名并<br>添加功能、工具超时中断等 |
| [MagiCude](https://github.com/er10yi/MagiCude) | v2.1 | 分布式端口（漏洞）扫描、资产安全管理、实时威胁监控与通知、高效漏<br>洞闭环、漏洞wiki、邮件报告通知、poc框架 |
| [Watchdog](https://github.com/CTF-MissFeng/Watchdog) |  | Watchdog是bayonet修改版，重新优化了数据库及web及扫描程序,加入多<br>节点 |
| [Tide](https://github.com/TideSec/Tide) |  | 目前实现了网络空间资产探测、指纹检索、漏洞检测、漏洞全生命周期管<br>理、poc定向检测、暗链检测、挂马监测、敏感字检测、DNS监测、网站可用<br>性监测、漏洞库管理、安全预警等等~ |
| [ARL](https://github.com/TophantTechnology/ARL) | v2.5.4 | ARL(Asset Reconnaissance Lighthouse)资产侦察灯塔系统旨在快速侦察<br>与目标关联的互联网资产，构建基础资产信息库。 协助甲方安全团队或者<br>渗透测试人员有效侦察和检索资产，发现存在的薄弱点和攻击面。 |
| [linglong](https://github.com/awake1t/linglong) |  | 一款甲方资产巡航扫描系统。系统定位是发现资产，进行端口爆破。帮助<br>企业更快发现弱口令问题。主要功能包括: 资产探测、端口爆破、定时任务<br>、管理后台识别、报表展示 |
| [sec-admin](https://github.com/smallcham/sec-admin) |  | 分布式资产安全扫描核心管理系统(弱口令扫描，漏洞扫描) |
| [linbing](https://github.com/taomujian/linbing) | v3.0 | 本系统是对Web中间件和Web框架进行自动化渗透的一个系统,根据扫描选<br>项去自动化收集资产,然后进行POC扫描,POC扫描时会根据指纹选择POC插件<br>去扫描,POC插件扫描用异步方式扫描.前端采用vue技术,后端采用python fa<br>stapi. |
| [Vulcan](https://github.com/XTeam-Wing/Vulcan) |  | VulCan资产管理系统|漏洞扫描|资产探测|定时扫描 |
| [bayonet](https://github.com/CTF-MissFeng/bayonet) | v1.1 | bayonet是一款src资产管理系统，从子域名、端口服务、漏洞、爬虫等一<br>体化的资产管理系统 |
| [fuxi](https://github.com/jeffzh3ng/fuxi) |  | Penetration Testing Platform |
| [WebScan](https://github.com/xuchaoa/WebScan) |  | 正在写的一个资产管理和扫描相结合的分布式扫描器 |
| [xunfeng](https://github.com/ysrc/xunfeng) | v0.1.1 | 巡风是一款适用于企业内网的漏洞快速应急，巡航扫描系统。 |
| [AppInfoScanner](https://github.com/kelvinBen/AppInfoScanner) | V1.0.9_Re<br>leases | 一款适用于以HW行动/红队/渗透测试团队为场景的移动端(Android、iOS<br>、WEB、H5、静态网站)信息收集扫描工具，可以帮助渗透测试工程师、攻击<br>队成员、红队成员快速收集到移动端或者静态WEB站点中关键的资产信息并<br>提供基本的信息输出,如：Title、Domain、CDN、指纹信息、状态信息等。 |
| [Sec-Tools](https://github.com/jwt1399/Sec-Tools) |  | 🍉一款基于Python-Django的多功能Web安全渗透测试工具，包含漏洞扫描<br>，端口扫描，指纹识别，目录扫描，旁站扫描，域名扫描等功能。 |
| [Komo](https://github.com/komomon/Komo) |  | 🚀Komo, a comprehensive asset collection and vulnerability scann<br>ing tool. Komo 一个综合资产收集和漏洞扫描工具，集成了20余款工具，<br>通过多种方式对子域进行获取，收集域名邮箱，进行存活探测，域名指纹识<br>别，域名反查ip，ip端口扫描，web服务链接爬取并发送给xray，对web服务<br>进行POC漏洞扫描，对主机进行主机漏洞扫描。 |
### 企业信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ENScan_GO](https://github.com/wgpsec/ENScan_GO) | 0.0.10 | 一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息<br>收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚<br>合导出。 |
### 小程序信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [wxapkgUnpack](https://github.com/jdr2021/wxapkgUnpack) | 1.0 | wxapkg解密解包工具，提供C#和wxappUnpacker两个版本的解包，并提取J<br>S中的URL和IP。 |
### C段信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [IPSearch](https://github.com/SleepingBag945/IPSearch) | v0.1 | 离线IP Whois查询工具。可根据IP查询所属IP段信息、根据关键词查询IP<br>段信息 |
### IP反查域名
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [iplookup](https://github.com/Lengso/iplookup) | v1.1 | IP反查域名 |
### 反查域名
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ipInfoSearch](https://github.com/Potato-py/ipInfoSearch) |  | ip域名反查、权重查询以及ICP备案查询。便于提交SRC时资产过滤。 |
### 域名信息查询
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [QueryTools](https://github.com/z-bool/QueryTools) |  | IP/域名资产验证神器(补天|权重、CNVD|注册资金)-功能(IP反查域名、<br>域名备案、ICP资产、公司注册资金、权重、IP定位)快速验证是否为需求资<br>产 |
### apk
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ApkAnalyser](https://github.com/TheKingOfDuck/ApkAnalyser) |  | 一键提取安卓应用中可能存在的敏感信息。 |
## 漏洞发现
### 漏洞扫描框架
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pocsuite3](https://github.com/knownsec/pocsuite3) | v2.0.3 | pocsuite3 is an open-sourced remote vulnerability testing framew<br>ork developed by the Knownsec 404 Team. |
| [Godscan](https://github.com/Guoke324/Godscan) | Godscan | Godscan 是一款python编写的具有图形化界面的漏洞检测框架，可以之定<br>义漏洞检测 poc ，主要是帮助安全测试者，更好的去记录和整理历史漏洞<br>，以便更好的进行漏洞检测，提高工作效率！ |
| [FrameScan-GUI](https://github.com/qianxiao996/FrameScan-GUI) | v1.4.3 | FrameScan-GUI 一款python3和Pyqt编写的具有图形化界面的cms漏洞检测<br>框架。 |
| [Gr33k](https://github.com/lijiaxing1997/Gr33k) |  | 图形化漏洞利用集成工具 |
| [kunpeng](https://github.com/opensec-cn/kunpeng) | 20190527 | kunpeng是一个Golang编写的开源POC框架/库，以动态链接库的形式提供<br>各种语言调用，通过此项目可快速开发漏洞检测类的系统。 |
| [pocassist](https://github.com/jweny/pocassist) | 1.0.5 | 傻瓜式漏洞PoC测试框架 |
### 半自动漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EasyPen](https://github.com/lijiejie/EasyPen) |  | EasyPen is a GUI program which helps pentesters do target discov<br>ery, vulnerability scan and exploitation |
| [xray](https://github.com/chaitin/xray) | 1.9.8 | 一款完善的安全评估工具，支持常见 web 安全问题扫描和自定义 poc | <br>使用之前务必先阅读文档 |
| [w13scan](https://github.com/w-digital-scanner/w13scan) |  | Passive Security Scanner (被动式安全扫描器) |
| [Fvuln](https://github.com/d3ckx1/Fvuln) | Fvuln_v1.<br>4.8 | F-vuln（全称：Find-Vulnerability）是为了自己工作方便专门编写的一<br>款自动化工具，主要适用于日常安全服务、渗透测试人员和RedTeam红队人<br>员，它集合的功能包括：存活IP探测、开放端口探测、web服务探测、web漏<br>洞扫描、smb爆破、ssh爆破、ftp爆破、mssql爆破等其他数据库爆破工作以<br>及大量web漏洞检测模块。 |
| [nuclei](https://github.com/projectdiscovery/nuclei) | v2.9.2 | Fast and customizable vulnerability scanner based on simple YAML<br> based DSL. |
| [afrog](https://github.com/zan8in/afrog) | v2.2.3 | A Vulnerability Scanning Tools For Penetration Testing |
| [vulmap](https://github.com/zhzyker/vulmap) | v0.9 | Vulmap 是一款 web 漏洞扫描和验证工具, 可对 webapps 进行漏洞扫描,<br> 并且具备漏洞验证功能 |
| [POC-bomber](https://github.com/tr0uble-mAker/POC-bomber) | v2.0.2-PO<br>C-bomber | 利用大量高威胁poc/exp快速获取目标权限，用于渗透和红队快速打点 |
| [QingTing](https://github.com/StarCrossPortal/QingTing) | v0.3 | 蜻蜓安全一个安全工具编排平台,可以自由编排你的工具流,集成108款工<br>具,包括xray、nmap、awvs等;你可以将喜欢的工具编排成一个场景，快速打<br>造适合自己的安全工作台~ |
| [myscan](https://github.com/amcai/myscan) |  | myscan被动扫描 |
### 中间件&框架漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WeblogicScan](https://github.com/rabbitmask/WeblogicScan) |  | Weblogic一键漏洞检测工具，V1.5，更新时间：20200730 |
| [weblogic-infodetect<br>or](https://github.com/woodpecker-appstore/weblogic-infodetector) | 0.2.4 | woodpecker框架weblogic信息探测插件 |
| [Jiraffe](https://github.com/0x48piraj/Jiraffe) | v2.0.6 | One stop place for exploiting Jira instances in your proximity |
| [Artillery](https://github.com/Weik1/Artillery) | v1.0_2022<br>0519 | JAVA 插件化漏洞扫描器，Gui基于javafx。POC 目前集成 Weblogic、Tom<br>cat、Shiro、Spring等。 |
### 安卓漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [appshark](https://github.com/bytedance/appshark) | v0.1.2 | Appshark is a static taint analysis platform to scan vulnerabili<br>ties in an Android app. |
### 代码审计
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [murphysec](https://github.com/murphysecurity/murphysec) | v3.0.1 | An open source tool focused on software supply chain security. <br>墨菲安全专注于软件供应链安全，具备专业的软件成分分析（SCA）、漏洞<br>检测、专业漏洞库。 |
| [Kunlun-M](https://github.com/LoRexxar/Kunlun-M) | v2.6.5 | KunLun-M是一个完全开源的静态白盒扫描工具，支持PHP、JavaScript的<br>语义扫描，基础安全、组件安全扫描，Chrome Ext\Solidity的基础扫描。 |
| [CodeQLpy](https://github.com/webraybtl/CodeQLpy) |  | CodeQLpy是一款基于CodeQL实现的半自动化代码审计工具，目前仅支持ja<br>va语言。实现从源码反编译，数据库生成，脆弱性发现的全过程，可以辅<br>助代码审计人员快速定位源码可能存在的漏洞。 |
### 容器漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [veinmind-tools](https://github.com/chaitin/veinmind-tools) | v2.1.2 | veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器安<br>全工具集 |
### 口令爆破
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [goon](https://github.com/i11us0ry/goon) | v3.5 | goon,集合了fscan和kscan等优秀工具功能的扫描爆破工具。功能包含：i<br>p探活、port扫描、web指纹扫描、title扫描、压缩文件扫描、fofa获取、<br>ms17010、mssql、mysql、postgres、redis、ssh、smb、rdp、telnet、to<br>mcat等爆破以及如netbios探测等功能。 |
| [SNETCracker](https://github.com/shack2/SNETCracker) | 1.0.20190<br>715 | 超级弱口令检查工具是一款Windows平台的弱口令审计工具，支持批量多<br>线程检查，可快速发现弱密码、弱口令账号，密码支持和用户名结合进行检<br>查，大大提高成功率，支持自定义服务端口和字典。 |
| [web-brutator](https://github.com/koutto/web-brutator) |  | Fast Modular Web Interfaces Bruteforcer |
| [WebCrack](https://github.com/yzddmr6/WebCrack) |  | WebCrack是一款web后台弱口令/万能密码批量检测工具，在工具中导入后<br>台地址即可进行自动化检测。 |
| [ssb](https://github.com/pwnesia/ssb) | v0.1.1 | Secure Shell Bruteforcer — A faster & simpler way to bruteforce<br> SSH server |
| [thc-hydra-windows](https://github.com/maaaaz/thc-hydra-windows) | v9.1 | The great THC-HYDRA tool compiled for Windows |
### 漏洞发现
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Dude](https://github.com/x364e3ab6/Dude) | v1.0.0.3 | Dude (大佬) WEB渗透测试辅助工具 |
### 信息泄露监控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [code6](https://github.com/4x99/code6) | 1.6.4 | 码小六 - GitHub 代码泄露监控系统 |
| [gshark](https://github.com/madneal/gshark) | v1.1.4 | Scan for sensitive information easily and effectively. |
## 漏洞利用
### 云原生安全工具合集
#### 云原生攻防靶场
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [metarget](https://github.com/Metarget/metarget) | v0.9.1 | Metarget is a framework providing automatic constructions of vul<br>nerable infrastructures. |
#### 容器漏洞利用工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CDK](https://github.com/cdk-team/CDK) | v1.5.2 | 📦Make security testing of K8s, Docker, and Containerd easier. |
#### 容器逃逸检测工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [container-escape-ch<br>eck](https://github.com/teamssix/container-escape-check) | v0.3 | docker container escape check || Docker 容器逃逸检测 |
#### 容器安全检测工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [veinmind-tools](https://github.com/chaitin/veinmind-tools) | v2.1.2 | veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器安<br>全工具集 |
#### 容器漏洞分析工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [clair](https://github.com/quay/clair) | v4.6.1 | Vulnerability Static Analysis for Containers |
#### 容器安全扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [trivy](https://github.com/aquasecurity/trivy) | v0.40.0 | Find vulnerabilities, misconfigurations, secrets, SBOM in contai<br>ners, Kubernetes, code repositories, clouds and more |
#### 容器镜像扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [grype](https://github.com/anchore/grype) | v0.61.1 | A vulnerability scanner for container images and filesystems |
| [syft](https://github.com/anchore/syft) | v0.79.0 | CLI tool and library for generating a Software Bill of Materials<br> from container images and filesystems |
#### K8S漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-hunter](https://github.com/aquasecurity/kube-hunter) | v0.6.8 | Hunt for security weaknesses in Kubernetes clusters |
#### K8S基线核查
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | v0.6.13 | Checks whether Kubernetes is deployed according to security best<br> practices as defined in the CIS Kubernetes Benchmark |
#### 云原生安全平台
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [neuvector](https://github.com/neuvector/neuvector) | v5.1.2 |  |
### 半自动化漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [railgun](https://github.com/lz520520/railgun) | v1.5.4 |  |
| [Goby](https://github.com/gobysec/Goby) | Beta2.2.0 | Attack surface mapping |
### 数据库利用
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
| [RequestTemplate](https://github.com/1n7erface/RequestTemplate) | v1.1.5 | 双语双端内网扫描以及验证工具 |
| [redis-rogue-server](https://github.com/Dliv3/redis-rogue-server) |  | Redis 4.x/5.x RCE |
| [Databasetools](https://github.com/Hel10-Web/Databasetools) | 1.2 | 一款用Go语言编写的数据库自动化提权工具，支持Mysql、MSSQL、Postgr<br>esql、Oracle、Redis数据库提权、命令执行、爆破以及ssh连接 |
### 中间件&框架漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [AttackTomcat](https://github.com/tpt11fb/AttackTomcat) | V1 | Tomcat常见漏洞GUI利用工具。CVE-2017-12615 PUT文件上传漏洞、tomca<br>t-pass-getshell 弱认证部署war包、弱口令爆破、CVE-2020-1938 Tomcat<br> AJP文件读取/包含 |
| [SpringExploit](https://github.com/SummerSec/SpringExploit) | 0.1.9 | 🚀 一款为了学习go而诞生的漏洞利用工具 |
| [shiro_rce_tool](https://github.com/wyzxxz/shiro_rce_tool) |  | shiro 反序列 命令执行辅助检测工具 |
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2) | 4.5.6 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原<br>版中NoCC的问题 https://github.com/j1anFen/shiro_attack |
| [shiro_attack](https://github.com/j1anFen/shiro_attack) | 2.2 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马） |
| [FastjsonExploit](https://github.com/c0ny1/FastjsonExploit) |  | Fastjson vulnerability quickly exploits the framework（fastjson<br>漏洞快速利用框架） |
| [fastjson_rec_exploi<br>t](https://github.com/mrknow001/fastjson_rec_exploit) |  | fastjson一键命令执行 |
| [jexboss](https://github.com/joaomatosf/jexboss) |  | JexBoss: Jboss (and Java Deserialization Vulnerabilities) verify<br> and EXploitation Tool |
| [weblogic-framework](https://github.com/dream0x01/weblogic-framework) | v0.2.3 | weblogic-framework is the best tool for detecting weblogic vulne<br>rabilities. |
| [WeblogicTool](https://github.com/KimJun1010/WeblogicTool) | v1.0 | WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马注<br>入、密码解密等（深信服深蓝实验室天威战队强力驱动） |
| [dubbo-exp](https://github.com/threedr3am/dubbo-exp) |  | dubbo学习demo，之前删了，重新上传。 |
| [STS2G](https://github.com/xfiftyone/STS2G) | 1.0 | Struts2漏洞扫描利用工具 - Golang版. Struts2 Scanner Written in G<br>olang |
| [Struts2-Scan](https://github.com/HatBoy/Struts2-Scan) |  | Struts2全漏洞扫描利用工具 |
| [log4j-shell-poc](https://github.com/kozmer/log4j-shell-poc) |  | A Proof-Of-Concept for the CVE-2021-44228 vulnerability.  |
| [SpringBootExploit](https://github.com/0x727/SpringBootExploit) | 1.3 | 项目是根据LandGrey/SpringBootVulExploit清单编写，目的hvv期间快速<br>利用漏洞、降低漏洞利用门槛。 |
| [SpringBoot-Scan-GUI](https://github.com/13exp/SpringBoot-Scan-GUI) | v1.2.2 |  |
| [CVE-2023-21839](https://github.com/4ra1n/CVE-2023-21839) |  | Weblogic CVE-2023-21839 / CVE-2023-21931 / CVE-2023-21979 一键检<br>测 |
| [Tomcat_PUT_GUI_EXP](https://github.com/xiaokp7/Tomcat_PUT_GUI_EXP) | 1.4 | Tomcat PUT方法任意文件写入（CVE-2017-12615）exp |
### 漏洞利用辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jndi_tool](https://github.com/wyzxxz/jndi_tool) |  | JNDI服务利用工具 RMI/LDAP，支持部分场景回显、内存shell，高版本JD<br>K场景下利用等，fastjson rce命令执行，log4j rce命令执行 漏洞检测辅<br>助工具 |
| [ysoserial](https://github.com/frohoff/ysoserial) | v0.0.6 | A proof-of-concept tool for generating payloads that exploit uns<br>afe Java object deserialization. |
| [Gopherus](https://github.com/tarunkant/Gopherus) |  | This tool generates gopher link for exploiting SSRF and gaining <br>RCE in various servers |
| [revsuit](https://github.com/Li4n0/revsuit) | v0.6.0 | RevSuit is a flexible and powerful reverse connection platform d<br>esigned for receiving connection from target host in penetration.<br>  |
| [DNSlog-GO](https://github.com/lanyi1998/DNSlog-GO) | 1.5.2 | DNSLog-GO 是一款golang编写的监控 DNS 解析记录的工具，自带WEB界面 |
| [godnslog](https://github.com/chennqqi/godnslog) | v0.7.0 | An exquisite dns&http log server for verify SSRF/XXE/RFI/RCE vul<br>nerability  |
| [ysomap](https://github.com/wh1t3p1g/ysomap) | v0.1.3 | A helpful Java Deserialization exploit framework. |
| [Antenna](https://github.com/wuba/Antenna) | v1.3.5 | Antenna是58同城安全团队打造的一款辅助安全从业人员验证网络中多种<br>漏洞是否存在以及可利用性的工具。其基于带外应用安全测试(OAST)通过任<br>务的形式，将不同漏洞场景检测能力通过插件的形式进行集合，通过与目标<br>进行out-bind的数据通信方式进行辅助检测。 |
| [cola_dnslog](https://github.com/AbelChe/cola_dnslog) | v1.3.2 | Cola Dnslog v1.3.2 更加强大的dnslog平台/无回显漏洞探测辅助平台 <br>完全开源 dnslog httplog ldaplog rmilog 支持dns http ldap rmi等协议<br> 提供API调用方式便于与其他工具结合 支持钉钉机器人、Bark等提醒 支<br>持docker一键部署 后端完全使用python实现 前端基于vue-element-admin<br>二开 |
| [ddddocr](https://github.com/sml2h3/ddddocr) |  | 带带弟弟 通用验证码识别OCR pypi版 |
| [ysoserial](https://github.com/su18/ysoserial) |  |  |
| [JNDIExploit](https://github.com/WhiteHSBG/JNDIExploit) | v1.4 | 对原版https://github.com/feihong-cs/JNDIExploit 进行了实用化修改 |
| [JNDIExploit-1](https://github.com/Mr-xn/JNDIExploit-1) | v1.2 | 一款用于 JNDI注入 利用的工具，大量参考/引用了 Rogue JNDI 项目的<br>代码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的方式<br>，适用于与自动化工具配合使用。（from https://github.com/feihong-cs<br>/JNDIExploit） |
| [JNDIExploit](https://github.com/0x727/JNDIExploit) | 1.1 | 一款用于JNDI注入利用的工具，大量参考/引用了Rogue JNDI项目的代码<br>，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的方式，适<br>用于与自动化工具配合使用。 |
| [Exp-Tools](https://github.com/cseroad/Exp-Tools) | v1.1.5 | 一款集成各种exp的实用性工具 |
### 重点CMS利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL) | OA-EXPTOO<br>L-0.72 | OA综合利用工具，集合将近20款OA漏洞批量扫描 |
| [seeyon_exp](https://github.com/Summer177/seeyon_exp) |  | 致远OA综合利用工具 |
| [SeeyonExploit-GUI](https://github.com/God-Ok/SeeyonExploit-GUI) |  | 致远OA综合利用工具V1.0 |
| [TDOA_RCE](https://github.com/xinyu2428/TDOA_RCE) | v1.0 | 通达OA综合利用工具 |
| [LandrayExploit](https://github.com/yuanhaiGreg/LandrayExploit) | 1.1 | 蓝凌OA漏洞利用工具/前台无条件RCE/文件写入 |
| [weaver_exp](https://github.com/z1un/weaver_exp) |  | 泛微OA漏洞综合利用脚本 |
| [EgGateWayGetShell](https://github.com/Tas9er/EgGateWayGetShell) |  | Code By:Tas9er |
| [CMSmap](https://github.com/Dionach/CMSmap) |  | CMSmap is a python open source CMS scanner that automates the pr<br>ocess of detecting security flaws of the most popular CMSs.  |
| [wprecon](https://github.com/blackbinn/wprecon) |  |  |
| [wordpress-exploit-f<br>ramework](https://github.com/rastating/wordpress-exploit-framework) | v2.0.1 | A Ruby framework designed to aid in the penetration testing of W<br>ordPress systems.  |
| [wpscan](https://github.com/wpscanteam/wpscan) | v3.8.22 | WPScan WordPress security scanner. Written for security professi<br>onals and blog maintainers to test the security of their WordPres<br>s websites. Contact us via contact@wpscan.com |
| [wprecon](https://github.com/AngraTeam/wprecon) |  |  |
| [Aazhen-RexHa](https://github.com/zangcc/Aazhen-RexHa) |  | 自研JavaFX图形化漏洞扫描工具，支持扫描的漏洞分别是： ThinkPHP-2.<br>x-RCE， ThinkPHP-5.0.23-RCE， ThinkPHP5.0.x-5.0.23通杀RCE， Think<br>PHP5-SQL注入&敏感信息泄露， ThinkPHP 3.x 日志泄露NO.1， ThinkPHP <br>3.x 日志泄露NO.2， ThinkPHP 5.x 数据库信息泄露的漏洞检测，以及批<br>量检测的功能。漏洞POC基本适用ThinkPHP全版本漏洞。 |
| [ThinkphpGUI](https://github.com/Lotus6/ThinkphpGUI) | 1.3 | Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，getsh<br>ell。 |
| [thinkphp_gui_tools](https://github.com/bewhale/thinkphp_gui_tools) | v2.4.2 | ThinkPHP漏洞综合利用工具, 图形化界面, 命令执行, 一键getshell, 批<br>量检测, 日志遍历, session包含,宝塔绕过 |
| [Apt_t00ls](https://github.com/White-hua/Apt_t00ls) | v0.6 | 高危漏洞利用工具 |
| [yonyou_exp_plus](https://github.com/li8u99/yonyou_exp_plus) |  | 用友系列全漏洞检测工具 |
### 信息泄露利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Cloud-Bucket-Leak-D<br>etection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | v0.4.0 | 六大云存储，泄露利用检测工具 |
| [aksk_tool](https://github.com/wyzxxz/aksk_tool) |  | AK资源管理工具，阿里云/腾讯云/华为云/AWS/UCLOUD/京东云/百度云/七<br>牛云存储AccessKey AccessKeySecret，利用AK获取资源信息和操作资源，E<br>CS/CVM/E2/UHOST/ECI/BCC执行命令，OSS/COS/S3/BOS管理，RDS/DB管理，<br>域名管理，添加RAM/CAM/IAM账号等 |
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
| [JDumpSpider](https://github.com/whwlsfb/JDumpSpider) | V1.1 | HeapDump敏感信息提取工具 |
### 漏洞检测利用仓库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [poc-hub](https://github.com/ybdt/poc-hub) |  | 漏洞复现 |
| [Awesome-Exploit](https://github.com/Threekiii/Awesome-Exploit) |  | 一个漏洞利用工具仓库 |
| [exphub](https://github.com/zhzyker/exphub) |  | Exphub[漏洞利用脚本库] 包括Webloigc、Struts2、Tomcat、Nexus、Sol<br>r、Jboss、Drupal的漏洞利用脚本，最新添加CVE-2020-14882、CVE-2020-<br>11444、CVE-2020-10204、CVE-2020-10199、CVE-2020-1938、CVE-2020-25<br>51、CVE-2020-2555、CVE-2020-2883、CVE-2019-17558、CVE-2019-6340 |
| [CVE-Master](https://github.com/wjl110/CVE-Master) | v1.0.1 | 收集本人自接触渗透测试用于漏洞验证的所有热门CVE、POC、CNVD攻击有<br>效载荷+测试工具+FUZZ,一个仓库满足许多攻击测试场景,开箱即用. |
| [0day](https://github.com/helloexp/0day) |  | 各种CMS、各种平台、各种系统、各种软件漏洞的EXP、POC ,该项目将持<br>续更新 |
| [PocList](https://github.com/1n7erface/PocList) |  | Alibaba-Nacos-Unauthorized/ApacheDruid-RCE_CVE-2021-25646/MS-Exc<br>hange-SSRF-CVE-2021-26885/Oracle-WebLogic-CVE-2021-2109_RCE/RG-CN<br>VD-2021-14536/RJ-SSL-VPN-UltraVires/Redis-Unauthorized-RCE/TDOA-V<br>11.7-GetOnlineCookie/VMware-vCenter-GetAnyFile/yongyou-GRP-U8-XXE<br>/Oracle-WebLogic-CVE-2020-14883/Oracle-WebLogic-CVE-2020-14882/Ap<br>ache-Solr-GetAnyFile/F5-BIG-IP-CVE-2021-22986/Sonicwall-SSL-VPN-R<br>CE/GitLab-Graphql-CNVD-2021-14193/D-Link-DCS-CVE-2020-25078/WLAN-<br>AP-WEA453e-RCE/360TianQing-Unauthorized/360TianQing-SQLinjection/<br>FanWeiOA-V8-SQLinjection/QiZhiBaoLeiJi-AnyUserLogin/QiAnXin-WangK<br>angFirewall-RCE/金山-V8-终端安全系统/NCCloud-SQLinjection/ShowDoc<br>-RCE |
| [vulnerability](https://github.com/lal0ne/vulnerability) |  | 收集、整理、修改互联网上公开的漏洞POC |
| [Some-PoC-oR-ExP](https://github.com/coffeehb/Some-PoC-oR-ExP) |  | 各种漏洞poc、Exp的收集或编写 |
| [POChouse](https://github.com/DawnFlame/POChouse) |  | POC&EXP仓库、hvv弹药库、Nday、1day |
| [PocOrExp_in_Github](https://github.com/ycdxsb/PocOrExp_in_Github) |  | 聚合Github上已有的Poc或者Exp，CVE信息来自CVE官网。Auto Collect P<br>oc Or Exp from Github by CVE ID. |
### 信息泄露漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [cf](https://github.com/teamssix/cf) | v0.4.4 | Cloud Exploitation Framework 云环境利用框架，方便安全人员在获得 <br>AK 的后续工作 |
| [Cloud-Bucket-Leak-D<br>etection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | v0.4.0 | 六大云存储，泄露利用检测工具 |
| [AliyunAccessKeyTool<br>s](https://github.com/NS-Sp4ce/AliyunAccessKeyTools) | 1.0 | 阿里云AccessKey泄漏利用工具 |
### 漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [slowhttptest](https://github.com/shekyan/slowhttptest) | v1.9.0 | Application Layer DoS attack simulator |
### WEB漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SSTImap](https://github.com/vladko312/SSTImap) | v1.1 | Automatic SSTI detection tool with interactive interface |
| [tplmap](https://github.com/epinna/tplmap) | v0.5 | Server-Side Template Injection and Code Injection Detection and <br>Exploitation Tool |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | 1.7 | Automatic SQL injection and database takeover tool |
### 服务漏洞利用
#### RMI
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [attackRmi](https://github.com/waderwu/attackRmi) | v0.1 | attackRmi |
| [attackRmi](https://github.com/A-D-Team/attackRmi) | v2.0 |  |
| [BaRMIe](https://github.com/NickstaDB/BaRMIe) | v1.01 | Java RMI enumeration and attack tool. |
| [rmiscout](https://github.com/BishopFox/rmiscout) | v1.4 | RMIScout uses wordlist and bruteforce strategies to enumerate Ja<br>va RMI functions and exploit RMI parameter unmarshalling vulnerab<br>ilities |
#### JDWP
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jdwp-shellifier](https://github.com/IOActive/jdwp-shellifier) |  |  |
## 漏洞文库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [bylibrary](https://github.com/BaizeSec/bylibrary) |  | 白阁文库是白泽Sec安全团队维护的一个漏洞POC和EXP公开项目 |
| [PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book) | PeiQi-WIK<br>I-Book-202<br>2-03-20 | 面向网络安全从业者的知识文库🍃 |
| [VulWiki](https://github.com/Ares-X/VulWiki) |  | VulWiki |
| [vulbase](https://github.com/cckuailong/vulbase) |  | 各大漏洞文库合集 |
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC) |  | 一个各类漏洞POC知识库 |
| [Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki) | v1.0 | 一个基于docsify的综合漏洞知识库，目前漏洞数量800+ |
| [yougar0.github.io](https://github.com/heise5yuetian/yougar0.github.io) |  | 漏洞知识库 |
| [Vulhub-Reproduce](https://github.com/Threekiii/Vulhub-Reproduce) |  | 一个Vulhub漏洞复现知识库 |
| [Report_Public](https://github.com/DVPNET/Report_Public) |  |  DVPNET 公开漏洞知识库 |
| [BUG-Pocket](https://github.com/light-Life/BUG-Pocket) |  | 小型漏洞库，提供FOFA语法及批量脚本，具体利用法请参考别的漏洞库，<br>共4种类型47项 |
| [WiKi](https://github.com/ScarecrowSec/WiKi) |  | 稻草人安全团队漏洞库 |
| [PoC-ExP](https://github.com/Cuerz/PoC-ExP) |  | 【漏洞Poc知识库】一个网络安全爱好者对网络上一些已知漏洞payload的<br>收录，持续更新。并编写了利用脚本，可用于日常学习或批量的src漏洞挖<br>掘 |
## 权限维持
### Shell管理
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Behinder](https://github.com/rebeyond/Behinder) | Behinder_<br>v4.0.6 | “冰蝎”动态二进制加密网站管理客户端 |
| [Godzilla](https://github.com/BeichenDream/Godzilla) | v4.0.1-go<br>dzilla | 哥斯拉 |
| [antSword](https://github.com/AntSwordProject/antSword) | 2.1.15 | 中国蚁剑是一款跨平台的开源网站管理工具。AntSword is a cross-plat<br>form website management toolkit. |
| [Platypus](https://github.com/WangYihang/Platypus) | v1.5.0 | :hammer: A modern multiple reverse shell sessions manager writte<br>n in go |
| [As-Exploits](https://github.com/yzddmr6/As-Exploits) |  | 中国蚁剑后渗透框架 |
### 后门
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CreateHiddenAccount](https://github.com/wgpsec/CreateHiddenAccount) | 0.2 | A tool for creating hidden accounts using the registry || 一个使<br>用注册表创建隐藏帐户的工具 |
### 远控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [noterce](https://github.com/xiao-zhu-zhu/noterce) | v1.2 | 一种另辟蹊径的免杀执行系统命令的木马 |
### 免杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shellcodeloader](https://github.com/knownsec/shellcodeloader) | v1.1 | shellcodeloader |
| [AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool) | 20230417 | 掩日 - 免杀执行器生成工具 |
## 权限提升
### windows提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BadPotato](https://github.com/BeichenDream/BadPotato) |  | Windows 权限提升 BadPotato |
### linux提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dirtycow](https://github.com/firefart/dirtycow) |  | Dirty Cow exploit - CVE-2016-5195 |
| [traitor](https://github.com/liamg/traitor) | v0.0.14 | :arrow_up: :skull_and_crossbones: :fire: Automatic Linux privesc<br> via exploitation of low-hanging fruit e.g. gtfobins, pwnkit, dir<br>ty pipe, +w docker.sock |
| [LinEnum](https://github.com/rebootuser/LinEnum) |  | Scripted Local Linux Enumeration & Privilege Escalation Checks |
| [PEASS-ng](https://github.com/carlospolop/PEASS-ng) | 20230425-<br>bd7331ea | PEASS - Privilege Escalation Awesome Scripts SUITE (with colors) |
| [traitor](https://github.com/liamg/traitor) | v0.0.14 | :arrow_up: :skull_and_crossbones: :fire: Automatic Linux privesc<br> via exploitation of low-hanging fruit e.g. gtfobins, pwnkit, dir<br>ty pipe, +w docker.sock |
### 容器提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [container-escape-ch<br>eck](https://github.com/teamssix/container-escape-check) | v0.3 | docker container escape check || Docker 容器逃逸检测 |
| [CDK](https://github.com/cdk-team/CDK) | v1.5.2 | 📦Make security testing of K8s, Docker, and Containerd easier. |
## 内网渗透
### 免杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shellcodeloader](https://github.com/knownsec/shellcodeloader) | v1.1 | shellcodeloader |
| [AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool) | 20230417 | 掩日 - 免杀执行器生成工具 |
### 代理转发
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [reGeorg](https://github.com/sensepost/reGeorg) |  | The successor to reDuh, pwn a bastion webserver and create SOCKS<br> proxies through the DMZ. Pivot and pwn. |
| [Stowaway](https://github.com/ph4ntonn/Stowaway) | v2.1 | 👻Stowaway -- Multi-hop Proxy Tool for pentesters |
| [PortForward](https://github.com/knownsec/PortForward) | 0.5.0 | The port forwarding tool developed by Golang solves the problem <br>that the internal and external networks cannot communicate in cer<br>tain scenarios |
### 密码提取
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [getIntrInfo](https://github.com/Potato-py/getIntrInfo) |  | 收集内部网信息。包括：浏览器书签、密码和浏览历史记录、cookie。Wi<br>fi信息和密码。主机信息。 |
| [FinalShell-Decoder](https://github.com/passer-W/FinalShell-Decoder) | V1.0 | FinallShell 密码解密GUI工具 |
| [Xdecrypt](https://github.com/dzxs/Xdecrypt) |  | Xshell Xftp password decrypt |
| [HackBrowserData](https://github.com/moonD4rk/HackBrowserData) | v0.4.4 | Decrypt passwords/cookies/history/bookmarks from the browser. 一<br>款可全平台运行的浏览器数据导出解密工具。 |
| [SharpDecryptPwd](https://github.com/ianxtianxt/SharpDecryptPwd) |  | Windows常用程序密码读取工具：SharpDecryptPwd |
### 漏洞发现
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InScan](https://github.com/inbug-team/InScan) |  | 边界打点后的自动化渗透工具 |
| [kscan](https://github.com/lcvvvv/kscan) | v1.85 | Kscan是一款纯go开发的全方位扫描器，具备端口扫描、协议检测、指纹<br>识别，暴力破解等功能。支持协议1200+，协议指纹10000+，应用指纹20000<br>+，暴力破解协议10余种。 |
| [fscan](https://github.com/shadow1ng/fscan) | 1.8.2 | 一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。 |
| [Gscan](https://github.com/hack2fun/Gscan) | v1.0 | Gscan is a high concurrency scanner based on golang |
| [ServerScan](https://github.com/Adminisme/ServerScan) | v1.0.2 | ServerScan一款使用Golang开发的高并发网络扫描、服务探测工具。 |
### 漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Viper](https://github.com/FunnyWolf/Viper) | v1.5.26 | Redteam operationplatform with webui 图形化红队行动辅助平台 |
### 横向工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WMIHACKER](https://github.com/rootclay/WMIHACKER) |  | A Bypass Anti-virus Software Lateral Movement Command Execution <br>Tool |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Ladon](https://github.com/k8gege/Ladon) | v10.10.4 | Ladon大型内网渗透工具，可PowerShell模块化、可CS插件化、可内存加<br>载，无文件扫描。含端口扫描、服务识别、网络资产探测、密码审计、高危<br>漏洞检测、漏洞利用、密码读取以及一键GetShell，支持批量A段/B段/C段<br>以及跨网段扫描，支持URL、主机、域名列表扫描等。10.10版本内置212个<br>功能模块,外部模块18个,网络资产探测模块28个通过多种协议(ICMP\NBT\DN<br>S\MAC\SMB\WMI\SSH\HTTP\HTTPS\Exchange\mssql\FTP\RDP)以及方法快速<br>获取目标网络存活主机IP、计算机名、工作组、共享资源、网卡地址、操作<br>系统版本、网站、子域名、中间件、开放服务、路由器、交换机、数据库、<br>打印机等信息，高危漏洞检测16个包含Cisco、Zimbra、Ex |
## 相关资源
### 工具集成环境
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先<br>利其器。 |
| [CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools) |  | 渊龙Sec安全团队CTF&AWD工具箱 |
| [PenKitGui](https://github.com/ccc-f/PenKitGui) |  | 渗透测试武器库 |
| [Taie-RedTeam-OS](https://github.com/taielab/Taie-RedTeam-OS) |  | 泰阿安全实验室-基于XUbuntu私人订制的红蓝对抗渗透操作系统 |
| [FreeGui](https://github.com/tyB-or/FreeGui) | v2.5 | freeGui：基于ttkbootstrap开发的一款用来管理自己的渗透测试工具的<br>一个小工具，并提供一些实用小功能，例如打开目录，运行工具，工具备忘<br>命令。 |
| [GUI_Tools](https://github.com/ghealer/GUI_Tools) | V1.1 | 一个由各种图形化渗透工具组成的工具集 |
| [Pentest-Windows](https://github.com/arch3rPro/Pentest-Windows) | v1.0 | Windows11 Penetration Suite Toolkit |
### 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先<br>利其器。 |
| [Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam) |  | 一个红队知识仓库 |
| [Threathunting-book](https://github.com/12306Bro/Threathunting-book) |  |  |
| [PenetrationTesttips](https://github.com/CYJoe-Cyclone/PenetrationTesttips) |  | 渗透测试Tips - Version1.3 |
| [Intranet_Penetratio<br>n_Tips](https://github.com/Ridter/Intranet_Penetration_Tips) |  | 2018年初整理的一些内网渗透TIPS，后面更新的慢，所以整理出来希望跟<br>小伙伴们一起更新维护~ |
| [Vuln-List](https://github.com/wwl012345/Vuln-List) |  | (持续更新)对网上出现的各种OA、中间件、CMS等漏洞进行整理，主要包<br>括漏洞介绍、漏洞影响版本以及漏洞POC/EXP等，并且会持续更新。 |
### 优秀项目集合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [404StarLink](https://github.com/knownsec/404StarLink) |  | 404StarLink - 推荐优质、有意义、有趣、坚持维护的安全开源项目 |
| [Scanners-Box](https://github.com/We5ter/Scanners-Box) |  | A powerful and open-source toolkit for hackers and security auto<br>mation - 安全行业从业者自研开源扫描器合辑 |
| [All-Defense-Tool](https://github.com/guchangan1/All-Defense-Tool) |  | 本项目集成了全网优秀的攻防武器工具项目，包含自动化利用，子域名、<br>目录扫描、端口扫描等信息收集工具，各大中间件、cms漏洞利用工具，爆<br>破工具、内网横向及免杀、社工钓鱼以及应急响应等资料。 |
| [About-Attack](https://github.com/lintstar/About-Attack) |  | 一个旨在通过应用场景 / 标签对 Github 红队向工具 / 资源进行分类收<br>集，降低红队技术门槛的手册【持续更新】 |
| [RedTeamTools](https://github.com/FiveAourThe/RedTeamTools) |  | 分享红队常用的工具 |
### 代理池
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [go_proxy_pool](https://github.com/pingc0y/go_proxy_pool) | 2022.11.2<br>2 | 无环境依赖开箱即用的代理IP池 |
| [rotateproxy](https://github.com/akkuman/rotateproxy) | v0.7.2 | 利用fofa搜索socks5开放代理进行代理池轮切的工具 |
| [Gofreeproxy](https://github.com/ja9er/Gofreeproxy) | v0.1 | 自用的动态代理小工具 |
### 工具集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [K8tools](https://github.com/k8gege/K8tools) |  | K8工具合集(内网渗透/提权工具/远程溢出/漏洞利用/扫描工具/密码破解<br>/免杀工具/Exploit/APT/0day/Shellcode/Payload/priviledge/BypassUAC<br>/OverFlow/WebShell/PenTest) Web GetShell Exploit(Struts2/Zimbra/W<br>eblogic/Tomcat/Apache/Jboss/DotNetNuke/zabbix) |
## 工具周边
### Burpsuite
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [PowerScanner](https://github.com/NeoTheCapt/PowerScanner) | 1.1.3 | 面向HW的红队半自动扫描器 |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | RouteVulS<br>can1.4 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的bu<br>rp插件 |
| [SpringScan](https://github.com/metaStor/SpringScan) | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [BurpSuite-collectio<br>ns](https://github.com/Mr-xn/BurpSuite-collections) |  | 有关burpsuite的插件(非商店),文章以及使用技巧的收集(此项目不再提<br>供burpsuite破解文件,如需要请在博客mrxn.net下载)---Collection of bu<br>rpsuite plugins (non-stores), articles and tips for using Burpsui<br>te, no crack version file |
| [BurpShiroPassiveSca<br>n](https://github.com/pmiaowu/BurpShiroPassiveScan) | BurpShiro<br>PassiveSca<br>n-2.0.0 | 一款基于BurpSuite的被动式shiro检测插件 |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | BurpFastJ<br>sonScan-2.<br>2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [HaE](https://github.com/gh0stkey/HaE) | 2.4.6 | HaE - Highlighter and Extractor, 赋能白帽 高效作战 |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9 | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集；<br>快速Title获取；外部工具联动；等等 |
| [Sylas](https://github.com/Acmesec/Sylas) | 1.1.1 | 新一代子域名主/被动收集工具 - Subdomain automatic/passive collec<br>tion tool |
| [GadgetProbe](https://github.com/BishopFox/GadgetProbe) | v1.0 | Probe endpoints consuming Java serialized objects to identify cl<br>asses, libraries, and library versions on remote Java classpaths. |
| [HopLa](https://github.com/synacktiv/HopLa) | 1.2 |  HopLa Burp Suite Extender plugin -Adds autocompletion support a<br>nd useful payloads in Burp Suite |
| [captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified) | 0.23-beta<br>5 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免费<br>ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, sup<br>port AES/RSA/DES/ExecJs(execute JS encryption code in burpsuite).<br> 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSuite插<br>件 |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.25 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等）<br>，类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础上，<br>不影响APP、网站加解密正常逻辑等。 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [AutoRepeater](https://github.com/nccgroup/AutoRepeater) |  | Automated HTTP Request Repeating With Burp Suite |
| [http-request-smuggl<br>er](https://github.com/portswigger/http-request-smuggler) |  |  |
| [burp-requests](https://github.com/silentsignal/burp-requests) | v0.2.4 | Copy as requests plugin for Burp Suite |
| [CORSScanner](https://github.com/zzzskd/CORSScanner) |  | CORS 跨域漏洞 burp 插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) |  |  |
| [HostHeaderAttack](https://github.com/weujieytt/HostHeaderAttack) | 0.1 | 检测host头攻击的Burpsuite被动扫描插件，Burpsuite passive scannin<br>g plugin responsible for detecting host header attack |
| [knife](https://github.com/bit4woo/knife) | v2.2 | A burp extension that add some useful function toContext Menu 添<br>加一些右键菜单让burp用起来更顺畅 |
| [log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner) | 0.25.0 | CVE-2021-44228 Log4j2 BurpSuite Scanner,Customize ceye.io api or<br> other apis,including internal networks |
| [passive-scan-client](https://github.com/c0ny1/passive-scan-client) | 0.3.1 | Burp被动扫描流量转发插件 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpSuiteCn](https://github.com/funkyoummp/BurpSuiteCn) | V2.0 | Burp Suite汉化 中文 |
| [NEW_xp_CAPTCHA](https://github.com/smxiazi/NEW_xp_CAPTCHA) | 4.2 | xp_CAPTCHA(瞎跑 白嫖版) burp 验证码 识别 burp插件 |
| [npscrack](https://github.com/weishen250/npscrack) | npscrack-<br>1.0 | 蓝队利器、溯源反制、NPS 漏洞利用、NPS exp、NPS poc、Burp插件、一<br>键利用 |
| [OneScan](https://github.com/vaycore/OneScan) | v1.0.0 | OneScan是递归目录扫描的BurpSuite插件 |
| [OutLook](https://github.com/KrystianLi/OutLook) |  |  |
| [passive-scan-client<br>-plus](https://github.com/winezer0/passive-scan-client-plus) | v0.4.12.0 | burpsuite passive-scan-client 插件维护分支 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpCRLFScan](https://github.com/A0WaQ4/BurpCRLFScan) | 1.4 | 使用java编写的CRLF-Injection-burp被动扫描插件 |
| [JsonDetect](https://github.com/a1phaboy/JsonDetect) | v1.0 | A burp Extender to detect json, include fastjson,jackson,gson |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.25 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等）<br>，类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础上，<br>不影响APP、网站加解密正常逻辑等。 |
| [burp-text4shell](https://github.com/silentsignal/burp-text4shell) | v0.1 | Text4Shell scanner for Burp Suite |
| [sweetPotato](https://github.com/z2p/sweetPotato) | version1.<br>4 | 基于burpsuite的资产分析工具 |
| [xia_Liao](https://github.com/smxiazi/xia_Liao) | 1.6 | xia Liao（瞎料）burp插件 用于Windows在线进程/杀软识别 与 web渗透<br>注册时，快速生成需要的资料用来填写，资料包含：姓名、手机号、身份证<br>、统一社会信用代码、组织机构代码、银行卡，以及各类web语言的hello w<br>orld输出和生成弱口令字典等。 |
| [base64encode](https://github.com/handbye/base64encode) | 1.0 | burpsuite POST数据包base64编码插件 |
| [HackTools](https://github.com/Vicl1fe/HackTools) | 1.4 | 提高渗透测试效率。#Burp插件##渗透测试##小工具# |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | RouteVulS<br>can1.4 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的bu<br>rp插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) |  |  |
| [burp-awesome-tls](https://github.com/sleeyax/burp-awesome-tls) | v0.0.4 | Fix Burp Suite's horrible TLS stack & spoof any browser fingerpr<br>int |
| [JustC2file](https://github.com/Peithon/JustC2file) | v1.0.2 | Burp插件，Malleable C2 Profiles生成器；可以通过Burp代理选中请求<br>，生成Cobalt Strike的profile文件(CSprofile) |
| [SpringScan](https://github.com/metaStor/SpringScan) | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified) | 0.23-beta<br>5 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免费<br>ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | BurpFastJ<br>sonScan-2.<br>2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [Log4j-check](https://github.com/bigsizeme/Log4j-check) |  | log4J burp被扫插件、CVE-2021-44228、支持dnclog.cn和burp内置DNS、<br>可配合JNDIExploit生成payload |
| [Log4j2Scan](https://github.com/whwlsfb/Log4j2Scan) | V0.13.1 | Log4j2 RCE Passive Scanner plugin for BurpSuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, sup<br>port AES/RSA/DES/ExecJs(execute JS encryption code in burpsuite).<br> 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSuite插<br>件 |
| [BurpBountyPlus](https://github.com/ggg4566/BurpBountyPlus) | 3 | BurpBounty 魔改版本 |
| [BurpExtractor](https://github.com/NetSPI/BurpExtractor) | v1.3.4 | A Burp extension for generic extraction and reuse of data within<br> HTTP requests and responses. |
| [burp-cph](https://github.com/elespike/burp-cph) | 3.0 | Custom Parameter Handler extension for Burp Suite. |
| [BurpJSLinkFinder](https://github.com/InitRoot/BurpJSLinkFinder) |  | Burp Extension for a passive scanning JS files for endpoint link<br>s. |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9 | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集；<br>快速Title获取；外部工具联动；等等 |
| [JC-AntiToken](https://github.com/chroblert/JC-AntiToken) |  | burp插件：python版，token防重放绕过 |
| [BurpSuite_403Bypass<br>er](https://github.com/sting8k/BurpSuite_403Bypasser) |  | Burpsuite Extension to bypass 403 restricted directory |
| [Burp-Non-HTTP-Exten<br>sion](https://github.com/summitt/Burp-Non-HTTP-Extension) | v1.6 | Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suite. |
| [Burp-Non-HTTP-Exten<br>sion](https://github.com/summitt/Burp-Non-HTTP-Extension) | v1.6 | Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suite. |
| [shiro-check](https://github.com/bigsizeme/shiro-check) | shirochek<br>3.0 | Shiro反序列化回显利用、内存shell、检查 Burp插件 |
| [FastjsonScan](https://github.com/Maskhe/FastjsonScan) | 1.0 | 一个简单的Fastjson反序列化检测burp插件 |
| [fastjsonScan](https://github.com/zilong3033/fastjsonScan) |  |  |
| [BurpSuite-Extender-<br>fastjson](https://github.com/uknowsec/BurpSuite-Extender-fastjson) |  | Reference：https://www.w2n1ck.com/article/44/ |
| [BurpSuite-Xkeys](https://github.com/vsec7/BurpSuite-Xkeys) |  | A Burp Suite Extension to extract interesting strings (key, secr<br>et, token, or etc.) from a webpage. |
| [Burp_AES_Plugin](https://github.com/jas502n/Burp_AES_Plugin) |  | Burpsuite Plugin For AES Crack |
| [burpJsEncrypter](https://github.com/TheKingOfDuck/burpJsEncrypter) | 0.1 | More Easier Burp Extension To Solve Javascript Front End Encrypt<br>ion,一款更易使用的解决前端加密问题的Burp插件。 |
| [burp-requests](https://github.com/silentsignal/burp-requests) | v0.2.4 | Copy as requests plugin for Burp Suite |
| [captcha-killer](https://github.com/c0ny1/captcha-killer) | 0.1.2 | burp验证码识别接口调用插件 |
| [BurpSuiteHTTPSmuggl<br>er](https://github.com/nccgroup/BurpSuiteHTTPSmuggler) | v0.1 | A Burp Suite extension to help pentesters to bypass WAFs or test<br> their effectiveness using a number of techniques |
| [sqlmap4burp-plus-pl<br>us](https://github.com/c0ny1/sqlmap4burp-plus-plus) | 0.2 | sqlmap4burp++是一款兼容Windows，mac，linux多个系统平台的Burp与sq<br>lmap联动插件 |
| [passive-scan-client](https://github.com/c0ny1/passive-scan-client) | 0.3.1 | Burp被动扫描流量转发插件 |
| [domain_hunter](https://github.com/bit4woo/domain_hunter) | v1.5 | A Burp Suite Extension that try to find all sub-domain, similar-<br>domain and related-domain of an organization automatically! 基于<br>流量自动收集整个企业或组织的子域名、相似域名、相关域名的burp插件 |
| [reCAPTCHA/blob](https://github.com/bit4woo/reCAPTCHA/blob) |  |  |
| [BurpSuiteLoggerPlus<br>Plus](https://github.com/nccgroup/BurpSuiteLoggerPlusPlus) |  |  |
| [HackBar](https://github.com/d3vilbug/HackBar) | 2.0 | HackBar plugin for Burpsuite |
| [chunked-coding-conv<br>erter](https://github.com/c0ny1/chunked-coding-converter) | 0.4.0 | Burp suite 分块传输辅助插件 |
| [TsojanScan](https://github.com/Tsojan/TsojanScan) | v1.4.4 | 一个集成的BurpSuite漏洞探测插件 |
### xray
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [yarx](https://github.com/zema1/yarx) | v0.2.0 | An awesome reverse engine for xray poc. | 一个自动化根据 xray po<br>c 生成对应靶站的工具 |
| [xray-poc-generation](https://github.com/phith0n/xray-poc-generation) |  | 🧬 辅助生成 XRay YAML POC |
| [super-xray](https://github.com/4ra1n/super-xray) | 1.6 | Web漏洞扫描工具XRAY的GUI启动器 (Web Vulnerability Scanner GUI St<br>arter) |
| [Xray_Cracked](https://github.com/NHPT/Xray_Cracked) | v1.9.8 | Update Xray1.9.8 Cracked for Windows,Linux and Mac OS. |
### pocsuite3
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ExpToPocsuite3](https://github.com/smallfox233/ExpToPocsuite3) | v1.0 | goby exp批量转换为pocsuite3 exp脚本 |
### 浏览器扩展
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Hack-Tools](https://github.com/LasCC/Hack-Tools) | 0.5.0 | The all-in-one Red Team extension for Web Pentester 🛠 |
| [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega) | v2.5.20 | Manage and switch between multiple proxies quickly & easily. |
| [untrusted-types](https://github.com/filedescriptor/untrusted-types) | 1.1.1 |  |
| [fofa_view](https://github.com/fofapro/fofa_view) | v0.0.5 | FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件，目前兼容Chrome<br>、Firefox、Opera。 |
| [mitaka](https://github.com/ninoseki/mitaka) | v1.2.0 | A browser extension for OSINT search |
| [anti-honeypot](https://github.com/cnrstar/anti-honeypot) |  | 一款可以检测WEB蜜罐并阻断请求的Chrome插件 |
| [Chromium-based-XSS-<br>Taint-Tracking](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) | v0.3 | Cyclops 是一款具有 XSS 检测功能的浏览器 |
| [Zoomeye-Tools](https://github.com/knownsec/Zoomeye-Tools) |  | Zoomeye Tools是配合Zoomeye使用的Chrome插件 |
| [Heimdallr](https://github.com/graynjo/Heimdallr) |  |  |
### pocassist
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pocassistdb](https://github.com/jweny/pocassistdb) | 1.0.2 | database of pocassist（漏洞库） |
### goby
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Library-POC](https://github.com/luck-ying/Library-POC) |  | 基于Pocsuite3、goby编写的漏洞poc&exp存档 |
### volatility
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [tool-for-CTF](https://github.com/ruokeqx/tool-for-CTF) |  | Virtual machine configuration for CTF |
### nuclei
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [NucleiTP](https://github.com/ExpLangcn/NucleiTP) |  | 自动整合全网Nuclei的漏洞POC，实时同步更新最新POC！ |
| [nucleix](https://github.com/mlq574/nucleix) |  | 整合nuclei与xray(社区版、自带高级版)，实现被动扫描+poc扫描自动化<br>渗透流程 |
| [nuclei-plus](https://github.com/Yong-An-Dang/nuclei-plus) | v7.0.0 | Functional enhancement based on nuclei |
### nessus
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [NessusToReport](https://github.com/Hypdncy/NessusToReport) | v1.2 | Nessus扫描报告自动化生成工具 |
| [NessusReportInChine<br>se](https://github.com/FunnyKun/NessusReportInChinese) |  | 半自动化将 Nessus 英文报告（csv格式）生成中文 excel ，中文漏洞库<br>已有700多条常见漏洞，后续再进一步加上新漏洞自动翻译，实现全自动化 |
| [CN_Nessus_Plugins_I<br>nterface](https://github.com/nszy007/CN_Nessus_Plugins_Interface) | 1 | nessus插件中文查询接口 |
| [docker_nessus_unlim<br>ited](https://github.com/xxcdd/docker_nessus_unlimited) |  | docker build nessus with unlimited ip |
| [nessus_api](https://github.com/starnightcyber/nessus_api) |  | Nessus REST API 封装 |
### rsas
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [nsfocus-rsas-knowle<br>dge-base](https://github.com/biggerwing/nsfocus-rsas-knowledge-base) |  | 绿盟科技漏洞扫描器(RSAS)漏洞库 |
| [RSAS-Data-Export](https://github.com/autoing/RSAS-Data-Export) | 2022-9-9 | 绿盟极光远程安全评估系统(RSAS)-RSAS漏洞数据导出工具 |
| [RSAS-Task-Release](https://github.com/autoing/RSAS-Task-Release) | v1.0 | 绿盟极光远程安全评估系统(RSAS)-RSAS批量下任务工具 |
### arl
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ARL-Finger-ADD](https://github.com/loecho-sec/ARL-Finger-ADD) |  | 灯塔（最新版）指纹添加脚本！ |
### cobaltstrike
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [taowu-cobalt-strike](https://github.com/pandasec888/taowu-cobalt-strike) |  |  |
| [geacon_pro](https://github.com/H4de5-7/geacon_pro) |  |  |
| [SharkExec](https://github.com/F3eev/SharkExec) |  | 内网渗透|红队工具|C#内存加载|cobaltstrike |
| [LSTAR](https://github.com/lintstar/LSTAR) | v2.1 | LSTAR - CobaltStrike 综合后渗透插件 |
### ZoomEye
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Kunyu](https://github.com/knownsec/Kunyu) | v1.7.2 | Kunyu, more efficient corporate asset collection |
| [ZoomEye-python](https://github.com/knownsec/ZoomEye-python) | v2.2.0 | ZoomEye-python: The official Python library and CLI by Knownsec <br>404 Team. |
| [ZoomEye-go](https://github.com/gyyyy/ZoomEye-go) | v1.5 | The Golang SDK and CLI of ZoomEye@Knownsec by gyyyy. |
### frida
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [frida-skeleton](https://github.com/Margular/frida-skeleton) | v2.0.0 | 基于frida的安卓hook框架，提供了很多frida自身不支持的功能，将hook<br>安卓变成简单便捷，人人都会的事情 |
### fofa
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [fofax](https://github.com/xiecat/fofax) | v0.1.44 | fofax is a command line query tool based on the API of https://f<br>ofa.info/, simple is the best! |
| [fofa_viewer](https://github.com/wgpsec/fofa_viewer) | 1.1.12 | A simple FOFA client written in JavaFX.Made by WgpSec, Maintaine<br>d by f1ashine. |
| [fofa_GUI](https://github.com/20142995/fofa_GUI) | v1.0.0 |  |
# CTF
## 杂项
### 图片隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegsolve](https://github.com/Giotino/stegsolve) | v1.4 |  |
| [BlindWatermark](https://github.com/ww23/BlindWatermark) | v0.0.3 | Java 盲水印 |
| [cloacked-pixel](https://github.com/livz/cloacked-pixel) |  | LSB steganography and detection |
| [CTFpics](https://github.com/RetrO-hash/CTFpics) |  | 用于自动化检测CTF中常出现得工具图片隐写题目 |
| [ImageStrike](https://github.com/zR00t1/ImageStrike) | V0.2 | ImageStrike是一款用于CTF中图片隐写的综合利用工具 |
| [stegpy](https://github.com/dhsdshdhk/stegpy) |  | Simple steganography program based on the LSB method. |
### 流量分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [UsbMiceDataHacker](https://github.com/WangYihang/UsbMiceDataHacker) |  | USB鼠标流量包取证工具 , 主要用于绘制鼠标移动以及拖动轨迹 |
| [UsbKeyboardDataHack<br>er](https://github.com/WangYihang/UsbKeyboardDataHacker) |  | USB键盘流量包取证工具 , 用于恢复用户的击键信息 |
### 编码解码
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [TomatoTools](https://github.com/ht0Ruial/TomatoTools) | v1.0.2 | TomatoTools 一款CTF杂项利器，支持36种常见编码和密码算法的加密和<br>解密，31种密文的分析和识别，支持自动提取flag，自定义插件等。 |
| [CyberChef](https://github.com/gchq/CyberChef) | v10.4.0 | The Cyber Swiss Army Knife - a web app for encryption, encoding,<br> compression and data analysis |
### 取证分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pyvmx-cracker](https://github.com/axcheron/pyvmx-cracker) |  | Simple tool to crack VMware VMX encryption passwords |
| [chatViewTool](https://github.com/Ormicron/chatViewTool) | BEAT | 基于Java实现的图形化微信聊天记录解密查看器 |
| [Sharp-dumpkey](https://github.com/Ormicron/Sharp-dumpkey) | 1 | 基于C#实现的获取微信数据库密钥的小工具 |
| [Sunflower_get_Passw<br>ord](https://github.com/wafinfo/Sunflower_get_Password) |  | 一款针对向日葵的识别码和验证码提取工具 |
| [SharpWxDump](https://github.com/AdminTest0/SharpWxDump) |  | 微信客户端取证，可获取用户个人信息(昵称/账号/手机/邮箱/数据库密<br>钥(用来解密聊天记录))；支持获取多用户信息，不定期更新新版本偏移，<br>目前支持所有新版本、正式版本 |
| [GoWxDump](https://github.com/SpenserCai/GoWxDump) | v1.0.10 | SharpWxDump的Go语言版。微信客户端取证，获取信息(微信号、手机号、<br>昵称)，微信聊天记录分析(Top N聊天的人、统计聊天最频繁的好友排行、<br>关键词列表搜索等) |
### 音频隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dtmf-decoder](https://github.com/ribt/dtmf-decoder) |  | Extract phone numbers from an audio recording of the dial tones. |
### 文件分离
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BlindWaterMark](https://github.com/chishaxie/BlindWaterMark) |  | 盲水印 by python |
### 压缩文件分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CRC32-Tools](https://github.com/AabyssZG/CRC32-Tools) | 2.2 | Easy CRC32 Tools，so easy！！！ |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools) |  | 渊龙Sec安全团队CTF&AWD工具箱 |
| [qsnctf-python](https://github.com/Moxin1044/qsnctf-python) | 0.0.8.9 | 青少年CTF的Python包，方便大家调用一些CTF常用功能。 |
| [CTF-Tools](https://github.com/qianxiao996/CTF-Tools) | v1.3.7 | 一款Python+Pyqt写的CTF编码、解码、加密、解密工具。 |
| [CTF_Hacker-Tools](https://github.com/Harveysn0w/CTF_Hacker-Tools) |  |  |
## 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CTF-Note](https://github.com/kitezzzGrim/CTF-Note) |  | CTF笔记：该项目主要记录CTF知识、刷题记录、工具等。 |
## 逆向
### pyc逆向
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegosaurus](https://github.com/AngelKitty/stegosaurus) | 1.0 | A steganography tool for embedding payloads within Python byteco<br>de. |
### Java反编译
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [JavaDecompileTool-G<br>UI](https://github.com/MountCloud/JavaDecompileTool-GUI) | V1.2 | Java Decompile Tool GUI-JAVA反编译工具（界面版） |
| [CodeReviewTools](https://github.com/Ppsoft1991/CodeReviewTools) | v1.31 | 通过正则搜索、批量反编译特定Jar包中的class名称 |
## WEB
### 敏感目录
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ctf-wscan](https://github.com/OrangeWatermelon/ctf-wscan) |  | 在kingkaki的项目上进行了修改，改为单线程，可以在任意目录下执行，<br>对重复的请求进行了过滤 |
| [scrabble](https://github.com/denny0223/scrabble) |  | Simple tool to recover .git folder from remote server |
## 密码学
### RSA
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [rsa-wiener-attack](https://github.com/pablocelayes/rsa-wiener-attack) |  | A Python implementation of the Wiener attack on RSA public-key e<br>ncryption scheme. |
| [RSA](https://github.com/Mr-Aur0ra/RSA) |  |  |
| [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) |  | RSA attack tool (mainly for ctf) - retreive private key from wea<br>k public key and/or uncipher data |
# 应急响应
## web日志分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [DecodeSomeJSPWebshe<br>ll](https://github.com/minhangxiaohui/DecodeSomeJSPWebshell) | v1.2 | 冰蝎、哥斯拉 jsp webshell通信流量解密器 |
## 内存马查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shell-analyzer](https://github.com/4ra1n/shell-analyzer) | 0.1 | Java内存马查杀GUI工具，实时动态分析，支持本地和远程查杀 |
## 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Emergency-Response-<br>Notes](https://github.com/Bypass007/Emergency-Response-Notes) |  | 应急响应实战笔记，一个安全工程师的自我修养。 |
## 后门查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmTools](https://github.com/RoomaSec/RmTools) |  | 蓝队应急工具 |
# 其他
## 其他
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [faker](https://github.com/joke2k/faker) | v18.5.1 | Faker is a Python package that generates fake data for you. |
| [SmsForwarder](https://github.com/pppscn/SmsForwarder) | v3.2.0 | 短信转发器——监控Android手机短信、来电、APP通知，并根据指定规则<br>转发到其他手机：钉钉群自定义机器人、钉钉企业内机器人、企业微信群机<br>器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram<br>机器人、Server酱、PushPlus、手机短信等。包括主动控制服务端与客户端<br>，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。（V3.0 新<br>增）PS.这个APK主要是学习与自用，如有BUG请提ISSUE，同时欢迎大家提PR<br>指正 |
| [dbeaver](https://github.com/dbeaver/dbeaver) | 23.0.3 | Free universal database tool and SQL client |
| [MySQLMonitor](https://github.com/TheKingOfDuck/MySQLMonitor) | 1.0 | MySQL实时监控工具(代码审计/黑盒/白盒审计辅助工具) |
| [flightsim](https://github.com/alphasoc/flightsim) | v2.3.0 | A utility to safely generate malicious network traffic patterns <br>and evaluate controls. |
## 渗透测试报告辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [APTRS](https://github.com/Anof-cyber/APTRS) |  | Automated Penetration Testing Reporting System |
| [BugRepoter_0x727](https://github.com/0x727/BugRepoter_0x727) |  | BugRepoter_0x727(自动化编写报告平台)根据安全团队定制化协同管理项<br>目安全，可快速查找历史漏洞，批量导出报告。 |
| [Savior](https://github.com/Mustard404/Savior) | new | 渗透测试报告自动生成工具！ |
| [SAReport](https://github.com/1u0Hun/SAReport) |  | 渗透测试自动化报告平台 |
| [pentest_report](https://github.com/dbgee/pentest_report) | v1.0.0 | A pentest reporter generator |
| [WaterExp](https://github.com/linshaoSec/WaterExp) |  | WaterExp:面向安服仔的 水报告模板和工具 |
## 动态口令
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [rotp](https://github.com/mdp/rotp) |  | Ruby One Time Password library |
## 科学上网
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [v2rayA](https://github.com/v2rayA/v2rayA) | v2.0.5 | A web GUI client of Project V which supports V2Ray, Xray, SS, SS<br>R, Trojan and Pingtunnel 🚀 |
## 笔记
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) |  | Python - 100天从新手到大师 |
## 渗透测试报告管理
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [report](https://github.com/CTF-MissFeng/report) | v1.0.1 | 乙方渗透测试漏洞报告管理系统 |
## 文档
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [HackReport](https://github.com/awake1t/HackReport) |  | 渗透测试报告/资料文档/渗透经验文档/安全书籍 |
## 文字识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | v1.3.4 | OCR图片转文字识别软件，完全离线。截屏/批量导入图片，支持多国语言<br>、合并段落、竖排文字。可排除水印区域，提取干净的文本。基于 PaddleO<br>CR 。 |
# 安全产品
## 威胁检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmEye](https://github.com/RoomaSec/RmEye) | v0.0.4 | 戎码之眼是一个window上的基于att&ck模型的威胁监控工具.有效检测常<br>见的未知威胁与已知威胁.防守方的利剑 |
## 主机入侵检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Elkeid](https://github.com/bytedance/Elkeid) | v1.7.0.11<br>-driver-ko<br>-20230426 | Elkeid is an open source solution that can meet the security req<br>uirements of various workloads such as hosts, containers and K8s,<br> and serverless. It is derived from ByteDance's internal best pra<br>ctices. |
| [Hades](https://github.com/theSecHunter/Hades) |  | Hades is an cross-platform HIDS with kernel-space data collectio<br>n. |
## Web应用防火墙
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [openstar](https://github.com/starjun/openstar) |  | lua waf,nginx+lua,openresty,luajit,waf+,cdn,nginx |
| [safeline](https://github.com/chaitin/safeline) | v1.1.0 | 长亭科技自研，基于业界领先的语义引擎检测技术，打造的简洁、易用的<br>免费 WAF |
## 欺骗防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Juggler](https://github.com/C4o/Juggler) |  | A system that may trick hackers.针对黑客的拟态欺骗系统。 |
| [MySQL_Fake_Server](https://github.com/fnmsd/MySQL_Fake_Server) |  | MySQL Fake Server use to help MySQL Client File Reading and JDBC<br> Client Java Deserialize |
| [MysqlT](https://github.com/BeichenDream/MysqlT) | v1.0 | 伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击攻<br>击者 |
## 主机入侵防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [iDefender](https://github.com/wecooperate/iDefender) | 2.6.0 | iDefender（冰盾 - 终端主动防御系统） |
# 靶场
## web靶场
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ElectricRat](https://github.com/linjiananallnt/ElectricRat) | v1.3.0 | 电气鼠靶场系统是一种带有漏洞的Web应用程序，旨在为Web安全渗透测试<br>学习者提供学习和实践的机会。The Electrical Mouse Target Range Syst<br>em is a web application with vulnerabilities designed to provide <br>learning and practice opportunities for web security penetration <br>testing learners. |
| [vulstudy](https://github.com/c0ny1/vulstudy) |  | 使用docker快速搭建各大漏洞靶场，目前可以一键搭建17个靶场。 |
| [sqli-labs](https://github.com/Audi-1/sqli-labs) |  | SQLI labs to test error based, Blind boolean based, Time based. |
| [bodgeit](https://github.com/psiinon/bodgeit) | 1.4.0 | The BodgeIt Store is a vulnerable web application which is curre<br>ntly aimed at people who are new to pen testing.  |
| [WackoPicko](https://github.com/adamdoupe/WackoPicko) |  | WackoPicko is a vulnerable web application used to test web appl<br>ication vulnerability scanners. |
| [WebGoat](https://github.com/WebGoat/WebGoat) | v2023.4 | WebGoat is a deliberately insecure application |
| [hackademic](https://github.com/Hackademic/hackademic) |  | the main hackademic code repository |
| [xssed](https://github.com/aj00200/xssed) |  | A set of XSS vulnerable PHP scripts for testing |
| [DSVW](https://github.com/stamparm/DSVW) |  | Damn Small Vulnerable Web |
| [vulnerable-node](https://github.com/cr0hn/vulnerable-node) |  | A very vulnerable web site written in NodeJS with the purpose of<br> have a project with identified vulnerabilities to test the quali<br>ty of security analyzers tools tools |
| [MCIR](https://github.com/SpiderLabs/MCIR) |  | The Magical Code Injection Rainbow! MCIR is a framework for buil<br>ding configurable vulnerability testbeds. MCIR is also a collecti<br>on of configurable vulnerability testbeds. |