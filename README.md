# 更新于 2023-03-18 09:05:51

## 近30天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
|2023-03-17 18:40:26|[naabu](https://github.com/projectdiscovery/naabu)|v2.1.3|## What's Changed * Fixed a issue to sk<br>ip host discovery in passive mode by @Mz<br>ack9999 in https://github.com/projectdis<br>covery/naabu/pull/583 * Fixed osutil + i<br>mproving error message with -sn on windo<br>ws by @Mzack9999 in https://github.com/p<br>rojectdiscovery/naabu/pull/588 * Added s<br>elf update option + version check by @Ra<br>manaReddy0M in https://github.com/projec<br>tdiscovery/naabu/pull/600 * Updated rele<br>ase workflow to include binary for mac/w<br>indows arch by @ehsandeep in https://git<br>hub.com/projectdiscovery/naabu/pull/598#<br># New Contributors * @RamanaReddy0M made<br> their first contribution in https://git<br>hub.com/projectdiscovery/naabu/pull/600*<br>*Full Changelog**: https://github.com/pr<br>ojectdiscovery/naabu/compare/v2.1.2...v2<br>.1.3|
|2023-03-17 16:15:20|[subfinder](https://github.com/projectdiscovery/subfinder)|v2.5.7|## What's Changed * Fixed Docker file t<br>o avoid version mismatch by @olearycrew <br>in https://github.com/projectdiscovery/s<br>ubfinder/pull/771 * Added self update op<br>tion (-update) + version checkby @Ramana<br>Reddy0M in https://github.com/projectdis<br>covery/subfinder/pull/780## New Contribu<br>tors * @olearycrew made their first cont<br>ribution in https://github.com/projectdi<br>scovery/subfinder/pull/771**Full Changel<br>og**: https://github.com/projectdiscover<br>y/subfinder/compare/v2.5.6...v2.5.7|
|2023-03-17 08:52:34|[HackTools](https://github.com/Vicl1fe/HackTools)|1.4|新增FindReport、jasypt解密功能|
|2023-03-17 08:22:08|[ARL](https://github.com/TophantTechnology/ARL)|v2.5.4|## 更新和优化 1. 优化泛解析域名爆破流程<br> 2. 修复nuclei 在执行时可能出现一个错误 <br>#481 3. nuclei版本更新 4. 截图生成文件名<br>正则优化 #498 5. 域名插件crt.sh，hunter_q<br>ax等优化 6. 修复302 URL过长导致入库失败<br>问题 @原来是老王 @ki9mu## 更新方法：docke<br>r-compose pull docker-dompose down docke<br>r-dompose up -d## 重装参考： [卸载并重装<br>](https://tophanttechnology.github.io/AR<br>L-doc/faq/#12-docker) |
|2023-03-16 18:36:03|[nuclei](https://github.com/projectdiscovery/nuclei)|v2.9.0|## What's Changed* Added support for te<br>mplates in JSON format by @CodFrm in htt<br>ps://github.com/projectdiscovery/nuclei/<br>pull/3333 * Added template sign/verify f<br>unctionality by @Mzack9999 in https://gi<br>thub.com/projectdiscovery/nuclei/pull/30<br>29 * Added -track-error option to add cu<br>stom errors to max-host-error watch list<br> by @austintraver in https://github.com/<br>projectdiscovery/nuclei/pull/3399 * Adde<br>d data race panic check in integration_t<br>ests by @tarunKoyalwar in https://github<br>.com/projectdiscovery/nuclei/pull/3303 *<br> Added CLI option to override fuzzing te<br>mplate options by @ShubhamRasal in https<br>://github.com/projectdiscovery/nuclei/pu<br>ll/3355 * Added ip_formats() helper func<br>tion by @xm1k3 in https://github.com/pro<br>jectdiscovery/nuclei/pull/3286 * Added r<br>esolve() helper function by @xm1k3 in ht<br>tps://github.com/projectdiscovery/nuclei<br>/pull/3321 * Added rawstringslice to mak<br>e reference url case insensitive by @Bis<br>stocuz in https://github.com/projectdisc<br>overy/nuclei/pull/3346 * Fixed a bug wit<br>h OR matcher condition with interactsh b<br>y @RamanaReddy0M in https://github.com/p<br>rojectdiscovery/nuclei/pull/3397 * Fixed<br> set-method option in headless template <br>by @Mzack9999 in https://github.com/proj<br>ectdiscovery/nuclei/pull/3373 * Fixed at<br>omic bool check by @Mzack9999 in https:/<br>/github.com/projectdiscovery/nuclei/pull<br>/3376 * Fixed bug in URL path and adds i<br>ntegration tests by @tarunKoyalwar in ht<br>tps://github.com/projectdiscovery/nuclei<br>/pull/3331 * Fixed crash with interactsh<br> integration by @Mzack9999 in https://gi<br>thub.com/projectdiscovery/nuclei/pull/33<br>12 * Fixed data race when using interact<br>sh_matchers by @tarunKoyalwar in https:/<br>/github.com/projectdiscovery/nuclei/pull<br>/3432 * Fixed file input in custom vars <br>with self-contained http template by @ta<br>runKoyalwar in https://github.com/projec<br>tdiscovery/nuclei/pull/3385 * Fixed miss<br>ing port in matched ssl templates by @ta<br>runKoyalwar in https://github.com/projec<br>tdiscovery/nuclei/pull/3380 * Fixed nil <br>pointer reference + use map helper by @M<br>zack9999 in https://github.com/projectdi<br>scovery/nuclei/pull/3421 * Fixed parseUr<br>l test by @ShubhamRasal in https://githu<br>b.com/projectdiscovery/nuclei/pull/3426 <br>* Fixed typo in -hc option by @sullo in <br>https://github.com/projectdiscovery/nucl<br>ei/pull/3400Issues closed in release - h<br>ttps://github.com/projectdiscovery/nucle<br>i/milestone/27## New Contributors * @nor<br>aj made their first contribution in http<br>s://github.com/projectdiscovery/nuclei/p<br>ull/3162 * @Bisstocuz made their first c<br>ontribution in https://github.com/projec<br>tdiscovery/nuclei/pull/3346 * @CodFrm ma<br>de their first contribution in https://g<br>ithub.com/projectdiscovery/nuclei/pull/3<br>333 * @austintraver made their first con<br>tribution in https://github.com/projectd<br>iscovery/nuclei/pull/3399 * @RamanaReddy<br>0M made their first contribution in http<br>s://github.com/projectdiscovery/nuclei/p<br>ull/3397**Full Changelog**: https://gith<br>ub.com/projectdiscovery/nuclei/compare/v<br>2.8.9...v2.9.0|
|2023-03-15 08:50:17|[Elkeid](https://github.com/bytedance/Elkeid)|scanner-v<br>2.2.0.1_20<br>230315||
|2023-03-14 14:33:27|[RequestTemplate](https://github.com/1n7erface/RequestTemplate)|v1.1.3|2023.3.14 22:30 1.解决了一个POC在运行过<br>程中线程提前中断的bug|
|2023-03-14 06:26:44|[captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified)|0.22|【2023-3-14】 0.22 重要问题修复 - 修复<br>了装载插件会影响proxy选项卡的问题|
|2023-03-13 18:58:37|[super-xray](https://github.com/4ra1n/super-xray)|1.6|## 1.6失眠，简单更新下更新内容： - [imp<br>ortant] 给RAD联动提供一种批量执行的办法 <br>#155 - [important] RAD联动支持Cookie配置<br> #153 - [feat] 第一次加载RAD后支持保存路<br>径下次直接加载 #156 - [feat] RAD联动支持<br>一键复制RAD命令 #154 - [bug] 备份xray目录<br>原来的config.yaml文件 #152 - [feat] RAD <br>联动支持拖拽功能 #151 - [feat] request 支<br>持自定义 user-agent #149 - [feat] 允许设<br>置请求Cookie内容 #150 - [feat] radium sup<br>port file input #148 (同#155)下载： - su<br>per-xray-1.6.jar 版本通过java -jar super<br>-xray-1.6.jar启动 - super-xray-1.6-jre-e<br>xe.zip 是内置了JRE的exe版本 - super-xray<br>-1.6-system-jre.exe 是使用系统JRE的exe版<br>本|
|2023-03-13 15:04:36|[koko-moni](https://github.com/burpheart/koko-moni)|v0.0.1|v0.0.1|
|2023-03-13 07:24:56|[log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner)|0.23.0-be<br>ta2|# 0.23.0-beta2 update ## 2023-3-13 1. f<br>ix problem _____________________________<br>________________________________ 1. 优化<br>选中内网ip时只发请求头含有%24payload的问<br>题，增至和普通被动扫描一样多的请求|
|2023-03-13 05:57:36|[Tomcat_PUT_GUI_EXP](https://github.com/xiaokp7/Tomcat_PUT_GUI_EXP)|1.4|修复命令执行回显中文乱码|
|2023-03-12 16:51:05|[Apt_t00ls](https://github.com/White-hua/Apt_t00ls)|v0.6|H3C 任意文件上传 致远帆软组件任意文件上<br>传 nacos任意用户添加 帆软任意文件上传 用<br>友GRP_U8任意文件上传 用友KSOA任意文件上传<br>rce -- 0day漏洞作者 https://github.com/c<br>dxiaodong|
|2023-03-12 16:46:59|[CDK](https://github.com/cdk-team/CDK)|v1.5.2|Release Date: 2023-03-12## What's Chang<br>ed * V1.5.2 alpha by @neargle in https:/<br>/github.com/cdk-team/CDK/pull/80## :scro<br>ll: Changelog### :bomb: Exploits* Fix 78<br>(exp): support containerd and other linu<br>x path### :toolbox: Tools* Fix #77(exp s<br>hadow-apiserver): anonymous-auth is not <br>valid, support v1.23.1### :sparkles: Oth<br>ers* Fix 78(exp): support containerd and<br> other linux path * Chore(exp): add aler<br>t message about flag auto-escape is depr<br>ecated## :sparkles: In Chinese* 支持 lin<br>ux 环境下的不同容器运行时，如 containerd<br>、runc、docker； * 修复shadow-apiserver匿<br>名访问无效的issue，支持新版本的k8s，如 v1<br>.23.1； * 添加迭代部分功能的消息提醒## :<br>key: Hash Table|SHA256|EXECTUE FILE| |--<br>-|---| |9f63e35d7b9d0814ad9f0ef23b89deb4<br>f823d3b07bcd33df9abc5b957bb8be0f|cdk_dar<br>win_amd64 d5c8e759b790c6ffb3134c8f0aae58<br>65e2ae4c672dc09eaa312bc928fd0d78bd|cdk_l<br>inux_386 64c86a12800b8d5064e7313a43eb6f5<br>504a7043ab15c227cecfddaf84cc74ced|cdk_li<br>nux_386_thin 364fcacd8b55d7d54162849b620<br>cd83e9f50ddb3c7c08478f391cce09449b452|cd<br>k_linux_386_thin_upx 242a11999f0c5b77640<br>0f2462854ef1d07101bd1085e3b29c9b7ba825c9<br>3a3fb|cdk_linux_386_upx af751c690671ffc0<br>da6380ef94a25df3dfc5911c448319f7f6b90df5<br>5cca7b7d|cdk_linux_amd64 f118a70fa7b02b8<br>58bb4fffb96d9a861e4b02f62df054a0d6985444<br>9682c8f85|cdk_linux_amd64_thin 3dc271adc<br>2565c38eda5fdaee3070bda8962159d17ba62546<br>7a0f3a6e5e440d0|cdk_linux_amd64_thin_upx<br> 924fb2bd1fe001f9eb62509a05546d1aaf97ebb<br>fca73c75eb665a38b34559c4e|cdk_linux_amd6<br>4_upx 594811dafdfb9f5cc56b604d8fe97777c2<br>3057e37803ec34afdf5680bf9276ea|cdk_linux<br>_arm 828aede9a7bc193899b66e8c10ac10d2439<br>8cf79575e771d9a970d3f9a4cdd92|cdk_linux_<br>arm64 2eb30e2abc71fadaee5980bd89a8e4a2c9<br>5bcc5d60857a3c13b006c186307e8e|cdk_linux<br>_arm64_thin|**Full Changelog**: https://<br>github.com/cdk-team/CDK/compare/v1.5.1..<br>.v1.5.2|
|2023-03-12 12:32:10|[feroxbuster](https://github.com/epi052/feroxbuster)|v2.9.1|## What's Changed * Implement auto upda<br>te feature by @aancw in https://github.c<br>om/epi052/feroxbuster/pull/813 * scan ma<br>nagement can now canx scans started with<br> -u | --stdin | the menu itself by @epi0<br>52 in https://github.com/epi052/feroxbus<br>ter/pull/821 * feroxbuster can be instal<br>led via chocolatey by @aancw in https://<br>github.com/epi052/feroxbuster/pull/807 *<br> fix resume with offset when --methods |<br> --extensions are used by @epi052 in htt<br>ps://github.com/epi052/feroxbuster/pull/<br>823**Full Changelog**: https://github.co<br>m/epi052/feroxbuster/compare/v2.9.0...v2<br>.9.1|
|2023-03-11 15:07:46|[Hack-Tools](https://github.com/LasCC/Hack-Tools)|0.5.0|# Version 0.5.0The new update is out! <br>🤩- Completely redesign the revershell co<br>mponent - New transfert methods componen<br>t - Fix the MSF Builder component## Inst<br>allation Steps :### Chrome - Extract **d<br>ist.zip** (you will obtain a folder name<br>d **dist**) - In your chromium based web<br>-browser upload the folder as an unpacke<br>d Extension ***check the repo readme.md*<br>****NEW** Link to the Chrome extension :<br> https://chrome.google.com/webstore/deta<br>il/hack-tools/cmbndhnoonmghfofefkcccljbk<br>dpamhi---### Firefoxhttps://addons.mozil<br>la.org/fr/firefox/addon/hacktools/Or ins<br>tall it as a temporary plugin in Firefox<br> in the page about:debugging#/runtime/th<br>is-firefox by selecting the manifest ins<br>ide **dist**---### Instructions to build<br> for SafariCreate a safari web extension<br> project using the command below. This i<br>s to be run once.bash xcrun safari-web-e<br>xtension-coverter [path_to_dist_folder]F<br>ollow the instructions to create the pro<br>ject the default language should be Swif<br>t.- Build project. - Open Safari and ena<br>ble unsigned extensions; Develop → Allo<br>w Unsigned Extensions. - Open Safari → <br>Preferences → Extensions and enable Hac<br>k-Tools - Click on the extension icon an<br>d switch to full screen mode.**Full Chan<br>gelog**: https://github.com/LasCC/Hack-T<br>ools/pull/133 |
|2023-03-11 02:07:48|[nemo_go](https://github.com/hanc00l/nemo_go)|v2.9.1|Update： 1、在任务中获取http指纹时，将H<br>TTP响应的Header与Body保存并进行查询。注<br>意： **由于新增加了两个数据库表，因此从v2<br>.9.0升级请导入http.sql。**|
|2023-03-10 07:42:24|[iDefender](https://github.com/wecooperate/iDefender)|2.5.0|**重大版本，建议更新**- 添加基础防护能<br>力- **智能防护：** 利用智能分析和识别恶意<br>软件行为，提供实时防护机制，确保系统免受<br>恶意软件侵害- **系统优化：** 拦截非必要的<br>软件和联网行为，提高系统运行速度和稳定性<br>，提供更优秀的用户体验- **安全加固：** 拦<br>截系统存在漏洞的组件和常见入侵途径，增强<br>系统安全性，避免遭受恶意软件攻击- **漏洞<br>防御：** 根据已知漏洞入侵方式开发专门的防<br>御规则，保障系统不受黑客攻击和恶意软件入<br>侵- **模板支持自动在线更新**- 规则记录添<br>加右键菜单 - 路径参数添加粘贴支持（方便快<br>速录入多条数据） - 路径参数添加多选删除 -<br> 弹框添加进程命令行信息（方便查看脚本进<br>程对应的脚本文件） - 添加规则过滤 - 优化<br>一些界面使用体验 - 修复一些问题软件下载|
|2023-03-10 03:32:44|[code6](https://github.com/4x99/code6)|1.6.4|### 更新日志 - 特性：[ 扫描结果 ] 支持<br>导出单页 CSV 数据（#245） - 优化：[ 扫描<br>结果 ] 新增支持 “处理人”、“说明” 字段<br>搜索（#247） - 修复：[ Docker 部署 ] 修复<br>重启可能导致配置项异常问题（#248） - 修复<br>：[ 扫描任务 ] 待执行任务配置被删导致扫描<br>队列阻塞问题（#252） - 修复：[ 通知配置 ]<br> 更新企业群消息机器人文档地址 - 特性：[ <br>通知配置 ] 邮件通知支持 SSL/TLS 加密（#24<br>7）### 升级指南 #### 源码安装 直接拉取最<br>新代码#### Docker 安装 拉取最新代码、创建<br>镜像并启动容器即可#### Docker-Compose 安<br>装 拉取最新代码启动容器即可 |
|2023-03-09 12:55:14|[TsojanScan](https://github.com/Tsojan/TsojanScan)|v1.4.4|## 更新说明 - v1.4.4 1. 优化代码结构； <br>2. 修复weblogic弱口令误报bug； 3. 增加ot<br>f后缀不扫描规则； 4. 删除asix/happaxis.j<br>sp扫描规则； 5. 增加sql语法错误的页面回<br>显扫描模块，只显示sql错误显示（参数后面增<br>加单引号、双引号、反斜线，去查看有没有SQL<br>错误语句）。 |
|2023-03-09 12:20:40|[ysoserial](https://github.com/su18/ysoserial)|v1.4|1. Transformer[] / BeanShell / C3P02 利<br>用链支持 LF 加载本地 class 文件功能； 2. <br>更新 JbossEcho 支持 JBoss-4.2.3.GA； 3. <br>更新 Struts2 回显及 Action 内存马； 4. 移<br>除 Tomcat Listener NeoReg 流量隧道、移除 <br>EncryptedTranscoder 及依赖； 5. 支持 suo<br>5 利用方式； 6. 更新命令执行混淆支持 win<br>dows/linux/unix jdk 1.6； 7. 修改打包 de<br>bug 信息为 false； 8. 更新 javassist 版<br>本，进行一些降低 payload 的尝试； 9. 更新<br> HelpFormatter 以执行终端大小动态调整，<br>最大宽度 200； 10. 打通 BCEL 类加载利用链<br>（详见代码）； 11. 使用 ScriptEngineManag<br>er 区分 Nashorn/Rhino 引擎，Rhino 使用 B<br>CEL 曲线救国类加载； 12. 增加 CC12 用 De<br>faultedMap 替换 LazyMap。|
|2023-03-09 08:37:22|[GoWxDump](https://github.com/SpenserCai/GoWxDump)|v1.0.9|通过注册表自从查找微信数据目录|
|2023-03-09 04:49:16|[JDumpSpider](https://github.com/whwlsfb/JDumpSpider)|V1.1|- 项目重构，增强不同环境下的兼容性。 - <br>增加类字段的用户信息模糊搜索功能。|
|2023-03-08 06:18:49|[pentest_report](https://github.com/dbgee/pentest_report)|v1.0.0|First orricial release |
|2023-03-06 08:49:57|[veinmind-tools](https://github.com/chaitin/veinmind-tools)|v2.0.6|## Feature - 降低镜像大小 @286515491## <br>Fix - 敏感信息检测增加文件限制 @testwill<br>- 优化容器逃逸权限检测逻辑 @286515491- <br>修复敏感信息路径扫描 @286515491 |
|2023-03-06 08:47:39|[ElectricRat](https://github.com/linjiananallnt/ElectricRat)|v1.3.0|# 更新说明 1. 新增越权漏洞案例，包含水<br>平、垂直越权。 2. 增加XSS过滤难度 3. 增加<br>SPEL和SSTI结果输出 4. 新增压缩文件自解压<br>案例# TODO - [x] 越权漏洞# 如何更新 1. 将<br> ElectricRat-docker.zip 中的 ElectricRat<br>.war 覆盖之前的 war 包。 2. 重启 docker<br>。sudo docker restart electricrat-web 3. <br>稍等片刻后，访问 http://127.0.0.1:12666/E<br>lectricRat/ |
|2023-03-05 17:56:39|[dbeaver](https://github.com/dbeaver/dbeaver)|23.0.0|Changes since 22.3.5: - SQL editor:- Co<br>lumn metadata resolution was fixed for q<br>uoted column names- SQL console now resp<br>ects "open separate connection" option- <br>Variables resolve in set and other comma<br>nds was fixed- Copy/paste command was fi<br>xed for editors without associated conne<br>ction - Data editor:- Spatial viewer: la<br>sso tool was fixed for Safari browser- S<br>upport of WKT format stored in BLOB colu<br>mns was added- Issues with image viewer <br>and BLOB columns was fixed (NullPointer <br>error))- Selected columns/rows data expo<br>rt was fixed (issue with BLOB value turn<br>ing into NULL in UI) - Accessibility:- F<br>ont settings are now respected in all ed<br>itors/popups- New keyboard shortcuts sch<br>ema was added "DBeaver Keyboard Only"- M<br>any new keyboard shortcuts were added- C<br>atalog/schema selector now supports keyb<br>oard only mode- Results tab pin/unpin co<br>mmand is now accessible from keyboard (t<br>hanks to hawthorne3341)- Reader texts we<br>re localized - Database dashboard create<br> wizard UI was fixed - Generate SQL dial<br>og now supports connection invalidation <br>- Clickhouse: driver version was updated<br> to 0.4.1 - Dremio: driver version was u<br>pdated to 24.0 - Firebird: table colum c<br>omments support was added - PostgreSQL:-<br> Issue with URL-based connections was re<br>solved (invalid host name)- Execution pl<br>an parameters are now saved - Redshift: <br>varbyte datatype suport was fixed - SQL <br>Server:- UI for Kerberos authentication <br>configuration was fixed- Table colum com<br>ments support was added - French localiz<br>ation was fixed (thanks to alexgille) - <br>Problems with Kerberos were resolved (we<br> have reverted to Java 11)|
|2023-03-03 16:59:23|[faker](https://github.com/joke2k/faker)|v17.6.0|See [CHANGELOG.md](https://github.com/j<br>oke2k/faker/blob/refs/tags/v17.6.0/CHANG<br>ELOG.md).|
|2023-03-03 01:00:04|[AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool)|20230303|1. 效果优化|
|2023-03-01 06:20:26|[Antenna](https://github.com/wuba/Antenna)|v1.3.2|1、优化了任务模块功能逻辑 2、修复python<br>3.6版本不支持socket解析ip的bug|
|2023-02-28 04:13:35|[OneScan](https://github.com/vaycore/OneScan)|v0.5.2|0.5.2 版本发布，版本更新内容如下：### <br>新增- 主面板新增 Filter 按钮，支持单列、<br>多列过滤规则配置 |
|2023-02-26 13:06:58|[go_proxy_pool](https://github.com/pingc0y/go_proxy_pool)|2022.11.2<br>2|2022.11.22|
|2023-02-26 07:27:26|[mitaka](https://github.com/ninoseki/mitaka)|v1.0.0|- Migrate to the Manifest V3 (#703) - R<br>eplace Mocha, Chai and Sinon with Jest (<br>#703) |
|2023-02-26 00:35:49|[qsnctf-python](https://github.com/Moxin1044/qsnctf-python)|0.0.8.9|更新了之前版本不存在的Web请求timeout导<br>致扫描时间过长，在0.0.8.9版本已修复此问题<br>。 您甚至可以指定timeout，感谢问题反馈！|
|2023-02-23 07:56:42|[nuclei-plus](https://github.com/Yong-An-Dang/nuclei-plus)|v7.0.0|> 第一个发布版本，也是第七个大版本，就<br>是这么奇怪:grin: #### :pushpin: Support- <br>[x] Support system tray - [x] Support pr<br>oject management - [x] Support configura<br>tion management - [x] Support template m<br>anagement - [x] Support template editing<br> - [x] Support internationalization, def<br>ault zh - [x] Support multiple network s<br>pace engine interface search**Full Chang<br>elog**: https://github.com/Yong-An-Dang/<br>nuclei-plus/commits/v7.0.0|
|2023-02-22 13:35:31|[autoDecoder](https://github.com/f0ng/autoDecoder)|0.23|## 2023.2.22 更新0.23 1. 优化了插件的一<br>些问题 2. 案例移步[autoDecoder-usages](ht<br>tps://github.com/f0ng/autoDecoder-usages<br>)|
|2023-02-22 09:37:42|[HaE](https://github.com/gh0stkey/HaE)|2.4.6|HaE 2.4.6 更新内容： 1. 加入多线程对数<br>据进行匹配和提取，减少卡顿现象； 2. 变更<br>配置文件更新地址为jsdelivr的CDN节点地址，<br>优化国内用户体验。|
|2023-02-21 03:59:42|[URLFinder](https://github.com/pingc0y/URLFinder)|2023.2.21|2023/2/21 修复 已知bug|
|2023-02-19 17:36:35|[wxapkgUnpack](https://github.com/jdr2021/wxapkgUnpack)|1.0||
|2023-02-17 13:57:27|[Search_Viewer](https://github.com/G3et/Search_Viewer)|v2.0|版本：v2.0 2023/02/17·修复导出时间戳·修<br>复Hunter情况恢复页码·界面稍微调整·新增360<br> Quake·新增Zoomeye 钟馗之眼|
|2023-02-17 03:46:29|[OutLook](https://github.com/KrystianLi/OutLook)|v1.2.0|1、优化代码和操作界面 2、新增数据保存功<br>能，导出格式为xls|
|2023-02-16 15:01:33|[npscrack](https://github.com/weishen250/npscrack)|npscrack-<br>1.0||
## 近30天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
|2023-03-18 01:00:16|[NucleiTP](https://github.com/ExpLangcn/NucleiTP)|更新啦❤️|
|2023-03-17 21:53:36|[PocOrExp_in_Github](https://github.com/ycdxsb/PocOrExp_in_Github)|update 2023-03-18 05:53:36|
|2023-03-17 18:05:43|[naabu](https://github.com/projectdiscovery/naabu)|Merge pull request #608 from projectdiscovery/devnaabu<br> v2.1.3|
|2023-03-17 16:51:30|[nuclei](https://github.com/projectdiscovery/nuclei)|Merge pull request #3433 from projectdiscovery/dependa<br>bot/go_modules/v2/google.golang.org/protobuf-1.29.1chor<br>e(deps): bump google.golang.org/protobuf from 1.29.0 to<br> 1.29.1 in /v2|
|2023-03-17 16:12:07|[subfinder](https://github.com/projectdiscovery/subfinder)|Merge pull request #791 from projectdiscovery/devsubfi<br>nder - v2.5.7|
|2023-03-17 15:42:26|[ysoserial](https://github.com/su18/ysoserial)|1、全面支持 AgentNoFile 内存马，目前支持 bx 的 Servlet<br>/TomcatFilter，使用方式 EX-Agent-Lin/Win-Servlet/Filter<br>-bx，例如 EX-Agent-Lin-Filter-bx，参数与原项目保持一致<br>，后续将逐步更新更多功能
2、修复 Base64 Util 类的反射调<br>用 BUG|
|2023-03-17 13:58:38|[dbeaver](https://github.com/dbeaver/dbeaver)|Merge remote-tracking branch 'origin/devel' into devel|
|2023-03-17 11:47:19|[feroxbuster](https://github.com/epi052/feroxbuster)|Merge branch 'main' of github.com:epi052/feroxbuster|
|2023-03-17 11:35:53|[Goby](https://github.com/gobysec/Goby)|Update README.md|
|2023-03-17 09:37:29|[HackTools](https://github.com/Vicl1fe/HackTools)|更新|
|2023-03-17 08:24:41|[ARL](https://github.com/TophantTechnology/ARL)|Merge pull request #505 from TophantTechnology/update/<br>docUpdate Readme.md|
|2023-03-17 06:17:13|[murphysec](https://github.com/murphysecurity/murphysec)|Merge pull request #148 from murphysecurity/dependabot<br>/go_modules/github.com/go-git/go-git/v5-5.6.1|
|2023-03-17 04:34:11|[BurpCrypto](https://github.com/whwlsfb/BurpCrypto)|enhance rsa exponent logic.|
|2023-03-17 01:54:20|[JDumpSpider](https://github.com/whwlsfb/JDumpSpider)|enhance heapfile version match logic.|
|2023-03-17 00:49:24|[RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)|Update williams_pp1.py|
|2023-03-16 10:46:49|[v2rayA](https://github.com/v2rayA/v2rayA)|fix: omit emty sni when sharing|
|2023-03-16 01:29:06|[SmsForwarder](https://github.com/pppscn/SmsForwarder)|整理：README|
|2023-03-15 22:00:16|[sqlmap](https://github.com/sqlmapproject/sqlmap)|Fixes #5364|
|2023-03-15 11:05:29|[iDefender](https://github.com/wecooperate/iDefender)|update|
|2023-03-15 09:09:00|[CodeQLpy](https://github.com/webraybtl/CodeQLpy)|优化因为重复import相同类名导致的bug|
|2023-03-15 07:02:43|[vulnerability](https://github.com/lal0ne/vulnerability)|CVE-2021-29441|
|2023-03-15 05:12:18|[0day](https://github.com/helloexp/0day)|Merge branch 'master' of https://github.com/helloexp/0<br>day|
|2023-03-15 03:38:02|[Apt_t00ls](https://github.com/White-hua/Apt_t00ls)|Update README.md|
|2023-03-15 02:33:56|[nemo_go](https://github.com/hanc00l/nemo_go)|Fix: ip_http and domain_http SaveOrUpdate function|
|2023-03-14 23:44:28|[gshark](https://github.com/madneal/gshark)|Merge pull request #149 from madneal/dependabot/npm_an<br>d_yarn/web/webpack-5.76.0Bump webpack from 5.69.1 to 5.<br>76.0 in /web|
|2023-03-14 21:39:08|[Hack-Tools](https://github.com/LasCC/Hack-Tools)|splitting webpack chunks + fixing zipping for firefox|
|2023-03-14 16:12:08|[faker](https://github.com/joke2k/faker)|Add territory zip codes for en_US (#1821)Close #1812|
|2023-03-14 09:43:45|[npscrack](https://github.com/weishen250/npscrack)|Add files via upload|
|2023-03-14 07:39:41|[Tomcat_PUT_GUI_EXP](https://github.com/xiaokp7/Tomcat_PUT_GUI_EXP)|Create README.md|
|2023-03-14 06:26:40|[captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified)|Update README.md|
|2023-03-14 03:28:48|[afrog](https://github.com/zan8in/afrog)|delete poc csz-cms-multiple-blind-sql-injection.yaml|
|2023-03-14 02:45:47|[koko-moni](https://github.com/burpheart/koko-moni)|Update readme.md|
|2023-03-14 02:39:44|[autoDecoder](https://github.com/f0ng/autoDecoder)|Update FAQ.md|
|2023-03-14 02:31:47|[Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki)|更新漏洞|
|2023-03-14 02:23:38|[Awesome-POC](https://github.com/Threekiii/Awesome-POC)|更新漏洞|
|2023-03-13 18:52:40|[super-xray](https://github.com/4ra1n/super-xray)|after release|
|2023-03-13 06:23:54|[404StarLink](https://github.com/knownsec/404StarLink)|weekly update at 2023-03-13|
|2023-03-12 16:40:00|[CDK](https://github.com/cdk-team/CDK)|Merge pull request #80 from cdk-team/v1.5.2-alphaV1.5.<br>2 alpha|
|2023-03-12 11:04:45|[HackBrowserData](https://github.com/moonD4rk/HackBrowserData)|Merge pull request #203 from moonD4rk/fix/leveldbfix: <br>missing key and value in local storage|
|2023-03-12 08:19:38|[domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro)|Update LineEntryMenu.java|
|2023-03-12 00:48:03|[AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool)|Update README.md|
|2023-03-11 13:36:23|[PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book)|漏洞相关:O2OA,联软,金山等相关漏洞|
|2023-03-10 16:04:54|[K8tools](https://github.com/k8gege/K8tools)|Add files via upload|
|2023-03-10 06:38:33|[log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner)|Update README.md|
|2023-03-10 03:31:53|[code6](https://github.com/4x99/code6)|Merge pull request #255 from 4x99/developv1.6.|
|2023-03-10 02:50:32|[Elkeid](https://github.com/bytedance/Elkeid)|using RASP runner|
|2023-03-09 14:17:46|[geacon_pro](https://github.com/H4de5-7/geacon_pro)|Update README.md|
|2023-03-09 12:56:21|[TsojanScan](https://github.com/Tsojan/TsojanScan)|Update README.md|
|2023-03-09 08:35:52|[GoWxDump](https://github.com/SpenserCai/GoWxDump)|fixed #5|
|2023-03-09 04:32:58|[qsnctf-python](https://github.com/Moxin1044/qsnctf-python)|更新README|
|2023-03-08 15:14:14|[QingTing](https://github.com/StarCrossPortal/QingTing)|更新|
|2023-03-08 07:14:47|[pentest_report](https://github.com/dbgee/pentest_report)|Create LICENSE|
|2023-03-08 02:32:40|[cf](https://github.com/teamssix/cf)|Merge pull request #214 from teamssix/betaperf: perf i<br>ssue ci|
|2023-03-07 08:44:53|[knife](https://github.com/bit4woo/knife)|Update ChineseTab.java|
|2023-03-07 07:33:10|[Godzilla](https://github.com/BeichenDream/Godzilla)|Update README.md|
|2023-03-06 14:39:54|[NessusToReport](https://github.com/Hypdncy/NessusToReport)|增加beautifulsoup4包|
|2023-03-06 08:46:31|[veinmind-tools](https://github.com/chaitin/veinmind-tools)|fix(veinmind-sensitive):fix scan path (#205)fix(veinmi<br>nd-sensitive):fix scan pathCo-authored-by: GiveMeAShell<br> |
|2023-03-06 08:41:18|[ElectricRat](https://github.com/linjiananallnt/ElectricRat)|Update README.md|
|2023-03-06 07:44:32|[Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam)|更新README.md|
|2023-03-06 07:41:58|[Vulhub-Reproduce](https://github.com/Threekiii/Vulhub-Reproduce)|更新漏洞|
|2023-03-05 16:10:52|[OA-EXPTOOL](https://github.com/LittleBear4/OA-EXPTOOL)|Add files via upload|
|2023-03-05 02:02:20|[CN_Nessus_Plugins_I<br>nterface](https://github.com/nszy007/CN_Nessus_Plugins_Interface)|20230301|
|2023-03-03 09:32:01|[Antenna](https://github.com/wuba/Antenna)|测试官方镜像2|
|2023-03-02 17:24:57|[rengine](https://github.com/yogeshojha/rengine)|Merge pull request #829 from yogeshojha/release/1.3.6R<br>elease/1.3.6|
|2023-03-01 09:10:31|[CVE-2023-21839](https://github.com/4ra1n/CVE-2023-21839)|Update README.md|
|2023-03-01 08:05:58|[Log4j2Scan](https://github.com/whwlsfb/Log4j2Scan)|replace fastjson to org.json.|
|2023-02-28 14:00:08|[BurpSuite-collectio<br>ns](https://github.com/Mr-xn/BurpSuite-collections)|add npscrack：蓝队利器、溯源反制、NPS 漏洞利用、NPS ex<br>p、NPS poc、一键利用的BurpSuite插件最新版（202212之后）<br>激活项目|
|2023-02-28 07:33:37|[RmTools](https://github.com/RoomaSec/RmTools)|11|
|2023-02-28 06:05:45|[Awesome-Exploit](https://github.com/Threekiii/Awesome-Exploit)|更新CVE-2023-21839 Exploit|
|2023-02-28 04:04:03|[OneScan](https://github.com/vaycore/OneScan)|更新说明文档及截图，添加设置过滤规则配置说明；更新版本<br>号0.5.2|
|2023-02-28 00:18:27|[Platypus](https://github.com/WangYihang/Platypus)|build(deps): bump http-cache-semantics in /web/fronten<br>d (#180)Bumps [http-cache-semantics](https://github.com<br>/kornelski/http-cache-semantics) from 4.1.0 to 4.1.1.- <br>[Release notes](https://github.com/kornelski/http-cache<br>-semantics/releases)- [Commits](https://github.com/korn<br>elski/http-cache-semantics/compare/v4.1.0...v4.1.1)---u<br>pdated-dependencies:- dependency-name: http-cache-seman<br>ticsdependency-type: indirect...Signed-off-by: dependab<br>ot[bot]Co-authored-by: dependabot[bot] |
|2023-02-26 13:10:45|[go_proxy_pool](https://github.com/pingc0y/go_proxy_pool)|Delete src directory|
|2023-02-26 07:24:32|[mitaka](https://github.com/ninoseki/mitaka)|Merge pull request #708 from ninoseki/change-packagech<br>ore: use plasmo build--zip for packaging [skip ci]|
|2023-02-24 13:25:09|[ysomap](https://github.com/wh1t3p1g/ysomap)|update|
|2023-02-24 08:06:16|[nuclei-plus](https://github.com/Yong-An-Dang/nuclei-plus)|update|
|2023-02-24 06:58:54|[Intranet_Penetratio<br>n_Tips](https://github.com/Ridter/Intranet_Penetration_Tips)|增加Exchange利用|
|2023-02-23 09:31:05|[Library-POC](https://github.com/luck-ying/Library-POC)|Update README.md|
|2023-02-23 07:36:27|[xray](https://github.com/chaitin/xray)|[fix] 文档地址|
|2023-02-23 05:56:50|[appshark](https://github.com/bytedance/appshark)|support pattern filed match.|
|2023-02-22 09:36:50|[HaE](https://github.com/gh0stkey/HaE)|Version: 2.4.6 Update|
|2023-02-22 08:29:41|[fscan](https://github.com/shadow1ng/fscan)|Merge pull request #265 from AgeloVito/mainUpdate eval<br>.go|
|2023-02-21 16:11:23|[dirsearch](https://github.com/maurosoria/dirsearch)|Merge pull request #1282 from 0x0d3ad/patch-3Update my<br> profile link github|
|2023-02-21 14:37:50|[RouteVulScan](https://github.com/F6JO/RouteVulScan)|Update README.md|
|2023-02-21 03:50:02|[URLFinder](https://github.com/pingc0y/URLFinder)|2023/2/21更新|
|2023-02-21 03:33:52|[IPSearch](https://github.com/SleepingBag945/IPSearch)|Update README.md|
|2023-02-21 02:04:04|[Scanners-Box](https://github.com/We5ter/Scanners-Box)|[+]Cyber-Buddy/APKHunt|
|2023-02-20 06:54:31|[Kunlun-M](https://github.com/LoRexxar/Kunlun-M)|Merge pull request #224 from LoRexxar/developfixed #22<br>3|
|2023-02-19 18:06:05|[wxapkgUnpack](https://github.com/jdr2021/wxapkgUnpack)|Update README.md|
|2023-02-19 16:36:47|[RedisEXP](https://github.com/yuyan-sec/RedisEXP)|解决支持中文路径|
|2023-02-19 12:41:37|[ffuf](https://github.com/ffuf/ffuf)|Fix HTML output (#640)|
|2023-02-17 13:54:38|[Search_Viewer](https://github.com/G3et/Search_Viewer)|Update search_viewer_ui.py|
|2023-02-17 03:44:49|[OutLook](https://github.com/KrystianLi/OutLook)|Update|
|2023-02-17 03:37:31|[poc-hub](https://github.com/ybdt/poc-hub)|整理|
|2023-02-17 02:22:13|[Xray_Cracked](https://github.com/NHPT/Xray_Cracked)|Update README.md|## 所有项目
### 信息收集
#### 资产测绘采集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll) | V1.2 | 为了方便安全从业人员在使用网络测绘平台进行信息搜集时的效率，本程<br>序集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并且合<br>并展示及导出。 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | v2.3.2 | 【支持Fofa、Zoomeye、Quake等网络空间搜索引擎】闪电搜索器；GUI图<br>形化渗透测试信息搜集工具；资产搜集引擎 |
| [Search_Viewer](https://github.com/G3et/Search_Viewer) | v2.0 | 集Fofa、Hunter鹰图、Shodan、360 quake、Zoomeye 钟馗之眼为一体的g<br>ui图形界面化工具 |
| [koko-moni](https://github.com/burpheart/koko-moni) | v0.0.1 | 一个网络空间搜索引擎监控平台，可定时进行资产信息爬取，及时发现新<br>增资产，本项目聚合了 Fofa、Hunter、Quake、Zoomeye 和 Threatbook 的<br>数据源，并对获取到的数据进行去重与清洗 |
#### 子域名收集
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
#### 目录扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dirsearch](https://github.com/maurosoria/dirsearch) | v0.4.3 | Web path scanner |
| [URLFinder](https://github.com/pingc0y/URLFinder) | 2023.2.21 | 类似JSFinder的golang实现，一款用于快速提取检测页面中JS与URL的工<br>具，更快更全更舒服 |
| [feroxbuster](https://github.com/epi052/feroxbuster) | v2.9.1 | A fast, simple, recursive content discovery tool written in Rust<br>. |
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
| [Glass](https://github.com/s7ckTeam/Glass) |  | Glass是一款针对资产列表的快速指纹识别工具，通过调用Fofa/ZoomEye/<br>Shodan/360等api接口快速查询资产信息并识别重点资产的指纹，也可针对<br>IP/IP段或资产列表进行快速的指纹识别。 |
#### 端口扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [TXPortMap](https://github.com/4dogs-cn/TXPortMap) | v1.1.2 | Port Scanner & Banner Identify From TianXiang |
| [naabu](https://github.com/projectdiscovery/naabu) | v2.1.3 | A fast port scanner written in go with a focus on reliability an<br>d simplicity. Designed to be used in combination with other tools<br> for attack surface discovery in bug bounties and pentests |
| [scaninfo](https://github.com/redtoolskobe/scaninfo) | v1.1.0 | fast scan for redtools |
#### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dismap](https://github.com/zhzyker/dismap) | v0.4 | Asset discovery and identification tools 快速识别 Web 指纹信息，<br>定位资产类型。辅助红队快速定位目标资产信息，辅助蓝队发现疑似脆弱点 |
#### 自动化信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [H](https://github.com/SiJiDo/H) |  | H是一款强大的资产收集管理平台 |
| [X-Marshal](https://github.com/XTeam-Wing/X-Marshal) |  | Golang-分布式资产探测&漏洞扫描&信息收集 |
| [heartsk_community](https://github.com/yqcs/heartsk_community) | LOWBUG@La<br>test | Hearts K-企业资产发现与脆弱性检查工具，自动化资产信息收集与漏洞<br>扫描 |
| [AnScan](https://github.com/Arbor01/AnScan) |  | AnScan是一款集合信息收集、分布式漏洞扫描、漏洞POC管理等为一体的<br>红队扫描工具 |
| [nemo_go](https://github.com/hanc00l/nemo_go) | v2.9.1 | Nemo是用来进行自动化信息收集的一个简单平台，通过集成常用的信息收<br>集工具和技术，实现对内网及互联网资产信息的自动收集，提高隐患排查和<br>渗透测试的工作效率，用Go语言完全重构了原Python版本。 |
| [rengine](https://github.com/yogeshojha/rengine) | v1.3.5 | reNgine is an automated reconnaissance framework for web applica<br>tions with a focus on highly configurable streamlined recon proce<br>ss via Engines, recon data correlation and organization, continuo<br>us monitoring, backed by a database, and simple yet intuitive Use<br>r Interface. reNgine makes it easy for penetration testers to gat<br>her reconnaissance with minimal configuration and with the help o<br>f reNgine's correlation, it just makes recon effortless. |
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
#### 企业信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ENScan_GO](https://github.com/wgpsec/ENScan_GO) | V0.0.9 | 一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息<br>收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚<br>合导出。 |
#### 小程序信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [wxapkgUnpack](https://github.com/jdr2021/wxapkgUnpack) | 1.0 | wxapkg解密解包工具，提供C#和wxappUnpacker两个版本的解包，并提取J<br>S中的URL和IP。 |
#### C段信息收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [IPSearch](https://github.com/SleepingBag945/IPSearch) | v0.1 | 离线IP Whois查询工具。可根据IP查询所属IP段信息、根据关键词查询IP<br>段信息 |
#### IP反查域名
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [iplookup](https://github.com/Lengso/iplookup) | v1.1 | IP反查域名 |
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
| [nuclei](https://github.com/projectdiscovery/nuclei) | v2.9.0 | Fast and customizable vulnerability scanner based on simple YAML<br> based DSL. |
| [afrog](https://github.com/zan8in/afrog) | v2.2.1 | A Vulnerability Scanning Tools For Penetration Testing |
| [vulmap](https://github.com/zhzyker/vulmap) | v0.9 | Vulmap 是一款 web 漏洞扫描和验证工具, 可对 webapps 进行漏洞扫描,<br> 并且具备漏洞验证功能 |
| [POC-bomber](https://github.com/tr0uble-mAker/POC-bomber) | v2.0.2-PO<br>C-bomber | 利用大量高威胁poc/exp快速获取目标权限，用于渗透和红队快速打点 |
| [QingTing](https://github.com/StarCrossPortal/QingTing) | v0.3 | 蜻蜓安全一个安全工具编排平台,可以自由编排你的工具流,集成108款工<br>具,包括xray、nmap、awvs等;你可以将喜欢的工具编排成一个场景，快速打<br>造适合自己的安全工作台~ |
| [myscan](https://github.com/amcai/myscan) |  | myscan被动扫描 |
#### 漏洞扫描框架
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pocsuite3](https://github.com/knownsec/pocsuite3) | v2.0.2 | pocsuite3 is an open-sourced remote vulnerability testing framew<br>ork developed by the Knownsec 404 Team. |
| [Godscan](https://github.com/Guoke324/Godscan) | Godscan | Godscan 是一款python编写的具有图形化界面的漏洞检测框架，可以之定<br>义漏洞检测 poc ，主要是帮助安全测试者，更好的去记录和整理历史漏洞<br>，以便更好的进行漏洞检测，提高工作效率！ |
| [FrameScan-GUI](https://github.com/qianxiao996/FrameScan-GUI) | v1.4.2 | FrameScan-GUI 一款python3和Pyqt编写的具有图形化界面的cms漏洞检测<br>框架。 |
| [Gr33k](https://github.com/lijiaxing1997/Gr33k) |  | 图形化漏洞利用集成工具 |
| [kunpeng](https://github.com/opensec-cn/kunpeng) | 20190527 | kunpeng是一个Golang编写的开源POC框架/库，以动态链接库的形式提供<br>各种语言调用，通过此项目可快速开发漏洞检测类的系统。 |
| [pocassist](https://github.com/jweny/pocassist) | 1.0.5 | 全新的漏洞测试框架。 |
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
| [RequestTemplate](https://github.com/1n7erface/RequestTemplate) | v1.1.3 | 双语双端内网扫描以及验证工具 |
| [redis-rogue-server](https://github.com/Dliv3/redis-rogue-server) |  | Redis 4.x/5.x RCE |
#### Shell管理
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Behinder](https://github.com/rebeyond/Behinder) | Behinder_<br>v4.0.6 | “冰蝎”动态二进制加密网站管理客户端 |
| [Godzilla](https://github.com/BeichenDream/Godzilla) | v4.0.1-go<br>dzilla | 哥斯拉 |
| [antSword](https://github.com/AntSwordProject/antSword) | 2.1.15 | 中国蚁剑是一款跨平台的开源网站管理工具。AntSword is a cross-plat<br>form website management toolkit. |
| [Platypus](https://github.com/WangYihang/Platypus) | v1.5.0 | :hammer: A modern multiple reverse shell sessions manager writte<br>n in go |
| [As-Exploits](https://github.com/yzddmr6/As-Exploits) |  | 中国蚁剑后渗透框架 |
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
| [SpringBoot-Scan-GUI](https://github.com/13exp/SpringBoot-Scan-GUI) | v1.2.2 |  |
| [CVE-2023-21839](https://github.com/4ra1n/CVE-2023-21839) |  | Weblogic CVE-2023-21839 RCE (无需Java依赖一键RCE) |
| [Tomcat_PUT_GUI_EXP](https://github.com/xiaokp7/Tomcat_PUT_GUI_EXP) | 1.4 | Tomcat PUT方法任意文件写入（CVE-2017-12615）exp |
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
| [revsuit](https://github.com/Li4n0/revsuit) | v0.5.2 | RevSuit is a flexible and powerful reverse connection platform d<br>esigned for receiving connection from target host in penetration.<br>  |
| [DNSlog-GO](https://github.com/lanyi1998/DNSlog-GO) | 1.5.2 | DNSLog-GO 是一款golang编写的监控 DNS 解析记录的工具，自带WEB界面 |
| [godnslog](https://github.com/chennqqi/godnslog) | v0.7.0 | An exquisite dns&http log server for verify SSRF/XXE/RFI/RCE vul<br>nerability  |
| [ysomap](https://github.com/wh1t3p1g/ysomap) | v0.1.3 | A helpful Java Deserialization exploit framework. |
| [Antenna](https://github.com/wuba/Antenna) | v1.3.2 | Antenna是58同城安全团队打造的一款辅助安全从业人员验证网络中多种<br>漏洞是否存在以及可利用性的工具。其基于带外应用安全测试(OAST)通过任<br>务的形式，将不同漏洞场景检测能力通过插件的形式进行集合，通过与目标<br>进行out-bind的数据通信方式进行辅助检测。 |
| [cola_dnslog](https://github.com/AbelChe/cola_dnslog) | v1.3.2 | Cola Dnslog v1.3.2 更加强大的dnslog平台/无回显漏洞探测辅助平台 <br>完全开源 dnslog httplog ldaplog rmilog 支持dns http ldap rmi等协议<br> 提供API调用方式便于与其他工具结合 支持钉钉机器人、Bark等提醒 支<br>持docker一键部署 后端完全使用python实现 前端基于vue-element-admin<br>二开 |
| [ddddocr](https://github.com/sml2h3/ddddocr) |  | 带带弟弟 通用验证码识别OCR pypi版 |
| [ysoserial](https://github.com/su18/ysoserial) | v1.4 | ysoserial for su18 |
| [JNDIExploit](https://github.com/WhiteHSBG/JNDIExploit) | v1.4 | 对原版https://github.com/feihong-cs/JNDIExploit 进行了实用化修改 |
| [JNDIExploit-1](https://github.com/Mr-xn/JNDIExploit-1) | v1.2 | 一款用于 JNDI注入 利用的工具，大量参考/引用了 Rogue JNDI 项目的<br>代码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的方式<br>，适用于与自动化工具配合使用。（from https://github.com/feihong-cs<br>/JNDIExploit） |
| [JNDIExploit](https://github.com/0x727/JNDIExploit) | 1.1 | 一款用于JNDI注入利用的工具，大量参考/引用了Rogue JNDI项目的代码<br>，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的方式，适<br>用于与自动化工具配合使用。 |
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
| [wpscan](https://github.com/wpscanteam/wpscan) | v3.8.22 | WPScan WordPress security scanner. Written for security professi<br>onals and blog maintainers to test the security of their WordPres<br>s websites. Contact us via contact@wpscan.com |
| [wprecon](https://github.com/AngraTeam/wprecon) |  |  |
| [Aazhen-RexHa](https://github.com/zangcc/Aazhen-RexHa) | Aazhen-Re<br>xHa_Scanne<br>r | 自研JavaFX图形化漏洞扫描工具，支持扫描的漏洞分别是： ThinkPHP-2.<br>x-RCE， ThinkPHP-5.0.23-RCE， ThinkPHP5.0.x-5.0.23通杀RCE， Think<br>PHP5-SQL注入&敏感信息泄露， ThinkPHP 3.x 日志泄露NO.1， ThinkPHP <br>3.x 日志泄露NO.2， ThinkPHP 5.x 数据库信息泄露的漏洞检测，以及批<br>量检测的功能。漏洞POC基本适用ThinkPHP全版本漏洞。 |
| [ThinkphpGUI](https://github.com/Lotus6/ThinkphpGUI) | 1.3 | Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，getsh<br>ell。 |
| [thinkphp_gui_tools](https://github.com/bewhale/thinkphp_gui_tools) | v2.4.2 | ThinkPHP漏洞综合利用工具, 图形化界面, 命令执行, 一键getshell, 批<br>量检测, 日志遍历, session包含,宝塔绕过 |
| [Apt_t00ls](https://github.com/White-hua/Apt_t00ls) | v0.6 | 高危漏洞利用工具 |
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
| [JDumpSpider](https://github.com/whwlsfb/JDumpSpider) | V1.1 | HeapDump敏感信息提取工具 |
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
| [poc-hub](https://github.com/ybdt/poc-hub) |  | 漏洞检测、漏洞利用 |
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
#### 信息泄露监控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [code6](https://github.com/4x99/code6) | 1.6.4 | 码小六 - GitHub 代码泄露监控系统 |
| [gshark](https://github.com/madneal/gshark) | v1.1.4 | Scan for sensitive information easily and effectively. |
#### windows提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BadPotato](https://github.com/BeichenDream/BadPotato) |  | Windows 权限提升 BadPotato |
#### linux提权
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dirtycow](https://github.com/firefart/dirtycow) |  | Dirty Cow exploit - CVE-2016-5195 |
#### 安卓漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [appshark](https://github.com/bytedance/appshark) | v0.1.2 | Appshark is a static taint analysis platform to scan vulnerabili<br>ties in an Android app. |
#### 代码审计
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [murphysec](https://github.com/murphysecurity/murphysec) | v3.0.1 | An open source tool focused on software supply chain security. <br>墨菲安全专注于软件供应链安全，具备专业的软件成分分析（SCA）、漏洞<br>检测、专业漏洞库。 |
| [Kunlun-M](https://github.com/LoRexxar/Kunlun-M) | v2.6.5 | KunLun-M是一个完全开源的静态白盒扫描工具，支持PHP、JavaScript的<br>语义扫描，基础安全、组件安全扫描，Chrome Ext\Solidity的基础扫描。 |
| [CodeQLpy](https://github.com/webraybtl/CodeQLpy) |  | CodeQLpy是一款基于CodeQL实现的半自动化代码审计工具，目前仅支持ja<br>va语言。实现从源码反编译，数据库生成，脆弱性发现的全过程，可以辅<br>助代码审计人员快速定位源码可能存在的漏洞。 |
#### 容器漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [veinmind-tools](https://github.com/chaitin/veinmind-tools) | v2.0.6 | veinmind-tools 是由长亭科技自研，基于 veinmind-sdk 打造的容器安<br>全工具集 |
#### 容器漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CDK](https://github.com/cdk-team/CDK) | v1.5.2 | 📦Make security testing of K8s, Docker, and Containerd easier. |
#### 信息泄露漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [cf](https://github.com/teamssix/cf) | v0.4.4 | Cloud Exploitation Framework 云环境利用框架，方便安全人员在获得 <br>AK 的后续工作 |
| [Cloud-Bucket-Leak-D<br>etection-Tools](https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools) | v0.4.0 | 六大云存储，泄露利用检测工具 |
#### 漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [slowhttptest](https://github.com/shekyan/slowhttptest) | v1.9.0 | Application Layer DoS attack simulator |
#### WEB漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SSTImap](https://github.com/vladko312/SSTImap) | v1.0 | Automatic SSTI detection tool with interactive interface |
| [tplmap](https://github.com/epinna/tplmap) | v0.5 | Server-Side Template Injection and Code Injection Detection and <br>Exploitation Tool |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | 1.7 | Automatic SQL injection and database takeover tool |
#### 远控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [noterce](https://github.com/xiao-zhu-zhu/noterce) | v1.1 | 一种另辟蹊径的免杀执行系统命令的木马 |
### 内网渗透
#### 密码提取
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [getIntrInfo](https://github.com/Potato-py/getIntrInfo) |  | 收集内部网信息。包括：浏览器书签、密码和浏览历史记录、cookie。Wi<br>fi信息和密码。主机信息。 |
| [FinalShell-Decoder](https://github.com/passer-W/FinalShell-Decoder) | V1.0 | FinallShell 密码解密GUI工具 |
| [Xdecrypt](https://github.com/dzxs/Xdecrypt) |  | Xshell Xftp password decrypt |
| [HackBrowserData](https://github.com/moonD4rk/HackBrowserData) | v0.4.4 | Decrypt passwords/cookies/history/bookmarks from the browser. 一<br>款可全平台运行的浏览器数据导出解密工具。 |
#### 代理转发
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [reGeorg](https://github.com/sensepost/reGeorg) |  | The successor to reDuh, pwn a bastion webserver and create SOCKS<br> proxies through the DMZ. Pivot and pwn. |
| [Stowaway](https://github.com/ph4ntonn/Stowaway) | v2.1 | 👻Stowaway -- Multi-hop Proxy Tool for pentesters |
| [PortForward](https://github.com/knownsec/PortForward) | 0.5.0 | The port forwarding tool developed by Golang solves the problem <br>that the internal and external networks cannot communicate in cer<br>tain scenarios |
#### 密码读取
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SharpDecryptPwd](https://github.com/ianxtianxt/SharpDecryptPwd) |  | Windows常用程序密码读取工具：SharpDecryptPwd |
#### 漏洞发现
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InScan](https://github.com/inbug-team/InScan) |  | 边界打点后的自动化渗透工具 |
| [kscan](https://github.com/lcvvvv/kscan) | v1.85 | Kscan是一款纯go开发的全方位扫描器，具备端口扫描、协议检测、指纹<br>识别，暴力破解等功能。支持协议1200+，协议指纹10000+，应用指纹20000<br>+，暴力破解协议10余种。 |
| [fscan](https://github.com/shadow1ng/fscan) | 1.8.2 | 一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。 |
| [Gscan](https://github.com/hack2fun/Gscan) | v1.0 | Gscan is a high concurrency scanner based on golang |
#### 漏洞利用框架
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Viper](https://github.com/FunnyWolf/Viper) | v1.5.26 | Redteam operationplatform with webui 图形化红队行动辅助平台 |
#### 横向工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [WMIHACKER](https://github.com/rootclay/WMIHACKER) |  | A Bypass Anti-virus Software Lateral Movement Command Execution <br>Tool |
#### 免杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shellcodeloader](https://github.com/knownsec/shellcodeloader) | v1.1 | shellcodeloader |
| [AV_Evasion_Tool](https://github.com/1y0n/AV_Evasion_Tool) | 20230303 | 掩日 - 免杀执行器生成工具 |
#### 漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ServerScan](https://github.com/Adminisme/ServerScan) | v1.0.2 | ServerScan一款使用Golang开发的高并发网络扫描、服务探测工具。 |
### 相关资源
#### 工具集成环境
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先<br>利其器。 |
| [CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools) |  | 渊龙Sec安全团队CTF&AWD工具箱 |
| [PenKitGui](https://github.com/ccc-f/PenKitGui) |  | 渗透测试武器库 |
| [Taie-RedTeam-OS](https://github.com/taielab/Taie-RedTeam-OS) |  | 泰阿安全实验室-基于XUbuntu私人订制的红蓝对抗渗透操作系统 |
| [FreeGui](https://github.com/tyB-or/FreeGui) | v2.5 | freeGui：基于ttkbootstrap开发的一款用来管理自己的渗透测试工具的<br>一个小工具，并提供一些实用小功能，例如打开目录，运行工具，工具备忘<br>命令。 |
| [GUI_Tools](https://github.com/ghealer/GUI_Tools) | V1.1 | 一个由各种图形化渗透工具组成的工具集 |
#### 知识库
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [penetration-suite-t<br>oolkit](https://github.com/makoto56/penetration-suite-toolkit) | v4.0 | 本项目制作的初衷是帮助渗透新手快速搭建工作环境，工欲善其事，必先<br>利其器。 |
| [Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam) |  | 一个红队知识仓库 |
| [Threathunting-book](https://github.com/12306Bro/Threathunting-book) |  |  |
| [PenetrationTesttips](https://github.com/CYJoe-Cyclone/PenetrationTesttips) |  | 渗透测试Tips - Version1.3 |
| [Intranet_Penetratio<br>n_Tips](https://github.com/Ridter/Intranet_Penetration_Tips) |  | 2018年初整理的一些内网渗透TIPS，后面更新的慢，所以整理出来希望跟<br>小伙伴们一起更新维护~ |
| [Vuln-List](https://github.com/wwl012345/Vuln-List) |  | (持续更新)对网上出现的各种OA、中间件、CMS等漏洞进行整理，主要包<br>括漏洞介绍、漏洞影响版本以及漏洞POC/EXP等，并且会持续更新。 |
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
| [go_proxy_pool](https://github.com/pingc0y/go_proxy_pool) | 2022.11.2<br>2 | 无环境依赖开箱即用的代理IP池 |
| [rotateproxy](https://github.com/akkuman/rotateproxy) | v0.7.2 | 利用fofa搜索socks5开放代理进行代理池轮切的工具 |
| [Gofreeproxy](https://github.com/ja9er/Gofreeproxy) | v0.1 | 自用的动态代理小工具 |
#### 工具集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [K8tools](https://github.com/k8gege/K8tools) |  | K8工具合集(内网渗透/提权工具/远程溢出/漏洞利用/扫描工具/密码破解<br>/免杀工具/Exploit/APT/0day/Shellcode/Payload/priviledge/BypassUAC<br>/OverFlow/WebShell/PenTest) Web GetShell Exploit(Struts2/Zimbra/W<br>eblogic/Tomcat/Apache/Jboss/DotNetNuke/zabbix) |
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
| [HaE](https://github.com/gh0stkey/HaE) | 2.4.6 | HaE - Highlighter and Extractor, 赋能白帽 高效作战 |
| [domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro) | v1.9-alph<br>a | domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集；<br>快速Title获取；外部工具联动；等等 |
| [Sylas](https://github.com/Acmesec/Sylas) | 1.1.1 | 新一代子域名主/被动收集工具 - Subdomain automatic/passive collec<br>tion tool |
| [GadgetProbe](https://github.com/BishopFox/GadgetProbe) | v1.0 | Probe endpoints consuming Java serialized objects to identify cl<br>asses, libraries, and library versions on remote Java classpaths. |
| [HopLa](https://github.com/synacktiv/HopLa) | 1.2 |  HopLa Burp Suite Extender plugin -Adds autocompletion support a<br>nd useful payloads in Burp Suite |
| [captcha-killer-modi<br>fied](https://github.com/f0ng/captcha-killer-modified) | 0.22 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免费<br>ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, sup<br>port AES/RSA/DES/ExecJs(execute JS encryption code in burpsuite).<br> 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSuite插<br>件 |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.23 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等）<br>，类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础上，<br>不影响APP、网站加解密正常逻辑等。 |
| [burpFakeIP](https://github.com/TheKingOfDuck/burpFakeIP) | 1.1 | 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件 |
| [AutoRepeater](https://github.com/nccgroup/AutoRepeater) |  | Automated HTTP Request Repeating With Burp Suite |
| [http-request-smuggl<br>er](https://github.com/portswigger/http-request-smuggler) |  |  |
| [burp-requests](https://github.com/silentsignal/burp-requests) | v0.2.4 | Copy as requests plugin for Burp Suite |
| [CORSScanner](https://github.com/zzzskd/CORSScanner) |  | CORS 跨域漏洞 burp 插件 |
| [fastjson-exp](https://github.com/skisw/fastjson-exp) |  |  |
| [HostHeaderAttack](https://github.com/weujieytt/HostHeaderAttack) | 0.1 | 检测host头攻击的Burpsuite被动扫描插件，Burpsuite passive scannin<br>g plugin responsible for detecting host header attack |
| [knife](https://github.com/bit4woo/knife) | v2.1 | A burp extension that add some useful function toContext Menu 添<br>加一些右键菜单让burp用起来更顺畅 |
| [log4j2burpscanner](https://github.com/f0ng/log4j2burpscanner) | 0.23.0-be<br>ta2 | CVE-2021-44228 Log4j2 BurpSuite Scanner,Customize ceye.io api or<br> other apis,including internal networks |
| [passive-scan-client](https://github.com/c0ny1/passive-scan-client) | 0.3.1 | Burp被动扫描流量转发插件 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpSuiteCn](https://github.com/funkyoummp/BurpSuiteCn) | V2.0 | Burp Suite汉化 中文 |
| [NEW_xp_CAPTCHA](https://github.com/smxiazi/NEW_xp_CAPTCHA) | 4.2 | xp_CAPTCHA(瞎跑 白嫖版) burp 验证码 识别 burp插件 |
| [npscrack](https://github.com/weishen250/npscrack) | npscrack-<br>1.0 | 蓝队利器、溯源反制、NPS 漏洞利用、NPS exp、NPS poc、Burp插件、一<br>键利用 |
| [OneScan](https://github.com/vaycore/OneScan) | v0.5.2 | OneScan是一个递归目录扫描的BurpSuite插件 |
| [OutLook](https://github.com/KrystianLi/OutLook) | v1.2.0 | 一款OutLook信息收集工具 |
| [passive-scan-client<br>-plus](https://github.com/winezer0/passive-scan-client-plus) | v0.4.12.0 | burpsuite passive-scan-client 插件维护分支 |
| [BurpCRLFScan](https://github.com/A0WaQ4/BurpCRLFScan) | 1.4 | 使用java编写的CRLF-Injection-burp被动扫描插件 |
| [JsonDetect](https://github.com/a1phaboy/JsonDetect) | v1.0 | A burp Extender to detect json, include fastjson,jackson,gson |
| [burp-text4shell](https://github.com/silentsignal/burp-text4shell) | v0.1 | Text4Shell scanner for Burp Suite |
| [sweetPotato](https://github.com/z2p/sweetPotato) | version1.<br>4 | 基于burpsuite的资产分析工具 |
| [xia_Liao](https://github.com/smxiazi/xia_Liao) | 1.6 | xia Liao（瞎料）burp插件 用于Windows在线进程/杀软识别 与 web渗透<br>注册时，快速生成需要的资料用来填写，资料包含：姓名、手机号、身份证<br>、统一社会信用代码、组织机构代码、银行卡，以及各类web语言的hello w<br>orld输出和生成弱口令字典等。 |
| [base64encode](https://github.com/handbye/base64encode) | 1.0 | burpsuite POST数据包base64编码插件 |
| [HackTools](https://github.com/Vicl1fe/HackTools) | 1.4 | 提高渗透测试效率。#Burp插件##渗透测试##小工具# |
| [burp-awesome-tls](https://github.com/sleeyax/burp-awesome-tls) | v0.0.4 | Fix Burp Suite's horrible TLS stack & spoof any browser fingerpr<br>int |
| [JustC2file](https://github.com/Peithon/JustC2file) | v1.0.2 | Burp插件，Malleable C2 Profiles生成器；可以通过Burp代理选中请求<br>，生成Cobalt Strike的profile文件(CSprofile) |
| [Log4j-check](https://github.com/bigsizeme/Log4j-check) |  | log4J burp被扫插件、CVE-2021-44228、支持dnclog.cn和burp内置DNS、<br>可配合JNDIExploit生成payload |
| [Log4j2Scan](https://github.com/whwlsfb/Log4j2Scan) | V0.13.1 | Log4j2 RCE Passive Scanner plugin for BurpSuite |
| [BurpBountyPlus](https://github.com/ggg4566/BurpBountyPlus) | 3 | BurpBounty 魔改版本 |
| [BurpExtractor](https://github.com/NetSPI/BurpExtractor) | v1.3.4 | A Burp extension for generic extraction and reuse of data within<br> HTTP requests and responses. |
| [burp-cph](https://github.com/elespike/burp-cph) | 3.0 | Custom Parameter Handler extension for Burp Suite. |
| [BurpJSLinkFinder](https://github.com/InitRoot/BurpJSLinkFinder) |  | Burp Extension for a passive scanning JS files for endpoint link<br>s. |
| [JC-AntiToken](https://github.com/chroblert/JC-AntiToken) |  | burp插件：python版，token防重放绕过 |
| [BurpSuite_403Bypass<br>er](https://github.com/sting8k/BurpSuite_403Bypasser) |  | Burpsuite Extension to bypass 403 restricted directory |
| [Burp-Non-HTTP-Exten<br>sion](https://github.com/summitt/Burp-Non-HTTP-Extension) | v1.6 | Non-HTTP Protocol Extension (NoPE) Proxy and DNS for Burp Suite. |
| [shiro-check](https://github.com/bigsizeme/shiro-check) | shirochek<br>3.0 | Shiro反序列化回显利用、内存shell、检查 Burp插件 |
| [FastjsonScan](https://github.com/Maskhe/FastjsonScan) | 1.0 | 一个简单的Fastjson反序列化检测burp插件 |
| [fastjsonScan](https://github.com/zilong3033/fastjsonScan) |  |  |
| [BurpSuite-Extender-<br>fastjson](https://github.com/uknowsec/BurpSuite-Extender-fastjson) |  | Reference：https://www.w2n1ck.com/article/44/ |
| [BurpSuite-Xkeys](https://github.com/vsec7/BurpSuite-Xkeys) |  | A Burp Suite Extension to extract interesting strings (key, secr<br>et, token, or etc.) from a webpage. |
| [Burp_AES_Plugin](https://github.com/jas502n/Burp_AES_Plugin) |  | Burpsuite Plugin For AES Crack |
| [burpJsEncrypter](https://github.com/TheKingOfDuck/burpJsEncrypter) | 0.1 | More Easier Burp Extension To Solve Javascript Front End Encrypt<br>ion,一款更易使用的解决前端加密问题的Burp插件。 |
| [captcha-killer](https://github.com/c0ny1/captcha-killer) | 0.1.2 | burp验证码识别接口调用插件 |
| [BurpSuiteHTTPSmuggl<br>er](https://github.com/nccgroup/BurpSuiteHTTPSmuggler) | v0.1 | A Burp Suite extension to help pentesters to bypass WAFs or test<br> their effectiveness using a number of techniques |
| [sqlmap4burp-plus-pl<br>us](https://github.com/c0ny1/sqlmap4burp-plus-plus) | 0.2 | sqlmap4burp++是一款兼容Windows，mac，linux多个系统平台的Burp与sq<br>lmap联动插件 |
| [domain_hunter](https://github.com/bit4woo/domain_hunter) | v1.5 | A Burp Suite Extension that try to find all sub-domain, similar-<br>domain and related-domain of an organization automatically! 基于<br>流量自动收集整个企业或组织的子域名、相似域名、相关域名的burp插件 |
| [reCAPTCHA/blob](https://github.com/bit4woo/reCAPTCHA/blob) |  |  |
| [BurpSuiteLoggerPlus<br>Plus](https://github.com/nccgroup/BurpSuiteLoggerPlusPlus) |  |  |
| [HackBar](https://github.com/d3vilbug/HackBar) | 2.0 | HackBar plugin for Burpsuite |
| [chunked-coding-conv<br>erter](https://github.com/c0ny1/chunked-coding-converter) | 0.4.0 | Burp suite 分块传输辅助插件 |
| [TsojanScan](https://github.com/Tsojan/TsojanScan) | v1.4.4 | 一个集成的BurpSuite漏洞探测插件 |
#### xray
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [yarx](https://github.com/zema1/yarx) | v0.2.0 | An awesome reverse engine for xray poc. | 一个自动化根据 xray po<br>c 生成对应靶站的工具 |
| [xray-poc-generation](https://github.com/phith0n/xray-poc-generation) |  | 🧬 辅助生成 XRay YAML POC |
| [super-xray](https://github.com/4ra1n/super-xray) | 1.6 | Web漏洞扫描工具XRAY的GUI启动器 (Web Vulnerability Scanner GUI St<br>arter) |
| [Xray_Cracked](https://github.com/NHPT/Xray_Cracked) | v1.9.4 | Update Xray1.9.4 Cracked for Windows,Linux and Mac OS. |
#### pocsuite3
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ExpToPocsuite3](https://github.com/smallfox233/ExpToPocsuite3) | v1.0 | goby exp批量转换为pocsuite3 exp脚本 |
#### 浏览器扩展
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Hack-Tools](https://github.com/LasCC/Hack-Tools) | 0.5.0 | The all-in-one Red Team extension for Web Pentester 🛠 |
| [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega) | v2.5.20 | Manage and switch between multiple proxies quickly & easily. |
| [untrusted-types](https://github.com/filedescriptor/untrusted-types) | 1.1.1 |  |
| [fofa_view](https://github.com/fofapro/fofa_view) | v0.0.5 | FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件，目前兼容Chrome<br>、Firefox、Opera。 |
| [mitaka](https://github.com/ninoseki/mitaka) | v1.0.0 | A browser extension for OSINT search |
| [anti-honeypot](https://github.com/cnrstar/anti-honeypot) |  | 一款可以检测WEB蜜罐并阻断请求的Chrome插件 |
| [Chromium-based-XSS-<br>Taint-Tracking](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) | v0.3 | Cyclops 是一款具有 XSS 检测功能的浏览器 |
| [Zoomeye-Tools](https://github.com/knownsec/Zoomeye-Tools) |  | Zoomeye Tools是配合Zoomeye使用的Chrome插件 |
| [Heimdallr](https://github.com/graynjo/Heimdallr) | v1.1.3 | 一款完全被动监听的谷歌插件，用于高危指纹识别、蜜罐特征告警和拦截<br>、机器特征对抗 |
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
| [nuclei-plus](https://github.com/Yong-An-Dang/nuclei-plus) | v7.0.0 | Functional enhancement based on nuclei |
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
#### arl
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ARL-Finger-ADD](https://github.com/loecho-sec/ARL-Finger-ADD) |  | 灯塔（最新版）指纹添加脚本！ |
#### cobaltstrike
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [taowu-cobalt-strike](https://github.com/pandasec888/taowu-cobalt-strike) |  |  |
| [geacon_pro](https://github.com/H4de5-7/geacon_pro) |  |  |
#### ZoomEye
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Kunyu](https://github.com/knownsec/Kunyu) | v1.7.2 | Kunyu, more efficient corporate asset collection |
| [ZoomEye-python](https://github.com/knownsec/ZoomEye-python) | v2.1.2 | ZoomEye-python: The official Python library and CLI by Knownsec <br>404 Team. |
| [ZoomEye-go](https://github.com/gyyyy/ZoomEye-go) | v1.5 | The Golang SDK and CLI of ZoomEye@Knownsec by gyyyy. |
#### frida
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [frida-skeleton](https://github.com/Margular/frida-skeleton) | v2.0.0 | 基于frida的安卓hook框架，提供了很多frida自身不支持的功能，将hook<br>安卓变成简单便捷，人人都会的事情 |
#### fofa
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [fofax](https://github.com/xiecat/fofax) | v0.1.42 | fofax is a command line query tool based on the API of https://f<br>ofa.info/, simple is the best! |
### CTF杂项
#### 图片隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegsolve](https://github.com/Giotino/stegsolve) | v1.4 |  |
| [BlindWatermark](https://github.com/ww23/BlindWatermark) | v0.0.3 | Java 盲水印 |
| [cloacked-pixel](https://github.com/livz/cloacked-pixel) |  | LSB steganography and detection |
| [CTFpics](https://github.com/RetrO-hash/CTFpics) |  | 用于自动化检测CTF中常出现得工具图片隐写题目 |
| [ImageStrike](https://github.com/zR00t1/ImageStrike) | V0.2 | ImageStrike是一款用于CTF中图片隐写的综合利用工具 |
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
| [GoWxDump](https://github.com/SpenserCai/GoWxDump) | v1.0.9 | SharpWxDump的Go语言版。微信客户端取证，获取信息(微信号、手机号、<br>昵称)，微信聊天记录分析(Top N聊天的人、统计聊天最频繁的好友排行、<br>关键词列表搜索等) |
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
| [qsnctf-python](https://github.com/Moxin1044/qsnctf-python) | 0.0.8.9 | 青少年CTF的Python包，方便大家调用一些CTF常用功能。 |
| [CTF-Tools](https://github.com/qianxiao996/CTF-Tools) | v1.3.7 | 一款Python+Pyqt写的CTF编码、解码、加密、解密工具。 |
| [CTF_Hacker-Tools](https://github.com/Harveysn0w/CTF_Hacker-Tools) |  | CTF-渗透测试~工具合集 |
### CTF逆向
#### pyc逆向
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegosaurus](https://github.com/AngelKitty/stegosaurus) | 1.0 | A steganography tool for embedding payloads within Python byteco<br>de. |
#### Java反编译
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [JavaDecompileTool-G<br>UI](https://github.com/MountCloud/JavaDecompileTool-GUI) | V1.2 | Java Decompile Tool GUI-JAVA反编译工具（界面版） |
| [CodeReviewTools](https://github.com/Ppsoft1991/CodeReviewTools) | v1.31 | 通过正则搜索、批量反编译特定Jar包中的class名称 |
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
#### 内存马查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [shell-analyzer](https://github.com/4ra1n/shell-analyzer) | 0.1 | Java内存马查杀GUI工具，实时动态分析，支持本地和远程查杀 |
### 其他
#### 其他
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [faker](https://github.com/joke2k/faker) | v17.6.0 | Faker is a Python package that generates fake data for you. |
| [SmsForwarder](https://github.com/pppscn/SmsForwarder) | v3.2.0 | 短信转发器——监控Android手机短信、来电、APP通知，并根据指定规则<br>转发到其他手机：钉钉群自定义机器人、钉钉企业内机器人、企业微信群机<br>器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram<br>机器人、Server酱、PushPlus、手机短信等。包括主动控制服务端与客户端<br>，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。（V3.0 新<br>增）PS.这个APK主要是学习与自用，如有BUG请提ISSUE，同时欢迎大家提PR<br>指正 |
| [dbeaver](https://github.com/dbeaver/dbeaver) | 23.0.0 | Free universal database tool and SQL client |
| [MySQLMonitor](https://github.com/TheKingOfDuck/MySQLMonitor) | 1.0 | MySQL实时监控工具(代码审计/黑盒/白盒审计辅助工具) |
#### 渗透测试报告辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [APTRS](https://github.com/Anof-cyber/APTRS) | 0.1 | Automated Penetration Testing Reporting System |
| [BugRepoter_0x727](https://github.com/0x727/BugRepoter_0x727) |  | BugRepoter_0x727(自动化编写报告平台)根据安全团队定制化协同管理项<br>目安全，可快速查找历史漏洞，批量导出报告。 |
| [Savior](https://github.com/Mustard404/Savior) | new | 渗透测试报告自动生成工具！ |
| [SAReport](https://github.com/1u0Hun/SAReport) |  | 渗透测试自动化报告平台 |
| [pentest_report](https://github.com/dbgee/pentest_report) | v1.0.0 | 渗透测试报告生成 |
#### 动态口令
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [rotp](https://github.com/mdp/rotp) |  | Ruby One Time Password library |
#### 科学上网
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [v2rayA](https://github.com/v2rayA/v2rayA) | v2.0.1 | A web GUI client of Project V which supports V2Ray, Xray, SS, SS<br>R, Trojan and Pingtunnel 🚀 |
#### 笔记
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) |  | Python - 100天从新手到大师 |
#### 渗透测试报告管理
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [report](https://github.com/CTF-MissFeng/report) | v1.0.1 | 乙方渗透测试漏洞报告管理系统 |
#### 文档
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [HackReport](https://github.com/awake1t/HackReport) |  | 渗透测试报告/资料文档/渗透经验文档/安全书籍 |
### 安全产品
#### 威胁检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmEye](https://github.com/RoomaSec/RmEye) | v0.0.4 | 戎码之眼是一个window上的基于att&ck模型的威胁监控工具.有效检测常<br>见的未知威胁与已知威胁.防守方的利剑 |
#### 主机入侵检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Elkeid](https://github.com/bytedance/Elkeid) | scanner-v<br>2.2.0.1_20<br>230315 | Elkeid is an open source solution that can meet the security req<br>uirements of various workloads such as hosts, containers and K8s,<br> and serverless. It is derived from ByteDance's internal best pra<br>ctices. |
| [Hades](https://github.com/theSecHunter/Hades) |  | Hades is an cross-platform HIDS with kernel-space data collectio<br>n. |
#### Web应用防火墙
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [openstar](https://github.com/starjun/openstar) |  | lua waf,nginx+lua,openresty,luajit,waf+,cdn,nginx |
#### 欺骗防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Juggler](https://github.com/C4o/Juggler) |  | A system that may trick hackers.针对黑客的拟态欺骗系统。 |
| [MySQL_Fake_Server](https://github.com/fnmsd/MySQL_Fake_Server) |  | MySQL Fake Server use to help MySQL Client File Reading and JDBC<br> Client Java Deserialize |
| [MysqlT](https://github.com/BeichenDream/MysqlT) | v1.0 | 伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击攻<br>击者 |
#### 主机入侵防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [iDefender](https://github.com/wecooperate/iDefender) | 2.5.0 | iDefender（冰盾 - 终端主动防御系统） |
### 应急工具
#### 后门查杀
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [RmTools](https://github.com/RoomaSec/RmTools) |  | 蓝队应急工具 |
### 靶场
#### web靶场
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ElectricRat](https://github.com/linjiananallnt/ElectricRat) | v1.3.0 | 电气鼠靶场系统是一种带有漏洞的Web应用程序，旨在为Web安全渗透测试<br>学习者提供学习和实践的机会。 |
