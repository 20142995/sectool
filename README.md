# 更新于 2023-09-10 08:35:47

## 近15天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
|2023-09-09 14:03:15|[URLFinder](https://github.com/pingc0y/URLFinder)|2023.9.<br>9|修复 -ff 重复验证问题  修复 自动识别<br>协议bug|
|2023-09-08 21:18:40|[faker](https://github.com/joke2k/faker)|v19.6.0|See .|
|2023-09-08 02:11:54|[Elkeid](https://github.com/bytedance/Elkeid)|rasp-v2<br>.2.0.9||
|2023-09-07 10:01:41|[safeline](https://github.com/chaitin/safeline)|v3.3.0|### 新增    - 支持设置拦截页面附加说<br>明（）  - 频率限制新增 “人机验证” 的<br>限制方式（）    ### 优化    - 当网站域<br>名不匹配的时候，返回 “网站不存在” ，<br>提示更清晰（）  - 修复 攻击事件->原始日<br>志 的 “攻击地址” 中显示额外的转义符的<br>问题  - 修复站点详情中 “今日总请求量”<br> 和站点列表的 “今日访问量” 不一致的<br>问题（）  - 频率限制后直接封禁的拦截状<br>态码改为 429，和普通拦截 403 区分开，方<br>便排查拦截原因  - 加强后台登录安全性（<br>感谢微信交流 20 群「千年之狐」提供的建<br>议）  - 优化安装/升级时 CPU ssse3 指令<br>集的检查方式（）  - 优化界面样式交互，<br>修复一些已知问题|
|2023-09-05 15:46:30|[goproxy](https://github.com/snail007/goproxy)|v13.9|1、修复了开启流量上报后，一定条件下导<br>致的内存上涨问题。|
|2023-09-05 14:59:29|[autoDecoder](https://github.com/f0ng/autoDecoder)|0.31|## 2023.9.5 更新0.31  1. 域名匹配模块<br>中可以进行多域名匹配，修复了原版本无法<br>在多个域名下显示选项卡问题  2. 将接口调<br>试模块的两个换行符取消|
|2023-09-05 13:23:34|[v2rayA](https://github.com/v2rayA/v2rayA)|v2.2.4|## What's Changed * Fix Windows insta<br>llers' blank version string by @Markso<br>nHon in https://github.com/v2rayA/v2ra<br>yA/pull/1079   **Full Changelog**: htt<br>ps://github.com/v2rayA/v2rayA/compare/<br>v2.2.3...v2.2.4|
|2023-09-04 16:43:03|[nemo_go](https://github.com/hanc00l/nemo_go)|v2.10.1|### Update    - IP/Domain列表视图下显<br>示当前页的统计信息，优化IP和Domain的列<br>表查询功能；  - 增加XScan任务通过API接<br>口获取资产、重构自定义API搜索代码，目前<br>支持FOFA、Hunter及Quake引擎； 对FOFA自<br>定义关键词进行界面的优化  - 重构网络空<br>间在线资产搜索接口的代码；在线资产搜索<br>平台FOFA、Hunter、Quake及备案查询的API<br>口支持同时配置多个（以,分开）；FOFA的AP<br>I采用email:  token的方式配置（取消单独<br>的email字段）；  - quake的域名从quake.3<br>60.cn 变更为quake.360.net；完善onlinea<br>pi查询的查询语句、去除可能包含敏感信息<br>的过滤词（可能API导致查询失败）  - 取消<br>web显示页面的siderbar的隐藏； Domain列<br>表增加端口的显示和快速链接  - web测试在<br>线资产api可用性采用多线程方式；优化web<br>测试在线资产api代码限制只测试100条记录 <br> - 在IP和Domain的Web列表视图中，只显示<br>前5张screenshot，添加点击显示更多的提示<br>信息  - 重构离线扫描结果资产导入，去除n<br>aabu和TXPortmap  - 增加web的https功能<br>，为RPC及filesync启用TLS加密功能；增加t<br>ls方式下的自签名证书的生成  - 文件同步<br>文件对比列表代码重构  - Makefile    ###<br> Fix    - Hunter与Fofa在重构代码时base<br>64编码器错误  - online search sizeTota<br>l limit  - IP和域名详情页http_header字<br>段超长导致显示效果异常  - XScan根据的Xo<br>rganization直接调用数据库查询IP和Domai<br>n资产的Bug|
|2023-09-04 12:23:06|[dbeaver](https://github.com/dbeaver/dbeaver)|23.2.0|             - Changes since 23.1.5: <br>                - Data Editor:        <br>             - Spatial values renderin<br>g was fixed                     - Spat<br>ial images capture was fixed          <br>           - Special characters render<br>ing was improved                     -<br> Grouping panel icons were improved   <br>              - ER Diagrams: saved dia<br>grams now can be opened on another com<br>puters                 - Data transfer<br>: import settings handling was improve<br>d                 - Accessibility:    <br>                 - Connection dialog n<br>ow supports screen readers            <br>         - Cell value reading was impr<br>oved                     - Ctrl+Shift/<br>Alt+PageDn: vertical tabs switch      <br>               - Ctrl+ALT+6: SQL edito<br>r and results tab switch              <br>       - Ctrl+Shift+Enter now opens ER<br> diagram entities                     <br>- Ctrl+Shift+N: new connection dialog <br>open                 - Database driver<br>s:                     - Bigquery: DDL<br> for tables, views and stored procedur<br>es was added                     - Cli<br>ckhouse: arrays and structures visuali<br>zation was fixed                     -<br> Greenplum: external tables reading wa<br>s fixed                     - Teradata<br>: issue with the missing templates was<br> fixed                 - Many minor UI<br> and database issues were resolved    <br>         |
|2023-09-04 10:30:10|[nuclei](https://github.com/projectdiscovery/nuclei)|v2.9.14|    ## What's Changed  ### 🎉 New Fea<br>tures  * Added **impact** field under <br>template information block by @ehsande<br>ep in https://github.com/projectdiscov<br>ery/nuclei/pull/4121    yaml    impact<br>: |      Successful exploitation of th<br>is vulnerability could allow an attack<br>er to send arbitrary requests from the<br> server, potentially leading to unauth<br>orized access or data leakage.      ##<br># 🔨 Maintenance  * Updated mock outpu<br>t writer to write the failed event by <br>@ShubhamRasal in https://github.com/pr<br>ojectdiscovery/nuclei/pull/4099  * Upd<br>ated stringsutil.HasPrefixAnyI by @dog<br>ancanbakir in https://github.com/proje<br>ctdiscovery/nuclei/pull/4097    ### Ot<br>her Changes  * Fixed data-race warning<br>s by @RamanaReddy0M in https://github.<br>com/projectdiscovery/nuclei/pull/4036 <br> * Fixed issue with connection reuse i<br>n host-spray mode by @Mzack9999 in htt<br>ps://github.com/projectdiscovery/nucle<br>i/pull/3991  * Added utm_source in ver<br>sion check by @tarunKoyalwar in https:<br>//github.com/projectdiscovery/nuclei/p<br>ull/4112  * Updated template URL from <br>GitHub to https://templates.nuclei.sh <br>in jsonl output  by @dogancanbakir in <br>https://github.com/projectdiscovery/nu<br>clei/pull/4110        **Full Changelog<br>**: https://github.com/projectdiscover<br>y/nuclei/compare/v2.9.13...v2.9.14|
|2023-09-04 10:27:44|[FreeRDP](https://github.com/FreeRDP/FreeRDP)|2.11.1|Notworthy changes:  * Backported #935<br>6: Fix issues with order updates    Fo<br>r a complete and detailed change log s<br>ince the last release run:  git log 2.<br>11.1...2.11.0|
|2023-09-03 09:29:04|[afrog](https://github.com/zan8in/afrog)|v2.8.0|**Add**  - Added PoC for backup file <br>detection  - Customize global cookies <br>and will not overwrite the cookies of <br>the original POC    **Optimization**  <br>- afrog API has been synchronized with<br> the latest features    **新增**  - 新<br>增备份文件检测的 PoC  - 自定义全局 cook<br>ie，不会覆盖原 POC 的 cookie  - 新增一<br>批 HVV2023 PoCs    **优化**  - afrog AP<br>I 已同步最新功能|
|2023-09-03 04:30:00|[PEASS-ng](https://github.com/carlospolop/PEASS-ng)|2023090<br>3-188479<br>ae||
|2023-09-01 06:38:35|[trivy](https://github.com/aquasecurity/trivy)|v0.45.0|## ⚡Release highlights and summary⚡<br>    👉 https://github.com/aquasecurity<br>/trivy/discussions/5082    ## Changelo<br>g  * cdab67e7f docs: add Bitnami (#507<br>8)  * 7acc5e831 feat(docker): add supp<br>ort for scanning Bitnami components (#<br>5062)  * 9628b1cbf feat: add support f<br>or .trivyignore.yaml (#5070)  * 4547e2<br>766 fix(terraform): improve detection <br>of terraform files (#4984)  * 0c8919e1<br>e feat: filter artifacts on --exclude-<br>owned flag (#5059)  * c04f234fa fix(sb<br>om): cyclonedx advisory should omit nu<br>ll value (#5041)  * f811ed2d4 build: m<br>aximize build space for build tests (#<br>5072)  * 69ea5bf70 feat: improve kbom <br>component name (#5058)  * 3715dcb3f fi<br>x(pom): add licenses for pom artifacts<br> (#5071)  * 07f7e9853 chore(deps): Upd<br>ate defsec to v0.92.0 (#5068)  * d4ca3<br>cce2 chore: bump Go to 1.20 (#5067)  *<br> 49fdd584b feat: PURL matching with qu<br>alifiers in OpenVEX (#5061)  * 4401998<br>ec feat(java): add graph support for p<br>om.xml (#4902)  * 9c211d005 feat(swift<br>): add vulns for cocoapods (#5037)  * <br>422fa414e fix: support image pull secr<br>et for additional workloads (#5052)  *<br> 8e933860a fix: #5033 Superfluous doub<br>le quote in html.tpl (#5036)  * 9345a9<br>8ed docs(repo): update trivy repo usag<br>e and example (#5049)  * 5d8da70c6 per<br>f: Optimize Dockerfile for reduced lay<br>ers and size (#5038)  * 1be9da7aa feat<br>: scan K8s Resources Kind with --all-n<br>amespaces (#5043)  * 0e17d0bef fix: vu<br>lnerability typo (#5044)  * d70fab231 <br>docs: adding a terraform tutorial to t<br>he docs (#3708)  * 2fa264ac1 feat(repo<br>rt): add licenses to sarif format (#48<br>66)  * 07ddf4790 feat(misconf): show t<br>he resource name in the report (#4806)<br>  * 9de360623 chore: update alpine bas<br>e images (#5015)  * ef70d2076 feat: ad<br>d Package.resolved swift files support<br> (#4932)  * ec5d8bec0 feat(nodejs): pa<br>rse licenses in yarn projects (#4652) <br> * 3114c87e6 fix: k8s private registri<br>es support (#5021)  * 6d79f55db bump g<br>ithub.com/testcontainers/testcontainer<br>s-go from 0.21.0 to 0.23.0 (#5018)  * <br>9ace59106 feat(vuln): support last_aff<br>ected field from osv (#4944)  * d44217<br>640 feat(server): add version endpoint<br> (#4869)  * 63cd41d20 feat: k8s privat<br>e registries support (#4987)  * cb16e2<br>3f1 fix(server): add indirect prop to <br>package (#4974)  * a4e981b4e docs: add<br> coverage (#4954)  * 6f03c7940 feat(c)<br>: add location for lock file dependenc<br>ies. (#4994)  * c74870500 docs: adding<br> blog post on ec2 (#4813)  * 4e1316c37<br> revert 32bit bins (#4977)  * fc959fc5<br>7 chore(deps): bump github.com/xlab/tr<br>eeprint from 1.1.0 to 1.2.0 (#4917)   <br> |
|2023-08-31 16:50:30|[grype](https://github.com/anchore/grype)|v0.66.0|#     ##  (2023-08-31)        ### Add<br>ed Features    - Allow for access to p<br>rivate CAs securely ] ] ]  - Filter ou<br>t packages that are owned by OS packag<br>es (ownership overlap) ] ] ]    ### Bu<br>g Fixes    - fix: Only remove packages<br> by binary overlap ] ]  - New version <br>notice only showing the version and no<br> text ] ]  - fix: set correct default <br>to exclude overlapping binaries ] ]  -<br> Portage version comparison is not wor<br>king ] ] ]    ### Additional Changes  <br>  - Update Syft to 0.89.0      |
|2023-08-31 15:42:19|[syft](https://github.com/anchore/syft)|v0.89.0|#     ##  (2023-08-31)        ### Add<br>ed Features    - Add registry certific<br>ate verification support  ] ]  - Add S<br>YFT_CONFIG environment variable for co<br>nfiguration file path ] ] ]    ### Bug<br> Fixes    - Fix quiet flag ] ]  - Comm<br>and line flags not overriding configur<br>ation file values ] ] ]  - Django pack<br>age CPE is not correct ] ] ]  - Config<br> parsing includes config.yaml in worki<br>ng dir ] ] ]  - Fix a possible panic o<br>n universal go binaries ] ] ]  - Disab<br>ling catalogers is not working in powe<br>r user command ] ] ]  - Virtual path c<br>hanges to java cataloger causing creat<br>ion of extra incorrect packages when j<br>ars are renamed ] ] ]      |
|2023-08-31 08:41:49|[Viper](https://github.com/FunnyWolf/Viper)|2023083<br>1|  ### 优化  - 清除不需要的日志,提高系<br>统运行速度  - 优化docker logs日志,存储<br>到日志目录便于问题定位  - docker health<br>check当前检查所有后台服务    ### Bugfi<br>x  - fix https://github.com/FunnyWolf/<br>Viper/issues/117  - fix https://github<br>.com/FunnyWolf/Viper/issues/145|
|2023-08-30 18:53:08|[rotp](https://github.com/mdp/rotp)|v6.3.0|##  (2023-08-30)   ### Features  * Al<br>low for non-standard provisioning URI <br>params, eg. image/icon () ()|
|2023-08-29 17:33:01|[mubeng](https://github.com/kitabisa/mubeng)|v0.14.1|## Changelog * 62f3832 build(deps): b<br>ump github.com/sourcegraph/conc from 0<br>.2.0 to 0.3.0 (#187) * 4535c2f build(d<br>eps): bump github.com/briandowns/spinn<br>er from 1.15.0 to 1.23.0 (#190) * 629e<br>737 build(deps): bump github.com/AlecA<br>ivazis/survey/v2 from 2.2.12 to 2.3.7 <br>(#198) * 236d3dc build(deps): bump git<br>hub.com/henvic/httpretty from 0.0.6 to<br> 0.1.2 (#199) * 8459f63 build(deps): b<br>ump docker/login-action from 2.1.0 to <br>2.2.0 (#200) * e3c1ced build(deps): bu<br>mp docker/build-push-action from 4.0.0<br> to 4.1.1 (#202) * 84f4788 build(deps)<br>: bump goreleaser/goreleaser-action fr<br>om 4.2.0 to 4.4.0 (#205) * 2d50755 mis<br>c: Update CONTRIBUTORS * 706cba6 build<br>(deps): bump golangci/golangci-lint-ac<br>tion from 3.4.0 to 3.7.0 (#206) * 5876<br>259 build(deps): bump github.com/valya<br>la/fasttemplate from 1.2.1 to 1.2.2 (#<br>172) * f1b84c8 build(deps): bump actio<br>ns/setup-go from 3 to 4 (#192) * 00c7f<br>87 build(deps): bump peter-evans/creat<br>e-pull-request from 4 to 5 (#194)  |
|2023-08-28 04:57:05|[Mobile-Security-F<br>ramework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)|v3.7.6|### v3.7.6 Beta Changelog    - Featur<br>es or Enhancements     - Docker base i<br>mage update to Ubuntu 22.04     - Dock<br>erfile QA     - Migrated from Pip to P<br>oetry for dependency management     - <br>Migrate from setup.py to use poetry fo<br>r build and publish     - Python 3.11 <br>support     - Docker ADB connection im<br>provements (host.docker.internal trans<br>lation for localhost)     -  IOS Swift<br> RulesUpdates ios_biometric_bool, ios_<br>biometric_acl, ios_keychain_weak_acl_d<br>evice_passcode, ios_keychain_weak_acce<br>ssibility_value, ios_insecure_random_n<br>o_generator, ios_biometry_hardened    <br> - Android SCA rules update     - Entr<br>opies scan support for strings     - R<br>egex Hardening: Fixes possible Regex D<br>oS in rules and MobSF code base     - <br>Tox QA     - Added poetry build test  <br>   - Updated mobsf PyPI publishing wor<br>kflow      - Update local DBs     - UR<br>Ls/Email extraction refactor     - Sta<br>tic and Dynamic Binary Analysis QA    <br> - Refactor Dex permissions     - Refa<br>ctor Androguard apk.APK() usage     - <br>Fallback certificate analysis using ap<br>ksigtool     - Use BeautifulSoup4 to p<br>rettify malformed XML     - Detect non<br> standard XML namespace in AndroidMani<br>fest.xml, Fixes : #2198     - Updated <br>android permissions list     - Updated<br> android permission update check scrip<br>t     - Github Actions version update <br>    - Apktool bump     - Bump httptool<br>s     - Bump yara-python-dex     - Doc<br>ker image build test for PRs     - iOS<br> Source Report Fix     - Removed unwan<br>ted pinned repository     - Frida APK <br>Patcher (WIP)     - Fix for Recent Sca<br>ns scan not completed for iOS zip     <br>- Fix for MachO stripped symbols false<br> positive     - Fix bug in IPA downloa<br>d     - iOS/Android form validation fi<br>x     - Fix missing exported component<br>s   - Enterprise Feature Request      <br>  - String extraction from APK, Source<br>, AAR, JAR, SO.        - Android strin<br>gs sections to show source of strings <br>extracted        - Strings extraction <br>refactor        - Support for independ<br>ent .so scan        - Dylib analysis s<br>upport        - Dylib string extractio<br>n        - Improved iOS Plist secret e<br>xtraction        - Support for Indepen<br>dent .dylib scan        - Symbols view<br> for dylib and so        - Trackers su<br>pport for so        - AAR/JAR obfuscat<br>ion and debug check        - Independe<br>nt Static Library(.a) ELF/MachO Analys<br>is        - Mac FAT binary only suppor<br>ted on Mac                            <br> ## What's Changed  * Update dynamic_a<br>nalysis.html by @ajinabraham in https:<br>//github.com/MobSF/Mobile-Security-Fra<br>mework-MobSF/pull/2218  * Hotfix: Hand<br>le Docker  ADB connectivity internally<br> by @ajinabraham in https://github.com<br>/MobSF/Mobile-Security-Framework-MobSF<br>/pull/2219  * update apktool to 2.8.1 <br>by @superpoussin22 in https://github.c<br>om/MobSF/Mobile-Security-Framework-Mob<br>SF/pull/2220  * update apktool by @sup<br>erpoussin22 in https://github.com/MobS<br>F/Mobile-Security-Framework-MobSF/pull<br>/2225  * HOTFIX: Dynamic Analyzer Supp<br>ort Alert by @ajinabraham in https://g<br>ithub.com/MobSF/Mobile-Security-Framew<br>ork-MobSF/pull/2227  * [HOTFIX] Regex <br>+ Rule Update by @ajinabraham in https<br>://github.com/MobSF/Mobile-Security-Fr<br>amework-MobSF/pull/2232  * [EFR06] Ind<br>ependent Shared Object (.so) Scan and <br>Improved String search by @ajinabraham<br> in https://github.com/MobSF/Mobile-Se<br>curity-Framework-MobSF/pull/2228  * Up<br>date macho_analysis.py - SYMBOLS STRIP<br>PED False Negative by @Karmaz95 in htt<br>ps://github.com/MobSF/Mobile-Security-<br>Framework-MobSF/pull/2234  * [EFR-08] <br>Dylib + Symbols + Other Features by @a<br>jinabraham in https://github.com/MobSF<br>/Mobile-Security-Framework-MobSF/pull/<br>2239  * Fix missing exported component<br>s by @Abb4d0n in https://github.com/Mo<br>bSF/Mobile-Security-Framework-MobSF/pu<br>ll/2176  * [EFR09] AAR/JAR obfuscation<br> and debug check + Exception Handed st<br>rings and symbols extraction by @ajina<br>braham in https://github.com/MobSF/Mob<br>ile-Security-Framework-MobSF/pull/2240<br>  * [EFR10] Independent Static Library<br>(.a) ELF/MachO Analysis by @ajinabraha<br>m in https://github.com/MobSF/Mobile-S<br>ecurity-Framework-MobSF/pull/2242  * P<br>ip to poetry and Dockerfile update by <br>@ajinabraham in https://github.com/Mob<br>SF/Mobile-Security-Framework-MobSF/pul<br>l/2244  * Docker Buildx test by @ajina<br>braham in https://github.com/MobSF/Mob<br>ile-Security-Framework-MobSF/pull/2247<br>  * [HOTFIX] bs4 malformed xml parsing<br> + xml namespace detection by @ajinabr<br>aham in https://github.com/MobSF/Mobil<br>e-Security-Framework-MobSF/pull/2248  <br>* [HOTFIX] Migrate from setup.py to po<br>etry, tox QA by @ajinabraham in https:<br>//github.com/MobSF/Mobile-Security-Fra<br>mework-MobSF/pull/2249    ## New Contr<br>ibutors  * @Karmaz95 made their first <br>contribution in https://github.com/Mob<br>SF/Mobile-Security-Framework-MobSF/pul<br>l/2234  * @Abb4d0n made their first co<br>ntribution in https://github.com/MobSF<br>/Mobile-Security-Framework-MobSF/pull/<br>2176    **Full Changelog**: https://gi<br>thub.com/MobSF/Mobile-Security-Framewo<br>rk-MobSF/compare/v3.6.9...v3.7.6|
|2023-08-27 18:25:14|[ghauri](https://github.com/r0oth3x49/ghauri)|1.2.4|## Fixes   - updated code quality   -<br> added payload for data extraction for<br> MSSQL|
|2023-08-26 11:42:13|[OneScan](https://github.com/vaycore/OneScan)|v1.2.1|1.2.1 版本发布，紧急修复    ### 修复 <br>   - 修复扫描时请求包出现 -1 的问题|
|2023-08-26 02:44:27|[qsnctf-python](https://github.com/Moxin1044/qsnctf-python)|0.0.8.1<br>0|### 说明  本次根据Issues提升了依赖PyE<br>xecJS的版本，由原先的**PyExecJS 1.5.1*<br>*直升到了**PyExecJS2 1.6.1**。  已经安<br>装的用户可以使用python3 -m pip install <br>-U qsnctf 进行更新，目前版本为0.0.8.10<br>。  如果在使用过程中有其他的问题，您可<br>使用Issues提交。|
## 近15天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
|2023-09-10 00:00:03|[free](https://github.com/freefq/free)|updated_at 09-10 08:00|
|2023-09-09 23:57:41|[DecoyMini](https://github.com/decoymini/DecoyMini)|Update README.md|
|2023-09-09 23:20:58|[PocOrExp_in_Githu<br>b](https://github.com/ycdxsb/PocOrExp_in_Github)|update 2023-09-10 07:20:58|
|2023-09-09 18:37:29|[kube-bench](https://github.com/aquasecurity/kube-bench)|build(deps): bump alpine from 3.18.2 to 3.18.3 (#14<br>87)  Bumps alpine from 3.18.2 to 3.18.3.    ---  upd<br>ated-dependencies:  - dependency-name: alpine    dep<br>endency-type: direct:production    update-type: vers<br>ion-update:semver-patch  ...    Signed-off-by: depen<br>dabot[bot]   Co-authored-by: dependabot[bot] |
|2023-09-09 14:01:45|[URLFinder](https://github.com/pingc0y/URLFinder)|2023/9/9更新|
|2023-09-09 12:31:38|[v2rayfree](https://github.com/aiboboxx/v2rayfree)|update|
|2023-09-09 11:09:19|[knife](https://github.com/bit4woo/knife)|Update FindUrlAndRequest.java|
|2023-09-09 11:09:02|[domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro)|Update SearchMenu.java|
|2023-09-09 10:35:10|[Komo](https://github.com/komomon/Komo)|Update requirement.txt|
|2023-09-09 06:57:59|[rustdesk](https://github.com/rustdesk/rustdesk)|Merge pull request #5639 from Mr-Update/patch-1  Up<br>date de.rs|
|2023-09-09 05:14:34|[all-in-one-v2](https://github.com/zaivanza/all-in-one-v2)|add zora, linea, base to merkly|
|2023-09-09 01:16:17|[0_zone_tool](https://github.com/wkend/0_zone_tool)|Update README.md|
|2023-09-08 21:18:01|[faker](https://github.com/joke2k/faker)|Bump version: 19.5.0 → 19.6.0|
|2023-09-08 18:10:00|[syft](https://github.com/anchore/syft)|chore(deps): update stereoscope to 057dda3667e7f2b5<br>e6ec6716747badd5f403c6de (#2109)  Signed-off-by: Git<br>Hub   Co-authored-by: kzantow |
|2023-09-08 17:31:55|[neuvector](https://github.com/neuvector/neuvector)|Merge pull request #997 from gfsuse/prune_ns  NVSHA<br>S-8246, Improve pruning namespace func to delete rel<br>ated rules faster to avoid holding lock too long|
|2023-09-08 16:16:36|[nuclei](https://github.com/projectdiscovery/nuclei)|dark mode fixes!|
|2023-09-08 15:01:49|[dbeaver](https://github.com/dbeaver/dbeaver)|Merge branch 'devel' of https://github.com/dbeaver/<br>dbeaver into devel|
|2023-09-08 14:04:16|[trivy](https://github.com/aquasecurity/trivy)|chore(deps): bump sigstore/cosign-installer (#5104)<br>  Bumps  from a5d81fb6bdbcbb3d239e864d65528204202544<br>94 to 4a861528be5e691840a69536975ada1d4c30349d. -  -<br>   --- updated-dependencies: - dependency-name: sigs<br>tore/cosign-installer   dependency-type: direct:prod<br>uction ...  Signed-off-by: dependabot[bot]  Co-autho<br>red-by: dependabot[bot] |
|2023-09-08 12:44:22|[FreeRDP](https://github.com/FreeRDP/FreeRDP)|[codec,interleaved] fix type definition|
|2023-09-08 08:40:42|[murphysec](https://github.com/murphysecurity/murphysec)|feat(cmd): SBOM scan|
|2023-09-08 05:43:49|[autoDecoder](https://github.com/f0ng/autoDecoder)|Update README.md|
|2023-09-08 04:05:36|[arthas](https://github.com/alibaba/arthas)|sysenv/sysprop command sorted by key #2619 (#2652)|
|2023-09-07 18:55:38|[grype](https://github.com/anchore/grype)|chore: update grype to use Go v1.21 (#1480)  Signed<br>-off-by: Christopher Phillips |
|2023-09-07 17:44:13|[vulhub](https://github.com/vulhub/vulhub)|Merge pull request #460 from vulhub/hadolint-upgrad<br>e  upgrade hadolint to 2.12.0|
|2023-09-07 11:15:11|[Elkeid](https://github.com/bytedance/Elkeid)|Merge pull request #533 from bytedance/fix-python-b<br>uild  Fix python build|
|2023-09-07 09:54:04|[safeline](https://github.com/chaitin/safeline)|fix(websiet): node 20.6 version can't compile docs|
|2023-09-07 09:03:01|[sqlmap](https://github.com/sqlmapproject/sqlmap)|Fixes #5521|
|2023-09-07 07:50:34|[vulnerability](https://github.com/lal0ne/vulnerability)|CVE-2023-38035|
|2023-09-07 06:55:06|[Mobile-Security-F<br>ramework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)|[HOTFIX] iOS Framework Analysis + Multiple Feature <br>QA (#2260)  * iOS Framework Analysis  * Static Analy<br>sis URL simplification  * Replace hardcoded urls in <br>template with {% url %}  * Code QA  * Remove unwante<br>d template file  * Remove rescan query param from ur<br>l  * Android icon SVG guessing improvements  * Icon <br>analysis refactoring, change icon storage location  <br>* Remove SVG to PNG converter. Support PNG and SVG i<br>con.  * Github docker release action update|
|2023-09-07 06:33:11|[impacket](https://github.com/fortra/impacket)|Address DHCP python3 bug (#1398)  * Address DHCP py<br>thon3 bug    * Fix packed packet format error    * A<br>pply suggestions from code review    ---------    Co<br>-authored-by: Ujwal Komarla   Co-authored-by: alexis<br>balbachan |
|2023-09-06 13:59:16|[iDefender](https://github.com/wecooperate/iDefender)|update|
|2023-09-06 12:42:03|[ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)|feat: Switch authentication from cookies to localSt<br>orage to support new extension features|
|2023-09-06 09:32:18|[0day](https://github.com/helloexp/0day)|add CVE-2021-4034 polkit privilege escalation explo<br>it|
|2023-09-06 07:16:01|[v2rayA](https://github.com/v2rayA/v2rayA)|Merge pull request #1081 from MarksonHon/feat_v5  c<br>i(release_feat_v5): some changes|
|2023-09-06 04:26:00|[zpscan](https://github.com/niudaii/zpscan)|fix: jsjump|
|2023-09-06 02:18:02|[frp](https://github.com/fatedier/frp)|support yaml/json/toml configuration format, make i<br>ni deprecated (#3599)|
|2023-09-06 00:52:01|[afrog](https://github.com/zan8in/afrog)|update|
|2023-09-05 15:15:04|[MockingBird](https://github.com/babysor/MockingBird)|Skip embedding (#950)  * Skip embedding    * Skip e<br>arlier    * Remove unused paramater    * Pass param|
|2023-09-05 06:56:25|[Awesome-POC](https://github.com/Threekiii/Awesome-POC)|更新漏洞|
|2023-09-05 06:44:46|[Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam)|更新README.md|
|2023-09-04 16:15:17|[nemo_go](https://github.com/hanc00l/nemo_go)|Update: v2.10.1|
|2023-09-04 13:20:16|[RouteVulScan](https://github.com/F6JO/RouteVulScan)|Update threads.java|
|2023-09-04 10:22:18|[suo5](https://github.com/zema1/suo5)|Merge pull request #37 from zema1/bump-go-version  <br>feat: bump up go to v1.20|
|2023-09-04 03:12:54|[404StarLink](https://github.com/knownsec/404StarLink)|weekly update at 2023-09-04|
|2023-09-02 15:38:22|[awesome-chatgpt-z<br>h](https://github.com/yzfly/awesome-chatgpt-zh)|add codellama, llms|
|2023-09-01 14:06:59|[dperf](https://github.com/baidu/dperf)|Merge pull request #368 from pengjianzhang/main  mo<br>ve docs to dperf.org|
|2023-09-01 11:00:54|[veinmind-tools](https://github.com/chaitin/veinmind-tools)|docs: update report manual (#266)|
|2023-09-01 07:34:07|[ObserverWard](https://github.com/0x727/ObserverWard)|Merge pull request #195 from 0x727/dependabot/cargo<br>/actix-web-4.4.0  Bump actix-web from 4.3.1 to 4.4.0|
|2023-08-31 08:41:02|[Viper](https://github.com/FunnyWolf/Viper)|update version 2023-08-31|
|2023-08-30 19:25:56|[rotp](https://github.com/mdp/rotp)|chore: Add the .gem file to release for easier publ<br>ishing in an MFA world (#133)|
|2023-08-30 13:24:01|[ddddocr](https://github.com/sml2h3/ddddocr)|修复pillow的版本引用问题|
|2023-08-29 15:14:11|[mubeng](https://github.com/kitabisa/mubeng)|build(deps): bump github.com/sourcegraph/conc from <br>0.2.0 to 0.3.0 (#187)  Bumps  from 0.2.0 to 0.3.0.  <br>-   -     ---  updated-dependencies:  - dependency-n<br>ame: github.com/sourcegraph/conc    dependency-type:<br> direct:production    update-type: version-update:se<br>mver-minor  ...    Signed-off-by: dependabot[bot]   <br>Co-authored-by: dependabot[bot] |
|2023-08-29 06:09:32|[Vuln-List](https://github.com/wwl012345/Vuln-List)|Update 终端软件漏洞合集.md|
|2023-08-28 09:28:41|[semgrepper](https://github.com/gand3lf/semgrepper)|Merge pull request #9 from tghosth/clarify-running <br> Update README.md with tutorial|
|2023-08-28 08:55:05|[Vulnerability-Wik<br>i](https://github.com/Threekiii/Vulnerability-Wiki)|更新漏洞|
|2023-08-28 07:56:06|[Vulhub-Reproduce](https://github.com/Threekiii/Vulhub-Reproduce)|更新漏洞|
|2023-08-28 07:37:55|[PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book)|Update README.md|
|2023-08-27 18:21:43|[ghauri](https://github.com/r0oth3x49/ghauri)|updated code quality, added payload for mssql, bump<br>ed version 1.2.3|
|2023-08-27 14:20:30|[Fastjson](https://github.com/safe6Sec/Fastjson)|Update README.md|
|2023-08-27 12:31:35|[WebGoat](https://github.com/WebGoat/WebGoat)|fix: potential NPE in the stored XSS assignment|
|2023-08-26 11:37:40|[OneScan](https://github.com/vaycore/OneScan)|修复扫描时请求包出现-1的问题；更新版本号为1.2.1|
|2023-08-26 10:15:19|[mitaka](https://github.com/ninoseki/mitaka)|Merge pull request #751 from ninoseki/refaoctor-nul<br>l-undefined  refactor: remove !== null/undefined|
|2023-08-26 03:35:58|[dirsearch](https://github.com/maurosoria/dirsearch)|Merge pull request #1310 from godspeedcurry/master <br> Update dicc.txt|
|2023-08-26 02:35:55|[qsnctf-python](https://github.com/Moxin1044/qsnctf-python)|build( Version ): ⬆️ 0.0.8.10|## 所有项目
# 渗透测试
## 信息收集
### 资产测绘采集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll) | V1.2 | 为了方便安全从业人员在使用网络测绘平台进行信息搜集时的效率，本<br>程序集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并<br>且合并展示及导出。 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | v2.5 | 【支持Fofa、Shodan、Hunter、Zoomeye、Quake网络空间搜索引擎】闪<br>电搜索器；GUI图形化渗透测试信息搜集工具；资产搜集引擎；hw红队工<br>具hvv |
| [Search_Viewer](https://github.com/G3et/Search_Viewer) | v3.0 | 集Fofa、Hunter鹰图、Shodan、360 quake、Zoomeye 钟馗之眼、censy<br>s 为一体的空间测绘gui图形界面化工具，支持一键采集爬取和导出fofa<br>、shodan等数据，方便快捷查看 |
| [koko-moni](https://github.com/burpheart/koko-moni) | v0.0.1 | 一个网络空间搜索引擎监控平台，可定时进行资产信息爬取，及时发现<br>新增资产，本项目聚合了 Fofa、Hunter、Quake、Zoomeye 和 Threatboo<br>k 的数据源，并对获取到的数据进行去重与清洗 |
| [AsamF](https://github.com/Kento-Sec/AsamF) | v0.2.5 | AsamF是集成Fofa、Quake、Hunter、Shodan、Zoomeye、Chinaz、0.zon<br>e及爱企查的一站式企业信息资产收集、网络资产测绘工具。 |
| [fshzqSearch](https://github.com/Ifory885/fshzqSearch) |  |  |
| [0_zone_tool](https://github.com/wkend/0_zone_tool) |  | 零零信安api信息系统查询脚本 |
| [TKHunter](https://github.com/HHa1ey/TKHunter) | TKHunte<br>r-v1.8 | 一个基于JavaFX写的一个Hunter资产测绘平台的图形化工具 |
### 子域名收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [subfinder](https://github.com/projectdiscovery/subfinder) | v2.6.2 | Fast passive subdomain enumeration tool. |
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
| [URLFinder](https://github.com/pingc0y/URLFinder) | 2023.9.<br>9 | 一款快速、全面、易用的页面信息提取工具，可快速发现和提取页面中<br>的JS、URL和敏感信息。 |
| [JSFinder](https://github.com/Threezh1/JSFinder) |  | JSFinder is a tool for quickly extracting URLs and subdomains <br>from JS files on a website. |
| [BBScan](https://github.com/lijiejie/BBScan) | v1.5 | A fast vulnerability scanner |
| [Dirscan](https://github.com/corunb/Dirscan) | v.1.5.2 | Dirscan是一款由go编写的高性能、高并发的目录扫描器，现在已经支<br>持GET、HEAD、递归扫描、代理、爬虫等功能功能,后续努力实现更多功能<br>。 |
### 指纹识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [EHole](https://github.com/EdgeSecurityTeam/EHole) | v3.1 | EHole(棱洞)3.0 重构版-红队重点攻击系统指纹探测工具 |
| [wappalyzergo](https://github.com/projectdiscovery/wappalyzergo) | v0.0.10<br>9 | A high performance go implementation of Wappalyzer Technology <br>Detection Library |
| [14Finger](https://github.com/b1ackc4t/14Finger) | V1.1 | 功能齐全的Web指纹识别和分享平台,基于vue3+django前后端分离的web<br>架构，并集成了长亭出品的rad爬虫的功能，内置了一万多条互联网开源<br>的指纹信息。 |
| [WhatWeb](https://github.com/urbanadventurer/WhatWeb) | v0.5.5 | Next generation web scanner |
| [TideFinger](https://github.com/TideSec/TideFinger) |  | TideFinger——指纹识别小工具，汲取整合了多个web指纹库，结合了<br>多种指纹检测方法，让指纹检测更快捷、准确。 |
| [Glass](https://github.com/s7ckTeam/Glass) |  | Glass是一款针对资产列表的快速指纹识别工具，通过调用Fofa/ZoomEy<br>e/Shodan/360等api接口快速查询资产信息并识别重点资产的指纹，也可<br>针对IP/IP段或资产列表进行快速的指纹识别。 |
| [Finger](https://github.com/EASY233/Finger) |  | 一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具 |
| [LazyDog](https://github.com/L10nK1n6/LazyDog) | 1.1 | LazyDog是一款通过网络空间测绘引擎读取资产并进行指纹识别的工具 |
| [whatweb-plus](https://github.com/winezer0/whatweb-plus) | v0.5.5.<br>19.fix | whatweb 增强版  8000+插件（提供windows可执行文件） |
| [Find-SomeThing](https://github.com/LittleBear4/Find-SomeThing) |  | 红队批量脆弱点搜集工具 |
| [ObserverWard](https://github.com/0x727/ObserverWard) | v2023.8<br>.21 | Cross platform community web fingerprint identification tool |
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
| [naabu](https://github.com/projectdiscovery/naabu) | v2.1.7 | A fast port scanner written in go with a focus on reliability <br>and simplicity. Designed to be used in combination with other t<br>ools for attack surface discovery in bug bounties and pentests |
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
| [nemo_go](https://github.com/hanc00l/nemo_go) | v2.10.1 | Nemo是用来进行自动化信息收集的一个简单平台，通过集成常用的信息<br>收集工具和技术，实现对内网及互联网资产信息的自动收集，提高隐患排<br>查和渗透测试的工作效率。 |
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
| [ENScan_GO](https://github.com/wgpsec/ENScan_GO) | 0.0.15 | 一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信<br>息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信<br>息聚合导出。 |
| [IEyes](https://github.com/SiJiDo/IEyes) | v0.1.2 | icp备案查询 |
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
| [Mobile-Security-F<br>ramework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | v3.7.6 | Mobile Security Framework (MobSF) is an automated, all-in-one <br>mobile application (Android/iOS/Windows) pen-testing, malware a<br>nalysis and security assessment framework capable of performing<br> static and dynamic analysis. |
## 漏洞发现
### 漏洞扫描框架
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pocsuite3](https://github.com/knownsec/pocsuite3) | v2.0.5 | pocsuite3 is an open-sourced remote vulnerability testing fram<br>ework developed by the Knownsec 404 Team. |
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
| [nuclei](https://github.com/projectdiscovery/nuclei) | v2.9.14 | Fast and customizable vulnerability scanner based on simple YA<br>ML based DSL. |
| [afrog](https://github.com/zan8in/afrog) | v2.8.0 | A Security Tool for Bug Bounty, Pentest and Red Teaming. |
| [vulmap](https://github.com/zhzyker/vulmap) | v0.9 | Vulmap 是一款 web 漏洞扫描和验证工具, 可对 webapps 进行漏洞扫<br>描, 并且具备漏洞验证功能 |
| [POC-bomber](https://github.com/tr0uble-mAker/POC-bomber) | POC-bom<br>ber-for-<br>Redteam-<br>v3.0.0 | 利用大量高威胁poc/exp快速获取目标权限，用于渗透和红队快速打点 |
| [QingTing](https://github.com/StarCrossPortal/QingTing) | v0.3 | 蜻蜓安全一个安全工具编排平台,可以自由编排你的工具流,集成108款<br>工具,包括xray、nmap、awvs等;你可以将喜欢的工具编排成一个场景，快<br>速打造适合自己的安全工作台~ |
| [myscan](https://github.com/amcai/myscan) |  | myscan  被动扫描 |
| [NextScan](https://github.com/tongcheng-security-team/NextScan) | v1.2.0 | 飞刃是一套完整的企业级黑盒漏洞扫描系统，集成漏洞扫描、漏洞管理<br>、扫描资产、爬虫等服务。 拥有强大的漏洞检测引擎和丰富的插件库，<br>覆盖多种漏洞类型和应用程序框架。 |
| [DarkAngel/](https://github.com/Bywalks/DarkAngel/) |  |  |
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
#### other
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [murphysec](https://github.com/murphysecurity/murphysec) | v3.1.1 | An open source tool focused on software supply chain security.<br> 墨菲安全专注于软件供应链安全，具备专业的软件成分分析（SCA）、<br>漏洞检测、专业漏洞库。 |
| [Kunlun-M](https://github.com/LoRexxar/Kunlun-M) | v2.6.5 | KunLun-M是一个完全开源的静态白盒扫描工具，支持PHP、JavaScript<br>的语义扫描，基础安全、组件安全扫描，Chrome Ext\Solidity的基础扫<br>描。 |
| [CodeQLpy](https://github.com/webraybtl/CodeQLpy) |  | CodeQLpy是一款基于CodeQL实现的半自动化代码审计工具，目前仅支持<br>java语言。实现从源码反编译，数据库生成，脆弱性发现的全过程，可<br>以辅助代码审计人员快速定位源码可能存在的漏洞。 |
#### java
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jar-analyzer-gui](https://github.com/4ra1n/jar-analyzer-gui) | 1.1 | 一个用于分析Jar包的GUI工具，可以用多种方式搜索你想要的信息，自<br>动构建方法调用关系，支持分析Spring框架（A Java GUI Tool for Anal<br>yzing Jar） |
| [code-inspector](https://github.com/4ra1n/code-inspector) | 0.2-bet<br>a | JavaWeb漏洞审计工具，构建方法调用链并模拟栈帧进行分析 |
| [codeql-cli-binari<br>es](https://github.com/github/codeql-cli-binaries) | v2.14.3 | Binaries for the CodeQL CLI |
| [CodeQLpy](https://github.com/webraybtl/CodeQLpy) |  | CodeQLpy是一款基于CodeQL实现的半自动化代码审计工具，目前仅支持<br>java语言。实现从源码反编译，数据库生成，脆弱性发现的全过程，可<br>以辅助代码审计人员快速定位源码可能存在的漏洞。 |
### 容器漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [veinmind-tools](https://github.com/chaitin/veinmind-tools) | v2.1.5 | veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器<br>安全工具集 |
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
| [Ingram](https://github.com/jorhelp/Ingram) | v2.0.0 | 网络摄像头漏洞扫描工具 | Webcam vulnerability scanning tool |
| [NextScan](https://github.com/tongcheng-security-team/NextScan) | v1.2.0 | 飞刃是一套完整的企业级黑盒漏洞扫描系统，集成漏洞扫描、漏洞管理<br>、扫描资产、爬虫等服务。 拥有强大的漏洞检测引擎和丰富的插件库，<br>覆盖多种漏洞类型和应用程序框架。 |
### 信息泄露监控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [code6](https://github.com/4x99/code6) | 1.6.4 | 码小六 - GitHub 代码泄露监控系统 |
| [gshark](https://github.com/madneal/gshark) | v1.2.1 | Scan for sensitive information easily and effectively. |
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
| [veinmind-tools](https://github.com/chaitin/veinmind-tools) | v2.1.5 | veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器<br>安全工具集 |
| [grype](https://github.com/anchore/grype) | v0.66.0 | A vulnerability scanner for container images and filesystems |
#### 容器漏洞分析工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [clair](https://github.com/quay/clair) | v4.7.1 | Vulnerability Static Analysis for Containers |
#### 容器安全扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [trivy](https://github.com/aquasecurity/trivy) | v0.45.0 | Find vulnerabilities, misconfigurations, secrets, SBOM in cont<br>ainers, Kubernetes, code repositories, clouds and more |
#### 容器镜像扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [grype](https://github.com/anchore/grype) | v0.66.0 | A vulnerability scanner for container images and filesystems |
| [syft](https://github.com/anchore/syft) | v0.89.0 | CLI tool and library for generating a Software Bill of Materia<br>ls from container images and filesystems |
#### K8S漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-hunter](https://github.com/aquasecurity/kube-hunter) | v0.6.8 | Hunt for security weaknesses in Kubernetes clusters |
#### K8S基线核查
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | v0.6.17 | Checks whether Kubernetes is deployed according to security be<br>st practices as defined in the CIS Kubernetes Benchmark |
#### 云原生安全平台
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [neuvector](https://github.com/neuvector/neuvector) | v5.2.1 |  |
| [ThunderCloud](https://github.com/Rnalter/ThunderCloud) |  | Cloud Exploit Framework |
### 半自动化漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [railgun](https://github.com/lz520520/railgun) | v1.5.5 |  |
| [Goby](https://github.com/gobysec/Goby) | Beta2.2<br>.0 | Attack surface mapping |
| [zpscan](https://github.com/niudaii/zpscan) | v1.8.39 | 一个有点好用的信息收集工具。A somewhat useful information gath<br>ering tool. |
### 漏洞利用框架
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [woodpecker-framew<br>ork-release](https://github.com/woodpecker-framework/woodpecker-framework-release) | 1.3.5 | 高危漏洞精准检测与深度利用框架 |
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
| [JNDIExploit](https://github.com/qi4L/JNDIExploit) |  |  |
| [JNDIExploit](https://github.com/WhiteHSBG/JNDIExploit) | v1.4 | 对原版https://github.com/feihong-cs/JNDIExploit 进行了实用化修<br>改 |
| [JNDIExploit-1](https://github.com/Mr-xn/JNDIExploit-1) | v1.2 | 一款用于 JNDI注入 利用的工具，大量参考/引用了 Rogue JNDI 项目<br>的代码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的<br>方式，适用于与自动化工具配合使用。（from https://github.com/feih<br>ong-cs/JNDIExploit） |
| [JNDIExploit](https://github.com/0x727/JNDIExploit) | 1.1 | 一款用于JNDI注入利用的工具，大量参考/引用了Rogue JNDI项目的代<br>码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的方式<br>，适用于与自动化工具配合使用。 |
| [Exp-Tools](https://github.com/cseroad/Exp-Tools) | v1.2.1 | 一款集成高危漏洞exp的实用性工具 |
### 重点CMS利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [LandrayExploit](https://github.com/yuanhaiGreg/LandrayExploit) |  |  |
| [weaver_exp](https://github.com/z1un/weaver_exp) |  | 泛微OA漏洞综合利用脚本 |
| [EgGateWayGetShell](https://github.com/Tas9er/EgGateWayGetShell) |  | Code By:Tas9er |
| [CMSmap](https://github.com/Dionach/CMSmap) |  | CMSmap is a python open source CMS scanner that automates the <br>process of detecting security flaws of the most popular CMSs.  |
| [wpreconx](https://github.com/blackcrw/wpreconx) | 2.4.5 | WPRecon, is a tool for the recognition of vulnerabilities and <br>blackbox information for wordpress. |
| [wordpress-exploit<br>-framework](https://github.com/rastating/wordpress-exploit-framework) | v2.0.1 | A Ruby framework designed to aid in the penetration testing of<br> WordPress systems.  |
| [wpscan](https://github.com/wpscanteam/wpscan) | v3.8.24 | WPScan WordPress security scanner. Written for security profes<br>sionals and blog maintainers to test the security of their Word<br>Press websites. Contact us via contact@wpscan.com |
| [wprecon](https://github.com/AngraTeam/wprecon) |  |  |
| [Apt_t00ls](https://github.com/White-hua/Apt_t00ls) | v0.7 | 高危漏洞利用工具 |
| [QVD-2023-13065](https://github.com/qi4L/QVD-2023-13065) |  | Nacos JRaft Hessian 反序列化 RCE EXP |
| [hikvision_CVE-201<br>7-7921_auth_bypass<br>_config_decryptor](https://github.com/chrisjd20/hikvision_CVE-2017-7921_auth_bypass_config_decryptor) |  | This python file will decrypt the configurationFile used by hi<br>kvision cameras vulnerable to CVE-2017-7921. |
| [CVE-2023-33246](https://github.com/SuperZero/CVE-2023-33246) |  | Apache RocketMQ 远程代码执行漏洞(CVE-2023-33246) Exploit |
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
| [vulcat](https://github.com/CLincat/vulcat) | v2.0.0 | vulcat可用于扫描Web端常见的CVE、CNVD等编号的漏洞，发现漏洞时会<br>返回Payload信息。部分漏洞还支持命令行交互模式，可以持续利用漏洞 |
## 漏洞检测利用库
### 服务漏洞
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
#### 数据库利用
##### redis
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [redis-rogue-serve<br>r](https://github.com/n0b0dyCN/redis-rogue-server) |  | Redis(<=5.0.5) RCE |
| [RedisEXP](https://github.com/yuyan-sec/RedisEXP) | 0.0.3 | Redis 漏洞利用工具 |
| [redis_rce](https://github.com/zyylhn/redis_rce) | v0.1.0 | Redis primary/secondary replication RCE |
| [redis-rce](https://github.com/Ridter/redis-rce) |  | Redis 4.x/5.x RCE |
| [redis-rogue-serve<br>r](https://github.com/Dliv3/redis-rogue-server) |  | Redis 4.x/5.x RCE |
##### mssql
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SharpSQLTools](https://github.com/uknowsec/SharpSQLTools) | 41 | SharpSQLTools 和@Rcoil一起写的小工具，可上传下载文件，xp_cmdsh<br>ell与sp_oacreate执行命令回显和clr加载程序集执行相应操作。 |
| [mssqlproxy](https://github.com/blackarrowsec/mssqlproxy) | 0.1 | mssqlproxy is a toolkit aimed to perform lateral movement in r<br>estricted environments through a compromised Microsoft SQL Serv<br>er via socket reuse |
##### Oracle
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [odat](https://github.com/quentinhardy/odat) | 5.1.1 | ODAT: Oracle Database Attacking Tool |
##### postgresql
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [postgresql_udf_he<br>lp](https://github.com/No-Github/postgresql_udf_help) |  | PostgreSQL 提权辅助脚本 |
##### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [MDUT](https://github.com/SafeGroceryStore/MDUT) | v2.1.1 | MDUT - Multiple Database Utilization Tools |
| [RequestTemplate](https://github.com/1n7erface/RequestTemplate) |  |  |
| [Databasetools](https://github.com/Hel10-Web/Databasetools) | 1.2 | 一款用Go语言编写的数据库自动化提权工具，支持Mysql、MSSQL、Post<br>gresql、Oracle、Redis数据库提权、命令执行、爆破以及ssh连接 |
### 常规web漏洞
#### XSS
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dalfox](https://github.com/hahwul/dalfox) | v2.9.0 | 🌙🦊 Dalfox is a powerful open-source XSS scanner and utility <br>focused on automation. |
| [findom-xss](https://github.com/dwisiswant0/findom-xss) |  | A fast DOM based XSS vulnerability scanner with simplicity. |
| [Chromium-based-XS<br>S-Taint-Tracking](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) | v0.3 | Cyclops 是一款具有 XSS 检测功能的浏览器 |
| [beef](https://github.com/beefproject/beef) | v0.5.4.<br>0 | The Browser Exploitation Framework Project |
| [xsscrapy](https://github.com/DanMcInerney/xsscrapy) |  | XSS spider - 66/66 wavsep XSS detected |
#### SQL注入
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | 1.7 | Automatic SQL injection and database takeover tool |
| [ghauri](https://github.com/r0oth3x49/ghauri) | 1.2.4 | An advanced cross-platform tool that automates the process of <br>detecting and exploiting SQL injection security flaws |
#### CLRF
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CRLFsuite](https://github.com/Nefcore/CRLFsuite) |  |  |
#### CORS
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CORScanner](https://github.com/chenjj/CORScanner) | 1.0.1 | 🎯 Fast CORS misconfiguration vulnerabilities scanner |
#### XXE
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [oxml_xxe](https://github.com/BuffaloWill/oxml_xxe) |  | A tool for embedding XXE/XML exploits into different filetypes |
| [docem](https://github.com/whitel1st/docem) | 1.3 |   Uility to embed XXE and XSS payloads in docx,odt,pptx,etc (O<br>XML_XEE on steroids) |
#### SSTI
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SSTImap](https://github.com/vladko312/SSTImap) | v1.1 | Automatic SSTI detection tool with interactive interface |
| [tplmap](https://github.com/epinna/tplmap) | v0.5 | Server-Side Template Injection and Code Injection Detection an<br>d Exploitation Tool |
#### SSRF
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ssrf-sheriff](https://github.com/teknogeek/ssrf-sheriff) |  | A simple SSRF-testing sheriff written in Go |
| [SSRFmap](https://github.com/swisskyrepo/SSRFmap) |  | Automatic SSRF fuzzer and exploitation tool |
#### JWT
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jwt_tool](https://github.com/ticarpi/jwt_tool) | v2.2.6 | :snake: A toolkit for testing, tweaking and cracking JSON Web <br>Tokens |
| [jwt-hack](https://github.com/hahwul/jwt-hack) | v1.1.2 | 🔩 jwt-hack is tool for hacking / security testing to JWT. Sup<br>ported for En/decoding JWT, Generate payload for JWT attack and<br> very fast cracking(dict/brutefoce) |
#### DOS
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [slowhttptest](https://github.com/shekyan/slowhttptest) | v1.9.0 | Application Layer DoS attack simulator |
#### 文件包含
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [liffy](https://github.com/mzfr/liffy) |  | Local file inclusion exploitation tool |
#### 解析漏洞
##### Nginx
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [nginxpwner](https://github.com/stark0de/nginxpwner) |  | Nginxpwner is a simple tool to look for common Nginx misconfig<br>urations and vulnerabilities. |
### 信息泄露漏洞
#### key泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Cloud-Bucket-Leak<br>-Detection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | v0.4.0 | 六大云存储，泄露利用检测工具 |
| [aksk_tool](https://github.com/wyzxxz/aksk_tool) |  | AK资源管理工具，阿里云/腾讯云/华为云/AWS/UCLOUD/京东云/百度云/<br>七牛云存储  AccessKey AccessKeySecret，利用AK获取资源信息和操作<br>资源，ECS/CVM/E2/UHOST/ECI/BCC执行命令，OSS/COS/S3/BOS管理，RDS/<br>DB管理，域名管理，添加RAM/CAM/IAM账号等 |
| [AliyunAccessKeyTo<br>ols](https://github.com/NS-Sp4ce/AliyunAccessKeyTools) | 1.0 | 阿里云AccessKey泄漏利用工具 |
| [cf](https://github.com/teamssix/cf) |  |  |
#### swagger接口
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [swagger-exp](https://github.com/lijiejie/swagger-exp) |  | A Swagger API Exploit |
| [swagger-hack](https://github.com/jayus0821/swagger-hack) |  | 自动化爬取并自动测试所有swagger接口 |
#### heapdump泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [heapdump_tool](https://github.com/wyzxxz/heapdump_tool) |  | heapdump敏感信息查询工具，例如查找 spring heapdump中的密码明文<br>，AK,SK等 |
| [JDumpSpider](https://github.com/whwlsfb/JDumpSpider) | dev-202<br>30406T03<br>1230 | HeapDump敏感信息提取工具 |
#### Webpack接口
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Packer-Fuzzer](https://github.com/rtcatc/Packer-Fuzzer) | v1.4 | Packer Fuzzer is a fast and efficient scanner for security det<br>ection of websites constructed by javascript module bundler suc<br>h as Webpack.  |
#### .git泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [GitHack](https://github.com/BugScanTeam/GitHack) |  | .git 泄漏利用工具，可还原历史版本 |
| [git-dumper](https://github.com/arthaud/git-dumper) |  | A tool to dump a git repository from a website |
| [GitDorker](https://github.com/obheda12/GitDorker) |  | A Python program to scrape secrets from GitHub through usage o<br>f a large repository of dorks. |
#### .DS_Store泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ds_store_exp](https://github.com/lijiejie/ds_store_exp) |  | A .DS_Store file disclosure exploit.   It parses .DS_Store fil<br>e and downloads files recursively. |
#### .svn泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [svnExploit](https://github.com/admintony/svnExploit) |  | SvnExploit支持SVN源代码泄露全版本Dump源码 |
#### 代码泄露综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dvcs-ripper](https://github.com/kost/dvcs-ripper) |  | Rip web accessible (distributed) version control systems: SVN/<br>GIT/HG... |
#### 敏感数据泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SecretFinder](https://github.com/m4ll0k/SecretFinder) |  | SecretFinder - A python script for find sensitive data (apikey<br>s, accesstoken,jwt,..) and search anything on javascript files  |
| [JSFScan.sh](https://github.com/KathanP19/JSFScan.sh) |  | Automation for javascript recon in bug bounty.  |
| [Mantra](https://github.com/MrEmpy/Mantra) | v.1.1 | 「🔑」A tool used to hunt down API key leaks in JS files and p<br>ages |
### 子域接管
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SubOver](https://github.com/Ice3man543/SubOver) | v1.2 | A Powerful Subdomain Takeover Tool |
### 编辑器漏洞
#### UEditor
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [UEditorGetShell](https://github.com/Tas9er/UEditorGetShell) |  | UEditor编辑器批量GetShell / Code By:Tas9er |
### 产品/组件/框架漏洞
#### Apache Dubbo
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dubbo-exp](https://github.com/threedr3am/dubbo-exp) |  | dubbo学习demo，之前删了，重新上传。 |
#### Apache Shiro
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shiro_rce_tool](https://github.com/wyzxxz/shiro_rce_tool) |  | shiro 反序列 命令执行辅助检测工具 |
| [ShiroAttack2](https://github.com/SummerSec/ShiroAttack2) | 4.7.0 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复<br>原版中NoCC的问题 https://github.com/j1anFen/shiro_attack |
| [shiro_attack](https://github.com/j1anFen/shiro_attack) | 2.2 | shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马） |
| [ShiroExploit-Depr<br>ecated](https://github.com/feihong-cs/ShiroExploit-Deprecated) | v2.51 | Shiro550/Shiro721 一键化利用工具，支持多种回显方式 |
#### Apache Struts2
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [STS2G](https://github.com/xfiftyone/STS2G) | 1.0 | Struts2漏洞扫描利用工具 - Golang版. Struts2 Scanner Written in<br> Golang |
| [Struts2-Scan](https://github.com/HatBoy/Struts2-Scan) |  | Struts2全漏洞扫描利用工具 |
#### Apache Tomcat
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [AttackTomcat](https://github.com/tpt11fb/AttackTomcat) | V1 | Tomcat常见漏洞GUI利用工具。CVE-2017-12615 PUT文件上传漏洞、tom<br>cat-pass-getshell 弱认证部署war包、弱口令爆破、CVE-2020-1938 To<br>mcat AJP文件读取/包含 |
| [Tomcat_PUT_GUI_EX<br>P](https://github.com/xiaokp7/Tomcat_PUT_GUI_EXP) | 1.4 | Tomcat PUT方法任意文件写入（CVE-2017-12615）exp |
#### Fastjson
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [FastjsonScan](https://github.com/a1phaboy/FastjsonScan) | v1.1 | Fastjson扫描器，可识别版本、依赖库、autoType状态等。A tool to <br>distinguish fastjson ,version and dependency |
| [Fastjson](https://github.com/safe6Sec/Fastjson) |  | Fastjson姿势技巧集合 |
| [FastjsonVulns](https://github.com/hosch3n/FastjsonVulns) |  | [fastjson 1.2.80] CVE-2022-25845 aspectj fileread & groovy rem<br>ote classload |
| [fastjson-autotype<br>-bypass-dem](https://github.com/iSafeBlue/fastjson-autotype-bypass-dem) |  |  |
| [FastjsonExploit](https://github.com/c0ny1/FastjsonExploit) |  | Fastjson vulnerability quickly exploits the framework（fastjso<br>n漏洞快速利用框架） |
| [fastjson_rec_expl<br>oit](https://github.com/mrknow001/fastjson_rec_exploit) |  | fastjson一键命令执行 |
#### JBoss
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [jexboss](https://github.com/joaomatosf/jexboss) |  | JexBoss: Jboss (and Java Deserialization Vulnerabilities) veri<br>fy and EXploitation Tool |
#### vmware
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Vm4J](https://github.com/NS-Sp4ce/Vm4J) |  | A tool for detect&exploit vmware product log4j(cve-2021-44228)<br> vulnerability.Support VMware HCX/vCenter/NSX/Horizon/vRealize <br>Operations Manager |
| [VcenterKiller](https://github.com/Schira4396/VcenterKiller) | v1.3.6 | 一款针对Vcenter的综合利用工具，包含目前最主流的CVE-2021-21972<br>、CVE-2021-21985以及CVE-2021-22005、One Access的CVE-2022-22954、<br>CVE-2022-22972/31656以及log4j，提供一键上传webshell，命令执行或<br>者上传公钥使用SSH免密连接 |
#### log4j
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [log4j-shell-poc](https://github.com/kozmer/log4j-shell-poc) |  | A Proof-Of-Concept for the CVE-2021-44228 vulnerability.  |
#### Spring Boot
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SpringExploit](https://github.com/SummerSec/SpringExploit) | 0.1.9 | 🚀 一款为了学习go而诞生的漏洞利用工具 |
| [SpringBootExploit](https://github.com/0x727/SpringBootExploit) | 1.3 | 项目是根据LandGrey/SpringBootVulExploit清单编写，目的hvv期间快<br>速利用漏洞、降低漏洞利用门槛。 |
| [SpringBoot-Scan-G<br>UI](https://github.com/13exp/SpringBoot-Scan-GUI) | v1.2.2 |  |
#### Thinkphp
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Aazhen-RexHa](https://github.com/zangcc/Aazhen-RexHa) |  | 自研JavaFX图形化漏洞扫描工具，支持扫描的漏洞分别是： ThinkPHP-<br>2.x-RCE， ThinkPHP-5.0.23-RCE， ThinkPHP5.0.x-5.0.23通杀RCE， T<br>hinkPHP5-SQL注入&敏感信息泄露， ThinkPHP 3.x 日志泄露NO.1， Thi<br>nkPHP 3.x 日志泄露NO.2， ThinkPHP 5.x 数据库信息泄露的漏洞检测<br>，以及批量检测的功能。漏洞POC基本适用ThinkPHP全版本漏洞。 |
| [ThinkphpGUI](https://github.com/Lotus6/ThinkphpGUI) | 1.3 | Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，get<br>shell。 |
| [thinkphp_gui_tool<br>s](https://github.com/bewhale/thinkphp_gui_tools) | v2.4.2 | ThinkPHP漏洞综合利用工具, 图形化界面, 命令执行, 一键getshell, <br>批量检测, 日志遍历, session包含,宝塔绕过 |
#### Weblogic
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [weblogic-framewor<br>k](https://github.com/dream0x01/weblogic-framework) | v0.2.3 | weblogic-framework is the best tool for detecting weblogic vul<br>nerabilities. |
| [WeblogicTool](https://github.com/KimJun1010/WeblogicTool) | v1.2 | WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马<br>注入、密码解密等（深信服深蓝实验室天威战队强力驱动） |
| [CVE-2023-21839](https://github.com/4ra1n/CVE-2023-21839) |  | Weblogic CVE-2023-21839 / CVE-2023-21931 / CVE-2023-21979 一键<br>检测 |
| [Decrypt_Weblogic_<br>Password](https://github.com/TideSec/Decrypt_Weblogic_Password) |  | 搜集了市面上绝大部分weblogic解密方式，整理了7种解密weblogic的<br>方法及响应工具。 |
#### SmartBI
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SmartBIAttackTool](https://github.com/yggo/SmartBIAttackTool) | v1.0 | SmartBI 登录代码逻辑漏洞导致的远程代码执行利用工具 |
#### Hikvision
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [HikvisionDecode](https://github.com/baogod404/HikvisionDecode) |  |  |
### OA产品漏洞
#### 通达OA
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [TongdaOATools](https://github.com/xiaokp7/TongdaOATools) | V1.2 | 通达OAEXP合集大礼包 |
| [TDOA_RCE](https://github.com/xinyu2428/TDOA_RCE) | v1.0 | 通达OA综合利用工具 |
#### 用友OA
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [fupo_for_yonyou](https://github.com/novysodope/fupo_for_yonyou) | 2.0RC1 | 用友漏洞检测，持续更新漏洞检测模块 |
| [yonyou_exp_plus](https://github.com/li8u99/yonyou_exp_plus) |  | 用友系列全漏洞检测工具 |
| [yonyou-nc-decrypt<br>er](https://github.com/woodpecker-appstore/yonyou-nc-decrypter) | 0.1.0 | 用友 nc 系列密码解密 |
#### 致远OA
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [seeyon_exp](https://github.com/Summer177/seeyon_exp) |  | 致远OA综合利用工具 |
| [SeeyonExploit-GUI](https://github.com/God-Ok/SeeyonExploit-GUI) |  | 致远OA综合利用工具V1.0 |
| [PassDecode-jar](https://github.com/Rvn0xsy/PassDecode-jar) | v0.1 | 帆软/致远密码解密工具 |
#### OA综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL) | 0.83 | OA综合利用工具，集合将近20款OA漏洞批量扫描 |
| [MYExploit](https://github.com/achuna33/MYExploit) | V2.0.4 | OAExploit一款基于产品的一键扫描工具。 |
### 数据库漏洞利用
#### 数据库自动化提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Databasetools](https://github.com/Hel10-Web/Databasetools) | 1.2 | 一款用Go语言编写的数据库自动化提权工具，支持Mysql、MSSQL、Post<br>gresql、Oracle、Redis数据库提权、命令执行、爆破以及ssh连接 |
## 漏洞文库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [bylibrary](https://github.com/BaizeSec/bylibrary) |  | 白阁文库是白泽Sec安全团队维护的一个漏洞POC和EXP公开项目 |
| [PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book) |  | 面向网络安全从业者的知识文库🍃 |
| [VulWiki](https://github.com/Ares-X/VulWiki) |  | VulWiki |
| [vulbase](https://github.com/cckuailong/vulbase) |  | 各大漏洞文库合集 |
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC) |  | 一个各类漏洞POC知识库 |
| [Vulnerability-Wik<br>i](https://github.com/Threekiii/Vulnerability-Wiki) | v1.0 | 基于 docsify 部署，目前漏洞数量 999+ |
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
| [WebshellManager](https://github.com/boy-hack/WebshellManager) |  | w8ay 一句话WEB端管理工具 |
| [Cknife](https://github.com/Chora10/Cknife) |  | Cknife |
| [Behinder](https://github.com/rebeyond/Behinder) | Behinde<br>r_v4.0.6 | “冰蝎”动态二进制加密网站管理客户端 |
| [Godzilla](https://github.com/BeichenDream/Godzilla) | v4.0.1-<br>godzilla | 哥斯拉 |
| [antSword](https://github.com/AntSwordProject/antSword) | 2.1.15 | 中国蚁剑是一款跨平台的开源网站管理工具。AntSword is a cross-pl<br>atform website management toolkit. |
| [Platypus](https://github.com/WangYihang/Platypus) | v1.5.0 | :hammer: A modern multiple reverse shell sessions manager writ<br>ten in go |
| [As-Exploits](https://github.com/yzddmr6/As-Exploits) |  | 中国蚁剑后渗透框架 |
| [Webshell_Generate](https://github.com/cseroad/Webshell_Generate) | v1.2.3 | 用于生成各类免杀webshell |
### webshell
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [webshell](https://github.com/backlion/webshell) |  | 这是一些常用的webshell |
### 后门
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CreateHiddenAccou<br>nt](https://github.com/wgpsec/CreateHiddenAccount) | 0.2 | A tool for creating hidden accounts using the registry || 一个<br>使用注册表创建隐藏帐户的工具 |
| [SchTask_0x727](https://github.com/0x727/SchTask_0x727) | v1.0 | 创建隐藏计划任务，权限维持，Bypass AV |
| [CloneX_0x727](https://github.com/0x727/CloneX_0x727) | 1.0 | 进行克隆用户、添加用户等账户防护安全检测的轻巧工具 |
### 远控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [noterce](https://github.com/xiao-zhu-zhu/noterce) | 1.3 | 一种另辟蹊径的免杀执行系统命令的木马 |
| [Supershell](https://github.com/tdragon6/Supershell) | latest | Supershell C2 远控平台，基于反向SSH隧道获取完全交互式Shell |
| [SimpleRemoter](https://github.com/yuanyuanxiang/SimpleRemoter) | v1.0.0.<br>5 | 基于gh0st的远程控制器：实现了终端管理、进程管理、窗口管理、远<br>程桌面、文件管理、语音管理、视频管理、服务管理、注册表管理等功能<br>，优化全部代码及整理排版，修复内存泄漏缺陷，程序运行稳定。项目代<br>码仅限于学习和交流用途。 |
| [trojan_simple_dem<br>o](https://github.com/Ciyfly/trojan_simple_demo) |  | 简单的用python写的远控demo 执行命令 只一个心跳完成所有操作 |
### 免杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shellcodeloader](https://github.com/knownsec/shellcodeloader) | v1.1 | shellcodeloader |
| [AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool) | 2023082<br>3 | 掩日 - 免杀执行器生成工具 |
| [GobypassAV-shellc<br>ode](https://github.com/Pizz33/GobypassAV-shellcode) |  | shellcode免杀加载器，使用go实现，免杀bypass火绒、360、核晶、de<br>f等主流杀软 |
| [ZheTian](https://github.com/yqcs/ZheTian) | v3 | ::ZheTian / 强大的免杀生成工具，Bypass All. |
| [encdecshellcode](https://github.com/blacknbunny/encdecshellcode) |  | Shellcode Encrypter & Decrypter via XOR Cipher |
| [SysWhispers2](https://github.com/jthuraisamy/SysWhispers2) |  | AV/EDR evasion via direct system calls. |
| [killEscaper](https://github.com/Anyyy111/killEscaper) |  | Shellcode 免杀生成器 绕过火绒、360（Windows版本） |
| [ShellCode_Loader](https://github.com/Axx8/ShellCode_Loader) | v0.0.1 | ShellCode_Loader - Msf&CobaltStrike免杀ShellCode加载器、Shellc<br>ode_encryption - 免杀Shellcode加密生成工具，目前测试免杀360&火<br>绒&电脑管家&Windows Defender（其他杀软未测试）。 |
| [shellcodeloader](https://github.com/knownsec/shellcodeloader) | v1.1 | shellcodeloader |
| [AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool) | 2023082<br>3 | 掩日 - 免杀执行器生成工具 |
| [GoBypassAV](https://github.com/TideSec/GoBypassAV) |  | 整理了基于Go的16种API免杀测试、8种加密测试、反沙盒测试、编译混<br>淆、加壳、资源修改等免杀技术，并搜集汇总了一些资料和工具。 |
| [bypassAV](https://github.com/pureqh/bypassAV) |  | 免杀shellcode加载器 |
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
| [PEASS-ng](https://github.com/carlospolop/PEASS-ng) | 2023090<br>3-188479<br>ae | PEASS - Privilege Escalation Awesome Scripts SUITE (with color<br>s) |
| | | https://i.hacking8.com/tiquan/ |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Kernelhub](https://github.com/Ascotbe/Kernelhub) | v1.1 | :palm_tree:Linux、macOS、Windows Kernel privilege escalation v<br>ulnerability collection, with compilation environment, demo GIF<br> map, vulnerability details, executable file  (提权漏洞合集)  |
### 容器提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [container-escape-<br>check](https://github.com/teamssix/container-escape-check) | v0.3 | docker container escape check || Docker 容器逃逸检测 |
| [CDK](https://github.com/cdk-team/CDK) | v1.5.2 | 📦  Make security testing of K8s, Docker, and Containerd easie<br>r. |
## 内网渗透
### 信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SharpHostInfo](https://github.com/shmilylty/SharpHostInfo) | v0.0.1 | SharpHostInfo是一款快速探测内网主机信息工具（深信服深蓝实验室<br>天威战队强力驱动） |
| [HostInfoScan](https://github.com/Y0-kan/HostInfoScan) |  | 红队小工具 | 利用DCERPC协议，无需认证获取Windows机器主机信息和<br>多网卡信息 |
| [ATAttack](https://github.com/c1y2m3/ATAttack) |  | 敌后侦察 |
### 网段探测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [netspy](https://github.com/shmilylty/netspy) | v0.0.5 | netspy是一款快速探测内网可达网段工具（深信服深蓝实验室天威战队<br>强力驱动） |
### 代理转发
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| | | https://www.proxifier.com/ |
| | | http://rootkiter.com/Termite/ |
| [reGeorg](https://github.com/sensepost/reGeorg) |  | The successor to reDuh, pwn a bastion webserver and create SOC<br>KS proxies through the DMZ. Pivot and pwn. |
| [Neo-reGeorg](https://github.com/L-codes/Neo-reGeorg) | v5.1.0 | Neo-reGeorg is a project that seeks to aggressively refactor r<br>eGeorg |
| [suo5](https://github.com/zema1/suo5) | v0.9.0 | 一款高性能 HTTP 代理隧道工具 | A high-performance http proxy t<br>unneling tool |
| [slcx](https://github.com/sechelper/slcx) | v1.0.2 | 端口转发工具，绕过流量安全检测。 |
| [pystinger](https://github.com/FunnyWolf/pystinger) | v1.6 | Bypass firewall for traffic forwarding using webshell 一款使用<br>webshell进行流量转发的出网工具 |
| [Stowaway](https://github.com/ph4ntonn/Stowaway) | v2.1 | 👻Stowaway -- Multi-hop Proxy Tool for pentesters |
| [PortForward](https://github.com/knownsec/PortForward) | 0.5.0 | The port forwarding tool developed by Golang solves the proble<br>m that the internal and external networks cannot communicate in<br> certain scenarios |
| [rakshasa](https://github.com/Mob2003/rakshasa) | v0.2.3 | 基于go编写的跨平台、稳定、隐秘的多级代理内网穿透工具 |
| [nps](https://github.com/ehang-io/nps) | v0.26.1<br>0 | 一款轻量级、高性能、功能强大的内网穿透代理服务器。支持tcp、udp<br>、socks5、http等几乎所有流量转发，可用来访问内网网站、本地支付接<br>口调试、ssh访问、远程桌面，内网dns解析、内网socks5代理等等……，<br>并带有功能强大的web管理端。a lightweight, high-performance, powe<br>rful intranet penetration proxy server, with a powerful web man<br>agement terminal. |
| [frp](https://github.com/fatedier/frp) | v0.51.3 | A fast reverse proxy to help you expose a local server behind <br>a NAT or firewall to the internet. |
| [Erfrp](https://github.com/Goqi/Erfrp) | v0.1 | Erfrp-frp二开-免杀与隐藏 |
| [frp_cmd](https://github.com/OrangeWatermelon/frp_cmd) | v0.38.0<br>_modify | frp修改版，增加socks、pf命令，便捷启用socks5代理、端口转发，且<br>去除流量特征，增加loadini命令，支持命令行参数导入base64编码的配<br>置文件 |
| [dns2tcp](https://github.com/alex-sector/dns2tcp) | v0.5.2 |  |
| [dnscat2](https://github.com/iagox86/dnscat2) |  |  |
| [icmpsh](https://github.com/inquisb/icmpsh) |  |  |
| [pingtunnel](https://github.com/esrrhs/pingtunnel) | 2.7 | Pingtunnel is a tool that send TCP/UDP traffic over ICMP |
| [ngrok](https://github.com/inconshreveable/ngrok) |  | Introspected tunnels to localhost |
| [goproxy](https://github.com/snail007/goproxy) | v13.9 | 🔥  Proxy is a high performance HTTP(S) proxies, SOCKS5 proxie<br>s,WEBSOCKET, TCP, UDP proxy server implemented by golang. Now, <br>it supports chain-style proxies,nat forwarding in different lan<br>,TCP/UDP port forwarding, SSH forwarding.Proxy是golang实现的高<br>性能http,https,websocket,tcp,socks5代理服务器,支持内网穿透,链式<br>代理,通讯加密,智能HTTP,SOCKS5代理,黑白名单,限速,限流量,限连接数,<br>跨平台,KCP支持,认证API。 |
### 密码提取
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [vhost_password_de<br>crypt](https://github.com/shmilylty/vhost_password_decrypt) |  | vhost password decrypt |
| [mimikatz](https://github.com/gentilkiwi/mimikatz) | 2.2.0-2<br>0220919 | A little tool to play with Windows security |
| [goLazagne](https://github.com/kerbyj/goLazagne) |  | Go library for credentials recovery  |
| [win-brute-logon](https://github.com/DarkCoderSc/win-brute-logon) |  | Crack any Microsoft Windows users password without any privile<br>ge (Guest account included) |
| [fakelogonscreen](https://github.com/bitsadmin/fakelogonscreen) | 1.1 | Fake Windows logon screen to steal passwords |
| [FinalShell-Decode<br>r](https://github.com/passer-W/FinalShell-Decoder) | V1.0 | FinallShell 密码解密GUI工具 |
| [SharpXDecrypt](https://github.com/JDArmy/SharpXDecrypt) | v0.1.4 | Xshell全版本密码恢复工具 |
| [Xdecrypt](https://github.com/dzxs/Xdecrypt) |  | Xshell Xftp password decrypt |
| [SharpDecryptPwd](https://github.com/RowTeam/SharpDecryptPwd) |  | SharpDecryptPwd source, To Decrypt Navicat,Xmanager,Filezilla,<br>Foxmail,WinSCP,etc |
| [SharpDecryptPwd](https://github.com/ianxtianxt/SharpDecryptPwd) |  | Windows常用程序密码读取工具：SharpDecryptPwd |
| [SharpDBeaver](https://github.com/lele8/SharpDBeaver) |  | DBeaver数据库密码解密工具 |
| [SharpDecryptPwd](https://github.com/uknowsec/SharpDecryptPwd) |  | 对密码已保存在 Windwos 系统上的部分程序进行解析,包括：Navicat,<br>TeamViewer,FileZilla,WinSCP,Xmangager系列产品（Xshell,Xftp)。源<br>码：https://github.com/RowTeam/SharpDecryptPwd |
| [TeamViewer](https://github.com/wafinfo/TeamViewer) |  | TeamView Get PassWord |
| [HackBrowserData](https://github.com/moonD4rk/HackBrowserData) | v0.4.4 | Decrypt passwords/cookies/history/bookmarks from the browser. <br>一款可全平台运行的浏览器数据导出解密工具。 |
| [SharpWeb](https://github.com/djhohnstein/SharpWeb) | v1.2 | .NET 2.0 CLR project to retrieve saved browser credentials fro<br>m Google Chrome, Mozilla Firefox and Microsoft Internet Explore<br>r/Edge. |
| [360SafeBrowserget<br>pass](https://github.com/hayasec/360SafeBrowsergetpass) | v0.1 | 这是一个一键辅助抓取360安全浏览器密码的CobaltStrike脚本以及解<br>密小工具，用于节省红队工作量，通过下载浏览器数据库、记录密钥来离<br>线解密浏览器密码。 |
| [BrowserGhost](https://github.com/QAX-A-Team/BrowserGhost) | 1 | 这是一个抓取浏览器密码的工具，后续会添加更多功能 |
| [Browser-cookie-st<br>eal](https://github.com/DeEpinGh0st/Browser-cookie-steal) |  | Python script for steal browser cookies |
| [getIntrInfo](https://github.com/Potato-py/getIntrInfo) |  | 收集内部网信息。包括：浏览器书签、密码和浏览历史记录、cookie。<br>Wifi信息和密码。主机信息。 |
| [SharpDPAPI](https://github.com/GhostPack/SharpDPAPI) |  | SharpDPAPI is a C# port of some Mimikatz DPAPI functionality. |
### 漏洞发现
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InScan](https://github.com/inbug-team/InScan) |  | 边界打点后的自动化渗透工具 |
| [kscan](https://github.com/lcvvvv/kscan) | v1.85 | Kscan是一款纯go开发的全方位扫描器，具备端口扫描、协议检测、指<br>纹识别，暴力破解等功能。支持协议1200+，协议指纹10000+，应用指纹2<br>0000+，暴力破解协议10余种。 |
| [fscan](https://github.com/shadow1ng/fscan) | 1.8.2 | 一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。 |
| [Gscan](https://github.com/hack2fun/Gscan) | v1.0 | Gscan is a high concurrency scanner based on golang |
| [ServerScan](https://github.com/Adminisme/ServerScan) | v1.0.2 | ServerScan一款使用Golang开发的高并发网络扫描、服务探测工具。 |
| [ADCSKiller](https://github.com/grimlockx/ADCSKiller) |  | An ADCS Exploitation Automation Tool Weaponizing Certipy and C<br>oercer |
| [goon](https://github.com/i11us0ry/goon) | v3.5 | goon,集合了fscan和kscan等优秀工具功能的扫描爆破工具。功能包含<br>：ip探活、port扫描、web指纹扫描、title扫描、压缩文件扫描、fofa获<br>取、ms17010、mssql、mysql、postgres、redis、ssh、smb、rdp、telne<br>t、tomcat等爆破以及如netbios探测等功能。 |
| [Template](https://github.com/1n7erface/Template) | v1.2.1 | Next generation RedTeam heuristic intranet scanning | 下一代Re<br>dTeam启发式内网扫描 |
### 漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Viper](https://github.com/FunnyWolf/Viper) | 2023083<br>1 | Redteam operation  platform with webui 图形化红队行动辅助平台 |
### 横向工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WMIHACKER](https://github.com/rootclay/WMIHACKER) |  | A Bypass Anti-virus Software Lateral Movement Command Executio<br>n Tool |
| [sharpwmi](https://github.com/QAX-A-Team/sharpwmi) | v2 | sharpwmi是一个基于rpc的横向移动工具，具有上传文件和执行命令功<br>能。 |
| [impacket](https://github.com/fortra/impacket) | impacke<br>t_0_11_0 | Impacket is a collection of Python classes for working with ne<br>twork protocols. |
| [wmiexec-Pro](https://github.com/XiaoliChan/wmiexec-Pro) | v0.2.6 | New generation of wmiexec.py |
| [taowu-cobalt-stri<br>ke](https://github.com/pandasec888/taowu-cobalt-strike) |  |  |
| [OLa](https://github.com/d3ckx1/OLa) | OLa__20<br>220724 |  |
| | | https://xz.aliyun.com/t/9382 |
| [VMInjector](https://github.com/hzphreak/VMInjector) |  | DLL Injection tool to unlock guest VMs |
### 域渗透工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ShuiYing_0x727](https://github.com/0x727/ShuiYing_0x727) | V1.0 | 检测域环境内，域机器的本地管理组成员是否存在弱口令和通用口令，<br>对域用户的权限分配以及域内委派查询 |
| [BloodHound](https://github.com/BloodHoundAD/BloodHound) | v4.3.1 | Six Degrees of Domain Admin |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Ladon](https://github.com/k8gege/Ladon) | v11.4 | Ladon大型内网渗透工具，可PowerShell模块化、可CS插件化、可内存<br>加载，无文件扫描。含端口扫描、服务识别、网络资产探测、密码审计、<br>高危漏洞检测、漏洞利用、密码读取以及一键GetShell，支持批量A段/B<br>段/C段以及跨网段扫描，支持URL、主机、域名列表扫描等。Ladon 11.4<br>内置245个功能,网络资产探测模块32个通过多种协议(ICMP\NBT\DNS\MAC\<br>SMB\WMI\SSH\HTTP\HTTPS\Exchange\mssql\FTP\RDP)以及方法快速获取<br>目标网络存活主机IP、计算机名、工作组、共享资源、网卡地址、操作系<br>统版本、网站、子域名、中间件、开放服务、路由器、交换机、数据库、<br>打印机等信息，高危漏洞检测16个含MS17010、Zimbra、Exchange |
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
| [Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam) |  | 一个攻防知识仓库 |
| [Threathunting-boo<br>k](https://github.com/12306Bro/Threathunting-book) |  |  |
| [PenetrationTestti<br>ps](https://github.com/CYJoe-Cyclone/PenetrationTesttips) |  | 渗透测试Tips - Version1.3 |
| [Intranet_Penetrat<br>ion_Tips](https://github.com/Ridter/Intranet_Penetration_Tips) |  | 2018年初整理的一些内网渗透TIPS，后面更新的慢，所以整理出来希望<br>跟小伙伴们一起更新维护~ |
| [Vuln-List](https://github.com/wwl012345/Vuln-List) |  | (持续更新)对网上出现的各种OA、中间件、CMS等漏洞进行整理，主要<br>包括漏洞介绍、漏洞影响版本以及漏洞POC/EXP等，并且会持续更新。 |
| [1earn](https://github.com/ffffffff0x/1earn) |  | 暂停维护 | ffffffff0x 团队维护的安全知识框架,内容包括不仅限于 <br>web安全、工控安全、取证、应急、蓝队设施部署、后渗透、Linux安全<br>、各类靶机writup |
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
| [proxy_pool](https://github.com/jhao104/proxy_pool) | 2.4.1 | Python ProxyPool for web spider |
| [mubeng](https://github.com/kitabisa/mubeng) | v0.14.1 | An incredibly fast proxy checker & IP rotator with ease. |
| [Venom-Transponder](https://github.com/z-bool/Venom-Transponder) |  | 毒液流量转发器：自动化捡洞/打点/跳板必备神器，支持联动URL爬虫<br>、各种被动扫描器。 |
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
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.31 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等<br>），类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础<br>上，不影响APP、网站加解密正常逻辑等。 |
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
| [OneScan](https://github.com/vaycore/OneScan) | v1.2.1 | OneScan是递归目录扫描的BurpSuite插件 |
| [OutLook](https://github.com/KrystianLi/OutLook) |  |  |
| [passive-scan-clie<br>nt-plus](https://github.com/winezer0/passive-scan-client-plus) | v0.4.12<br>.0 | burpsuite passive-scan-client 插件维护分支 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpCRLFScan](https://github.com/A0WaQ4/BurpCRLFScan) | 1.4 | 使用java编写的CRLF-Injection-burp被动扫描插件 |
| [JsonDetect](https://github.com/a1phaboy/JsonDetect) | v1.0 | A burp Extender to detect json, include fastjson,jackson,gson |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.31 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等<br>），类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础<br>上，不影响APP、网站加解密正常逻辑等。 |
| [burp-text4shell](https://github.com/silentsignal/burp-text4shell) | v0.1 | Text4Shell scanner for Burp Suite |
| [sweetPotato](https://github.com/z2p/sweetPotato) | version<br>1.6 | 基于burpsuite的资产分析工具 |
| [xia_Liao](https://github.com/smxiazi/xia_Liao) | 1.6 | xia Liao（瞎料）burp插件 用于Windows在线进程/杀软识别 与 web渗<br>透注册时，快速生成需要的资料用来填写，资料包含：姓名、手机号、身<br>份证、统一社会信用代码、组织机构代码、银行卡，以及各类web语言的h<br>ello world输出和生成弱口令字典等。 |
| [base64encode](https://github.com/handbye/base64encode) | 1.0 | burpsuite POST数据包base64编码插件 |
| [HackTools](https://github.com/Vicl1fe/HackTools) | 1.5 | 提高渗透测试效率。#Burp插件##渗透测试##小工具# |
| [RouteVulScan](https://github.com/F6JO/RouteVulScan) | RouteVu<br>lScan1.5 | Burpsuite - Route Vulnerable Scanning 递归式被动检测脆弱路径的<br>burp插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) |  |  |
| [burp-awesome-tls](https://github.com/sleeyax/burp-awesome-tls) | v1.1.0 | Fixes Burp Suite's poor TLS stack. Bypass WAF, spoof any brows<br>er. |
| [JustC2file](https://github.com/Peithon/JustC2file) | v1.0.2 | Burp插件，Malleable C2 Profiles生成器；可以通过Burp代理选中请<br>求，生成Cobalt Strike的profile文件(CSprofile) |
| [SpringScan](https://github.com/metaStor/SpringScan) | V1.7 | SpringScan 漏洞检测 Burp插件 |
| [captcha-killer-mo<br>dified](https://github.com/f0ng/captcha-killer-modified) | 0.24.1 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免<br>费ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpFastJsonScan](https://github.com/pmiaowu/BurpFastJsonScan) | BurpFas<br>tJsonSca<br>n-2.2.2 | 一款基于BurpSuite的被动式FastJson检测插件 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [Log4j-check](https://github.com/bigsizeme/Log4j-check) |  | log4J burp被扫插件、CVE-2021-44228、支持dnclog.cn和burp内置DNS<br>、可配合JNDIExploit生成payload |
| [Log4j2Scan](https://github.com/whwlsfb/Log4j2Scan) | dev-202<br>30804T02<br>5448 | Log4j2 RCE Passive Scanner plugin for BurpSuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, s<br>upport AES/RSA/DES/ExecJs(execute JS encryption code in burpsui<br>te). 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSu<br>ite插件 |
| [BurpBountyPlus](https://github.com/ggg4566/BurpBountyPlus) | 3 | BurpBounty 魔改版本 |
| [BurpExtractor](https://github.com/NetSPI/BurpExtractor) | v1.3.4 | A Burp extension for generic extraction and reuse of data with<br>in HTTP requests and responses. |
| [burp-cph](https://github.com/elespike/burp-cph) | 3.0 | Custom Parameter Handler extension for Burp Suite. |
| [BurpJSLinkFinder](https://github.com/InitRoot/BurpJSLinkFinder) |  | Burp Extension for a passive scanning JS files for endpoint li<br>nks. |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9 | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集<br>；快速Title获取；外部工具联动；等等 |
| [JC-AntiToken](https://github.com/chroblert/JC-AntiToken) |  | burp插件：python版，token防重放绕过 |
| [BurpSuite_403Bypa<br>sser](https://github.com/sting8k/BurpSuite_403Bypasser) |  | Burpsuite Extension to bypass 403 restricted directory |
| [Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension) | v1.7.2 | Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suit<br>e. |
| [Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension) | v1.7.2 | Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suit<br>e. |
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
| [SpringVulScan](https://github.com/tpt11fb/SpringVulScan) | SpringV<br>ulScan-1<br>.1 | burpsuite 的Spring漏洞扫描插件。SpringVulScan：支持检测：路由<br>泄露|CVE-2022-22965|CVE-2022-22963|CVE-2022-22947|CVE-2016-4977 |
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
| [mitaka](https://github.com/ninoseki/mitaka) | v1.3.2 | A browser extension for OSINT search |
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
| [CyberChef](https://github.com/gchq/CyberChef) | v10.5.2 | The Cyber Swiss Army Knife - a web app for encryption, encodin<br>g, compression and data analysis |
### 取证分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pyvmx-cracker](https://github.com/axcheron/pyvmx-cracker) |  | Simple tool to crack VMware VMX encryption passwords |
| [chatViewTool](https://github.com/Ormicron/chatViewTool) | BEAT | 基于Java实现的图形化微信聊天记录解密查看器 |
| [Sharp-dumpkey](https://github.com/Ormicron/Sharp-dumpkey) | 1 | 基于C#实现的获取微信数据库密钥的小工具 |
| [Sunflower_get_Pas<br>sword](https://github.com/wafinfo/Sunflower_get_Password) |  | 一款针对向日葵的识别码和验证码提取工具 |
| [SharpWxDump](https://github.com/AdminTest0/SharpWxDump) |  | 微信客户端取证，可获取用户个人信息(昵称/账号/手机/邮箱/数据库<br>密钥(用来解密聊天记录))；支持获取多用户信息，不定期更新新版本偏<br>移，目前支持所有新版本、正式版本 |
| [GoWxDump](https://github.com/SpenserCai/GoWxDump) | v1.0.12 | SharpWxDump的Go语言版。微信客户端取证，获取信息(微信号、手机号<br>、昵称)，微信聊天记录分析(Top N聊天的人、统计聊天最频繁的好友排<br>行、关键词列表搜索等) |
| [qq_msg_decode](https://github.com/saucer-man/qq_msg_decode) |  | 解码qq聊天数据库 |
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
| [qsnctf-python](https://github.com/Moxin1044/qsnctf-python) | 0.0.8.1<br>0 | 青少年CTF的Python包，方便大家调用一些CTF常用功能。 |
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
### 防护
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [AoiAWD](https://github.com/DasSecurity-HatLab/AoiAWD) |  | AoiAWD-专为比赛设计，便携性好，低权限运行的EDR系统。 |
| [CTF-WAF](https://github.com/sharpleung/CTF-WAF) |  | 针对CTF线下赛的通用WAF，日志审计功能。 |
| [k4l0ng_WAF](https://github.com/dr0op/k4l0ng_WAF) |  | A broute detect WAF by PHP using to AWD |
# 应急响应
## Linux
### 自动化检查
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [GScan](https://github.com/grayddq/GScan) |  | 本程序旨在为安全应急响应人员对Linux主机排查时提供便利，实现主<br>机侧Checklist的自动全面化检测，根据检测结果自动数据聚合，进行黑<br>客攻击路径溯源。 |
| [LinuxCheck](https://github.com/al0ne/LinuxCheck) | V2.3 | Linux应急处置/信息搜集/漏洞检测工具，支持基础配置/网络流量/任<br>务计划/环境变量/用户信息/Services/bash/恶意文件/内核Rootkit/SSH/<br>Webshell/挖矿文件/挖矿进程/供应链/服务器风险等13类70+项检查 |
| [malwoverview](https://github.com/alexandreborges/malwoverview) | v5.4.1 | Malwoverview is a first response tool used for threat hunting <br>and offers intel information from Virus Total, Hybrid Analysis,<br> URLHaus, Polyswarm, Malshare, Alien Vault, Malpedia, Malware B<br>azaar, ThreatFox, Triage, InQuest and it is able to scan Androi<br>d devices against VT. |
| | | http://rkhunter.sourceforge.net/ |
| [RmTools](https://github.com/RoomaSec/RmTools) |  | 蓝队应急工具 |
### 进程分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [uroboros](https://github.com/evilsocket/uroboros) |  | A GNU/Linux monitoring and profiling tool focused on single pr<br>ocesses. |
| | | https://processhacker.sourceforge.io/ |
### 命令辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [whohk](https://github.com/heikanet/whohk) |  |  |
## Windows
### 进程分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [YDArk](https://github.com/ClownQq/YDArk) |  | X64内核小工具 |
| | | https://docs.microsoft.com/zh-cn/sysinternals/downloads/ |
### 日志分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| | | https://www.nirsoft.net/utils/full_event_log_view.html |
| | | https://www.microsoft.com/en-us/download/details.aspx?id=24659 |
| [windodws-logs-ana<br>lysis](https://github.com/dogadmin/windodws-logs-analysis) |  | windows日志一键分析小工具 |
| [APT-Hunter](https://github.com/ahmedkhlief/APT-Hunter) | V3.0 | APT-Hunter is Threat Hunting tool for windows event logs which<br> made by purple team mindset to provide detect APT movements hi<br>dden in the sea of windows event logs to decrease the time to u<br>ncover suspicious activity |
| [WELA](https://github.com/Yamato-Security/WELA) | v1.0.0 | WELA (Windows Event Log Analyzer): The Swiss Army knife for Wi<br>ndows Event Logs! ゑ羅（ウェラ） |
### 信息采集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [FireKylin](https://github.com/MountCloud/FireKylin) | v1.4.0 | 🔥火麒麟-网络安全应急响应工具(系统痕迹采集)Cybersecurity emerg<br>ency response tool.👍👍👍 |
## web日志分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [DecodeSomeJSPWebs<br>hell](https://github.com/minhangxiaohui/DecodeSomeJSPWebshell) | v1.2 | 冰蝎、哥斯拉 jsp webshell通信流量解密器 |
| [SerializationDump<br>er-Shiro](https://github.com/r00tuser111/SerializationDumper-Shiro) |  | 基于SerializationDumper的Shiro Cookie序列化数据解密小工具 |
## webshell查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| | | http://www.shelldetector.com/ |
| | | https://www.shellpub.com/ |
| [kunwu](https://github.com/kunwu2023/kunwu) | 0.1.0 | kunwu是新一代webshell检测引擎，使用了内置了模糊规则、污点分析<br>模拟执行、机器学习三种高效的检测策略 |
## 内存马查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shell-analyzer](https://github.com/4ra1n/shell-analyzer) | 0.1 | Java内存马查杀GUI工具，实时动态分析，支持本地和远程查杀 |
| [arthas](https://github.com/alibaba/arthas) | arthas-<br>all-3.7.<br>1 | Alibaba Java Diagnostic Tool Arthas/Alibaba Java诊断利器Arthas |
| [DuckMemoryScan](https://github.com/huoji120/DuckMemoryScan) |  | 检测绝大部分所谓的内存免杀马 |
| [java-memshell-sca<br>nner](https://github.com/c0ny1/java-memshell-scanner) |  | 通过jsp脚本扫描java web Filter/Servlet型内存马 |
| [copagent](https://github.com/LandGrey/copagent) |  | java memory web shell extracting tool |
| [aLIEz](https://github.com/r00t4dm/aLIEz) |  | 杀内存马的工具，欢迎code review，提出更好的意见 |
## 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Emergency-Respons<br>e-Notes](https://github.com/Bypass007/Emergency-Response-Notes) |  | 应急响应实战笔记，一个安全工程师的自我修养。 |
## 威胁情报收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [tig](https://github.com/wgpsec/tig) | v0.5.4 | Threat Intelligence Gathering 威胁情报收集，旨在提高蓝队拿到攻<br>击 IP 后对其进行威胁情报信息收集的效率。 |
| [ARTIF](https://github.com/CRED-CLUB/ARTIF) | 1.0 | An advanced real time threat intelligence framework to identif<br>y threats and malicious web traffic on the basis of IP reputati<br>on and historical data. |
## 勒索解密
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Decryption-Tools](https://github.com/jiansiting/Decryption-Tools) |  | Decryption-Tools |
# 安全产品
## 威胁检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmEye](https://github.com/RoomaSec/RmEye) | v0.0.4 | 戎码之眼是一个window上的基于att&ck模型的威胁监控工具.有效检测<br>常见的未知威胁与已知威胁.防守方的利剑 |
## 主机入侵检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Elkeid](https://github.com/bytedance/Elkeid) | rasp-v2<br>.2.0.9 | Elkeid is an open source solution that can meet the security r<br>equirements of various workloads such as hosts, containers and <br>K8s, and serverless. It is derived from ByteDance's internal be<br>st practices. |
| [Hades](https://github.com/theSecHunter/Hades) |  | Hades is an cross-platform HIDS with kernel-space data collect<br>ion. |
## Web应用防火墙
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [openstar](https://github.com/starjun/openstar) |  | lua waf,nginx+lua,openresty,luajit,waf+,cdn,nginx |
| [safeline](https://github.com/chaitin/safeline) | v3.3.0 | 一款足够简单、足够好用、足够强的免费 WAF。基于业界领先的语义引<br>擎检测技术，作为反向代理接入，保护你的网站不受黑客攻击。 |
## 欺骗防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [DecoyMini](https://github.com/decoymini/DecoyMini) | v2.0.66<br>91 | 🐝 A highly scalable, safe, free enterprise honeypots 一款高可<br>扩展、安全、免费的企业级蜜罐系统 |
| [Juggler](https://github.com/C4o/Juggler) |  | A system that may trick hackers.  针对黑客的拟态欺骗系统。 |
| [MySQL_Fake_Server](https://github.com/fnmsd/MySQL_Fake_Server) |  | MySQL Fake Server use to help MySQL Client File Reading and JD<br>BC Client Java Deserialize |
| [MysqlT](https://github.com/BeichenDream/MysqlT) | v1.0 | 伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击<br>攻击者 |
| [mysql-fake-server](https://github.com/4ra1n/mysql-fake-server) | 0.0.2 | MySQL Fake Server (纯Java实现，内置常见Java反序列化Payload，支<br>持GUI版和命令行版，提供Dockerfile) |
| [WhetherMysqlSham](https://github.com/BeichenDream/WhetherMysqlSham) | v1.0 | 检测目标Mysql数据库是不是蜜罐 |
| [Ehoney](https://github.com/seccome/Ehoney) | v3.0.0 | 安全、快捷、高交互、企业级的蜜罐管理系统，护网；支持多种协议蜜<br>罐、蜜签、诱饵等功能。A safe, fast, highly interactive and enter<br>prise level honeypot management system, supports multiple proto<br>col honeypots, honeytokens, baits and other functions. |
## 主机入侵防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [iDefender](https://github.com/wecooperate/iDefender) | 2.9.0 | iDefender（冰盾 - 终端主动防御系统） |
# 杂七杂八
## 远程软件
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [FreeRDP](https://github.com/FreeRDP/FreeRDP) | 2.11.1 | FreeRDP is a free remote desktop protocol library and clients |
| [Quasar](https://github.com/quasar/Quasar) | v1.4.1 | Remote Administration Tool for Windows |
| [rustdesk](https://github.com/rustdesk/rustdesk) | 1.2.2 | An open-source remote desktop, and alternative to TeamViewer. |
## 生成虚假数据
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [faker](https://github.com/joke2k/faker) | v19.6.0 | Faker is a Python package that generates fake data for you. |
## 短信转发器
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SmsForwarder](https://github.com/pppscn/SmsForwarder) | v3.2.0 | 短信转发器——监控Android手机短信、来电、APP通知，并根据指定规<br>则转发到其他手机：钉钉群自定义机器人、钉钉企业内机器人、企业微信<br>群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Tel<br>egram机器人、Server酱、PushPlus、手机短信等。包括主动控制服务端<br>与客户端，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。<br>（V3.0 新增）PS.这个APK主要是学习与自用，如有BUG请提ISSUE，同时<br>欢迎大家提PR指正 |
## 数据库管理软件
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dbeaver](https://github.com/dbeaver/dbeaver) | 23.2.0 | Free universal database tool and SQL client |
## MySQL实时监控工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [MySQLMonitor](https://github.com/TheKingOfDuck/MySQLMonitor) | 1.0 | MySQL实时监控工具(代码审计/黑盒/白盒审计辅助工具) |
## 恶意网络流量模拟
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [flightsim](https://github.com/alphasoc/flightsim) | v2.5.0 | A utility to safely generate malicious network traffic pattern<br>s and evaluate controls. |
## 克隆声音
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [MockingBird](https://github.com/babysor/MockingBird) | v0.0.1 | 🚀AI拟声: 5秒内克隆您的声音并生成任意语音内容 Clone a voice in<br> 5 seconds to generate arbitrary speech in real-time |
## 渗透测试报告辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [APTRS](https://github.com/Anof-cyber/APTRS) |  | Automated Penetration Testing Reporting System |
| [BugRepoter_0x727](https://github.com/0x727/BugRepoter_0x727) |  | BugRepoter_0x727(自动化编写报告平台)根据安全团队定制化协同管理<br>项目安全，可快速查找历史漏洞，批量导出报告。 |
| [Savior](https://github.com/Mustard404/Savior) | new | 渗透测试报告自动生成工具！ |
| [SAReport](https://github.com/1u0Hun/SAReport) |  | 渗透测试自动化报告平台 |
| [pentest_report](https://github.com/dbgee/pentest_report) | v1.0.0 | A pentest reporter generator |
| [WaterExp](https://github.com/linshaoSec/WaterExp) |  | WaterExp:面向安服仔的 水报告模板和工具 |
| [report](https://github.com/CTF-MissFeng/report) | v1.0.1 | 乙方渗透测试漏洞报告管理系统 |
## 动态口令
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [rotp](https://github.com/mdp/rotp) | v6.3.0 | Ruby One Time Password library |
## 科学上网
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [v2rayA](https://github.com/v2rayA/v2rayA) | v2.2.4 | A web GUI client of Project V which supports VMess, VLESS, SS,<br> SSR, Trojan, Tuic and Juicity protocols. 🚀 |
| [free](https://github.com/freefq/free) |  | 翻墙、免费翻墙、免费科学上网、免费节点、免费梯子、免费ss/v2ray<br>/trojan节点、蓝灯、谷歌商店、翻墙梯子 |
| [v2rayfree](https://github.com/aiboboxx/v2rayfree) |  | v2ray节点、免费节点、免费v2ray节点、最新公益免费v2ray节点订阅<br>地址、免费v2ray节点每日更新、免费ss/v2ray/trojan节点、freefq  |
## python笔记
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) |  | Python - 100天从新手到大师 |
## 报告模板
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
| [ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut) |  | 🚀💪Maximize your efficiency and productivity, support for Eng<br>lish,中文,Español,العربية. 让生产力加倍的ChatGPT快捷指令，无需<br>熟悉提示词，就能轻松搜索、优化和管理Prompts，适应多语言及各种生<br>产效率场景。 |
## APP合规
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [camille](https://github.com/zhengjim/camille) |  | 基于Frida的Android App隐私合规检测辅助工具 |
## 区块链
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [all-in-one-v2](https://github.com/zaivanza/all-in-one-v2) |  |  |
| [zksync](https://github.com/nftscripts/zksync) |  |  |
| [zksync-auto](https://github.com/bxdoan/zksync-auto) |  | some help for zksync incentive |
| [zksync2-python](https://github.com/zksync-sdk/zksync2-python) | v0.6.0 |  |
## 网站压测工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WebBench](https://github.com/EZLippi/WebBench) |  | Webbench是Radim Kolar在1997年写的一个在linux下使用的非常简单的<br>网站压测工具。它使用fork()模拟多个客户端同时访问我们设定的URL，<br>测试网站在压力下工作的性能，最多可以模拟3万个并发连接去测试网站<br>的负载能力。官网地址:http://home.tiscali.cz/~cz210552/webbench.h<br>tml |
| [dperf](https://github.com/baidu/dperf) | v1.5.0 | dperf is a DPDK based 100Gbps network performance and load tes<br>ting software. |
## web靶场
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ElectricRat](https://github.com/linjiananallnt/ElectricRat) | v1.3.0 | 电气鼠靶场系统是一种带有漏洞的Web应用程序，旨在为Web安全渗透测<br>试学习者提供学习和实践的机会。The Electrical Mouse Target Range <br>System is a web application with vulnerabilities designed to pr<br>ovide learning and practice opportunities for web security pene<br>tration testing learners. |
| [vulstudy](https://github.com/c0ny1/vulstudy) |  | 使用docker快速搭建各大漏洞靶场，目前可以一键搭建17个靶场。 |
| [sqli-labs](https://github.com/Audi-1/sqli-labs) |  | SQLI labs to test error based, Blind boolean based, Time based<br>. |
| [upload-labs](https://github.com/c0ny1/upload-labs) | 0.1 | 一个想帮你总结所有类型的上传漏洞的靶场 |
| [SecExample](https://github.com/tangxiaofeng7/SecExample) |  | JAVA 漏洞靶场 (Vulnerability Environment For Java) |
| [Hello-Java-Sec](https://github.com/j3ers3/Hello-Java-Sec) | 1.10 | ☕️ Java Security，安全编码和代码审计 |
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
| [xxe-lab](https://github.com/c0ny1/xxe-lab) |  | 一个包含php,java,python,C#等各种语言版本的XXE漏洞Demo |
| | | https://dvwa.co.uk/ |
| | | https://www.pentesterlab.com/exercises/web_for_pentester/course |
| [SpringBootVulExpl<br>oit](https://github.com/LandGrey/SpringBootVulExploit) |  | SpringBoot 相关漏洞学习资料，利用方法和技巧合集，黑盒安全评估 <br>check list |
| [vulhub](https://github.com/vulhub/vulhub) |  | Pre-Built Vulnerable Environments Based on Docker-Compose |
| [vulfocus](https://github.com/fofapro/vulfocus) | v0.3.2.<br>11 | 🚀Vulfocus 是一个漏洞集成平台，将漏洞环境 docker 镜像，放入即<br>可使用，开箱即用。 |
| | | https://hackmyvm.eu/anon/ |
## 短信轰炸
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SMSBoom](https://github.com/OpenEthan/SMSBoom) | main | 短信轰炸/短信测压/ | 一个健壮免费的python短信轰炸程序，专门炸<br>坏蛋蛋，百万接口，多线程全自动添加有效接口，支持异步协程百万并发<br>，全免费的短信轰炸工具！！hongkonger开发全网首发！！ |
## 验证码生成
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Calculate_Captcha](https://github.com/fupinglee/Calculate_Captcha) | v1.1 | 计算验证码生成器，用于训练使用 |
## 机器学习
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dddd_trainer](https://github.com/sml2h3/dddd_trainer) |  | ddddocr训练工具 |
| [Augmentor](https://github.com/mdbloice/Augmentor) |  | Image augmentation library in Python for machine learning. |
## 安全思维脑图
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [HackerMind](https://github.com/Ascotbe/HackerMind) |  | 渗透步骤，web安全，CTF，业务安全，人工智能，区块链安全，数据安<br>全，安全开发，无线安全，社会工程学，二进制安全，移动安全，红蓝对<br>抗，运维安全，风控安全，linux安全 |