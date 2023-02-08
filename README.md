# 更新于 2023-02-08 09:06:48

## 近30天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
|2023-02-07 20:37:21|[faker](https://github.com/joke2k/faker)|v16.7.0|See [CHANGELOG.md](https://github.com/j<br>oke2k/faker/blob/refs/tags/v16.7.0/CHANG<br>ELOG.md).|
|2023-02-06 09:28:04|[ffuf](https://github.com/ffuf/ffuf)|v2.0.0|## Changelog
* e952deb Fix the v2 taggi<br>ng for go install (#639)
* 19e07c0 Fix r<br>equired go version (#637)
* 77cc45c Prep<br>are for v2.0 release (#635)
* c7d0fb5 Gr<br>acefully error in case stdin is used for<br> search result (#634)
* 643f6b8 Scraper <br>functionality (#633)
* 39c8934 Added add<br>itional proxy URL verification (#574)
* <br>bbb97ab Typo fix (#581)
* 3b219f2 fix: c<br>hanged usage from version 1.3.0 to versi<br>on 1.5.0 (#595)
* 633893c Change precede<br>nce of quiet and JSON output to favour J<br>SON (#570)
* 0236210 Add homebrew instal<br>l method (#552)
* 7bff9e7 Fix time-based<br> matcher (#575)
* ebb4c44 Sniper templat<br>e parsing - fixes #579 (#580)
* 9bddff7 <br>New functionality to map fired blind pay<br>loads back to the initial request (#632)<br>
* b7adc50 Fix jsonlines output while in<br> silent mode (#630)
* 2ce2217 Enhanced r<br>ate limiting (#620)
* 1a684a9 Fix the ac<br> for good now (#615)
* 3328a28 Fix linte<br>r workflow and autocalibration for lines<br> & words match (#614)|
|2023-02-05 18:31:19|[dbeaver](https://github.com/dbeaver/dbeaver)|22.3.4|- ChatGPT integration for smart complet<br>ion and code generation (as optional ext<br>ension)- Accessibility:- Text reader for<br> entity editor was improved- Text reader<br> for data grid was improved- SQL editor:<br>- Query generation from human language t<br>ext was added- Server output log levels <br>configuration was improved- Global metad<br>ata search was fixed- Variables resoluti<br>on is fixed in strings and comments- Iss<br>ue with queries with invalid line feeds <br>was resolved- Data editor:- Grouping pan<br>el messages were improved- Datetime cale<br>ndar editor was fixed (in panel and inli<br>ne editor)- Database navigator: issue wi<br>th rename/refresh was resolved- Dashboar<br>ds were fixed for inherited databases- P<br>roject import now sets DBeaver nature (t<br>hanks to @froque- ERD: custom diagram ed<br>itor was fixed (issue wth missing notes <br>and connections was resolved)- Databrick<br>s: table DDL reading was fixed, extra SQ<br>L keywords were added (thanks to @mixam2<br>4)- DB2 BigSQL: table with RID_BIT colum<br>ns data reading was fixed (thanks to @bk<br>yle)- MySQL: numeric identifiers quoting<br> was fixed- Netezza: tables/views search<br> query was improved- PostgreSQL:- Proced<br>ures invocation was improved (thanks to <br>@plotn)- Filter by enum was fixed (thank<br>s to @plotn)- Redshift: triggers DDL rea<br>ding was fixed- Snowflake: table constra<br>ints reading was fixed- We switched to J<br>ava 17 so now DBeaver supports all newes<br>t JDBC drivers|
|2023-02-04 14:54:34|[afrog](https://github.com/zan8in/afrog)|v2.2.1|Merge many fingerprint pocs into the pa<br>nel-detect.yaml file to reduce the numbe<br>r of http requestsConsoleprint date form<br>at, 2023-01-01 changed to 01-01Simplifie<br>d afrog-config configurationFixed: inval<br>id -fc configurationTip: Configure the -<br>c command, which can increase the concur<br>rency speed very quickly----------------<br>----------------------------------------<br>---------------------将多个 panel 指纹探<br>测合并到文件 panel-detect.yaml，大幅减少 <br>http 请求精简控制台日期打印，2023-01-01 <br>改为 01-01精简 afrog-config 配置信息解决<br>：-fc 命令配置无效问题提示：配置 -c 命令<br>能明显提高扫描速度|
|2023-02-04 08:54:47|[URLFinder](https://github.com/pingc0y/URLFinder)|2023.2.3|## 2023/2/3 更新新增 域名信息展示变化 -<br>i配置文件可配置抓取规则等|
|2023-02-03 10:17:50|[passive-scan-client](https://github.com/c0ny1/passive-scan-client)|0.3.1|1. 添加url黑明单2. 添加右键Send to Pass<br>ive Scan Client手动转发thx @i11us0ry |
|2023-02-01 03:28:42|[captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified)|0.21|【2023-2-1】 0.21- 增加默认验证码模板dd<br>ddocr，适配codereg.py- 增加识别结果关键<br>字显示，方便查看关键字是否与验证码对应|
|2023-01-30 08:25:35|[railgun](https://github.com/lz520520/railgun)|v1.5.2|解压密码railgun1. 增加gRPC模式，扩展ser<br>ver端a. 实现了dnslog，通过客户端可直接管<br>理server，并做了一些优化。b. 实现了UDP/TC<br>P的socket反连，通过不同伪装头部来过滤。c<br>. 实现了ICMP反连，通过发送特定长度的ping<br>包来过滤。d. 实现HTTP/HTTPS serverⅰ. HTT<br>P LOG1. 增加http 完整请求包记录ⅱ. 任意<br>内容和大文件下载ⅲ. 扩展服务配置参数，并<br>添加已启动服务信息单独查看窗口。e. gRPC完<br>成tls双向认证f. 增加鉴权，目前只设置管理<br>员和普通用户。g. 历史搜索里，增加查询服务<br>端数据库，目前暂定管理员可查（迁移至gRPC<br>模块）。h. 增加单独gRPC模块，可用于gRPC的<br>设置、用户管理以及历史搜索。2. 编码转换a.<br> 将https://github.com/lz520520/encrypt-j<br>s 合入，通过Dict2ConsoleJS和ConsoleExtra<br>ctEncryptPwd两种编码来实现|
|2023-01-24 19:34:39|[nuclei](https://github.com/projectdiscovery/nuclei)|v2.8.8|## What's Changed* **Fixed url encoding<br> issues by @tarunKoyalwar** in https://g<br>ithub.com/projectdiscovery/nuclei/pull/3<br>211* **Fixed host spray race condition b<br>y @tarunKoyalwar** in https://github.com<br>/projectdiscovery/nuclei/pull/3213* Fixe<br>d panic crash with non-existent target i<br>nput by @Ice3man543 in https://github.co<br>m/projectdiscovery/nuclei/pull/3205* Fix<br>ed aws signer missing template variables<br> by @tarunKoyalwar in https://github.com<br>/projectdiscovery/nuclei/pull/3206* **Ad<br>ded clustering support for DNS templates<br> by @Ice3man543** in https://github.com/<br>projectdiscovery/nuclei/pull/3204* **Add<br>ed clustering support for TLS templates <br>by @Ice3man543** in https://github.com/p<br>rojectdiscovery/nuclei/pull/3209* Added <br>support for -no-mhe option by @Mzack9999<br> in https://github.com/projectdiscovery/<br>nuclei/pull/3219Issues closed in release<br> - https://github.com/projectdiscovery/n<br>uclei/milestone/25?closed=1## New Contri<br>butors* @AndreAngelucci made their first<br> contribution in https://github.com/proj<br>ectdiscovery/nuclei/pull/3214**Full Chan<br>gelog**: https://github.com/projectdisco<br>very/nuclei/compare/v2.8.7...v2.8.8|
|2023-01-20 18:22:12|[OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL)|OA-EXPTOO<br>L-v0.7|更新内容如下：1.代理功能已经实装2.日志<br>功能已经载入源码，目前只有一米OA会产生日<br>志（日志第二次调用会产生问题，暂不实装）<br>修复部分poc报错问题，修复通达OAshell的代<br>码错误导致无法连接问题增加泛微OA_doexcel<br>泛微OA_ktree_upload泛微OA_v10_OfficeServe<br>r.phpuploadweaveroa-eoffice8-upload-RCE<br>增加用友：yongyou_KSOA_imageupload|
|2023-01-19 06:03:37|[super-xray](https://github.com/4ra1n/super-xray)|1.4|## 1.4春节快乐，从该版本以后使用更帅的*<br>*黑暗主题**，并且简单重构了UI解决了重要<br>的问题：CPU占用过高。允许QPS和最大HOST连<br>接数等参数的设置，优化了一些功能更新内容<br>：- [important] [improve] CPU占用较高需要<br>进行优化 #128- [important] [feat] 1.4版本<br>以后将全面适配黑暗主题（更帅一些） #135- <br>[important] [feat] 每秒最大http请求数max<br>_qps参数设置 #137- [bug] 提示文字的翻译<br>有误 #133- [feat] 被动扫描允许自由设置（<br>目前仅支持127） #131- [feat] 最大HOST允许<br>的连接数（降低对服务的影响） #138- [impro<br>ve] 查看搜索PoC时应该排序以提高效率 #134<br>- [improve] 不常用的配置应该都移到高级配<br>置中 #132- [improve] 避免直接使用其他项目<br>的图标 #130- [improve] 删除没有必要的动态<br>皮肤并简单重构UI #136- 使用更好的exe图标-<br> 删除扫雷和弹球（不好玩且与黑暗主题不适<br>配）下载：- super-xray-1.4.jar版本通过jav<br>a -jar super-xray-1.4.jar启动- super-xra<br>y-1.4-jre-exe.zip是内置了JRE的exe版本- s<br>uper-xray-1.4-system-jre.exe是使用系统JR<br>E的exe版本|
|2023-01-17 10:55:12|[Goby](https://github.com/gobysec/Goby)|Beta2.2.0|# In this update## Community version up<br>date:1. New memory shell plugin2. ShellH<br>ub plugin update3. Vulnerability module <br>added a function to generate deserializa<br>tion Payload, through the memory shell i<br>njection process4. Five Java deserializa<br>tion vulnerabilities were added, includi<br>ng- Bonitasoft Platform serverAPI Deseri<br>alization Vulnerability- Liferay Portal <br>Unauthenticated 7.2.1 C3P0 Deserializati<br>on Vulnerability (CVE-2020-7961)- Manage<br>Engine OpManager Deserialization Vulnera<br>bility (CVE-2020-28653)- Zkteco Shiro De<br>serialization Vulnerability- ZOHO Manage<br>Engine Password Manager Pro Deserializat<br>ion Vulnerability5. Fixed the problem th<br>at the environment variable http_proxy c<br>aused Goby to report errors abnormally6.<br> Goby can now be updated online and vuln<br>erabilities can be updated even if Goby <br>is not in the Mac system Application dir<br>ectory7. Fixed the problem of occasional<br> white horizontal lines in Goby8. remove<br> network error report## Red team/Enterpr<br>ise version update content1. All update <br>content of 2.2.0 community version2. 20 <br>new deserialization vulnerabilities were<br> added, including- Apache OFBiz xmlrpc D<br>eserialization Vulnerability (CVE-2020-9<br>496)- Apereo CAS Before 4.1.7 Deserializ<br>ation Vulnerability- Dreamer CMS Shiro D<br>eserialization Vulnerability- EasyReport<br> Shiro Deserialization Vulnerability- FE<br>BS Shiro Deserialization Vulnerability- <br>FH Admin Shiro Deserialization Vulnerabi<br>lity- FineReport V10 Deserialization RCE<br> Vulnerability- ForgeRock AM Deserializa<br>tion Vulnerability (CVE-2021-35464)- Gun<br>s Shiro Deserialization Vulnerability- J<br>2eeFAST Shiro Deserialization Vulnerabil<br>ity- JavaWeb_Layui Shiro Deserialization<br> Vulnerability- Liferay Portal 6.1.1 CE <br>GA2 CB Deserialization Vulnerability- MC<br>MS Shiro Deserialization Vulnerability (<br>CVE-2022-22928)- OneBlog Shiro Deseriali<br>zation Vulnerability- pb-cms Shiro Deser<br>ialization Vulnerability- QVIS-NVR Camer<br>a Management System RCE (CVE-2021-41419)<br>- RuoYi-plus Shiro Deserialization Vulne<br>rability- TIMO Shiro Deserialization Vul<br>nerability- Ysk ERP Shiro Deserializatio<br>n Vulnerability**Zkteco Shiro Deserializ<br>ation Vulnerability**![5s8l2F.gif](https<br>://www.gobies.org/img/Zkteco_Shiro_Deser<br>ialization_Vulnerability.gif)**Apache OF<br>Biz xmlrpc Deserialization Vulnerability<br> (CVE-2020-9496)**![5s8l2F.gif](https://<br>www.gobies.org/img/OneBlog_Shiro_Deseria<br>lization_Vulnerability.gif)|
|2023-01-13 07:43:44|[RequestTemplate](https://github.com/1n7erface/RequestTemplate)|v1.1.1|2023.1.13 13:441.通过列出共享解决了部分<br>smb误报的问题。2.列出ftp文件。3.通过OXID<br>识别多网卡机器。|
|2023-01-10 07:36:28|[NessusToReport](https://github.com/Hypdncy/NessusToReport)|v1.1.1||
|2023-01-10 07:30:58|[xray](https://github.com/chaitin/xray)|1.9.4|# 更新内容## 插件更新1. 添加[XStream扫<br>描插件](https://docs.xray.cool/#/configra<br>tion/plugins?id=xstream)，支持列表如下（<br>该插件需开启反连平台）- CVE-2021-21344- C<br>VE-2021-21345- CVE-2021-39141- CVE-2021-<br>39144- ...(共29个插件)2. fastjson插件支<br>持cve-2022-25845的检测## POC编写/执行更新<br>1. 新增警告信息，师傅们可以根据警告信息<br>删除检测插件创建的文件等2. 支持在GET，HEA<br>D，OPTION时添加body3. 添加[compare versi<br>on](https://docs.xray.cool/#/guide/poc/f<br>unc?id=版本)函数，可以对匹配出的版本进行<br>对比4. 添加[html实体编码](https://docs.xr<br>ay.cool/#/guide/poc/example/encode/htmlE<br>scape)/[解码](https://docs.xray.cool/#/g<br>uide/poc/example/encode/htmlUnescape)函<br>数5. 添加[java反序列化函数](https://docs.<br>xray.cool/#/guide/poc/example/ysoGadget/<br>javaGadget)6. 添加[hex](https://docs.xra<br>y.cool/#/guide/poc/example/encode/hex)/[<br>hexDecode](https://docs.xray.cool/#/guid<br>e/poc/example/encode/hexDecode)函数## 优<br>化内容1. 优化了反连平台漏洞捕获逻辑，提高<br>了命中率2. 优化了 poc lint 变得更人性化3.<br> yaml脚本支持获取rmi反连平台的链接，具体<br>使用请参考官方文档4. 优化了Struts2检测模<br>块，添加反连确认，减少误报漏报## 修复POC#<br>## 规则优化，规则弱poc-yaml-drawio-cve-2<br>022-1713-ssrfpoc-yaml-h3c-cvm-upload-fil<br>e-uploadpoc-yaml-iis-cve-2017-7269poc-ya<br>ml-74cms-sqli-cve-2020-22209poc-yaml-rep<br>orter-file-readpoc-yaml-wanhu-ezoffice-d<br>ocumentedit-sqlipoc-yaml-joomla-cve-2017<br>-8917-sqlipoc-yaml-iis-cve-2017-7269poc-<br>yaml-emerge-e3-cve-2019-7256poc-yaml-ali<br>baba-nacos-v1-auth-bypasspoc-yaml-wanhu-<br>ezoffice-documentedit-sqlipoc-yaml-magic<br>flow-gateway-main-xp-file-readpoc-yaml-g<br>itblit-cve-2022-31268poc-yaml-phpstudy-n<br>ginx-wrong-resolvepoc-yaml-confluence-cv<br>e-2022-26138poc-yaml-metinfo-lfi-cnvd-20<br>18-13393poc-yaml-zabbix-cve-2019-17382po<br>c-yaml-wordpress-paypal-pro-cve-2020-140<br>92-sqlipoc-yaml-vite-cnvd-2022-44615poc-<br>yaml-phpmyadmin-cve-2018-12613-file-incl<br>usionpoc-yaml-zabbix-cve-2022-23134poc-y<br>aml-ametys-cms-cve-2022-26159### 优化删<br>除（功能与xray的通用插件重复）poc-yaml-ne<br>xusdb-cve-2020-24571-path-traversalpoc-y<br>aml-specoweb-cve-2021-32572-filereadpoc-<br>yaml-tvt-nvms-1000-file-read-cve-2019-20<br>085poc-yaml-zyxel-vmg1312-b10d-cve-2018-<br>19326-path-traversal### 新增无害化处理po<br>c-yaml-fanruan-v9-file-uploadpoc-yaml-h3<br>c-cvm-upload-file-uploadpoc-yaml-seeyon-<br>unauthorized-fileuploadpoc-yaml-thinkcmf<br>-write-shellpoc-yaml-wanhu-oa-officeserv<br>er-file-uploadpoc-yaml-weaver-oa-workrel<br>ate-file-uploadpoc-yaml-yonyou-grp-u8-fi<br>le-uploadpoc-yaml-yonyou-nc-file-accept-<br>uploadpoc-yaml-yonyou-u8c-file-uploadpoc<br>-yaml-zhiyuan-oa-wpsassistservlet-file-u<br>pload## 新增POC 96个poc-yaml-ruijie-file<br>upload-fileupload-rcepoc-yaml-eweaver-oa<br>-mecadminaction-sqlexecpoc-yaml-xxl-job-<br>default-passwordpoc-yaml-wordpress-plugi<br>n-superstorefinder-ssf-social-action-php<br>-sqlipoc-yaml-magento-config-disclosure-<br>info-leakpoc-yaml-ukefu-cnvd-2021-18305-<br>file-readpoc-yaml-ukefu-cnvd-2021-18303-<br>ssrfpoc-yaml-eweaver-eoffice-mainselect-<br>info-leakpoc-yaml-linksys-cnvd-2014-0126<br>0poc-yaml-wordpress-welcart-ecommerce-cv<br>e-2022-41840-path-traversalpoc-yaml-jees<br>ite-userfiles-path-traversalpoc-yaml-yon<br>gyou-nc-iupdateservice-xxepoc-yaml-v-sol<br>-olt-platform-unauth-config-downloadpoc-<br>yaml-ibm-websphere-portal-hcl-cve-2021-2<br>7748-ssrfpoc-yaml-yonyou-nc-uapws-db-inf<br>o-leakpoc-yaml-yonyou-nc-service-info-le<br>akpoc-yaml-yongyou-nc-cloud-fs-sqlipoc-y<br>aml-finecms-filedownloadpoc-yaml-weaver-<br>eoffice-userselect-unauthpoc-yaml-fortin<br>et-cve-2022-40684-auth-bypasspoc-yaml-da<br>pr-dashboard-cve-2022-38817-unauthpoc-ya<br>ml-wordpress-zephyr-project-manager-cve-<br>2022-2840-sqlipoc-yaml-jira-cve-2022-399<br>60-unauthpoc-yaml-qnap-cve-2022-27593-fi<br>leuploadpoc-yaml-wordpress-all-in-one-vi<br>deo-gallery-cve-2022-2633-lfipoc-yaml-at<br>lassian-bitbucket-archive-cve-2022-36804<br>-remote-command-execpoc-yaml-wordpress-s<br>imply-schedule-appointments-cve-2022-237<br>3-unauthpoc-yaml-zoho-manageengine-opman<br>ager-cve-2022-36923poc-yaml-red-hat-free<br>ipa-cve-2022-2414-xxepoc-yaml-wavlink-cv<br>e-2022-2488-rcepoc-yaml-wavlink-cve-2022<br>-34045-info-leakpoc-yaml-wordpress-share<br>aholic-cve-2022-0594-info-leakpoc-yaml-w<br>ordpress-wp-stats-manager-cve-2022-33965<br>-sqlipoc-yaml-opencart-newsletter-custom<br>-popup-sqlipoc-yaml-wordpress-events-mad<br>e-easy-cve-2022-1905-sqlipoc-yaml-wordpr<br>ess-kivicare-cve-2022-0786-sqlipoc-yaml-<br>wordpress-cve-2022-1609-rcepoc-yaml-sola<br>rview-compact-cve-2022-29303-rcepoc-yaml<br>-wordpress-arprice-lite-cve-2022-0867-sq<br>lipoc-yaml-wordpress-fusion-cve-2022-138<br>6-ssrfpoc-yaml-wordpress-nirweb-cve-2022<br>-0781-sqlipoc-yaml-wordpress-metform-cve<br>-2022-1442-info-leakpoc-yaml-wordpress-m<br>apsvg-cve-2022-0592-sqlipoc-yaml-wordpre<br>ss-badgeos-cve-2022-0817-sqlipoc-yaml-wo<br>rdpress-daily-prayer-time-cve-2022-0785-<br>sqlipoc-yaml-wordpress-woo-product-table<br>-cve-2022-1020-rcepoc-yaml-wordpress-doc<br>umentor-cve-2022-0773-sqlipoc-yaml-wordp<br>ress-multiple-shipping-address-woocommer<br>ce-cve-2022-0783-sqlipoc-yaml-gitlab-cve<br>-2022-1162-hardcoded-passwordpoc-yaml-th<br>inkphp-cve-2022-25481-info-leakpoc-yaml-<br>wordpress-cve-2022-0591-ssrfpoc-yaml-wor<br>dpress-simple-link-directory-cve-2022-07<br>60-sqlipoc-yaml-wordpress-ti-woocommerce<br>-wishlist-cve-2022-0412-sqlipoc-yaml-wor<br>dpress-notificationx-cve-2022-0349-sqlip<br>oc-yaml-wordpress-page-views-count-cve-2<br>022-0434-sqlipoc-yaml-wordpress-masterst<br>udy-lms-cve-2022-0441-unauthpoc-yaml-wor<br>dpress-seo-cve-2021-25118-info-leakpoc-y<br>aml-wordpress-perfect-survey-cve-2021-24<br>762-sqlipoc-yaml-wordpress-asgaros-forum<br>-cve-2021-24827-sqlipoc-yaml-tcexam-cve-<br>2021-20114-info-leakpoc-yaml-wordpress-w<br>oocommerce-cve-2021-32789-sqlipoc-yaml-w<br>ordpress-profilepress-cve-2021-34621-una<br>uthpoc-yaml-wordpress-wp-statistics-cve-<br>2021-24340-sqlipoc-yaml-voipmonitor-cve-<br>2021-30461-rcepoc-yaml-rocket-chat-cve-2<br>021-22911-nosqlipoc-yaml-pega-infinity-c<br>ve-2021-27651-unauthpoc-yaml-wordpress-m<br>odern-events-calendar-lite-cve-2021-2414<br>6-info-leakpoc-yaml-afterlogic-webmail-c<br>ve-2021-26294-path-traversalpoc-yaml-wav<br>link-cve-2020-13117-rcepoc-yaml-prestash<br>op-cve-2021-3110-sqlipoc-yaml-cockpit-cv<br>e-2020-35847-nosqlipoc-yaml-cockpit-cve-<br>2020-35848-nosqlipoc-yaml-keycloak-cve-2<br>020-10770-ssrfpoc-yaml-prestashop-cve-20<br>20-26248-sqlipoc-yaml-wordpress-paypal-p<br>ro-cve-2020-14092-sqlipoc-yaml-microstra<br>tegy-cve-2020-11450-info-leakpoc-yaml-ad<br>obe-experience-manager-cve-2019-8086-xxe<br>poc-yaml-blogengine-net-cve-2019-10717-p<br>ath-traversalpoc-yaml-dotcms-cve-2018-17<br>422-url-redirectionpoc-yaml-php-proxy-cv<br>e-2018-19458-filereadpoc-yaml-circarlife<br>-scada-cve-2018-16671-info-leakpoc-yaml-<br>circarlife-scada-cve-2018-16670-info-lea<br>kpoc-yaml-circarlife-scada-cve-2018-1666<br>8-info-leakpoc-yaml-dotnetnuke-cve-2017-<br>0929-ssrfpoc-yaml-orchid-core-vms-cve-20<br>18-10956-path-traversalpoc-yaml-circarli<br>fe-scada-cve-2018-12634-info-leakpoc-yam<br>l-nuuo-nvrmini2-cve-2018-11523-uploadpoc<br>-yaml-jolokia-cve-2018-1000130-code-inje<br>ctionpoc-yaml-fiberhome-cve-2017-15647-p<br>ath-traversalpoc-yaml-opendreambox-cve-2<br>017-14135-rcepoc-yaml-sap-cve-2017-12637<br>-filereadpoc-yaml-glassfish-cve-2017-100<br>0029-lfipoc-yaml-boa-cve-2017-9833-filer<br>eadpoc-yaml-mantisbt-cve-2017-7615-unaut<br>hpoc-yaml-wordpress-cve-2017-5487-info-l<br>eakpoc-yaml-thinkcmf-cve-2018-19898-sqli|
|2023-01-09 07:30:10|[ExpToPocsuite3](https://github.com/smallfox233/ExpToPocsuite3)|v1.0||
## 近30天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
|2023-02-08 01:00:02|[NucleiTP](https://github.com/ExpLangcn/NucleiTP)|更新啦❤️|
|2023-02-07 23:33:18|[PocOrExp_in_Github](https://github.com/ycdxsb/PocOrExp_in_Github)|update 2023-02-08 07:33:18|
|2023-02-07 20:55:22|[faker](https://github.com/joke2k/faker)|Merge branch 'kity-linuxero-master'|
|2023-02-07 16:11:56|[dbeaver](https://github.com/dbeaver/dbeaver)|#18751 Respect URL-based configuration (#18981)|
|2023-02-07 06:16:20|[OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL)|Update 泛微OA_v10_upload.py|
|2023-02-06 21:19:35|[RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)|replace logger.info with logger.error on some error me<br>ssages|
|2023-02-06 13:13:40|[poc-hub](https://github.com/ybdt/poc-hub)|整理|
|2023-02-06 09:20:28|[ffuf](https://github.com/ffuf/ffuf)|Fix the v2 tagging for go install (#639)|
|2023-02-06 07:07:53|[vulnerability](https://github.com/lal0ne/vulnerability)|CVE-2022-47966|
|2023-02-06 03:12:09|[404StarLink](https://github.com/knownsec/404StarLink)|weekly update at 2023-02-06|
|2023-02-06 01:53:21|[Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki)|更新漏洞|
|2023-02-06 01:44:57|[Vulhub-Reproduce](https://github.com/Threekiii/Vulhub-Reproduce)|更新漏洞|
|2023-02-05 11:24:30|[SmsForwarder](https://github.com/pppscn/SmsForwarder)|修复：通道测试闪退|
|2023-02-05 07:11:23|[RouteVulScan](https://github.com/F6JO/RouteVulScan)|Update Config_yaml.yaml|
|2023-02-04 15:13:48|[afrog](https://github.com/zan8in/afrog)|update mod|
|2023-02-04 08:56:24|[URLFinder](https://github.com/pingc0y/URLFinder)|Delete URLFinder-linux-amd64|
|2023-02-03 16:09:26|[qsnctf-python](https://github.com/Moxin1044/qsnctf-python)|fix api.py 421|
|2023-02-03 10:10:16|[passive-scan-client](https://github.com/c0ny1/passive-scan-client)|恢复默认端口和整理代码符合低版本语法糖|
|2023-02-03 05:08:20|[captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified)|Update FAQ.md|
|2023-02-02 08:46:07|[RedisEXP](https://github.com/yuyan-sec/RedisEXP)|update|
|2023-02-02 06:50:04|[mitaka](https://github.com/ninoseki/mitaka)|Merge pull request #694 from ninoseki/renovate/typescr<br>ipt-eslint-monorepochore(deps): update typescript-eslin<br>t monorepo to v5.44.0|
|2023-02-02 02:36:25|[JDumpSpider](https://github.com/whwlsfb/JDumpSpider)|add SpringSecurityUsernamePasswordAuthenticationToken <br>spider.|
|2023-02-01 17:54:42|[dirsearch](https://github.com/maurosoria/dirsearch)|Merge pull request #1275 from AkshayraviC09YC47/patch-<br>3Update CONTRIBUTORS.md|
|2023-02-01 12:26:23|[RequestTemplate](https://github.com/1n7erface/RequestTemplate)|Update README.md|
|2023-02-01 01:39:12|[CRC32-Tools](https://github.com/AabyssZG/CRC32-Tools)|Update README.md|
|2023-01-30 07:49:55|[super-xray](https://github.com/4ra1n/super-xray)|#142|
|2023-01-26 05:21:12|[CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools)|Update README.md|
|2023-01-24 18:01:28|[nuclei](https://github.com/projectdiscovery/nuclei)|Merge pull request #3239 from projectdiscovery/devnucl<br>ei v2.8.8|
|2023-01-18 08:16:24|[Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam)|更新README.md|
|2023-01-17 09:41:54|[Packer-Fuzzer](https://github.com/rtcatc/Packer-Fuzzer)|v1.4.15 更新demo图片|
|2023-01-17 06:40:28|[Some-PoC-oR-ExP](https://github.com/coffeehb/Some-PoC-oR-ExP)|Create CVE-2019-16097.md|
|2023-01-17 05:49:54|[gospider](https://github.com/jaeles-project/gospider)|Merge pull request #59 from aidanhall34/dockerfileCrea<br>ted dockerfile and updated README.md|
|2023-01-17 03:03:16|[CN_Nessus_Plugins_I<br>nterface](https://github.com/nszy007/CN_Nessus_Plugins_Interface)|20230113|
|2023-01-16 10:59:37|[Scanners-Box](https://github.com/We5ter/Scanners-Box)|[+]kvesta/vesta|
|2023-01-13 11:53:18|[feroxbuster](https://github.com/epi052/feroxbuster)|Update README.md|
|2023-01-12 02:31:07|[OneForAll](https://github.com/shmilylty/OneForAll)|Update docker-image.yml拼写错误|
|2023-01-11 09:43:37|[InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll)|Update README.md|
|2023-01-10 10:59:45|[http-request-smuggl<br>er](https://github.com/portswigger/http-request-smuggler)|Merge pull request #58 from Hannah-PortSwigger/masterU<br>pdate case statement to state technique.|
|2023-01-10 07:34:19|[NessusToReport](https://github.com/Hypdncy/NessusToReport)|增加tenable.py|
|2023-01-09 07:27:17|[ExpToPocsuite3](https://github.com/smallfox233/ExpToPocsuite3)|Update README.md|## 所有项目
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
| [URLFinder](https://github.com/pingc0y/URLFinder) | 2023.2.3 | 类似JSFinder的golang实现，一款用于快速提取检测页面中JS与URL的工<br>具，更快更全更舒服 |
| [feroxbuster](https://github.com/epi052/feroxbuster) | v2.7.3 | A fast, simple, recursive content discovery tool written in Rust<br>. |
| [ffuf](https://github.com/ffuf/ffuf) | v2.0.0 | Fast web fuzzer written in Go |
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
| [railgun](https://github.com/lz520520/railgun) | v1.5.2 |  |
| [Goby](https://github.com/gobysec/Goby) | Beta2.2.0 | Attack surface mapping |
#### 半自动漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EasyPen](https://github.com/lijiejie/EasyPen) |  | EasyPen is a GUI program which helps pentesters do target discov<br>ery, vulnerability scan and exploitation |
| [xray](https://github.com/chaitin/xray) | 1.9.4 | 一款完善的安全评估工具，支持常见 web 安全问题扫描和自定义 poc | <br>使用之前务必先阅读文档 |
| [w13scan](https://github.com/w-digital-scanner/w13scan) |  | Passive Security Scanner (被动式安全扫描器) |
| [Fvuln](https://github.com/d3ckx1/Fvuln) | Fvuln_v1.<br>4.8 | F-vuln（全称：Find-Vulnerability）是为了自己工作方便专门编写的一<br>款自动化工具，主要适用于日常安全服务、渗透测试人员和RedTeam红队人<br>员，它集合的功能包括：存活IP探测、开放端口探测、web服务探测、web漏<br>洞扫描、smb爆破、ssh爆破、ftp爆破、mssql爆破等其他数据库爆破工作以<br>及大量web漏洞检测模块。 |
| [nuclei](https://github.com/projectdiscovery/nuclei) | v2.8.8 | Fast and customizable vulnerability scanner based on simple YAML<br> based DSL. |
| [afrog](https://github.com/zan8in/afrog) | v2.2.1 | A Vulnerability Scanning Tools For Penetration Testing |
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
| [RequestTemplate](https://github.com/1n7erface/RequestTemplate) | v1.1.1 | 双语双端内网扫描以及验证工具 |
#### Shell管理
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Behinder](https://github.com/rebeyond/Behinder) | Behinder_<br>v4.0.6 | “冰蝎”动态二进制加密网站管理客户端 |
| [Godzilla](https://github.com/BeichenDream/Godzilla) | v4.0.1-go<br>dzilla | 哥斯拉 |
#### 中间件&框架漏洞利用
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
| [OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL) | OA-EXPTOO<br>L-v0.7 | OA综合利用工具，集合将近20款OA漏洞批量扫描 |
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
| [Apt_t00ls](https://github.com/White-hua/Apt_t00ls) | v0.5 | 高危漏洞利用工具 |
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
| [poc-hub](https://github.com/ybdt/poc-hub) |  | 漏洞复现、漏洞检测、漏洞利用 |
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
#### 代理池
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [go_proxy_pool](https://github.com/pingc0y/go_proxy_pool) |  | 无环境依赖开箱即用的代理IP池 |
| [rotateproxy](https://github.com/akkuman/rotateproxy) | v0.7.1 | 利用fofa搜索socks5开放代理进行代理池轮切的工具 |
### 工具&插件
#### Burpsuite
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [PowerScanner](https://github.com/NeoTheCapt/PowerScanner) | 1.1.3 | 面向HW的红队半自动扫描器 |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | RouteVulS<br>can1.4 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的bu<br>rp插件 |
| [SpringScan](https://github.com/metaStor/SpringScan) | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [BurpSuite-collectio<br>ns](https://github.com/Mr-xn/BurpSuite-collections) |  | 有关burpsuite的插件(非商店),文章以及使用技巧的收集(此项目不再提<br>供burpsuite破解文件,如需要请在博客mrxn.net下载)---Collection of bu<br>rpsuite plugins (non-stores), articles and tips for using Burpsui<br>te, no crack version file |
| [BurpShiroPassiveSca<br>n](https://github.com/pmiaowu/BurpShiroPassiveScan) | BurpShiro<br>PassiveSca<br>n-2.0.0 | 一款基于BurpSuite的被动式shiro检测插件 |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | BurpFastJ<br>sonScan-2.<br>2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [HaE](https://github.com/gh0stkey/HaE) | 2.4.5 | HaE - Highlighter and Extractor, 赋能白帽 高效作战 |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9-alph<br>a | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集；<br>快速Title获取；外部工具联动；等等 |
| [Sylas](https://github.com/Acmesec/Sylas) | 1.1.1 | 新一代子域名主/被动收集工具 - Subdomain automatic/passive collec<br>tion tool |
| [GadgetProbe](https://github.com/BishopFox/GadgetProbe) | v1.0 | Probe endpoints consuming Java serialized objects to identify cl<br>asses, libraries, and library versions on remote Java classpaths. |
| [HopLa](https://github.com/synacktiv/HopLa) | 1.2 |  HopLa Burp Suite Extender plugin -Adds autocompletion support a<br>nd useful payloads in Burp Suite |
| [captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified) | 0.21 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免费<br>ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, sup<br>port AES/RSA/DES/ExecJs(execute JS encryption code in burpsuite).<br> 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSuite插<br>件 |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.20 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等）<br>，类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础上，<br>不影响APP、网站加解密正常逻辑等。 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [AutoRepeater](https://github.com/nccgroup/AutoRepeater) |  | Automated HTTP Request Repeating With Burp Suite |
| [http-request-smuggl<br>er](https://github.com/portswigger/http-request-smuggler) |  |  |
| [burp-requests](https://github.com/silentsignal/burp-requests) | v0.2.4 | Copy as requests plugin for Burp Suite |
| [CORSScanner](https://github.com/zzzskd/CORSScanner) |  | CORS 跨域漏洞 burp 插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) | v1.0.0 | fastjson利用，支持tomcat、spring回显，哥斯拉内存马；回显利用链为<br>dhcp、ibatis、c3p0。 |
| [HostHeaderAttack](https://github.com/weujieytt/HostHeaderAttack) | 0.1 | 检测host头攻击的Burpsuite被动扫描插件，Burpsuite passive scannin<br>g plugin responsible for detecting host header attack |
| [knife](https://github.com/bit4woo/knife) | v2.1 | A burp extension that add some useful function toContext Menu 添<br>加一些右键菜单让burp用起来更顺畅 |
| [log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner) | 0.21.0 | CVE-2021-44228 Log4j2 BurpSuite Scanner,Customize ceye.io api or<br> other apis,including internal networks |
| [passive-scan-client](https://github.com/c0ny1/passive-scan-client) | 0.3.1 | Burp被动扫描流量转发插件 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpSuiteCn](https://github.com/funkyoummp/BurpSuiteCn) | V2.0 | Burp Suite汉化 中文 |
#### xray
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [yarx](https://github.com/zema1/yarx) | v0.2.0 | An awesome reverse engine for xray poc. | 一个自动化根据 xray po<br>c 生成对应 server 的工具 |
| [xray-poc-generation](https://github.com/phith0n/xray-poc-generation) |  | 🧬 辅助生成 XRay YAML POC |
| [super-xray](https://github.com/4ra1n/super-xray) | 1.4 | Web漏洞扫描工具XRAY的GUI启动器 (Web Vulnerability Scanner GUI St<br>arter) |
#### pocsuite3
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ExpToPocsuite3](https://github.com/smallfox233/ExpToPocsuite3) | v1.0 | goby exp批量转换为pocsuite3 exp脚本 |
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
| [nucleix](https://github.com/mlq574/nucleix) |  | 整合nuclei与xray(社区版、自带高级版)，实现被动扫描+poc扫描自动化<br>渗透流程 |
#### nessus
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [NessusToReport](https://github.com/Hypdncy/NessusToReport) | v1.1.1 | Nessus扫描报告自动化生成工具 |
| [NessusReportInChine<br>se](https://github.com/FunnyKun/NessusReportInChinese) |  | 半自动化将 Nessus 英文报告（csv格式）生成中文 excel ，中文漏洞库<br>已有700多条常见漏洞，后续再进一步加上新漏洞自动翻译，实现全自动化 |
| [CN_Nessus_Plugins_I<br>nterface](https://github.com/nszy007/CN_Nessus_Plugins_Interface) | 1 | nessus插件中文查询接口 |
| [docker_nessus_unlim<br>ited](https://github.com/xxcdd/docker_nessus_unlimited) |  | docker build nessus with unlimited ip |
| [nessus_api](https://github.com/starnightcyber/nessus_api) |  | Nessus REST API 封装 |
#### rsas
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [nsfocus-rsas-knowle<br>dge-base](https://github.com/biggerwing/nsfocus-rsas-knowledge-base) |  | 绿盟科技漏洞扫描器(RSAS)漏洞库 |
| [RSAS-Data-Export](https://github.com/autoing/RSAS-Data-Export) | 2022-9-9 | 绿盟极光远程安全评估系统(RSAS)-RSAS漏洞数据导出工具 |
| [RSAS-Task-Release](https://github.com/autoing/RSAS-Task-Release) | v1.0 | 绿盟极光远程安全评估系统(RSAS)-RSAS批量下任务工具 |
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
| [CyberChef](https://github.com/gchq/CyberChef) | v9.55.0 | The Cyber Swiss Army Knife - a web app for encryption, encoding,<br> compression and data analysis |
#### 取证分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pyvmx-cracker](https://github.com/axcheron/pyvmx-cracker) |  | Simple tool to crack VMware VMX encryption passwords |
| [chatViewTool](https://github.com/Ormicron/chatViewTool) | BEAT | 基于Java实现的图形化微信聊天记录解密查看器 |
| [Sharp-dumpkey](https://github.com/Ormicron/Sharp-dumpkey) | 1 | 基于C#实现的获取微信数据库密钥的小工具 |
| [Sunflower_get_Passw<br>ord](https://github.com/wafinfo/Sunflower_get_Password) |  | 一款针对向日葵的识别码和验证码提取工具 |
| [SharpWxDump](https://github.com/AdminTest0/SharpWxDump) |  | 微信客户端取证，可获取用户个人信息(昵称/账号/手机/邮箱/数据库密<br>钥(用来解密聊天记录))；支持获取多用户信息，不定期更新新版本偏移，<br>目前支持所有新版本、正式版本 |
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
#### 工具集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools) |  | 渊龙Sec安全团队CTF&AWD工具箱 |
| [qsnctf-python](https://github.com/Moxin1044/qsnctf-python) |  | 青少年CTF的Python包，方便大家调用一些CTF常用功能。 |
| [CTF-Tools](https://github.com/qianxiao996/CTF-Tools) | v1.3.7 | 一款Python+Pyqt写的CTF编码、解码、加密、解密工具。 |
### CTF逆向
#### pyc逆向
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegosaurus](https://github.com/AngelKitty/stegosaurus) | 1.0 | A steganography tool for embedding payloads within Python byteco<br>de. |
#### Java反编译
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [JavaDecompileTool-G<br>UI](https://github.com/MountCloud/JavaDecompileTool-GUI) | V1.2 | Java Decompile Tool GUI-JAVA反编译工具（界面版） |
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
| [faker](https://github.com/joke2k/faker) | v16.7.0 | Faker is a Python package that generates fake data for you. |
| [SmsForwarder](https://github.com/pppscn/SmsForwarder) | v3.1.1 | 短信转发器——监控Android手机短信、来电、APP通知，并根据指定规则<br>转发到其他手机：钉钉群自定义机器人、钉钉企业内机器人、企业微信群机<br>器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram<br>机器人、Server酱、PushPlus、手机短信等。包括主动控制服务端与客户端<br>，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。（V3.0 新<br>增）PS.这个APK主要是学习与自用，如有BUG请提ISSUE，同时欢迎大家提PR<br>指正 |
| [dbeaver](https://github.com/dbeaver/dbeaver) | 22.3.4 | Free universal database tool and SQL client |
### 安全产品
#### 威胁检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmEye](https://github.com/RoomaSec/RmEye) | v0.0.4 | 戎码之眼是一个window上的基于att&ck模型的威胁监控工具.有效检测常<br>见的未知威胁与已知威胁.防守方的利剑 |
### 应急工具
#### 后门查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmTools](https://github.com/RoomaSec/RmTools) |  | 蓝队应急工具 |
