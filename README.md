# 更新于 2023-07-10 08:53:54

## 近15天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
|2023-07-09 16:23:13|[dbeaver](https://github.com/dbeaver/dbeaver)|23.1.2|                 - SQL editor:       <br>              - Mouse hovering over ed<br>itor annotations was fixed            <br>         - Trailing DDL query delimite<br>r processing was fixed                <br> - Data editor:                     - <br>References panel refresh was fixed    <br>                 - XML presentation wa<br>s fixed (NULL value handler)          <br>       - General UI:                  <br>   - Settings reset UI and behavior we<br>re redesigned                     - Ed<br>itor tab tooltip now contains informat<br>ion abut resource's project           <br>          - CLI parameter for app vers<br>ion print was added                   <br>  - Objects with mixed case names cach<br>ing was fixed                     - Is<br>sue with program launch with wrong Jav<br>a version was fixed                   <br>  - Preferences export/import UI was i<br>mproved                     - Maven sn<br>apshot repository was added to default<br> configuration                 - Conne<br>ctions: kerberos support in legacy JDB<br>C drivers (Hive) was fixed            <br>     - Data transfer: table informatio<br>n for tasks with broken connection was<br> fixed                 - Databases:   <br>                  - BigQuery: driver v<br>ersion was upgraded to 1.3.3 (thanks t<br>o @fredlegaucher)                     <br>- DuckDB: LIST data type support was a<br>dded                     - Firebird: f<br>ilters and sorting in grouping panel w<br>ere fixed                     - IBM i:<br> driver download was fixed            <br>         - Oracle:                    <br>     - Partitions cache refresh was fi<br>xed                         - Stored p<br>rocedures edit/save was fixed         <br>            - PostgreSQL: enum columns<br> alter was fixed                     -<br> Snowflake:                         - <br>Client application name set was fixed <br>                        - Quoted ident<br>ifiers auto-completion was fixed      <br>           - Misc: internal app contro<br>ller server now uses HTTP instead of R<br>MI             |
|2023-07-09 09:39:37|[Viper](https://github.com/FunnyWolf/Viper)|v1.6.1|## v1.6.1 20230709  ### 优化  - 合并m<br>etasploit-framework 6.3.25版本  ### Bu<br>gfix  - 修复NAT网络Linux主机(各大云厂<br>商VPS)IP显示为::1问题  - 修复NAT网络Lin<br>ux主机(各大云厂商VPS)上线生成多个主机<br>问题|
|2023-07-09 09:23:08|[OneScan](https://github.com/vaycore/OneScan)|v1.1.0|  1.1.0 版本发布，版本更新内容如下   <br> ### 新增    - 新增停止扫描任务功能（<br>停止正在扫描的所有任务）  - 新增导入 Ur<br>l 功能（需要导入完整 Url 链接）  - 数<br>据看板列表新增请求包来源 From 字段（方<br>便过滤）  - 数据看板列表新增 “获取body<br>Md5值”、“获取bodyHash值” 菜单项（更<br>方便师傅们添加指纹规则）  - 指纹模块新<br>增 bodyHash 数据源（与 Fofa 的 icon_has<br>h 计算方式一样）  |
|2023-07-09 05:05:02|[ENScan_GO](https://github.com/wgpsec/ENScan_GO)|0.0.13|- 修复天X查BUG （需要设置代理挂上burp<br>参考 #66）   > -n 小米 -type tyc --debu<br>g --proxy http://127.0.0.1:8080/|
|2023-07-07 18:15:00|[Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension)|v1.7.1|* Fixed issue where some requests are<br> not being intercepted|
|2023-07-07 16:00:38|[faker](https://github.com/joke2k/faker)|v18.13.<br>0|See .|
|2023-07-07 09:40:41|[trivy](https://github.com/aquasecurity/trivy)|v0.43.1|## Changelog * 5d76abadc chore(deps):<br> Update defsec to v0.90.3 (#4793) * fe<br>d446c51 chore(deps): bump google.golan<br>g.org/protobuf from 1.30.0 to 1.31.0 (<br>#4752) * df62927e5 chore(deps): bump a<br>lpine from 3.18.0 to 3.18.2 (#4748) * <br>1b9b9a84f chore(deps): bump github.com<br>/alicebob/miniredis/v2 from 2.30.3 to <br>2.30.4 (#4758) * 3c16ca821 docs(image)<br>: fix the comment on the soft/hard lin<br>k (#4740) * e5bee5ccc check Type when <br>filling pkgs in vulns (#4776) * 4b9f31<br>0b9 feat: add support of linux/ppc64le<br> and linux/s390x architectures for Ins<br>tall.sh script (#4770) * 8e7fb7cc8 cho<br>re(deps): bump modernc.org/sqlite from<br> 1.20.3 to 1.23.1 (#4756) * a9badeaba <br>fix(rocky): add architectures support <br>for advisories (#4691) * f8ebccc68 cho<br>re(deps): bump github.com/opencontaine<br>rs/image-spec (#4751) * 1c81948e0 chor<br>e(deps): bump github.com/package-url/p<br>ackageurl-go (#4754) * 497cc10d8 chore<br>(deps): bump golang.org/x/sync from 0.<br>2.0 to 0.3.0 (#4750) * 065f0afa5 chore<br>(deps): bump github.com/tetratelabs/wa<br>zero from 1.2.0 to 1.2.1 (#4755) * e26<br>03056d chore(deps): bump github.com/te<br>stcontainers/testcontainers-go (#4759)<br> * 0621402bf fix: documentation about <br>reseting trivy image (#4733) * 798fdbc<br>01 fix(suse): Add openSUSE Leap 15.5 e<br>ol date as well (#4744) * 34a89293d fi<br>x: update Amazon Linux 1 EOL (#4761)  |
|2023-07-07 05:40:12|[safeline](https://github.com/chaitin/safeline)|v2.1.2|- 修复了日志详情中防护策略模块没有翻<br>译的问题|
|2023-07-06 15:50:09|[WeblogicTool](https://github.com/KimJun1010/WeblogicTool)|v1.2|更新记录  - 新增批量探测T3、IIOP、web<br>接口功能  - 修复多个bug|
|2023-07-06 15:21:10|[autoDecoder](https://github.com/f0ng/autoDecoder)|0.30|## 2023.7.6 更新0.30  1. Repeater、In<br>truder模块中，增加右键加密、解密，当设<br>置好相应的方法后可以对请求体的body进行<br>加密、解密        2. #16 修复Send to Re<br>peater、Send to Intruder不会带上端口号<br>的问题，感谢@P1a0z1 反馈|
|2023-07-06 12:31:30|[afrog](https://github.com/zan8in/afrog)|v2.7.1|● Add anti-link platform survival de<br>tection function  ● Add extractor fun<br>ctionality to extract sensitive inform<br>ation such as version numbers  ● Dele<br>te PoC: CNVD-2021-15824、t-soft-e-comm<br>erce4-urunadi-stored-xss、clicshopping<br>-v2-xss    ● 新增反链平台存活检测功能<br>  ● 新增提取器 extractors 功能，可提<br>取版本号等敏感信息  ● 删除 PoC ： CNVD<br>-2021-15824、t-soft-e-commerce4-urunad<br>i-stored-xss、clicshopping-v2-xss|
|2023-07-06 11:10:32|[Elkeid](https://github.com/bytedance/Elkeid)|rasp-v2<br>.2.0.6||
|2023-07-06 05:43:13|[neuvector](https://github.com/neuvector/neuvector)|v5.2.0|##### Enhancements   + Searchable Saa<br>S service for CVE lookups. NVSHAS-5852<br> Search the latest NeuVector CVE datab<br>ase to see if a specific CVE exists in<br> the database.  + Support tokens for N<br>euVector API access. NVSHAS-6293  + Su<br>pport AWS Marketplace PAYG billing for<br> NeuVector monthly support subscriptio<br>ns. Users can subscribe to NeuVector b<br>y SUSE support, billed monthly to thei<br>r AWS account based on previous month'<br>s average node count usage. Details . <br> + Support image signing for admission<br> controls. NVSHAS-6217, NVSHAS-6216.  <br>+ Enable each admission control rule t<br>o have its own mode of Monitor or Prot<br>ect.NVSHAS-4062 A Deny action in Monit<br>or mode will alert, and a Deny action <br>in Protect mode will block. Allow acti<br>ons are unaffected.  + Add a new "oper<br>ator" in Policy > Admission Control > <br>Add Rule. NVSHAS-6726 Support operator<br>s "is between" and "is not between" fo<br>r both "Users" and "User Groups".  + A<br>dd support for custom admission contro<br>l criteria such as resource limits. NV<br>SHAS-7717  + Support invoking NeuVecto<br>r scanner from Harbor registries throu<br>gh the  interface.  + Allow user to di<br>sable network protection but keep WAF/<br>DLP functioning. Configure Network Pol<br>icy Enablement in Settings -> Configur<br>ation. NVSHAS-7725  + Use less privile<br>ged services accounts as required for <br>each NeuVector component. NVSHAS-7603.<br> A variable “leastPrivilege” is intr<br>oduced. The default is false. NOTE: Us<br>ing the current helm chart with this v<br>ariable on a release prior to 5.2.0 wi<br>ll not function properly.  + Bind to n<br>on-default service account to meet CIS<br> 1.5 5.1.5 recommendation. NVSHAS-7619<br>  + Enable administrator to configure <br>user default Session Time out. NVSHAS-<br>7621  + Customizable login banner NVSH<br>AS-6675.   + Customizable UI header te<br>xt NVSHAS-7330.  + SYSLOG support for <br>TLS encrypted transport. NVSHAS-4377  <br>+ Enable deployment of the NeuVector m<br>onitor helm chart from Rancher Manager<br>.  + Remove upper limit for top level <br>domain in URL validator for registry s<br>canning. NVSHAS-7935  + Scan golang de<br>pendencies, including run-time scans. <br> + Support Debian 12 (Bookworm) vulner<br>ability scan.  + Add CSV export for Re<br>gistry / Details to export CVEs for al<br>l images in configured registry. NVSHA<br>S-5993  + Allow NeuVector to set sever<br>al ADFS certificates in parallel in x.<br>509 certificate field. NVSHAS-7335  + <br>Add and display the comment field for <br>Response Rules.  ##### Bug Fixes  + Re<br>duce repeating logs in enforcer/contro<br>ller logs. NVSHAS-7832 {TBD???}  + Mul<br>tiple clusters page does not render. N<br>VSHAS-7742  + Empty group auto-removal<br> takes 2 hours to delete instead of 1 <br>hour according to schedule. NVSHAS-779<br>1  + Manually allowed network rule not<br> getting applied and resulting in viol<br>ation for pause image. NVSHAS-7807  + <br>Blocking SSL connections even if a net<br>work rule permits the traffic under ce<br>rtain initial conditions. NVSHAS-7923 <br> + Security events warning even with a<br>llowed network rules due to policy upd<br>ate issue in synchronization. NVSHAS-8<br>019  + Despite defining the network ru<br>les, violations getting logged under s<br>ecurity events (false positives) when <br>the container has stopped due to out o<br>f memory (OOM) error. NVSHAS-7830  + A<br>llow user to disable/enable detection <br>and protection against unmanaged conta<br>iner in cluster. NVSHAS-7804. This can<br> be set through the Manager CLI:    se<br>t system detect_unmanaged_wl status -h<br>  Usage: cli set system detect_unmanag<br>ed_wl status [OPTIONS] {true|false}   <br> Enable/disable detect unmanaged conta<br>iner    ##### Other  + Add "leastPrivi<br>lege" setting in Helm chart.  + Enable<br> AWS integration settings in Helm char<br>t. |
|2023-07-04 06:58:05|[veinmind-tools](https://github.com/chaitin/veinmind-tools)|v2.1.4|## 🔥 Feature  * feat(plugins): Add v<br>einmind-privilege-escalation plugin fo<br>r detecting privilege escalation risks<br>, including checks for suid and sudo  <br>by @ek1ng in https://github.com/chaiti<br>n/veinmind-tools/pull/250    ## 🔧 Fix<br>  * fix(libveinmind): fix libveinmind <br>walk data race error by @DVKunion in h<br>ttps://github.com/chaitin/veinmind-too<br>ls/pull/231  * fix(veinmind-weakpass)/<br>add_error_check by  @testwill in https<br>://github.com/chaitin/veinmind-tools/p<br>ull/249  * fix(docs): fix errors in do<br>cumentation on how to initialize plugi<br>ns by @ek1ng in https://github.com/cha<br>itin/veinmind-tools/pull/247  * fix(do<br>cs): fix README format by @ek1ng in ht<br>tps://github.com/chaitin/veinmind-tool<br>s/pull/251    ## 📒 Others  * chore(li<br>bveinmind): update libveinmind 1.9.21 <br>by @DVKunion in https://github.com/cha<br>itin/veinmind-tools/pull/243  * chore(<br>ci):  add auto sync to registry by @DV<br>Kunion  in https://github.com/chaitin/<br>veinmind-tools/pull/254      **Full Ch<br>angelog**: https://github.com/chaitin/<br>veinmind-tools/compare/v2.1.3...v2.1.4|
|2023-07-03 16:16:47|[RedisEXP](https://github.com/yuyan-sec/RedisEXP)|0.0.2|github actions 自动编译|
|2023-07-03 14:41:37|[nuclei](https://github.com/projectdiscovery/nuclei)|v2.9.8|    ## What's Changed  ### 🐞 Bugs  *<br> **Fixed issue to preserve the order o<br>f query parameters** by @tarunKoyalwar<br> in https://github.com/projectdiscover<br>y/nuclei/pull/3887  * Fixed with netwo<br>rk connection read and write deadline <br>by @praetorian-thendrickson in https:/<br>/github.com/projectdiscovery/nuclei/pu<br>ll/3845  * Fixed issue with showing mu<br>ltiple matches per template with -ms o<br>ption by @RamanaReddy0M in https://git<br>hub.com/projectdiscovery/nuclei/pull/3<br>770    ## New Contributors  * @praetor<br>ian-thendrickson made their first cont<br>ribution in https://github.com/project<br>discovery/nuclei/pull/3845    **Full C<br>hangelog**: https://github.com/project<br>discovery/nuclei/compare/v2.9.7...v2.9<br>.8|
|2023-07-03 11:35:40|[ghauri](https://github.com/r0oth3x49/ghauri)|1.2.2|# Fixes   - fixed issue with regex pr<br>ocessing multipart/form-data|
|2023-07-02 10:36:57|[captcha-killer-mo<br>dified](https://github.com/f0ng/captcha-killer-modified)|0.24.1|【2023-7-2】 0.24.1  - #27 修复加载插<br>件影响intruder速度的问题(临时增加了一个<br>按钮控制是否开启该插件)      |
|2023-07-02 06:47:07|[ShiroAttack2](https://github.com/SummerSec/ShiroAttack2)|4.7.0|https://github.com/SummerSec/ShiroAtt<br>ack2/issues/45 thanks @y4tacker |
|2023-07-02 04:28:53|[PEASS-ng](https://github.com/carlospolop/PEASS-ng)|2023070<br>2-bc7ce3<br>ac||
|2023-07-01 05:29:18|[NextScan](https://github.com/tongcheng-security-team/NextScan)|v1.2.0|##### v1.2.0发布    ## Changelog    -<br>  perf 🚀 : yaml模版格式更新  -  perf <br>🚀 : 漏洞详情页面优化  -  perf 🚀 : 任<br>务查询功能优化  -  fix🐛: 修复爬虫运行<br>时错误  - fix:🐛 任务运行异常问题若干  <br>  |
|2023-06-30 16:49:10|[cf](https://github.com/teamssix/cf)|v0.5.0|### 新增功能    *  新增阿里云用户数据<br>后门功能  *  新增阿里云镜像共享功能  * <br> 新增阿里云接管控制台时自动创建 AK 功<br>能  *  新增阿里云 RDS 列出详细信息功能 <br> *  新增阿里云 RDS 添加账号功能  *  新<br>增阿里云 RDS 创建公网访问地址的功能  * <br> 新增阿里云 RDS 添加白名单的功能  *   <br>新增查询 AK 所属云厂商功能   *  新增支<br>持 brew 安装    ### 功能优化    *  优化<br>配置功能，现在能自动识别配置是否处于可<br>用状态  *  优化实例公网 IP 展示，不存在<br>时会展示为空  *  优化 OSS 下载功能，现<br>在默认会下载所有文件  *  优化更新处理逻<br>辑  *  优化华为云 OBS 列出功能    ### B<br>ug 修复    *  修复批量执行命令时，没有<br>安装云助手导致批量执行中断的 Bug  *  修<br>复 OSS 下载文件无法自动创建目录的 Bug  <br>  ## 新贡献者  * @shadowabi made their<br> first contribution in https://github.<br>com/teamssix/cf/pull/227    **Full Cha<br>ngelog**: https://github.com/teamssix/<br>cf/compare/v0.4.5...v0.5.0|
|2023-06-30 15:53:31|[grype](https://github.com/anchore/grype)|v0.63.1|# Changelog  ##  (2023-06-30)    ### <br>Bug Fixes  - Add more log4j-adjacent p<br>ackage ignore rules ] ] - The summary <br>by severity is confusing ] ] ]    |
|2023-06-29 17:24:30|[syft](https://github.com/anchore/syft)|v0.84.1|# Changelog    ##  (2023-06-29)      <br>  ### Bug Fixes    - Fix version detec<br>tion in Java archive name parsing ] ] <br> - Improve support for Dart SDK packag<br>e dependency lockfiles ] ]  - Fix lice<br>nse output for some CycloneDX JSON SBO<br>Ms ] ] ]  - Correctly discover Debian <br>file relationships in distroless image<br>s ] ] ]    ### Additional Changes    -<br> Simplify the SBOM writer interface ] <br>]        |
|2023-06-28 09:28:17|[Exp-Tools](https://github.com/cseroad/Exp-Tools)|v1.2.0|- 新增用友畅捷通T+SQL注入  - 新增致远<br>帆软报表文件读取-bypass  - 新增泛微eoff<br>ice uploadify上传  - 新增php-framework<br>和java-framework  - 新增nacos任意用户添<br>加  - 新增金蝶云星空反序列化  - 优化部<br>分代码|
|2023-06-27 13:43:22|[fofa_viewer](https://github.com/wgpsec/fofa_viewer)|1.1.13|fix-bug:  1. 解决添加规则的报错问题  <br>optimize :  1. 考虑到有师傅会把jar包打<br>包成app，因此将日志路径修改为用户目录下|
|2023-06-27 08:57:25|[mitaka](https://github.com/ninoseki/mitaka)|v1.3.0|-  Add Add Coalition searcher (#737) <br>     - https://ess.coalitioninc.com/ |
|2023-06-27 03:53:11|[AsamF](https://github.com/Kento-Sec/AsamF)|v0.2.4|1. 修复了fofa type接口问题。目前根据f<br>ofa政策，高级会员无法使用该接口。    2<br>. 修复了0zone读取apikey的问题。|
|2023-06-26 02:21:06|[Dirscan](https://github.com/corunb/Dirscan)|v1.5.1|[+] 新增反向递归扫描：-Ar    [!] 增加<br>探存活开关：-Cs(默认是开的)    |
## 近15天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
|2023-07-10 00:45:19|[NucleiTP](https://github.com/ExpLangcn/NucleiTP)|更新啦❤️|
|2023-07-10 00:00:02|[free](https://github.com/freefq/free)|updated_at 07-10 08:00|
|2023-07-09 20:22:51|[PocOrExp_in_Githu<br>b](https://github.com/ycdxsb/PocOrExp_in_Github)|update 2023-07-10 04:22:51|
|2023-07-09 13:29:16|[X-Marshal](https://github.com/XTeam-Wing/X-Marshal)|Update README.md|
|2023-07-09 12:39:45|[v2rayfree](https://github.com/aiboboxx/v2rayfree)|update|
|2023-07-09 09:38:47|[Viper](https://github.com/FunnyWolf/Viper)|update version v1.6.1|
|2023-07-09 09:19:10|[OneScan](https://github.com/vaycore/OneScan)|更新README.md中的一些说明和截图|
|2023-07-09 05:23:19|[ENScan_GO](https://github.com/wgpsec/ENScan_GO)|修改文档补充说明 fix #65|
|2023-07-09 03:53:12|[afrog](https://github.com/zan8in/afrog)|update|
|2023-07-08 18:09:34|[vulhub](https://github.com/vulhub/vulhub)|Merge pull request #449 from al4n233/patch-1  fixed<br> a typo|
|2023-07-08 12:39:32|[ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)|Merge pull request #34 from VMCoud/patch-1  Create <br>docker.yml|
|2023-07-07 21:01:05|[clair](https://github.com/quay/clair)|docs: Add description of debugging services availab<br>le during local-dev  As pyroscope was added I realiz<br>ed that these services are not documented but could <br>be really useful to contributors.  Signed-off-by: cr<br>ozzy |
|2023-07-07 20:43:54|[neuvector](https://github.com/neuvector/neuvector)|Merge pull request #887 from kyledong-suse/main  NV<br>SHAS-5703 & NVSHAS-5365: Implement IP-FQDN mapping t<br>able|
|2023-07-07 18:08:49|[Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension)|bug in way interceptors work|
|2023-07-07 15:59:57|[faker](https://github.com/joke2k/faker)|Bump version: 18.12.0 → 18.13.0|
|2023-07-07 08:13:56|[trivy](https://github.com/aquasecurity/trivy)|chore(deps): Update defsec to v0.90.3 (#4793)  * ch<br>ore(deps): Update defsec to v0.90.2  Signed-off-by: <br>Simar   * go mod tidy  ---------  Signed-off-by: Sim<br>ar |
|2023-07-07 08:12:50|[dbeaver](https://github.com/dbeaver/dbeaver)|dbeaver/pro#1766 Legacy krb5 support (#20493)  * db<br>eaver/pro#1766 Legacy krb5 support    * 23.1.2 versi<br>on bump|
|2023-07-07 07:26:47|[safeline](https://github.com/chaitin/safeline)|fix: https://github.com/chaitin/safeline/security/d<br>ependabot/57|
|2023-07-07 07:14:15|[FrameVul](https://github.com/Awrrays/FrameVul)|Update README.md|
|2023-07-07 07:09:42|[captcha-killer-mo<br>dified](https://github.com/f0ng/captcha-killer-modified)|Update FAQ.md|
|2023-07-07 06:38:43|[SmsForwarder](https://github.com/pppscn/SmsForwarder)|升级：XUI框架版本（优化XToastUtils等）|
|2023-07-07 03:44:50|[Pentest-Windows](https://github.com/arch3rPro/Pentest-Windows)|Update README.md|
|2023-07-07 02:52:30|[awesome-chatgpt-z<br>h](https://github.com/yzfly/awesome-chatgpt-zh)|add ChatLaw|
|2023-07-07 02:24:11|[Awesome-ChatGPT](https://github.com/dalinvip/Awesome-ChatGPT)|Update README.md|
|2023-07-06 20:56:07|[syft](https://github.com/anchore/syft)|fix(install): return with right error code (#1915) <br> This resolves #1566.    Signed-off-by: Lorenzo Orsa<br>tti   Co-authored-by: Christopher Phillips |
|2023-07-06 16:05:15|[WeblogicTool](https://github.com/KimJun1010/WeblogicTool)|Update README.md|
|2023-07-06 15:19:29|[autoDecoder](https://github.com/f0ng/autoDecoder)|Update README.md|
|2023-07-06 15:11:43|[iDefender](https://github.com/wecooperate/iDefender)|update|
|2023-07-06 13:01:49|[grype](https://github.com/anchore/grype)|Port to new syft source API (#1376)  * port to new <br>syft source API    Signed-off-by: Alex Goodman     *<br> fix linting    Signed-off-by: Alex Goodman     ----<br>-----    Signed-off-by: Alex Goodman |
|2023-07-06 10:50:26|[Elkeid](https://github.com/bytedance/Elkeid)|fix bug: update musl toolchain linker path|
|2023-07-06 08:43:43|[sqlmap](https://github.com/sqlmapproject/sqlmap)|Implements #5452|
|2023-07-06 06:32:34|[CodeQLpy](https://github.com/webraybtl/CodeQLpy)|Update README.md|
|2023-07-06 03:49:38|[HackBrowserData](https://github.com/moonD4rk/HackBrowserData)|Merge pull request #227 from moonD4rk/static/update<br>-logo  chore: update logo filetype|
|2023-07-05 15:04:54|[Vuln-List](https://github.com/wwl012345/Vuln-List)|Update Windows&Linux提权&RCE合集.md|
|2023-07-05 09:40:36|[domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro)|Update SuperJTextArea.java|
|2023-07-05 02:22:34|[Vulnerability-Wik<br>i](https://github.com/Threekiii/Vulnerability-Wiki)|commit|
|2023-07-05 01:49:54|[Awesome-Exploit](https://github.com/Threekiii/Awesome-Exploit)|更新README.md|
|2023-07-05 01:49:32|[Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam)|更新README.md|
|2023-07-05 01:20:42|[Awesome-POC](https://github.com/Threekiii/Awesome-POC)|更新漏洞|
|2023-07-05 00:29:39|[cf](https://github.com/teamssix/cf)|Merge pull request #256 from teamssix/beta  docs: u<br>pdate readme|
|2023-07-04 09:53:57|[knife](https://github.com/bit4woo/knife)|update|
|2023-07-03 16:14:56|[RedisEXP](https://github.com/yuyan-sec/RedisEXP)|github actions|
|2023-07-03 14:48:33|[veinmind-tools](https://github.com/chaitin/veinmind-tools)|feat(ci): add auto sync to registry (#254)|
|2023-07-03 13:12:25|[nuclei](https://github.com/projectdiscovery/nuclei)|dep update|
|2023-07-03 11:33:07|[ghauri](https://github.com/r0oth3x49/ghauri)|updated code quality fixed issue with regex process<br>ing multipart/form-data, bumped version 1.2.2|
|2023-07-03 10:25:32|[mitaka](https://github.com/ninoseki/mitaka)|docs: remove Tines logo [skip ci]|
|2023-07-03 08:50:31|[Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)|新功能：为联动翻译设定单独的快捷键（#166）|
|2023-07-03 07:07:35|[ARL](https://github.com/TophantTechnology/ARL)|Merge pull request #589 from ox01024/update-ipGeo-S<br>ource  使用第三方源的GeoLite2-City更新|
|2023-07-03 05:26:39|[vulnerability](https://github.com/lal0ne/vulnerability)|CVE-2023-34939|
|2023-07-03 03:00:44|[404StarLink](https://github.com/knownsec/404StarLink)|weekly update at 2023-07-03|
|2023-07-02 16:09:12|[PEASS-ng](https://github.com/carlospolop/PEASS-ng)|Update aicoder.yml|
|2023-07-02 07:50:07|[kube-bench](https://github.com/aquasecurity/kube-bench)|Fix test_items in cis-1.7 - node - 4.2.12 (#1469)  <br>Related issue: https://github.com/aquasecurity/kube-<br>bench/issues/1468|
|2023-07-01 22:24:38|[ShiroAttack2](https://github.com/SummerSec/ShiroAttack2)|:bug: fix https://github.com/SummerSec/ShiroAttack2<br>/issues/37|
|2023-07-01 15:14:35|[pikachu](https://github.com/zhuifengshaonianhanlu/pikachu)|Merge pull request #33 from 8023/master  优化docker<br>file|
|2023-07-01 15:12:07|[chatgpt](https://github.com/LangLangShanDeNanKe/chatgpt)|Update README.md|
|2023-06-30 16:04:02|[All-Defense-Tool](https://github.com/guchangan1/All-Defense-Tool)|更新v2.4|
|2023-06-30 06:32:51|[murphysec](https://github.com/murphysecurity/murphysec)|fix: JSON output|
|2023-06-30 05:38:09|[RouteVulScan](https://github.com/F6JO/RouteVulScan)|Update Config_yaml.yaml|
|2023-06-29 13:26:32|[fscan](https://github.com/shadow1ng/fscan)|Merge pull request #280 from dksslq/main  输出格式<br>调整|
|2023-06-29 02:24:05|[v2rayA](https://github.com/v2rayA/v2rayA)|Fix Windows installer build|
|2023-06-28 09:23:27|[Exp-Tools](https://github.com/cseroad/Exp-Tools)|Update README.md|
|2023-06-27 13:38:48|[fofa_viewer](https://github.com/wgpsec/fofa_viewer)|修复CI|
|2023-06-27 11:00:22|[RmEye](https://github.com/RoomaSec/RmEye)|Update readme.md|
|2023-06-27 10:59:07|[RmTools](https://github.com/RoomaSec/RmTools)|Update README.md|
|2023-06-27 09:31:15|[Kunlun-M](https://github.com/LoRexxar/Kunlun-M)|Merge pull request #235 from LoRexxar/develop  upda<br>te startlink|
|2023-06-26 07:04:59|[GobypassAV-shellc<br>ode](https://github.com/Pizz33/GobypassAV-shellcode)|Update README.md|
|2023-06-26 02:41:07|[Dirscan](https://github.com/corunb/Dirscan)|v1.5.1|## 所有项目
# 渗透测试
## 信息收集
### 资产测绘采集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll) | V1.2 | 为了方便安全从业人员在使用网络测绘平台进行信息搜集时的效率，本<br>程序集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并<br>且合并展示及导出。 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | v2.3.3 | 【支持Fofa、Zoomeye、Quake等网络空间搜索引擎】闪电搜索器；GUI<br>图形化渗透测试信息搜集工具；资产搜集引擎 |
| [Search_Viewer](https://github.com/G3et/Search_Viewer) | v2.0 | 集Fofa、Hunter鹰图、Shodan、360 quake、Zoomeye 钟馗之眼为一体<br>的gui图形界面化工具 |
| [koko-moni](https://github.com/burpheart/koko-moni) | v0.0.1 | 一个网络空间搜索引擎监控平台，可定时进行资产信息爬取，及时发现<br>新增资产，本项目聚合了 Fofa、Hunter、Quake、Zoomeye 和 Threatboo<br>k 的数据源，并对获取到的数据进行去重与清洗 |
| [AsamF](https://github.com/Kento-Sec/AsamF) | v0.2.4 | AsamF是集成Fofa、Quake、Hunter、Shodan、Zoomeye、Chinaz、0.zon<br>e及爱企查的一站式企业信息资产收集、网络资产测绘工具。 |
| [fshzqSearch](https://github.com/Ifory885/fshzqSearch) |  | fofa、shodan、hunter、zoomeye、quake网络空间搜索引擎及github聚<br>合搜索，并对结果进行finger指纹识别。 |
| [0_zone_tool](https://github.com/wkend/0_zone_tool) |  | 零零信安api信息系统查询脚本 |
### 子域名收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [subfinder](https://github.com/projectdiscovery/subfinder) | v2.6.0 | Fast passive subdomain enumeration tool. |
| [ksubdomain](https://github.com/knownsec/ksubdomain) | v0.7 | 无状态子域名爆破工具 |
| [OneForAll](https://github.com/shmilylty/OneForAll) | v0.4.5 | OneForAll是一款功能强大的子域收集工具 |
| [LangSrcCurise](https://github.com/LangziFun/LangSrcCurise) |  | SRC子域名资产监控 |
| [github-subdomains](https://github.com/gwen001/github-subdomains) | v1.2.2 | Find subdomains on GitHub. |
| [LayerDomainFinder](https://github.com/euphrat1ca/LayerDomainFinder) | 3 | Layer子域名挖掘机 |
| [dnsub](https://github.com/yunxu1/dnsub) | v2.1 | dnsub一款好用且强大的子域名扫描工具 |
| [ksubdomain](https://github.com/boy-hack/ksubdomain) | v1.9.5 | Subdomain enumeration tool, asynchronous dns packets, use pcap<br> to scan 1600,000 subdomains in 1 second |
| [ct](https://github.com/knownsec/ct) | v1.0.9 | 简单易用的域名爆破工具 |
| [subDomainsBrute](https://github.com/lijiejie/subDomainsBrute) | v1.4 | A fast sub domain brute tool for pentesters |
### 目录扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dirsearch](https://github.com/maurosoria/dirsearch) | v0.4.3 | Web path scanner |
| [feroxbuster](https://github.com/epi052/feroxbuster) | v2.10.0 | A fast, simple, recursive content discovery tool written in Ru<br>st. |
| [ffuf](https://github.com/ffuf/ffuf) | v2.0.0 | Fast web fuzzer written in Go |
| [dirmap](https://github.com/H4ckForJob/dirmap) |  | An advanced web directory & file scanning tool that will be mo<br>re powerful than DirBuster, Dirsearch, cansina, and Yu Jian.一<br>个高级web目录、文件扫描工具，功能将会强于DirBuster、Dirsearch、c<br>ansina、御剑。 |
| [cansina](https://github.com/deibit/cansina) | 1.0.0 | Web Content Discovery Tool |
| [urlbrute](https://github.com/ReddyyZ/urlbrute) | v1.0.2 | Directory/Subdomain scanner developed in GoLang. |
| [yjdirscan](https://github.com/foryujian/yjdirscan) | yjdirsc<br>an | 御剑目录扫描专业版，简单实用的命令行网站目录扫描工具，支持爬虫<br>、fuzz、自定义字典、字典变量、UA修改、假404自动过滤、扫描控速等<br>功能。 |
| [SWebScan](https://github.com/shack2/SWebScan) | 5.0.201<br>8.08.21 | SWebScan是一款基于C#的Web目录扫描器。 |
| [yuhScan](https://github.com/hunyaio/yuhScan) | v1.0 | web目录快速扫描工具 |
| [gospider](https://github.com/jaeles-project/gospider) | v1.1.6 | Gospider - Fast web spider written in Go |
| [rad](https://github.com/chaitin/rad) | 1.0 |  |
| [URLFinder](https://github.com/pingc0y/URLFinder) | 2023.5.<br>11 | 一款快速、全面、易用的页面信息提取工具，可快速发现和提取页面中<br>的JS、URL和敏感信息。 |
| [JSFinder](https://github.com/Threezh1/JSFinder) |  | JSFinder is a tool for quickly extracting URLs and subdomains <br>from JS files on a website. |
| [BBScan](https://github.com/lijiejie/BBScan) | v1.5 | A fast vulnerability scanner |
| [Dirscan](https://github.com/corunb/Dirscan) | v1.5.1 | Dirscan是一款由go编写的高性能、高并发的目录扫描器，现在已经支<br>持GET、HEAD、递归扫描、代理、爬虫等功能功能,后续努力实现更多功能<br>。 |
### 指纹识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EHole](https://github.com/EdgeSecurityTeam/EHole) | v3.1 | EHole(棱洞)3.0 重构版-红队重点攻击系统指纹探测工具 |
| [Glass](https://github.com/s7ckTeam/Glass) |  | Glass是一款针对资产列表的快速指纹识别工具，通过调用Fofa/ZoomEy<br>e/Shodan/360等api接口快速查询资产信息并识别重点资产的指纹，也可<br>针对IP/IP段或资产列表进行快速的指纹识别。 |
| [Finger](https://github.com/EASY233/Finger) |  | 一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具 |
| [LazyDog](https://github.com/L10nK1n6/LazyDog) | 1.1 | LazyDog是一款通过网络空间测绘引擎读取资产并进行指纹识别的工具 |
| [whatweb-plus](https://github.com/winezer0/whatweb-plus) | v0.5.5.<br>19.fix | whatweb 增强版  8000+插件（提供windows可执行文件） |
### WAF识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [identYwaf](https://github.com/stamparm/identYwaf) |  | Blind WAF identification tool |
### 端口扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [webfinder-next](https://github.com/Liqunkit/webfinder-next) |  | 对小米范webfinder http://www.cnblogs.com/SEC-fsq/p/5610981.htm<br>l 进行了小修改 |
| [yujianportscan](https://github.com/foryujian/yujianportscan) |  | 一个基于VB.NET + IOCP模型开发的高效端口扫描工具，支持IP区间合<br>并，端口区间合并，端口指纹深度探测 |
| [TXPortMap](https://github.com/4dogs-cn/TXPortMap) | v1.1.2 | Port Scanner & Banner Identify From TianXiang |
| [naabu](https://github.com/projectdiscovery/naabu) | v2.1.6 | A fast port scanner written in go with a focus on reliability <br>and simplicity. Designed to be used in combination with other t<br>ools for attack surface discovery in bug bounties and pentests |
| [scaninfo](https://github.com/redtoolskobe/scaninfo) | v1.1.0 | fast scan for redtools |
| [portscan](https://github.com/20142995/portscan) |  |  |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dismap](https://github.com/zhzyker/dismap) | v0.4 | Asset discovery and identification tools 快速识别 Web 指纹信息<br>，定位资产类型。辅助红队快速定位目标资产信息，辅助蓝队发现疑似脆<br>弱点 |
| [AssetsHunter](https://github.com/rabbitmask/AssetsHunter) |  | 资产狩猎框架-AssetsHunter，信息收集是一项艺术~ |
| [TScan](https://github.com/dyboy2017/TScan) |  | TScan 提供了CMS指纹识别、端口扫描、旁站信息、信息泄漏等功能，<br>期许在最短的时间辅助安全人员在渗透前做好充分的信息搜集 |
### 自动化信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [H](https://github.com/SiJiDo/H) |  | H是一款强大的资产收集管理平台 |
| [slime](https://github.com/ccreater222/slime) |  | Slime是一个组合众多优秀安全工具的漏扫软件，它将目光集中在安全<br>工具的组合上，而不是自己实现漏扫的某一流程。 |
| [X-Marshal](https://github.com/XTeam-Wing/X-Marshal) |  | Marshal-EASM |
| [heartsk_community](https://github.com/yqcs/heartsk_community) | LOWBUG@<br>Latest | Hearts K-企业资产发现与脆弱性检查工具，自动化资产信息收集与漏<br>洞扫描 |
| [AnScan](https://github.com/Arbor01/AnScan) |  | AnScan是一款集合信息收集、分布式漏洞扫描、漏洞POC管理等为一体<br>的红队扫描工具 |
| [nemo_go](https://github.com/hanc00l/nemo_go) | v2.9.3 | Nemo是用来进行自动化信息收集的一个简单平台，通过集成常用的信息<br>收集工具和技术，实现对内网及互联网资产信息的自动收集，提高隐患排<br>查和渗透测试的工作效率。 |
| [rengine](https://github.com/yogeshojha/rengine) | v1.3.6 | reNgine is an automated reconnaissance framework for web appli<br>cations with a focus on highly configurable streamlined recon p<br>rocess via Engines, recon data correlation and organization, co<br>ntinuous monitoring, backed by a database, and simple yet intui<br>tive User Interface. reNgine makes it easy for penetration test<br>ers to gather reconnaissance with minimal configuration and wit<br>h the help of reNgine's correlation, it just makes recon effort<br>less. |
| [ShuiZe_0x727](https://github.com/0x727/ShuiZe_0x727) | v1.0 | 信息收集自动化工具 |
| [DBJ](https://github.com/wgpsec/DBJ) |  | 大宝剑-边界资产梳理工具（红队、蓝队、企业组织架构、子域名、Web<br>资产梳理、Web指纹识别、ICON_Hash资产匹配） |
| [Voyager](https://github.com/xundididi/Voyager) |  | 一个安全工具集合平台，用来提高乙方安全人员的工作效率，请勿用于<br>非法项目 |
| [GoScan](https://github.com/CTF-MissFeng/GoScan) |  | GoScan是采用Golang语言编写的一款分布式综合资产管理系统，适合红<br>队、SRC等使用 |
| [Autoscanner](https://github.com/zongdeiqianxing/Autoscanner) | v1.2.1 | 输入域名>爆破子域名>扫描子域名端口>发现扫描web服务>集成报告的<br>全流程全自动扫描器。集成oneforall、masscan、nmap、dirsearch、cra<br>wlergo、xray等工具，另支持cdn识别、网页截图、站点定位；动态识别<br>域名并添加功能、工具超时中断等 |
| [MagiCude](https://github.com/er10yi/MagiCude) | v2.1 | 分布式端口（漏洞）扫描、资产安全管理、实时威胁监控与通知、高效<br>漏洞闭环、漏洞wiki、邮件报告通知、poc框架 |
| [Watchdog](https://github.com/CTF-MissFeng/Watchdog) |  | Watchdog是bayonet修改版，重新优化了数据库及web及扫描程序,加入<br>多节点 |
| [Tide](https://github.com/TideSec/Tide) |  | 目前实现了网络空间资产探测、指纹检索、漏洞检测、漏洞全生命周期<br>管理、poc定向检测、暗链检测、挂马监测、敏感字检测、DNS监测、网站<br>可用性监测、漏洞库管理、安全预警等等~ |
| [ARL](https://github.com/TophantTechnology/ARL) | v2.5.5 | ARL(Asset Reconnaissance Lighthouse)资产侦察灯塔系统旨在快速侦<br>察与目标关联的互联网资产，构建基础资产信息库。 协助甲方安全团队<br>或者渗透测试人员有效侦察和检索资产，发现存在的薄弱点和攻击面。 |
| [linglong](https://github.com/awake1t/linglong) |  | 一款甲方资产巡航扫描系统。系统定位是发现资产，进行端口爆破。帮<br>助企业更快发现弱口令问题。主要功能包括: 资产探测、端口爆破、定时<br>任务、管理后台识别、报表展示 |
| [sec-admin](https://github.com/smallcham/sec-admin) |  | 分布式资产安全扫描核心管理系统(弱口令扫描，漏洞扫描) |
| [linbing](https://github.com/taomujian/linbing) | v3.0 | 本系统是对Web中间件和Web框架进行自动化渗透的一个系统,根据扫描<br>选项去自动化收集资产,然后进行POC扫描,POC扫描时会根据指纹选择POC<br>插件去扫描,POC插件扫描用异步方式扫描.前端采用vue技术,后端采用pyt<br>hon fastapi. |
| [Vulcan](https://github.com/XTeam-Wing/Vulcan) |  | VulCan资产管理系统|漏洞扫描|资产探测|定时扫描 |
| [bayonet](https://github.com/CTF-MissFeng/bayonet) | v1.1 | bayonet是一款src资产管理系统，从子域名、端口服务、漏洞、爬虫等<br>一体化的资产管理系统 |
| [fuxi](https://github.com/jeffzh3ng/fuxi) |  | Penetration Testing Platform |
| [WebScan](https://github.com/xuchaoa/WebScan) |  | 正在写的一个资产管理和扫描相结合的分布式扫描器 |
| [xunfeng](https://github.com/ysrc/xunfeng) | v0.1.1 | 巡风是一款适用于企业内网的漏洞快速应急，巡航扫描系统。 |
| [AppInfoScanner](https://github.com/kelvinBen/AppInfoScanner) | V1.0.9_<br>Releases | 一款适用于以HW行动/红队/渗透测试团队为场景的移动端(Android、iO<br>S、WEB、H5、静态网站)信息收集扫描工具，可以帮助渗透测试工程师、<br>攻击队成员、红队成员快速收集到移动端或者静态WEB站点中关键的资产<br>信息并提供基本的信息输出,如：Title、Domain、CDN、指纹信息、状态<br>信息等。 |
| [Sec-Tools](https://github.com/jwt1399/Sec-Tools) |  | 🍉一款基于Python-Django的多功能Web安全渗透测试工具，包含漏洞扫<br>描，端口扫描，指纹识别，目录扫描，旁站扫描，域名扫描等功能。 |
| [Komo](https://github.com/komomon/Komo) |  | 🚀Komo, a comprehensive asset collection and vulnerability sca<br>nning tool. Komo 一个综合资产收集和漏洞扫描工具，集成了20余款工<br>具，通过多种方式对子域进行获取，收集域名邮箱，进行存活探测，域名<br>指纹识别，域名反查ip，ip端口扫描，web服务链接爬取并发送给xray，<br>对web服务进行POC漏洞扫描，对主机进行主机漏洞扫描。 |
| [mscan](https://github.com/mscandev/mscan) |  | 方便快捷是这款扫描器的优点，能随意修改增加模块。目前的版本功能<br>如下：支持子域名收集、POC批量验证、目录扫描、检测CDN、域名转IP、<br>主机扫描、过滤重复、检测HTTP状态、压缩程序、XRAY扫描。 |
| [vulcat](https://github.com/CLincat/vulcat) | v2.0.0 | vulcat可用于扫描Web端常见的CVE、CNVD等编号的漏洞，发现漏洞时会<br>返回Payload信息。部分漏洞还支持命令行交互模式，可以持续利用漏洞 |
### 企业信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ENScan_GO](https://github.com/wgpsec/ENScan_GO) | 0.0.13 | 一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信<br>息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信<br>息聚合导出。 |
### 小程序信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [wxapkgUnpack](https://github.com/jdr2021/wxapkgUnpack) | 1.0 | wxapkg解密解包工具，提供C#和wxappUnpacker两个版本的解包，并提<br>取JS中的URL和IP。 |
### C段信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [IPSearch](https://github.com/SleepingBag945/IPSearch) | v0.1 | 离线IP Whois查询工具。可根据IP查询所属IP段信息、根据关键词查询<br>IP段信息 |
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
| [QueryTools](https://github.com/z-bool/QueryTools) |  | IP/域名资产验证神器(补天|权重、CNVD|注册资金)-功能(IP反查域名<br>、域名备案、ICP资产、公司注册资金、权重、IP定位)快速验证是否为需<br>求资产 |
### apk
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ApkAnalyser](https://github.com/TheKingOfDuck/ApkAnalyser) |  | 一键提取安卓应用中可能存在的敏感信息。 |
| [Mobile-Security-F<br>ramework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | v3.6.0 | Mobile Security Framework (MobSF) is an automated, all-in-one <br>mobile application (Android/iOS/Windows) pen-testing, malware a<br>nalysis and security assessment framework capable of performing<br> static and dynamic analysis. |
## 漏洞发现
### 漏洞扫描框架
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pocsuite3](https://github.com/knownsec/pocsuite3) | v2.0.4 | pocsuite3 is an open-sourced remote vulnerability testing fram<br>ework developed by the Knownsec 404 Team. |
| [Godscan](https://github.com/Guoke324/Godscan) | Godscan | Godscan 是一款python编写的具有图形化界面的漏洞检测框架，可以之<br>定义漏洞检测 poc ，主要是帮助安全测试者，更好的去记录和整理历史<br>漏洞，以便更好的进行漏洞检测，提高工作效率！ |
| [FrameScan-GUI](https://github.com/qianxiao996/FrameScan-GUI) | v1.4.3 | FrameScan-GUI 一款python3和Pyqt编写的具有图形化界面的cms漏洞检<br>测框架。 |
| [Gr33k](https://github.com/lijiaxing1997/Gr33k) |  | 图形化漏洞利用集成工具 |
| [kunpeng](https://github.com/opensec-cn/kunpeng) | 2019052<br>7 | kunpeng是一个Golang编写的开源POC框架/库，以动态链接库的形式提<br>供各种语言调用，通过此项目可快速开发漏洞检测类的系统。 |
| [pocassist](https://github.com/jweny/pocassist) | 1.0.5 | 傻瓜式漏洞PoC测试框架 |
### 半自动漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EasyPen](https://github.com/lijiejie/EasyPen) |  | EasyPen is a GUI program which helps pentesters do target disc<br>overy, vulnerability scan and exploitation |
| [xray](https://github.com/chaitin/xray) | 1.9.11 | 一款完善的安全评估工具，支持常见 web 安全问题扫描和自定义 poc <br>| 使用之前务必先阅读文档 |
| [w13scan](https://github.com/w-digital-scanner/w13scan) |  | Passive Security Scanner (被动式安全扫描器) |
| [Fvuln](https://github.com/d3ckx1/Fvuln) | Fvuln-1<br>.4.9 | F-vuln（全称：Find-Vulnerability）是为了自己工作方便专门编写的<br>一款自动化工具，主要适用于日常安全服务、渗透测试人员和RedTeam红<br>队人员，它集合的功能包括：存活IP探测、开放端口探测、web服务探测<br>、web漏洞扫描、smb爆破、ssh爆破、ftp爆破、mssql爆破等其他数据库<br>爆破工作以及大量web漏洞检测模块。 |
| [nuclei](https://github.com/projectdiscovery/nuclei) | v2.9.8 | Fast and customizable vulnerability scanner based on simple YA<br>ML based DSL. |
| [afrog](https://github.com/zan8in/afrog) | v2.7.1 | A Security Tool for Bug Bounty, Pentest and Red Teaming. |
| [vulmap](https://github.com/zhzyker/vulmap) | v0.9 | Vulmap 是一款 web 漏洞扫描和验证工具, 可对 webapps 进行漏洞扫<br>描, 并且具备漏洞验证功能 |
| [POC-bomber](https://github.com/tr0uble-mAker/POC-bomber) | POC-bom<br>ber-for-<br>Redteam-<br>v3.0.0 | 利用大量高威胁poc/exp快速获取目标权限，用于渗透和红队快速打点 |
| [QingTing](https://github.com/StarCrossPortal/QingTing) | v0.3 | 蜻蜓安全一个安全工具编排平台,可以自由编排你的工具流,集成108款<br>工具,包括xray、nmap、awvs等;你可以将喜欢的工具编排成一个场景，快<br>速打造适合自己的安全工作台~ |
| [myscan](https://github.com/amcai/myscan) |  | myscan  被动扫描 |
| [NextScan](https://github.com/tongcheng-security-team/NextScan) | v1.2.0 | 飞刃是一套完整的企业级黑盒漏洞扫描系统，集成漏洞扫描、漏洞管理<br>、扫描资产、爬虫等服务。 拥有强大的漏洞检测引擎和丰富的插件库，<br>覆盖多种漏洞类型和应用程序框架。 |
### 中间件&框架漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WeblogicScan](https://github.com/rabbitmask/WeblogicScan) |  | Weblogic一键漏洞检测工具，V1.5，更新时间：20200730 |
| [weblogic-infodete<br>ctor](https://github.com/woodpecker-appstore/weblogic-infodetector) | 0.2.4 | woodpecker框架weblogic信息探测插件 |
| [Jiraffe](https://github.com/0x48piraj/Jiraffe) | v2.0.6 | One stop place for exploiting Jira instances in your proximity |
| [Artillery](https://github.com/Weik1/Artillery) | v1.0_20<br>220519 | JAVA 插件化漏洞扫描器，Gui基于javafx。POC 目前集成 Weblogic、T<br>omcat、Shiro、Spring等。 |
### 安卓漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [appshark](https://github.com/bytedance/appshark) | v0.1.2 | Appshark is a static taint analysis platform to scan vulnerabi<br>lities in an Android app. |
### 代码审计
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [murphysec](https://github.com/murphysecurity/murphysec) | v3.1.1 | An open source tool focused on software supply chain security.<br> 墨菲安全专注于软件供应链安全，具备专业的软件成分分析（SCA）、<br>漏洞检测、专业漏洞库。 |
| [Kunlun-M](https://github.com/LoRexxar/Kunlun-M) | v2.6.5 | KunLun-M是一个完全开源的静态白盒扫描工具，支持PHP、JavaScript<br>的语义扫描，基础安全、组件安全扫描，Chrome Ext\Solidity的基础扫<br>描。 |
| [CodeQLpy](https://github.com/webraybtl/CodeQLpy) |  | CodeQLpy是一款基于CodeQL实现的半自动化代码审计工具，目前仅支持<br>java语言。实现从源码反编译，数据库生成，脆弱性发现的全过程，可<br>以辅助代码审计人员快速定位源码可能存在的漏洞。 |
### 容器漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [veinmind-tools](https://github.com/chaitin/veinmind-tools) | v2.1.4 | veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器<br>安全工具集 |
### 口令爆破
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [goon](https://github.com/i11us0ry/goon) | v3.5 | goon,集合了fscan和kscan等优秀工具功能的扫描爆破工具。功能包含<br>：ip探活、port扫描、web指纹扫描、title扫描、压缩文件扫描、fofa获<br>取、ms17010、mssql、mysql、postgres、redis、ssh、smb、rdp、telne<br>t、tomcat等爆破以及如netbios探测等功能。 |
| [SNETCracker](https://github.com/shack2/SNETCracker) | 1.0.201<br>90715 | 超级弱口令检查工具是一款Windows平台的弱口令审计工具，支持批量<br>多线程检查，可快速发现弱密码、弱口令账号，密码支持和用户名结合进<br>行检查，大大提高成功率，支持自定义服务端口和字典。 |
| [web-brutator](https://github.com/koutto/web-brutator) |  | Fast Modular Web Interfaces Bruteforcer |
| [WebCrack](https://github.com/yzddmr6/WebCrack) |  | WebCrack是一款web后台弱口令/万能密码批量检测工具，在工具中导入<br>后台地址即可进行自动化检测。 |
| [ssb](https://github.com/pwnesia/ssb) | v0.1.1 | Secure Shell Bruteforcer — A faster & simpler way to brutefor<br>ce SSH server |
| [thc-hydra-windows](https://github.com/maaaaz/thc-hydra-windows) | v9.1 | The great THC-HYDRA tool compiled for Windows |
### 漏洞发现
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Dude](https://github.com/x364e3ab6/Dude) |  |  |
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
| [metarget](https://github.com/Metarget/metarget) | v0.9.1 | Metarget is a framework providing automatic constructions of v<br>ulnerable infrastructures. |
#### 容器漏洞利用工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CDK](https://github.com/cdk-team/CDK) | v1.5.2 | 📦  Make security testing of K8s, Docker, and Containerd easie<br>r. |
#### 容器逃逸检测工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [container-escape-<br>check](https://github.com/teamssix/container-escape-check) | v0.3 | docker container escape check || Docker 容器逃逸检测 |
#### 容器安全检测工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [veinmind-tools](https://github.com/chaitin/veinmind-tools) | v2.1.4 | veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器<br>安全工具集 |
#### 容器漏洞分析工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [clair](https://github.com/quay/clair) | v4.6.1 | Vulnerability Static Analysis for Containers |
#### 容器安全扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [trivy](https://github.com/aquasecurity/trivy) | v0.43.1 | Find vulnerabilities, misconfigurations, secrets, SBOM in cont<br>ainers, Kubernetes, code repositories, clouds and more |
#### 容器镜像扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [grype](https://github.com/anchore/grype) | v0.63.1 | A vulnerability scanner for container images and filesystems |
| [syft](https://github.com/anchore/syft) | v0.84.1 | CLI tool and library for generating a Software Bill of Materia<br>ls from container images and filesystems |
#### K8S漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-hunter](https://github.com/aquasecurity/kube-hunter) | v0.6.8 | Hunt for security weaknesses in Kubernetes clusters |
#### K8S基线核查
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | v0.6.15 | Checks whether Kubernetes is deployed according to security be<br>st practices as defined in the CIS Kubernetes Benchmark |
#### 云原生安全平台
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [neuvector](https://github.com/neuvector/neuvector) | v5.2.0 |  |
### 半自动化漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [railgun](https://github.com/lz520520/railgun) | v1.5.5 |  |
| [Goby](https://github.com/gobysec/Goby) | Beta2.2<br>.0 | Attack surface mapping |
| [zpscan](https://github.com/niudaii/zpscan) | v1.8.39 | 一个有点好用的信息收集工具。A somewhat useful information gath<br>ering tool. |
### 数据库利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [MDUT](https://github.com/SafeGroceryStore/MDUT) | v2.1.1 | MDUT - Multiple Database Utilization Tools |
| [SharpSQLTools](https://github.com/uknowsec/SharpSQLTools) | 41 | SharpSQLTools 和@Rcoil一起写的小工具，可上传下载文件，xp_cmdsh<br>ell与sp_oacreate执行命令回显和clr加载程序集执行相应操作。 |
| [mssqlproxy](https://github.com/blackarrowsec/mssqlproxy) | 0.1 | mssqlproxy is a toolkit aimed to perform lateral movement in r<br>estricted environments through a compromised Microsoft SQL Serv<br>er via socket reuse |
| [odat](https://github.com/quentinhardy/odat) | 5.1.1 | ODAT: Oracle Database Attacking Tool |
| [redis-rogue-serve<br>r](https://github.com/n0b0dyCN/redis-rogue-server) |  | Redis(<=5.0.5) RCE |
| [redis-rce](https://github.com/Ridter/redis-rce) |  | Redis 4.x/5.x RCE |
| [RedisEXP](https://github.com/yuyan-sec/RedisEXP) | 0.0.2 | Redis 漏洞利用工具 |
| [redis_rce](https://github.com/zyylhn/redis_rce) | v0.1.0 | Redis primary/secondary replication RCE |
| [RequestTemplate](https://github.com/1n7erface/RequestTemplate) |  |  |
| [redis-rogue-serve<br>r](https://github.com/Dliv3/redis-rogue-server) |  | Redis 4.x/5.x RCE |
| [Databasetools](https://github.com/Hel10-Web/Databasetools) | 1.2 | 一款用Go语言编写的数据库自动化提权工具，支持Mysql、MSSQL、Post<br>gresql、Oracle、Redis数据库提权、命令执行、爆破以及ssh连接 |
### 中间件&框架漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [AttackTomcat](https://github.com/tpt11fb/AttackTomcat) | V1 | Tomcat常见漏洞GUI利用工具。CVE-2017-12615 PUT文件上传漏洞、tom<br>cat-pass-getshell 弱认证部署war包、弱口令爆破、CVE-2020-1938 To<br>mcat AJP文件读取/包含 |
| [SpringExploit](https://github.com/SummerSec/SpringExploit) | 0.1.9 | 🚀 一款为了学习go而诞生的漏洞利用工具 |
| [shiro_rce_tool](https://github.com/wyzxxz/shiro_rce_tool) |  | shiro 反序列 命令执行辅助检测工具 |
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2) | 4.7.0 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复<br>原版中NoCC的问题 https://github.com/j1anFen/shiro_attack |
| [shiro_attack](https://github.com/j1anFen/shiro_attack) | 2.2 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马） |
| [FastjsonExploit](https://github.com/c0ny1/FastjsonExploit) |  | Fastjson vulnerability quickly exploits the framework（fastjso<br>n漏洞快速利用框架） |
| [fastjson_rec_expl<br>oit](https://github.com/mrknow001/fastjson_rec_exploit) |  | fastjson一键命令执行 |
| [jexboss](https://github.com/joaomatosf/jexboss) |  | JexBoss: Jboss (and Java Deserialization Vulnerabilities) veri<br>fy and EXploitation Tool |
| [weblogic-framewor<br>k](https://github.com/dream0x01/weblogic-framework) | v0.2.3 | weblogic-framework is the best tool for detecting weblogic vul<br>nerabilities. |
| [WeblogicTool](https://github.com/KimJun1010/WeblogicTool) | v1.2 | WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马<br>注入、密码解密等（深信服深蓝实验室天威战队强力驱动） |
| [dubbo-exp](https://github.com/threedr3am/dubbo-exp) |  | dubbo学习demo，之前删了，重新上传。 |
| [STS2G](https://github.com/xfiftyone/STS2G) | 1.0 | Struts2漏洞扫描利用工具 - Golang版. Struts2 Scanner Written in<br> Golang |
| [Struts2-Scan](https://github.com/HatBoy/Struts2-Scan) |  | Struts2全漏洞扫描利用工具 |
| [log4j-shell-poc](https://github.com/kozmer/log4j-shell-poc) |  | A Proof-Of-Concept for the CVE-2021-44228 vulnerability.  |
| [SpringBootExploit](https://github.com/0x727/SpringBootExploit) | 1.3 | 项目是根据LandGrey/SpringBootVulExploit清单编写，目的hvv期间快<br>速利用漏洞、降低漏洞利用门槛。 |
| [SpringBoot-Scan-G<br>UI](https://github.com/13exp/SpringBoot-Scan-GUI) | v1.2.2 |  |
| [CVE-2023-21839](https://github.com/4ra1n/CVE-2023-21839) |  | Weblogic CVE-2023-21839 / CVE-2023-21931 / CVE-2023-21979 一键<br>检测 |
| [Tomcat_PUT_GUI_EX<br>P](https://github.com/xiaokp7/Tomcat_PUT_GUI_EXP) | 1.4 | Tomcat PUT方法任意文件写入（CVE-2017-12615）exp |
### 漏洞利用辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jndi_tool](https://github.com/wyzxxz/jndi_tool) |  | JNDI服务利用工具 RMI/LDAP，支持部分场景回显、内存shell，高版本<br>JDK场景下利用等，fastjson rce命令执行，log4j rce命令执行 漏洞检<br>测辅助工具 |
| [ysoserial](https://github.com/frohoff/ysoserial) | v0.0.6 | A proof-of-concept tool for generating payloads that exploit u<br>nsafe Java object deserialization. |
| [Gopherus](https://github.com/tarunkant/Gopherus) |  | This tool generates gopher link for exploiting SSRF and gainin<br>g RCE in various servers |
| [revsuit](https://github.com/Li4n0/revsuit) | v0.7.1 | RevSuit is a flexible and powerful reverse connection platform<br> designed for receiving connection from target host in penetrat<br>ion.  |
| [DNSlog-GO](https://github.com/lanyi1998/DNSlog-GO) | 1.5.6 | DNSLog-GO 是一款golang编写的监控 DNS 解析记录的工具，自带WEB界<br>面 |
| [godnslog](https://github.com/chennqqi/godnslog) | v0.7.0 | An exquisite dns&http log server for verify SSRF/XXE/RFI/RCE v<br>ulnerability  |
| [ysomap](https://github.com/wh1t3p1g/ysomap) | v0.1.3 | A helpful Java Deserialization exploit framework. |
| [Antenna](https://github.com/wuba/Antenna) | v1.3.5 | Antenna是58同城安全团队打造的一款辅助安全从业人员验证网络中多<br>种漏洞是否存在以及可利用性的工具。其基于带外应用安全测试(OAST)通<br>过任务的形式，将不同漏洞场景检测能力通过插件的形式进行集合，通过<br>与目标进行out-bind的数据通信方式进行辅助检测。 |
| [cola_dnslog](https://github.com/AbelChe/cola_dnslog) | v1.3.2 | Cola Dnslog v1.3.2 更加强大的dnslog平台/无回显漏洞探测辅助平台<br> 完全开源 dnslog httplog ldaplog rmilog 支持dns http ldap rmi等<br>协议 提供API调用方式便于与其他工具结合 支持钉钉机器人、Bark等提<br>醒 支持docker一键部署 后端完全使用python实现 前端基于vue-element<br>-admin二开 |
| [ddddocr](https://github.com/sml2h3/ddddocr) |  | 带带弟弟 通用验证码识别OCR pypi版 |
| [ysoserial](https://github.com/su18/ysoserial) |  |  |
| [JNDIExploit](https://github.com/WhiteHSBG/JNDIExploit) | v1.4 | 对原版https://github.com/feihong-cs/JNDIExploit 进行了实用化修<br>改 |
| [JNDIExploit-1](https://github.com/Mr-xn/JNDIExploit-1) | v1.2 | 一款用于 JNDI注入 利用的工具，大量参考/引用了 Rogue JNDI 项目<br>的代码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的<br>方式，适用于与自动化工具配合使用。（from https://github.com/feih<br>ong-cs/JNDIExploit） |
| [JNDIExploit](https://github.com/0x727/JNDIExploit) | 1.1 | 一款用于JNDI注入利用的工具，大量参考/引用了Rogue JNDI项目的代<br>码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的方式<br>，适用于与自动化工具配合使用。 |
| [Exp-Tools](https://github.com/cseroad/Exp-Tools) | v1.2.0 | 一款集成各种exp的实用性工具 |
### 重点CMS利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL) | OA-EXPT<br>OOL-0.72 | OA综合利用工具，集合将近20款OA漏洞批量扫描 |
| [seeyon_exp](https://github.com/Summer177/seeyon_exp) |  | 致远OA综合利用工具 |
| [SeeyonExploit-GUI](https://github.com/God-Ok/SeeyonExploit-GUI) |  | 致远OA综合利用工具V1.0 |
| [TDOA_RCE](https://github.com/xinyu2428/TDOA_RCE) | v1.0 | 通达OA综合利用工具 |
| [LandrayExploit](https://github.com/yuanhaiGreg/LandrayExploit) |  |  |
| [weaver_exp](https://github.com/z1un/weaver_exp) |  | 泛微OA漏洞综合利用脚本 |
| [EgGateWayGetShell](https://github.com/Tas9er/EgGateWayGetShell) |  | Code By:Tas9er |
| [CMSmap](https://github.com/Dionach/CMSmap) |  | CMSmap is a python open source CMS scanner that automates the <br>process of detecting security flaws of the most popular CMSs.  |
| [wprecon](https://github.com/blackbinn/wprecon) |  |  |
| [wordpress-exploit<br>-framework](https://github.com/rastating/wordpress-exploit-framework) | v2.0.1 | A Ruby framework designed to aid in the penetration testing of<br> WordPress systems.  |
| [wpscan](https://github.com/wpscanteam/wpscan) | v3.8.24 | WPScan WordPress security scanner. Written for security profes<br>sionals and blog maintainers to test the security of their Word<br>Press websites. Contact us via contact@wpscan.com |
| [wprecon](https://github.com/AngraTeam/wprecon) |  |  |
| [Aazhen-RexHa](https://github.com/zangcc/Aazhen-RexHa) |  | 自研JavaFX图形化漏洞扫描工具，支持扫描的漏洞分别是： ThinkPHP-<br>2.x-RCE， ThinkPHP-5.0.23-RCE， ThinkPHP5.0.x-5.0.23通杀RCE， T<br>hinkPHP5-SQL注入&敏感信息泄露， ThinkPHP 3.x 日志泄露NO.1， Thi<br>nkPHP 3.x 日志泄露NO.2， ThinkPHP 5.x 数据库信息泄露的漏洞检测<br>，以及批量检测的功能。漏洞POC基本适用ThinkPHP全版本漏洞。 |
| [ThinkphpGUI](https://github.com/Lotus6/ThinkphpGUI) | 1.3 | Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，get<br>shell。 |
| [thinkphp_gui_tool<br>s](https://github.com/bewhale/thinkphp_gui_tools) | v2.4.2 | ThinkPHP漏洞综合利用工具, 图形化界面, 命令执行, 一键getshell, <br>批量检测, 日志遍历, session包含,宝塔绕过 |
| [Apt_t00ls](https://github.com/White-hua/Apt_t00ls) | v0.6 | 高危漏洞利用工具 |
| [yonyou_exp_plus](https://github.com/li8u99/yonyou_exp_plus) |  | 用友系列全漏洞检测工具 |
### 信息泄露利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Cloud-Bucket-Leak<br>-Detection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | v0.4.0 | 六大云存储，泄露利用检测工具 |
| [aksk_tool](https://github.com/wyzxxz/aksk_tool) |  | AK资源管理工具，阿里云/腾讯云/华为云/AWS/UCLOUD/京东云/百度云/<br>七牛云存储  AccessKey AccessKeySecret，利用AK获取资源信息和操作<br>资源，ECS/CVM/E2/UHOST/ECI/BCC执行命令，OSS/COS/S3/BOS管理，RDS/<br>DB管理，域名管理，添加RAM/CAM/IAM账号等 |
| [swagger-exp](https://github.com/lijiejie/swagger-exp) |  | A Swagger API Exploit |
| [swagger-hack](https://github.com/jayus0821/swagger-hack) |  | 自动化爬取并自动测试所有swagger接口 |
| [heapdump_tool](https://github.com/wyzxxz/heapdump_tool) |  | heapdump敏感信息查询工具，例如查找 spring heapdump中的密码明文<br>，AK,SK等 |
| [Packer-Fuzzer](https://github.com/rtcatc/Packer-Fuzzer) | v1.4 | Packer Fuzzer is a fast and efficient scanner for security det<br>ection of websites constructed by javascript module bundler suc<br>h as Webpack.  |
| [GitHack](https://github.com/BugScanTeam/GitHack) |  | .git 泄漏利用工具，可还原历史版本 |
| [dvcs-ripper](https://github.com/kost/dvcs-ripper) |  | Rip web accessible (distributed) version control systems: SVN/<br>GIT/HG... |
| [ds_store_exp](https://github.com/lijiejie/ds_store_exp) |  | A .DS_Store file disclosure exploit.   It parses .DS_Store fil<br>e and downloads files recursively. |
| [svnExploit](https://github.com/admintony/svnExploit) |  | SvnExploit支持SVN源代码泄露全版本Dump源码 |
| [git-dumper](https://github.com/arthaud/git-dumper) |  | A tool to dump a git repository from a website |
| [GitDorker](https://github.com/obheda12/GitDorker) |  | A Python program to scrape secrets from GitHub through usage o<br>f a large repository of dorks. |
| [SecretFinder](https://github.com/m4ll0k/SecretFinder) |  | SecretFinder - A python script for find sensitive data (apikey<br>s, accesstoken,jwt,..) and search anything on javascript files  |
| [JSFScan.sh](https://github.com/KathanP19/JSFScan.sh) |  | Automation for javascript recon in bug bounty.  |
| [SubOver](https://github.com/Ice3man543/SubOver) | v1.2 | A Powerful Subdomain Takeover Tool |
| [JDumpSpider](https://github.com/whwlsfb/JDumpSpider) | dev-202<br>30406T03<br>1230 | HeapDump敏感信息提取工具 |
### 漏洞检测利用仓库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [poc-hub](https://github.com/ybdt/poc-hub) |  |  |
| [Awesome-Exploit](https://github.com/Threekiii/Awesome-Exploit) |  | 一个漏洞利用工具仓库 |
| [exphub](https://github.com/zhzyker/exphub) |  | Exphub[漏洞利用脚本库] 包括Webloigc、Struts2、Tomcat、Nexus、S<br>olr、Jboss、Drupal的漏洞利用脚本，最新添加CVE-2020-14882、CVE-2<br>020-11444、CVE-2020-10204、CVE-2020-10199、CVE-2020-1938、CVE-2<br>020-2551、CVE-2020-2555、CVE-2020-2883、CVE-2019-17558、CVE-201<br>9-6340 |
| [CVE-Master](https://github.com/wjl110/CVE-Master) | v1.0.1 | 收集本人自接触渗透测试用于漏洞验证的所有热门CVE、POC、CNVD攻击<br>有效载荷+测试工具+FUZZ,一个仓库满足许多攻击测试场景,开箱即用. |
| [0day](https://github.com/helloexp/0day) |  | 各种CMS、各种平台、各种系统、各种软件漏洞的EXP、POC ,该项目将<br>持续更新 |
| [PocList](https://github.com/1n7erface/PocList) |  | Alibaba-Nacos-Unauthorized/ApacheDruid-RCE_CVE-2021-25646/MS-E<br>xchange-SSRF-CVE-2021-26885/Oracle-WebLogic-CVE-2021-2109_RCE/R<br>G-CNVD-2021-14536/RJ-SSL-VPN-UltraVires/Redis-Unauthorized-RCE/<br>TDOA-V11.7-GetOnlineCookie/VMware-vCenter-GetAnyFile/yongyou-GR<br>P-U8-XXE/Oracle-WebLogic-CVE-2020-14883/Oracle-WebLogic-CVE-202<br>0-14882/Apache-Solr-GetAnyFile/F5-BIG-IP-CVE-2021-22986/Sonicwa<br>ll-SSL-VPN-RCE/GitLab-Graphql-CNVD-2021-14193/D-Link-DCS-CVE-20<br>20-25078/WLAN-AP-WEA453e-RCE/360TianQing-Unauthorized/360TianQi<br>ng-SQLinjection/FanWeiOA-V8-SQLinjection/QiZhiBaoLeiJi-AnyUserL<br>ogin/QiAnXin-WangKangFirewall-RCE/金山-V8-终端安全系统/NCCloud-<br>SQLinjection/ShowDoc-RCE |
| [vulnerability](https://github.com/lal0ne/vulnerability) |  | 收集、整理、修改互联网上公开的漏洞POC |
| [Some-PoC-oR-ExP](https://github.com/coffeehb/Some-PoC-oR-ExP) |  | 各种漏洞poc、Exp的收集或编写 |
| [POChouse](https://github.com/DawnFlame/POChouse) |  | POC&EXP仓库、hvv弹药库、Nday、1day |
| [PocOrExp_in_Githu<br>b](https://github.com/ycdxsb/PocOrExp_in_Github) |  | 聚合Github上已有的Poc或者Exp，CVE信息来自CVE官网。Auto Collect<br> Poc Or Exp from Github by CVE ID. |
### 信息泄露漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [cf](https://github.com/teamssix/cf) | v0.5.0 | Cloud Exploitation Framework 云环境利用框架，方便安全人员在获<br>得 AK 的后续工作 |
| [Cloud-Bucket-Leak<br>-Detection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | v0.4.0 | 六大云存储，泄露利用检测工具 |
| [AliyunAccessKeyTo<br>ols](https://github.com/NS-Sp4ce/AliyunAccessKeyTools) | 1.0 | 阿里云AccessKey泄漏利用工具 |
### 漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [slowhttptest](https://github.com/shekyan/slowhttptest) | v1.9.0 | Application Layer DoS attack simulator |
### WEB漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SSTImap](https://github.com/vladko312/SSTImap) | v1.1 | Automatic SSTI detection tool with interactive interface |
| [tplmap](https://github.com/epinna/tplmap) | v0.5 | Server-Side Template Injection and Code Injection Detection an<br>d Exploitation Tool |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | 1.7 | Automatic SQL injection and database takeover tool |
| [ghauri](https://github.com/r0oth3x49/ghauri) | 1.2.2 | An advanced cross-platform tool that automates the process of <br>detecting and exploiting SQL injection security flaws |
### 服务漏洞利用
#### RMI
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [attackRmi](https://github.com/waderwu/attackRmi) | v0.1 | attackRmi |
| [attackRmi](https://github.com/A-D-Team/attackRmi) | v2.0 |  |
| [BaRMIe](https://github.com/NickstaDB/BaRMIe) | v1.01 | Java RMI enumeration and attack tool. |
| [rmiscout](https://github.com/BishopFox/rmiscout) | v1.4 | RMIScout uses wordlist and bruteforce strategies to enumerate <br>Java RMI functions and exploit RMI parameter unmarshalling vuln<br>erabilities |
#### JDWP
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jdwp-shellifier](https://github.com/IOActive/jdwp-shellifier) |  |  |
## 漏洞文库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [bylibrary](https://github.com/BaizeSec/bylibrary) |  | 白阁文库是白泽Sec安全团队维护的一个漏洞POC和EXP公开项目 |
| [PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book) | PeiQi-W<br>IKI-Book<br>-2022-03<br>-20 | 面向网络安全从业者的知识文库🍃 |
| [VulWiki](https://github.com/Ares-X/VulWiki) |  | VulWiki |
| [vulbase](https://github.com/cckuailong/vulbase) |  | 各大漏洞文库合集 |
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC) |  | 一个各类漏洞POC知识库 |
| [Vulnerability-Wik<br>i](https://github.com/Threekiii/Vulnerability-Wiki) | v1.0 | 一个基于 docsify 的综合漏洞知识库，目前漏洞数量 900+ |
| [yougar0.github.io](https://github.com/heise5yuetian/yougar0.github.io) |  | 漏洞知识库 |
| [Vulhub-Reproduce](https://github.com/Threekiii/Vulhub-Reproduce) |  | 一个Vulhub漏洞复现知识库 |
| [Report_Public](https://github.com/DVPNET/Report_Public) |  |  DVPNET 公开漏洞知识库 |
| [BUG-Pocket](https://github.com/light-Life/BUG-Pocket) |  | 小型漏洞库，提供FOFA语法及批量脚本，具体利用法请参考别的漏洞库<br>，共4种类型47项 |
| [WiKi](https://github.com/ScarecrowSec/WiKi) |  | 稻草人安全团队漏洞库 |
| [PoC-ExP](https://github.com/Cuerz/PoC-ExP) |  | 【漏洞Poc知识库】一个网络安全爱好者对网络上一些已知漏洞payload<br>的收录，持续更新。并编写了利用脚本，可用于日常学习或批量的src漏<br>洞挖掘 |
| [FrameVul](https://github.com/Awrrays/FrameVul) |  | POC集合，框架nday漏洞利用 |
## 权限维持
### Shell管理
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Behinder](https://github.com/rebeyond/Behinder) | Behinde<br>r_v4.0.6 | “冰蝎”动态二进制加密网站管理客户端 |
| [Godzilla](https://github.com/BeichenDream/Godzilla) | v4.0.1-<br>godzilla | 哥斯拉 |
| [antSword](https://github.com/AntSwordProject/antSword) | 2.1.15 | 中国蚁剑是一款跨平台的开源网站管理工具。AntSword is a cross-pl<br>atform website management toolkit. |
| [Platypus](https://github.com/WangYihang/Platypus) | v1.5.0 | :hammer: A modern multiple reverse shell sessions manager writ<br>ten in go |
| [As-Exploits](https://github.com/yzddmr6/As-Exploits) |  | 中国蚁剑后渗透框架 |
### 后门
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CreateHiddenAccou<br>nt](https://github.com/wgpsec/CreateHiddenAccount) | 0.2 | A tool for creating hidden accounts using the registry || 一个<br>使用注册表创建隐藏帐户的工具 |
### 远控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [noterce](https://github.com/xiao-zhu-zhu/noterce) | 1.3 | 一种另辟蹊径的免杀执行系统命令的木马 |
| [Supershell](https://github.com/tdragon6/Supershell) | latest | Supershell C2 远控平台，基于反向SSH隧道获取完全交互式Shell |
| [SimpleRemoter](https://github.com/yuanyuanxiang/SimpleRemoter) | v1.0.0.<br>5 | 基于gh0st的远程控制器：实现了终端管理、进程管理、窗口管理、远<br>程桌面、文件管理、语音管理、视频管理、服务管理、注册表管理等功能<br>，优化全部代码及整理排版，修复内存泄漏缺陷，程序运行稳定。项目代<br>码仅限于学习和交流用途。 |
### 免杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shellcodeloader](https://github.com/knownsec/shellcodeloader) | v1.1 | shellcodeloader |
| [AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool) | 2023041<br>7 | 掩日 - 免杀执行器生成工具 |
| [GobypassAV-shellc<br>ode](https://github.com/Pizz33/GobypassAV-shellcode) |  | 免杀shellcode加载器，使用go实现，免杀bypass火绒、360、核晶、de<br>f等主流杀软 |
| [ZheTian](https://github.com/yqcs/ZheTian) | v3 | ::ZheTian / 强大的免杀生成工具，Bypass All. |
## 权限提升
### windows提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BadPotato](https://github.com/BeichenDream/BadPotato) |  | Windows 权限提升 BadPotato |
| [Windows-exploits](https://github.com/lyshark/Windows-exploits) | Windows<br>Exploits<br>Collecti<br>ons | Windows 平台提权漏洞大合集，长期收集各种提权漏洞利用工具。    <br>    A large collection of rights raising vulnerabilities on the<br> windows platform, which collects various rights raising vulner<br>ability utilization tools for a long time. |
### linux提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dirtycow](https://github.com/firefart/dirtycow) |  | Dirty Cow exploit - CVE-2016-5195 |
| [traitor](https://github.com/liamg/traitor) | v0.0.14 | :arrow_up: :skull_and_crossbones: :fire: Automatic Linux prive<br>sc via exploitation of low-hanging fruit e.g. gtfobins, pwnkit,<br> dirty pipe, +w docker.sock |
| [LinEnum](https://github.com/rebootuser/LinEnum) |  | Scripted Local Linux Enumeration & Privilege Escalation Checks |
| [PEASS-ng](https://github.com/carlospolop/PEASS-ng) | 2023070<br>2-bc7ce3<br>ac | PEASS - Privilege Escalation Awesome Scripts SUITE (with color<br>s) |
| [traitor](https://github.com/liamg/traitor) | v0.0.14 | :arrow_up: :skull_and_crossbones: :fire: Automatic Linux prive<br>sc via exploitation of low-hanging fruit e.g. gtfobins, pwnkit,<br> dirty pipe, +w docker.sock |
### 容器提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [container-escape-<br>check](https://github.com/teamssix/container-escape-check) | v0.3 | docker container escape check || Docker 容器逃逸检测 |
| [CDK](https://github.com/cdk-team/CDK) | v1.5.2 | 📦  Make security testing of K8s, Docker, and Containerd easie<br>r. |
## 内网渗透
### 免杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shellcodeloader](https://github.com/knownsec/shellcodeloader) | v1.1 | shellcodeloader |
| [AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool) | 2023041<br>7 | 掩日 - 免杀执行器生成工具 |
### 代理转发
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [reGeorg](https://github.com/sensepost/reGeorg) |  | The successor to reDuh, pwn a bastion webserver and create SOC<br>KS proxies through the DMZ. Pivot and pwn. |
| [Stowaway](https://github.com/ph4ntonn/Stowaway) | v2.1 | 👻Stowaway -- Multi-hop Proxy Tool for pentesters |
| [PortForward](https://github.com/knownsec/PortForward) | 0.5.0 | The port forwarding tool developed by Golang solves the proble<br>m that the internal and external networks cannot communicate in<br> certain scenarios |
### 密码提取
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [getIntrInfo](https://github.com/Potato-py/getIntrInfo) |  | 收集内部网信息。包括：浏览器书签、密码和浏览历史记录、cookie。<br>Wifi信息和密码。主机信息。 |
| [FinalShell-Decode<br>r](https://github.com/passer-W/FinalShell-Decoder) | V1.0 | FinallShell 密码解密GUI工具 |
| [Xdecrypt](https://github.com/dzxs/Xdecrypt) |  | Xshell Xftp password decrypt |
| [HackBrowserData](https://github.com/moonD4rk/HackBrowserData) | v0.4.4 | Decrypt passwords/cookies/history/bookmarks from the browser. <br>一款可全平台运行的浏览器数据导出解密工具。 |
| [SharpDecryptPwd](https://github.com/ianxtianxt/SharpDecryptPwd) |  | Windows常用程序密码读取工具：SharpDecryptPwd |
### 漏洞发现
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InScan](https://github.com/inbug-team/InScan) |  | 边界打点后的自动化渗透工具 |
| [kscan](https://github.com/lcvvvv/kscan) | v1.85 | Kscan是一款纯go开发的全方位扫描器，具备端口扫描、协议检测、指<br>纹识别，暴力破解等功能。支持协议1200+，协议指纹10000+，应用指纹2<br>0000+，暴力破解协议10余种。 |
| [fscan](https://github.com/shadow1ng/fscan) | 1.8.2 | 一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。 |
| [Gscan](https://github.com/hack2fun/Gscan) | v1.0 | Gscan is a high concurrency scanner based on golang |
| [ServerScan](https://github.com/Adminisme/ServerScan) | v1.0.2 | ServerScan一款使用Golang开发的高并发网络扫描、服务探测工具。 |
| [ADCSKiller](https://github.com/grimlockx/ADCSKiller) |  | An ADCS Exploitation Automation Tool Weaponizing Certipy and C<br>oercer |
### 漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Viper](https://github.com/FunnyWolf/Viper) | v1.6.1 | Redteam operation  platform with webui 图形化红队行动辅助平台 |
### 横向工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WMIHACKER](https://github.com/rootclay/WMIHACKER) |  | A Bypass Anti-virus Software Lateral Movement Command Executio<br>n Tool |
| [sharpwmi](https://github.com/QAX-A-Team/sharpwmi) | v2 | sharpwmi是一个基于rpc的横向移动工具，具有上传文件和执行命令功<br>能。 |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Ladon](https://github.com/k8gege/Ladon) | v11.0 | Ladon大型内网渗透工具，可PowerShell模块化、可CS插件化、可内存<br>加载，无文件扫描。含端口扫描、服务识别、网络资产探测、密码审计、<br>高危漏洞检测、漏洞利用、密码读取以及一键GetShell，支持批量A段/B<br>段/C段以及跨网段扫描，支持URL、主机、域名列表扫描等。Ladon 11.0<br>内置234个功能,网络资产探测模块32个通过多种协议(ICMP\NBT\DNS\MAC\<br>SMB\WMI\SSH\HTTP\HTTPS\Exchange\mssql\FTP\RDP)以及方法快速获取<br>目标网络存活主机IP、计算机名、工作组、共享资源、网卡地址、操作系<br>统版本、网站、子域名、中间件、开放服务、路由器、交换机、数据库、<br>打印机等信息，高危漏洞检测16个含MS17010、Zimbra、Exchange |
## 社会工程学
### 钓鱼辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EmailSender](https://github.com/A10ha/EmailSender) |  | 钓鱼邮件便捷发送工具（GUI） |
## 相关资源
### 工具集成环境
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite<br>-toolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必<br>先利其器。 |
| [CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools) |  | 渊龙Sec安全团队CTF&AWD工具箱 |
| [PenKitGui](https://github.com/ccc-f/PenKitGui) |  | 渗透测试武器库 |
| [Taie-RedTeam-OS](https://github.com/taielab/Taie-RedTeam-OS) |  | 泰阿安全实验室-基于XUbuntu私人订制的红蓝对抗渗透操作系统 |
| [FreeGui](https://github.com/tyB-or/FreeGui) | v2.5 | freeGui：基于ttkbootstrap开发的一款用来管理自己的渗透测试工具<br>的一个小工具，并提供一些实用小功能，例如打开目录，运行工具，工具<br>备忘命令。 |
| [GUI_Tools](https://github.com/ghealer/GUI_Tools) | V1.1 | 一个由各种图形化渗透工具组成的工具集 |
| [Pentest-Windows](https://github.com/arch3rPro/Pentest-Windows) | v2.1 | Windows11 Penetration Suite Toolkit |
| [ApoalypseSecTools](https://github.com/ApocalypseSec/ApoalypseSecTools) |  | ApoalypseSecTool更新地址 |
### 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite<br>-toolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必<br>先利其器。 |
| [Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam) |  | 一个红队知识仓库 |
| [Threathunting-boo<br>k](https://github.com/12306Bro/Threathunting-book) |  |  |
| [PenetrationTestti<br>ps](https://github.com/CYJoe-Cyclone/PenetrationTesttips) |  | 渗透测试Tips - Version1.3 |
| [Intranet_Penetrat<br>ion_Tips](https://github.com/Ridter/Intranet_Penetration_Tips) |  | 2018年初整理的一些内网渗透TIPS，后面更新的慢，所以整理出来希望<br>跟小伙伴们一起更新维护~ |
| [Vuln-List](https://github.com/wwl012345/Vuln-List) |  | (持续更新)对网上出现的各种OA、中间件、CMS等漏洞进行整理，主要<br>包括漏洞介绍、漏洞影响版本以及漏洞POC/EXP等，并且会持续更新。 |
### 优秀项目集合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [404StarLink](https://github.com/knownsec/404StarLink) |  | 404StarLink - 推荐优质、有意义、有趣、坚持维护的安全开源项目 |
| [Scanners-Box](https://github.com/We5ter/Scanners-Box) |  | A powerful and open-source toolkit for hackers and security au<br>tomation - 安全行业从业者自研开源扫描器合辑 |
| [All-Defense-Tool](https://github.com/guchangan1/All-Defense-Tool) |  | 本项目集成了全网优秀的攻防武器工具项目，包含自动化利用，子域名<br>、目录扫描、端口扫描等信息收集工具，各大中间件、cms漏洞利用工具<br>，爆破工具、内网横向及免杀、社工钓鱼以及应急响应等资料。 |
| [About-Attack](https://github.com/lintstar/About-Attack) |  | 一个旨在通过应用场景 / 标签对 Github 红队向工具 / 资源进行分类<br>收集，降低红队技术门槛的手册【持续更新】 |
| [RedTeamTools](https://github.com/FiveAourThe/RedTeamTools) |  | 分享红队常用的工具 |
### 代理池
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [go_proxy_pool](https://github.com/pingc0y/go_proxy_pool) | 2022.11<br>.22 | 无环境依赖开箱即用的代理IP池 |
| [rotateproxy](https://github.com/akkuman/rotateproxy) | v0.7.2 | 利用fofa搜索socks5开放代理进行代理池轮切的工具 |
| [Gofreeproxy](https://github.com/ja9er/Gofreeproxy) | v0.1 | 自用的动态代理小工具 |
| [ProxyPoolxSocks](https://github.com/Anyyy111/ProxyPoolxSocks) | v1.2 | ☁️Socks代理池服务端自动化搭建工具☁️ |
| [proxyServer](https://github.com/safe6Sec/proxyServer) | v1.0 | 本项目其实就是个简单的代理服务器，把代理池集成进来来了。 |
| [proxy_pool](https://github.com/jhao104/proxy_pool) | 2.4.1 | Python爬虫代理IP池(proxy pool) |
### 工具集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [K8tools](https://github.com/k8gege/K8tools) |  | K8工具合集(内网渗透/提权工具/远程溢出/漏洞利用/扫描工具/密码破<br>解/免杀工具/Exploit/APT/0day/Shellcode/Payload/priviledge/Bypass<br>UAC/OverFlow/WebShell/PenTest) Web GetShell Exploit(Struts2/Zim<br>bra/Weblogic/Tomcat/Apache/Jboss/DotNetNuke/zabbix) |
## 工具周边
### Burpsuite
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [PowerScanner](https://github.com/NeoTheCapt/PowerScanner) | 1.1.3 | 面向HW的红队半自动扫描器 |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | RouteVu<br>lScan1.5 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的<br>burp插件 |
| [SpringScan](https://github.com/metaStor/SpringScan) | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [BurpSuite-collect<br>ions](https://github.com/Mr-xn/BurpSuite-collections) |  | 有关burpsuite的插件(非商店),文章以及使用技巧的收集(此项目不再<br>提供burpsuite破解文件,如需要请在博客mrxn.net下载)---Collection o<br>f burpsuite plugins (non-stores), articles and tips for using B<br>urpsuite, no crack version file |
| [BurpShiroPassiveS<br>can](https://github.com/pmiaowu/BurpShiroPassiveScan) | BurpShi<br>roPassiv<br>eScan-2.<br>0.0 | 一款基于BurpSuite的被动式shiro检测插件 |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | BurpFas<br>tJsonSca<br>n-2.2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [HaE](https://github.com/gh0stkey/HaE) | 2.4.6 | HaE - Highlighter and Extractor, 赋能白帽 高效作战 |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9 | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集<br>；快速Title获取；外部工具联动；等等 |
| [Sylas](https://github.com/Acmesec/Sylas) | 1.1.1 | 新一代子域名主/被动收集工具 - Subdomain automatic/passive coll<br>ection tool |
| [GadgetProbe](https://github.com/BishopFox/GadgetProbe) | v1.0 | Probe endpoints consuming Java serialized objects to identify <br>classes, libraries, and library versions on remote Java classpa<br>ths. |
| [HopLa](https://github.com/synacktiv/HopLa) | 1.2 |  HopLa Burp Suite Extender plugin -  Adds autocompletion suppo<br>rt and useful payloads in Burp Suite |
| [captcha-killer-mo<br>dified](https://github.com/f0ng/captcha-killer-modified) | 0.24.1 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免<br>费ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, s<br>upport AES/RSA/DES/ExecJs(execute JS encryption code in burpsui<br>te). 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSu<br>ite插件 |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.30 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等<br>），类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础<br>上，不影响APP、网站加解密正常逻辑等。 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [AutoRepeater](https://github.com/nccgroup/AutoRepeater) |  | Automated HTTP Request Repeating With Burp Suite |
| [http-request-smug<br>gler](https://github.com/portswigger/http-request-smuggler) |  |  |
| [burp-requests](https://github.com/silentsignal/burp-requests) | v0.2.4 | Copy as requests plugin for Burp Suite |
| [CORSScanner](https://github.com/zzzskd/CORSScanner) |  | CORS 跨域漏洞 burp 插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) |  |  |
| [HostHeaderAttack](https://github.com/weujieytt/HostHeaderAttack) | 0.1.1 | 检测host头攻击的Burpsuite被动扫描插件，Burpsuite passive scann<br>ing plugin responsible for detecting host header attack |
| [knife](https://github.com/bit4woo/knife) | v2.2 | A burp extension that add some useful function to  Context Men<br>u 添加一些右键菜单让burp用起来更顺畅 |
| [log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner) | 0.25.0 | CVE-2021-44228 Log4j2 BurpSuite Scanner,Customize ceye.io api <br>or other apis,including internal networks |
| [passive-scan-clie<br>nt](https://github.com/c0ny1/passive-scan-client) | 0.3.1 | Burp被动扫描流量转发插件 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpSuiteCn](https://github.com/funkyoummp/BurpSuiteCn) |  |  |
| [NEW_xp_CAPTCHA](https://github.com/smxiazi/NEW_xp_CAPTCHA) | 4.2 | xp_CAPTCHA(瞎跑 白嫖版) burp 验证码 识别 burp插件 |
| [npscrack](https://github.com/weishen250/npscrack) | npscrac<br>k-1.0 | 蓝队利器、溯源反制、NPS 漏洞利用、NPS exp、NPS poc、Burp插件、<br>一键利用 |
| [OneScan](https://github.com/vaycore/OneScan) | v1.1.0 | OneScan是递归目录扫描的BurpSuite插件 |
| [OutLook](https://github.com/KrystianLi/OutLook) |  |  |
| [passive-scan-clie<br>nt-plus](https://github.com/winezer0/passive-scan-client-plus) | v0.4.12<br>.0 | burpsuite passive-scan-client 插件维护分支 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpCRLFScan](https://github.com/A0WaQ4/BurpCRLFScan) | 1.4 | 使用java编写的CRLF-Injection-burp被动扫描插件 |
| [JsonDetect](https://github.com/a1phaboy/JsonDetect) | v1.0 | A burp Extender to detect json, include fastjson,jackson,gson |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.30 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等<br>），类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础<br>上，不影响APP、网站加解密正常逻辑等。 |
| [burp-text4shell](https://github.com/silentsignal/burp-text4shell) | v0.1 | Text4Shell scanner for Burp Suite |
| [sweetPotato](https://github.com/z2p/sweetPotato) | version<br>1.6 | 基于burpsuite的资产分析工具 |
| [xia_Liao](https://github.com/smxiazi/xia_Liao) | 1.6 | xia Liao（瞎料）burp插件 用于Windows在线进程/杀软识别 与 web渗<br>透注册时，快速生成需要的资料用来填写，资料包含：姓名、手机号、身<br>份证、统一社会信用代码、组织机构代码、银行卡，以及各类web语言的h<br>ello world输出和生成弱口令字典等。 |
| [base64encode](https://github.com/handbye/base64encode) | 1.0 | burpsuite POST数据包base64编码插件 |
| [HackTools](https://github.com/Vicl1fe/HackTools) | 1.5 | 提高渗透测试效率。#Burp插件##渗透测试##小工具# |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | RouteVu<br>lScan1.5 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的<br>burp插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) |  |  |
| [burp-awesome-tls](https://github.com/sleeyax/burp-awesome-tls) | v1.1.0 | Fix Burp Suite's poor TLS stack and bypass WAFs by spoofing an<br>y browser |
| [JustC2file](https://github.com/Peithon/JustC2file) | v1.0.2 | Burp插件，Malleable C2 Profiles生成器；可以通过Burp代理选中请<br>求，生成Cobalt Strike的profile文件(CSprofile) |
| [SpringScan](https://github.com/metaStor/SpringScan) | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [captcha-killer-mo<br>dified](https://github.com/f0ng/captcha-killer-modified) | 0.24.1 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免<br>费ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | BurpFas<br>tJsonSca<br>n-2.2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [Log4j-check](https://github.com/bigsizeme/Log4j-check) |  | log4J burp被扫插件、CVE-2021-44228、支持dnclog.cn和burp内置DNS<br>、可配合JNDIExploit生成payload |
| [Log4j2Scan](https://github.com/whwlsfb/Log4j2Scan) | V0.13.1 | Log4j2 RCE Passive Scanner plugin for BurpSuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, s<br>upport AES/RSA/DES/ExecJs(execute JS encryption code in burpsui<br>te). 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSu<br>ite插件 |
| [BurpBountyPlus](https://github.com/ggg4566/BurpBountyPlus) | 3 | BurpBounty 魔改版本 |
| [BurpExtractor](https://github.com/NetSPI/BurpExtractor) | v1.3.4 | A Burp extension for generic extraction and reuse of data with<br>in HTTP requests and responses. |
| [burp-cph](https://github.com/elespike/burp-cph) | 3.0 | Custom Parameter Handler extension for Burp Suite. |
| [BurpJSLinkFinder](https://github.com/InitRoot/BurpJSLinkFinder) |  | Burp Extension for a passive scanning JS files for endpoint li<br>nks. |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9 | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集<br>；快速Title获取；外部工具联动；等等 |
| [JC-AntiToken](https://github.com/chroblert/JC-AntiToken) |  | burp插件：python版，token防重放绕过 |
| [BurpSuite_403Bypa<br>sser](https://github.com/sting8k/BurpSuite_403Bypasser) |  | Burpsuite Extension to bypass 403 restricted directory |
| [Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension) | v1.7.1 | Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suit<br>e. |
| [Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension) | v1.7.1 | Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suit<br>e. |
| [shiro-check](https://github.com/bigsizeme/shiro-check) | shiroch<br>ek3.0 | Shiro反序列化回显利用、内存shell、检查 Burp插件 |
| [FastjsonScan](https://github.com/Maskhe/FastjsonScan) | 1.0 | 一个简单的Fastjson反序列化检测burp插件 |
| [fastjsonScan](https://github.com/zilong3033/fastjsonScan) |  | fastjson漏洞burp插件，检测fastjson<1.2.68基于dnslog，fastjson<<br>=1.2.24和1.2.33<=fatjson<=1.2.47的不出网检测和TomcatEcho,Spring<br>Echo回显方案。 |
| [BurpSuite-Extende<br>r-fastjson](https://github.com/uknowsec/BurpSuite-Extender-fastjson) |  | Reference：https://www.w2n1ck.com/article/44/ |
| [BurpSuite-Xkeys](https://github.com/vsec7/BurpSuite-Xkeys) |  | A Burp Suite Extension to extract interesting strings (key, se<br>cret, token, or etc.) from a webpage. |
| [Burp_AES_Plugin](https://github.com/jas502n/Burp_AES_Plugin) |  | Burpsuite Plugin For AES Crack |
| [burpJsEncrypter](https://github.com/TheKingOfDuck/burpJsEncrypter) | 0.1 | More Easier Burp Extension To Solve Javascript Front End Encry<br>ption,一款更易使用的解决前端加密问题的Burp插件。 |
| [burp-requests](https://github.com/silentsignal/burp-requests) | v0.2.4 | Copy as requests plugin for Burp Suite |
| [captcha-killer](https://github.com/c0ny1/captcha-killer) | 0.1.2 | burp验证码识别接口调用插件 |
| [BurpSuiteHTTPSmug<br>gler](https://github.com/nccgroup/BurpSuiteHTTPSmuggler) | v0.1 | A Burp Suite extension to help pentesters to bypass WAFs or te<br>st their effectiveness using a number of techniques |
| [sqlmap4burp-plus-<br>plus](https://github.com/c0ny1/sqlmap4burp-plus-plus) | 0.2 | sqlmap4burp++是一款兼容Windows，mac，linux多个系统平台的Burp与<br>sqlmap联动插件 |
| [passive-scan-clie<br>nt](https://github.com/c0ny1/passive-scan-client) | 0.3.1 | Burp被动扫描流量转发插件 |
| [domain_hunter](https://github.com/bit4woo/domain_hunter) | v1.5 | A Burp Suite Extension that try to find all sub-domain, simila<br>r-domain and related-domain of an organization automatically! <br>基于流量自动收集整个企业或组织的子域名、相似域名、相关域名的burp<br>插件 |
| [reCAPTCHA/blob](https://github.com/bit4woo/reCAPTCHA/blob) |  |  |
| [BurpSuiteLoggerPl<br>usPlus](https://github.com/nccgroup/BurpSuiteLoggerPlusPlus) |  |  |
| [HackBar](https://github.com/d3vilbug/HackBar) | 2.0 | HackBar plugin for Burpsuite |
| [chunked-coding-co<br>nverter](https://github.com/c0ny1/chunked-coding-converter) | 0.4.0 | Burp suite 分块传输辅助插件 |
| [TsojanScan](https://github.com/Tsojan/TsojanScan) | v1.4.4 | 一个集成的BurpSuite漏洞探测插件 |
| [burp-api-drops](https://github.com/bit4woo/burp-api-drops) |  | burp插件开发指南 |
| [semgrepper](https://github.com/gand3lf/semgrepper) | v1.3 | An extension to use Semgrep inside Burp Suite. |
### xray
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [yarx](https://github.com/zema1/yarx) | v0.2.0 | An awesome reverse engine for xray poc. | 一个自动化根据 xray <br>poc 生成对应靶站的工具 |
| [xray-poc-generati<br>on](https://github.com/phith0n/xray-poc-generation) |  | 🧬 辅助生成 XRay YAML POC |
| [super-xray](https://github.com/4ra1n/super-xray) | 1.7 | Web漏洞扫描工具XRAY的GUI启动器 |
| [Xray_Cracked](https://github.com/NHPT/Xray_Cracked) | v1.9.11 | Update Xray1.9.11 Cracked for Windows,Linux and Mac OS. |
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
| [fofa_view](https://github.com/fofapro/fofa_view) | v0.0.5 | FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件，目前兼容  Chr<br>ome、Firefox、Opera。 |
| [mitaka](https://github.com/ninoseki/mitaka) | v1.3.0 | A browser extension for OSINT search |
| [anti-honeypot](https://github.com/cnrstar/anti-honeypot) |  | 一款可以检测WEB蜜罐并阻断请求的Chrome插件 |
| [Chromium-based-XS<br>S-Taint-Tracking](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) | v0.3 | Cyclops 是一款具有 XSS 检测功能的浏览器 |
| [Zoomeye-Tools](https://github.com/knownsec/Zoomeye-Tools) |  | Zoomeye Tools是配合Zoomeye使用的Chrome插件 |
| [Heimdallr](https://github.com/graynjo/Heimdallr) |  |  |
| [superSearchPlus](https://github.com/dark-kingA/superSearchPlus) |  | 谷歌插件版本- superSearchPlus是聚合型信息收集插件，支持综合查<br>询，资产测绘查询，信息收集 敏感信息提取 js资源扫描 目录扫描 vue<br>组件扫描 整合了目前常见的资产测绘平台 同时支持数据导出 |
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
| [nucleix](https://github.com/mlq574/nucleix) |  | 整合nuclei与xray(社区版、自带高级版)，实现被动扫描+poc扫描自动<br>化渗透流程 |
| [nuclei-plus](https://github.com/Yong-An-Dang/nuclei-plus) | v7.0.0 | Functional enhancement based on nuclei |
### nessus
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [NessusToReport](https://github.com/Hypdncy/NessusToReport) | v1.2 | Nessus扫描报告自动化生成工具 |
| [NessusReportInChi<br>nese](https://github.com/FunnyKun/NessusReportInChinese) |  | 半自动化将 Nessus 英文报告（csv格式）生成中文 excel ，中文漏洞<br>库已有700多条常见漏洞，后续再进一步加上新漏洞自动翻译，实现全自<br>动化 |
| [CN_Nessus_Plugins<br>_Interface](https://github.com/nszy007/CN_Nessus_Plugins_Interface) | 1 | nessus插件中文查询接口 |
| [docker_nessus_unl<br>imited](https://github.com/xxcdd/docker_nessus_unlimited) |  | docker build nessus with unlimited ip |
| [nessus_api](https://github.com/starnightcyber/nessus_api) |  | Nessus REST API 封装 |
| | | [nessus下载地址](https://www.tenable.com/downloads/nessus?loginAttempted=true) |
### rsas
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [nsfocus-rsas-know<br>ledge-base](https://github.com/biggerwing/nsfocus-rsas-knowledge-base) |  | 绿盟科技漏洞扫描器(RSAS)漏洞库 |
| [RSAS-Data-Export](https://github.com/autoing/RSAS-Data-Export) | 2022-9-<br>9 | 绿盟极光远程安全评估系统(RSAS)-RSAS漏洞数据导出工具 |
| [RSAS-Task-Release](https://github.com/autoing/RSAS-Task-Release) | v1.0 | 绿盟极光远程安全评估系统(RSAS)-RSAS批量下任务工具 |
### arl
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ARL-Finger-ADD](https://github.com/loecho-sec/ARL-Finger-ADD) |  | 灯塔（最新版）指纹添加脚本！ |
### cobaltstrike
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [taowu-cobalt-stri<br>ke](https://github.com/pandasec888/taowu-cobalt-strike) |  |  |
| [geacon_pro](https://github.com/H4de5-7/geacon_pro) |  |  |
| [SharkExec](https://github.com/F3eev/SharkExec) |  | 内网渗透|红队工具|C#内存加载|cobaltstrike |
| [LSTAR](https://github.com/lintstar/LSTAR) | v2.1 | LSTAR - CobaltStrike 综合后渗透插件 |
### ZoomEye
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Kunyu](https://github.com/knownsec/Kunyu) | v1.7.2 | Kunyu, more efficient corporate asset collection |
| [ZoomEye-python](https://github.com/knownsec/ZoomEye-python) | v2.2.0 | ZoomEye-python: The official Python library and CLI by Knownse<br>c 404 Team. |
| [ZoomEye-go](https://github.com/gyyyy/ZoomEye-go) | v1.5 | The Golang SDK and CLI of ZoomEye@Knownsec by gyyyy. |
### frida
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [frida-skeleton](https://github.com/Margular/frida-skeleton) | v2.0.0 | 基于frida的安卓hook框架，提供了很多frida自身不支持的功能，将ho<br>ok安卓变成简单便捷，人人都会的事情 |
### fofa
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [fofax](https://github.com/xiecat/fofax) | v0.1.44 | fofax is a command line query tool based on the API of https:/<br>/fofa.info/, simple is the best! |
| [fofa_viewer](https://github.com/wgpsec/fofa_viewer) | 1.1.13 | A simple FOFA client written in JavaFX.  Made by WgpSec, Maint<br>ained by f1ashine. |
| [fofa_GUI](https://github.com/20142995/fofa_GUI) | v1.0.0 |  |
### frp
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [frpCracker](https://github.com/SleepingBag945/frpCracker) | v0.1 | 一款golang编写的，批量检测frp server未授权访问、弱token的工具 |
# CTF
## 杂项
### 图片隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegsolve](https://github.com/Giotino/stegsolve) | v1.4 |  |
| [BlindWatermark](https://github.com/ww23/BlindWatermark) | v0.0.3 | Java 盲水印 |
| [cloacked-pixel](https://github.com/livz/cloacked-pixel) |  | LSB steganography and detection |
| [CTFpics](https://github.com/RetrO-hash/CTFpics) |  |  |
| [ImageStrike](https://github.com/zR00t1/ImageStrike) | V0.2 | ImageStrike是一款用于CTF中图片隐写的综合利用工具 |
| [stegpy](https://github.com/dhsdshdhk/stegpy) |  | Simple steganography program based on the LSB method. |
| [steganography](https://github.com/7thSamurai/steganography) |  | Simple C++ Image Steganography tool to encrypt and hide files <br>insde images using Least-Significant-Bit encoding. |
### 流量分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [UsbMiceDataHacker](https://github.com/WangYihang/UsbMiceDataHacker) |  | USB鼠标流量包取证工具 , 主要用于绘制鼠标移动以及拖动轨迹 |
| [UsbKeyboardDataHa<br>cker](https://github.com/WangYihang/UsbKeyboardDataHacker) |  | USB键盘流量包取证工具 , 用于恢复用户的击键信息 |
### 编码解码
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [TomatoTools](https://github.com/ht0Ruial/TomatoTools) | v1.0.2 | TomatoTools 一款CTF杂项利器，支持36种常见编码和密码算法的加密<br>和解密，31种密文的分析和识别，支持自动提取flag，自定义插件等。 |
| [CyberChef](https://github.com/gchq/CyberChef) | v10.4.0 | The Cyber Swiss Army Knife - a web app for encryption, encodin<br>g, compression and data analysis |
### 取证分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pyvmx-cracker](https://github.com/axcheron/pyvmx-cracker) |  | Simple tool to crack VMware VMX encryption passwords |
| [chatViewTool](https://github.com/Ormicron/chatViewTool) | BEAT | 基于Java实现的图形化微信聊天记录解密查看器 |
| [Sharp-dumpkey](https://github.com/Ormicron/Sharp-dumpkey) | 1 | 基于C#实现的获取微信数据库密钥的小工具 |
| [Sunflower_get_Pas<br>sword](https://github.com/wafinfo/Sunflower_get_Password) |  | 一款针对向日葵的识别码和验证码提取工具 |
| [SharpWxDump](https://github.com/AdminTest0/SharpWxDump) |  | 微信客户端取证，可获取用户个人信息(昵称/账号/手机/邮箱/数据库<br>密钥(用来解密聊天记录))；支持获取多用户信息，不定期更新新版本偏<br>移，目前支持所有新版本、正式版本 |
| [GoWxDump](https://github.com/SpenserCai/GoWxDump) | v1.0.12 | SharpWxDump的Go语言版。微信客户端取证，获取信息(微信号、手机号<br>、昵称)，微信聊天记录分析(Top N聊天的人、统计聊天最频繁的好友排<br>行、关键词列表搜索等) |
### 音频隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dtmf-decoder](https://github.com/ribt/dtmf-decoder) |  | Extract phone numbers from an audio recording of the dial tone<br>s. |
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
| [apachecn-ctf-wiki](https://github.com/apachecn/apachecn-ctf-wiki) |  |  |
## 逆向
### pyc逆向
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegosaurus](https://github.com/AngelKitty/stegosaurus) | 1.0 | A steganography tool for embedding payloads within Python byte<br>code. |
### Java反编译
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [JavaDecompileTool<br>-GUI](https://github.com/MountCloud/JavaDecompileTool-GUI) | V1.2 | Java Decompile Tool GUI-JAVA反编译工具（界面版） |
| [CodeReviewTools](https://github.com/Ppsoft1991/CodeReviewTools) | v1.31 | 通过正则搜索、批量反编译特定Jar包中的class名称 |
## WEB
### 敏感目录
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ctf-wscan](https://github.com/OrangeWatermelon/ctf-wscan) |  | 在kingkaki的项目上进行了修改，改为单线程，可以在任意目录下执行<br>，对重复的请求进行了过滤 |
| [scrabble](https://github.com/denny0223/scrabble) |  | Simple tool to recover .git folder from remote server |
## 密码学
### RSA
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [rsa-wiener-attack](https://github.com/pablocelayes/rsa-wiener-attack) |  | A Python implementation of the Wiener attack on RSA public-key<br> encryption scheme. |
| [RSA](https://github.com/Mr-Aur0ra/RSA) |  |  |
| [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) |  | RSA attack tool (mainly for ctf) - retreive private key from w<br>eak public key and/or uncipher data |
## AWD
### 线下平台
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Cardinal](https://github.com/vidar-team/Cardinal) | v0.7.3 | CTF🚩 AWD (Attack with Defense) 线下赛平台 / AWD platform - 欢<br>迎 Star~ ✨ |
| [H1ve](https://github.com/D0g3-Lab/H1ve) | 1.1.3 | An Easy / Quick / Cheap Integrated Platform |
| [AWD_CTF_Platform](https://github.com/mo-xiaoxi/AWD_CTF_Platform) |  | 一个简单的AWD训练平台 |
| [CTF_AWD_Platform](https://github.com/xuchaoa/CTF_AWD_Platform) |  | CTF 攻防对抗平台 |
| [awd-platform](https://github.com/zhl2008/awd-platform) |  | platform for awd |
| [JJUCTF_V2.0](https://github.com/BJLIYANLIANG/JJUCTF_V2.0) |  | JJU网络安全靶场实训平台 |
### 脚本
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Prepare-for-AWD](https://github.com/admintony/Prepare-for-AWD) |  | AWD攻防赛脚本集合 |
| [AWD-Predator-Fram<br>ework](https://github.com/Ares-X/AWD-Predator-Framework) |  | AWD攻防赛webshell批量利用框架 |
| [awd_attack_framew<br>ork](https://github.com/Wfzsec/awd_attack_framework) |  | awd攻防常用脚本+不死马+crontab+防御方法 |
### 靶场
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [20190511_awd_dock<br>er](https://github.com/glzjin/20190511_awd_docker) |  | 2019 年 5 月 11 日防灾科技学院 “应急挑战杯” 大学生网络安全邀<br>请赛 AWD 靶机题目。 |
| [awd-platform](https://github.com/zhl2008/awd-platform) |  | platform for awd |
| [AWD_CTF_Platform](https://github.com/mo-xiaoxi/AWD_CTF_Platform) |  | 一个简单的AWD训练平台 |
| [AWDDocker](https://github.com/Cl0udG0d/AWDDocker) |  | 标准化AWD靶场Docker |
| [Liaoning-provinci<br>al-competition-tar<br>get-1](https://github.com/yqw1212/Liaoning-provincial-competition-target-1) |  | 第三届辽宁省ctf线下awd靶机1web |
| [wordpress](https://github.com/871339097/wordpress) |  | AWD靶机 |
| [awd-platform](https://github.com/zhl2008/awd-platform) |  | platform for awd |
### 防护
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [AoiAWD](https://github.com/DasSecurity-HatLab/AoiAWD) |  | AoiAWD-专为比赛设计，便携性好，低权限运行的EDR系统。 |
| [CTF-WAF](https://github.com/sharpleung/CTF-WAF) |  | 针对CTF线下赛的通用WAF，日志审计功能。 |
| [k4l0ng_WAF](https://github.com/dr0op/k4l0ng_WAF) |  | A broute detect WAF by PHP using to AWD |
# 应急响应
## web日志分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [DecodeSomeJSPWebs<br>hell](https://github.com/minhangxiaohui/DecodeSomeJSPWebshell) | v1.2 | 冰蝎、哥斯拉 jsp webshell通信流量解密器 |
## 内存马查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shell-analyzer](https://github.com/4ra1n/shell-analyzer) | 0.1 | Java内存马查杀GUI工具，实时动态分析，支持本地和远程查杀 |
## 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Emergency-Respons<br>e-Notes](https://github.com/Bypass007/Emergency-Response-Notes) |  | 应急响应实战笔记，一个安全工程师的自我修养。 |
## 后门查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmTools](https://github.com/RoomaSec/RmTools) |  | 蓝队应急工具 |
# 其他
## 其他
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [faker](https://github.com/joke2k/faker) | v18.13.<br>0 | Faker is a Python package that generates fake data for you. |
| [SmsForwarder](https://github.com/pppscn/SmsForwarder) | v3.2.0 | 短信转发器——监控Android手机短信、来电、APP通知，并根据指定规<br>则转发到其他手机：钉钉群自定义机器人、钉钉企业内机器人、企业微信<br>群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Tel<br>egram机器人、Server酱、PushPlus、手机短信等。包括主动控制服务端<br>与客户端，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。<br>（V3.0 新增）PS.这个APK主要是学习与自用，如有BUG请提ISSUE，同时<br>欢迎大家提PR指正 |
| [dbeaver](https://github.com/dbeaver/dbeaver) | 23.1.2 | Free universal database tool and SQL client |
| [MySQLMonitor](https://github.com/TheKingOfDuck/MySQLMonitor) | 1.0 | MySQL实时监控工具(代码审计/黑盒/白盒审计辅助工具) |
| [flightsim](https://github.com/alphasoc/flightsim) | v2.3.0 | A utility to safely generate malicious network traffic pattern<br>s and evaluate controls. |
## 渗透测试报告辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [APTRS](https://github.com/Anof-cyber/APTRS) |  | Automated Penetration Testing Reporting System |
| [BugRepoter_0x727](https://github.com/0x727/BugRepoter_0x727) |  | BugRepoter_0x727(自动化编写报告平台)根据安全团队定制化协同管理<br>项目安全，可快速查找历史漏洞，批量导出报告。 |
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
| [v2rayA](https://github.com/v2rayA/v2rayA) | v2.0.5 | A web GUI client of Project V which supports V2Ray, Xray, SS, <br>SSR, Trojan and Pingtunnel 🚀 |
| [free](https://github.com/freefq/free) |  | 翻墙、免费翻墙、免费科学上网、免费节点、免费梯子、免费ss/v2ray<br>/trojan节点、蓝灯、谷歌商店、翻墙梯子 |
| [v2rayfree](https://github.com/aiboboxx/v2rayfree) |  | v2ray公益免费节点、最新2ray免费v节点订阅地址、v2ray免费节点每<br>日更新、免费ss/v2ray/trojan节点、freefq  |
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
| [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | v1.3.5 | OCR图片转文字识别软件，完全离线。截屏/批量导入图片，支持多国语<br>言、合并段落、竖排文字。可排除水印区域，提取干净的文本。基于 Pad<br>dleOCR 。 |
## chatgpt
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [chatgpt](https://github.com/LangLangShanDeNanKe/chatgpt) |  | ChatGPT网址导航，分享免费好用AI网站！ |
| [Awesome-ChatGPT](https://github.com/dalinvip/Awesome-ChatGPT) |  | ChatGPT资料汇总学习，持续更新...... |
| [awesome-chatgpt-z<br>h](https://github.com/yzfly/awesome-chatgpt-zh) |  | ChatGPT 中文指南🔥，ChatGPT 中文调教指南，指令指南，应用开发指<br>南，精选资源清单，更好的使用 chatGPT 让你的生产力 up up up! 🚀 |
| [chatgpt-mac](https://github.com/vincelwt/chatgpt-mac) | v0.0.5 | ChatGPT for Mac, living in your menubar. |
| [ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut) |  | 🚀💪Maximize your efficiency and productivity, support for Eng<br>lish, 中文, 日本語, and 한국어. 让生产力加倍的 ChatGPT 快捷指令<br>，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复<br>制。 |
# 安全产品
## 威胁检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmEye](https://github.com/RoomaSec/RmEye) | v0.0.4 | 戎码之眼是一个window上的基于att&ck模型的威胁监控工具.有效检测<br>常见的未知威胁与已知威胁.防守方的利剑 |
## 主机入侵检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Elkeid](https://github.com/bytedance/Elkeid) | rasp-v2<br>.2.0.6 | Elkeid is an open source solution that can meet the security r<br>equirements of various workloads such as hosts, containers and <br>K8s, and serverless. It is derived from ByteDance's internal be<br>st practices. |
| [Hades](https://github.com/theSecHunter/Hades) |  | Hades is an cross-platform HIDS with kernel-space data collect<br>ion. |
## Web应用防火墙
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [openstar](https://github.com/starjun/openstar) |  | lua waf,nginx+lua,openresty,luajit,waf+,cdn,nginx |
| [safeline](https://github.com/chaitin/safeline) | v2.1.2 | 一款足够简单、足够好用、足够强的免费 WAF。基于业界领先的语义引<br>擎检测技术，作为反向代理接入，保护你的网站不受黑客攻击。 |
## 欺骗防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Juggler](https://github.com/C4o/Juggler) |  | A system that may trick hackers.  针对黑客的拟态欺骗系统。 |
| [MySQL_Fake_Server](https://github.com/fnmsd/MySQL_Fake_Server) |  | MySQL Fake Server use to help MySQL Client File Reading and JD<br>BC Client Java Deserialize |
| [MysqlT](https://github.com/BeichenDream/MysqlT) | v1.0 | 伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击<br>攻击者 |
## 主机入侵防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [iDefender](https://github.com/wecooperate/iDefender) | 2.8.0 | iDefender（冰盾 - 终端主动防御系统） |
# 靶场
## web靶场
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ElectricRat](https://github.com/linjiananallnt/ElectricRat) | v1.3.0 | 电气鼠靶场系统是一种带有漏洞的Web应用程序，旨在为Web安全渗透测<br>试学习者提供学习和实践的机会。The Electrical Mouse Target Range <br>System is a web application with vulnerabilities designed to pr<br>ovide learning and practice opportunities for web security pene<br>tration testing learners. |
| [vulstudy](https://github.com/c0ny1/vulstudy) |  | 使用docker快速搭建各大漏洞靶场，目前可以一键搭建17个靶场。 |
| [sqli-labs](https://github.com/Audi-1/sqli-labs) |  | SQLI labs to test error based, Blind boolean based, Time based<br>. |
| [bodgeit](https://github.com/psiinon/bodgeit) | 1.4.0 | The BodgeIt Store is a vulnerable web application which is cur<br>rently aimed at people who are new to pen testing.  |
| [WackoPicko](https://github.com/adamdoupe/WackoPicko) |  | WackoPicko is a vulnerable web application used to test web ap<br>plication vulnerability scanners. |
| [WebGoat](https://github.com/WebGoat/WebGoat) | v2023.4 | WebGoat is a deliberately insecure application |
| [hackademic](https://github.com/Hackademic/hackademic) |  | the main hackademic code repository |
| [xssed](https://github.com/aj00200/xssed) |  | A set of XSS vulnerable PHP scripts for testing |
| [DSVW](https://github.com/stamparm/DSVW) |  | Damn Small Vulnerable Web |
| [vulnerable-node](https://github.com/cr0hn/vulnerable-node) |  | A very vulnerable web site written in NodeJS with the purpose <br>of have a project with identified vulnerabilities to test the q<br>uality of security analyzers tools tools |
| [MCIR](https://github.com/SpiderLabs/MCIR) |  | The Magical Code Injection Rainbow! MCIR is a framework for bu<br>ilding configurable vulnerability testbeds. MCIR is also a coll<br>ection of configurable vulnerability testbeds. |
| [pikachu](https://github.com/zhuifengshaonianhanlu/pikachu) |  | 一个好玩的Web安全-漏洞测试平台 |
| [webug4.0](https://github.com/wangai3176/webug4.0) |  | webug4.0 |
| [DoraBox](https://github.com/0verSp4ce/DoraBox) |  | DoraBox - Basic Web Vulnerability Training  |
| [BWVS](https://github.com/bugku/BWVS) |  | Web漏洞渗透测试靶场 |
| [VulApps](https://github.com/Medicean/VulApps) |  | 快速搭建各种漏洞环境(Various vulnerability environment) |
| [vulhub](https://github.com/vulhub/vulhub) |  | Pre-Built Vulnerable Environments Based on Docker-Compose |
## AWD靶场
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [20190511_awd_dock<br>er](https://github.com/glzjin/20190511_awd_docker) |  | 2019 年 5 月 11 日防灾科技学院 “应急挑战杯” 大学生网络安全邀<br>请赛 AWD 靶机题目。 |
| [awd-platform](https://github.com/zhl2008/awd-platform) |  | platform for awd |
| [AWD_CTF_Platform](https://github.com/mo-xiaoxi/AWD_CTF_Platform) |  | 一个简单的AWD训练平台 |
| [AWDDocker](https://github.com/Cl0udG0d/AWDDocker) |  | 标准化AWD靶场Docker |
| [Liaoning-provinci<br>al-competition-tar<br>get-1](https://github.com/yqw1212/Liaoning-provincial-competition-target-1) |  | 第三届辽宁省ctf线下awd靶机1web |
| [wordpress](https://github.com/871339097/wordpress) |  | AWD靶机 |
| [awd-platform](https://github.com/zhl2008/awd-platform) |  | platform for awd |
# 压力测试
## 网站压测工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WebBench](https://github.com/EZLippi/WebBench) |  | Webbench是Radim Kolar在1997年写的一个在linux下使用的非常简单的<br>网站压测工具。它使用fork()模拟多个客户端同时访问我们设定的URL，<br>测试网站在压力下工作的性能，最多可以模拟3万个并发连接去测试网站<br>的负载能力。官网地址:http://home.tiscali.cz/~cz210552/webbench.h<br>tml |
## 其他
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dperf](https://github.com/baidu/dperf) | v1.5.0 | dperf is a DPDK based 100Gbps network performance and load tes<br>ting software. |