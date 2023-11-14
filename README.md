# 更新于 2023-11-14 08:45:39

## 近15天release更新记录
| 更新时间 | 项目名称 | 版本 | 更新内容 |
| :---- | :---- | :---- | :---- |
|2023-11-14 00:39:31|[wekan](https://github.com/wekan/wekan)|v7.18|This release adds the following new f<br>eatures:    - .    Thanks to gustaveng<br>strom.    and adds the following updat<br>es:    - .    Thanks to xet7.    and f<br>ixes the following bugs:    - .    Tha<br>nks to mueller-ma.    Thanks to above <br>GitHub users for their contributions a<br>nd translators for their translations.|
|2023-11-13 23:08:30|[rundeck](https://github.com/rundeck/rundeck)|v4.17.3|Release v4.17.3|
|2023-11-13 16:04:41|[AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)|v0.107.<br>41|Bugs are as certain as the change of <br>the seasons :calendar:.  However, in t<br>his release we have not only fixed qui<br>te a few of them, but also added some <br>features that will make it easier to c<br>onfigure AdGuard Home and protect it f<br>rom DDoS attacks!        ##  Acknowled<br>gements    A special thanks to our ope<br>n-source contributor, @TimTheBig, as w<br>ell as to everyone who filed and inspe<br>cted issues, added translations, and h<br>elped us test this release!        ## <br> Full changelog    See also the [v0.10<br>7.41 GitHub milestone][ms-v0.107.41]. <br>      ###  Security     *  Go version <br>has been updated to prevent the possib<br>ility of exploiting the CVE-2023-45283<br> and CVE-2023-45284 Go vulnerabilities<br> fixed in [Go 1.20.11][go-1.20.11].   <br>    ###  Added     *  Ability to speci<br>fy subnet lengths for IPv4 and IPv6 ad<br>dresses, used for rate limiting reques<br>ts, in the configuration file (#6368).<br>     *  Ability to specify multiple do<br>main specific upstreams per line, e.g.<br>  [/domain1/../domain2/]upstream1 upst<br>ream2 .. upstreamN (#4977).       ### <br> Changed     *  Increased the height o<br>f the ready-to-use filter lists dialog<br> (#6358).     *  Improved logging of a<br>uthentication failures (#6357).      #<br>###  Configuration changes     *  New <br>properties dns.ratelimit_subnet_len_ip<br>v4 and dns.ratelimit_subnet_len_ipv6 h<br>ave been added to the configuration fi<br>le (#6368).       ###  Fixed     *  Sc<br>hedule timezone not being sent (#6401)<br>.     *  Average request processing ti<br>me calculation (#6220).     *  Redunda<br>nt truncation of long client names in <br>the Top Clients table (#6338).     *  <br>Scrolling column headers in the tables<br> (#6337).     *  $important,dnsrewrite<br> rules not overriding allowlist rules <br>(#6204).     *  Dark mode DNS rewrite <br>background (#6329).     *  Issues with<br> QUIC and HTTP/3 upstreams on Linux (#<br>6335).    [go-1.20.11]:   https://grou<br>ps.google.com/g/golang-announce/c/4tU8<br>LZfBFkY/m/d-jSKR_jBwAJ  [ms-v0.107.41]<br>: https://github.com/AdguardTeam/AdGua<br>rdHome/milestone/76?closed=1  |
|2023-11-13 14:11:23|[mitmproxy](https://github.com/mitmproxy/mitmproxy)|10.1.4|Changes: See .  You can find the late<br>st release packages at https://mitmpro<br>xy.org/downloads/. |
|2023-11-13 12:29:10|[codeql-cli-binari<br>es](https://github.com/github/codeql-cli-binaries)|v2.15.2|### Breaking changes    - C++ extract<br>ion has been updated to output more ac<br>curate C++ value categories. Note you <br>may need to recompile query packs that<br> were compiled with an older CodeQL (s<br>ee full changelog below for details). <br>   ### New features    - codeql databa<br>se analyze and codeql database interpr<br>et-results can now    output human-rea<br>dable analysis summaries in a new form<br>at. To enable this new format, pass th<br>e --analysis-summary-v2 flag. See the <br>full changelog for compatibility infor<br>mation if you intend to use this with <br>GitHub Enterprise Server.  - CodeQL no<br>w supports    distinguishing file cove<br>rage information between related langu<br>ages C and C++, Java and Kotlin,    an<br>d JavaScript and TypeScript.  See the <br>full changelog for usage and compatibi<br>lity information.  - All CLI commands <br>now support --common-caches, which con<br>trols the location of the    cached da<br>ta that is persisted between several r<br>uns of the CLI, such as downloaded QL <br>packs    and compiled query plans.    <br>### Improvements    - Model packs that<br> are used in an analysis will now be i<br>ncluded in an output SARIF results fil<br>e. All model packs now include the isC<br>odeQLModelPack: true property in their<br> tool component property bag.    For m<br>ore information about the changes incl<br>uded in this release, see the .    You<br> can download _either_ the codeql-PLAT<br>FORM.zip for your platform, _or_ the g<br>eneric codeql.zip which contains binar<br>ies for all supported platforms. Pleas<br>e ignore the additional "source code" <br>downloads below the .zip artifacts.   <br> This release is compatible with the C<br>odeQL language packs from .  |
|2023-11-13 11:40:22|[broot](https://github.com/Canop/broot)|v1.28.1|- fix a regression in handling of roo<br>ted gitignore patterns - Fix #795  |
|2023-11-13 09:47:51|[jumpserver](https://github.com/jumpserver/jumpserver)|v3.8.2|⚠️ 注意    3.0 架构上和 2.0 变化较<br>大，建议全新安装一套环境来体验。如需升<br>级，请务必升级前进行备份，并查阅文档： <br>    # 一、安装和升级    ## 1.1 在线方<br>式 ✈️    仅需两步快速安装 JumpServer<br>：    1. 准备一台 4核8G （最低）且可以<br>访问互联网的 64 位 Linux 主机；  2. 以 <br>root 用户执行如下命令一键安装 JumpServ<br>er。    国内用户   sh  curl -sSL https<br>://resource.fit2cloud.com/jumpserver/j<br>umpserver/releases/latest/download/qui<br>ck_start.sh | bash      海外用户   sh <br> curl -sSL https://github.com/jumpserv<br>er/jumpserver/releases/latest/download<br>/quick_start.sh | bash      ## 1.2 离<br>线方式 🚢         详细安装和升级文档请<br>参考：        # 二、更新日志    ## 2.1 <br>功能优化 🚀     - perf: 优化发布机选择<br>策略    ## 2.2 问题修复 🐛    - fix: 修<br>复 DB2 资产平台已经存在导致迁移失败的问<br>题  - fix: 修复资产节点名称（Apps）重复<br>导致升级失败的问题  - fix: 修复 Elastic<br>search（6 版本）查询不到命令记录的问题<br>  - fix: 修复 MySQL 未写默认数据库导致<br> Web GUI 方式连接失败的问题（Chen）  -<br> fix: 修复用户使用 SSH 密钥登录失败的<br>问题（KoKo）  - fix: 修复云账号页面更新<br>报错的问题【企业版】  - fix: 修复创建工<br>单搜索资产不显示的问题【企业版】  - fix<br>: 修复创建工单账号字段搜索后点击下拉选<br>项时重复添加的问题【企业版】  |
|2023-11-13 07:48:30|[nemo_go](https://github.com/hanc00l/nemo_go)|v2.10.3|### Update    - 增加漏洞的批量删除功<br>能  - 更新iconhash代码  - 一些测试用例<br>信息  - 更新thirdparty第三方组件  - Go <br>版本更新到1.21    ### Fix    - iplocati<br>on in xscan    ### Thirdparty版本    -<br> Httpx：1.3.6  - Subfinder：2.6.3  - N<br>uclei：3.0.3  - Observe_ward：2023.10.<br>13  - Goby: 2.7.9|
|2023-11-13 07:26:10|[httpx](https://github.com/projectdiscovery/httpx)|v1.3.7|    ## What's Changed    ### 🐞 Bug F<br>ixes  * Fixed new line break issue wit<br>h -title option by @dogancanbakir in h<br>ttps://github.com/projectdiscovery/htt<br>px/pull/1439  * Fixed build error on t<br>ermux/android by @RamanaReddy0M in htt<br>ps://github.com/projectdiscovery/httpx<br>/pull/1424  * Fixed path issue on wind<br>ows by @dogancanbakir in https://githu<br>b.com/projectdiscovery/httpx/pull/1431<br>  * Fixed chrome zombie process using <br>leakless by @dogancanbakir in https://<br>github.com/projectdiscovery/httpx/pull<br>/1426  * Fixed panic crash with -asn o<br>ption    ### Other Changes  * Added SN<br>I to jsonl output by @RamanaReddy0M in<br> https://github.com/projectdiscovery/h<br>ttpx/pull/1423  * Added optional flag <br>(-eph) to skip private host / ips for <br>probing by @CodyCline in https://githu<br>b.com/projectdiscovery/httpx/pull/1408<br>  * Added hyperlink to host result by <br>@pdelteil in https://github.com/projec<br>tdiscovery/httpx/pull/1430  * Increase<br>d timeout for a page lifecycle event b<br>y @dogancanbakir in https://github.com<br>/projectdiscovery/httpx/pull/1440    #<br># New Contributors  * @CodyCline made <br>their first contribution in https://gi<br>thub.com/projectdiscovery/httpx/pull/1<br>408  * @pdelteil made their first cont<br>ribution in https://github.com/project<br>discovery/httpx/pull/1430    **Full Ch<br>angelog**: https://github.com/projectd<br>iscovery/httpx/compare/v1.3.6...v1.3.7|
|2023-11-13 03:34:35|[v2rayA](https://github.com/v2rayA/v2rayA)|v2.2.4.<br>3|Fix Docker images|
|2023-11-12 18:25:18|[MoreFind](https://github.com/mstxq17/MoreFind)|v1.5.5|## Changelog * d01e122 perf: parse xl<br>sx/xls  enhanchment  |
|2023-11-12 17:54:46|[locust](https://github.com/locustio/locust)|2.18.3|## What's Changed  * Modern UI: Add s<br>orting to columns on statistics page a<br>nd downloaded report by @andrewbaldwin<br>44 in https://github.com/locustio/locu<br>st/pull/2453  * Add Modern UI HTML Rep<br>ort to --html Option by @andrewbaldwin<br>44 in https://github.com/locustio/locu<br>st/pull/2459  * List Andrew as maintai<br>ner of the Modern web UI by @cyberw in<br> https://github.com/locustio/locust/pu<br>ll/2460      **Full Changelog**: https<br>://github.com/locustio/locust/compare/<br>2.18.2...2.18.3|
|2023-11-12 13:10:54|[fzf](https://github.com/junegunn/fzf)|0.44.0|- (Experimental) Sixel image support <br>in preview window (not available on Wi<br>ndows)      -  is added to demonstrate<br> how to display an image using Kitty i<br>mage protocol or Sixel. You can use it<br> like so:        sh        fzf --previ<br>ew='fzf-preview.sh {}'          - (Exp<br>erimental) iTerm2 inline image protoco<br>l support in preview window (not avail<br>able on Windows)    sh    # Using http<br>s://iterm2.com/utilities/imgcat    fzf<br> --preview 'imgcat -W $FZF_PREVIEW_COL<br>UMNS -H $FZF_PREVIEW_LINES {}'        <br>    - HTTP server can be configured to<br> accept remote connections    sh    # <br>FZF_API_KEY is required for a non-loca<br>lhost listen address    export FZF_API<br>_KEY="$(head -c 32 /dev/urandom | base<br>64)"    fzf --listen 0.0.0.0:6266     <br>     - To allow remote process executi<br>on, use --listen-unsafe instead       <br> (execute*, reload*, become, preview, <br>change-preview, transform-*)        sh<br>        fzf --listen-unsafe 0.0.0.0:62<br>66          - Bug fixes    |
|2023-11-12 04:29:42|[PEASS-ng](https://github.com/carlospolop/PEASS-ng)|2023111<br>2-0a42c5<br>50||
|2023-11-11 19:20:44|[dnsx](https://github.com/projectdiscovery/dnsx)|v1.1.6|    ## What's Changed  ### Other Chan<br>ges  * Added additional public resolve<br>r by @Devang-Solanki in https://github<br>.com/projectdiscovery/dnsx/pull/480  *<br> Fixed panic crash    ## New Contribut<br>ors  * @Devang-Solanki made their firs<br>t contribution in https://github.com/p<br>rojectdiscovery/dnsx/pull/480    **Ful<br>l Changelog**: https://github.com/proj<br>ectdiscovery/dnsx/compare/v1.1.5...v1.<br>1.6|
|2023-11-11 15:14:40|[autoDecoder](https://github.com/f0ng/autoDecoder)|0.34|## 2023.11.11 更新0.34  1. 增加header<br>头关键字判断|
|2023-11-10 19:29:05|[pulumi](https://github.com/pulumi/pulumi)|v3.93.0|## 3.93.0 (2023-11-09)      ### Featu<br>res    -       ### Bug Fixes    -     <br>-     - |
|2023-11-10 18:30:08|[neuvector](https://github.com/neuvector/neuvector)|v5.2.3|New Features:  Support usage based bi<br>lling in GCP and Azure     Bug fixes: <br> NVSHAS-8426: Not to revert admission <br>control webhook if the cloud service m<br>odify it at the same time  NVSHAS-8411<br>: possible deadlock when running on si<br>ngle node  Various bug fixes on vulner<br>ability reporting    Scanner:  Support<br> container host scan in standalone mod<br>e  Support vulnerability NVD API 2.0|
|2023-11-10 16:21:49|[faker](https://github.com/joke2k/faker)|v20.0.0|See .|
|2023-11-10 14:20:15|[CotEditor](https://github.com/coteditor/CotEditor)|4.6.5|system requirements: __macOS 13__ and<br> later      ### Improvements    - Opti<br>mize the performance of the incompatib<br>le character scan.  - [trivial] Add a <br>tooltip to font fields in the Appearan<br>ce settings pane.  - [dev] Migrate the<br> custom sort pattern view to SwiftUI. <br>     ### Fixes    - Fix an issue that <br>changes in the multiple replacement de<br>finition editor did not save.  - Fix a<br>n issue that the application could han<br>g when opening a large document withou<br>t line breaks.  - Fix an issue that a <br>label was not localized.  |
|2023-11-10 13:32:30|[celery](https://github.com/celery/celery)|v5.3.5|Main theme of this release is adding <br>Python 3.12 compatibility support to a<br>ll through the projects dependencies. <br>Also lots of bugs were squashed. Depen<br>dencies upgraded and docs improved.   <br> ## What's Changed  * Update test.txt <br>versions by @auvipy in https://github.<br>com/celery/celery/pull/8481  * fix os.<br>getcwd() FileNotFoundError by @mortime<br>r2015 in https://github.com/celery/cel<br>ery/pull/8448  * Fix typo in CONTRIBUT<br>ING.rst by @monteiro-renato in https:/<br>/github.com/celery/celery/pull/8494  *<br> typo(doc): configuration.rst by @shif<br>enhutu in https://github.com/celery/ce<br>lery/pull/8484  * assert before raise <br>by @monteiro-renato in https://github.<br>com/celery/celery/pull/8495  * Update <br>GHA checkout version by @auvipy in htt<br>ps://github.com/celery/celery/pull/849<br>6  * Fixed replaced_task_nesting by @N<br>usnus in https://github.com/celery/cel<br>ery/pull/8500  * Fix code indentation <br>for route_task() example by @stefmolin<br> in https://github.com/celery/celery/p<br>ull/8502  * support redis 5.x by @dulm<br>andakh in https://github.com/celery/ce<br>lery/pull/8504  * Fix typos in test_ca<br>nvas.py by @monteiro-renato in https:/<br>/github.com/celery/celery/pull/8498  *<br> Marked flaky tests by @Nusnus in http<br>s://github.com/celery/celery/pull/8508<br>  * Fix typos in calling.rst by @visit<br>orckw in https://github.com/celery/cel<br>ery/pull/8506  * Added support for rep<br>laced_task_nesting in chains by @Nusnu<br>s in https://github.com/celery/celery/<br>pull/8501  * Fix typos in canvas.rst b<br>y @visitorckw in https://github.com/ce<br>lery/celery/pull/8509  * Patch Version<br> Release Checklist by @Nusnus in https<br>://github.com/celery/celery/pull/8488 <br> * Added Python 3.11 support to Docker<br>file by @Nusnus in https://github.com/<br>celery/celery/pull/8511  * Dependabot <br>(Celery) by @Nusnus in https://github.<br>com/celery/celery/pull/8510  * Bump ac<br>tions/checkout from 3 to 4 by @dependa<br>bot in https://github.com/celery/celer<br>y/pull/8512  * [pre-commit.ci] pre-com<br>mit autoupdate by @pre-commit-ci in ht<br>tps://github.com/celery/celery/pull/85<br>15  * Update ETA example to include ti<br>mezone by @amantri in https://github.c<br>om/celery/celery/pull/8516  * Replaces<br> datetime.fromisoformat with the more <br>lenient dateutil parser by @stumpylog <br>in https://github.com/celery/celery/pu<br>ll/8507  * Fixed indentation in Docker<br>file for Python 3.11 by @Nusnus in htt<br>ps://github.com/celery/celery/pull/852<br>7  * Fix git bug in Dockerfile by @Nus<br>nus in https://github.com/celery/celer<br>y/pull/8528  * Tox lint upgrade from P<br>ython 3.9 to Python 3.11 by @Nusnus in<br> https://github.com/celery/celery/pull<br>/8526  * Document gevent concurrency b<br>y @cunla in https://github.com/celery/<br>celery/pull/8520  * Update test.txt by<br> @auvipy in https://github.com/celery/<br>celery/pull/8530  * Celery Docker Upgr<br>ades by @Nusnus in https://github.com/<br>celery/celery/pull/8531  * pyupgrade u<br>pgrade v3.11.0 -> v3.13.0 by @Nusnus i<br>n https://github.com/celery/celery/pul<br>l/8535  * Update msgpack.txt by @auvip<br>y in https://github.com/celery/celery/<br>pull/8548  * Update auth.txt by @auvip<br>y in https://github.com/celery/celery/<br>pull/8547  * Update msgpack.txt to fix<br> build issues by @auvipy in https://gi<br>thub.com/celery/celery/pull/8552  * Ba<br>sic ElasticSearch / ElasticClient 8.x <br>Support by @q2justin in https://github<br>.com/celery/celery/pull/8519  * Fix ea<br>ger tasks does not populate name field<br> by @KOliver94 in https://github.com/c<br>elery/celery/pull/8486  * [pre-commit.<br>ci] pre-commit autoupdate by @pre-comm<br>it-ci in https://github.com/celery/cel<br>ery/pull/8559  * Fix typo in celery.ap<br>p.control by @Spaceface16518 in https:<br>//github.com/celery/celery/pull/8563  <br>* Update solar.txt ephem by @auvipy in<br> https://github.com/celery/celery/pull<br>/8566  * Update test.txt pytest-timeou<br>t by @auvipy in https://github.com/cel<br>ery/celery/pull/8565  * Correct some m<br>ypy errors by @rbtcollins in https://g<br>ithub.com/celery/celery/pull/8570  * [<br>pre-commit.ci] pre-commit autoupdate b<br>y @pre-commit-ci in https://github.com<br>/celery/celery/pull/8572  * Update ela<br>sticsearch.txt by @auvipy in https://g<br>ithub.com/celery/celery/pull/8573  * U<br>pdate test.txt deps by @auvipy in http<br>s://github.com/celery/celery/pull/8574<br>  * [pre-commit.ci] pre-commit autoupd<br>ate by @pre-commit-ci in https://githu<br>b.com/celery/celery/pull/8587  * Updat<br>e test.txt by @auvipy in https://githu<br>b.com/celery/celery/pull/8590  * Impro<br>ved the "Next steps" documentation (#8<br>561). by @frolenkov-nikita in https://<br>github.com/celery/celery/pull/8600  * <br>Disabled couchbase tests due to broken<br> package breaking main by @Nusnus in h<br>ttps://github.com/celery/celery/pull/8<br>602  * Update elasticsearch deps by @a<br>uvipy in https://github.com/celery/cel<br>ery/pull/8605  * Update cryptography==<br>41.0.5 by @auvipy in https://github.co<br>m/celery/celery/pull/8604  * Update py<br>test==7.4.3 by @auvipy in https://gith<br>ub.com/celery/celery/pull/8606  * test<br> initial support of python 3.12.x by @<br>auvipy in https://github.com/celery/ce<br>lery/pull/8549  * updated new versions<br> to fix CI by @auvipy in https://githu<br>b.com/celery/celery/pull/8607  * Updat<br>e zstd.txt by @auvipy in https://githu<br>b.com/celery/celery/pull/8609  * Fixed<br> CI Support with Python 3.12 by @Nusnu<br>s in https://github.com/celery/celery/<br>pull/8611  * updated CI, docs and clas<br>sifier for next release by @auvipy in <br>https://github.com/celery/celery/pull/<br>8613  * updated dockerfile to add pyth<br>on 3.12 by @auvipy in https://github.c<br>om/celery/celery/pull/8614  * lint,myp<br>y,docker-unit-tests -> Python 3.12 by <br>@Nusnus in https://github.com/celery/c<br>elery/pull/8617  * Correct type of req<br>uest in task_revoked documentation by <br>@RJPercival in https://github.com/cele<br>ry/celery/pull/8616  * update docs doc<br>ker image by @auvipy in https://github<br>.com/celery/celery/pull/8618  * Fixed <br>RecursionError caused by giving config<br>_from_object nested mod… by @frolenko<br>v-nikita in https://github.com/celery/<br>celery/pull/8619  * Fix: serialization<br> error when gossip working by @kitsuyu<br>i in https://github.com/celery/celery/<br>pull/6566  * [documentation] broker_co<br>nnection_max_retries of 0 does not mea<br>n "retry forever" by @jakila in https:<br>//github.com/celery/celery/pull/8626  <br>* added 2  debian package for better s<br>tability in Docker by @auvipy in https<br>://github.com/celery/celery/pull/8629 <br> * Added changelog for v5.3.5 by @auvi<br>py in https://github.com/celery/celery<br>/pull/8623    ## New Contributors  * @<br>mortimer2015 made their first contribu<br>tion in https://github.com/celery/cele<br>ry/pull/8448  * @monteiro-renato made <br>their first contribution in https://gi<br>thub.com/celery/celery/pull/8494  * @s<br>hifenhutu made their first contributio<br>n in https://github.com/celery/celery/<br>pull/8484  * @stefmolin made their fir<br>st contribution in https://github.com/<br>celery/celery/pull/8502  * @visitorckw<br> made their first contribution in http<br>s://github.com/celery/celery/pull/8506<br>  * @dependabot made their first contr<br>ibution in https://github.com/celery/c<br>elery/pull/8512  * @amantri made their<br> first contribution in https://github.<br>com/celery/celery/pull/8516  * @cunla <br>made their first contribution in https<br>://github.com/celery/celery/pull/8520 <br> * @q2justin made their first contribu<br>tion in https://github.com/celery/cele<br>ry/pull/8519  * @Spaceface16518 made t<br>heir first contribution in https://git<br>hub.com/celery/celery/pull/8563  * @rb<br>tcollins made their first contribution<br> in https://github.com/celery/celery/p<br>ull/8570  * @frolenkov-nikita made the<br>ir first contribution in https://githu<br>b.com/celery/celery/pull/8600  * @RJPe<br>rcival made their first contribution i<br>n https://github.com/celery/celery/pul<br>l/8616  * @kitsuyui made their first c<br>ontribution in https://github.com/cele<br>ry/celery/pull/6566  * @jakila made th<br>eir first contribution in https://gith<br>ub.com/celery/celery/pull/8626    **Fu<br>ll Changelog**: https://github.com/cel<br>ery/celery/compare/v5.3.4...v5.3.5|
|2023-11-10 10:43:50|[nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)|v9.6.9|🔥 Release Highlights 🔥    - network<br>/cves/2023/CVE-2023-46604.yaml by @Ice<br>3man,@Mzack9999,@pdresearch 🔥  - java<br>script/cves/2023/CVE-2023-34039.yaml b<br>y @tarunKoyalwar 🔥  - code/cves/2023/<br>CVE-2023-4911.yaml by @nybble04 🔥  - <br>http/cves/2023/CVE-2023-43795.yaml by <br>@DhiyaneshDK 🔥  - http/cves/2022/CVE-<br>2022-35653.yaml by @iamnoooob,@pdresea<br>rch 🔥  - http/cves/2023/CVE-2023-2251<br>8.yaml by @iamnoooob,@rootxharsh,@pdre<br>search 🔥  - http/cves/2023/CVE-2023-2<br>0198.yaml by @iamnoooob,@rootxharsh,@p<br>dresearch 🔥  - http/cves/2020/CVE-202<br>0-24701.yaml by @DhiyaneshDk 🔥  - htt<br>p/cves/2023/CVE-2023-1719.yaml by @Dhi<br>yaneshDk 🔥    ## What's Changed  ####<br> New Templates Added: 73 | CVEs Added:<br> 13 | First-time contributions: 7    -<br> network/cves/2023/CVE-2023-46604.yaml<br> by @Ice3man,@Mzack9999,@pdresearch 🔥<br>  - javascript/cves/2023/CVE-2023-3403<br>9.yaml by @tarunKoyalwar 🔥  - code/cv<br>es/2023/CVE-2023-4911.yaml by @nybble0<br>4 🔥  - http/cves/2023/CVE-2023-43795.<br>yaml by @DhiyaneshDK 🔥  - http/cves/2<br>023/CVE-2023-40068.yaml by @E1A  - htt<br>p/cves/2022/CVE-2022-35653.yaml by @ia<br>mnoooob,@pdresearch 🔥  - http/cves/20<br>23/CVE-2023-34020.yaml by @LeDoubleTak<br>e  - http/cves/2023/CVE-2023-33629.yam<br>l by @DhiyaneshDK  - http/cves/2023/CV<br>E-2023-22518.yaml by @iamnoooob,@rootx<br>harsh,@pdresearch 🔥  - http/cves/2023<br>/CVE-2023-20198.yaml by @iamnoooob,@ro<br>otxharsh,@pdresearch 🔥  - http/cves/2<br>020/CVE-2020-24701.yaml by @DhiyaneshD<br>k 🔥  - http/cves/2023/CVE-2023-1719.y<br>aml by @DhiyaneshDk 🔥  - http/cves/20<br>23/CVE-2023-4169.yaml by @DhiyaneshDK <br> - http/cves/2023/CVE-2023-4415.yaml b<br>y @DhiyaneshDK  - http/default-logins/<br>dell/dell-dpi-default-login.yaml by @m<br>egamansec  - http/default-logins/goip-<br>default-login.yaml by @drfabiocastro  <br>- http/exposed-panels/appsuite-panel.y<br>aml by @DhiyaneshDK  - http/exposed-pa<br>nels/cisco/cisco-ios-xe-panel.yaml by <br>@bhutch  - http/exposed-panels/fusiona<br>uth-admin-panel.yaml by @ritikchaddha <br> - http/exposed-panels/homer-panel.yam<br>l by @rxerium  - http/exposed-panels/k<br>iteworks-pcn-panel.yaml by @righettod <br> - http/exposed-panels/librephotos-pan<br>el.yaml by @ritikchaddha  - http/expos<br>ed-panels/librespeed-panel.yaml by @ri<br>tikchaddha  - http/exposed-panels/offi<br>ce-webapps-panel.yaml by @DhiyaneshDK <br> - http/exposed-panels/overseerr-panel<br>.yaml by @rxerium  - http/exposed-pane<br>ls/plausible-panel.yaml by @rxerium  -<br> http/exposed-panels/rdweb-panel.yaml <br>by @rxerium,@sorrowx3  - http/exposed-<br>panels/servicenow-panel.yaml by @righe<br>ttod  - http/exposed-panels/truenas-sc<br>ale-panel.yaml by @rxerium  - http/exp<br>osed-panels/unauth/tautulli-unauth.yam<br>l by @ritikchaddha  - http/honeypot/ci<br>trix-honeypot-detect.yaml by @UnaPibaG<br>eek  - http/honeypot/dionaea-http-hone<br>ypot-detect.yaml by @UnaPibaGeek  - ht<br>tp/honeypot/elasticpot-honeypot-detect<br>.yaml by @UnaPibaGeek  - http/honeypot<br>/snare-honeypot-detect.yaml by @UnaPib<br>aGeek  - http/misconfiguration/fusiona<br>uth-admin-setup.yaml by @ritikchaddha <br> - http/misconfiguration/installer/cub<br>e-105-install.yaml by @ritikchaddha  -<br> http/misconfiguration/installer/impri<br>vata-installer.yaml by @ritikchaddha  <br>- http/misconfiguration/installer/oran<br>gescrum-install.yaml by @ritikchaddha <br> - http/misconfiguration/installer/ruc<br>kus-smartzone-install.yaml by @ritikch<br>addha  - http/misconfiguration/install<br>er/ruckus-unleashed-install.yaml by @r<br>itikchaddha  - http/misconfiguration/i<br>nstaller/sugarcrm-install.yaml by @rit<br>ikchaddha  - http/misconfiguration/ins<br>taller/tautulli-install.yaml by @ritik<br>chaddha  - http/misconfiguration/insta<br>ller/webcalendar-install.yaml by @riti<br>kchaddha  - http/misconfiguration/inst<br>aller/webtrees-install.yaml by @ritikc<br>haddha  - http/misconfiguration/less-h<br>istory.yaml by @kazet  - http/misconfi<br>guration/mysql-history.yaml by @kazet <br> - http/misconfiguration/searchreplace<br>db2-exposure.yaml by @kazet  - http/mi<br>sconfiguration/untangle-admin-setup.ya<br>ml by @ritikchaddha  - http/technologi<br>es/dell/dell-dpi-panel.yaml by @megama<br>nsec  - http/technologies/wordpress/pl<br>ugins/hostinger.yaml by @ricardomaia  <br>- http/technologies/wordpress/plugins/<br>metform.yaml by @ricardomaia  - http/v<br>ulnerabilities/hikvision/hikvision-js-<br>files-upload.yaml by @Xc1Ym  - http/vu<br>lnerabilities/microsoft/office-webapps<br>-ssrf.yaml by @DhiyaneshDK  - http/vul<br>nerabilities/other/podcast-generator-s<br>srf.yaml by @ritikchaddha,@MrHarshvard<br>han  - javascript/default-logins/mssql<br>-default-logins.yaml by @Ice3man543,@t<br>arunKoyalwar  - javascript/default-log<br>ins/postgres-default-logins.yaml by @I<br>ce3man  - javascript/default-logins/re<br>dis-default-logins.yaml by @tarunKoyal<br>war  - javascript/default-logins/ssh-d<br>efault-logins.yaml by @tarunKoyalwar  <br>- javascript/detection/mssql-detect.ya<br>ml by @Ice3man543,@tarunKoyalwar  - ja<br>vascript/detection/ssh-auth-methods.ya<br>ml by @Ice3man543  - javascript/enumer<br>ation/ssh-password-auth.yaml by @princ<br>echaddha  - javascript/enumeration/ssh<br>-server-enumeration.yaml by @Ice3man54<br>3,@tarunKoyalwar  - network/honeypot/a<br>dbhoney-honeypot-cnxn-detect.yaml by @<br>UnaPibaGeek  - network/honeypot/adbhon<br>ey-honeypot-shell-detect.yaml by @UnaP<br>ibaGeek  - network/honeypot/conpot-sie<br>mens-honeypot-detect.yaml by @UnaPibaG<br>eek  - network/honeypot/cowrie-ssh-hon<br>eypot-detect.yaml by @UnaPibaGeek  - n<br>etwork/honeypot/dionaea-ftp-honeypot-d<br>etect.yaml by @UnaPibaGeek  - network/<br>honeypot/dionaea-mqtt-honeypot-detect.<br>yaml by @UnaPibaGeek  - network/honeyp<br>ot/dionaea-mysql-honeypot-detect.yaml <br>by @UnaPibaGeek  - network/honeypot/di<br>onaea-smb-honeypot-detect.yaml by @Una<br>PibaGeek  - network/honeypot/gaspot-ho<br>neypot-detect.yaml by @UnaPibaGeek  - <br>network/honeypot/mailoney-honeypot-det<br>ect.yaml by @UnaPibaGeek  - network/ho<br>neypot/redis-honeypot-detect.yaml by @<br>UnaPibaGeek    ## New Contributors  * <br>@k0z4c made their first contribution i<br>n https://github.com/projectdiscovery/<br>nuclei-templates/pull/8468  * @byt3bl3<br>3d3r made their first contribution in <br>https://github.com/projectdiscovery/nu<br>clei-templates/pull/8457  * @0xorOne m<br>ade their first contribution in https:<br>//github.com/projectdiscovery/nuclei-t<br>emplates/pull/8500  * @jzr made their <br>first contribution in https://github.c<br>om/projectdiscovery/nuclei-templates/p<br>ull/8546  * @Xc1Ym made their first co<br>ntribution in https://github.com/proje<br>ctdiscovery/nuclei-templates/pull/8548<br>  * @adilsoybali made their first cont<br>ribution in https://github.com/project<br>discovery/nuclei-templates/pull/8540  <br>* @rumble773 made their first contribu<br>tion in https://github.com/projectdisc<br>overy/nuclei-templates/pull/8572    **<br>Full Changelog**: https://github.com/p<br>rojectdiscovery/nuclei-templates/compa<br>re/v9.6.8...v9.6.9|
|2023-11-10 09:08:46|[mapcidr](https://github.com/projectdiscovery/mapcidr)|v1.1.15|    - asnmap dep update    **Full Cha<br>ngelog**: https://github.com/projectdi<br>scovery/mapcidr/compare/v1.1.14...v1.1<br>.15|
|2023-11-10 07:18:45|[yakit](https://github.com/yaklang/yakit)|v1.2.7-<br>sp4||
|2023-11-09 15:02:57|[grype](https://github.com/anchore/grype)|v0.73.1|### Bug Fixes  - CycloneDX based anal<br>ysis failing   @anchore-actions-token-<br>generator] - False negatives when scan<br>ning debian trixie/sid images from Doc<br>kerhub   @willmurphyscode]  ### Additi<br>onal Changes  - avoid allocations with<br> (*regexp.Regexp).MatchString  @Juneez<br>ee]  ****  |
|2023-11-09 14:56:49|[croc](https://github.com/schollz/croc)|v9.6.6|## Changelog  * 159f0f8 Merge pull re<br>quest #625 from gravetii/patch-1  * 6a<br>c67b6 Merge pull request #570 from PTh<br>orpe92/main  * 0af35d7 feat: add suppo<br>rt to respect .gitignore files  * f91c<br>7a9 Merge pull request #587 from fereb<br>ee/main  * cff8cdd Merge pull request <br>#589 from zx9597446/main  * 80aabea fi<br>x architecture detection for Apple Sil<br>icon    |
|2023-11-09 14:11:50|[syft](https://github.com/anchore/syft)|v0.96.0|### Added Features  - Check maven cen<br>tral as well for licenses in parents p<br>oms for nested jars  @coheigea] - stor<br>e image annotations inside the SBOM   <br>@noqcks] - Support parsing license inf<br>ormation in Maven projects via parent <br>poms ]  ### Bug Fixes  - SPDX file has<br> duplicate sha256 tag in versionInfo  <br>@coheigea] - Report virtual path consi<br>stently between file.Resolvers   @wago<br>odman] - Unable to identify CycloneDX <br>JSON documents without $schema propert<br>y   @kzantow]  ****  |
|2023-11-09 14:08:16|[asnmap](https://github.com/projectdiscovery/asnmap)|v1.0.6|    ## What's Changed  ### 🐞 Bugs Fi<br>xes  * Adding missing response json ta<br>gs by @Mzack9999 in https://github.com<br>/projectdiscovery/asnmap/pull/213     <br> **Full Changelog**: https://github.co<br>m/projectdiscovery/asnmap/compare/v1.0<br>.5...v1.0.6|
|2023-11-09 10:26:05|[PostgresApp](https://github.com/PostgresApp/PostgresApp)|v2.6.8|This release contains the latest bugf<br>ixes for all supported versions of Pos<br>tgreSQL.    * PostgreSQL 16.1 with Pos<br>tGIS 3.4.0  * PostgreSQL 15.5 with Pos<br>tGIS 3.3.4  * PostgreSQL 14.10 with Po<br>stGIS 3.2.5  * PostgreSQL 13.13 with P<br>ostGIS 3.1.9  * PostgreSQL 12.17 with <br>PostGIS 3.0.9  * PostgreSQL 11.22 with<br> PostGIS 2.5.9    Notable changes sinc<br>e Postgres.app 2.6.7:  * PostGIS: supp<br>ort for writeable MVT in OGR  * PostGI<br>S: support for netCDF in GDAL / OGR (#<br>731) with PostgreSQL 16  * New version<br>s of extensions pgrouting and pgvector<br>. Run  to update  * PostgreSQL got sev<br>eral fixes affecting index creation an<br>d maintenance. Please check the  wheth<br>er or not your databases may be affect<br>ed and reindexing would be advisable. <br> * Fixed an issue where Postgres.app d<br>idn't auto-start when not in /Applicat<br>ions  * Fixed an issue where Postgres.<br>app didn't launch on macOS 10.13 when <br>not in /Applications    You can find a<br>n overview of the fixes in PostgreSQL <br>in the  and all details in the .    **<br>This will likely be the final release <br>of PostgreSQL 11.** If you still have <br>databases running on PostgreSQL 11, yo<br>u should consider upgrading your datab<br>ase after installing this update.|
|2023-11-09 10:22:58|[stratus-red-team](https://github.com/DataDog/stratus-red-team)|v2.10.0|## Changelog    * d151fe9 New attack <br>technique: Persistence AWS Lambda Laye<br>r Extension (#427) by @adanalvarez   |
|2023-11-09 02:37:19|[feroxbuster](https://github.com/epi052/feroxbuster)|v2.10.1|## What's Changed  * fixed scan menu <br>range issue by @epi052 in https://gith<br>ub.com/epi052/feroxbuster/pull/936  * <br>enable reading extensions from file by<br> @andreademurtas in https://github.com<br>/epi052/feroxbuster/pull/976  * fixed <br>collect backups filtering by @epi052 i<br>n https://github.com/epi052/feroxbuste<br>r/pull/1016  * added http/2 support by<br> @epi052 in https://github.com/epi052/<br>feroxbuster/pull/1020  * allowed --jso<br>n in conjunction with --silent by @epi<br>052 in https://github.com/epi052/ferox<br>buster/pull/1022    ## New Contributor<br>s  * @andreademurtas made their first <br>contribution in https://github.com/epi<br>052/feroxbuster/pull/976    **Full Cha<br>ngelog**: https://github.com/epi052/fe<br>roxbuster/compare/v2.10.0...v2.10.1|
|2023-11-09 00:09:18|[goreleaser](https://github.com/goreleaser/goreleaser)|v1.22.1|## Changelog ### Bug fixes * e33d0536<br>129abeee90f46fbde5950403ba37cee1: fix:<br> --single-target when no match (@caarl<br>os0) * c0b2be344fca8c66fda35391ca76d9c<br>3ca9753c8: fix: handle configs with no<br> explicit targets on --single-target (<br>@caarlos0) ### Build process updates *<br> 4f17fba173ec6d8feb93b15607fc692dd2b64<br>533: build: fix setup-task rate limit <br>(@caarlos0) * be9ad4d47dd09c218c8fd32b<br>321a99ff7eb5956d: build: update workfl<br>ow (@caarlos0)  **Full Changelog**: ht<br>tps://github.com/goreleaser/goreleaser<br>/compare/v1.22.0...v1.22.1  ## Helping<br> out  This release is only possible th<br>anks to **all** the support of some **<br>awesome people**!  Want to be one of t<br>hem? You can , get a  or .  ## Where t<br>o go next?  * Find examples and commen<br>ted usage of all options in our . * Re<br>ach out on  and !    |
|2023-11-08 17:22:30|[audacity](https://github.com/audacity/audacity)|Audacit<br>y-3.4.1| This is a hotfix release. It fixes t<br>he following bugs:     * #5467 Fix 24-<br>bit recording.   * #5488 Fix a crash w<br>ith .aup importing.   * #5471 #5483 Fi<br>x crossfading of clips and tracks.   *<br> #5473 Exporting multiple files honors<br> sample rate settings again.   * #5480<br> #5417 Fix crashes related to external<br> program exports.   * #5479 #5476 Fix <br>BSD and ARM builds.   * #5498 Ctrl+J i<br>s now a standard shortcut for joining <br>clips.   * #5389 Stereo tracks no long<br>er randomly split into mono.   * #5007<br> When exporting a file, the file exten<br>sion is now always added (except for c<br>ustom FFmpeg and external program expo<br>rts).   * #5516 Fix a crash when expor<br>ting Opus with older CPUs that don't s<br>upport AVX.|
|2023-11-08 13:43:08|[pyscript](https://github.com/pyscript/pyscript)|2023.11<br>.1|A whole new world. Thank you to every<br>one who has contributed to this from-t<br>he-ground-up re-build of PyScript.    <br>      ## New Contributors  * @Mr-Sungl<br>asses made their first contribution in<br> https://github.com/pyscript/pyscript/<br>pull/1279  * @WebReflection made their<br> first contribution in https://github.<br>com/pyscript/pyscript/pull/1284  * @zi<br>pperer made their first contribution i<br>n https://github.com/pyscript/pyscript<br>/pull/1307  * @aneesh98 made their fir<br>st contribution in https://github.com/<br>pyscript/pyscript/pull/1332  * @chench<br>en100 made their first contribution in<br> https://github.com/pyscript/pyscript/<br>pull/1292  * @cnelir98 made their firs<br>t contribution in https://github.com/p<br>yscript/pyscript/pull/1375  * @sfermig<br>ier made their first contribution in h<br>ttps://github.com/pyscript/pyscript/pu<br>ll/1386  * @eltociear made their first<br> contribution in https://github.com/py<br>script/pyscript/pull/1399  * @MrValdez<br> made their first contribution in http<br>s://github.com/pyscript/pyscript/pull/<br>1410  * @CameronCairns made their firs<br>t contribution in https://github.com/p<br>yscript/pyscript/pull/1409  * @Stefano<br>Hiway made their first contribution in<br> https://github.com/pyscript/pyscript/<br>pull/1473  * @bugzpodder made their fi<br>rst contribution in https://github.com<br>/pyscript/pyscript/pull/1603  * @shubh<br>algupta made their first contribution <br>in https://github.com/pyscript/pyscrip<br>t/pull/1797    **Full Changelog**: htt<br>ps://github.com/pyscript/pyscript/comp<br>are/2023.03.1...2023.11.1|
|2023-11-08 09:31:17|[ghauri](https://github.com/r0oth3x49/ghauri)|1.2.8|### Fixes:   - fixed issue #110    - <br>fixed issue with payload encoding when<br> injection is found in cookies.|
|2023-11-07 16:10:39|[OneScan](https://github.com/vaycore/OneScan)|v1.4.0|1.4.0 版本发布，版本更新内容如下    #<br>## 新增    - 新增 Payload Processing <br>开关，用于控制 Payload Processing 功能<br>的启用与禁用  - 数据看板的 From 字段新<br>增 Process 来源显示（表示 Payload Proce<br>ssing 处理后的数据包）    ### 优化    <br>- 增强 Payload Processing 功能，可添加<br>多条规则，每条规则处理完成后会单独发起<br>请求  - 优化 Databoard 数据看板的过滤功<br>能，将过滤规则存储到配置文件中  - 删除 <br>Databoard 数据看板中的 Merge Payload P<br>rocessing 开关  |
|2023-11-07 15:45:45|[soapui](https://github.com/SmartBear/soapui)|v5.7.2|SoapUI release 5.7.2 (GA 11/07/2023) <br>                      |
|2023-11-06 20:49:57|[CSS-Exchange](https://github.com/microsoft/CSS-Exchange)|v23.11.<br>06.2048|Script | Version | SHA256 Hash  -----<br>--|---------|------------   | 23.01.13<br>.1832 | E3D524998D30005B8C3143C154AB94<br>9E16C36EADE1014D851ECC9F382DB01081   |<br> 23.01.13.1832 | 4AACB71EA2ACC68DF8DE1<br>0E1F48F0450647D19998DB77D6BD21B5F487A4<br>B5ADE   | 23.01.06.2348 | 4F9492260BA6<br>1F8B42269A78AB61C5946324D9E8F25BE76446<br>E0E1335C4AA468   | 23.01.13.1832 | 971<br>BA4C6051A29097676EE5FB4F365B09C7DC54EE<br>C3F28ED1D791F7A5FED4137   | 23.02.01.1<br>855 | 9E637BB7AF4B0D80590B72794ADCE411<br>EBD4063216A08BD158EE34DC8261BBE3   | 2<br>3.11.06.0849 | FEB3F3B80148D4C6C95674F<br>94458871589317E236356BE76860BAB4031772<br>E88   | 23.10.10.1649 | 61BFBEA6D7FC86<br>003F697F969413D12EE1E4DFECA293A578C80D<br>4BE6F611C835   | 23.07.26.1007 | 3B4D4<br>BCB7486976054676032CD47722E7680C3E66DB<br>B19F1FA81D49D113245B0   | 23.02.16.135<br>7 | 8322E64B5E3AF8CFA10609884185CDAB1D<br>69206A929A54F509B2BD6176BEC29E   | 23.<br>10.26.1737 | F6B670D7B84BAB3DB0F436268<br>7BC2BF5FA93664B27E684180E3276E517BE78C<br>7   | 23.10.26.1737 | 5A2DBAE9F4355F95<br>4A9D53D73B5B809F5A16B608654458FEEF4BB1<br>D4879B68E3   | 23.10.26.1737 | B138B58<br>2E36262922FDBA2119F938A3EB5F9EB7A04093<br>6704A30CC4885DFF7EE   | 23.10.26.1737 <br>| 16BA543752D150607C58B88328AB24B36502<br>B43FE52BD9EEE6126D171DFEF7D1   | 23.06<br>.13.1537 | 9646B626107F3EB7030944F28E2<br>89C0E6659F301DB8E4CE1C2FC2BB6997D5DD4 <br>  | 23.01.13.1832 | AA8DB0B9CBDA1F4FD0<br>33065A35FDAE3CB82391D1A7F669A4878E5239<br>01F5FBE8   | 23.10.20.2025 | 78BCC2D70<br>670F674100F57FA60FA2337BF88B980AB4CD0C<br>9D62A2D7F3ABEB220   | 23.03.07.2213 | <br>7D04D18E2BF2606FF78A71C486E03CD52375B3<br>3DA83C0E3778F59CC60B6A0877   | 23.02.1<br>3.1837 | 097C9EB5DDFE90E157213F73AA005<br>D04B6CB41CEBACCF9B2A5C67767FD9E84E2   <br>| 23.05.23.2111 | 1A53C4CC2072D34F49A2<br>230DDD917C6C23836BB546601A446EF0923D63<br>A42D1C   | 23.11.04.1715 | 568B091523C<br>DFAE9EF38F7E90F7C7FD2193D655D7D4B57252<br>3291B86DF77894D   | 23.02.10.2040 | C1<br>410C9D957358D04EFAFB86DB160DAF1B682B1F<br>C774F4BCAA57723705B851F8   | 23.10.23.<br>1741 | BE07DA96CAD3A7A7A017E05D52791D9<br>B37F2916EBADFDC64AA5E0A7181F29CDA   | <br>23.11.01.1654 | 42CDAD55D76E6A52C14C0C<br>7F8B49A27A77061E7E75E434D667C92F8C735E<br>9F46   | 23.01.13.1832 | 9B38B2B89338A<br>7D86EE4DB51C565523FB3ECE1162EE0DBC2E00<br>A348E829F2E3B   | 23.11.01.2049 | D20A<br>3AECB380DD0D9949D16EC0C24C6B58F10DF7C5<br>DF896214D2732C0C646741   | 23.10.23.17<br>41 | 60EE398DF5F63F2F614505784B37E5E91<br>F7F83FCB1DCA3BFDFACC720AF6AC0F4   | 23<br>.08.10.1807 | 7DC6D6BD195B3DA44BBA5CEA<br>54F3C424EAE406ACABE529EFB4E967E37D693D<br>A9   | 22.03.15.2220 | FE6948DE101FFBA<br>4FBAEA3BA9E993FC2F97707C8D068267E6FF20<br>FB429BACBB2   | 23.02.28.1412 | E9CB7B<br>FCF67F4670083408E452D25460859951E23C6F<br>BF32AE1250913AB2C845   | 23.01.13.1832<br> | AD74A6EBD87CB333D8370EFD2721C51785A<br>BA3BEC6C2CF0C2EF19091C480794A   | 23.0<br>8.10.1807 | 2530F00379DD42ECFEE2B72E06<br>8D922F89448742CED09D392ABE12E15A90EA96<br>   | 23.08.10.1807 | E9FC03E463BEFED0F<br>204DA85C30D87BA323936FC42263AB350AF470<br>BE4DDEDFD   | 23.10.23.1741 | A9309EFD<br>9AEABD59438933048D712C323C813CFC56CA95<br>321CB1D438FD7E9513   | 23.10.23.1741 |<br> 51F564CB3949996CF929C1C76DC467B8E1721<br>4CE1613704321ED240DDF59A266   | 23.01.<br>13.1832 | FC0E042434D58EF9D0506BB814D6<br>A4D16CBCA03EA4FA5DE00CFEFA0046CC2F38  <br> | 23.04.21.1447 | 18EDA6A42C207F1BAAC<br>EA31B9D141C52CEC0D9B78CB83C97280E78CE6<br>9BC0D67   | 23.10.10.1648 | 064AE9852D<br>97F237A4B84620987D450A43CD0EA16969A4CF<br>CAC4431621A6AD57   | 22.11.11.1040 | 9<br>90FE1803B7FDA29347376AB3DEAA79269471C6<br>CE7B897FC47AB1A90897D7AD5   | 23.10.10<br>.1239 | 3782E739846F116466C0848B90D4F3<br>88D8C2013AAA569BE07082BD483A7443F2   |<br> 23.03.27.1832 | C43D2FEA9A61BB0B1F841<br>1A60E7426689D14CFFD0CFBAFF698A3BE122A6<br>87ADD   | 23.01.13.1832 | 41344EE02300<br>859A0EC3F97E4F4F52D5067BF7ADBC6B8106B6<br>8D32B88A36D446   | 23.06.12.1645 | D6E<br>60FED241F770F1AA130C94A774DDEC09926101<br>2C2BE1496EB080EBE4E1B63   | 23.04.21.1<br>447 | 0A98897B52E36C53D3F182FFADCD06C9<br>5A5EE62AC4225D453FB40CF5B1359DB7   | 2<br>3.06.19.0935 | CC53DE9B9C1ACC646D9870F<br>614FADE09B2DF235BD320FF78239894E7889F6<br>D99   | 23.01.13.1832 | D6051E69502A8B<br>24F789B387301AC7DBA72DFC93D3770BDE59BF<br>88BA568815D6   | 23.08.10.1807 | 342C9<br>C5A2448BFB29FE5AD925F0EC1212A9B1475B50<br>326EDA7E778E923C1BBC4    ## Changes:  <br>* 238eacb17452a4aed18cc59cd01020e31e0c<br>7b5c Merge pull request #1874 from mic<br>rosoft/main * 141355e0f44ea47a3efcde79<br>599aaf1059cc1510 Merge pull request #1<br>872 from Shanefe/CalLogSummaryAutoUpda<br>te * cecaf2db8f9b06564223d41881132d10a<br>99cd46c Merge branch 'main' into CalLo<br>gSummaryAutoUpdate * f1643ab2c7886c80d<br>580822851b3c7670fb2bec0 Merge pull req<br>uest #1873 from guruxp/apascualCTMM * <br>4fed035e4d8f09c4319bb76998d761af7d037c<br>51 Merge branch 'main' into apascualCT<br>MM * 29d06735b4a794a2f69e2f0019ef3b380<br>8465049 Fix for Issue 1863 * 3e33a66af<br>3e6c796aa9fe69f0c5dd9fe8c160a28 Added <br>Documenation headers to TimeLine Funct<br>ions * cd447848aae1d0a4e09e4c5a873dd9b<br>bffd831d1 Update TimeLine Text generat<br>ion * dfb702e9fbe7b0936d956a57ee61b1d6<br>0f2e002c Autoupdate w/o user confirmat<br>ion * b132078c96e107072be6df1bc202d3f5<br>0fe4ff26 Add AutoUpdate Code See More <br> * 474e67e99a4415c52419a3e1aeb94071455<br>2f19a Merge pull request #1865 from Sh<br>anefe/CalLogSummaryUpdate * 458a2b5ffb<br>b6e592c23203c83716922db1ad188a Merge b<br>ranch 'main' into CalLogSummaryUpdate <br>* 9b738bddb00927a2e89d5337a6e26ad3d601<br>c8a3 Merge pull request #1871 from mic<br>rosoft/dpaul-HcCredGuard * ffa2b48aaaf<br>bacd1fd087ce3695a9b5201724284 spelling<br> * 9af0d442bd74d3e85e0261bf90c50bc34e1<br>7d6ab Improve Credential Guard Running<br> Check * 7dfe518afae89e0684cede6df4776<br>b11e815b7a7 PR Comments * b6ad3894f703<br>8a90f2f6e17eed51e18980934830 Merge bra<br>nch 'main' into CalLogSummaryUpdate * <br>9d5ca30a0685339b256b5bce15db80a4e9b15e<br>fa Merge pull request #1868 from Shane<br>fe/UpdateRBA_WarningToInfo * 1ef79bf4c<br>19d4e7cdeaf6dd8c1fe82f2266bc502 Merge <br>branch 'main' into UpdateRBA_WarningTo<br>Info * 1e075a6f94f1bc0266cd34034e1611b<br>e1ab07433 Added Shared Folder Name res<br>olver * 5cc56d23b8d384e1b0c311e45bebfa<br>a1c840241c 1st Pass on Summary Update <br>* 52409c44f3df8884d7d5b22ddb1164ed18ff<br>19f9 Merge pull request #1862 from mic<br>rosoft/dpaul-CodeFormatter * 595151d1d<br>103ef2c18584d9f02b2df4da6dca699 latest<br> version of PSScriptAnalyzer * 441956c<br>59693726e25637c8a8fea64ffeb901429 Merg<br>e pull request #1869 from microsoft/dp<br>aul-FixHcPester * da4c817ea951e566c34e<br>cc69c309d57ce43bed37 Increase count fo<br>r security section for expired auth ce<br>rt in testing data * 494dad6995d9a5ad1<br>4d2b2c4da30993614f6ba6b Fix Spacing * <br>3ed5c72e416d136e133947238933f9667011cc<br>85 Update warning * cc0918b28d4a71acd6<br>72dc1376dcb7145adaa257 Merge pull requ<br>est #1853 from microsoft/bilong-curlyq<br>uotescheck * 8640c32f7ffa20b5bb804f177<br>a5a676a95396312 Merge branch 'main' in<br>to bilong-curlyquotescheck * 04f30a4eb<br>f89405c5af5e552bc1add502701aa4b Merge <br>pull request #1864 from microsoft/bilo<br>ng-codeformatter * cdb2b561c64460ee511<br>6c6835f0f015034db2f85 Fix PSUseCorrect<br>Casing errors * ef12467c0941befd5e3660<br>629a42b3fb9cd81b8f Fix curly quotes * <br>f5ac415e9ebdc5efa6146ab70c36ce6d6d4a21<br>67 Add CodeFormatter check for curly q<br>uotes  This list of changes was .|
|2023-11-06 18:39:30|[fingerprintx](https://github.com/praetorian-inc/fingerprintx)|v1.1.11|Fixes https://github.com/praetorian-i<br>nc/fingerprintx/issues/25 |
|2023-11-06 17:06:39|[ILSpy](https://github.com/icsharpcode/ILSpy)|v8.2|ILSpy 8.x is based on .NET 6.0. All a<br>rtifacts **except** the self-contained<br> distribution are built framework-depe<br>ndent, which means  must be installed <br>prior to starting ILSpy.     # New Lan<br>guage Features  * C# 7.1 Pattern match<br>ing with generics  * C# 8.0 Recursive <br>patterns  * C# 9.0 Relational patterns<br>  * C# 9.0 not patterns  * C# 10.0 sta<br>tic abstract members in interfaces  * <br>C# 11.0 switch on (ReadOnly)Span    # <br>Contributions  * Add entry size info (<br>@startewho, #3052)  * Add GC Info to R<br>2R output (@eduardo-vp, #3076)  * Upda<br>te R2R (@cshung, #3088)  * Reduce "uns<br>afe" by replacing byte* pointer usage <br>with ReadOnlySpan&lt;byte&gt; (@fowl2,<br> #3106 )    # Enhancements  * #3090: a<br>dd support for the NUGET_PACKAGES envi<br>ronment variable  * Fixed some quirks <br>in our search: #3064, #3065 and #3038 <br>   # Performance  * #3075: Avoid proce<br>ssing already-transformed blocks by in<br>troducing BlockTransformContext.IndexO<br>fFirstAlreadyTransformedInstruction, w<br>hich allows us to track already transf<br>ormed instructions after a block has b<br>een merged into another by ConditionDe<br>tection.  * #3075: Add NextSetBit oper<br>ation to BitSet to avoid looking at ev<br>ery store bit individually in Reaching<br>DefinitionsVisitor.GetStores()  * #307<br>5: Fix ILVariableEqualityComparer.GetH<br>ashCode  * #3075: Improve performance <br>of CSharpResolver.LookupSimpleNameOrTy<br>peName in cases with a large number of<br> local variables.  * #3075: Eliminate <br>recursion in some parts of the decompi<br>ler engine  * ILSpy UI: #3057 - sub-op<br>timal use of StringBuilder when constr<br>ucting tree-node labels    # Bug fixes<br>  * #3061: Handler blocks of exception<br> filter blocks do not have a header.  <br>* #3103: unaligned.stobj cannot be tra<br>nsformed into inline assignment  * #30<br>91: extension methods named Add were s<br>kipping some checks in AccessPathEleme<br>nt.IsMethodApplicable.  * #3004: Metad<br>ataModule.ResolveEntity() returning nu<br>ll for System.IntPtr when C# 11 native<br> integers are enabled.  * #3105 - VS20<br>17-2019 addin didn't properly match su<br>bdirectory structure of 2022 addin  * <br>#3014: Missing type information in lam<br>bda expressions    And many other fixe<br>s, for a full list click .|
|2023-11-06 08:48:59|[color](https://github.com/fatih/color)|v1.16.0|## What's Changed    * Update dependa<br>bot.yml by @ilyabrin in https://github<br>.com/fatih/color/pull/200  * color: ad<br>d newline after wrapping text by @fati<br>h in https://github.com/fatih/color/pu<br>ll/192  * [Test] Nil check added by @h<br>yunsooda in https://github.com/fatih/c<br>olor/pull/203  * fixes #206 (using und<br>erline with a different fg color break<br>s) by @gregpoirson in https://github.c<br>om/fatih/color/pull/210    ### Depende<br>ncy updates  * Bump dominikh/staticche<br>ck-action from 1.2.0 to 1.3.0 by @depe<br>ndabot in https://github.com/fatih/col<br>or/pull/201  * Bump github.com/mattn/g<br>o-isatty from 0.0.17 to 0.0.18 by @dep<br>endabot in https://github.com/fatih/co<br>lor/pull/193  * Bump golang.org/x/sys <br>from 0.6.0 to 0.8.0 by @dependabot in <br>https://github.com/fatih/color/pull/19<br>5  * Bump github.com/mattn/go-isatty f<br>rom 0.0.18 to 0.0.19 by @dependabot in<br> https://github.com/fatih/color/pull/1<br>96  * Bump golang.org/x/sys from 0.8.0<br> to 0.10.0 by @dependabot in https://g<br>ithub.com/fatih/color/pull/199  * Bump<br> github.com/mattn/go-isatty from 0.0.1<br>9 to 0.0.20 by @dependabot in https://<br>github.com/fatih/color/pull/212  * Bum<br>p golang.org/x/sys from 0.10.0 to 0.13<br>.0 by @dependabot in https://github.co<br>m/fatih/color/pull/209  * Bump actions<br>/setup-go from 3 to 4 by @dependabot i<br>n https://github.com/fatih/color/pull/<br>202  * Bump actions/checkout from 3 to<br> 4 by @dependabot in https://github.co<br>m/fatih/color/pull/208  * Bump golang.<br>org/x/sys from 0.13.0 to 0.14.0 by @de<br>pendabot in https://github.com/fatih/c<br>olor/pull/213    ## New Contributors  <br>* @ilyabrin made their first contribut<br>ion in https://github.com/fatih/color/<br>pull/200  * @hyunsooda made their firs<br>t contribution in https://github.com/f<br>atih/color/pull/203  * @gregpoirson ma<br>de their first contribution in https:/<br>/github.com/fatih/color/pull/210    **<br>Full Changelog**: https://github.com/f<br>atih/color/compare/v1.15.0...v1.16.0|
|2023-11-06 06:41:17|[trivy](https://github.com/aquasecurity/trivy)|v0.47.0|## ⚡Release highlights and summary⚡<br>    👉 https://github.com/aquasecurity<br>/trivy/discussions/5520    ## Changelo<br>g  * d6df5fbcd docs: add info that lic<br>ense scanning supports file-patterns f<br>lag (#5484)  * 156d4cc60 docs: add Zor<br>a integration into Ecosystem session (<br>#5490)  * 772d1d08f fix(sbom): Use UUI<br>D as BomRef for packages with empty pu<br>rl (#5448)  * df47073fa ci: use maximi<br>ze build space for K8s tests (#5387)  <br>* fed471018 fix: correct error mismatc<br>h causing race in fast walks (#5516)  <br>* 46f1b9e7d docs: k8s vulnerability sc<br>anning (#5515)  * fdb3a15b2 chore(deps<br>): bump github.com/aws/aws-sdk-go-v2/s<br>ervice/sts from 1.23.2 to 1.25.0 (#550<br>6)  * d0d956fdc chore(deps): bump gith<br>ub.com/owenrumney/go-sarif/v2 from 2.2<br>.2 to 2.3.0 (#5493)  * 68b0797e5 docs:<br> remove glad for java datasources (#55<br>08)  * 474167c47 chore(deps): bump git<br>hub.com/testcontainers/testcontainers-<br>go/modules/localstack from 0.21.0 to 0<br>.26.0 (#5475)  * 7299867c2 chore: remo<br>ve unused logger attribute in amazon d<br>etector (#5476)  * 8656bd9f7 fix: corr<br>ect error mismatch causing race in fas<br>t walks (#5482)  * 2e10cd2eb chore(dep<br>s): bump goreleaser/goreleaser-action <br>from 4 to 5 (#5502)  * 13df74652 chore<br>(deps): bump docker/build-push-action <br>from 4 to 5 (#5500)  * b0141cfba chore<br>(deps): bump github.com/package-url/pa<br>ckageurl-go from 0.1.2-0.2023081222382<br>8-f8bb31c1f10b to 0.1.2 (#5491)  * 520<br>830b51 fix(server): add licenses to Bl<br>obInfo message (#5382)  * 9a6e125c7 ch<br>ore(deps): bump actions/checkout from <br>4.1.0 to 4.1.1 (#5501)  * 6e5927266 ch<br>ore(deps): bump github.com/aws/aws-sdk<br>-go-v2/service/ecr from 1.17.18 to 1.2<br>1.0 (#5497)  * f3de7bc3b feat: scan vu<br>lns on k8s core component apps (#5418)<br>  * e2fb3dd58 fix(java): fix infinite <br>loop when relativePath field points to<br> pom.xml being scanned (#5470)  * 3e83<br>3be7d chore(deps): bump github.com/doc<br>ker/docker from 24.0.5+incompatible to<br> 24.0.7+incompatible (#5472)  * ca50b7<br>7a3 fix(sbom): save digests for packag<br>e/application when scanning SBOM files<br> (#5432)  * 048150d43 docs: fix the br<br>oken link (#5454)  * 013d90199 docs: f<br>ix error when installing PyYAML for gh<br> pages (#5462)  * 26b495954 fix(java):<br> download java-db once (#5442)  * 57fa<br>701a8 chore(deps): bump google.golang.<br>org/grpc from 1.57.0 to 1.57.1 (#5447)<br>  * 53c9a7d76 docs(misconf): Update --<br>tf-exclude-downloaded-modules descript<br>ion (#5419)  * 01c98d151 feat(misconf)<br>: Support --ignore-policy in config sc<br>ans (#5359)  * 05b3c86a1 docs(misconf)<br>: fix broken table for Use container i<br>mage section (#5425)  * 1a15a3adb feat<br>(dart): add graph support (#5374)  * f<br>2a12f5f9 refactor: define a new struct<br> for scan targets (#5397)  * 6040d9f43<br> fix(sbom): add missed primaryURL and <br>source severity for CycloneDX (#5399) <br> * e5317c7bc fix: correct invalid MD5 <br>hashes for rpms ending with one or mor<br>e zero bytes (#5393)  * 9fba79f0b chor<br>e(deps): move to aws-sdk-go-v2 (#5381)<br>  * 00f2059e5 docs: remove --scanners <br>none (#5384)  * 57a102231 docs: Update<br> container_image.md #5182 (#5193)  * 5<br>b2b4ea38 feat(report): Add InstalledFi<br>les field to Package (#4706)    |
|2023-11-05 22:45:27|[merlin](https://github.com/Ne0nd0g/merlin)|v2.0.0|### Added    - Peer-to-Peer Agent com<br>munications  - gRPC Server for     - D<br>efault interface/port is 127.0.0.1:500<br>51 and default password is merlin    -<br> -addr the address to listen for gRPC <br>connections from the Merlin CLI    - -<br>password the password for CLI RPC clie<br>nts to connect to the Merlin server   <br> - -secure require client TLS certific<br>ate verification    - -tlsCA TLS Certi<br>ficate Authority file path to verify c<br>lient certificates    - -tlsCert TLS c<br>ertificate file path for the Merlin se<br>rver    - -tlsKey TLS private key file<br> path for the Merlin server  - Structu<br>red logging in JSON format to STDOUT u<br>sing  package    - -debug enable debug<br> output    - -extra enable extra debug<br> output (e.g., HTTP requests/responses<br>)    - -trace enable trace output to s<br>ee stepping through functions  - New S<br>MB/UDP/TCP listeners    - Used to conf<br>igure how the listener process Agent t<br>raffic    - Listeners DO NOT bind to i<br>nterfaces/ports on the Merlin server, <br>used for Agent configuration/generatio<br>n ONLY  - Delegate message types and f<br>unctions for processing them  - Config<br>urable listener authentication methods<br> for Agent communications: OPAQUE & no<br>ne  - Configurable listener transforms<br> for Agent communications: aes, base64<br>-byte, base64-string, hex-byte, hex-st<br>ring, gob-base, gob-string, jwe, rc4, <br>and xor    - The last transform in the<br> list **MUST** be gob-base  - GitHub A<br>ctions for building and testing the Me<br>rlin Agent    ### Changed    - Refacto<br>red _some_ areas to align with DDD and<br> SOLID to alleviate circular dependenc<br>ies implementing peer-to-peer comms   <br> - Implemented base "entity" structure<br>s and "aggregates"    - Implemented th<br>e "Repository" pattern for Agents, Del<br>egates, Groups, Listeners, Servers    <br>- Implemented the "Services" patter fo<br>r interacting with Agents, Listeners, <br>& Base messages  - Configurable JWT ke<br>y value for HTTP listeners  - Upgraded<br>  to v0.40.0  - The Minimum supported <br>Go version is now 1.21  - Listeners ar<br>e now handled by a UUID and no longer <br>by a name as a string  - Moved the bui<br>ld string out of main.go and into pkg/<br>merlin.go  - Removed PWNBoard from mai<br>n.go  - Removed wiki documentation fro<br>m docs to a new repository at https://<br>github.com/Ne0nd0g/merlin-documentatio<br>n  - Replaced github.com/satori/go.uui<br>d with github.com/google/uuid  - Repla<br>ced github.com/square/go-jose with git<br>hub.com/go-jose/go-jose  - Replaced gi<br>thub.com/Ne0nd0g/merlin/pkg/messages w<br>ith github.com/Ne0nd0g/merlin-message <br>   - Removes the need to depend on or <br>import the Merlin Server package    ##<br># Removed    - Removed the interactive<br> CLI menu to     - Uses gRPC to commun<br>icate with the Merlin server    ---   <br> **The data/bin directory contains com<br>piled versions of the Merlin CLI and M<br>erlin Agents**    Merlin documentation<br> and Wiki can be found     > The compr<br>essed files have a password of merlin|
|2023-11-05 17:31:13|[dbeaver](https://github.com/dbeaver/dbeaver)|23.2.4|                 - SQL editor:       <br>              - Code completion for up<br>date statements was added             <br>        - Smart completion and replace<br>ments of quoted expressions was fixed <br>                    - Redundant errors<br> on opening SQL Editor for the first t<br>ime were removed from the logs        <br>         - Database Navigator:        <br>             - Filtered objects visual<br>ization was added                     <br>- Script folder opening was fixed     <br>            - Data transfer:          <br>           - Attributes names for quot<br>ed attributes are handled correctly   <br>                  - "Copy as HTML" res<br>ult presentation is improved          <br>       - Data editor:                 <br>    - Background color reset was fixed<br>                     - Message about c<br>ontent representation size limit was f<br>ixed                     - App freeze <br>in binary editor was fixed (MacOS)    <br>             - ER diagrams: one-to-one<br> connection rendering was fixed       <br>          - Connections:              <br>       - SSH connection page validatio<br>n is enhanced for jump servers        <br>             - Complex JDBC driver sup<br>port was improved (context classloader<br> + driver cache)                 - Gen<br>eral:                     - Script nam<br>es are sorted alphabetically          <br>           - Refresh button was added <br>to the ‘Generate DDL’ dialog        <br>             - Issue with app launch w<br>as fixed (rare case)                 -<br> Databases:                     - Orac<br>le: search package bodies as packages <br>was supported                     - Po<br>stgreSQL:                         - De<br>fault privileges presentation and edit<br>ing was supported                     <br>    - Sequences permissions reading fo<br>r quoted roles was fixed              <br>       - SQLite: required columns crea<br>ting was fixed             |
|2023-11-05 17:11:19|[lsassy](https://github.com/Hackndo/lsassy)|v3.1.9|* Add some tests 92e4ae429404bc680528<br>70e4ddcd6346fd4dd8cf (Still need some <br>work to do, but better than nothing :)<br>)  * Expiration time in ticket filenam<br>es f088fedd159a776cacbf8e1146fd730f211<br>6a247 & bc31c0e4f1301659bdf5d3524a7c3f<br>5f0ac5778a  * Update EDRSandBlast modu<br>le 041b91c32f295400f88ee3385ebf2ef027a<br>468c8  * Fix deployement of tests by @<br>noraj #85   * Fix pretty output (and n<br>ice code refactor) by @n3rada #88 |
|2023-11-05 14:30:07|[Online_tools](https://github.com/Zhao-sai-sai/Online_tools)|0.4.0|### 增加新工具  - nc  - Nmap  - D盾  <br>- 河马webshell查杀    ### 新功能添加  <br>增加了工具搜索功能，可以按alt+d键快速弹<br>出|
|2023-11-05 07:49:31|[gshark](https://github.com/madneal/gshark)|v1.2.2|## Fixed    * 修复数据库初始化逻辑问<br>题  * 升级前端组件版本|
|2023-11-05 03:44:43|[Ladon](https://github.com/k8gege/Ladon)|v11.9|Ladon 11.9  20231105  [u]LadonStudy  <br>支持bypassEDR  [u]LadonShell  支持tls 1<br>.2  [u]RdpInfo    优化RDP Ntlm探测系统<br>信息  [u]RdpLog   查看3389连接日志(IP、<br>用户名、CertHash)  [+]CVE-2023-46604 Ac<br>tiveMQ CVE-2023-46604 RCE Exploit     <br> Ladon 11.8  20231018  [u]InfoScan   <br>新增SmtpInfo  [+]SmtpInfo   新增Smtp Nt<br>lm探测系统信息(25、465、587端口)  [u]I<br>nfoScan   新增HttpInfo  [+]HttpInfo   <br>新增Http/Https Ntlm探测系统信息(SharePo<br>int)      Ladon 11.7 20231010  [u]BadP<br>otato  本地提权 支持Base64参数 解决Cob<br>alt Strike或LadonShell下双引号等问题  <br>[u]EfsPotato  本地提权 支持Base64参数 <br>解决Cobalt Strike或LadonShell下双引号等<br>问题  [u]GodPotato  本地提权 支持Base64<br>参数 解决Cobalt Strike或LadonShell下双<br>引号等问题  [u]SweetPotato  本地提权 支<br>持Base64参数 解决Cobalt Strike或LadonSh<br>ell下双引号等问题  [u]McpPotato  本地<br>提权 支持Base64参数 解决Cobalt Strike或<br>LadonShell下双引号等问题  [+]clsLog   <br>新增清理最近访问文件记录    9.24  [u] W<br>miExec2  横向移动 内网渗透 修复b64cmd<br>参数Bug  [u] WmiExec   横向移动 内网渗<br>透 修复域用户连接Bug  [+] AtExec   横向<br>移动 内网渗透 Base64统一为Unicode(如who<br>ami编码 dwBoAG8AYQBtAGkA )    9.18  [u<br>]PostShell   hexupload支持任意文件上传<br>-当前目录|
|2023-11-03 12:57:34|[merlin-agent](https://github.com/Ne0nd0g/merlin-agent)|v2.0.0|### Added    - Peer-to-Peer Agent com<br>munication methods: smb-bind, smb-reve<br>rse, tcp-bind, tcp-reverse, udp-bind, <br>udp-reverse    - An associated Listene<br>r UUID must be provided with -listener<br> command line argument or LISTENER Mak<br>e file variable    - An associated net<br>work interface and port must be provid<br>ed with the -addr command line argumen<br>t or ADDR Make file variable    - Dele<br>gate message type and associated handl<br>ing  - Configurable Agent authenticati<br>on methods: OPAQUE & none    - Added a<br>uth variable to main.go    - Added AUT<br>H variable to Make file (e.g., make wi<br>ndows AUTH=OPAQUE)    - Added -auth co<br>mmand line argument  - Configurable Ag<br>ent transforms: gob-base, gob-string, <br>base64-byte, base64-string, hex,-byte,<br> hex-string, aes, jwe, rc4, and xor   <br> - Added transforms variable to main.g<br>o    - Added TRANSFORMS variable to Ma<br>ke file (e.g., make windows TRANSFORMS<br>=aes,gob-base)    - Added -transforms <br>command line argument  - link command <br>for the Agent to initiate a peer-to-pe<br>er connection with a listening bind ag<br>ent    - Example: link tcp 192.168.1.7<br>2:4444  - listener command for the Age<br>nt to start a listener to receive a co<br>nnection from a reverse peer-to-peer c<br>onnection    - list to return a list o<br>f instantiated on the Agent (e.g., lis<br>tener list)    - start to start a list<br>ener based on the passed in type and i<br>nterface      - Example: listener star<br>t tcp 0.0.0.0:4444    - stop to stop a<br>n already created listener      - Exam<br>ple: listener stop tcp  to v0.40.0  - <br>The Minimum supported Go version is no<br>w 1.20  - HTTP URL rotation strategy i<br>s now random instead of round-robin  -<br> Replaced github.com/satori/go.uuid wi<br>th github.com/google/uuid  - Replaced <br>github.com/square/go-jose with github.<br>com/go-jose/go-jose  - Replaced github<br>.com/Ne0nd0g/merlin/pkg/messages with <br>github.com/Ne0nd0g/merlin-message    -<br> Removes the need to depend on or impo<br>rt the Merlin Server package     Merli<br>n documentation and Wiki can be found <br>    > The compressed files have a pass<br>word of merlin|
|2023-11-03 04:34:30|[safeline](https://github.com/chaitin/safeline)|v3.10.1|### 修复    - 修复无法修改 通用配置-<br>其他-拦截页面附加说明 的问题|
|2023-11-03 03:30:09|[DongTai](https://github.com/HXSecurity/DongTai)|v1.16.0|## What's Changed  * feat: improve pa<br>tch type hint by @st1020 in https://gi<br>thub.com/HXSecurity/DongTai/pull/1841 <br> * feat: modify user field by @st1020 <br>in https://github.com/HXSecurity/DongT<br>ai/pull/1839  * feat: remove login loc<br>k by @st1020 in https://github.com/HXS<br>ecurity/DongTai/pull/1840  * feat:add <br>agent version api. by @Bidaya0 in http<br>s://github.com/HXSecurity/DongTai/pull<br>/1838  * feat/project_type_summary by <br>@Bidaya0 in https://github.com/HXSecur<br>ity/DongTai/pull/1842  * deps: add pyo<br>tp dep by @st1020 in https://github.co<br>m/HXSecurity/DongTai/pull/1846  * feat<br>: add project status change notify by <br>@st1020 in https://github.com/HXSecuri<br>ty/DongTai/pull/1845  * fix: percentag<br>e zero error. by @Bidaya0 in https://g<br>ithub.com/HXSecurity/DongTai/pull/1847<br>  * fix: zero divide by @Bidaya0 in ht<br>tps://github.com/HXSecurity/DongTai/pu<br>ll/1849  * fix: project current versio<br>n auth fix. by @Bidaya0 in https://git<br>hub.com/HXSecurity/DongTai/pull/1848  <br>* feat: add request topo models. by @B<br>idaya0 in https://github.com/HXSecurit<br>y/DongTai/pull/1853  * feat: project t<br>ype summary list. by @Bidaya0 in https<br>://github.com/HXSecurity/DongTai/pull/<br>1854  * feat: modify user info api by <br>@st1020 in https://github.com/HXSecuri<br>ty/DongTai/pull/1856  * feat: increase<br> buffer size. by @Bidaya0 in https://g<br>ithub.com/HXSecurity/DongTai/pull/1855<br>  * feat: add tantivy search by @st102<br>0 in https://github.com/HXSecurity/Don<br>gTai/pull/1857  * deps: add qrcode dep<br> by @st1020 in https://github.com/HXSe<br>curity/DongTai/pull/1858  * feat: chan<br>ge tantivy index path by @st1020 in ht<br>tps://github.com/HXSecurity/DongTai/pu<br>ll/1859  * Feat/add ldap settings by @<br>Bidaya0 in https://github.com/HXSecuri<br>ty/DongTai/pull/1860  * feat: add upda<br>te vul tantivy index receiver by @st10<br>20 in https://github.com/HXSecurity/Do<br>ngTai/pull/1861  * feat: vul status ch<br>ange msg. by @Bidaya0 in https://githu<br>b.com/HXSecurity/DongTai/pull/1862  * <br>build(deps):  fix deps . by @Bidaya0 i<br>n https://github.com/HXSecurity/DongTa<br>i/pull/1864  * build(deps):  fix deps <br>. by @Bidaya0 in https://github.com/HX<br>Security/DongTai/pull/1865  * fix: tan<br>tivy search error by @st1020 in https:<br>//github.com/HXSecurity/DongTai/pull/1<br>866  * build(deps):  fix deps . by @Bi<br>daya0 in https://github.com/HXSecurity<br>/DongTai/pull/1867  * fix: tantivy sea<br>rch error by @st1020 in https://github<br>.com/HXSecurity/DongTai/pull/1868  * f<br>eat/msg_status_log by @Bidaya0 in http<br>s://github.com/HXSecurity/DongTai/pull<br>/1869  * feat load vul fix by @Bidaya0<br> in https://github.com/HXSecurity/Dong<br>Tai/pull/1870  * fix: change log level<br>. by @Bidaya0 in https://github.com/HX<br>Security/DongTai/pull/1873  * fix: loa<br>d hook strategy with dup data. by @Bid<br>aya0 in https://github.com/HXSecurity/<br>DongTai/pull/1874  * fix: tantivy path<br> error by @st1020 in https://github.co<br>m/HXSecurity/DongTai/pull/1875  * feat<br>: add strategy case. by @Bidaya0 in ht<br>tps://github.com/HXSecurity/DongTai/pu<br>ll/1877  * feat: add vul log time rang<br>e. by @Bidaya0 in https://github.com/H<br>XSecurity/DongTai/pull/1878  * Feat/ad<br>d vul log time range by @Bidaya0 in ht<br>tps://github.com/HXSecurity/DongTai/pu<br>ll/1879  * Feat/add 1.16 strategy p2 b<br>y @Bidaya0 in https://github.com/HXSec<br>urity/DongTai/pull/1880  * feat: add 1<br>.16 strategy. by @Bidaya0 in https://g<br>ithub.com/HXSecurity/DongTai/pull/1876<br>  * fix: vul_log msg record by @Bidaya<br>0 in https://github.com/HXSecurity/Don<br>gTai/pull/1881  * fix: vul_log msg rec<br>ord by @Bidaya0 in https://github.com/<br>HXSecurity/DongTai/pull/1882  * fix: v<br>ul_log msg record by @Bidaya0 in https<br>://github.com/HXSecurity/DongTai/pull/<br>1883  * feat: migration permissions. b<br>y @Bidaya0 in https://github.com/HXSec<br>urity/DongTai/pull/1884  * feat: updat<br>e ci by @tscuite in https://github.com<br>/HXSecurity/DongTai/pull/1885  * feat:<br> update ci by @tscuite in https://gith<br>ub.com/HXSecurity/DongTai/pull/1886  *<br> feat: update ci by @tscuite in https:<br>//github.com/HXSecurity/DongTai/pull/1<br>887  * feat: update ci by @tscuite in <br>https://github.com/HXSecurity/DongTai/<br>pull/1888  * fix: dockerfile by @st102<br>0 in https://github.com/HXSecurity/Don<br>gTai/pull/1889  * Develop to Beta by @<br>st1020 in https://github.com/HXSecurit<br>y/DongTai/pull/1892  * Beta to Main by<br> @st1020 in https://github.com/HXSecur<br>ity/DongTai/pull/1893  * Develop to Be<br>ta by @st1020 in https://github.com/HX<br>Security/DongTai/pull/1895  * Beta to <br>Main by @st1020 in https://github.com/<br>HXSecurity/DongTai/pull/1896  * Update<br> release_dongtai.yml by @lingyuguo in <br>https://github.com/HXSecurity/DongTai/<br>pull/1898  * Beta by @lingyuguo in htt<br>ps://github.com/HXSecurity/DongTai/pul<br>l/1899  * cos gitaction by @lingyuguo <br>in https://github.com/HXSecurity/DongT<br>ai/pull/1902  * Beta by @lingyuguo in <br>https://github.com/HXSecurity/DongTai/<br>pull/1903    ## New Contributors  * @l<br>ingyuguo made their first contribution<br> in https://github.com/HXSecurity/Dong<br>Tai/pull/1898    **Full Changelog**: h<br>ttps://github.com/HXSecurity/DongTai/c<br>ompare/v1.15.0...v1.16.0|
|2023-11-02 23:33:26|[console](https://github.com/minio/console)|v0.41.0|## What's Changed  * Updated Playwrig<br>ht tests by @bexsoft in https://github<br>.com/minio/console/pull/3070  * Fixed <br>Failing integration test by @bexsoft i<br>n https://github.com/minio/console/pul<br>l/3071  * mds-released-v0.9.3 by @mini<br>o-bot in https://github.com/minio/cons<br>ole/pull/3073  * Updated README file b<br>y @bexsoft in https://github.com/minio<br>/console/pull/3074  * Removed deprecat<br>ed components and replaced them with m<br>ds ones by @bexsoft in https://github.<br>com/minio/console/pull/3077  * Updated<br> FileSelector and removed old componen<br>t by @bexsoft in https://github.com/mi<br>nio/console/pull/3076  * Removed mui s<br>upport from PasswordSelector component<br> by @bexsoft in https://github.com/min<br>io/console/pull/3078  * Add HelpTips t<br>o Console by @jinapurapu in https://gi<br>thub.com/minio/console/pull/3054  * Fi<br>x: cache clientIP in GetConsoleHTTPCli<br>ent by @adriangitvitz in https://githu<br>b.com/minio/console/pull/3056  * Compo<br>nents cleanup by @bexsoft in https://g<br>ithub.com/minio/console/pull/3079  * R<br>emoved FormSwitchWrapper component by <br>@bexsoft in https://github.com/minio/c<br>onsole/pull/3081  * Migrated mui Box t<br>o use mds component by @bexsoft in htt<br>ps://github.com/minio/console/pull/308<br>2  * mui Grid component replacement by<br> @bexsoft in https://github.com/minio/<br>console/pull/3084  * Bump golang.org/x<br>/net from 0.15.0 to 0.17.0 by @dependa<br>bot in https://github.com/minio/consol<br>e/pull/3086  * Use the new golang vers<br>ion 1.21.3 by @shtripat in https://git<br>hub.com/minio/console/pull/3087  * Upd<br>ated styling methods to remove mui and<br> replace it with mds by @bexsoft in ht<br>tps://github.com/minio/console/pull/30<br>85  * Updated mds version to v0.9.6 by<br> @bexsoft in https://github.com/minio/<br>console/pull/3090  * Replaced mui acco<br>rdion with mds component by @bexsoft i<br>n https://github.com/minio/console/pul<br>l/3089  * Update swagger generated fil<br>es with latest swagger version by @ces<br>nietor in https://github.com/minio/con<br>sole/pull/3094  * Add global params fo<br>r limit and offset by @reivaj05 in htt<br>ps://github.com/minio/console/pull/309<br>6  * Add share link exp api by @cesnie<br>tor in https://github.com/minio/consol<br>e/pull/3095  * Improved error handling<br> in Object Browser by @bexsoft in http<br>s://github.com/minio/console/pull/3097<br>  * Replace missing icons from mui by <br>@bexsoft in https://github.com/minio/c<br>onsole/pull/3101  * MDS Console improv<br>ements by @bexsoft in https://github.c<br>om/minio/console/pull/3102  * Replaced<br> Notification components with mds vari<br>ants by @bexsoft in https://github.com<br>/minio/console/pull/3103  * Autocomple<br>te component replacement by @bexsoft i<br>n https://github.com/minio/console/pul<br>l/3104  * Migrated Selector & Chart To<br>oltips styles by @bexsoft in https://g<br>ithub.com/minio/console/pull/3107  * M<br>igrated Object Manager components to m<br>ds by @bexsoft in https://github.com/m<br>inio/console/pull/3108  * update docke<br>r file to ubi9 base image by @aead in <br>https://github.com/minio/console/pull/<br>3109  * Restored ENV var display suppo<br>rt in Console Configuration pages. by <br>@bexsoft in https://github.com/minio/c<br>onsole/pull/3112  * Replaced MenuDropd<br>own components with mds variables by @<br>bexsoft in https://github.com/minio/co<br>nsole/pull/3113  * Support resolving o<br>f listen addrs to multiple IPv4/IPv6 b<br>y @vadmeste in https://github.com/mini<br>o/console/pull/3100  * Updated Logs Pa<br>ge to use mds components by @bexsoft i<br>n https://github.com/minio/console/pul<br>l/3114  * update the madmin-go dep by <br>@jiuker in https://github.com/minio/co<br>nsole/pull/3115  * Fix days selector t<br>o ignore daylight savings by @nreising<br>ercres in https://github.com/minio/con<br>sole/pull/3117  * Updated common bars <br>by @bexsoft in https://github.com/mini<br>o/console/pull/3118  * Updated HelpMen<br>u components to use only mds subcompon<br>ents by @bexsoft in https://github.com<br>/minio/console/pull/3119  * Updated Lo<br>gin Error Callback page to mds by @bex<br>soft in https://github.com/minio/conso<br>le/pull/3120  * Release v0.41.0 by @be<br>xsoft in https://github.com/minio/cons<br>ole/pull/3121    ## New Contributors  <br>* @adriangitvitz made their first cont<br>ribution in https://github.com/minio/c<br>onsole/pull/3056  * @aead made their f<br>irst contribution in https://github.co<br>m/minio/console/pull/3109  * @nreising<br>ercres made their first contribution i<br>n https://github.com/minio/console/pul<br>l/3117    **Full Changelog**: https://<br>github.com/minio/console/compare/v0.40<br>.0...v0.41.10|
|2023-11-02 21:58:20|[filebrowser](https://github.com/filebrowser/filebrowser)|v2.26.0|## Changelog * a4cb813d chore(release<br>): 2.26.0 * 4d0a68e7 fix: goreleaser y<br>aml * a744bd22 build(deps): bump golan<br>g.org/x/image from 0.5.0 to 0.10.0 (#2<br>800) * da1fe7c9 fix: disable static re<br>source files listing * 7fabadc8 feat: <br>make user session timeout configurable<br> (#2753) * c3079d30 feat: add modern g<br>reek translation (#2778) * 6a31af6c fi<br>x: solve docker build failed issue (#2<br>797) * 21d361ad build(deps-dev): bump <br>postcss from 8.4.27 to 8.4.31 in /fron<br>tend (#2749) * d574fb6d build(deps): b<br>ump golang.org/x/net from 0.11.0 to 0.<br>17.0 (#2758) * bb4bb508 build(deps): b<br>ump @babel/traverse in /frontend (#277<br>5) * edd808f1 fix: avoid the front-end<br> calling api/renew loop (#2792) * cdcd<br>9a31 fix: display file size as base 2 <br>(KiB instead of KB) (#2779) * d0c3aeac<br> chore: update en translation (#2777) <br>* 94844545 chore: update en translatio<br>n (#2776) * bd3c1941 fix: revert fetch<br>URL changes in auth (Fixes #2729) (#27<br>39) * 01f7842a docs: add demo url to R<br>EADME * 38f77882 build: fix deprecated<br> goreleaser config options  |
|2023-11-02 14:46:40|[nuclei](https://github.com/projectdiscovery/nuclei)|v3.0.3|    ## What's Changed  * Added self-c<br>ontained template support to headless <br>protocol by @dogancanbakir in https://<br>github.com/projectdiscovery/nuclei/pul<br>l/4322  * Added miscellaneous SDK enha<br>ncements by @tarunKoyalwar in https://<br>github.com/projectdiscovery/nuclei/pul<br>l/4301  * Fixed issue with trailing do<br>t in dns protocol by @dogancanbakir in<br> https://github.com/projectdiscovery/n<br>uclei/pull/4295  * Fixed connection is<br>sues in javascript, network protocol @<br>tarunKoyalwar in https://github.com/pr<br>ojectdiscovery/nuclei/pull/4313  * Fix<br>ed issue in flow to use javascript by <br>@tarunKoyalwar in https://github.com/p<br>rojectdiscovery/nuclei/pull/4313  * Up<br>dated cloned directory structure (proj<br>ect owner => repo) for GitHub by @doga<br>ncanbakir in https://github.com/projec<br>tdiscovery/nuclei/pull/4293    ## New <br>Contributors  * @atomiczsec made their<br> first contribution in https://github.<br>com/projectdiscovery/nuclei/pull/4296 <br>   **Full Changelog**: https://github.<br>com/projectdiscovery/nuclei/compare/v3<br>.0.2...v3.0.3|
|2023-11-02 13:13:38|[gau](https://github.com/lc/gau)|v2.2.1|## Changelog * d556483 Merge pull req<br>uest #115 from lc/lc/fix-panic * 4fa05<br>2d fix(panic): update version * 6dae65<br>7 fix(panic): fix output panic * c146c<br>22 fix(panic): fix output panic * abf8<br>b12 Merge pull request #111 from zerod<br>ivisi0n/feature/arm64-arch * 7029d1a A<br>dd arm64 arch  |
|2023-11-02 11:48:46|[aliyun-cli](https://github.com/aliyun/aliyun-cli)|v3.0.18<br>6|## What's Changed * upload: fix flags<br> by @JacksonTian in https://github.com<br>/aliyun/aliyun-cli/pull/858   **Full C<br>hangelog**: https://github.com/aliyun/<br>aliyun-cli/compare/v3.0.185...v3.0.186|
|2023-11-02 03:54:39|[emp3r0r](https://github.com/jm33-m0/emp3r0r)|v1.32.2|##  (2023-11-02)   ### Bug Fixes  * F<br>ileBaseName needs to strip / ()|
|2023-11-02 01:22:36|[harbor](https://github.com/goharbor/harbor)|v2.9.1|  ## What's Changed ### Component upd<br>ates ⬆️ * (cherry-pick) Remove job s<br>tatus track information from redis aft<br>er stop the job in the queue by @stone<br>zdj in https://github.com/goharbor/har<br>bor/pull/19307 * (cherry-pick) fix sto<br>rage.redirect.disable migrate template<br> error release-2.9.0 by @MinerYang in <br>https://github.com/goharbor/harbor/pul<br>l/19336 * [Cherry-pick]Hide version pr<br>operty if the value is undefined by @A<br>llForNothing in https://github.com/goh<br>arbor/harbor/pull/19396 * (cherry-pick<br>) Change fixed_version to package_vers<br>ion by @stonezdj in https://github.com<br>/goharbor/harbor/pull/19432 * [cherry-<br>pick]bump golang to 1.20.10 by @MinerY<br>ang in https://github.com/goharbor/har<br>bor/pull/19431 * fix: bump up TRIVYVER<br>SION=v0.46.0 && TRIVYADAPTERVERSION=v0<br>.30.17 by @zyyw in https://github.com/<br>goharbor/harbor/pull/19447 * [cherry-p<br>ick] Use batch to list the job id in t<br>he job queue to avoid crash redis by @<br>stonezdj in https://github.com/goharbo<br>r/harbor/pull/19455 * bump golang.org/<br>x/net to v0.17.0 && go.opentelemetry.i<br>o/contrib on release-2.9.0 by @MinerYa<br>ng in https://github.com/goharbor/harb<br>or/pull/19460 * bump go.opentelemetry.<br>io/contrib/instrumentation/github.com/<br>gorilla/m… by @MinerYang in https://g<br>ithub.com/goharbor/harbor/pull/19476 *<br> bump golang to 1.21.3 on release-2.9.<br>0 by @MinerYang in https://github.com/<br>goharbor/harbor/pull/19503 * fix: bump<br> up TRIVYVERSION=v0.46.1 && TRIVYADAPT<br>ERVERSION=v0.30.18 by @zyyw in https:/<br>/github.com/goharbor/harbor/pull/19499<br> * update ut mock anything by @MinerYa<br>ng in https://github.com/goharbor/harb<br>or/pull/19506 * bump google.golang.org<br>/grpc by @MinerYang in https://github.<br>com/goharbor/harbor/pull/19513 ### Oth<br>er Changes * [cherry-pick]Refactor uns<br>table test cases by @YangJiao0817 in h<br>ttps://github.com/goharbor/harbor/pull<br>/19351 * [cherry-pick]Add security hub<br> API test case by @YangJiao0817 in htt<br>ps://github.com/goharbor/harbor/pull/1<br>9377 * [cherry-pick]Add security hub U<br>I test case by @YangJiao0817 in https:<br>//github.com/goharbor/harbor/pull/1944<br>9 * Bump up version to v2.9.1 by @Yang<br>Jiao0817 in https://github.com/goharbo<br>r/harbor/pull/19451 * [cherry-pick]Add<br> GC accessory API test case by @YangJi<br>ao0817 in https://github.com/goharbor/<br>harbor/pull/19463 * [cherry-pick]Add G<br>C accessory UI test case by @YangJiao0<br>817 in https://github.com/goharbor/har<br>bor/pull/19471 * Refresh base images o<br>n release-2.9.0 by @YangJiao0817 in ht<br>tps://github.com/goharbor/harbor/pull/<br>19475 * [cherry-pick]Add GC details an<br>d GC workers API test case by @YangJia<br>o0817 in https://github.com/goharbor/h<br>arbor/pull/19483 * [cherry-pick]Add GC<br> details and GC workers UI test case b<br>y @YangJiao0817 in https://github.com/<br>goharbor/harbor/pull/19488 * [cherry-p<br>ick]Add banner message API test case b<br>y @YangJiao0817 in https://github.com/<br>goharbor/harbor/pull/19514   **Full Ch<br>angelog**: https://github.com/goharbor<br>/harbor/compare/v2.9.0...v2.9.1 |
|2023-11-01 18:00:41|[smbmap](https://github.com/ShawnDEvans/smbmap)|v1.9.3.<br>1|We've had one release yes, but what a<br>bout second release?     * Additional <br>error checking to account for hosts th<br>at allow an SMB connection but host  z<br>ero shares  * Paths were displaying in<br>correctly in CSV, Grepable, and stdout<br> formats under certain conditions  * M<br>ore accurate messages in the progress <br>indicator  * Probably added a few bugs<br>...    Enjoy! |
|2023-11-01 15:32:57|[terraform](https://github.com/hashicorp/terraform)|v1.6.3|## 1.6.3 (November 1, 2023)  ENHANCEM<br>ENTS: * backend/s3: Adds the parameter<br> skip_s3_checksum to allow users to di<br>sable checksum on S3 uploads for compa<br>tibility with "S3-compatible" APIs. ()<br>  |
|2023-11-01 12:02:45|[upx](https://github.com/upx/upx)|v4.2.1|Please see the file  for a detailed l<br>ist of changes.    Note: all versions <br>are functionally equivalent, i.e. each<br> version can handle **all** executable<br> formats, so you only need the file th<br>at runs on your host OS.    Security/V<br>irusTotal links are listed in the pinn<br>ed issue https://github.com/upx/upx/is<br>sues/437    | Asset / File | Descripti<br>on / Host OS |  | --- | --- |  |  | UP<br>X - Linux version |  | upx-4.2.1-arm64<br>_linux.tar.xz | UPX - Linux version | <br> | upx-4.2.1-armeb_linux.tar.xz | UPX <br>- Linux version |  | upx-4.2.1-arm_lin<br>ux.tar.xz | UPX - Linux version |  | u<br>px-4.2.1-dos.zip | UPX - DOS version |<br>  | upx-4.2.1-i386_linux.tar.xz | UPX <br>- Linux version |  | upx-4.2.1-mipsel_<br>linux.tar.xz | UPX - Linux version |  <br>| upx-4.2.1-mips_linux.tar.xz | UPX - <br>Linux version |  | upx-4.2.1-powerpc64<br>le_linux.tar.xz | UPX - Linux version <br>|  | upx-4.2.1-powerpc_linux.tar.xz | <br>UPX - Linux version |  |  | UPX - **so<br>urce code tarball** |  | upx-4.2.1-win<br>32.zip | UPX - X86 Win32 version |  | <br>  | UPX - X64 Win64 version ||
|2023-11-01 08:57:43|[gopsutil](https://github.com/shirou/gopsutil)|v3.23.1<br>0|    ## What's Changed  ### cpu  * fix<br>(linux): validate cpu fields length be<br>fore accessing index by @JanDeDobbelee<br>r in https://github.com/shirou/gopsuti<br>l/pull/1544  ### host  * [host][darwin<br>]: fix Users by @shirou in https://git<br>hub.com/shirou/gopsutil/pull/1537  ###<br> process  * [process][darwin]: skip pr<br>ocess.Nice test if darwin on GitHub Ac<br>tion by @shirou in https://github.com/<br>shirou/gopsutil/pull/1536      **Full <br>Changelog**: https://github.com/shirou<br>/gopsutil/compare/v3.23.9...v3.23.10|
|2023-11-01 08:54:27|[APIKit](https://github.com/API-Security/APIKit)|v1.5.1|1. 美化Do Target API Scan的UI。  2. <br>允许Do Target API Scan时输入多个header<br>，直接换行即可。  3. 修复Do Target API <br>Scan的API Document URL不能带参数的bug<br>。  4. 修复Header重复冲突的问题。|
|2023-11-01 03:30:09|[WeblogicTool](https://github.com/KimJun1010/WeblogicTool)|v1.3|更新记录    - 修复CVE_2020_14882特殊<br>环境下漏报问题  - 修复CVE_2018_2894工作<br>目录路径问题|
|2023-11-01 03:28:43|[afrog](https://github.com/zan8in/afrog)|v2.9.1|### 为了解决2.9.0版本代码优化引发的重<br>大漏洞问题，该漏洞会严重干扰漏洞探测结<br>果，我们强烈建议您立即升级到2.9.1版本，<br>或者使用2.8.9版本或更低版本。  ### 受影<br>响的版本：v2.9.0    ### Added -resume c<br>ommand to resume scanning using the sp<br>ecified afrog-resume.cfg file  ### 新<br>增 -resume 命令，使用指定的 afrog-resum<br>e.cfg 文件恢复扫描    |
|2023-10-31 14:22:43|[trufflehog](https://github.com/trufflesecurity/trufflehog)|v3.62.1|## What's Changed  * update kingpin i<br>mport by @dustin-decker in https://git<br>hub.com/trufflesecurity/trufflehog/pul<br>l/2053  * Re-add detector version by @<br>rosecodym in https://github.com/truffl<br>esecurity/trufflehog/pull/2060  * Dete<br>ctor-Competition-Fix: Fix currencyclou<br>d.com API key by @lc in https://github<br>.com/trufflesecurity/trufflehog/pull/1<br>917  * Detector-Competition-Fix: Fix B<br>itcoin Average detector by @lc in http<br>s://github.com/trufflesecurity/truffle<br>hog/pull/1929  * Detector-Competition-<br>Fix: Update formio regex to match Jwt <br>token by @fumblehool in https://github<br>.com/trufflesecurity/trufflehog/pull/1<br>935  * Detector-Competition-Fix: Fix S<br>alesBlink Detection & Verification by <br>@lc in https://github.com/trufflesecur<br>ity/trufflehog/pull/1950  * Support mu<br>ltiple custom detectors by @rosecodym <br>in https://github.com/trufflesecurity/<br>trufflehog/pull/2064  * [chore] Fix So<br>urceManager flaky test by @mcastorina <br>in https://github.com/trufflesecurity/<br>trufflehog/pull/2059  * Centralize log<br>ic for checking archive extraction too<br>ls by @ahrav in https://github.com/tru<br>fflesecurity/trufflehog/pull/2063     <br> **Full Changelog**: https://github.co<br>m/trufflesecurity/trufflehog/compare/v<br>3.62.0...v3.62.1|
|2023-10-31 06:21:51|[scan4all](https://github.com/hktalent/scan4all)|2.8.7|## Changelog * 4a569aaa fixed dir for<br> windows 2023-10-31 * 57a92842 fixed c<br>onfig/51pwn/yaml/Fortinet FortiOS/ for<br> windows can not build bug 2023-10-31 <br> |
|2023-10-31 03:17:46|[retoolkit](https://github.com/mentebinaria/retoolkit)|2023.10|* Added:      * AutoIt-Ripper      * <br>malduck      * Simple Assembly Explore<br>r (SAE)      * SpeakEasy      * UWPSpy<br>      * XELFViewer    * Changes:      <br>* Windows Update Blocker is now explic<br>tly added as a tool, so users can enab<br>le or disable Windows Updates as they <br>wish. \\]      * retoolkit shortcut mo<br>ved from "Send to" folder to the root <br>of the right click menu. \\]      * Ad<br>ded uninstall icon.|
|2023-10-30 18:16:34|[delve](https://github.com/go-delve/delve)|v1.21.2|  DAP: add concrete type to interface<br> type (@suzmue, #3510)  Support for VS<br>Code in the edit command (@derekparker<br>, #3524)  Follow-mode support for Wind<br>ows (@aarzilli, #3507)      Fix bugs h<br>andling stdout/stderr in DAP (@hyangah<br>, #3522)  Fix bug with autogenerated w<br>rappers for methods of generic types (<br>@aarzilli, #3528)      Use Cgo instead<br> of C code in the FreeBSD backend (@4a<br>6f656c, #3529)  Remove obsolete build <br>tags (+build) (@alexandear, #3513)|
|2023-10-30 07:03:23|[aliyun-oss-python<br>-sdk](https://github.com/aliyun/aliyun-oss-python-sdk)|2.18.3|- 增加：write_get_object_response 接<br>口|
## 近15天commit提交记录
| 提交时间 | 项目名称 | 更新内容 |
| :---- | :---- | :---- |
|2023-11-14 00:40:54|[ImHex](https://github.com/WerWolv/ImHex)|feat: Add color names to color picker view|
|2023-11-14 00:33:52|[notify](https://github.com/nikoksr/notify)|fix(deps): update module github.com/aws/aws-sdk-go-<br>v2/config to v1.24.0 (#751)  Co-authored-by: renovat<br>e[bot] |
|2023-11-14 00:31:01|[PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub)|Auto Update 2023/11/14 00:31:01|
|2023-11-14 00:26:23|[wekan](https://github.com/wekan/wekan)|v7.18|
|2023-11-14 00:00:16|[free](https://github.com/freefq/free)|updated_at 11-14 08:00|
|2023-11-13 23:57:44|[PocOrExp_in_Githu<br>b](https://github.com/ycdxsb/PocOrExp_in_Github)|update 2023-11-14 07:57:44|
|2023-11-13 23:26:36|[ruby](https://github.com/ruby/ruby)|Don't overwrite shape capacity when removing ivar  <br>Other objects may be using the shape, so we can't ch<br>ange the capacity otherwise the other objects may ha<br>ve a buffer overflow.|
|2023-11-13 23:14:41|[python-codext](https://github.com/dhondta/python-codext)|Updated coverage.svg|
|2023-11-13 23:12:23|[cas](https://github.com/apereo/cas)|renovatebot(deps): update dependency urllib3 to v2.<br>1.0    This PR contains the following updates:  | Pa<br>ckage | Change | Age | Adoption | Passing | Confiden<br>ce | |---|---|---|---|---|---| |  () | ==2.0.7 -> ==<br>2.1.0 |  |  |  |  |  ---  ### Release Notes   urllib<br>3/urllib3 (urllib3)  ###     \==================  Re<br>ad the v2 migration guide \__ for help upgrading to <br>the latest version of urllib3.  ## Removals  -   Rem<br>oved support for the deprecated urllib3\. View repos<br>itory job log . |
|2023-11-13 22:50:43|[DIE-engine](https://github.com/horsicq/DIE-engine)|Update module: FormatWidgets 2023-11-13|
|2023-11-13 22:42:22|[containerd](https://github.com/containerd/containerd)|Merge pull request #9358 from thaJeztah/bump_runc_b<br>inary_1.1.10  update runc binary to v1.1.10|
|2023-11-13 22:10:11|[mapcidr](https://github.com/projectdiscovery/mapcidr)|Merge pull request #276 from projectdiscovery/depen<br>dabot/go_modules/main/github.com/projectdiscovery/hm<br>ap-0.0.25|
|2023-11-13 22:06:12|[sdk-api](https://github.com/MicrosoftDocs/sdk-api)|Merge pull request #1683 from DJm00n/patch-10  Upda<br>te nf-rpcdce-uuidtostring.md|
|2023-11-13 21:59:40|[sliver](https://github.com/BishopFox/sliver)|Merge pull request #1455 from BishopFox/go/v1.21.4 <br> Go/v1.21.4|
|2023-11-13 21:58:48|[miniforge](https://github.com/conda-forge/miniforge)|Merge pull request #515 from nsoranzo/patch-1  Fix <br>typo in README.md|
|2023-11-13 21:17:03|[pulumi](https://github.com/pulumi/pulumi)|Auto fill in URNs for parents in import files (#145<br>24)    # Description    This allows you to use the p<br>arent feature in an import file for another resource<br> in the same deployment without having to fill in wh<br>at the URN for that parent resource is in the name t<br>able.  ## Checklist  - [x] I have run make tidy to u<br>pdate any new dependencies - [x] I have run make lin<br>t to verify my code passes the lint check   - [ ] I <br>have formatted my code using gofumpt   - [x] I have <br>added tests that prove my fix is effective or that m<br>y feature works  - [ ] I have run make changelog and<br> committed the changelog/pending/ documenting my cha<br>nge  - [ ] Yes, there are changes in this PR that wa<br>rrants bumping the Pulumi Cloud API version |
|2023-11-13 21:16:33|[compose](https://github.com/docker/compose)|bump golang to version 1.21.4  Signed-off-by: Guill<br>aume Lours |
|2023-11-13 21:10:30|[masscan](https://github.com/robertdavidgraham/masscan)|Update README.md|
|2023-11-13 20:26:43|[zmap](https://github.com/zmap/zmap)|Fixed typos in man pages and --help text (#739)  * <br>phillip/man-pages: fixed typo in --help output    * <br>phillip/man-pages: fixed typo in man pages and re-ge<br>nerated man pages with ronn|
|2023-11-13 20:19:25|[garble](https://github.com/burrowers/garble)|strip struct tags when hashing structs for type ide<br>ntity  This was a long standing TODO, and a user fin<br>ally ran into it. The fix isn't terribly straightfor<br>ward, but I'm pretty happy with it.  Add a test case<br> where the same struct field is identical with no ta<br>g, with the "tagged1" json tag, and again with "tagg<br>ed2". While here, we add a test case for a regular n<br>amed field too.  Fixes #801.|
|2023-11-13 20:19:25|[logging-log4j2](https://github.com/apache/logging-log4j2)|Try fixing FileOutputTest on Windows|
|2023-11-13 19:36:52|[celery](https://github.com/celery/celery)|  Co-authored-by: pre-commit-ci[bot] |
|2023-11-13 19:13:10|[scrapy](https://github.com/scrapy/scrapy)|Updated README.rst (#6144)|
|2023-11-13 18:43:44|[FreeRDP](https://github.com/FreeRDP/FreeRDP)|[build] fix windows build under mingw  The path to <br>resource file was wrong.|
|2023-11-13 18:34:17|[anti-AD](https://github.com/privacy-protection-tools/anti-AD)|Auto renew the anti-AD list.|
|2023-11-13 18:33:09|[spring-framework](https://github.com/spring-projects/spring-framework)|Polish|
|2023-11-13 18:11:55|[console](https://github.com/minio/console)|Added new blog and video content to HelpMenu (#3124<br>)|
|2023-11-13 18:11:48|[monkey](https://github.com/guardicore/monkey)|Ransomware: Move comment to improve clarity|
|2023-11-13 17:46:34|[phpmyadmin](https://github.com/phpmyadmin/phpmyadmin)|Translated using Weblate (Slovenian)  Currently tra<br>nslated at 100.0% (3404 of 3404 strings)  [ci skip] <br> Translation: phpMyAdmin/Development Translate-URL: <br>https://hosted.weblate.org/projects/phpmyadmin/maste<br>r/sl/ Signed-off-by: Domen |
|2023-11-13 17:39:20|[clair](https://github.com/quay/clair)|build(deps): bump github.com/google/uuid from 1.3.1<br> to 1.4.0  Bumps  from 1.3.1 to 1.4.0. -  -  -   ---<br> updated-dependencies: - dependency-name: github.com<br>/google/uuid   dependency-type: direct:production   <br>update-type: version-update:semver-minor ...  Signed<br>-off-by: dependabot[bot] |
|2023-11-13 17:22:05|[locust](https://github.com/locustio/locust)|Merge pull request #2462 from andrewbaldwin44/bugfi<br>x/2399  Replace Updating Stats useEffect Hook with u<br>seInterval|
|2023-11-13 17:17:35|[CotEditor](https://github.com/coteditor/CotEditor)|Fix HeadingMenuItem|
|2023-11-13 16:49:05|[AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)|Pull request 2072: upd-chlog-deps  Squashed commit <br>of the following:  commit fc63c08a89a3eb51da5a31cbb5<br>f15aebb6a498f9 Author: Ainar Garipov  Date:   Mon No<br>v 13 19:22:57 2023 +0300      all: imp chlog  commit<br> 5005d897c2c6128a9b7bc17901d6080870191d4e Author: Ai<br>nar Garipov  Date:   Mon Nov 13 19:18:54 2023 +0300 <br>     all: upd chlog, deps|
|2023-11-13 16:46:59|[LaZagne](https://github.com/AlessandroZ/LaZagne)|Fix #623|
|2023-11-13 16:33:35|[dbeaver](https://github.com/dbeaver/dbeaver)|CB-4015 extract common class for row data receiver <br>(#21819)  Co-authored-by: Daria Marutkina |
|2023-11-13 16:32:18|[PST-Bucket](https://github.com/arch3rPro/PST-Bucket)|easysrv: Update to version 2.2.3|
|2023-11-13 15:57:18|[Mythic](https://github.com/its-a-feature/Mythic)|v3.1.7  Added support for parallelized file chunk d<br>ownloads|
|2023-11-13 15:48:04|[nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)|Auto Template Signing [Mon Nov 13 15:48:03 UTC 2023<br>] :robot:|
|2023-11-13 15:35:44|[goreleaser](https://github.com/goreleaser/goreleaser)|feat(docs): Update command in SLSA verification blo<br>g post (#4420)  Great blog post! I added it to the d<br>ocumentation of the  https://github.com/slsa-framewo<br>rk/slsa-github-generator :)    This PR fixes the com<br>mand to verify SLSA provenance in the blog post  htt<br>ps://goreleaser.com/blog/slsa-generation-for-your-ar<br>tifacts/.    The verification for binary artifacts i<br>s correct.    The verification for container images <br>is incorrect:  - The command verifies the identity o<br>f the builder only, but it should  also verify the s<br>ource repository  - The command does not verify the <br>release version, which _may_ allows an  attacker to <br>perform a downgrade attack. (not a super big deal, b<br>ut still  useful to close this gap if the image was <br>built on a tag trigger)    This follows the same ste<br>ps on argoCD's documentation  https://argo-cd.readth<br>edocs.io/en/stable/operator-manual/signed-release-as<br>sets/#verification-of-container-image-with-slsa-atte<br>stations    Thanks!    ---------    Signed-off-by: l<br>aurentsimon |
|2023-11-13 15:33:53|[rustdesk](https://github.com/rustdesk/rustdesk)|Merge pull request #6358 from basilgello/vcpkg-deps<br>  vcpkg deps|
|2023-11-13 15:17:42|[terraform](https://github.com/hashicorp/terraform)|terraform test: add support for importing overridde<br>n resources (#34216)  * terraform test: add support <br>for importing overridden resources    * fix broken c<br>omment|
|2023-11-13 15:00:16|[dnscrypt-proxy-co<br>nfig](https://github.com/CNMan/dnscrypt-proxy-config)|Mon Nov 13 03:00:16 PM UTC 2023|
|2023-11-13 14:22:53|[pdns](https://github.com/PowerDNS/pdns)|Merge pull request #13191 from rgacogne/use-unique-<br>pointer-for-dir  Wrap DIR* objects in unique pointer<br>s to prevent memory leaks|
|2023-11-13 14:16:51|[LogonTracer](https://github.com/JPCERTCC/LogonTracer)|Supported SQLAlchemy 1.4|
|2023-11-13 14:11:21|[mitmproxy](https://github.com/mitmproxy/mitmproxy)|reopen main for development|
|2023-11-13 13:44:27|[feroxbuster](https://github.com/epi052/feroxbuster)|fixed bug with url parsing; re: devx00|
|2023-11-13 13:18:17|[audacity](https://github.com/audacity/audacity)|Merge remote-tracking branch 'audacity/release-3.4.<br>2' into master|
|2023-11-13 12:36:49|[v2rayfree](https://github.com/aiboboxx/v2rayfree)|update|
|2023-11-13 12:21:04|[codeql-cli-binari<br>es](https://github.com/github/codeql-cli-binaries)|Merge pull request #167 from github/smowton/admin/u<br>pdate-changelog-2.15.2  Update Changelog for 2.15.2 <br>release|
|2023-11-13 12:15:43|[QEMU](https://github.com/qemu/QEMU)|Merge tag 'pull-request-2023-11-13' of https://gitl<br>ab.com/thuth/qemu into staging  * Fix compilation wi<br>th Clang 17 on s390x hosts * Two small s390x PCI fix<br>es * Update MAINTAINERS file with more entries * Fix<br> NetBSD VM test * Clean up some bad wordings  # ----<br>-BEGIN PGP SIGNATURE----- # # iQJFBAABCAAvFiEEJ7iIR+<br>7gJQEY8+q5LtnXdP5wLbUFAmVSAoIRHHRodXRoQHJl # ZGhhdC5<br>jb20ACgkQLtnXdP5wLbVXBg//VVZS5CXEfOFV91I1kqQnLCvgwmu<br>AyqEg # PI2/HBxuhzeBx+F1t7uR0n15tUPi1zkFFBOpyBDBubvW<br>cp4vGvFwLQoiBCUvNzBA # +b1vMySP+K0OO1X5yT3cFHXF9q0o0<br>V5WADwemf5RglIPjlTOIiz9qhD4EYqd2QHC # EUd9Y45DP4Y0V5<br>raHLjY990f/zr3PuSAB6MASFTUnKdgGkRqonLWdLDdIZNDrZuL #<br> oGwx1ALXgBOMV3yNyQx9jZBT24git/ai1vd9AU/d3JRKDPsd+4v<br>C39+PTI9NH4h6 # oQglvo399f64cir1f1JJ3MN4ZtwXZpwUkjeT<br>McR9XZxk7GibU7P2arG5M3TERdmE # VLqylYsnbJojWOeCH+TVi<br>JapRhg1CzUveVlQofr7GHvf2N3oy3BrKaV715gauEyW # zpjbhS<br>PpIQu9WFXt8+tSquqbvpAP/VlLrOV73D4LzJ7WdTa9CHmSek8D0z<br>oRQDZR # 8OixrgoBKS+pmBDmTve5gFsIKhZIz9CrmaAKKYdskC8<br>blENxCng8LOFp7sg2PK3M # U0lWYoDS7qZ85761Bl+QaBdFocda<br>hQqkO/LUQuhoSt2OvA1EGAz2FdVSKkmPDdSS # P/homr4hOXIqJ<br>FSsZj0YNUTIXsXwLBvKjvcJPAWYgbXZhim0LtPQTQO3+ignwGyu <br># RXjaVkvkf/s= # =+2rp # -----END PGP SIGNATURE-----<br> # gpg: Signature made Mon 13 Nov 2023 06:03:30 EST <br># gpg:                using RSA key 27B88847EEE02501<br>18F3EAB92ED9D774FE702DB5 # gpg:                issue<br>r "thuth@redhat.com" # gpg: Good signature from "Tho<br>mas Huth " [full] # gpg:                 aka "Thomas<br> Huth " [full] # gpg:                 aka "Thomas Hu<br>th " [full] # gpg:                 aka "Thomas Huth <br>" [unknown] # Primary key fingerprint: 27B8 8847 EEE<br>0 2501 18F3  EAB9 2ED9 D774 FE70 2DB5  * tag 'pull-r<br>equest-2023-11-13' of https://gitlab.com/thuth/qemu:<br>   hw/audio/es1370: Clean up comment   tests/tsan: R<br>ename the file with the entries that should be ignor<br>ed   test-resv-mem: Fix CID 1523911   tests/vm/netbs<br>d: Use Python v3.11   MAINTAINERS: Add a general arc<br>hitecture section for x86   MAINTAINERS: Extend the <br>Stellaris section   MAINTAINERS: Add hw/display/sii9<br>022.c to the Versatile Express section   MAINTAINERS<br>: Add hw/input/ads7846.c to the PXA2XX section   MAI<br>NTAINERS: Add include/hw/input/pl050.h to the PrimeC<br>ell/CMSDK section   s390x/pci: only limit DMA apertu<br>re if vfio DMA limit reported   s390x/pci: bypass vf<br>io DMA counting when using cdev   host/include/gener<br>ic/host/atomic128: Fix compilation problem with Clan<br>g 17  Signed-off-by: Stefan Hajnoczi |
|2023-11-13 12:08:00|[metasploit-framew<br>ork](https://github.com/rapid7/metasploit-framework)|Land #18524, Update reverse_tcp.md, improper switch<br>es|
|2023-11-13 12:00:32|[etcd](https://github.com/etcd-io/etcd)|Merge pull request #16930 from sharathsivakumar/shs<br>i/bump_deps_8  dependency: bump go.opentelemetry.io/<br>contrib/instrumentation/google.g…|
|2023-11-13 11:07:53|[ImageMagick](https://github.com/ImageMagick/ImageMagick)|Bump azure/azure-code-signing-action from 0.2.21 to<br> 0.2.22  Bumps  from 0.2.21 to 0.2.22. -  -   --- up<br>dated-dependencies: - dependency-name: azure/azure-c<br>ode-signing-action   dependency-type: direct:product<br>ion   update-type: version-update:semver-patch ...  <br>Signed-off-by: dependabot[bot] |
|2023-11-13 10:58:13|[broot](https://github.com/Canop/broot)|version 1.28.1|
|2023-11-13 10:29:17|[upx](https://github.com/upx/upx)|cmake update|
|2023-11-13 10:12:02|[Awesome-Redteam](https://github.com/Threekiii/Awesome-Redteam)|更新README.md|
|2023-11-13 10:09:09|[jumpserver](https://github.com/jumpserver/jumpserver)|perf: 修改默认 ansible_python_interpreter (#12093) <br> Co-authored-by: feng |
|2023-11-13 10:08:19|[DongTai](https://github.com/HXSecurity/DongTai)|Merge pull request #1906 from st1020/fix/schemathes<br>is-workflows  fix: schemathesis workflows|
|2023-11-13 09:59:47|[falco](https://github.com/falcosecurity/falco)|fix(userspace/falco): fix create_dir behaviour  Sig<br>ned-off-by: Roberto Scolaro |
|2023-11-13 09:41:54|[fscan](https://github.com/shadow1ng/fscan)|Update|
|2023-11-13 09:10:52|[MQTTX](https://github.com/emqx/MQTTX)|docs(web): update readme|
|2023-11-13 09:09:41|[ThinkAdmin](https://github.com/zoujingli/ThinkAdmin)|同步更新代码|
|2023-11-13 07:54:38|[APT_REPORT](https://github.com/blackorbird/APT_REPORT)|Add files via upload|
|2023-11-13 07:33:50|[nemo_go](https://github.com/hanc00l/nemo_go)|Update: v2.10.3|
|2023-11-13 07:24:22|[trivy](https://github.com/aquasecurity/trivy)|fix(cli): set correct scanners for k8s target (#556<br>1)|
|2023-11-13 07:19:42|[httpx](https://github.com/projectdiscovery/httpx)|Merge branch 'dev'|
|2023-11-13 06:37:41|[harbor](https://github.com/goharbor/harbor)|fix: sorting quota (#19538)  fix: sort Project Quot<br>as    Signed-off-by: Shengwen Yu |
|2023-11-13 06:33:49|[commix](https://github.com/commixproject/commix)|Trivial update|
|2023-11-13 03:51:46|[404StarLink](https://github.com/knownsec/404StarLink)|weekly update at 20231113|
|2023-11-13 03:49:16|[yakit](https://github.com/yaklang/yakit)|improve yakurl|
|2023-11-13 03:48:29|[fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts)|Merge pull request #22 from aaddmin1122345/master  <br>'directoryDicts'添加dirsearch字典|
|2023-11-12 23:02:33|[nmap](https://github.com/nmap/nmap)|Correct packet size testing in KNX scripts. Fixes #<br>2727, fixes #2728|
|2023-11-12 22:24:45|[theHarvester](https://github.com/laramies/theHarvester)|Fix otx test|
|2023-11-12 21:36:00|[usql](https://github.com/xo/usql)|Updating dependencies|
|2023-11-12 20:08:51|[wabt](https://github.com/WebAssembly/wabt)|wasm2c: Fix test harness UB with SIMD (#2327)|
|2023-11-12 19:40:03|[coreruleset](https://github.com/coreruleset/coreruleset)|Merge pull request #3380 from coreruleset/revert-33<br>79-fix-request-filename  fix: revert PR new rule to <br>set request_filename var|
|2023-11-12 19:38:47|[sqlmap](https://github.com/sqlmapproject/sqlmap)|Fixes #5566|
|2023-11-12 18:22:11|[ctf-archives](https://github.com/sajjadium/ctf-archives)|MCTF chals|
|2023-11-12 18:20:49|[MoreFind](https://github.com/mstxq17/MoreFind)|docs: revise version number|
|2023-11-12 18:20:43|[easy-rsa](https://github.com/OpenVPN/easy-rsa)|Updating OpenSSL to 3.1.4  Signed-off-by: Eric F Cr<br>ist |
|2023-11-12 17:35:49|[fish-shell](https://github.com/fish-shell/fish-shell)|Replaced double quotation marks with single in dnf.<br>fish completions|
|2023-11-12 17:21:16|[PayloadsAllTheThi<br>ngs](https://github.com/swisskyrepo/PayloadsAllTheThings)|Merge pull request #692 from jlkl/master  Add two m<br>ethods about LFI to RCE via PHP PEARCMD|
|2023-11-12 14:56:06|[ezXSS](https://github.com/ssl/ezXSS)|Retrieve reports using archive status|
|2023-11-12 13:08:08|[fzf](https://github.com/junegunn/fzf)|0.44.0|
|2023-11-12 12:33:23|[v2rayA](https://github.com/v2rayA/v2rayA)|docker_helper.sh: Fix creating softlink|
|2023-11-12 12:29:34|[aria2](https://github.com/aria2/aria2)|Merge pull request #2132 from aria2/docker-bump-car<br>es  Dockerfile: Bump c-ares to 1.21.0|
|2023-11-12 11:01:21|[delve](https://github.com/go-delve/delve)|pkg/proc: unskip passing tests and reorganize (#356<br>1)|
|2023-11-12 09:44:33|[dalfox](https://github.com/hahwul/dalfox)|Merge pull request #507 from hahwul/dependabot/go_m<br>odules/golang.org/x/term-0.14.0  Bump golang.org/x/t<br>erm from 0.13.0 to 0.14.0|
|2023-11-12 08:47:01|[kube-bench](https://github.com/aquasecurity/kube-bench)|build(deps): bump github.com/fatih/color from 1.14.<br>1 to 1.16.0 (#1520)  Bumps  from 1.14.1 to 1.16.0.  <br>-   -     ---  updated-dependencies:  - dependency-n<br>ame: github.com/fatih/color    dependency-type: dire<br>ct:production    update-type: version-update:semver-<br>minor  ...    Signed-off-by: dependabot[bot]   Co-au<br>thored-by: dependabot[bot] |
|2023-11-12 08:32:49|[DSInternals](https://github.com/MichaelGrafnetter/DSInternals)|GitHub Dark Theme Support|
|2023-11-12 08:05:43|[domain_hunter_pro](https://github.com/bit4woo/domain_hunter_pro)|Update LineTableModel.java|
|2023-11-12 06:55:05|[Search_Viewer](https://github.com/G3et/Search_Viewer)|Update Search_Viewer.py|
|2023-11-12 05:03:47|[gmpy](https://github.com/aleaxit/gmpy)|Merge pull request #455 from skirpichev/docs  Impro<br>ve sphinx documentation|
|2023-11-12 03:07:34|[gmhelper](https://github.com/ZZMarquis/gmhelper)|尽量再兼容一下Java7|
|2023-11-12 02:24:25|[druid](https://github.com/alibaba/druid)|修复解析PARTITION OF导致OracleCreateTableTest11跑失<br>败的问题  修复解析PARTITION OF导致OracleCreateTableTe<br>st11跑失败的问题|
|2023-11-12 01:37:03|[gopsutil](https://github.com/shirou/gopsutil)|Merge pull request #1551 from blinklabs-io/feat/use<br>-lsof-freebsd-connections  feat: use lsof for net_co<br>nnections on FreeBSD|
|2023-11-12 00:23:53|[ttyd](https://github.com/tsl0922/ttyd)|update manual (#1246)|
|2023-11-11 17:05:27|[dnsx](https://github.com/projectdiscovery/dnsx)|dep update|
|2023-11-11 16:37:37|[werkzeug](https://github.com/pallets/werkzeug)|Merge branch '3.0.x'|
|2023-11-11 15:14:47|[autoDecoder](https://github.com/f0ng/autoDecoder)|Update README.md|
|2023-11-11 14:30:19|[signature-base](https://github.com/Neo23x0/signature-base)|fix: IOCs without score|
|2023-11-11 13:35:36|[Nuitka](https://github.com/Nuitka/Nuitka)|New pre-release.|
|2023-11-11 09:21:47|[glances](https://github.com/nicolargo/glances)|Alerts showing different time than time plugin #221<br>4|
|2023-11-11 09:08:23|[sharry](https://github.com/eikek/sharry)|Merge pull request #1241 from eikek/update-java  Up<br>date java to jdk17|
|2023-11-11 06:50:07|[neuvector](https://github.com/neuvector/neuvector)|Merge pull request #1091 from holyspectral/dismiss-<br>gosaml2-false-positive  NVSHAS-7616 dismiss false po<br>sitive on dependabot|
|2023-11-11 03:02:53|[syft](https://github.com/anchore/syft)|Fall back to searching maven central using groupIDF<br>romJavaMetadata (#2295)  Signed-off-by: Colm O hEige<br>artaigh |
|2023-11-11 00:01:21|[openrasp](https://github.com/baidu/openrasp)|Merge pull request #444 from baidu/dependabot/npm_a<br>nd_yarn/rasp-vue/fsevents-1.2.13  Bump fsevents from<br> 1.2.9 to 1.2.13 in /rasp-vue|
|2023-11-10 22:29:54|[jadx](https://github.com/skylot/jadx)|fix(plugin): check for valid identifiers from Kotli<br>n metadata (PR #2041)|
|2023-11-10 21:51:13|[stratus-red-team](https://github.com/DataDog/stratus-red-team)|Bump actions/setup-go from 4.0.1 to 4.1.0 (#404)  B<br>umps  from 4.0.1 to 4.1.0.  -   -     ---  updated-d<br>ependencies:  - dependency-name: actions/setup-go   <br> dependency-type: direct:production    update-type: <br>version-update:semver-minor  ...    Signed-off-by: d<br>ependabot[bot]   Co-authored-by: dependabot[bot] |
|2023-11-10 19:29:37|[jd](https://github.com/josephburnett/jd)|Add diff and Bash syntax highlighting to README.md <br>(#60)|
|2023-11-10 18:52:14|[wesng](https://github.com/bitsadmin/wesng)|Updated 20231110|
|2023-11-10 18:12:39|[bandit](https://github.com/PyCQA/bandit)|Add official support of Python 3.12 (#1068)  Python<br> 3.12 was released on Monday Oct 2. Bandit should be<br> built  and tested on this version going forward.   <br> Signed-off-by: Eric Brown |
|2023-11-10 17:01:31|[tabby](https://github.com/Eugeny/tabby)|Revert "fixes"  This reverts commit 4c0231cd67822df<br>c368cbe0000ab884dd25f898f.|
|2023-11-10 16:54:32|[ProcDump-for-Linu<br>x](https://github.com/Sysinternals/ProcDump-for-Linux)|Update ProcDump to use cmake rather than make (#218<br>)  * Move to CMake check-point    * Update build and<br> contributing docs    * Add cmake to pre-reqs    * u<br>pdate path|
|2023-11-10 16:21:15|[faker](https://github.com/joke2k/faker)|Bump version: 19.13.0 → 20.0.0|
|2023-11-10 16:18:30|[pyscript](https://github.com/pyscript/pyscript)|Add Deprecation message when loading from latest (#<br>1848)  * add tests to verify if we show an error ban<br>ner when users load from latest    * add deprecation<br> manager to take care of showing a notification in c<br>ase script src is being loaded from latest    * [pre<br>-commit.ci] auto fixes from pre-commit.com hooks    <br>for more information, see https://pre-commit.ci    *<br> make sure deprecation warning also register onWorke<br>r    * restore tests for banner in worker    * [pre-<br>commit.ci] auto fixes from pre-commit.com hooks    f<br>or more information, see https://pre-commit.ci    * <br>add a wait selector when testing banner since worker<br> seems to take too long to render in CI    * [pre-co<br>mmit.ci] auto fixes from pre-commit.com hooks    for<br> more information, see https://pre-commit.ci    * Fi<br>x test_deprecate_loading_scripts_from_latest: I thin<br>k that the  previous failure was because we actually<br> TRIED to execute the js from  latest/core.js and it<br> conflicted with our local copy.    But to trigger t<br>he warning is enough to have a script pointing to  p<br>yscript.net/latest, there is no need to execute it: <br>modify it with  type="ignore-me" and an URL which do<br>esn't exist.    ---------    Co-authored-by: pre-com<br>mit-ci[bot]   Co-authored-by: Antonio Cuni |
|2023-11-10 14:40:08|[static-analysis](https://github.com/analysis-tools-dev/static-analysis)|Commit list|
|2023-11-10 14:00:23|[ioc](https://github.com/avast/ioc)|Merge pull request #56 from BraKram/clearfake  clea<br>rfake 11 2023|
|2023-11-10 13:54:18|[RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)|Change uncipher to decrypt. issue 398|
|2023-11-10 13:14:27|[apollo](https://github.com/apolloconfig/apollo)|Apply audit log functions to portal using audit-log<br> module (#5008)  * Fix serious appendDataInfluence b<br>ug in AuditSpanAspect.    Add patch of dealing with <br>collection-type arg when AOP capturing input paramet<br>er for "AnyMatched".    * Fix front-end bugs.    * F<br>ix front-end bugs and Enhance front-end styles.    *<br> rawly implement basic needs in issue    * implement<br> basic needs in issue    * Optimize code structure a<br>nd add unit test for ApolloAuditSpanAspect.    * add<br> license    * update ApolloAuditSpanAspect|
|2023-11-10 12:31:31|[rengine](https://github.com/yogeshojha/rengine)|Merge pull request #1029 from luizmlo/patch-1  Adde<br>d tooltip text to dashboard total vulnerabilities to<br>oltip|
|2023-11-10 10:38:32|[gotestwaf](https://github.com/wallarm/gotestwaf)|Add information about test result to report (#219) <br> * Add information about test result to report    * <br>Small improvements    * Small improvements|
|2023-11-10 09:27:18|[safeline](https://github.com/chaitin/safeline)|fix(fe): missing install count|
|2023-11-10 08:49:11|[f8x](https://github.com/ffffffff0x/f8x)|update(2023/11/10)|
|2023-11-10 08:00:28|[bat](https://github.com/sharkdp/bat)|Consider adding ?exclude_unsupported=1 to repology <br>badge|
|2023-11-10 07:15:04|[trash-cli](https://github.com/andreafrancia/trash-cli)|Bump version to '0.23.11.10'|
|2023-11-10 03:36:23|[Online_tools](https://github.com/Zhao-sai-sai/Online_tools)|0.4.0文件下载错修复|
|2023-11-10 00:55:01|[FrameVul](https://github.com/Awrrays/FrameVul)|Update README.md|
|2023-11-09 22:34:11|[psutil](https://github.com/giampaolo/psutil)|fix #2325: fix compilation on PyPy|
|2023-11-09 22:34:01|[yq](https://github.com/mikefarah/yq)|Fixes dos line separator issue when reading express<br>ion file #1860|
|2023-11-09 20:42:15|[rundeck](https://github.com/rundeck/rundeck)|Merge pull request #8676 from rundeck/RCLOUD-1046-m<br>aint  Small tweaks to execution and notification ser<br>vices for RCLOUD-1046|
|2023-11-09 17:48:08|[trufflehog](https://github.com/trufflesecurity/trufflehog)|Adding Sumo Logic how to rotate (#2103)|
|2023-11-09 17:40:54|[suricata](https://github.com/OISF/suricata)|http2: update brotli crate  Fixes debug assertion f<br>ound by oss-fuzz: https://bugs.chromium.org/p/oss-fu<br>zz/issues/detail?id=63144|
|2023-11-09 16:08:22|[grype](https://github.com/anchore/grype)|chore(deps): update bootstrap tools to latest versi<br>ons (#1595)  Signed-off-by: GitHub   Co-authored-by:<br> westonsteimel |
|2023-11-09 14:56:42|[croc](https://github.com/schollz/croc)|bump 9.6.6|
|2023-11-09 14:54:17|[glpi](https://github.com/glpi-project/glpi)|fix(ticket): followup display|
|2023-11-09 14:06:58|[asnmap](https://github.com/projectdiscovery/asnmap)|Merge branch 'dev'|
|2023-11-09 13:41:46|[FiraCode](https://github.com/tonsky/FiraCode)|Update Notepad++ instructions link #1555|
|2023-11-09 12:43:57|[photon](https://github.com/vmware/photon)|createrepo_c: bump version after rpm upgrade  Chang<br>e-Id: I5670de37140a6aab509022d5035127262148eb72 Sign<br>ed-off-by: Shreenidhi Shedi  Reviewed-on: http://pho<br>ton-jenkins.eng.vmware.com:8082/c/photon/+/22332 Tes<br>ted-by: gerrit-photon |
|2023-11-09 12:04:42|[all-in-one-v2](https://github.com/zaivanza/all-in-one-v2)|change data to datas|
|2023-11-09 11:03:40|[yara](https://github.com/VirusTotal/yara)|Add missing data file to BUILD.bazel|
|2023-11-09 10:25:36|[PostgresApp](https://github.com/PostgresApp/PostgresApp)|Release Postgres.app 2.6.8|
|2023-11-09 09:19:27|[nacos](https://github.com/alibaba/nacos)|Develop refactor topn (#11352)  * Move topn to core<br> module.    * StringTopNCounter replace TopnCounterM<br>etricsContainer.java    * Use ServiceTopNCounter rep<br>lace StringTopNCounterTest for naming.    * Use Fixe<br>dSizePriorityQueue replace PriorityQueue to save mem<br>ory.    * For PMD.|
|2023-11-09 02:26:35|[aliyun-cli](https://github.com/aliyun/aliyun-cli)|Bump golang.org/x/crypto from 0.14.0 to 0.15.0  Bum<br>ps  from 0.14.0 to 0.15.0. -   --- updated-dependenc<br>ies: - dependency-name: golang.org/x/crypto   depend<br>ency-type: direct:production   update-type: version-<br>update:semver-minor ...  Signed-off-by: dependabot[b<br>ot] |
|2023-11-09 00:09:38|[list](https://github.com/publicsuffix/list)|Update public_suffix_list.dat (#1848)  The company <br>structure has changed from a general partnership (OG<br>) to a limited liability company (GmbH). Please refe<br>r to: https://www.futureweb.at/de/impressum/ for mor<br>e details.|
|2023-11-08 23:23:17|[alive-progress](https://github.com/rsalmei/alive-progress)|bump version|
|2023-11-08 21:06:26|[shellcheck](https://github.com/koalaman/shellcheck)|Merge pull request #2837 from ulidtko/fix/missed-te<br>st(1)-bashisms  Fix: extend []-related bashism check<br>s on test calls too|
|2023-11-08 20:20:09|[volatility3](https://github.com/volatilityfoundation/volatility3)|Merge pull request #1024 from volatilityfoundation/<br>feature/citation  Documentation: Add in a CITATION.c<br>ff file|
|2023-11-08 17:57:11|[malleable-c2](https://github.com/threatexpress/malleable-c2)| cs4.9 updates (#19)|
|2023-11-08 17:44:21|[fyne](https://github.com/fyne-io/fyne)|add myself to github sponsors|
|2023-11-08 16:59:46|[filebrowser](https://github.com/filebrowser/filebrowser)|fix: set correct port in docker healthcheck (#2812)<br>  When the FB_PORT environment variable is set, resp<br>ect its value. Otherwise, pick the port from the con<br>figuration.|
|2023-11-08 16:57:20|[Damn-Vulnerable-G<br>raphQL-Application](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application)|Merge pull request #81 from thomas-serre-sonarsourc<br>e/master  Add __init__.py files in core and db folde<br>r|
|2023-11-08 16:08:28|[impacket](https://github.com/fortra/impacket)|Handle unknown NTSTATUS in SessionError (#1311)  * <br>Handle unknown NTSTATUS in SessionError    * Handle <br>unknown NTSTATUS in other places|
|2023-11-08 15:42:15|[iDefender](https://github.com/wecooperate/iDefender)|update|
|2023-11-08 13:37:49|[git-lfs](https://github.com/git-lfs/git-lfs)|Merge pull request #5555 from bk2204/remote-ssh-pro<br>tocol  Allow configuring the SSH protocol|
|2023-11-08 11:43:38|[rich](https://github.com/Textualize/rich)|Fix issue with trailing whitespace (#3195)  * chore<br>: upgrade all pre-commit hooks to latest version    <br>* chore: add trailing-whitespace pre-commit hook    <br>* refactor: Avoid trailing whitespace in box definit<br>ions    * docs: Add Robin Bowes as a contributor    <br>---------    Co-authored-by: Robin Bowes |
|2023-11-08 11:40:11|[openvpn-install](https://github.com/Nyr/openvpn-install)|Update README.md|
|2023-11-08 09:28:46|[ghauri](https://github.com/r0oth3x49/ghauri)|updated readme with latest version..|
|2023-11-08 09:27:13|[naxsi](https://github.com/nbs-system/naxsi)|Project status update. (#631)|
|2023-11-08 08:20:07|[HFish](https://github.com/hacklcx/HFish)|update|
|2023-11-08 07:00:36|[oss-browser](https://github.com/aliyun/oss-browser)|Merge pull request #474 from aliyun/csg/fix/develop<br>/53081334  fix: unable to load more objects after se<br>tting the maximum number of listed objects|
|2023-11-08 06:09:01|[PeiQi-WIKI-Book](https://github.com/PeiQi0/PeiQi-WIKI-Book)|Merge branch 'main' of github.com:PeiQi0/PeiQi-WIKI<br>-Book|
|2023-11-08 03:15:06|[ihoneyBakFileScan<br>_Modify](https://github.com/VMsec/ihoneyBakFileScan_Modify)|Update README.md|
|2023-11-08 01:55:24|[LOLBAS](https://github.com/LOLBAS-Project/LOLBAS)|Adding GitHub Actions workflow test for duplicate f<br>ilenames (#340)  * Adding GitHub Actions workflow te<br>st for duplicate filenames    * Adding generic error<br> message    * Deduping fsutil.exe and teams.exe|
|2023-11-07 19:43:35|[wpscan](https://github.com/wpscanteam/wpscan)|Merge pull request #1814 from wpscanteam/fix/non-la<br>tin-character-slugs  Fix case where a theme slug is <br>all non-latin characters|
|2023-11-07 18:29:50|[fd](https://github.com/sharkdp/fd)|Merge pull request #1421 from acuteenvy/fix-no-colo<br>r  fix: display color when NO_COLOR is an empty stri<br>ng|
|2023-11-07 17:46:33|[node-red](https://github.com/node-red/node-red)|Merge pull request #4416 from node-red/mqtt-check-t<br>opic-length  check topic length > 0 before publish|
|2023-11-07 16:04:17|[OneScan](https://github.com/vaycore/OneScan)|更新版本号为1.4.0；更新说明文档和部分截图|
|2023-11-07 15:40:26|[soapui](https://github.com/SmartBear/soapui)|Merge pull request #786 from SmartBear/release-5.7.<br>2  Update SoapUI version to 5.7.2|
|2023-11-07 13:15:52|[ModSecurity](https://github.com/SpiderLabs/ModSecurity)|Merge pull request #3014 from martinhsv/v3/master  <br>Fix: validateDTD compile fails if when libxml2 not i<br>nstalled|
|2023-11-07 12:40:00|[sm-crypto](https://github.com/JuneAndGreen/sm-crypto)|update: README.md|
|2023-11-07 12:16:48|[ARL](https://github.com/TophantTechnology/ARL)|Merge pull request #652 from chushuai/patch-1  360Q<br>uake子域名查询优化|
|2023-11-07 10:53:08|[heapdump_tool](https://github.com/wyzxxz/heapdump_tool)|Update README.md|
|2023-11-07 07:12:38|[csprecon](https://github.com/edoardottt/csprecon)|Merge pull request #140 from edoardottt/devel  Deve<br>l update|
|2023-11-07 07:03:52|[pdfparser](https://github.com/smalot/pdfparser)|Major Update to PDFObject.php + Ancillary (#634)  *<br> Rewrite PDFObject.php + ancillary    This is a majo<br>r update to the PHPObject.php file. Where previously<br> PdfParser would attempt to gather document stream d<br>ata using a series of multiline regular expressions,<br> this update changes the behaviour of cleanContent()<br> to the following:  - Hide all (strings)  - Remove a<br>ll newlines and carriage-returns  - Hide all >  - No<br>rmalize all whitespace  - Using a list of valid Oper<br>ators from the PDF Reference, add \r\n back to the r<br>emaining text so that there is a single PDF command <br>on every line  - Restore the > and (strings)    By u<br>sing this system, it is then much easier to examine <br>and parse the document stream in a line-by-line mann<br>er, instead of PREG extraction. getSections() text h<br>as been updated to do just this, stepping through th<br>e output of cleanContent() line-by-line and returnin<br>g an array of only the relevant commands needed to p<br>osition and display text.    The guts of getText() h<br>ave been moved to getTextArray() to reduce code dupl<br>ication. getTextArray() now takes into account both <br>the current graphics position cm and the scaling fac<br>tors of the text matrix Tm when adding \n and \t whi<br>tespace for positioning. Positioning is only taken i<br>nto account at the point of inserting text, rather t<br>han whenever a Tm or Td/TD was found.    It also tre<br>ats Q and q as a stack of stored states rather than <br>a single stored state.    The presence of ActualText<br> BDC commands is also taken into account and the con<br>tents of the ActualText will replace the formerly ou<br>tput text in both content and position. This require<br>s the new parseDictionary() method to reliably extra<br>ct such commands as well as any others PdfParser may<br> take into account in the future.    decodeText() in<br> **Font.php** now takes into account the current tex<br>t matrix when considering whether or not to add spac<br>es between words. Instead of implode()-ing the resul<br>t array with a space joiner, rely on the positioning<br> check to add all required spacing.    In decodeCont<br>ent() in **Font.php** add a check to see if the stri<br>ng to decode has the UTF-16BE BOM and decode it dire<br>ctly as Unicode if so.    * Add test, check for text<br>/plain    Add a unit test for correctly decoding an <br>emdash in Cyrillic text. Use sample PDF from issue h<br>ttps://github.com/smalot/pdfparser/issues/585 User @<br>se-ti allowed use of this file in issue https://gith<br>ub.com/smalot/pdfparser/issues/586#issuecomment-1634<br>361636    In cleanContent() once all strings and dic<br>tionaries are hidden, do a MIME-type check on the re<br>maining content. If it doesn't register as text/plai<br>n, then return an empty string. This prevents non-do<br>cument-stream data from being passed to cleanContent<br>() such as JPEG data in file '12249.pdf' from https:<br>//github.com/smalot/pdfparser/issues/458    Remove w<br>hitespace-adding code from **Font.php**. I originall<br>y added this code as a "shim" because decodeText() d<br>id not take into account the current Text Matrix whe<br>n considering what counted as "words". Now that it d<br>oes, the previous code of just implode()-ing with a <br>space character works.    * Modify some code comment<br>s + q and Q update    Modify several code comments t<br>o be clearer.    Remove the $key =>  from decodeText<br>() in **Font.php** as it's no longer needed.    Also<br>, now that cleanContent() is ignoring non text/plain<br> content, there should be no errant q or Q commands <br>that cause the stored-state stack to try restoring a<br> state that doesn't exist. Remove the kludgy code th<br>at prevented this.    * Update Font.php    Remove un<br>necessary $whitespace line.    * PHP-cs-fixer edits <br>   * Address some reviewed changes    * Use text mat<br>rix 'i' instead of 'b'    The correct matrix element<br>s to use for scaling the x-axis are actually the fir<br>st *column*, so 'a' and 'i', not 'a' and 'b'. My bad<br>! It worked before because almost always the x-axis <br>scaling is equal to the y-axis scaling.    * Use mb_<br>detect_encoding() instead of finfo()    The Fileinfo<br> functions are not installed by default on Windows, <br>so use a different method to determine whether the s<br>tream is valid or binary.    * Update Font.php    PH<br>P CS Fixer native_function_invocation    * Sort swit<br>ch statement cases in getTextArray()    Make the cas<br>es a little bit more alphabetical. Remove cases/comm<br>ands that aren't relevant to getting and positioning<br> text.    * Edit documentation comments, add tests  <br>  Add some documentation comment text to PDFObject.p<br>hp and fix a comment typo in Font.php.    Add a test<br> accounting for text-matrix scaling in Font::decodeT<br>ext().    Add a test verifying that a string prefixe<br>d by a UTF-16BE BOM is decoded directly by Font::dec<br>odeContent().    Move "ET in font name" test from te<br>stCleanContent() to testGetSectionsText() as that is<br> the function the test uses.    Add a test that veri<br>fies cleanContent() returns an empty string for bina<br>ry content.    Remove unnecessary variable reset fro<br>m ET command in Page::getDataTm. Only needed under B<br>T.    * Update ParserTest.php    Add a fixed numeric<br>al value instead of a multiple of $baselineMemory so<br> there's less dependence on the initial memory value<br> and more focus on how much memory the loading of th<br>e PDF actually takes. Hopefully fixes the last unit-<br>test failure?    Change tests to assertGreaterThan a<br>nd assertLessThan so it provides better failure info<br> than just assertTrue (will tell us the values).    <br>In my PHP 8.2.7 test env, the $usedMemory exceeds $b<br>aselineMemory by ~209,000,000 bytes at this point (l<br>ine 379). 180,000,000 should be safe?    * Restore o<br>riginal cleanContent()    Rename the new function fo<br>rmatContent() and restore the original cleanContent(<br>) function and tests. If anyone relied on these func<br>tions before then this will not be a backwards incom<br>patible change.    * added a few PDFs generated with<br> various tools to check conformance    * fixed CS is<br>sue    * Remove textMatrix from decodeText()    As i<br>t turns out, the current text matrix *can* be used t<br>o position text in decodeText(), but it is actually <br>applied **both** to the $offset and the user-selecte<br>d font space limit. In this way it cancels out, and <br>importing the text matrix into the function is not n<br>ecessary. Remove two tests in FontTest.php that were<br> associated with this, as they're no longer valid.  <br>  In decodeText() account for strings of text that h<br>ave spaces with large offsets, such as  'a    line  <br>  of    text    that    is    full-width    justifie<br>d.'  Treat these as single spaces instead of honouri<br>ng the offsets given and spacing them out unnecessar<br>ily.    Save and use the current font-size when gues<br>sing the "fudge" factor for text block width. Make s<br>ure this is saved as well when the q command is seen<br>.    Adjust the position factor threshold up from 10<br> to 24 for deciding when to insert tabs or spaces.  <br>  Also update the current horizontal position when s<br>toring the last-written-position for use by an Actua<br>lText.    Add a test for Microsoft Print-to-PDF v1.7<br>.    This change actually reverts the output value i<br>n a ParserTest assertion back to the original value <br>before this PR. So that's good!    * Account for tex<br>t leading, font-size factor    Keep track of, and ac<br>count for, the current text leading (space between l<br>ines) value when determining whether or not to inser<br>t newlines \n.    Use the current font size as a fac<br>tor in determining whether or not to insert position<br>ing whitespace.    Take more care wrt adding whitesp<br>ace. Examine some points where whitespace might be a<br>dded, and remove it if it's unnecessary. Implode wor<br>ds in Font.php, but examine the words to see if they<br> already have space characters on their fronts and e<br>nds.    TD and Td "move to the start of the next lin<br>e" so use a $current_position_td['x'] of zero (0) to<br> start with. This change shouldn't really affect muc<br>h since enough of a y-axis leading should be added t<br>hat a newline \n results.    In Integration\FontTest<br>.php remove "group linux-only" from testDecodeTextFo<br>rFontWithIndirectEncodingWithoutTypeEncoding() as th<br>is now succeeds in any environment. Before where Pdf<br>Parser was adding spaces after the "zůstatek:" lines<br> whereas now PdfParser adds tabs, which makes far mo<br>re sense when looking at the document /samples/bugs/<br>PullRequest500.pdf So change the expected results to<br> match the output.    * Update FontTest.php    Don't<br> use HEREDOC syntax to compose the expected value fo<br>r the testDecodeTextForFontWithIndirectEncodingWitho<br>utTypeEncoding() test in FontTest.php. This should a<br>llow it to work regardless of the PHP file line-endi<br>ngs.    * Misc fixes    - When assigning $current_te<br>xt_leading, take the negative as described in the PD<br>F Reference. Initialize it to zero, also as in the R<br>eference.  - Add back $current_position_td['x'] when<br> considering a Td or TD command as this appears to b<br>e the way it's supposed to be handled according to t<br>he reference.  - Add another check to remove unneces<br>sary whitespace by examining the previous string of <br>text for a trailing space.  - $current_position_tm['<br>x'] and $current_position_tm['y'] aren't tested for <br>an initial false value, so initialize them to 0.  - <br>Use double null bytes to implode the string in Font.<br>php to avoid catching UTF-8 bytes that might include<br> a single null byte.  - Base the text-box width gues<br>s on the current font size instead of a constant val<br>ue of 4.    - In PageTest.php, PdfParser now correct<br>ly inserts a newline between Aardappelen and Zak, so<br> change the test.  - In ParserTest.php, we are now r<br>emoving unnecessary whitespace, including double spa<br>ces, so change this test to match the output. (Doubl<br>e spaces changed to single spaces)    * Add SmallPDF<br> sample PDF and unit test    * Pass horizontal fontF<br>actor to decodeText()    Pass the fontFactor value (<br>font size multiplied by the text-matrix scale value)<br> to decodeText() so it can more accurately separate <br>text into words by position. A font factor divided b<br>y four seems to give the best results for both horiz<br>ontal and vertical positioning, although this value <br>is selected arbitrarily.    In Font::decodeText() so<br>me PDFs may have text-matrix scale values so large t<br>hat directly encoded horizontal tabs are used in pla<br>ce of spaces. Remove internal tabs from texts and re<br>place them with plain spaces.    * Update PDFObject.<br>php    Restore the $offset parameter to public funct<br>ion getCommandsText() for backwards compatibility.  <br>  * moved new PDFs into special folder    adapted pa<br>ths in tests    * split DocumentTest class    spit i<br>nto a general one, one that is issue related and  on<br>e which is PDF generator related    * added 3 PDFs g<br>enerated by different generators + tests    * More a<br>ccounting for horizontal font factor    Account for <br>the entire font-factor (font-size multiplied by the <br>horizontal scaling factor of the text-matrix) when e<br>stimating the width of the current text block.    In<br>sert a fix when decoding octal strings in Font::deco<br>deOctal(), check further ahead for escaped backslash<br>es.    Remove tests for images in DocumentGeneratorF<br>ocusTest.php. These also fail in the current v2.7.0 <br>release and they should be looked at in a separate P<br>R.    * Revert decodeOctal(), add @internal    Rever<br>t the change to Font::decodeOctal() as it's been sup<br>erceded by PR #640.    Add @internal notes to format<br>Content() and parseDictionary().    * Proper use of <br>PHPDoc "internal"    The @internal tag hides the con<br>tent that comes _after_ it from the documentation, s<br>o adjust these comments as appropriate. See: https:/<br>/manual.phpdoc.org/HTMLSmartyConverter/HandS/phpDocu<br>mentor/tutorial_tags.internal.pkg.html    * Disable <br>a failing test    This test will succeed once PR #64<br>0 is merged. It doesn't have anything to do with the<br> current PR, so disable it for now.    * Update PDFO<br>bject.php    Switch to tagging method for @internal.<br> Adjust comments.    * Update PDFObject.php    PHP-C<br>S-Fixer requires spaces between @ statements I guess<br>.    * Return empty array if no valid command detect<br>ed    In some edge cases, the formatContent() method<br> may return a document stream row containing an inva<br>lid command. Make sure we just ignore these commands<br> instead of triggering warnings for missing $matches<br> array elements.    * Update DocumentGeneratorFocusT<br>est.php    Re-enable this assertion, now that we hav<br>e merged #640.    * Make formatContent() private    <br>Make the formatContent() method private to PDFObject<br> so that @internal isn't required. Adjust the unit t<br>ests with ReflectionMethod to account for this.    -<br>--------    Co-authored-by: Konrad Abicht |
|2023-11-07 07:01:17|[VolatilityPro](https://github.com/Tokeii0/VolatilityPro)|Update README.md|
|2023-11-07 06:13:46|[ILSpy](https://github.com/icsharpcode/ILSpy)|Merge pull request #3111 from ElektroKill/fix/debug<br>-customdebuginfo-browser|
|2023-11-07 02:48:45|[grafanaExp](https://github.com/A-D-Team/grafanaExp)|add source code|
|2023-11-07 02:14:07|[color](https://github.com/gookit/color)|build(deps): bump golang.org/x/sys from 0.13.0 to 0<br>.14.0 (#77)|
|2023-11-07 02:03:50|[Elkeid](https://github.com/bytedance/Elkeid)|Merge pull request #551 from bytedance/fix-re_match<br>  Fix re match|
|2023-11-06 22:27:01|[csvtk](https://github.com/shenwei356/csvtk)|concat: fix the panic when no data given|
|2023-11-06 20:43:24|[CSS-Exchange](https://github.com/microsoft/CSS-Exchange)|Merge pull request #1872 from Shanefe/CalLogSummary<br>AutoUpdate  Add AutoUpdate Code|
|2023-11-06 17:34:10|[interactsh](https://github.com/projectdiscovery/interactsh)|Adding a newline to re-render the README (#707)|
|2023-11-06 16:26:44|[fingerprintx](https://github.com/praetorian-inc/fingerprintx)|Merge pull request #27 from praetorian-inc/golint-f<br>ix  golint fix|
|2023-11-06 13:56:48|[afrog](https://github.com/zan8in/afrog)|fix set-cookie|
|2023-11-06 09:36:07|[emp3r0r](https://github.com/jm33-m0/emp3r0r)|upgrade go version in release-please action|
|2023-11-06 08:25:55|[color](https://github.com/fatih/color)|Merge pull request #213 from fatih/dependabot/go_mo<br>dules/golang.org/x/sys-0.14.0  Bump golang.org/x/sys<br> from 0.13.0 to 0.14.0|
|2023-11-06 03:24:23|[vulnerability](https://github.com/lal0ne/vulnerability)|CVE-2023-46604|
|2023-11-06 02:51:48|[frp](https://github.com/fatedier/frp)|Code refactoring related to message handling and re<br>try logic. (#3745)|
|2023-11-05 22:39:25|[merlin](https://github.com/Ne0nd0g/merlin)|Updated CHANGELOG.MD v2.0.0 date|
|2023-11-05 21:01:49|[dnSpy](https://github.com/dnSpyEx/dnSpy)|Update dnlib to 4.3.0|
|2023-11-05 18:36:23|[spiderfoot](https://github.com/smicallef/spiderfoot)|sfwebui: Update jQuery 3.6.0 to 3.7.1 (#1822)|
|2023-11-05 17:10:09|[lsassy](https://github.com/Hackndo/lsassy)|Build only on merge|
|2023-11-05 08:22:46|[CTF-QuickStart](https://github.com/ProbiusOfficial/CTF-QuickStart)|Update README.md|
|2023-11-05 06:27:53|[Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)|Merge branch 'main' of https://github.com/hiroi-sor<br>a/Umi-OCR  # Conflicts: # README.md|
|2023-11-05 05:03:51|[gshark](https://github.com/madneal/gshark)|Update release.yml|
|2023-11-05 03:49:11|[K8tools](https://github.com/k8gege/K8tools)|Add files via upload|
|2023-11-05 03:42:03|[Ladon](https://github.com/k8gege/Ladon)|Add files via upload|
|2023-11-04 18:48:02|[weird_proxies](https://github.com/GrrrDog/weird_proxies)|test|
|2023-11-04 17:33:59|[Windows11_Hardeni<br>ng](https://github.com/beerisgood/Windows11_Hardening)|23H2 added|
|2023-11-04 15:23:09|[KaTeX](https://github.com/KaTeX/KaTeX)|docs(users): add bearbei (#3897)  * Update siteConf<br>ig.js    Update Bearbei to the list and update it in<br> the order and with smaller picture.    * lint    --<br>-------    Co-authored-by: Erik Demaine |
|2023-11-04 13:05:56|[HikariCP](https://github.com/brettwooldridge/HikariCP)|update readme with latest artifact (5.1.0)|
|2023-11-04 11:26:49|[HackerPermKeeper](https://github.com/RuoJi6/HackerPermKeeper)|Update adduser_new_user.py|
|2023-11-04 04:22:46|[Microsoft-Activat<br>ion-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts)|Evade AV's detection - 7|
|2023-11-04 03:19:34|[dperf](https://github.com/baidu/dperf)|Merge pull request #387 from pengjianzhang/main  fi<br>x: 1. compile warnnings,  2 don't clear sequences in<br> time-wait state|
|2023-11-03 21:48:34|[Rubeus](https://github.com/GhostPack/Rubeus)|Merge pull request #172 from GhostPack/HarmJ0y-patc<br>h-1  Update KrbCredInfo.cs|
|2023-11-03 20:32:39|[Mobile-Security-F<br>ramework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)|Build(deps): Bump django from 4.1.12 to 4.1.13 (#22<br>82)  Bumps  from 4.1.12 to 4.1.13.  -     ---  updat<br>ed-dependencies:  - dependency-name: django    depen<br>dency-type: direct:production  ...    Signed-off-by:<br> dependabot[bot]   Co-authored-by: dependabot[bot] |
|2023-11-03 20:26:12|[protections-artif<br>acts](https://github.com/elastic/protections-artifacts)|Updating artifacts|
|2023-11-03 12:45:07|[merlin-agent](https://github.com/Ne0nd0g/merlin-agent)|Fix module semantic versioning|
|2023-11-03 10:51:38|[appshark](https://github.com/bytedance/appshark)|Merge pull request #50 from firmianay/dev  add Mani<br>festRisk|
|2023-11-03 09:23:18|[http-request-smug<br>gler](https://github.com/PortSwigger/http-request-smuggler)|Fix integrated turbo-intruder, bump version to 2.16|
|2023-11-03 06:26:55|[pingtunnel](https://github.com/esrrhs/pingtunnel)|delete|
|2023-11-03 03:27:51|[vulhub](https://github.com/vulhub/vulhub)|Merge pull request #465 from za/update-readme-cve-2<br>022-34265|
|2023-11-03 01:51:33|[BerylEnigma](https://github.com/ffffffff0x/BerylEnigma)|节点添加可显示/隐藏属性|
|2023-11-03 01:07:55|[ObserverWard](https://github.com/0x727/ObserverWard)|Merge pull request #211 from 0x727/dependabot/cargo<br>/csv-1.3.0  Bump csv from 1.2.2 to 1.3.0|
|2023-11-02 23:26:19|[telebot](https://github.com/tucnak/telebot)|Merge pull request #628 from tucnak/v3-middleware-f<br>ix  middleware: fix the append's capacity reusing|
|2023-11-02 22:58:45|[tmux](https://github.com/tmux/tmux)|Merge branch 'obsd-master'|
|2023-11-02 19:35:52|[Vuln-List](https://github.com/wwl012345/Vuln-List)|Update 中间件&框架&平台&第三方服务漏洞.md|
|2023-11-02 14:33:19|[nuclei](https://github.com/projectdiscovery/nuclei)|Merge branch 'dev'|
|2023-11-02 13:09:27|[gau](https://github.com/lc/gau)|Merge pull request #115 from lc/lc/fix-panic  fix(p<br>anic): fix gau panic when output flag is provided|
|2023-11-02 07:13:39|[WebGoat](https://github.com/WebGoat/WebGoat)|chore: bump org.apache.maven.plugins:maven-checksty<br>le-plugin (#1640)  Bumps  from 3.3.0 to 3.3.1.  -   <br>  ---  updated-dependencies:  - dependency-name: org<br>.apache.maven.plugins:maven-checkstyle-plugin    dep<br>endency-type: direct:production    update-type: vers<br>ion-update:semver-patch  ...    Signed-off-by: depen<br>dabot[bot]   Co-authored-by: dependabot[bot] |
|2023-11-02 02:26:35|[pwndbg](https://github.com/pwndbg/pwndbg)|introduce github-ci lockfile checking for: flake.lo<br>ck, poetry.lock  Signed-off-by: psondej |
|2023-11-01 20:24:15|[dnstwist](https://github.com/elceef/dnstwist)|Added proxy notification|
|2023-11-01 17:54:39|[smbmap](https://github.com/ShawnDEvans/smbmap)|Version update|
|2023-11-01 15:39:59|[linux-kernel-expl<br>oitation](https://github.com/xairy/linux-kernel-exploitation)|September/October updates|
|2023-11-01 13:54:19|[ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)|style: Optimize the style of the favor icon for log<br>ged-out users|
|2023-11-01 07:14:55|[ctf-wiki](https://github.com/ctf-wiki/ctf-wiki)|Merge pull request #883 from juicymio/patch-1  Upda<br>te house-of-pig.md|
|2023-11-01 04:18:55|[java-memshell-gen<br>erator-release](https://github.com/pen4uin/java-memshell-generator-release)|archived|
|2023-11-01 04:16:51|[SecurityInterview<br>Guide](https://github.com/FeeiCN/SecurityInterviewGuide)|Update README.md|
|2023-11-01 02:03:27|[FingerprintHub](https://github.com/0x727/FingerprintHub)|Auto Update FingerPrint [Wed Nov  1 02:03:27 UTC 20<br>23] :robot:|
|2023-10-31 22:19:31|[magic-wormhole](https://github.com/magic-wormhole/magic-wormhole)|Merge pull request #511 from meejah/feature/zipstre<br>am-ng  news for #503|
|2023-10-31 13:53:44|[focalboard](https://github.com/mattermost/focalboard)|Enhance Readme To Explain How To Contribute Transla<br>tions (#4918)  * feature/translations-contribution a<br>dding steps on how to contribute a translation    * <br>feature/translations-contribution added fruther deta<br>il of location of json file    * feature/translation<br>s-contribution updating snapshots    * feature/trans<br>lations-contribution adding step to run updating sna<br>pshot command    * feature/translations-contribution<br> reverting snapshot changes    * feature/translation<br>s-contribution reverting snapshot changes|
|2023-10-31 12:02:27|[mitaka](https://github.com/ninoseki/mitaka)|Merge pull request #762 from ninoseki/renovate/npm-<br>zod-vulnerability  fix(deps): update dependency zod <br>to v3.22.3 [security]|
|2023-10-31 12:00:54|[PetitPotam](https://github.com/topotam/PetitPotam)|Update README.md|
|2023-10-31 07:32:16|[shuji](https://github.com/paazmaya/shuji)|chore(deps): update dependency eslint to v8.52.0  S<br>igned-off-by: renovate[bot] |
|2023-10-31 07:28:28|[firmadyne](https://github.com/firmadyne/firmadyne)|fix #207 (#216)  Fix the makeNetwork.sh error with <br>Unicode characters when parsing the qemu log file|
|2023-10-31 03:28:27|[scan4all](https://github.com/hktalent/scan4all)|fixed dir for windows 2023-10-31|
|2023-10-31 03:08:12|[retoolkit](https://github.com/mentebinaria/retoolkit)|Update CHECKSUMS|
|2023-10-31 01:56:54|[Pentest-Windows](https://github.com/arch3rPro/Pentest-Windows)|Update README.md|
|2023-10-31 00:08:33|[slopShell](https://github.com/oldkingcone/slopShell)|:smile_cat:  Some updates.|
|2023-10-30 15:59:25|[SCFProxy](https://github.com/shimmeris/SCFProxy)|Update README_zh.md|
|2023-10-30 09:35:17|[al-khaser](https://github.com/LordNoteworthy/al-khaser)|Add cheat engine for anti-analysis (#264)  * Add ch<br>eat engine for analysis_tools_process    * Update RE<br>ADME.md|
|2023-10-30 08:28:08|[beef](https://github.com/beefproject/beef)|Locking otr-activerecord to version 2.1.2 until we <br>can fix the bugs with the later version|
|2023-10-30 06:18:02|[aliyun-oss-python<br>-sdk](https://github.com/aliyun/aliyun-oss-python-sdk)|release 2.18.3|
|2023-10-30 04:07:33|[Sentinel](https://github.com/alibaba/Sentinel)|make all ThreadPool static final (#3243)  * make al<br>l ThreadPool static final    * update github workflo<br>w|
|2023-10-30 03:15:51|[CTFd](https://github.com/CTFd/CTFd)|Merge pull request #2419 from Nils1729/fix/dynamic-<br>challenge-next  * Fix missing next_id on dynamic cha<br>llenges  * Closes #2418.|
|2023-10-30 02:44:26|[fucking-algorithm](https://github.com/labuladong/fucking-algorithm)|update content|
|2023-10-30 01:25:20|[Awesome-POC](https://github.com/Threekiii/Awesome-POC)|更新漏洞|
|2023-10-30 01:24:55|[Vulnerability-Wik<br>i](https://github.com/Threekiii/Vulnerability-Wiki)|更新漏洞|## 所有项目
# 渗透测试
## 信息收集
### 资产测绘采集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [InfoSearchAll](https://github.com/ExpLangcn/InfoSearchAll) | V1.2 | 为了方便安全从业人员在使用网络测绘平台进行信息搜集时的效率，本<br>程序集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并<br>且合并展示及导出。 |
| [ThunderSearch](https://github.com/xzajyjs/ThunderSearch) | v2.5.1 | 【支持Fofa、Shodan、Hunter、Zoomeye、Quake网络空间搜索引擎】闪<br>电搜索器；GUI图形化(Mac/Windows)渗透测试信息搜集工具；资产搜集引<br>擎；hw红队工具hvv |
| [Search_Viewer](https://github.com/G3et/Search_Viewer) | v3.0 | 集Fofa、Hunter鹰图、Shodan、360 quake、Zoomeye 钟馗之眼、censy<br>s 为一体的空间测绘gui图形界面化工具，支持一键采集爬取和导出fofa<br>、shodan等数据，方便快捷查看 |
| [koko-moni](https://github.com/burpheart/koko-moni) | v0.0.1 | 一个网络空间搜索引擎监控平台，可定时进行资产信息爬取，及时发现<br>新增资产，本项目聚合了 Fofa、Hunter、Quake、Zoomeye 和 Threatboo<br>k 的数据源，并对获取到的数据进行去重与清洗 |
| [AsamF](https://github.com/Kento-Sec/AsamF) | v0.2.5 | AsamF是集成Fofa、Quake、Hunter、Shodan、Zoomeye、Chinaz、0.zon<br>e及爱企查的一站式企业信息资产收集、网络资产测绘工具。 |
| [fshzqSearch](https://github.com/Ifory885/fshzqSearch) |  |  |
| [0_zone_tool](https://github.com/wkend/0_zone_tool) |  | 零零信安api信息系统查询脚本 |
| [TKHunter](https://github.com/HHa1ey/TKHunter) | TKHunte<br>r-v1.8 | 一个基于JavaFX写的一个Hunter资产测绘平台的图形化工具 |
### 子域名收集
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [subfinder](https://github.com/projectdiscovery/subfinder) | v2.6.3 | Fast passive subdomain enumeration tool. |
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
| [dirsearch_bypass4<br>03](https://github.com/lemonlove7/dirsearch_bypass403) | v0.2 | 目录扫描+JS文件中提取URL和子域+403状态绕过+指纹识别 |
| [dirsearch](https://github.com/maurosoria/dirsearch) | v0.4.3 | Web path scanner |
| [feroxbuster](https://github.com/epi052/feroxbuster) | v2.10.1 | A fast, simple, recursive content discovery tool written in Ru<br>st. |
| [ffuf](https://github.com/ffuf/ffuf) | v2.1.0 | Fast web fuzzer written in Go |
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
| [ObserverWard](https://github.com/0x727/ObserverWard) | v2023.1<br>0.13 | Cross platform community web fingerprint identification tool |
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
| [naabu](https://github.com/projectdiscovery/naabu) | v2.1.9 | A fast port scanner written in go with a focus on reliability <br>and simplicity. Designed to be used in combination with other t<br>ools for attack surface discovery in bug bounties and pentests |
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
| [nemo_go](https://github.com/hanc00l/nemo_go) | v2.10.3 | Nemo是用来进行自动化信息收集的一个简单平台，通过集成常用的信息<br>收集工具和技术，实现对内网及互联网资产信息的自动收集，提高隐患排<br>查和渗透测试的工作效率。 |
| [rengine](https://github.com/yogeshojha/rengine) | v2.0.1 | reNgine is an automated reconnaissance framework for web appli<br>cations with a focus on highly configurable streamlined recon p<br>rocess via Engines, recon data correlation and organization, co<br>ntinuous monitoring, backed by a database, and simple yet intui<br>tive User Interface. reNgine makes it easy for penetration test<br>ers to gather reconnaissance with minimal configuration and wit<br>h the help of reNgine's correlation, it just makes recon effort<br>less. |
| [ShuiZe_0x727](https://github.com/0x727/ShuiZe_0x727) | v1.0 | 信息收集自动化工具 |
| [DBJ](https://github.com/wgpsec/DBJ) |  | 大宝剑-边界资产梳理工具（红队、蓝队、企业组织架构、子域名、Web<br>资产梳理、Web指纹识别、ICON_Hash资产匹配） |
| [Voyager](https://github.com/xundididi/Voyager) |  | 一个安全工具集合平台，用来提高乙方安全人员的工作效率，请勿用于<br>非法项目 |
| [GoScan](https://github.com/CTF-MissFeng/GoScan) |  | GoScan是采用Golang语言编写的一款分布式综合资产管理系统，适合红<br>队、SRC等使用 |
| [Autoscanner](https://github.com/zongdeiqianxing/Autoscanner) | v1.2.1 | 输入域名>爆破子域名>扫描子域名端口>发现扫描web服务>集成报告的<br>全流程全自动扫描器。集成oneforall、masscan、nmap、dirsearch、cra<br>wlergo、xray等工具，另支持cdn识别、网页截图、站点定位；动态识别<br>域名并添加功能、工具超时中断等 |
| [MagiCude](https://github.com/er10yi/MagiCude) | v2.1 | 分布式端口（漏洞）扫描、资产安全管理、实时威胁监控与通知、高效<br>漏洞闭环、漏洞wiki、邮件报告通知、poc框架 |
| [Watchdog](https://github.com/CTF-MissFeng/Watchdog) |  | Watchdog是bayonet修改版，重新优化了数据库及web及扫描程序,加入<br>多节点 |
| [Tide](https://github.com/TideSec/Tide) |  | 目前实现了网络空间资产探测、指纹检索、漏洞检测、漏洞全生命周期<br>管理、poc定向检测、暗链检测、挂马监测、敏感字检测、DNS监测、网站<br>可用性监测、漏洞库管理、安全预警等等~ |
| [ARL](https://github.com/TophantTechnology/ARL) | v2.6 | ARL(Asset Reconnaissance Lighthouse)资产侦察灯塔系统旨在快速侦<br>察与目标关联的互联网资产，构建基础资产信息库。 协助甲方安全团队<br>或者渗透测试人员有效侦察和检索资产，发现存在的薄弱点和攻击面。 |
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
| [nuclei](https://github.com/projectdiscovery/nuclei) | v3.0.3 | Fast and customizable vulnerability scanner based on simple YA<br>ML based DSL. |
| [afrog](https://github.com/zan8in/afrog) | v2.9.1 | A Security Tool for Bug Bounty, Pentest and Red Teaming. |
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
### 安卓抓包辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [r0capture](https://github.com/r0ysue/r0capture) |  | 安卓应用层抓包通杀脚本 |
### 微信小程序辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [wxapkg](https://github.com/wux1an/wxapkg) | v1.5.0 | 微信小程序反编译工具，.wxapkg 文件扫描 + 解密 + 解包工具 |
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
| [codeql-cli-binari<br>es](https://github.com/github/codeql-cli-binaries) | v2.15.2 | Binaries for the CodeQL CLI |
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
| [gshark](https://github.com/madneal/gshark) | v1.2.2 | Scan for sensitive information easily and effectively. |
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
| [grype](https://github.com/anchore/grype) | v0.73.1 | A vulnerability scanner for container images and filesystems |
#### 容器漏洞分析工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [clair](https://github.com/quay/clair) | v4.7.2 | Vulnerability Static Analysis for Containers |
#### 容器安全扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [trivy](https://github.com/aquasecurity/trivy) | v0.47.0 | Find vulnerabilities, misconfigurations, secrets, SBOM in cont<br>ainers, Kubernetes, code repositories, clouds and more |
#### 容器镜像扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [grype](https://github.com/anchore/grype) | v0.73.1 | A vulnerability scanner for container images and filesystems |
| [syft](https://github.com/anchore/syft) | v0.96.0 | CLI tool and library for generating a Software Bill of Materia<br>ls from container images and filesystems |
#### K8S漏洞扫描
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-hunter](https://github.com/aquasecurity/kube-hunter) | v0.6.8 | Hunt for security weaknesses in Kubernetes clusters |
#### K8S基线核查
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | v0.6.19 | Checks whether Kubernetes is deployed according to security be<br>st practices as defined in the CIS Kubernetes Benchmark |
#### 云原生安全平台
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [neuvector](https://github.com/neuvector/neuvector) | v5.2.3 |  |
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
| [DNSlog-GO](https://github.com/lanyi1998/DNSlog-GO) | master | DNSLog-GO 是一款golang编写的监控 DNS 解析记录的工具，自带WEB界<br>面 |
| [godnslog](https://github.com/chennqqi/godnslog) | v0.7.0 | An exquisite dns&http log server for verify SSRF/XXE/RFI/RCE v<br>ulnerability  |
| [ysomap](https://github.com/wh1t3p1g/ysomap) | v0.1.4 | A helpful Java Deserialization exploit framework. |
| [Antenna](https://github.com/wuba/Antenna) | v1.3.5 | Antenna是58同城安全团队打造的一款辅助安全从业人员验证网络中多<br>种漏洞是否存在以及可利用性的工具。其基于带外应用安全测试(OAST)通<br>过任务的形式，将不同漏洞场景检测能力通过插件的形式进行集合，通过<br>与目标进行out-bind的数据通信方式进行辅助检测。 |
| [cola_dnslog](https://github.com/AbelChe/cola_dnslog) | v1.3.2 | Cola Dnslog v1.3.2 更加强大的dnslog平台/无回显漏洞探测辅助平台<br> 完全开源 dnslog httplog ldaplog rmilog 支持dns http ldap rmi等<br>协议 提供API调用方式便于与其他工具结合 支持钉钉机器人、Bark等提<br>醒 支持docker一键部署 后端完全使用python实现 前端基于vue-element<br>-admin二开 |
| [ddddocr](https://github.com/sml2h3/ddddocr) |  | 带带弟弟 通用验证码识别OCR pypi版 |
| [ysoserial](https://github.com/su18/ysoserial) |  |  |
| [JNDIExploit](https://github.com/qi4L/JNDIExploit) |  |  |
| [JNDIExploit](https://github.com/WhiteHSBG/JNDIExploit) | v1.4 | 对原版https://github.com/feihong-cs/JNDIExploit 进行了实用化修<br>改 |
| [JNDIExploit-1](https://github.com/Mr-xn/JNDIExploit-1) | v1.2 | 一款用于 JNDI注入 利用的工具，大量参考/引用了 Rogue JNDI 项目<br>的代码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的<br>方式，适用于与自动化工具配合使用。（from https://github.com/feih<br>ong-cs/JNDIExploit） |
| [JNDIExploit](https://github.com/0x727/JNDIExploit) | 1.1 | 一款用于JNDI注入利用的工具，大量参考/引用了Rogue JNDI项目的代<br>码，支持直接植入内存shell，并集成了常见的bypass 高版本JDK的方式<br>，适用于与自动化工具配合使用。 |
| [Exp-Tools](https://github.com/cseroad/Exp-Tools) | v1.2.3 | 一款集成高危漏洞exp的实用性工具 |
### 重点CMS利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [LandrayExploit](https://github.com/yuanhaiGreg/LandrayExploit) |  |  |
| [weaver_exp](https://github.com/z1un/weaver_exp) |  | 泛微OA漏洞综合利用脚本 |
| [EgGateWayGetShell](https://github.com/Tas9er/EgGateWayGetShell) |  | Code By:Tas9er |
| [CMSmap](https://github.com/Dionach/CMSmap) |  | CMSmap is a python open source CMS scanner that automates the <br>process of detecting security flaws of the most popular CMSs.  |
| [wpreconx](https://github.com/blackcrw/wpreconx) | 2.4.5 | WPRecon, is a tool for the recognition of vulnerabilities and <br>blackbox information for wordpress. |
| [wordpress-exploit<br>-framework](https://github.com/rastating/wordpress-exploit-framework) | v2.0.1 | A Ruby framework designed to aid in the penetration testing of<br> WordPress systems.  |
| [wpscan](https://github.com/wpscanteam/wpscan) | v3.8.25 | WPScan WordPress security scanner. Written for security profes<br>sionals and blog maintainers to test the security of their Word<br>Press websites. Contact us via contact@wpscan.com |
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
| [jdwp-shellifier](https://github.com/Lz1y/jdwp-shellifier) |  | 修改利用方式为通过对Sleeping的线程发送单步执行事件，达成断点，<br>从而可以直接获取上下文、执行命令，而不用等待断点被击中。 |
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
| [ghauri](https://github.com/r0oth3x49/ghauri) | 1.2.8 | An advanced cross-platform tool that automates the process of <br>detecting and exploiting SQL injection security flaws |
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
| [JWTPyCrack](https://github.com/Ch1ngg/JWTPyCrack) |  | JWT 弱口令 Key 爆破以及生成 NONE 加密的无 Key 的 JWTString |
| [JWT_GUI](https://github.com/Aiyflowers/JWT_GUI) | replace<br>_brute_e<br>rror | 基于pyqt5和pyjwt实现的jwt加解密爆破一体化工具(ps:其实是水的pyt<br>hon课设) |
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
| [cloudTools](https://github.com/dark-kingA/cloudTools) | main | 云资产管理工具 目前工具定位是云安全相关工具，目前是两个模块 云<br>存储工具、云服务工具， 云存储工具主要是针对oss存储、查看、删除、<br>上传、下载、预览等等 云服务工具主要是针对rds、服务器的管理，查看<br>、执行命令、接管等等 |
| [API-T00L](https://github.com/pykiller/API-T00L) | v1.2 | 互联网厂商API利用工具。 |
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
| [GitHack](https://github.com/lijiejie/GitHack) |  | A .git folder disclosure exploit |
| [GitHack](https://github.com/BugScanTeam/GitHack) |  | .git 泄漏利用工具，可还原历史版本 |
| [git-dumper](https://github.com/arthaud/git-dumper) |  | A tool to dump a git repository from a website |
| [GitDorker](https://github.com/obheda12/GitDorker) |  | A Python program to scrape secrets from GitHub through usage o<br>f a large repository of dorks. |
| [scrabble](https://github.com/denny0223/scrabble) |  | Simple tool to recover .git folder from remote server |
#### .DS_Store泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ds_store_exp](https://github.com/lijiejie/ds_store_exp) |  | A .DS_Store file disclosure exploit.   It parses .DS_Store fil<br>e and downloads files recursively. |
#### .svn泄露
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [svnExploit](https://github.com/admintony/svnExploit) |  | SvnExploit支持SVN源代码泄露全版本Dump源码 |
#### idea
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [idea_exploit](https://github.com/lijiejie/idea_exploit) |  | Gather sensitive information from (.idea) folder for pentester<br>s |
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
#### IIS
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [IIS_shortname_Sca<br>nner](https://github.com/lijiejie/IIS_shortname_Scanner) |  | an IIS shortname Scanner |
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
| [VulnerabilityTool<br>s](https://github.com/bingtangbanli/VulnerabilityTools) |  | [CVE_2023_28432漏洞 、CVE_2023_32315漏洞、 ThinkPHP 2.x 任意代<br>码执行漏洞 、ThinkPHP5 5.0.22/5.1.29 远程代码执行漏洞、 ThinkPHP<br>5 5.0.23 远程代码执行漏洞 ThinkPHP 多语言本地文件包含漏洞] |
#### Weblogic
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [weblogic-framewor<br>k](https://github.com/dream0x01/weblogic-framework) | v0.2.3 | weblogic-framework is the best tool for detecting weblogic vul<br>nerabilities. |
| [WeblogicTool](https://github.com/KimJun1010/WeblogicTool) | v1.3 | WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马<br>注入、密码解密等（深信服深蓝实验室天威战队强力驱动） |
| [CVE-2023-21839](https://github.com/4ra1n/CVE-2023-21839) |  |  |
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
| [TongdaOATools](https://github.com/xiaokp7/TongdaOATools) |  |  |
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
| [Awesome-POC](https://github.com/Threekiii/Awesome-POC) |  | 一个漏洞POC知识库 |
| [Vulnerability-Wik<br>i](https://github.com/Threekiii/Vulnerability-Wiki) | v1.0 | 基于 docsify 部署，目前漏洞数量 1000+ |
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
| [java-memshell-gen<br>erator-release](https://github.com/pen4uin/java-memshell-generator-release) | v1.0.7.<br>beta2 | 一款支持高度自定义的 Java 内存马生成工具 |
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
| [HackerPermKeeper](https://github.com/RuoJi6/HackerPermKeeper) | 6.0 |  |
### 远控
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [noterce](https://github.com/xiao-zhu-zhu/noterce) | 1.3 | 一种另辟蹊径的免杀执行系统命令的木马 |
| [Supershell](https://github.com/tdragon6/Supershell) | v2.0.0 | Supershell C2 远控平台，基于反向SSH隧道获取完全交互式Shell |
| [SimpleRemoter](https://github.com/yuanyuanxiang/SimpleRemoter) | v1.0.0.<br>5 | 基于gh0st的远程控制器：实现了终端管理、进程管理、窗口管理、远<br>程桌面、文件管理、语音管理、视频管理、服务管理、注册表管理等功能<br>，优化全部代码及整理排版，修复内存泄漏缺陷，程序运行稳定。项目代<br>码仅限于学习和交流用途。 |
| [trojan_simple_dem<br>o](https://github.com/Ciyfly/trojan_simple_demo) |  | 简单的用python写的远控demo 执行命令 只一个心跳完成所有操作 |
### 免杀相关
#### 签名伪造
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SigThief](https://github.com/secretsquirrel/SigThief) |  | Stealing Signatures and Making One Invalid Signature at a Time |
| [Sign-Sacker](https://github.com/langsasec/Sign-Sacker) |  | Sign-Sacker(签名掠夺者)：一款数字签名复制器，可将其他官方exe中<br>数字签名，图标，详细信息复制到没有签名的exe中，作为免杀，权限维<br>持，伪装的一种小手段。 |
#### 图标提取
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BeCyIconGrabberPo<br>rtable](https://github.com/JarlPenguin/BeCyIconGrabberPortable) |  | BeCyIconGrabber allows you to extract icons from almost any fi<br>le! |
#### 文件时间修改
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ChangeTimestamp](https://github.com/sorabug/ChangeTimestamp) |  | 一键修改exe、dll的编译时间、创建时间、修改时间和访问时间 |
| [ChTimeStamp](https://github.com/MsF-NTDLL/ChTimeStamp) |  | Changing the Creation time and the Last Written time of a drop<br>ped file by the timestamp of  other one , like the "kernel32.dl<br>l" timestamp |
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
| [noterce](https://github.com/xiao-zhu-zhu/noterce) | 1.3 | 一种另辟蹊径的免杀执行系统命令的木马 |
| [BypassAntiVirus](https://github.com/TideSec/BypassAntiVirus) |  | 远控免杀系列文章及配套工具，汇总测试了互联网上的几十种免杀工具<br>、113种白名单免杀方式、8种代码编译免杀、若干免杀实战技术，并对免<br>杀效果进行了一一测试，为远控的免杀和杀软对抗免杀提供参考。 |
| [SharpShellcodeLoa<br>der_Rc4Aes](https://github.com/xf555er/SharpShellcodeLoader_Rc4Aes) |  | 用于解密并加载shellcode，支持RC4和AES两种解密方法，并使用DInvo<br>ke来动态调用WinAPI函数，从而尝试绕过某些安全解决方案 |
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
| [PEASS-ng](https://github.com/carlospolop/PEASS-ng) | 2023111<br>2-0a42c5<br>50 | PEASS - Privilege Escalation Awesome Scripts SUITE (with color<br>s) |
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
| [frp](https://github.com/fatedier/frp) | v0.52.3 | A fast reverse proxy to help you expose a local server behind <br>a NAT or firewall to the internet. |
| [Erfrp](https://github.com/Goqi/Erfrp) | v0.1 | Erfrp-frp二开-免杀与隐藏 |
| [frp_cmd](https://github.com/OrangeWatermelon/frp_cmd) | v0.38.0<br>_modify | frp修改版，增加socks、pf命令，便捷启用socks5代理、端口转发，且<br>去除流量特征，增加loadini命令，支持命令行参数导入base64编码的配<br>置文件 |
| [dns2tcp](https://github.com/alex-sector/dns2tcp) | v0.5.2 |  |
| [dnscat2](https://github.com/iagox86/dnscat2) |  |  |
| [icmpsh](https://github.com/inquisb/icmpsh) |  |  |
| [pingtunnel](https://github.com/esrrhs/pingtunnel) |  | Pingtunnel is a tool that send TCP/UDP traffic over ICMP |
| [ngrok](https://github.com/inconshreveable/ngrok) |  | Introspected tunnels to localhost |
| [goproxy](https://github.com/snail007/goproxy) | v14.0 | 🔥  Proxy is a high performance HTTP(S) proxies, SOCKS5 proxie<br>s,WEBSOCKET, TCP, UDP proxy server implemented by golang. Now, <br>it supports chain-style proxies,nat forwarding in different lan<br>,TCP/UDP port forwarding, SSH forwarding.Proxy是golang实现的高<br>性能http,https,websocket,tcp,socks5代理服务器,支持内网穿透,链式<br>代理,通讯加密,智能HTTP,SOCKS5代理,黑白名单,限速,限流量,限连接数,<br>跨平台,KCP支持,认证API。 |
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
| [WIFIpass](https://github.com/lijiejie/WIFIpass) |  | decrypt all saved WIFI passwords on your PC |
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
| [Template](https://github.com/1n7erface/Template) | v1.2.5 | Next generation RedTeam heuristic intranet scanning | 下一代Re<br>dTeam启发式内网扫描 |
### 漏洞利用
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Viper](https://github.com/FunnyWolf/Viper) | 2023-09<br>-25-09-5<br>8-43 | Redteam operation  platform with webui 图形化红队行动辅助平台 |
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
| [Intranet-tools](https://github.com/private-null/Intranet-tools) |  |  |
| [impacket-gui](https://github.com/yutianqaq/impacket-gui) |  | impacket-gui |
| [Intranet-Movement<br>-Kit](https://github.com/AduraK2/Intranet-Movement-Kit) | V1.0 | 内网横向移动工具箱 |
| [Impacket_For_Web](https://github.com/XiaoBai-12138/Impacket_For_Web) |  |  |
| [java-impacket-gui](https://github.com/Suq3rm4n/java-impacket-gui) |  | java-impacket-gui |
### 域渗透工具
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ShuiYing_0x727](https://github.com/0x727/ShuiYing_0x727) | V1.0 | 检测域环境内，域机器的本地管理组成员是否存在弱口令和通用口令，<br>对域用户的权限分配以及域内委派查询 |
| [BloodHound](https://github.com/BloodHoundAD/BloodHound) | v4.3.1 | Six Degrees of Domain Admin |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Ladon](https://github.com/k8gege/Ladon) | v11.9 | Ladon大型内网渗透工具，可PowerShell模块化、可CS插件化、可内存<br>加载，无文件扫描。含端口扫描、服务识别、网络资产探测、密码审计、<br>高危漏洞检测、漏洞利用、密码读取以及一键GetShell，支持批量A段/B<br>段/C段以及跨网段扫描，支持URL、主机、域名列表扫描等。Ladon 11.9<br>内置255个功能,网络资产探测模块32个通过多种协议(ICMP\NBT\DNS\MAC\<br>SMB\WMI\SSH\HTTP\HTTPS\Exchange\mssql\FTP\RDP)以及方法快速获取<br>目标网络存活主机IP、计算机名、工作组、共享资源、网卡地址、操作系<br>统版本、网站、子域名、中间件、开放服务、路由器、交换机、数据库、<br>打印机等信息，高危漏洞检测16个含MS17010、Zimbra、Exchange |
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
| [PenKitGui](https://github.com/ccc-f/PenKitGui) |  | 渗透测试武器库 |
| [Taie-RedTeam-OS](https://github.com/taielab/Taie-RedTeam-OS) |  | 泰阿安全实验室-基于XUbuntu私人订制的红蓝对抗渗透操作系统 |
| [FreeGui](https://github.com/tyB-or/FreeGui) | v2.5 | freeGui：基于ttkbootstrap开发的一款用来管理自己的渗透测试工具<br>的一个小工具，并提供一些实用小功能，例如打开目录，运行工具，工具<br>备忘命令。 |
| [GUI_Tools](https://github.com/ghealer/GUI_Tools) | V1.1 | 一个由各种图形化渗透工具组成的工具集 |
| [Pentest-Windows](https://github.com/arch3rPro/Pentest-Windows) | v2.2 | Windows11 Penetration Suite Toolkit 一个开箱即用的windows渗透<br>测试环境 |
| [ApoalypseSecTools](https://github.com/ApocalypseSec/ApoalypseSecTools) |  | ApoalypseSecTool更新地址 |
| [commando-vm](https://github.com/mandiant/commando-vm) |  | Complete Mandiant Offensive VM (Commando VM), a fully customiz<br>able Windows-based pentesting virtual machine distribution. com<br>mandovm@mandiant.com |
| [PST-Bucket](https://github.com/arch3rPro/PST-Bucket) |  | Scoop-Buket for Penetration Suite Toolkit |
| [okfafu-pentestVM-<br>public](https://github.com/mrl64/okfafu-pentestVM-public) |  | okfafu渗透虚拟机公开版 |
| [Online_tools](https://github.com/Zhao-sai-sai/Online_tools) | 0.4.0 | 该工具是一个集成了非常多渗透测试工具，类似软件商城的工具可以进<br>行工具下载，工具的更新，工具编写了自动化的安装脚本，不用担心工具<br>跑不起来。 |
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
| [Pentools-wiki](https://github.com/ProbiusOfficial/Pentools-wiki) |  | 先是渗透工具合集，其次是wiki，做点不一样的x |
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
#### 绕过指纹检测
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [burp-awesome-tls](https://github.com/sleeyax/burp-awesome-tls) | v1.1.0 | Fixes Burp Suite's poor TLS stack. Bypass WAF, spoof any brows<br>er. |
#### 未分类
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
| [captcha-killer-mo<br>dified](https://github.com/f0ng/captcha-killer-modified) | 0.24.2 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免<br>费ocr库，用于验证码爆破，适配新版Burpsuite |
| [BurpCrypto](https://github.com/whwlsfb/BurpCrypto) |  | BurpCrypto is a collection of burpsuite encryption plug-ins, s<br>upport AES/RSA/DES/ExecJs(execute JS encryption code in burpsui<br>te). 支持多种加密算法或直接执行JS代码的用于爆破前端加密的BurpSu<br>ite插件 |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.34 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等<br>），类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础<br>上，不影响APP、网站加解密正常逻辑等。 |
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
| [OneScan](https://github.com/vaycore/OneScan) | v1.4.0 | OneScan是递归目录扫描的BurpSuite插件 |
| [OutLook](https://github.com/KrystianLi/OutLook) |  |  |
| [passive-scan-clie<br>nt-plus](https://github.com/winezer0/passive-scan-client-plus) | v0.4.12<br>.0 | burpsuite passive-scan-client 插件维护分支 |
| [BpScan](https://github.com/EASY233/BpScan) | 1.0.0 | 一款用于辅助渗透测试工程师日常渗透测试的Burp被动漏扫插件 |
| [BurpCRLFScan](https://github.com/A0WaQ4/BurpCRLFScan) | 1.4 | 使用java编写的CRLF-Injection-burp被动扫描插件 |
| [JsonDetect](https://github.com/a1phaboy/JsonDetect) | v1.0 | A burp Extender to detect json, include fastjson,jackson,gson |
| [autoDecoder](https://github.com/f0ng/autoDecoder) | 0.34 | Burp插件，根据自定义来达到对数据包的处理（适用于加解密、爆破等<br>），类似mitmproxy，不同点在于经过了burp中转，在自动加解密的基础<br>上，不影响APP、网站加解密正常逻辑等。 |
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
| [captcha-killer-mo<br>dified](https://github.com/f0ng/captcha-killer-modified) | 0.24.2 | captcha-killer的修改版，支持关键词识别base64编码的图片，添加免<br>费ocr库，用于验证码爆破，适配新版Burpsuite |
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
| [Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension) |  |  |
| [Burp-Non-HTTP-Ext<br>ension](https://github.com/summitt/Burp-Non-HTTP-Extension) |  |  |
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
| [mitaka](https://github.com/ninoseki/mitaka) | v1.3.3 | A browser extension for OSINT search |
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
### 二维码批量识别
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [QrScan](https://github.com/zfb132/QrScan) | v2.9.0 | 离线批量检测图片是否包含二维码以及识别二维码 |
### 自动拼图
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [PuzzleSolver](https://github.com/JamesHoi/PuzzleSolver) | v1.0.1-<br>beta | 一款专门为CTF比赛设计的拼图工具 |
### 图片隐写
#### 其他
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [stegsolve](https://github.com/Giotino/stegsolve) | v1.4 |  |
| [cloacked-pixel](https://github.com/livz/cloacked-pixel) |  | LSB steganography and detection |
| [CTFpics](https://github.com/RetrO-hash/CTFpics) |  |  |
| [ImageStrike](https://github.com/zR00t1/ImageStrike) | V0.2 | ImageStrike是一款用于CTF中图片隐写的综合利用工具 |
| [stegpy](https://github.com/dhsdshdhk/stegpy) |  | Simple steganography program based on the LSB method. |
| [steganography](https://github.com/7thSamurai/steganography) |  | Simple C++ Image Steganography tool to encrypt and hide files <br>insde images using Least-Significant-Bit encoding. |
| [Acropalypse-Multi<br>-Tool](https://github.com/frankthetank-music/Acropalypse-Multi-Tool) | v1.0.0 | Easily detect and restore Acropalypse vulnerable PNG and GIF f<br>iles with simple Python GUI. |
| [ImageMagick](https://github.com/ImageMagick/ImageMagick) | 7.1.1-2<br>1 | 🧙‍♂️ ImageMagick 7 |
#### 图片盲水印
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BlindWatermark](https://github.com/ww23/BlindWatermark) | v0.0.3 | Java 盲水印 |
| [BlindWaterMark](https://github.com/chishaxie/BlindWaterMark) |  | 盲水印 by python |
| [blind-watermark](https://github.com/linyacool/blind-watermark) |  | Watermark added to the frequency domain by Fourier transform |
| [blind_watermark](https://github.com/guofei9987/blind_watermark) | 0.2.1 | Blind&Invisible Watermark ，图片盲水印，提取水印无须原图！ |
#### png隐写
##### png宽高修复
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Deformed-Image-Re<br>storer](https://github.com/AabyssZG/Deformed-Image-Restorer) | V1.02 | 自动爆破PNG图片宽高并一键修复工具 |
### 流量分析
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [UsbMiceDataHacker](https://github.com/WangYihang/UsbMiceDataHacker) |  | USB鼠标流量包取证工具 , 主要用于绘制鼠标移动以及拖动轨迹 |
| [UsbKeyboardDataHa<br>cker](https://github.com/WangYihang/UsbKeyboardDataHacker) |  | USB键盘流量包取证工具 , 用于恢复用户的击键信息 |
| [UsbKbCracker](https://github.com/P001water/UsbKbCracker) |  | CTF中常见键盘流量解密脚本 |
| [webshell_detect](https://github.com/webraybtl/webshell_detect) |  | webshell_detect |
### 16进制编辑
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ImHex](https://github.com/WerWolv/ImHex) | v1.31.0 | 🔍 A Hex Editor for Reverse Engineers, Programmers and people <br>who value their retinas when working at 3 AM. |
### 编码解码
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Ciphey](https://github.com/Ciphey/Ciphey) | 5.14.0 | ⚡ Automatically decrypt encryptions without knowing the key o<br>r cipher, decode encodings, and crack hashes ⚡ |
| [TomatoTools](https://github.com/ht0Ruial/TomatoTools) | v1.0.2 | TomatoTools 一款CTF杂项利器，支持36种常见编码和密码算法的加密<br>和解密，31种密文的分析和识别，支持自动提取flag，自定义插件等。 |
| [CyberChef](https://github.com/gchq/CyberChef) | v10.5.2 | The Cyber Swiss Army Knife - a web app for encryption, encodin<br>g, compression and data analysis |
| [CTFCrackTools](https://github.com/0Chencc/CTFCrackTools) | 4.0.7 | China's first CTFTools framework.中国国内首个CTF工具框架,旨在<br>帮助CTFer快速攻克难关 |
### 取证分析
#### 内存取证
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [VolatilityPro](https://github.com/Tokeii0/VolatilityPro) |  | 一款用于自动化处理内存取证的Python脚本，并提供GUI界面 |
| [MemProcFS](https://github.com/ufrisk/MemProcFS) | v5.8 | MemProcFS |
#### vmx加密破解
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pyvmx-cracker](https://github.com/axcheron/pyvmx-cracker) |  | Simple tool to crack VMware VMX encryption passwords |
#### 微信取证
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [chatViewTool](https://github.com/Ormicron/chatViewTool) | BEAT | 基于Java实现的图形化微信聊天记录解密查看器 |
| [Sharp-dumpkey](https://github.com/Ormicron/Sharp-dumpkey) | 1 | 基于C#实现的获取微信数据库密钥的小工具 |
| [SharpWxDump](https://github.com/AdminTest0/SharpWxDump) |  | 微信客户端取证，可获取用户个人信息(昵称/账号/手机/邮箱/数据库<br>密钥(用来解密聊天记录))；支持获取多用户信息，不定期更新新版本偏<br>移，目前支持所有新版本、正式版本 |
| [GoWxDump](https://github.com/SpenserCai/GoWxDump) | v1.0.12 | SharpWxDump的Go语言版。微信客户端取证，获取信息(微信号、手机号<br>、昵称)，微信聊天记录分析(Top N聊天的人、统计聊天最频繁的好友排<br>行、关键词列表搜索等) |
#### 向日葵取证
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [Sunflower_get_Pas<br>sword](https://github.com/wafinfo/Sunflower_get_Password) |  | 一款针对向日葵的识别码和验证码提取工具 |
#### QQ取证
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [qq_msg_decode](https://github.com/saucer-man/qq_msg_decode) |  | 解码qq聊天数据库 |
### 音频隐写
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [audacity](https://github.com/audacity/audacity) | Audacit<br>y-3.4.1 | Audio Editor                                      |
| [dtmf-decoder](https://github.com/ribt/dtmf-decoder) |  | Extract phone numbers from an audio recording of the dial tone<br>s. |
| [QSSTV](https://github.com/ON4QZ/QSSTV) |  | Receive and transmit images over radio using analog SSTV or di<br>gital DRM |
### 压缩文件分析
#### CRC爆破
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CRC32-Tools](https://github.com/AabyssZG/CRC32-Tools) | 2.2 | Easy CRC32 Tools，so easy！！！ |
#### ZIP伪加密
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [ZipCenOp](https://github.com/442048209as/ZipCenOp) |  | ZipCenOp is a Java tool to play with Zip pseudo-encryption. |
### 综合
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools) |  | 渊龙Sec安全团队CTF&AWD工具箱 |
| [qsnctf-python](https://github.com/Moxin1044/qsnctf-python) | 0.0.8.1<br>0 | 青少年CTF的Python包，方便大家调用一些CTF常用功能。 |
| [CTF-Tools](https://github.com/qianxiao996/CTF-Tools) | v1.3.7 | 一款Python+Pyqt写的CTF编码、解码、加密、解密工具。 |
| [CTF_Hacker-Tools](https://github.com/Harveysn0w/CTF_Hacker-Tools) |  |  |
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
### 查壳
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [DIE-engine](https://github.com/horsicq/DIE-engine) | 3.08 | DIE engine |
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
| [CTF-RSA-tool](https://github.com/6u661e/CTF-RSA-tool) |  | a little tool help CTFer solve RSA problem |
| [rsa-wiener-attack](https://github.com/pablocelayes/rsa-wiener-attack) |  | A Python implementation of the Wiener attack on RSA public-key<br> encryption scheme. |
| [RSA](https://github.com/Mr-Aur0ra/RSA) |  |  |
| [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) |  | RSA attack tool (mainly for ctf) - retrieve private key from w<br>eak public key and/or uncipher data |
### autokey
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [breakautokey](https://github.com/hotzzzzy/breakautokey) |  | breakautokey |
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
## 相关资源
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SecToolKit](https://github.com/ProbiusOfficial/SecToolKit) |  | Cybersecurity tool repository / Wiki 收录常用 / 前沿 的CTF和渗<br>透工具以及其 官方/使用 文档，致力于让每个工具都能发挥作用ww，不<br>管你是萌新还是领域从业者希望你都能在这里找到适合你的工具或者获得<br>一定的启发。 |
| [CTF-QuickStart](https://github.com/ProbiusOfficial/CTF-QuickStart) |  | 源仓库存档 |
| [CTFtools-wiki](https://github.com/ProbiusOfficial/CTFtools-wiki) |  | 【Hello CTF】录常用 / 优秀 的CTF工具项目及其文档,一个对各阶段C<br>TFer都很友好的工具仓库,让所有的工具都发挥作用！ |
| [CTF-Note](https://github.com/kitezzzGrim/CTF-Note) |  | CTF笔记：该项目主要记录CTF知识、刷题记录、工具等。 |
| [apachecn-ctf-wiki](https://github.com/apachecn/apachecn-ctf-wiki) |  |  |
| | | http://www.ctftools.com/ |
| [ctf-tools](https://github.com/ctf-wiki/ctf-tools) |  | CTF 工具集合 |
| [ctf_ics_traffic](https://github.com/NewBee119/ctf_ics_traffic) |  | 工控CTF比赛工具，各种网络数据包处理脚本 |
| [CTF-Tools](https://github.com/Aabyss-Team/CTF-Tools) |  | 渊龙Sec安全团队CTF&AWD工具箱 |
| [BerylEnigma](https://github.com/ffffffff0x/BerylEnigma) | 1.15.0 | ffffffff0x team toolset for penetration testing, cryptography <br>research, CTF and daily use. | ffffffff0x 团队工具集，用来进行<br>渗透测试，密码学研究，CTF和日常使用。 |
| [CTFd](https://github.com/CTFd/CTFd) | 3.6.0 | CTFs as you need them |
| [CTFd_chinese_CN](https://github.com/Gu-f/CTFd_chinese_CN) | v1.2.0 | 对CTFd平台各版本的汉化记录。key:中文、汉化、翻译、chinese、CN<br>、CTFd |
# 应急响应
## Linux
### 自动化检查
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [GScan](https://github.com/grayddq/GScan) |  | 本程序旨在为安全应急响应人员对Linux主机排查时提供便利，实现主<br>机侧Checklist的自动全面化检测，根据检测结果自动数据聚合，进行黑<br>客攻击路径溯源。 |
| [LinuxCheck](https://github.com/al0ne/LinuxCheck) | V2.3 | Linux应急处置/信息搜集/漏洞检测工具，支持基础配置/网络流量/任<br>务计划/环境变量/用户信息/Services/bash/恶意文件/内核Rootkit/SSH/<br>Webshell/挖矿文件/挖矿进程/供应链/服务器风险等13类70+项检查 |
| [malwoverview](https://github.com/alexandreborges/malwoverview) | v5.4.2 | Malwoverview is a first response tool used for threat hunting <br>and offers intel information from Virus Total, Hybrid Analysis,<br> URLHaus, Polyswarm, Malshare, Alien Vault, Malpedia, Malware B<br>azaar, ThreatFox, Triage, InQuest and it is able to scan Androi<br>d devices against VT. |
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
| [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) |  | Sysmon configuration file template with default high-quality e<br>vent tracing |
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
| [ASP.NET-Memshell-<br>Scanner](https://github.com/yzddmr6/ASP.NET-Memshell-Scanner) |  | asp.net内存马检测工具 |
## 分析辅助
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [BlueTeamTools](https://github.com/abc123info/BlueTeamTools) | BlueTea<br>mToolsV0<br>.89版本 | 蓝队分析研判工具箱，功能包括内存马反编译分析、各种代码格式化、<br>网空资产测绘功能、溯源辅助、解密冰蝎流量、解密哥斯拉流量、解密Sh<br>iro/CAS/Log4j2的攻击payload、IP/端口连接分析、各种编码/解码功能<br>、蓝队分析常用网址、java反序列化数据包分析、Java类名搜索、Fofa搜<br>索、Hunter搜索等。 |
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
| [Elkeid](https://github.com/bytedance/Elkeid) | rasp-v2<br>.2.1.0-p<br>re | Elkeid is an open source solution that can meet the security r<br>equirements of various workloads such as hosts, containers and <br>K8s, and serverless. It is derived from ByteDance's internal be<br>st practices. |
| [Hades](https://github.com/theSecHunter/Hades) |  | Hades is an cross-platform HIDS with kernel-space data collect<br>ion. |
## Web应用防火墙
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [openstar](https://github.com/starjun/openstar) |  | lua waf,nginx+lua,openresty,luajit,waf+,cdn,nginx |
| [safeline](https://github.com/chaitin/safeline) | v3.10.1 | 一款足够简单、足够好用、足够强的免费 WAF。基于业界领先的语义引<br>擎检测技术，作为反向代理接入，保护你的网站不受黑客攻击。 |
## 欺骗防御
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [DecoyMini](https://github.com/decoymini/DecoyMini) | v2.0.66<br>91 | 🐝 A highly scalable, safe, free enterprise honeypots 一款高可<br>扩展、安全、免费的企业级蜜罐系统 |
| [Juggler](https://github.com/C4o/Juggler) |  | A system that may trick hackers.  针对黑客的拟态欺骗系统。 |
| [MySQL_Fake_Server](https://github.com/fnmsd/MySQL_Fake_Server) |  | MySQL Fake Server use to help MySQL Client File Reading and JD<br>BC Client Java Deserialize |
| [MysqlT](https://github.com/BeichenDream/MysqlT) | v1.0 | 伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击<br>攻击者 |
| [mysql-fake-server](https://github.com/4ra1n/mysql-fake-server) | 0.0.4 | MySQL Fake Server (纯Java实现，支持GUI版和命令行版，提供Docker<br>file，支持多种常见JDBC利用) |
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
| [FreeRDP](https://github.com/FreeRDP/FreeRDP) | 2.11.2 | FreeRDP is a free remote desktop protocol library and clients |
| [Quasar](https://github.com/quasar/Quasar) | v1.4.1 | Remote Administration Tool for Windows |
| [rustdesk](https://github.com/rustdesk/rustdesk) | 1.2.3 | An open-source remote desktop, and alternative to TeamViewer. |
## 生成虚假数据
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [faker](https://github.com/joke2k/faker) | v20.0.0 | Faker is a Python package that generates fake data for you. |
## 短信转发器
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [SmsForwarder](https://github.com/pppscn/SmsForwarder) | v3.2.0 | 短信转发器——监控Android手机短信、来电、APP通知，并根据指定规<br>则转发到其他手机：钉钉群自定义机器人、钉钉企业内机器人、企业微信<br>群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Tel<br>egram机器人、Server酱、PushPlus、手机短信等。包括主动控制服务端<br>与客户端，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。<br>（V3.0 新增）PS.这个APK主要是学习与自用，如有BUG请提ISSUE，同时<br>欢迎大家提PR指正 |
## 数据库管理软件
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [dbeaver](https://github.com/dbeaver/dbeaver) | 23.2.4 | Free universal database tool and SQL client |
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
| [v2rayA](https://github.com/v2rayA/v2rayA) | v2.2.4.<br>3 | A web GUI client of Project V which supports VMess, VLESS, SS,<br> SSR, Trojan, Tuic and Juicity protocols. 🚀 |
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
| [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | v1.3.7 | OCR图片转文字识别软件，完全离线。截屏/批量导入图片，支持多国语<br>言、合并段落、竖排文字。可排除水印区域，提取干净的文本。基于 Pad<br>dleOCR 。 |
## chatgpt
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [chatgpt](https://github.com/LangLangShanDeNanKe/chatgpt) |  | ChatGPT网址导航，分享免费好用AI网站！ |
| [Awesome-ChatGPT](https://github.com/dalinvip/Awesome-ChatGPT) |  | ChatGPT资料汇总学习，持续更新...... |
| [awesome-chatgpt-z<br>h](https://github.com/yzfly/awesome-chatgpt-zh) |  | ChatGPT 中文指南🔥，ChatGPT 中文调教指南，指令指南，应用开发指<br>南，精选资源清单，更好的使用 chatGPT 让你的生产力 up up up! 🚀 |
| [chatgpt-mac](https://github.com/vincelwt/chatgpt-mac) | v0.0.5 | ChatGPT for Mac, living in your menubar. |
| [ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut) |  | 🚀💪Maximize your efficiency and productivity, support for Eng<br>lish,中文,Español,العربية. 让生产力加倍的AI快捷指令。更有效地定<br>制、保存和分享自己的提示词。在提示词分享社区中，轻松找到适用于不<br>同场景的指令。 |
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
| [dperf](https://github.com/baidu/dperf) | v1.6.0 | dperf is a 100Gbps network load tester. |
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
## github加速
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [FastGithub](https://github.com/dotnetcore/FastGithub) | 2.1.4 | github加速神器，解决github打不开、用户头像无法加载、releases无<br>法上传下载、git-clone、git-pull、git-push失败等问题 |
## 按键精灵
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [KeymouseGo](https://github.com/taojy123/KeymouseGo) | v5.1.1 | 类似按键精灵的鼠标键盘录制和自动化操作 模拟点击和键入 | automa<br>te mouse clicks and keyboard input |
## pppoe拦截
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [pppoe-intercept](https://github.com/akkuman/pppoe-intercept) | v0.3 | 用来模拟中间人拦截 pppoe 拨号过程的账号密码 |
# 未分类
| 项目名称 | 版本 | 项目描述 |
| :---- | :---- | :---- |
| [windows-kernel-ex<br>ploits](https://github.com/SecWiki/windows-kernel-exploits) |  | windows-kernel-exploits   Windows平台提权漏洞集合 |
| [jd](https://github.com/josephburnett/jd) | v1.7.1 | JSON diff and patch |
| [requests](https://github.com/wangluozhe/requests) | v1.1.19 | 用于快速请求HTTP或HTTPS，并支持修改ja3指纹 |
| [containerd](https://github.com/containerd/containerd) | v1.7.8 | An open and reliable container runtime |
| [Quickdraw-Snort](https://github.com/digitalbond/Quickdraw-Snort) |  | Digital Bond's IDS/IPS rules for ICS and ICS protocols. |
| [TPScan](https://github.com/tangxiaofeng7/TPScan) |  |  |
| [CVE-2020-1066-EXP](https://github.com/cbwang505/CVE-2020-1066-EXP) | exp | CVE-2020-1066-EXP支持Windows 7和Windows Server 2008 R2操作系统 |
| [ccat](https://github.com/frostbits-security/ccat) | v1.01 | Cisco Config Analysis Tool |
| [wavecrack](https://github.com/wavestone-cdt/wavecrack) | v1.0 | Wavestone's web interface for password cracking with hashcat |
| [shiro-550-with-No<br>CC](https://github.com/dr0op/shiro-550-with-NoCC) | V1.1 | Shiro-550 不依赖CC链利用工具 |
| [bandit](https://github.com/PyCQA/bandit) | 1.7.5 | Bandit is a tool designed to find common security issues in Py<br>thon code. |
| [AwesomeScript](https://github.com/AntSwordProject/AwesomeScript) |  | AntSword Shell 脚本分享/示例 |
| [hindsight](https://github.com/obsidianforensics/hindsight) | v2023.0<br>3 | Web browser forensics for Google Chrome/Chromium |
| [cve-2021-22005-ex<br>p](https://github.com/shmilylty/cve-2021-22005-exp) |  |  |
| [jdupes](https://github.com/jbruchon/jdupes) | v1.27.3 | A powerful duplicate file finder and an enhanced fork of 'fdup<br>es'. |
| [spring-boot-start<br>er-swagger](https://github.com/dyc87112/spring-boot-starter-swagger) |  |  |
| [big-list-of-naugh<br>ty-strings](https://github.com/minimaxir/big-list-of-naughty-strings) |  | The Big List of Naughty Strings is a list of strings which hav<br>e a high probability of causing issues when used as user-input <br>data. |
| [ModSecurity](https://github.com/SpiderLabs/ModSecurity) | v3.0.10 | ModSecurity is an open source, cross platform web application <br>firewall (WAF) engine for Apache, IIS and Nginx that is develop<br>ed by Trustwave's SpiderLabs. It has a robust event-based progr<br>amming language which provides protection from a range of attac<br>ks against web applications and allows for HTTP traffic monitor<br>ing, logging and real-time analysis. With over 10,000 deploymen<br>ts world-wide, ModSecurity is the most widely deployed WAF in e<br>xistence.  |
| [CVE-2021-36260-me<br>tasploit](https://github.com/TaroballzChen/CVE-2021-36260-metasploit) |  | the metasploit script(POC) about CVE-2021-36260  |
| [go-mimikatz](https://github.com/vyrus001/go-mimikatz) |  | A wrapper around a pre-compiled version of the Mimikatz execut<br>able for the purpose of anti-virus evasion. |
| [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) |  |  |
| [Python-Brainfuck](https://github.com/pocmo/Python-Brainfuck) |  | Just a small Brainfuck interpreter written in Python |
| [exa](https://github.com/ogham/exa) | v0.10.1 | A modern replacement for ‘ls’. |
| [EggShell](https://github.com/neoneggplant/EggShell) |  |  |
| [halive](https://github.com/gnebbia/halive) |  | A fast http and https prober, to check which URLs are alive |
| [wxappUnpacker](https://github.com/xuedingmiaojun/wxappUnpacker) |  |  |
| [public](https://github.com/tinysec/public) |  | my public code |
| [yingji](https://github.com/tide-emergency/yingji) |  | 应急相关内容积累 |
| [MoAn_Honey_Pot_Ur<br>ls](https://github.com/NS-Sp4ce/MoAn_Honey_Pot_Urls) |  | X安蜜罐用的一些存在JSonp劫持的API |
| [USB-Rubber-Ducky](https://github.com/hak5darren/USB-Rubber-Ducky) |  |  |
| [CVE-2022-40127](https://github.com/Mr-xn/CVE-2022-40127) |  | Apache Airflow < 2.4.0 DAG  example_bash_operator RCE POC |
| [gobuster](https://github.com/OJ/gobuster) | v3.6.0 | Directory/File, DNS and VHost busting tool written in Go |
| [Jira-Lens](https://github.com/MayankPandey01/Jira-Lens) | v1.0.2 | Fast and customizable vulnerability scanner For JIRA written i<br>n Python |
| [docker_practice](https://github.com/yeasy/docker_practice) | v1.3.0 | Learn and understand Docker&Container technologies, with real <br>DevOps practice! |
| [CVE-2020-8813](https://github.com/mhaskar/CVE-2020-8813) |  | The official exploit for Cacti v1.2.8 Remote Code Execution CV<br>E-2020-8813 |
| [cas](https://github.com/apereo/cas) | v6.6.13 | Apereo CAS - Identity & Single Sign On for all earthlings and <br>beyond. |
| [Caidao-AES-Versio<br>n](https://github.com/ekgg/Caidao-AES-Version) |  | 一个Burp插件，实现用AES算法透明加密原版菜刀Caidao.exe与服务器<br>端交互的http数据流 |
| [hikvision-decrypt<br>er](https://github.com/WormChickenWizard/hikvision-decrypter) | v1.0 | A simple cross platform program written in C++ used for decryp<br>ting the configuration files created by Hikvision Security Came<br>ras. Successor to my hikvision-xor-decrypter |
| [capa](https://github.com/fireeye/capa) |  |  |
| [slopShell](https://github.com/oldkingcone/slopShell) |  | the only php webshell you need. |
| [alicloud-tools](https://github.com/iiiusky/alicloud-tools) | v1.0.5 | 阿里云ECS、策略组辅助小工具 |
| [PySharpSphere](https://github.com/RicterZ/PySharpSphere) |  | Yet another SharpSphere |
| [PoC-CVE-2022-3019<br>0](https://github.com/JMousqueton/PoC-CVE-2022-30190) |  | POC CVE-2022-30190 : CVE 0-day MS Offic RCE aka msdt follina |
| [w8fuckcdn](https://github.com/boy-hack/w8fuckcdn) |  | Get website IP address by scanning the entire net  通过扫描全<br>网绕过CDN获取网站IP地址 |
| [static-binaries](https://github.com/andrew-d/static-binaries) |  | Various *nix tools built as statically-linked binaries |
| [tsh-go](https://github.com/CykuTW/tsh-go) |  | Tiny SHell Go - An open-source backdoor written in Go |
| [goreleaser](https://github.com/goreleaser/goreleaser) | v1.22.1 | Deliver Go binaries as fast and easily as possible |
| [jsonhero-web](https://github.com/jsonhero-io/jsonhero-web) |  |  |
| [Venom](https://github.com/Dliv3/Venom) | v1.1.0 | Venom - A Multi-hop Proxy for Penetration Testers |
| [server](https://github.com/hashtopolis/server) | v0.14.1 | Hashtopolis - A Hashcat wrapper for distributed password recov<br>ery |
| [BlueKeep](https://github.com/Ekultek/BlueKeep) |  | Proof of concept for CVE-2019-0708 |
| [metinfo_sqlinject<br>ion](https://github.com/T3qui1a/metinfo_sqlinjection) |  |  |
| [luacheck](https://github.com/mpeterv/luacheck) | 0.23.0 |  A tool for linting and static analysis of Lua code.  |
| [seeyou_exp](https://github.com/z1un/seeyou_exp) |  |  |
| [HTTPHeadModifer](https://github.com/c0ny1/HTTPHeadModifer) | v0.1 | 一款快速修改HTTP数据包头的Burp Suite插件 |
| [weblogicScanner](https://github.com/0xn0ne/weblogicScanner) |  | weblogic 漏洞扫描工具。目前包含对以下漏洞的检测能力：CVE-2014-<br>4210、CVE-2016-0638、CVE-2016-3510、CVE-2017-3248、CVE-2017-350<br>6、CVE-2017-10271、CVE-2018-2628、CVE-2018-2893、CVE-2018-2894<br>、CVE-2018-3191、CVE-2018-3245、CVE-2018-3252、CVE-2019-2618、CV<br>E-2019-2725、CVE-2019-2729、CVE-2019-2890、CVE-2020-2551、CVE-2<br>020-14750、CVE-2020-14882、CVE-2020-14883 |
| [ThreatHound](https://github.com/n4ll3ec/ThreatHound) |  | ThreatHound is a threat intelligence query tool use for detect<br>ing potentially malicious IP or domains. It combines the MISP o<br>pen source threat intelligence sharing platform as its back-end<br> intelligence library, and currently integrates 69 open source <br>threat intelligence data feeds from the security community. |
| [SecurityInterview<br>Guide](https://github.com/FeeiCN/SecurityInterviewGuide) |  | 网络信息安全从业者面试指南 |
| [SharpSphere](https://github.com/JamesCooteUK/SharpSphere) | 2.1 | .NET Project for Attacking vCenter |
| [CVE-2019-7609](https://github.com/LandGrey/CVE-2019-7609) |  | exploit CVE-2019-7609(kibana RCE) on right way by python2 scri<br>pts |
| [trojan](https://github.com/Jrohy/trojan) | v2.15.3 | trojan多用户管理部署程序, 支持web页面管理 |
| [clash](https://github.com/Dreamacro/clash) |  |  |
| [some_pocsuite](https://github.com/hanc00l/some_pocsuite) |  | 用于漏洞排查的pocsuite3验证POC代码 |
| [JNDI-Exploit-Kit](https://github.com/pimps/JNDI-Exploit-Kit) |  | JNDI-Exploitation-Kit（A modified version of the great JNDI-In<br>jection-Exploit created by @welk1n. This tool can be used to st<br>art an HTTP Server, RMI Server and LDAP Server to exploit java <br>web apps vulnerable to JNDI Injection） |
| [shiro-cve-2020-17<br>523](https://github.com/jweny/shiro-cve-2020-17523) |  | shiro-cve-2020-17523 漏洞的两种绕过姿势分析 以及配套的漏洞环境 |
| [JavaScript-MD5](https://github.com/blueimp/JavaScript-MD5) |  | JavaScript MD5 implementation. Compatible with server-side env<br>ironments like node.js, module loaders like RequireJS and all w<br>eb browsers. |
| [SecurityBaselineC<br>heck](https://github.com/chroblert/SecurityBaselineCheck) |  |  |
| [java-sec-code](https://github.com/JoyChou93/java-sec-code) | v2.0.0 | Java web common vulnerabilities and security code which is bas<br>e on springboot and spring security |
| [firmware-mod-kit](https://github.com/rampageX/firmware-mod-kit) |  | Automatically exported from code.google.com/p/firmware-mod-kit |
| [APTnotes](https://github.com/kbandla/APTnotes) |  | Various public documents, whitepapers and articles about APT c<br>ampaigns |
| [CVE-2018-0296](https://github.com/milo2012/CVE-2018-0296) | v0.0.4 | Test CVE-2018-0296 and extract usernames |
| [go-shellcode](https://github.com/brimstone/go-shellcode) |  | Load shellcode into a new process |
| [Beta](https://github.com/DidierStevens/Beta) |  | Beta versions of my software |
| [Powershellery](https://github.com/nullbind/Powershellery) |  | This repo contains Powershell scripts used for general hackery<br>. |
| [Syborg](https://github.com/MilindPurswani/Syborg) |  | Recursive DNS Subdomain Enumerator with dead-end avoidance sys<br>tem (BETA) |
| [PSGumshoe](https://github.com/PSGumshoe/PSGumshoe) | v2.0 |  |
| [binwalk](https://github.com/ReFirmLabs/binwalk) | v2.3.4 | Firmware Analysis Tool |
| [shodan](https://github.com/shadowscatcher/shodan) | v1.0.7 | yet another Shodan.io client |
| [qqwry](https://github.com/out0fmemory/qqwry) |  |  |
| [RSA-In-CTF](https://github.com/yifeng-lee/RSA-In-CTF) |  |  |
| [Bashfuscator](https://github.com/Bashfuscator/Bashfuscator) |  | A fully configurable and extendable Bash obfuscation framework<br>. This tool is intended to help both red team and blue team. |
| [assetfinder](https://github.com/tomnomnom/assetfinder) |  | Find domains and subdomains related to a given domain |
| [lor-axe](https://github.com/ajmwagar/lor-axe) |  | 🪓 a multi-threaded, low-bandwidth HTTP DOS tool |
| [Pentest_Interview](https://github.com/Leezj9671/Pentest_Interview) |  | 个人准备渗透测试和安全面试的经验之谈，和去部分厂商的面试题，干<br>货真的满满~ |
| [Erebus](https://github.com/DeEpinGh0st/Erebus) | V1.3.6 | CobaltStrike后渗透测试插件 |
| [lib_mysqludf_sys](https://github.com/mysqludf/lib_mysqludf_sys) |  | A UDF library with functions to interact with the operating sy<br>stem. These functions allow you to interact with the execution <br>environment in which MySQL runs. |
| [jarm](https://github.com/salesforce/jarm) |  |  |
| [Rubeus](https://github.com/GhostPack/Rubeus) | 1.6.4 | Trying to tame the three-headed dog. |
| [PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub) |  | 📡 PoC auto collect from GitHub. ⚠️ Be careful Malware. |
| [JavaID](https://github.com/Cryin/JavaID) |  | java source code static code analysis and danger function iden<br>tify prog |
| [network-fingerpri<br>nt](https://github.com/projectdiscovery/network-fingerprint) | v0.0.1 | A fingerprint generation helper for nuclei network templates |
| [hideNsneak](https://github.com/rmikehodges/hideNsneak) |  |  |
| [SeeyonEXP](https://github.com/nex121/SeeyonEXP) |  |  |
| [S2-061](https://github.com/EvilPulsar/S2-061) |  | some struts tag ,  attributes which out of the range will call<br> SetDynamicAttribute() function, it will cause ONGL expression <br>execute |
| [MQTTX](https://github.com/emqx/MQTTX) | v1.9.6 | A Powerful and All-in-One MQTT 5.0 client toolbox for Desktop,<br> CLI and WebSocket. |
| [Digispark-Duckdui<br>no](https://github.com/PlatyPew/Digispark-Duckduino) |  | Poor man's rubber ducky |
| [jumpserver_rce](https://github.com/Skactor/jumpserver_rce) |  |  |
| [simplehttpserver](https://github.com/projectdiscovery/simplehttpserver) | v0.0.6 | Go alternative of python SimpleHTTPServer |
| [CVE-2019-1579](https://github.com/securifera/CVE-2019-1579) |  |  |
| [CVE-2021-1675-LPE](https://github.com/hlldz/CVE-2021-1675-LPE) |  | Local Privilege Escalation Edition for CVE-2021-1675/CVE-2021-<br>34527 |
| [MySQL-Monitor](https://github.com/cw1997/MySQL-Monitor) |  | MySQL服务器执行SQL记录实时监控（WEB版本） |
| [teler](https://github.com/kitabisa/teler) | v2.0.0-<br>dev.3 | Real-time HTTP Intrusion Detection |
| [pwnginx](https://github.com/t57root/pwnginx) |  | Pwn nginx - a nginx backdoor provides shell access, socks5 tun<br>neling, http password sniffing. |
| [writeups](https://github.com/httpvoid/writeups) |  |  |
| [webshell-detect-b<br>ypass](https://github.com/LandGrey/webshell-detect-bypass) |  | 绕过专业工具检测的Webshell研究文章和免杀的Webshell |
| [CVE-2018-10933](https://github.com/blacknbunny/CVE-2018-10933) |  | Spawn to shell without any credentials by using CVE-2018-10933<br> (LibSSH) |
| [Malleable-C2-Prof<br>iles](https://github.com/rsmudge/Malleable-C2-Profiles) |  | Malleable C2 is a domain specific language to redefine indicat<br>ors in Beacon's communication. This repository is a collection <br>of Malleable C2 profiles that you may use. These profiles work <br>with Cobalt Strike 3.x. |
| [tmux](https://github.com/tmux/tmux) | 3.3a | tmux source code |
| [Microsoft-Activat<br>ion-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 2.4 | A Windows and Office activator using HWID / Ohook / KMS38 / On<br>line KMS activation methods, with a focus on open-source code a<br>nd fewer antivirus detections. |
| [navicat_password_<br>decrypt](https://github.com/Zhuoyuan1/navicat_password_decrypt) | v2.0 | 忘记navicat密码时,此工具可以帮您查看密码 |
| [community3](https://github.com/volatilityfoundation/community3) |  | Volatility3 plugins developed and maintained by the community |
| [GeoIP2-CN](https://github.com/Hackl0us/GeoIP2-CN) |  | 小巧精悍、准确、实用 GeoIP2 数据库 |
| [GoogleHacking-Pag<br>e](https://github.com/K0rz3n/GoogleHacking-Page) |  | This is a summary of my study and use of Google hacking. I hop<br>e I can share it with you. If you like, please give me a star o<br>r fork it, thank you. |
| [YarnRpcRCE](https://github.com/cckuailong/YarnRpcRCE) | 0.0.1 |  |
| [gokart](https://github.com/praetorian-inc/gokart) | v0.5.1 | A static analysis tool for securing Go code |
| [ProxyNotShell-PoC](https://github.com/testanull/ProxyNotShell-PoC) |  |  |
| [SiteServer-CMS-Re<br>mote-download-Gets<br>hell](https://github.com/zhaoweiho/SiteServer-CMS-Remote-download-Getshell) |  |  |
| [s3tk](https://github.com/ankane/s3tk) |  | A security toolkit for Amazon S3 |
| [CVE-2022-0540-RCE](https://github.com/Pear1y/CVE-2022-0540-RCE) |  | Atlassian Jira Seraph Authentication Bypass RCE（CVE-2022-0540<br>） |
| [coreruleset](https://github.com/coreruleset/coreruleset) | v3.3.5 | OWASP ModSecurity Core Rule Set (Official Repository) |
| [xerosploit](https://github.com/LionSec/xerosploit) | v1.0 | Efficient and advanced man in the middle framework |
| [sunlogin_rce](https://github.com/Mr-xn/sunlogin_rce) | new | 向日葵 RCE |
| [nps](https://github.com/cnlh/nps) |  |  |
| [EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness) |  |  |
| [the-craft-of-self<br>teaching](https://github.com/selfteaching/the-craft-of-selfteaching) |  | One has no future if one couldn't teach themself. |
| [memtriage](https://github.com/gleeda/memtriage) | v0.3.2-<br>alpha | Allows you to quickly query a Windows machine for RAM artifact<br>s |
| [kerberoast](https://github.com/nidem/kerberoast) |  |  |
| [Limelighter](https://github.com/Tylous/Limelighter) |  | A tool for generating fake code signing certificates or signin<br>g real ones |
| [Drupalgeddon2](https://github.com/dreadlocked/Drupalgeddon2) |  | Exploit for Drupal v7.x + v8.x (Drupalgeddon 2 / CVE-2018-7600<br> / SA-CORE-2018-002) |
| [ipv6toolkit](https://github.com/fgont/ipv6toolkit) |  | SI6 Networks' IPv6 Toolkit |
| [ezXSS](https://github.com/ssl/ezXSS) | 4.1 | ezXSS is an easy way for penetration testers and bug bounty hu<br>nters to test (blind) Cross Site Scripting. |
| [cve-2022-23131](https://github.com/Mr-xn/cve-2022-23131) |  | cve-2022-23131 zabbix-saml-bypass-exp |
| [o365enum](https://github.com/gremwell/o365enum) |  | Enumerate valid usernames from Office 365 using ActiveSync, Au<br>todiscover v1, or office.com login page. |
| [JNDIMonitor](https://github.com/r00tSe7en/JNDIMonitor) |  | 一个LDAP请求监听器，摆脱dnslog平台 |
| [CVE-2022-27666](https://github.com/plummm/CVE-2022-27666) |  | Exploit for CVE-2022-27666 |
| [DotNetToJScriptMi<br>ni](https://github.com/KINGSABRI/DotNetToJScriptMini) |  | A simplified version of DotNetToJScript to create a JScript fi<br>le which loads a .NET v2 assembly from memory. |
| [CANToolz](https://github.com/CANToolz/CANToolz) | v3.7.0 | CANToolz - Black-box CAN network analysis framework |
| [joffrey](https://github.com/zombiesam/joffrey) |  | Stupid MQTT Brute Forcer |
| [evolve](https://github.com/JamesHabben/evolve) | v1.6 | Web interface for the Volatility Memory Forensics Framework |
| [Jumpserver-EXP](https://github.com/Veraxy00/Jumpserver-EXP) |  | JumpServer远程代码执行漏洞检测利用脚本 |
| [bugbounty-cheatsh<br>eet](https://github.com/EdOverflow/bugbounty-cheatsheet) |  | A list of interesting payloads, tips and tricks for bug bounty<br> hunters. |
| [IFaultrepElevated<br>DataCollectionUAC](https://github.com/Wh04m1001/IFaultrepElevatedDataCollectionUAC) |  |  |
| [awesome-incident-<br>response](https://github.com/meirwah/awesome-incident-response) |  | A curated list of tools for incident response |
| [cve-2019-19781](https://github.com/trustedsec/cve-2019-19781) |  | This is a tool published for the Citrix ADC (NetScaler) vulner<br>ability. We are only disclosing this due to others publishing t<br>he exploit code first. |
| [filterbypass](https://github.com/masatokinugawa/filterbypass) |  | Browser's XSS Filter Bypass Cheat Sheet |
| [console](https://github.com/minio/console) | v0.41.0 | Simple UI for MinIO Object Storage :abacus: |
| [f5-bigip-rce-cve-<br>2020-5902](https://github.com/theLSA/f5-bigip-rce-cve-2020-5902) |  | F5 BIG-IP RCE CVE-2020-5902 automatic check tool |
| [chrome_password_g<br>rabber](https://github.com/x899/chrome_password_grabber) |  |  |
| [protections-artif<br>acts](https://github.com/elastic/protections-artifacts) |  | Elastic Security detection content for Endpoint |
| [cheetah](https://github.com/shmilylty/cheetah) |  | a very fast brute force webshell password tool |
| [updog](https://github.com/sc0tfree/updog) | 1.4 | Updog is a replacement for Python's SimpleHTTPServer. It allow<br>s uploading and downloading via HTTP/S, can set ad hoc SSL cert<br>ificates and use http basic auth. |
| [ProfSvcLPE](https://github.com/klinix5/ProfSvcLPE) |  |  |
| [cloudflair](https://github.com/christophetd/cloudflair) |  | 🔎 Find origin servers of websites behind CloudFlare by using <br>Internet-wide scan data from Censys. |
| [sliver-gui](https://github.com/BishopFox/sliver-gui) | v0.0.9 | A Sliver GUI Client |
| [qiling](https://github.com/qilingframework/qiling) | 1.4.6 | A True Instrumentable Binary Emulation Framework |
| [Landray-OA-Treexm<br>l-Rce](https://github.com/tangxiaofeng7/Landray-OA-Treexml-Rce) |  | 蓝凌OA远程代码执行漏洞批量检查 |
| [DigiKeyboard_DE](https://github.com/BesoBerlin/DigiKeyboard_DE) |  | angepasste Header-Dateien für Deutsches Tastatur Layout | modf<br>ied headers for german keyboard layout |
| [Azure-Red-Team](https://github.com/rootsecdev/Azure-Red-Team) |  | Azure Security Resources and Notes |
| [CVE-2019-11510](https://github.com/projectzeroindia/CVE-2019-11510) |  | Exploit for Arbitrary File Read on Pulse Secure SSL VPN (CVE-2<br>019-11510) |
| [DBconfigReader](https://github.com/jas502n/DBconfigReader) |  | 泛微ecology OA系统接口存在数据库配置信息泄露漏洞 |
| [fmem](https://github.com/NateBrune/fmem) |  | Linux Kernel Module designed to help analyze volatile memory i<br>n the linux kernel |
| [CVE-2021-41277](https://github.com/Seals6/CVE-2021-41277) |  | Metabase任意文件读取漏洞批量扫描工具 |
| [TLS-poison](https://github.com/jmdx/TLS-poison) |  |  |
| [slipstream](https://github.com/samyk/slipstream) |  | NAT Slipstreaming allows an attacker to remotely access any TC<br>P/UDP services bound to a victim machine, bypassing the victim<br>’s NAT/firewall, just by anyone on the victim's network visitin<br>g a website |
| [dcpwn](https://github.com/QAX-A-Team/dcpwn) |  | an impacket-dependent script exploiting CVE-2019-1040 |
| [KillDefender](https://github.com/Octoberfest7/KillDefender) |  | A small (Edited) POC to make defender useless by removing its <br>token privileges and lowering the token integrity   |
| [jboss-_CVE-2017-1<br>2149](https://github.com/yunxu1/jboss-_CVE-2017-12149) |  | CVE-2017-12149 jboss反序列化 可回显 |
| [Hacking-With-Gola<br>ng](https://github.com/re4lity/Hacking-With-Golang) |  |  |
| [SeeYouCM-Thief](https://github.com/trustedsec/SeeYouCM-Thief) |  |  |
| [firmadyne](https://github.com/firmadyne/firmadyne) |  | Platform for emulation and dynamic analysis of Linux-based fir<br>mware |
| [PostConfluence](https://github.com/BeichenDream/PostConfluence) | v1.0 | 哥斯拉Confluence后渗透插件  MakeToken SearchPage  ListAllUser <br>AddAdminUser ListAllPage ........ |
| [proxyshell-for-ex<br>change_workload](https://github.com/wudicainiao/proxyshell-for-exchange_workload) |  |  |
| [KMS_VL_ALL](https://github.com/kkkgo/KMS_VL_ALL) | 44 | 🔑KMS_VL_ALL - Smart Activation Script |
| [ssh-audit](https://github.com/arthepsy/ssh-audit) |  | SSH server auditing (banner, key exchange, encryption, mac, co<br>mpression, compatibility, security, etc) |
| [1earn](https://github.com/No-Github/1earn) |  |  |
| [docker-oracle-xe-<br>11g](https://github.com/wnameless/docker-oracle-xe-11g) |  | Dockerfile of Oracle Database Express Edition 11g Release 2 |
| [RoarCTF-Writeup-s<br>ome-Source-Code](https://github.com/berTrAM888/RoarCTF-Writeup-some-Source-Code) |  | 没有怎么整理，大家将就看吧，有问题发一个issue给我 |
| [impacket-examples<br>-windows](https://github.com/maaaaz/impacket-examples-windows) | v0.9.17 | The great impacket example scripts compiled for Windows |
| [Corsy](https://github.com/s0md3v/Corsy) | 1.0-rc | CORS Misconfiguration Scanner |
| [ctop](https://github.com/bcicen/ctop) | v0.7.7 | Top-like interface for container metrics |
| [SharpPack](https://github.com/mdsecactivebreach/SharpPack) |  | An Insider Threat Toolkit |
| [CVE-2019-12409](https://github.com/jas502n/CVE-2019-12409) |  | Apache Solr RCE (ENABLE_REMOTE_JMX_OPTS="true") |
| [Gitlab-CVE-2021-2<br>2205](https://github.com/mr-r3bot/Gitlab-CVE-2021-22205) |  |  |
| [CVE-2019-1040](https://github.com/Ridter/CVE-2019-1040) |  | CVE-2019-1040 with Exchange |
| [dnSpy](https://github.com/dnSpyEx/dnSpy) | v6.4.1 | Unofficial revival of the well known .NET debugger and assembl<br>y editor, dnSpy |
| [HackMySQL](https://github.com/T3st0r-Git/HackMySQL) |  | Using To MySQL Elevate Privileges. |
| [CVE-2021-30128](https://github.com/r0ckysec/CVE-2021-30128) |  |  |
| [ysoserial-mangguo<br>gan](https://github.com/MrMeizhi/ysoserial-mangguogan) |  |  |
| [dc_find](https://github.com/heikanet/dc_find) |  |  |
| [BurpCollect](https://github.com/orleven/BurpCollect) |  | 基于BurpCollector的二次开发， 记录Burpsuite Site Map记录的里的<br>数据包中的目录路径参数名信息，并存入Sqlite，并可导出txt文件。 |
| [FingerPrint](https://github.com/tanjiti/FingerPrint) |  | web应用指纹识别 |
| [tabby](https://github.com/Eugeny/tabby) | v1.0.20<br>1 | A terminal for a more modern age |
| [e-cology](https://github.com/jas502n/e-cology) |  | e-cology OA_Beanshell_RCE |
| [Markdown-XSS-Payl<br>oads](https://github.com/cujanovic/Markdown-XSS-Payloads) |  | XSS payloads for exploiting Markdown syntax |
| [ihoneyBakFileScan<br>_Modify](https://github.com/VMsec/ihoneyBakFileScan_Modify) |  | 批量网站备份文件扫描器，增加文件规则，优化内存占用 |
| [IllegalWordsDetec<br>tion](https://github.com/NewbieGameCoder/IllegalWordsDetection) |  | 提供高效率的较简单的Unity3d手游客户端的敏感词检测的算法，能应<br>付大部分敏感词过滤需求 |
| [netview](https://github.com/mubix/netview) | latest | Netview enumerates systems using WinAPI calls |
| [Win-Logs-Parse-to<br>ol](https://github.com/Clayeee/Win-Logs-Parse-tool) |  |  |
| [antiHoneypot](https://github.com/Monyer/antiHoneypot) | 0.7.2 | 一个拦截 XSSI & 识别Web蜜罐的Chrome扩展 |
| [face_recognition](https://github.com/ageitgey/face_recognition) | v1.2.2 | The world's simplest facial recognition api for Python and the<br> command line |
| [SpringBootLearnin<br>g](https://github.com/gf-huanchupk/SpringBootLearning) |  | Spring Boot learning process |
| [Arjun](https://github.com/s0md3v/Arjun) | 2.2.1 | HTTP parameter discovery suite. |
| [celery](https://github.com/celery/celery) | v5.3.5 | Distributed Task Queue (development branch) |
| [VindicateTool](https://github.com/Rushyo/VindicateTool) |  | LLMNR/NBNS/mDNS Spoofing Detection Toolkit |
| [masscan](https://github.com/robertdavidgraham/masscan) | 1.3.2 | TCP port scanner, spews SYN packets asynchronously, scanning e<br>ntire Internet in under 5 minutes. |
| [CVE-2019-0708](https://github.com/worawit/CVE-2019-0708) |  | CVE-2019-0708 (BlueKeep) |
| [CVE-2021-33909](https://github.com/Liang2580/CVE-2021-33909) |  | Sequoia exploit (7/20/21) |
| [TongDaOA-Fake-Use<br>r](https://github.com/NS-Sp4ce/TongDaOA-Fake-User) |  | 通达OA 任意用户登录漏洞 |
| [CVE-2020-0688](https://github.com/zcgonvh/CVE-2020-0688) |  | Exploit and detect tools for CVE-2020-0688 |
| [knock](https://github.com/guelfoweb/knock) | 5.4.0 | Knock Subdomain Scan |
| [CVE-2020-3153](https://github.com/goichot/CVE-2020-3153) |  | Cisco AnyConnect < 4.8.02042 privilege escalation through path<br> traversal |
| [CVE-2019-0230](https://github.com/ramoncjs3/CVE-2019-0230) |  | CVE-2019-0230 & s2-059 poc. |
| [easy-rsa](https://github.com/OpenVPN/easy-rsa) | v3.1.7 | easy-rsa - Simple shell based CA utility |
| [geckodriver](https://github.com/mozilla/geckodriver) | v0.33.0 | WebDriver for Firefox |
| [poc_CVE-2018-1002<br>105](https://github.com/evict/poc_CVE-2018-1002105) |  | PoC for CVE-2018-1002105. |
| [git-lfs](https://github.com/git-lfs/git-lfs) | v3.4.0 | Git extension for versioning large files |
| [RiskySPN](https://github.com/cyberark/RiskySPN) |  | Detect and abuse risky SPNs |
| [linux-inject](https://github.com/gaffe23/linux-inject) |  | Tool for injecting a shared object into a Linux process |
| [findWebshell](https://github.com/he1m4n6a/findWebshell) |  | findWebshell是一款基于python开发的webshell检测工具。 |
| [krbrelayx](https://github.com/dirkjanm/krbrelayx) |  | Kerberos unconstrained delegation abuse toolkit |
| [security](https://github.com/7ym0n/security) |  |  |
| [PentestDB](https://github.com/safe6Sec/PentestDB) |  | 各种数据库的利用姿势 |
| [httpie](https://github.com/jakubroztocil/httpie) |  |  |
| [fastjson-1](https://github.com/CaijiOrz/fastjson-1) |  |  |
| [See-SURF](https://github.com/In3tinct/See-SURF) | v2.0 | Python based scanner to find potential SSRF parameters |
| [Struts2VulsTools](https://github.com/shack2/Struts2VulsTools) | 2.3.201<br>90927 | Struts2系列漏洞检查工具 |
| [leaky-repo](https://github.com/Plazmaz/leaky-repo) | 1.1.2 | Benchmarking repo for secrets scanning |
| [CycleTLS](https://github.com/Danny-Dasilva/CycleTLS) |  | Spoof TLS/JA3 fingerprints in GO and Javascript  |
| [PadBuster](https://github.com/AonCyberLabs/PadBuster) |  | Automated script for performing Padding Oracle attacks |
| [webshell-find-too<br>ls](https://github.com/mornone/webshell-find-tools) |  | 分析web访问日志以及web目录文件属性，用于根据查找可疑后门文件的<br>相关脚本。 |
| [CVE-2016-5195](https://github.com/gbonacini/CVE-2016-5195) |  | A CVE-2016-5195 exploit example. |
| [CTF-RSA](https://github.com/kur0mi/CTF-RSA) |  | 总结一下各路大师傅的RSA脚本233 |
| [ueditor-getshell](https://github.com/theLSA/ueditor-getshell) |  | ueditor .net getshell |
| [3vilGu4rd](https://github.com/PDWR/3vilGu4rd) | 3vilGu4<br>rd-V0.2 | This is a daemon process which make a programe runing all time<br>. |
| [thinkphp-RCE-POC-<br>Collection](https://github.com/SkyBlueEternal/thinkphp-RCE-POC-Collection) |  | thinkphp v5.x 远程代码执行漏洞-POC集合 |
| [gojwtcrack](https://github.com/x1sec/gojwtcrack) |  |  |
| [CSAgent](https://github.com/Twi1ight/CSAgent) |  |  |
| [Linux_Exploit_Sug<br>gester](https://github.com/InteliSecureLabs/Linux_Exploit_Suggester) |  | Linux Exploit Suggester; based on operating system release num<br>ber  |
| [javaboy-code-samp<br>les](https://github.com/lenve/javaboy-code-samples) |  | 公众号【江南一点雨】文章案例汇总，技术文章请戳这里-----> |
| [CVE-2019-3396](https://github.com/jas502n/CVE-2019-3396) |  | Confluence 未授权 RCE (CVE-2019-3396) 漏洞 |
| [chacal](https://github.com/p3tr0v/chacal) |  | Golang anti-vm framework for Red Team and Pentesters |
| [OscpStudyGroup](https://github.com/xuanhusec/OscpStudyGroup) |  | Oscp study group |
| [RustScan](https://github.com/RustScan/RustScan) | 2.1.1 | 🤖 The Modern Port Scanner 🤖 |
| [CVE-2020-6308-PoC](https://github.com/InitRoot/CVE-2020-6308-PoC) |  | PoC CVE-2020-6308 |
| [vulnerability](https://github.com/M00nBack/vulnerability) |  |  |
| [redis-rogue-serve<br>r-win](https://github.com/No-Github/redis-rogue-server-win) |  | Redis 4.x & 5.x RCE |
| [lazydocker](https://github.com/jesseduffield/lazydocker) | v0.23.1 | The lazier way to manage everything docker |
| [redis_lua_exploit](https://github.com/QAX-A-Team/redis_lua_exploit) |  |  |
| [7z2hashcat](https://github.com/philsmd/7z2hashcat) | 1.9 | extract information from password-protected .7z archives (and <br>.sfx files) such that you can crack these "hashes" with hashcat |
| [suricata-rules](https://github.com/sudohyak/suricata-rules) |  | Suricata rules for the new critical vulnerabilities |
| [CVE-2019-0192](https://github.com/mpgn/CVE-2019-0192) |  | RCE on Apache Solr using deserialization of untrusted data via<br> jmx.serviceUrl |
| [proxychains-ng](https://github.com/rofl0r/proxychains-ng) | v4.16 | proxychains ng (new generation) - a preloader which hooks call<br>s to sockets in dynamically linked programs and redirects it th<br>rough one or more socks/http proxies. continuation of the unmai<br>ntained proxychains project. the sf.net page is currently not u<br>pdated, use releases from github release page instead. |
| [isf](https://github.com/dark-lbp/isf) | v0.1.0 | ISF(Industrial Control System Exploitation Framework)，a explo<br>itation framework based on Python |
| [nyancat](https://github.com/klange/nyancat) | 1.2.1 | Nyancat in your terminal, rendered through ANSI escape sequenc<br>es. This is the source for the Debian package nyancat. |
| [Jenkins](https://github.com/blackye/Jenkins) |  | Jenkins漏洞探测、用户抓取爆破 |
| [ssti-payloads](https://github.com/payloadbox/ssti-payloads) |  | 🎯 Server Side Template Injection Payloads |
| [StandIn](https://github.com/FuzzySecurity/StandIn) | v1.3 | StandIn is a small .NET35/45 AD post-exploitation toolkit |
| [nps-auth-bypass](https://github.com/carr0t2/nps-auth-bypass) |  | nps认证绕过利用工具，CVE-2022-40494，使用此工具可在浏览器访问w<br>eb控制端后台页面，或者批量获取socks5和http代理 |
| [linux-kernel-expl<br>oits](https://github.com/SecWiki/linux-kernel-exploits) |  | linux-kernel-exploits Linux平台提权漏洞集合 |
| [forbidden](https://github.com/ivan-sincek/forbidden) | v10.2 | Bypass 4xx HTTP response status codes and more. Based on PycUR<br>L and Python Requests. |
| [htmlq](https://github.com/mgdm/htmlq) | v0.4.0 | Like jq, but for HTML. |
| [speedtest-cli](https://github.com/sivel/speedtest-cli) | v2.1.3 | Command line interface for testing internet bandwidth using sp<br>eedtest.net |
| [Ruoyi-All](https://github.com/passer-W/Ruoyi-All) |  |  |
| [CVE-2018-8174_EXP](https://github.com/Yt1g3r/CVE-2018-8174_EXP) |  | CVE-2018-8174_python |
| [evilzip](https://github.com/TheKingOfDuck/evilzip) | 1.1 | evilzip lets you create a zip file(with password) that contain<br>s files with directory traversal characters in their embedded p<br>ath. |
| [WinPmem](https://github.com/Velocidex/WinPmem) | v4.0.rc<br>1 | The multi-platform memory acquisition tool. |
| [CVE-2019-0708-EXP<br>-Windows](https://github.com/cbwang505/CVE-2019-0708-EXP-Windows) | 1.0 | CVE-2019-0708-EXP-Windows版单文件exe版,运行后直接在当前控制台<br>反弹System权限Shell |
| [fireprox](https://github.com/ustayready/fireprox) |  | AWS API Gateway management tool for creating on the fly HTTP p<br>ass-through proxies for unique IP rotation |
| [httprobe](https://github.com/tomnomnom/httprobe) | v0.2 | Take a list of domains and probe for working HTTP and HTTPS se<br>rvers |
| [Loki-bot](https://github.com/TheKingOfDuck/Loki-bot) |  | 多功能Windows机器运维管理工具 |
| [cidr-merger](https://github.com/zhanhb/cidr-merger) | v1.1.3 | A simple command line tool to merge ip/ip cidr/ip range, suppo<br>rts IPv4/IPv6 |
| [ew](https://github.com/idlefire/ew) |  | 内网穿透(跨平台) |
| [Havoc](https://github.com/HavocFramework/Havoc) |  | The Havoc Framework. |
| [open-vm-tools](https://github.com/vmware/open-vm-tools) | stable-<br>12.3.5 | Official repository of VMware open-vm-tools project |
| [Pass-to-hash-EWS](https://github.com/pentest-tools-public/Pass-to-hash-EWS) |  |  |
| [merlin](https://github.com/Ne0nd0g/merlin) | v2.0.0 | Merlin is a cross-platform post-exploitation HTTP/2 Command & <br>Control  server and agent written in golang. |
| [CVE-2017-11882](https://github.com/embedi/CVE-2017-11882) |  | Proof-of-Concept exploits for CVE-2017-11882 |
| [ShadowUser](https://github.com/An0nySec/ShadowUser) |  | 影子用户 克隆 |
| [ClashA](https://github.com/ccg2018/ClashA) | 0.0.3.9 | A Android GUI for Clash |
| [Weaver-OA-E-colog<br>y-Database-Leak](https://github.com/NS-Sp4ce/Weaver-OA-E-cology-Database-Leak) |  | 泛微OA数据库配置泄漏检测脚本 |
| [CloudUnflare](https://github.com/greycatz/CloudUnflare) |  | Reconnaissance Real IP address for Cloudflare Bypass |
| [CVE-2021-22005](https://github.com/r0ckysec/CVE-2021-22005) |  |  |
| [javasec_study](https://github.com/proudwind/javasec_study) |  | java代码审计学习笔记 |
| [Dirpath_List](https://github.com/DictionaryHouse/Dirpath_List) |  | Dirpath_List 目录扫描字典 |
| [rich](https://github.com/Textualize/rich) | v13.5.3 | Rich is a Python library for rich text and beautiful formattin<br>g in the terminal. |
| [how-does-SecureCR<br>T-encrypt-password](https://github.com/HyperSine/how-does-SecureCRT-encrypt-password) |  | Transferred from https://github.com/DoubleLabyrinth/how-does-S<br>ecureCRT-encrypt-password |
| [xpinyin](https://github.com/lxneng/xpinyin) |  | Translate Chinese hanzi to pinyin (拼音) by Python, 汉字转拼音 |
| [anchore-engine](https://github.com/anchore/anchore-engine) |  | A service that analyzes docker images and scans for vulnerabil<br>ities |
| [skyscorpion](https://github.com/shack2/skyscorpion) | 1.0.rel<br>ease.202<br>10322 | 新版将不再对外公开发布。天蝎权限管理工具采用Java平台的JavaFX技<br>术开发的桌面客户端，支持跨平台运行，目前基于JDK1.8开发，运行必须<br>安装JDK或JRE 1.8，注意不能是open jdk，只能是oracle的jdk。 天蝎权<br>限管理工具基于冰蝎加密流量进行WebShell通信管理的原理，目前实现了<br>jsp、aspx、php、asp端的常用操作功能，在原基础上，优化了大文件上<br>传下载、Socket代理的问题，修改了部分API接口代码。 |
| [CVE-2020-2551](https://github.com/hktalent/CVE-2020-2551) |  | how detect CVE-2020-2551 poc exploit python Weblogic RCE with <br>IIOP |
| [fav-up](https://github.com/pielco11/fav-up) | v0.2 | IP lookup by favicon using Shodan |
| [RedisModules-Exec<br>uteCommand-for-Win<br>dows](https://github.com/0671/RedisModules-ExecuteCommand-for-Windows) |  | 可在Windows下执行系统命令的Redis模块，可用于Redis主从复制攻击<br>。 |
| [CVE-2021-22205](https://github.com/inspiringz/CVE-2021-22205) |  | GitLab CE/EE Preauth RCE using ExifTool |
| [massh-enum](https://github.com/trimstray/massh-enum) |  | OpenSSH 2.3 up to 7.4 Mass Username Enumeration (CVE-2018-1547<br>3). |
| [suricata-rules](https://github.com/suricata-rules/suricata-rules) |  |  |
| [exrex](https://github.com/asciimoo/exrex) |  | Irregular methods on regular expressions |
| [wrk](https://github.com/wg/wrk) |  | Modern HTTP benchmarking tool |
| [cve-2017-7269](https://github.com/zcgonvh/cve-2017-7269) |  | fixed msf module for cve-2017-7269 |
| [all-about-apikey](https://github.com/daffainfo/all-about-apikey) |  | Detailed information about API key / OAuth token (Description,<br> Request, Response, Regex, Example) |
| [dirtycow-vdso](https://github.com/scumjr/dirtycow-vdso) |  | PoC for Dirty COW (CVE-2016-5195) |
| [ThinkPHP-Vuln](https://github.com/Mochazz/ThinkPHP-Vuln) |  | 关于ThinkPHP框架的历史漏洞分析集合 |
| [CVE-2019-7238](https://github.com/mpgn/CVE-2019-7238) |  | 🐱‍💻 Poc of CVE-2019-7238 - Nexus Repository Manager 3 Remot<br>e Code Execution 🐱‍💻 |
| [RedWarden](https://github.com/mgeeky/RedWarden) |  | Cobalt Strike C2 Reverse proxy that fends off Blue Teams, AVs,<br> EDRs, scanners through packet inspection and malleable profile<br> correlation |
| [Vegile](https://github.com/Screetsec/Vegile) |  | This tool will setting up your backdoor/rootkits when backdoor<br> already setup it will be hidden your spesisifc process,unlimit<br>ed your session in metasploit and transparent. Even when it kil<br>led, it will re-run again. There always be a procces which whil<br>e run another process,So we can assume that this procces is uns<br>topable like a Ghost in The Shell |
| [RedisWriteFile](https://github.com/r35tart/RedisWriteFile) |  | 通过 Redis 主从写出无损文件 |
| [CVE-2021-3156-plu<br>s](https://github.com/Rvn0xsy/CVE-2021-3156-plus) |  | CVE-2021-3156非交互式执行命令 |
| [security-bucket-b<br>rigade](https://github.com/databricks/security-bucket-brigade) |  |  |
| [rtsp_authgrinder](https://github.com/Tek-Security-Group/rtsp_authgrinder) |  | A authentication brute forcing tool for the rtsp protocol |
| [AboutSecurity](https://github.com/ffffffff0x/AboutSecurity) | v2 | Everything for pentest. | 用于渗透测试的 payload 和 bypass 字<br>典. |
| [DNSLog-Platform-G<br>olang](https://github.com/yumusb/DNSLog-Platform-Golang) | v0.3 | DNSLOG平台 golang |
| [passToJs](https://github.com/yaunsky/passToJs) |  | 爆破js加密的后台登陆；JS加密；爆破密码；PyExecJS |
| [tqdm](https://github.com/tqdm/tqdm) | v4.66.1 | :zap: A Fast, Extensible Progress Bar for Python and CLI |
| [list](https://github.com/publicsuffix/list) |  | The Public Suffix List |
| [lmg](https://github.com/halpomeranz/lmg) |  | Script for automating Linux memory capture and analysis |
| [ja3transport](https://github.com/CUCyber/ja3transport) |  | Impersonating JA3 signatures |
| [CVE-2022-2992](https://github.com/CsEnox/CVE-2022-2992) |  | Authenticated Remote Command Execution in Gitlab via GitHub im<br>port |
| [MQTT-Explorer](https://github.com/thomasnordquist/MQTT-Explorer) | v0.3.5 | An all-round MQTT client that provides a structured topic over<br>view |
| [JavaFileDict](https://github.com/f0ng/JavaFileDict) |  | Java应用的一些配置文件字典，来源于公开的字典与平时收集 |
| [awesome-oscp](https://github.com/0x4D31/awesome-oscp) |  | A curated list of awesome OSCP resources |
| [security](https://github.com/numirias/security) |  | Some of my security stuff and vulnerabilities. Nothing advance<br>d. More to come. |
| [fastjson_gadgets_<br>scanner](https://github.com/Lonely-night/fastjson_gadgets_scanner) |  |  |
| [snmpwn](https://github.com/hatlord/snmpwn) |  | An SNMPv3 User Enumerator and Attack tool |
| [PHP_INCLUDE_TO_SH<br>ELL_CHAR_DICT](https://github.com/wupco/PHP_INCLUDE_TO_SHELL_CHAR_DICT) |  |  |
| [jenv](https://github.com/jenv/jenv) | 0.5.6 | Manage your Java environment  |
| [docker_api_vul](https://github.com/Tycx2ry/docker_api_vul) |  | docker 未授权访问漏洞利用脚本 |
| [burp-UnicodeAutoD<br>ecode](https://github.com/KagamigawaMeguri/burp-UnicodeAutoDecode) |  | Burpsuite插件，Unicode自动转码为中文，提高测试效率。 |
| [apkleaks](https://github.com/dwisiswant0/apkleaks) | v2.6.1 | Scanning APK file for URIs, endpoints & secrets. |
| [shellcheck](https://github.com/koalaman/shellcheck) | v0.9.0 | ShellCheck, a static analysis tool for shell scripts |
| [check-virtual-mac<br>hine](https://github.com/Ast1rtes/check-virtual-machine) |  |  |
| [gogsownz](https://github.com/TheZ3ro/gogsownz) |  | Gogs CVEs |
| [FingerprintHub](https://github.com/0x727/FingerprintHub) | default | 侦查守卫(ObserverWard)的指纹库 |
| [Finger](https://github.com/aliyunav/Finger) |  | A tool for recognizing function symbol |
| [discuz-ml-rce](https://github.com/theLSA/discuz-ml-rce) |  | discuz ml rce |
| [patoolkit](https://github.com/pentesteracademy/patoolkit) | v1.0 | PA Toolkit is a collection of traffic analysis plugins focused<br> on security |
| [firmwalker](https://github.com/craigz28/firmwalker) |  | Script for searching the extracted firmware file system for go<br>odies! |
| [awesome-shodan-qu<br>eries](https://github.com/jakejarvis/awesome-shodan-queries) |  | 🔍 A collection of interesting, funny, and depressing search q<br>ueries to plug into shodan.io 👩‍💻 |
| [HFish](https://github.com/hacklcx/HFish) |  | 安全、可靠、简单、免费的企业级蜜罐 |
| [CANoodler](https://github.com/newaetech/CANoodler) |  | CANoolder: CAN to 3.3V logic level interface. Dumb. Cheap. Sim<br>ple. Pick 3. |
| [CVE-2019-8449](https://github.com/mufeedvh/CVE-2019-8449) |  | CVE-2019-8449 Exploit for Jira v2.1 - v8.3.4 |
| [EVTX-ATTACK-SAMPL<br>ES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) |  | Windows Events Attack Samples |
| [fuzz](https://github.com/Bo0oM/fuzz) |  |  |
| [ffuf-scripts](https://github.com/ffuf/ffuf-scripts) |  | Scripts to help with different ffuf tasks and workflows |
| [shiro-exploit](https://github.com/Ares-X/shiro-exploit) |  | Shiro反序列化利用工具，支持新版本(AES-GCM)Shiro的key爆破，配合<br>ysoserial，生成回显Payload |
| [CVE-2021-23132](https://github.com/HoangKien1020/CVE-2021-23132) |  | com_media allowed paths that are not intended for image upload<br>s to RCE |
| [LandrayDES](https://github.com/zhutougg/LandrayDES) | V1 | 蓝凌OA的前后台密码的加解密工具 |
| [Jsdir](https://github.com/Lopseg/Jsdir) |  | Jsdir is a Burp Suite extension that extracts hidden paths fro<br>m js files and beautifies it for further reading. |
| [mitm6](https://github.com/dirkjanm/mitm6) | v0.3.0 | pwning IPv4 via IPv6 |
| [GBByPass](https://github.com/czz1233/GBByPass) |  | 冰蝎 哥斯拉 WebShell bypass |
| [etcd](https://github.com/etcd-io/etcd) | v3.5.10 | Distributed reliable key-value store for the most critical dat<br>a of a distributed system |
| [SharPyShell](https://github.com/antonioCoco/SharPyShell) | v1.3.0 | SharPyShell - tiny and obfuscated ASP.NET webshell for C# web <br>applications |
| [PayloadsAllTheThi<br>ngs](https://github.com/swisskyrepo/PayloadsAllTheThings) | 3.0 | A list of useful payloads and bypass for Web Application Secur<br>ity and Pentest/CTF |
| [hello-world](https://github.com/docker-library/hello-world) |  |  |
| [CVE-2021-22555-Pi<br>peVersion](https://github.com/veritas501/CVE-2021-22555-PipeVersion) |  | CVE-2021-22555 exploit rewritten with pipe primitive |
| [SUDO_KILLER](https://github.com/TH3xACE/SUDO_KILLER) |  | A tool designed to exploit a privilege escalation vulnerabilit<br>y in the sudo program on Unix-like systems. It takes advantage <br>of a specific misconfiguration or flaw in sudo to gain elevated<br> privileges on the system, essentially allowing a regular user <br>to execute commands as the root user. |
| [dfimage](https://github.com/LanikSJ/dfimage) |  | Reverse-engineer a Dockerfile from a Docker image. |
| [RCE-Exploit-in-BI<br>G-IP](https://github.com/h4x0r-dz/RCE-Exploit-in-BIG-IP) |  |  |
| [Kali-learning-not<br>es](https://github.com/Keybird0/Kali-learning-notes) |  | Write down some kali learning notes |
| [CVE-2021-3156](https://github.com/blasty/CVE-2021-3156) |  |  |
| [stratus-red-team](https://github.com/DataDog/stratus-red-team) | v2.10.0 | :cloud: :zap: Granular, Actionable Adversary Emulation for the<br> Cloud |
| [s2-016-exp](https://github.com/OneSourceCat/s2-016-exp) |  | S2-016 Exploit && Scanner |
| [csirt](https://github.com/Spacial/csirt) |  |  |
| [MoreFind](https://github.com/mstxq17/MoreFind) | v1.5.5 | 一款用于快速导出URL、Domain和IP的小工具 |
| [xia_sql](https://github.com/smxiazi/xia_sql) | 3.3 | xia SQL (瞎注)  burp 插件 ，在每个参数后面填加一个单引号，两个<br>单引号，一个简单的判断注入小插件。 |
| [idcardgenerator](https://github.com/airob0t/idcardgenerator) | win_v1.<br>3 | 身份证图片生成工具 generate an id card picture |
| [csbruter](https://github.com/ryanohoro/csbruter) |  | Cobalt Strike team server password brute force tool |
| [danderspritz-evtx](https://github.com/fox-it/danderspritz-evtx) | v1.0 | Parse evtx files and detect use of the DanderSpritz eventloged<br>it module |
| [ProxyVulns](https://github.com/hosch3n/ProxyVulns) |  | [ProxyLogon] CVE-2021-26855 & CVE-2021-27065 Fixed RawIdentity<br> Bug Exploit. [ProxyOracle] CVE-2021-31195 & CVE-2021-31196 Exp<br>loit Chains. [ProxyShell] CVE-2021-34473 & CVE-2021-34523 & CVE<br>-2021-31207 Exploit Chains. |
| [Invoke-WCMDump](https://github.com/peewpw/Invoke-WCMDump) |  | PowerShell Script to Dump Windows Credentials from the Credent<br>ial Manager |
| [CAS_EXP](https://github.com/langligelang/CAS_EXP) | 0.0.1 | CAS 硬编码 远程代码执行漏洞 |
| [CVE-2022-0185-Pip<br>eVersion](https://github.com/veritas501/CVE-2022-0185-PipeVersion) |  | CVE-2022-0185 exploit rewritten with pipe primitive |
| [Hyuga](https://github.com/Buzz2d0/Hyuga) |  |  |
| [signature-base](https://github.com/Neo23x0/signature-base) | v2.0 | YARA signature and IOC database for my scanners and tools |
| [get_AV](https://github.com/r00tSe7en/get_AV) |  | Windows杀软在线对比辅助 |
| [psutil](https://github.com/giampaolo/psutil) |  | Cross-platform lib for process and system monitoring in Python |
| [OpenRedireX](https://github.com/devanshbatham/OpenRedireX) |  | A fuzzer for detecting open redirect vulnerabilities |
| [IIS-ShortName-Sca<br>nner](https://github.com/irsdl/IIS-ShortName-Scanner) |  | latest version of scanners for IIS short filename (8.3) disclo<br>sure vulnerability |
| [yaml-payload-for-<br>Win](https://github.com/bkfish/yaml-payload-for-Win) |  | 用于windows反弹shell的yaml-payload |
| [terraform](https://github.com/hashicorp/terraform) | v1.6.3 | Terraform enables you to safely and predictably create, change<br>, and improve infrastructure. It is a source-available tool tha<br>t codifies APIs into declarative configuration files that can b<br>e shared amongst team members, treated as code, edited, reviewe<br>d, and versioned. |
| [ZeroNights-HackQu<br>est-2016](https://github.com/GrrrDog/ZeroNights-HackQuest-2016) |  | 2 web tasks from ZeroNights HackQuest 2016 |
| [Internal-Monologu<br>e](https://github.com/eladshamir/Internal-Monologue) |  | Internal Monologue Attack: Retrieving NTLM Hashes without Touc<br>hing LSASS |
| [openvpn-install](https://github.com/Nyr/openvpn-install) |  | OpenVPN road warrior installer for Ubuntu, Debian, AlmaLinux, <br>Rocky Linux, CentOS and Fedora |
| [wait-for-it](https://github.com/vishnubob/wait-for-it) |  | Pure bash script to test and wait on the availability of a TCP<br> host and port |
| [Whonix](https://github.com/Whonix/Whonix) |  |  |
| [clusterd](https://github.com/hatRiot/clusterd) | 0.5 | application server attack toolkit |
| [WindowsElevation](https://github.com/Al1ex/WindowsElevation) |  | Windows Elevation(持续更新) |
| [BaiLu-SED-Tool](https://github.com/HongLuDianXue/BaiLu-SED-Tool) |  |  |
| [CVE-2021-40444](https://github.com/lockedbyte/CVE-2021-40444) |  | CVE-2021-40444 PoC |
| [RedGhost](https://github.com/d4rk007/RedGhost) |  | Linux post exploitation framework written in bash designed to <br>assist red teams in persistence, reconnaissance, privilege esca<br>lation and leaving no trace.  |
| [CSS-Exchange](https://github.com/microsoft/CSS-Exchange) | v23.11.<br>06.2048 | Exchange Server support tools and scripts |
| [MSSQL-Fileless-Ro<br>otkit-WarSQLKit](https://github.com/mindspoof/MSSQL-Fileless-Rootkit-WarSQLKit) |  | Bildiğiniz üzere uzun zamandır MSSQL üzerine çalışmalar yapmak<br>tayım. Bu yazımda uzun zamandır uğraştığım bir konuyu ele alaca<br>ğım, MSSQL Rootkit. Bildiğiniz üzere şimdiye kadar MS-SQL için <br>anlatılan post-exploitation işlemlerinin büyük çoğunluğu “xp_c<br>mdshell” ve “sp_OACreate” stored procedure’lerini kullanara<br>k anlatılır. Peki xp_cmdshell ve sp_OACreate stored procedure’<br>lerinin olmadığı bir MSSQL sunucusunun “sa” hesabını ele geçi<br>rmişsek, o sisteme girmekten vaz mı geçeceğiz? Tabii ki vazgeçm<br>ememiz gerekiyor. Bu makale “sa” hesabının yakalandığı ve “x<br>p_cmdshell”, “sp_OACreate”, “sp_OAMethod” vb. prosedürleri<br>n hiç birinin çalışmadığı bir senaryo düşünülerek kaleme alınmı<br>ştır. |
| [awesome-iocs](https://github.com/sroberts/awesome-iocs) |  | A collection of sources of indicators of compromise. |
| [nosferatu](https://github.com/kindtime/nosferatu) |  | Windows NTLM Authentication Backdoor |
| [dumpall](https://github.com/0xHJK/dumpall) | v0.4.0 | 一款信息泄漏利用工具，适用于.git/.svn/.DS_Store泄漏和目录列出 |
| [Shiro-721](https://github.com/3ndz/Shiro-721) |  |  |
| [ja3_4java](https://github.com/lafaspot/ja3_4java) |  |  Java library for SSL/TLS ja3 fingerprint |
| [wpa-dictionary](https://github.com/conwnet/wpa-dictionary) |  | WPA/WPA2 密码字典，用于 wifi 密码暴力破解 |
| [PHP_Code_Challeng<br>e](https://github.com/yaofeifly/PHP_Code_Challenge) |  | 总结一些php代码审计ctf练习题 |
| [Freeze](https://github.com/optiv/Freeze) | v1.3 | Freeze is a payload toolkit for bypassing EDRs using suspended<br> processes, direct syscalls, and alternative execution methods |
| [dedecmscan](https://github.com/lengjibo/dedecmscan) |  |  |
| [ctf-archives](https://github.com/sajjadium/ctf-archives) |  |  CTF Archives: Collection of CTF Challenges. |
| [gitleaks](https://github.com/zricethezav/gitleaks) |  |  |
| [sdk-api](https://github.com/MicrosoftDocs/sdk-api) |  | Public contributions for win32 API documentation |
| [burp-wildcard](https://github.com/hvqzao/burp-wildcard) | 1.08 | Burp extension intended to compact Burp extension tabs by hija<br>cking them to own tab. |
| [fish-shell](https://github.com/fish-shell/fish-shell) | 3.6.1 | The user-friendly command line shell. |
| [sql-injection-pay<br>load-list](https://github.com/payloadbox/sql-injection-payload-list) |  | 🎯 SQL Injection Payload List |
| [dirhunt](https://github.com/Nekmo/dirhunt) | v0.9.0 | Find web directories without bruteforce |
| [xss-payload-list](https://github.com/ismailtasdelen/xss-payload-list) |  |  |
| [zipcreater](https://github.com/Rvn0xsy/zipcreater) | v0.0.2 | ZipCreater主要应用于跨目录的文件上传漏洞的利用，它能够快速进行<br>压缩包生成。 |
| [retoolkit](https://github.com/mentebinaria/retoolkit) | 2023.10 | Reverse Engineer's Toolkit |
| [python-codext](https://github.com/dhondta/python-codext) |  | Python codecs extension featuring CLI tools for encoding/decod<br>ing anything |
| [CVE-2019-3396_EXP](https://github.com/Yt1g3r/CVE-2019-3396_EXP) |  | CVE-2019-3396 confluence SSTI RCE |
| [ModSecurity-nginx](https://github.com/SpiderLabs/ModSecurity-nginx) | v1.0.3 | ModSecurity v3 Nginx Connector |
| [Blasting_dictiona<br>ry](https://github.com/rootphantomer/Blasting_dictionary) |  | 爆破字典 |
| [Suborner](https://github.com/r4wd3r/Suborner) | 1.0.1 |  |
| [endlessh](https://github.com/skeeto/endlessh) | 1.0 | SSH tarpit that slowly sends an endless banner |
| [CMWTAT_Digital_Ed<br>ition](https://github.com/TGSAN/CMWTAT_Digital_Edition) | 2.7.1.0 | CloudMoe Windows 10/11 Activation Toolkit get digital license,<br> the best open source Win 10/11 activator in GitHub. GitHub 上<br>最棒的开源 Win10/Win11 数字权利（数字许可证）激活工具！ |
| [sliver](https://github.com/BishopFox/sliver) | v1.5.41 | Adversary Emulation Framework |
| [xortool](https://github.com/hellman/xortool) |  | A tool to analyze multi-byte xor cipher |
| [shellshock_scanne<br>r](https://github.com/scottjpack/shellshock_scanner) |  | Python Scanner for "ShellShock" (CVE-2014-6271) |
| [CallStranger](https://github.com/yunuscadirci/CallStranger) |  | Vulnerability checker for Callstranger (CVE-2020-12695) |
| [CVE-2021-22986](https://github.com/Al1ex/CVE-2021-22986) |  | CVE-2021-22986 & F5 BIG-IP RCE |
| [CVE-2021-44228-Po<br>C-log4j-bypass-wor<br>ds](https://github.com/Puliczek/CVE-2021-44228-PoC-log4j-bypass-words) |  | 🐱‍💻 ✂️ 🤬 CVE-2021-44228 - LOG4J Java exploit - WAF bypas<br>s tricks |
| [Paper](https://github.com/Cryin/Paper) |  | Web Security Technology & Vulnerability Analysis Whitepapers |
| [BruteShark](https://github.com/odedshimon/BruteShark) | v1.2.5 | Network Analysis Tool |
| [cupp](https://github.com/Mebus/cupp) |  | Common User Passwords Profiler (CUPP) |
| [CVE-2020-9548](https://github.com/fairyming/CVE-2020-9548) |  | CVE-2020-9548：FasterXML/jackson-databind 远程代码执行漏洞 |
| [HostCollision](https://github.com/pmiaowu/HostCollision) | HostCol<br>lision-2<br>.2.8 | 用于host碰撞而生的小工具,专门检测渗透中需要绑定hosts才能访问的<br>主机或内部系统 |
| [AngelSword](https://github.com/Lucifer1993/AngelSword) |  | Python3编写的CMS漏洞检测框架 |
| [fuxploider](https://github.com/almandin/fuxploider) | v1.0 | File upload vulnerability scanner and exploitation tool. |
| [CNVD-2022-10270-L<br>PE](https://github.com/Ryze-T/CNVD-2022-10270-LPE) | 2022-02<br>-24 | 基于向日葵RCE的本地权限提升，无需指定端口 |
| [InfinityHook](https://github.com/everdox/InfinityHook) |  | Hook system calls, context switches, page faults and more. |
| [poodle-PoC](https://github.com/mpgn/poodle-PoC) |  | :poodle: Poodle (Padding Oracle On Downgraded Legacy Encryptio<br>n) attack CVE-2014-3566 :poodle: |
| [NetLoader](https://github.com/Flangvik/NetLoader) |  | Loads any C# binary in mem, patching AMSI + ETW.  |
| [YourNextBugTip](https://github.com/giteshnxtlvl/YourNextBugTip) |  |  |
| [webapp-wordlists](https://github.com/p0dalirius/webapp-wordlists) |  | This repository contains wordlists for each versions of common<br> web applications and content management systems (CMS). Each ve<br>rsion contains a wordlist of all the files directories for this<br> version. |
| [monkey](https://github.com/guardicore/monkey) | v2.3.0 | Infection Monkey - An open-source adversary emulation platform |
| [TongdaOA-exp](https://github.com/z1un/TongdaOA-exp) |  | TongdaOA 11.7 ~11.8 通达OA，任意用户登录+后台getshell |
| [Benchmarks](https://github.com/re4lity/Benchmarks) |  |  |
| [aria2](https://github.com/aria2/aria2) | release<br>-1.36.0 | aria2 is a lightweight multi-protocol & multi-source, cross pl<br>atform download utility operated in command-line. It supports H<br>TTP/HTTPS, FTP, SFTP, BitTorrent and Metalink. |
| [foolav](https://github.com/hvqzao/foolav) | v1.0 | Pentest tool for antivirus evasion and running arbitrary paylo<br>ad on target Wintel host |
| [PLCinject](https://github.com/SCADACS/PLCinject) |  |  |
| [SessionGopher](https://github.com/Arvanaghi/SessionGopher) |  | SessionGopher is a PowerShell tool that uses WMI to extract sa<br>ved session information for remote access tools such as WinSCP,<br> PuTTY, SuperPuTTY, FileZilla, and Microsoft Remote Desktop. It<br> can be run remotely or locally. |
| [RS256-2-HS256](https://github.com/3v4Si0N/RS256-2-HS256) |  | JWT Attack to change the algorithm RS256 to HS256 |
| [Catch-Browser](https://github.com/SD-XD/Catch-Browser) |  | This is a crawler password tool |
| [windows_exploit_d<br>owser](https://github.com/akabe1/windows_exploit_dowser) |  | A simple tool which could be useful to identify the exploits a<br>fflicting a Windows OS |
| [CVE-2018-8581](https://github.com/WyAtu/CVE-2018-8581) |  | CVE-2018-8581 | Microsoft Exchange Server Elevation of Privile<br>ge Vulnerability |
| [AWSBucketDump](https://github.com/jordanpotti/AWSBucketDump) |  | Security Tool to Look For Interesting Files in S3 Buckets |
| [CVE-2021-31166](https://github.com/0vercl0k/CVE-2021-31166) | v1 | Proof of concept for CVE-2021-31166, a remote HTTP.sys use-aft<br>er-free triggered remotely. |
| [kostebek](https://github.com/esecuritylab/kostebek) | v1.2.0 |  |
| [fortify](https://github.com/liweibin123/fortify) |  | fortify内置规则加密破解 |
| [dirtycow](https://github.com/dirtycow/dirtycow) |  |  |
| [mipsAudit](https://github.com/t3ls/mipsAudit) |  | IDA  MIPS静态扫描脚本，汇编审计辅助脚本 |
| [Duckyspark](https://github.com/toxydose/Duckyspark) |  | Translator from USB-Rubber-Ducky payloads to a Digispark code. |
| [LiME](https://github.com/504ensicsLabs/LiME) | v1.9.1 | LiME (formerly DMD) is a Loadable Kernel Module (LKM), which a<br>llows the acquisition of volatile memory from Linux and Linux-b<br>ased devices, such as those powered by Android. The tool suppor<br>ts acquiring memory either to the file system of the device or <br>over the network. LiME is unique in that it is the first tool t<br>hat allows full memory captures from Android devices. It also m<br>inimizes its interaction between user and kernel space processe<br>s during acquisition, which allows it to produce memory capture<br>s that are more forensically sound than those of other tools de<br>signed for Linux memory acquisition. |
| [suricata-traffici<br>d](https://github.com/jasonish/suricata-trafficid) |  | Application and service identification rules for Suricata |
| [CNVD-2021-49104](https://github.com/bigsizeme/CNVD-2021-49104) |  | CNVD-2021-49104——泛微E-Office文件上传漏洞 |
| [CVE-2021-21985_Po<br>C](https://github.com/alt3kx/CVE-2021-21985_PoC) |  |  |
| [crc32](https://github.com/theonlypwner/crc32) | v0.1 | CRC32 tools: reverse, undo/rewind, and calculate hashes |
| [pwn_jenkins](https://github.com/gquere/pwn_jenkins) |  | Notes about attacking Jenkins servers |
| [CNVD-2020-10487-T<br>omcat-Ajp-lfi](https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi) |  | Tomcat-Ajp协议文件读取漏洞 |
| [CVE-2017-1000486](https://github.com/pimps/CVE-2017-1000486) |  | Primefaces <= 5.2.21, 5.3.8 or 6.0 - Remote Code Execution Exp<br>loit |
| [hotoloti](https://github.com/RealityNet/hotoloti) |  | documentation, scripts, tools related to Zena Forensics (http:<br>//blog.digital-forensics.it) |
| [Struts-S2-xxx](https://github.com/sie504/Struts-S2-xxx) |  | 整理收集Struts2漏洞环境 |
| [linux-exploit-sug<br>gester-2](https://github.com/jondonas/linux-exploit-suggester-2) |  | Next-Generation Linux Kernel Exploit Suggester |
| [CVE-2021-1727](https://github.com/klinix5/CVE-2021-1727) |  |  |
| [Joker](https://github.com/ZhuriLab/Joker) |  |  |
| [CVE-2017-1000353](https://github.com/vulhub/CVE-2017-1000353) | 1.1 | jenkins CVE-2017-1000353 POC |
| [BKScan](https://github.com/nccgroup/BKScan) |  | BlueKeep scanner supporting NLA |
| [usbrply](https://github.com/JohnDMcMaster/usbrply) |  | Replay USB messages from Wireshark (.cap) files |
| [peepdf](https://github.com/jesparza/peepdf) |  | Powerful Python tool to analyze PDF documents |
| [Evaluation_tools](https://github.com/lis912/Evaluation_tools) |  | 测评工具 |
| [CVE-2022-22972](https://github.com/horizon3ai/CVE-2022-22972) |  |  |
| [Convert-Invoke-Ke<br>rberoast](https://github.com/blacklanternsecurity/Convert-Invoke-Kerberoast) |  | Converts the output from Invoke-Kerberoast into hashcat format<br>. |
| [hackergame2021-wr<br>iteups](https://github.com/USTC-Hackergame/hackergame2021-writeups) |  | 中国科学技术大学第八届信息安全大赛的官方与非官方题解 |
| [anti-portscan](https://github.com/EtherDream/anti-portscan) |  | 使用 iptables 防止端口扫描 |
| [company-crawler](https://github.com/bouxinLou/company-crawler) |  |  |
| [CVE-Exploits](https://github.com/lockedbyte/CVE-Exploits) |  | PoC exploits for software vulnerabilities |
| [redis-rce](https://github.com/iSafeBlue/redis-rce) |  | Redis RCE 的几种方法 |
| [scrapy](https://github.com/scrapy/scrapy) | 2.11.0 | Scrapy, a fast high-level web crawling & scraping framework fo<br>r Python. |
| [struts-pwn_CVE-20<br>17-9805](https://github.com/mazen160/struts-pwn_CVE-2017-9805) |  | An exploit for Apache Struts CVE-2017-9805 |
| [Print-My-Shell](https://github.com/sameera-madushan/Print-My-Shell) |  | Python script wrote to automate the process of generating vari<br>ous reverse shells. |
| [LOG-HUB](https://github.com/ffffffff0x/LOG-HUB) |  | 日志分析库,nuclei 的另一种用法 |
| [awesome-serverles<br>s-security](https://github.com/puresec/awesome-serverless-security) |  | A curated list of awesome serverless security resources such a<br>s (e)books, articles, whitepapers, blogs and research papers. |
| [mijisou](https://github.com/entropage/mijisou) |  | Privacy-respecting metasearch engine |
| [CVE-2018-2894](https://github.com/LandGrey/CVE-2018-2894) |  | CVE-2018-2894 WebLogic Unrestricted File Upload Lead To RCE Ch<br>eck Script |
| [LaZagne](https://github.com/AlessandroZ/LaZagne) | v2.4.5 | Credentials recovery project |
| [DFA](https://github.com/Ldundun/DFA) |  |  |
| [dsq](https://github.com/multiprocessio/dsq) | v0.23.0 | Commandline tool for running SQL queries against JSON, CSV, Ex<br>cel, Parquet, and more. |
| [JavaCodeAudit](https://github.com/cn-panda/JavaCodeAudit) |  | Getting started with java code auditing  代码审计入门的小项目 |
| [windows_protocol](https://github.com/daikerSec/windows_protocol) |  |  |
| [MyTools](https://github.com/No4l/MyTools) |  |  |
| [ASWCrypter](https://github.com/AbedAlqaderSwedan1/ASWCrypter) |  | An Bash&Python Script For Generating Payloads that Bypasses Al<br>l Antivirus so far [FUD] |
| [collaborator-ever<br>ywhere](https://github.com/PortSwigger/collaborator-everywhere) |  | A Burp Suite Pro extension which augments your proxy traffic b<br>y injecting non-invasive headers designed to reveal backend sys<br>tems by causing pingbacks to Burp Collaborator |
| [wechat-backup](https://github.com/greycodee/wechat-backup) | v1.0.0 | 微信聊天记录持久化备份本地硬盘，释放手机存储空间。 |
| [wechat_info_colle<br>ct](https://github.com/ecat-sec/wechat_info_collect) |  |  |
| [hackbar2](https://github.com/Mr-xn/hackbar2) |  |  |
| [CVE-2021-37580](https://github.com/Liang2580/CVE-2021-37580) |  | CVE-2021-37580 |
| [how-does-navicat-<br>encrypt-password](https://github.com/HyperSine/how-does-navicat-encrypt-password) |  | Transferred from https://github.com/DoubleLabyrinth/how-does-n<br>avicat-encrypt-password |
| [crlfuzz](https://github.com/dwisiswant0/crlfuzz) | v1.4.1 | A fast tool to scan CRLF vulnerability written in Go |
| [soapui](https://github.com/SmartBear/soapui) | v5.7.2 | SoapUI is a free and open source cross-platform functional tes<br>ting solution for APIs and web services. |
| [struts2-057-exp](https://github.com/Ivan1ee/struts2-057-exp) |  | s2-057 最新漏洞分析和EXP脚本 |
| [webuploader-0](https://github.com/jas502n/webuploader-0) |  |  |
| [Linux_LPE_eBPF_CV<br>E-2021-3490](https://github.com/chompie1337/Linux_LPE_eBPF_CVE-2021-3490) |  |  |
| [ADFSRelay](https://github.com/praetorian-inc/ADFSRelay) | v1.0 | Proof of Concept Utilities Developed to Research NTLM Relaying<br> Attacks Targeting ADFS |
| [Sylas](https://github.com/Ryze-T/Sylas) | beta | 数据库综合利用工具 |
| [AllatoriCrack](https://github.com/lqs1848/AllatoriCrack) | 7.6.2 | 破解 Java 混淆工具 Allatori |
| [ide-honeypot](https://github.com/wendell1224/ide-honeypot) |  | 一款针对于IDE的反制蜜罐 IDE-honeypot |
| [CTF-Training](https://github.com/hongriSec/CTF-Training) |  | 收集各大比赛的题目和Writeup |
| [fastjson](https://github.com/alibaba/fastjson) | 1.2.83 | FASTJSON 2.0.x has been released, faster and more secure, reco<br>mmend you upgrade. |
| [peerflix](https://github.com/mafintosh/peerflix) |  | Streaming torrent client for node.js |
| [qqwry2mmdb](https://github.com/leolovenet/qqwry2mmdb) | 2023041<br>9 | 为 Wireshark 能使用纯真网络 IP 数据库(QQwry)而提供的格式转换工<br>具 |
| [TaskSchedulerMisc](https://github.com/zcgonvh/TaskSchedulerMisc) |  | Misc TaskScheduler Plays |
| [libssh-scanner](https://github.com/leapsecurity/libssh-scanner) |  |  |
| [Girsh](https://github.com/nodauf/Girsh) | v0.41 | Automatically spawn a reverse shell fully interactive for Linu<br>x or Windows victim |
| [CVE-2022-21907-ht<br>tp](https://github.com/p0dalirius/CVE-2022-21907-http) |  |  |
| [ysoserial](https://github.com/pwntester/ysoserial) |  | A proof-of-concept tool for generating payloads that exploit u<br>nsafe Java object deserialization. |
| [zoom_vulnerabilit<br>y_poc](https://github.com/JLLeitschuh/zoom_vulnerability_poc) |  |  |
| [ADCSPwn](https://github.com/bats3c/ADCSPwn) | ADCSPwn | A tool to escalate privileges in an active directory network b<br>y coercing authenticate from machine accounts and relaying to t<br>he certificate service. |
| [CVE-2018-13379](https://github.com/milo2012/CVE-2018-13379) |  | CVE-2018-13379 |
| [DirtyPipe-Android](https://github.com/polygraphene/DirtyPipe-Android) | 1.0.3 | Dirty Pipe root exploit for Android (Pixel 6) |
| [names](https://github.com/Debdut/names) |  |  |
| [ShadowCoerce](https://github.com/ShutdownRepo/ShadowCoerce) |  | MS-FSRVP coercion abuse PoC |
| [dnsAutoRebinding](https://github.com/Tr3jer/dnsAutoRebinding) |  | ssrf、ssrfIntranetFuzz、dnsRebinding、recordEncode、dnsPoisoni<br>ng、Support ipv4/ipv6 |
| [aeskeyfind](https://github.com/makomk/aeskeyfind) |  | Fork of aeskeyfind that knows more formats of AES key schedule |
| [linux-kernel-expl<br>oitation](https://github.com/xairy/linux-kernel-exploitation) |  | A collection of links related to Linux kernel security and exp<br>loitation |
| [katana](https://github.com/projectdiscovery/katana) | v1.0.4 | A next-generation crawling and spidering framework. |
| [Solr-SSRF](https://github.com/Henry4E36/Solr-SSRF) |  | Apache Solr SSRF(CVE-2021-27905) |
| [linuxprivchecker](https://github.com/sleventyeleven/linuxprivchecker) |  | linuxprivchecker.py -- a Linux Privilege Escalation Check Scri<br>pt |
| [struts-scan](https://github.com/Lucifer1993/struts-scan) |  | Python2编写的struts2漏洞全版本检测和利用工具 |
| [zmap](https://github.com/zmap/zmap) | v3.0.0 | ZMap is a fast single packet network scanner designed for Inte<br>rnet-wide network surveys. |
| [massdns](https://github.com/blechschmidt/massdns) | v1.0.0 | A high-performance DNS stub resolver for bulk lookups and reco<br>nnaissance (subdomain enumeration) |
| [dictionary](https://github.com/H4lo/dictionary) |  |  List of some dictionaries |
| [btop](https://github.com/aristocratos/btop) | v1.2.13 | A monitor of resources |
| [domain_screen](https://github.com/TheKingOfDuck/domain_screen) |  | 站点批量截图 |
| [e-cology-OA-SQL](https://github.com/AdministratorGithub/e-cology-OA-SQL) |  | 泛微 e-cology OA 前台SQL注入 |
| [CVE-2020-17144](https://github.com/zcgonvh/CVE-2020-17144) |  | weaponized tool for CVE-2020-17144 |
| [SMBGhost_RCE_PoC](https://github.com/chompie1337/SMBGhost_RCE_PoC) |  |  |
| [CVE-2021-4034-NoG<br>CC](https://github.com/EstamelGG/CVE-2021-4034-NoGCC) | v4.0 | CVE-2021-4034简单优化，以应对没有安装gcc和make的目标环境 |
| [SAP_EEM_CVE-2020-<br>6207](https://github.com/chipik/SAP_EEM_CVE-2020-6207) |  | PoC for CVE-2020-6207  (Missing Authentication Check in SAP So<br>lution Manager) |
| [client-side-proto<br>type-pollution](https://github.com/BlackFan/client-side-prototype-pollution) |  | Prototype Pollution and useful Script Gadgets |
| [broot](https://github.com/Canop/broot) | v1.28.1 | A new way to see and navigate directory trees : https://dystro<br>y.org/broot |
| [dnSpy](https://github.com/dnSpy/dnSpy) | v6.1.8 | .NET debugger and assembly editor |
| [CVE-2021-3493](https://github.com/briskets/CVE-2021-3493) |  | Ubuntu OverlayFS Local Privesc |
| [CVE-2021-1732-Exp<br>loit](https://github.com/KaLendsi/CVE-2021-1732-Exploit) |  | CVE-2021-1732 Exploit |
| [cas4](https://github.com/cL0und/cas4) |  |  |
| [awesome-jenkins-r<br>ce-2019](https://github.com/orangetw/awesome-jenkins-rce-2019) |  | There is no pre-auth RCE in Jenkins since May 2017, but this i<br>s the one! |
| [yongyou_nc_poc](https://github.com/kezibei/yongyou_nc_poc) |  |  |
| [aliyun-accesskey-<br>Tools](https://github.com/mrknow001/aliyun-accesskey-Tools) | v1.3 | 阿里云accesskey利用工具 |
| [cloud-native-secu<br>rity-book](https://github.com/Metarget/cloud-native-security-book) |  | 《云原生安全：攻防实践与体系构建》资料仓库 |
| [miniforge](https://github.com/conda-forge/miniforge) | 23.3.1-<br>1 | A conda-forge distribution. |
| [vipasswordict](https://github.com/xnohat/vipasswordict) |  | Vietnamese Password Dicts |
| [Realtek_switch_ha<br>cking](https://github.com/libc0607/Realtek_switch_hacking) |  | 折腾交换机 |
| [conote-community](https://github.com/phith0n/conote-community) |  |  |
| [Cas_Exploit](https://github.com/21superman/Cas_Exploit) |  |  |
| [JNDI-Injection-Ex<br>ploit](https://github.com/welk1n/JNDI-Injection-Exploit) | v1.0 | JNDI注入测试工具（A tool which generates JNDI links can start <br>several servers to exploit JNDI Injection vulnerability,like Ja<br>ckson,Fastjson,etc） |
| [vulnapp](https://github.com/hxer/vulnapp) |  | use docker to attack web as a demo |
| [learn-java-bug](https://github.com/hex0wn/learn-java-bug) |  |  |
| [nmap](https://github.com/nmap/nmap) |  | Nmap - the Network Mapper. Github mirror of official SVN repos<br>itory. |
| [solr-injection](https://github.com/veracode-research/solr-injection) |  | Apache Solr Injection Research |
| [k8s-CVE-2021-4355<br>7-poc](https://github.com/xvnpw/k8s-CVE-2021-43557-poc) |  | PoC for CVE-2021-43557 |
| [CVE-2020-8559](https://github.com/tdwyer/CVE-2020-8559) |  | This is a PoC exploit for CVE-2020-8559 Kubernetes Vulnerabili<br>ty  |
| [code-server](https://github.com/cdr/code-server) |  |  |
| [mscache](https://github.com/QAX-A-Team/mscache) |  | a tool to manipulate dcc(domain cached credentials) in windows<br> registry, based mainly on the work of mimikatz and impacket |
| [PrivescCheck](https://github.com/itm4n/PrivescCheck) |  | Privilege Escalation Enumeration Script for Windows |
| [CoreMailUploadRce](https://github.com/jimoyong/CoreMailUploadRce) |  | Coremail任意文件上传漏洞POC |
| [vulnd_xxe](https://github.com/TheTwitchy/vulnd_xxe) |  | A server vulnerable to XXE that can be used to test payloads u<br>sing the xxer tool. |
| [cve-2017-18635](https://github.com/ShielderSec/cve-2017-18635) |  | PoC for CVE-2017-18635 |
| [grafanaExp](https://github.com/A-D-Team/grafanaExp) | V1.1 | A exploit tool for Grafana Unauthorized arbitrary file reading<br> vulnerability (CVE-2021-43798), it can burst plugins / extract<br> secret_key / decrypt data_source info automatic. |
| [JWT4B](https://github.com/ozzi-/JWT4B) | 2.3 | JWT Support for Burp  |
| [fuzzdb](https://github.com/tennc/fuzzdb) | v0.3 | Dictionary of attack patterns and primitives for black-box app<br>lication fault injection and resource discovery. |
| [nginxconfig](https://github.com/digitalocean/nginxconfig) |  |  |
| [csvtk](https://github.com/shenwei356/csvtk) | v0.28.0 | A cross-platform, efficient and practical CSV/TSV toolkit in G<br>olang |
| [satellite](https://github.com/t94j0/satellite) | v0.0.4 | easy-to-use payload hosting |
| [CVE-2018-9995_dvr<br>_credentials](https://github.com/ezelf/CVE-2018-9995_dvr_credentials) |  | (CVE-2018-9995) Get DVR Credentials |
| [hashtopolis](https://github.com/s3inlc/hashtopolis) |  |  |
| [js-port-knocking](https://github.com/EtherDream/js-port-knocking) |  | Web 端口敲门的奇思妙想 |
| [Unix-Privilege-Es<br>calation-Exploits-<br>Pack](https://github.com/Kabot/Unix-Privilege-Escalation-Exploits-Pack) |  | Exploits for getting local root on Linux, BSD, AIX, HP-UX, Sol<br>aris, RHEL, SUSE etc. |
| [awvs13_batch_py3](https://github.com/test502git/awvs13_batch_py3) |  |  |
| [Mod_Rewrite_Autom<br>ation](https://github.com/cedowens/Mod_Rewrite_Automation) |  | Scripts to automate standing up apache2 with mod_rewrite in fr<br>ont of C2 servers. |
| [getsystem-offline](https://github.com/xpn/getsystem-offline) |  | Small tool to get a SYSTEM shell |
| [cobaltstrike-bof-<br>toolset](https://github.com/AttackTeamFamily/cobaltstrike-bof-toolset) |  |  |
| [Serverless-Goat](https://github.com/OWASP/Serverless-Goat) |  | OWASP ServerlessGoat: a serverless application demonstrating c<br>ommon serverless security flaws |
| [OA-tongda-RCE](https://github.com/jas502n/OA-tongda-RCE) |  | Office Anywhere网络智能办公系统 |
| [Proxylogon-exploi<br>t](https://github.com/sirpedrotavares/Proxylogon-exploit) |  | proxylogon exploit - CVE-2021-26857 |
| [HERCULES](https://github.com/EgeBalci/HERCULES) |  | HERCULES is a special payload generator that can bypass antivi<br>rus softwares.  |
| [kekeo](https://github.com/gentilkiwi/kekeo) | 2.2.0-2<br>0211214 | A little toolbox to play with Microsoft Kerberos in C |
| [cuckoo](https://github.com/cuckoosandbox/cuckoo) | 2.0.6 | Cuckoo Sandbox is an automated dynamic malware analysis system |
| [WTSRM](https://github.com/rad9800/WTSRM) |  | WTSRM |
| [altdns](https://github.com/infosec-au/altdns) |  | Generates permutations, alterations and mutations of subdomain<br>s and then resolves them |
| [impacket](https://github.com/SecureAuthCorp/impacket) |  |  |
| [blueming](https://github.com/bufsnake/blueming) | 2022080<br>20633 | 备份文件扫描，并自动进行下载 |
| [Blind-SSRF](https://github.com/0xAwali/Blind-SSRF) |  | Nuclei Templates to reproduce Cracking the lens's Research |
| [bluescan](https://github.com/fO-000/bluescan) |  |  |
| [CVE-2019-2890](https://github.com/jas502n/CVE-2019-2890) |  | CVE-2019-2890 WebLogic 反序列化RCE漏洞 |
| [pure-bash-bible](https://github.com/dylanaraps/pure-bash-bible) |  | 📖 A collection of pure bash alternatives to external processe<br>s. |
| [hackergame2018-wr<br>iteups](https://github.com/ustclug/hackergame2018-writeups) |  | Write-ups for hackergame 2018 |
| [xxx](https://github.com/xxx/xxx) |  |  |
| [BeRoot](https://github.com/AlessandroZ/BeRoot) | 1.0.1 | Privilege Escalation Project - Windows / Linux / Mac |
| [RedGuard](https://github.com/wikiZ/RedGuard) | 23.08.2<br>1 | RedGuard is a C2 front flow control tool,Can avoid Blue Teams,<br>AVs,EDRs check. |
| [CVE-2020-10199](https://github.com/aleenzz/CVE-2020-10199) |  | CVE-2020-10199 回显版本 |
| [SAP_RECON](https://github.com/chipik/SAP_RECON) |  | PoC for CVE-2020-6287, CVE-2020-6286 (SAP RECON vulnerability) |
| [solr_exploit](https://github.com/1135/solr_exploit) |  | Apache Solr远程代码执行漏洞(CVE-2019-0193) Exploit |
| [Kage](https://github.com/WayzDev/Kage) |  |  |
| [LsassSilentProces<br>sExit](https://github.com/deepinstinct/LsassSilentProcessExit) |  | Command line interface to dump LSASS memory to disk via Silent<br>ProcessExit |
| [CVE-2017-12149](https://github.com/jreppiks/CVE-2017-12149) |  | Jboss Java Deserialization RCE (CVE-2017-12149) |
| [motd](https://github.com/abcfy2/motd) |  | My funny motd config. Just for fun! |
| [duck2spark](https://github.com/mame82/duck2spark) |  | Converter for raw RubberDucky payloads to Digispark Arduino ID<br>E Sketch source. |
| [SMx](https://github.com/NEWPLAN/SMx) |  | 国家商用加密算法 SMx（SM2,SM3,SM4） |
| [Damn-Vulnerable-G<br>raphQL-Application](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application) | 2.1.2 | Damn Vulnerable GraphQL Application is an intentionally vulner<br>able implementation of Facebook's GraphQL technology, to learn <br>and practice GraphQL Security. |
| [WXDBDecrypt](https://github.com/Mr0x01/WXDBDecrypt) |  |  |
| [SMBGhost](https://github.com/ollypwn/SMBGhost) |  |  |
| [CiscoRV320Dump](https://github.com/0x27/CiscoRV320Dump) |  | CVE-2019-1652 /CVE-2019-1653 Exploits For Dumping Cisco RV320 <br>Configurations & Debugging Data AND Remote Root Exploit! |
| [CVE-2021-26084_Po<br>C](https://github.com/alt3kx/CVE-2021-26084_PoC) |  |  |
| [LinuxVolProfiles](https://github.com/KDPryor/LinuxVolProfiles) | 2.0 | Volatility Linux Profiles |
| [jieba](https://github.com/fxsjy/jieba) | v0.42.1 | 结巴中文分词 |
| [fd](https://github.com/sharkdp/fd) | v8.7.1 | A simple, fast and user-friendly alternative to 'find' |
| [awvs_script_decod<br>e](https://github.com/fnmsd/awvs_script_decode) |  | 解密好的AWVS10.5 data/script/目录下的脚本 |
| [zhuqingcode](https://github.com/zhuqingcode/zhuqingcode) |  |  |
| [Webshell_finder](https://github.com/chiruom/Webshell_finder) |  | 网站木马检测 |
| [xcdn](https://github.com/3xp10it/xcdn) |  | Try to find out the real ip behind cdn |
| [dnsenum](https://github.com/fwaeytens/dnsenum) | 1.2.4.2 | dnsenum is a perl script that enumerates DNS information |
| [Mind-Map](https://github.com/phith0n/Mind-Map) |  | 各种安全相关思维导图整理收集 |
| [EmailAll](https://github.com/Taonn/EmailAll) |  | EmailAll is a powerful Email Collect tool — 一款强大的邮箱收<br>集工具 |
| [generator-burp-ex<br>tension](https://github.com/rsrdesarrollo/generator-burp-extension) |  | Everything you need about Burp Extension Generation |
| [bash-tutorial](https://github.com/wangdoc/bash-tutorial) |  | Bash 教程 |
| [ios-malware](https://github.com/ashishb/ios-malware) |  | iOS malware samples |
| [ThinkCMF_getshell](https://github.com/jas502n/ThinkCMF_getshell) |  | ThinkCMF 框架上的任意内容包含漏洞 |
| [thc-hydra](https://github.com/vanhauser-thc/thc-hydra) | v9.5 | hydra |
| [CVE-2021-29200](https://github.com/r0ckysec/CVE-2021-29200) |  |  |
| [can-i-take-over-x<br>yz](https://github.com/EdOverflow/can-i-take-over-xyz) |  | "Can I take over XYZ?" — a list of services and how to claim <br>(sub)domains with dangling DNS records. |
| [waybackurls](https://github.com/tomnomnom/waybackurls) | v0.1.0 | Fetch all the URLs that the Wayback Machine knows about for a <br>domain |
| [XXEpayload](https://github.com/hackping/XXEpayload) |  |  |
| [JVWA](https://github.com/ffffffff0x/JVWA) |  | java 代码审计学习靶场 |
| [SHIRO-550](https://github.com/jas502n/SHIRO-550) |  | Shiro RememberMe 1.2.4 反序列化 漏洞 |
| [ntdsxtract](https://github.com/csababarta/ntdsxtract) |  | Active Directory forensic framework |
| [s3reverse](https://github.com/hahwul/s3reverse) | v1.0.1 | The format of various s3 buckets is convert in one format. for<br> bugbounty and security testing. |
| [SavvyCAN](https://github.com/collin80/SavvyCAN) | V213 | QT based cross platform canbus tool |
| [PrintNightmare](https://github.com/afwu/PrintNightmare) |  |  |
| [CVE-2020-0601](https://github.com/ollypwn/CVE-2020-0601) |  |  |
| [SimpleDnsCrypt](https://github.com/bitbeans/SimpleDnsCrypt) | 0.7.1 | A simple management tool for dnscrypt-proxy |
| [WeblogicScanLot](https://github.com/rabbitmask/WeblogicScanLot) |  | WeblogicScanLot系列，Weblogic漏洞批量检测工具，V2.2 |
| [Pentest-Windows](https://github.com/itm4n/Pentest-Windows) |  | Windows internals and exploitation tricks |
| [LuCI_RCE_exp](https://github.com/HACHp1/LuCI_RCE_exp) |  | Exp of cve-2019-12272 |
| [trevorc2](https://github.com/trustedsec/trevorc2) |  | TrevorC2 is a legitimate website (browsable) that tunnels clie<br>nt/server communications for covert command execution. |
| [fyne](https://github.com/fyne-io/fyne) | v2.4.1 | Cross platform GUI toolkit in Go inspired by Material Design |
| [From-System-autho<br>rity-to-Medium-aut<br>hority](https://github.com/3gstudent/From-System-authority-to-Medium-authority) |  | Penetration test |
| [CrackSleeve](https://github.com/ca3tie1/CrackSleeve) |  | 破解CS4.0 |
| [FinalShellDecodeP<br>ass](https://github.com/jas502n/FinalShellDecodePass) |  | FinalShellDecodePass 加密解密 |
| [katoolin](https://github.com/LionSec/katoolin) |  | Automatically install all Kali linux tools |
| [debugtron](https://github.com/bytedance/debugtron) |  |  |
| [RSA](https://github.com/Zui-Qing-Feng/RSA) |  |  |
| [CVE-2019-0708](https://github.com/k8gege/CVE-2019-0708) |  | 3389远程桌面代码执行漏洞CVE-2019-0708批量检测工具(Rdpscan Blue<br>keep Check) |
| [one_gadget](https://github.com/david942j/one_gadget) | v1.8.1 | The best tool for finding one gadget RCE in libc.so.6 |
| [gau](https://github.com/lc/gau) | v2.2.1 | Fetch known URLs from AlienVault's Open Threat Exchange, the W<br>ayback Machine, and Common Crawl. |
| [alive-progress](https://github.com/rsalmei/alive-progress) |  | A new kind of Progress Bar, with real-time throughput, ETA, an<br>d very cool animations! |
| [DFSCoerce](https://github.com/Wh04m1001/DFSCoerce) |  |  |
| [MobaXterm-Decrypt<br>or](https://github.com/xillwillx/MobaXterm-Decryptor) |  | MobaXterm Decryptor |
| [Nmap-Tools](https://github.com/SpiderLabs/Nmap-Tools) |  | SpiderLabs shared Nmap Tools |
| [CVE-2021-21974](https://github.com/Shadow0ps/CVE-2021-21974) |  | POC for CVE-2021-21974 VMWare ESXi RCE Exploit |
| [tphack](https://github.com/whirlwind110/tphack) |  | Thinkphp3/5 Log文件泄漏利用工具 |
| [basecrack](https://github.com/mufeedvh/basecrack) | v4.0 | Decode All Bases - Base Scheme Decoder |
| [JsRpc](https://github.com/jxhczhl/JsRpc) | v1.02 | 远程调用(rpc)浏览器方法，免去抠代码补环境 |
| [windows-exploits](https://github.com/73696e65/windows-exploits) |  | Used for the osce exam preparation |
| [msdat](https://github.com/quentinhardy/msdat) |  | MSDAT: Microsoft SQL Database Attacking Tool |
| [bypass_disablefun<br>c_via_LD_PRELOAD](https://github.com/yangyangwithgnu/bypass_disablefunc_via_LD_PRELOAD) |  | bypass disable_functions via LD_PRELOA  (no need /usr/sbin/sen<br>dmail) |
| [APTSimulator](https://github.com/NextronSystems/APTSimulator) | v0.9.4 | A toolset to make a system look as if it was the victim of an <br>APT attack |
| [spring-framework](https://github.com/spring-projects/spring-framework) | v6.0.13 | Spring Framework |
| [IPList](https://github.com/DeerCloud/IPList) |  |  |
| [morty](https://github.com/asciimoo/morty) |  | Privacy aware web content sanitizer proxy as a service |
| [LangNetworkTopolo<br>gy3](https://github.com/LangziFun/LangNetworkTopology3) |  |  |
| [SecLists](https://github.com/danielmiessler/SecLists) | 2023.2 | SecLists is the security tester's companion. It's a collection<br> of multiple types of lists used during security assessments, c<br>ollected in one place. List types include usernames, passwords,<br> URLs, sensitive data patterns, fuzzing payloads, web shells, a<br>nd many more. |
| [cobalt_strike_bot](https://github.com/evi1ox/cobalt_strike_bot) |  |  |
| [CVE-2022-3602](https://github.com/colmmacc/CVE-2022-3602) |  |  |
| [bucket-stream](https://github.com/eth0izzle/bucket-stream) |  | Find interesting Amazon S3 Buckets by watching certificate tra<br>nsparency logs. |
| [jsEncrypter](https://github.com/c0ny1/jsEncrypter) | 0.3.2 | 一个用于前端加密Fuzz的Burp Suite插件 |
| [CVE-2019-2615](https://github.com/chiaifan/CVE-2019-2615) |  |  |
| [solr_rce](https://github.com/jas502n/solr_rce) |  | Apache Solr RCE via Velocity template |
| [LLC](https://github.com/Macr0phag3/LLC) |  | Linux Log Cleaner (utmp, wtmp, btmp, lastlog) |
| [Wsdler](https://github.com/NetSPI/Wsdler) | 2.0.12 | WSDL Parser extension for Burp |
| [BlockRDPBrute](https://github.com/y11en/BlockRDPBrute) |  | [HIPS]RDP(3389)爆破防护 |
| [CVE-2020-0683](https://github.com/padovah4ck/CVE-2020-0683) |  | CVE-2020-0683 - Windows MSI “Installer service” Elevation of<br> Privilege |
| [tools](https://github.com/nullsecuritynet/tools) |  | Security and Hacking Tools, Exploits, Proof of Concepts, Shell<br>codes, Scripts. |
| [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) |  | Living Off The Land Binaries And Scripts - (LOLBins and LOLScr<br>ipts) |
| [cve-2021-34558](https://github.com/alexzorin/cve-2021-34558) |  |  |
| [pyscript](https://github.com/pyscript/pyscript) | 2023.11<br>.1 | Home Page: https://pyscript.net  Examples: https://pyscript.ne<br>t/examples |
| [WeChatUserDB](https://github.com/x1hy9/WeChatUserDB) |  | GetWeChat DBPassword&&UserInfo(获取PC数据库密码以及相关微信用<br>户信息支持多系统数据库解密) |
| [csdroid](https://github.com/linshaoSec/csdroid) |  | cs手机版的源码，此处不放源jar包，自行添加编译 |
| [CVE-2018-1111](https://github.com/knqyf263/CVE-2018-1111) |  | Environment for DynoRoot (CVE-2018-1111) |
| [color](https://github.com/fatih/color) | v1.16.0 | Color package for Go (golang) |
| [blackeye](https://github.com/thelinuxchoice/blackeye) |  |  |
| [jsencrypt](https://github.com/travist/jsencrypt) |  | A zero-dependency Javascript library to perform OpenSSL RSA En<br>cryption, Decryption, and Key Generation. |
| [ProcDump-for-Linu<br>x](https://github.com/Sysinternals/ProcDump-for-Linux) | 2.2 | A Linux version of the ProcDump Sysinternals tool |
| [SharpRDPLog](https://github.com/Adminisme/SharpRDPLog) | 0.1 | Windows rdp相关的登录记录导出工具，可用于后渗透中Windows服务器<br>的信息收集阶段。输出内容包括：本地rdp端口、mstsc缓存、cmdkey缓存<br>、登录成功、失败日志事件。 |
| [malleable-c2](https://github.com/threatexpress/malleable-c2) |  | Cobalt Strike Malleable C2 Design and Reference Guide |
| [APT_REPORT](https://github.com/blackorbird/APT_REPORT) |  | Interesting APT Report Collection And Some Special IOC |
| [FiraCode](https://github.com/tonsky/FiraCode) | 6.2 | Free monospaced font with programming ligatures |
| [how-to-exit-vim](https://github.com/hakluke/how-to-exit-vim) |  | Below are some simple methods for exiting vim. |
| [geye](https://github.com/lightless233/geye) | 1.2.0 | 🚀Faster Github Monitor🚀 |
| [ShadowSteal](https://github.com/HuskyHacks/ShadowSteal) |  | Pure Nim implementation for exploiting CVE-2021-36934, the Ser<br>iousSAM local privilege escalation |
| [PocCollect](https://github.com/nanshihui/PocCollect) |  | a plenty of poc based on python |
| [NATBypass](https://github.com/cw1997/NATBypass) |  | 一款lcx在golang下的实现, 可用于内网穿透, 建立TCP反弹隧道用以绕<br>过防火墙入站限制等, A tool for establish reverse tunnel for NAT <br>network environment and proxy, support all functions of lcx.exe |
| [SharpChromium](https://github.com/djhohnstein/SharpChromium) |  | .NET 4.0 CLR Project to retrieve Chromium data, such as cookie<br>s, history and saved logins. |
| [shakeitoff](https://github.com/jbaines-r7/shakeitoff) | AKB-Rel<br>ease | Windows MSI Installer LPE (CVE-2021-43883) |
| [funNLP](https://github.com/fighting41love/funNLP) |  | 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推<br>断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写<br>库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换<br>、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义<br>词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中<br>文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地<br>名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽<br>车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集<br>、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoN<br>LP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语<br>言百科知识图谱、清华大学人工智能技术系列报告、自然语言生成、NLU<br>太难了系列、自动对联数据及机器人、用户名黑名单列表、罪名法务名词<br>及分类模型、微信公众号语料、cs224n深度学习自然语言处理课程、中文<br>手写汉字识别、中文自然语言处理 语料/数据集、变量命名神器、分词语<br>料库+代码、任务型对话英文数据集、ASR 语音数据集 + 基于深度学习的<br>中文语音识别系统、笑声检测器、Microsoft多语言数字/单位/如日期时<br>间识别包、中华新华字典数据库及api(包括常用歇后语、成语、词语和汉<br>字)、文档图谱自动生成、SpaCy 中文模型、Common Voice语音识别数据<br>集新版、神经网络关系抽取、基于bert的命名实体识别、关键词(Keyphra<br>se)抽取包pke、基于医疗领域知识图谱的问答系统、基于依存句法与语<br>义角色标注的事件三元组抽取、依存句法分析4万句高质量标注数据、cno<br>cr：用来做中文OCR的Python3包、中文人物关系知识图谱项目、中文nlp<br>竞赛项目及代码汇总、中文字符数据、speech-aligner: 从“人声语音”<br>及其“语言文本”产生音素级别时间对齐标注的工具、AmpliGraph: 知识<br>图谱表示学习(Python)库：知识图谱概念链接预测、Scattertext 文本可<br>视化(python)、语言/知识表示工具：BERT & ERNIE、中文对比英文自然<br>语言处理NLP的区别综述、Synonyms中文近义词工具包、HarvestText领域<br>自适应文本挖掘工具（新词发现-情感分析-实体链接等）、word2word：(<br>Python)方便易用的多语言词-词对集：62种语言/3,564个多语言对、语<br>音识别语料生成工具：从具有音频/字幕的在线视频创建自动语音识别(AS<br>R)语料库、构建医疗实体识别的模型（包含词典和语料标注）、单文档<br>非监督的关键词抽取、Kashgari中使用gpt-2语言模型、开源的金融投资<br>数据提取工具、文本自动摘要库TextTeaser: 仅支持英文、人民日报语料<br>处理工具集、一些关于自然语言的基本模型、基于14W歌曲知识库的问答<br>尝试--功能包括歌词接龙and已知歌词找歌曲以及歌曲歌手歌词三角关系<br>的问答、基于Siamese bilstm模型的相似句子判定模型并提供训练数据集<br>和测试数据集、用Transformer编解码模型实现的根据Hacker News文章标<br>题自动生成评论、用BERT进行序列标记和文本分类的模板代码、LitBank<br>：NLP数据集——支持自然语言处理和计算人文学科任务的100部带标记英<br>文小说语料、百度开源的基准信息抽取系统、虚假新闻数据集、Facebook<br>: LAMA语言模型分析，提供Transformer-XL/BERT/ELMo/GPT预训练语言<br>模型的统一访问接口、CommonsenseQA：面向常识的英文QA挑战、中文知<br>识图谱资料、数据及工具、各大公司内部里大牛分享的技术文档 PDF 或<br>者 PPT、自然语言生成SQL语句（英文）、中文NLP数据增强（EDA）工具<br>、英文NLP数据增强工具 、基于医药知识图谱的智能问答系统、京东商品<br>知识图谱、基于mongodb存储的军事领域知识图谱问答项目、基于远监督<br>的中文关系抽取、语音情感分析、中文ULMFiT-情感分析-文本分类-语料<br>及模型、一个拍照做题程序、世界各国大规模人名库、一个利用有趣中文<br>语料库 qingyun 训练出来的中文聊天机器人、中文聊天机器人seqGAN、<br>省市区镇行政区划数据带拼音标注、教育行业新闻语料库包含自动文摘功<br>能、开放了对话机器人-知识图谱-语义理解-自然语言处理工具及数据、<br>中文知识图谱：基于百度百科中文页面-抽取三元组信息-构建中文知识图<br>谱、masr: 中文语音识别-提供预训练模型-高识别率、Python音频数据增<br>广库、中文全词覆盖BERT及两份阅读理解数据、ConvLab：开源多域端到<br>端对话系统平台、中文自然语言处理数据集、基于最新版本rasa搭建的对<br>话系统、基于TensorFlow和BERT的管道式实体及关系抽取、一个小型的证<br>券知识图谱/知识库、复盘所有NLP比赛的TOP方案、OpenCLaP：多领域开<br>源中文预训练语言模型仓库、UER：基于不同语料+编码器+目标任务的中<br>文预训练模型仓库、中文自然语言处理向量合集、基于金融-司法领域(兼<br>有闲聊性质)的聊天机器人、g2pC：基于上下文的汉语读音自动标记模块<br>、Zincbase 知识图谱构建工具包、诗歌质量评价/细粒度情感诗歌语料库<br>、快速转化「中文数字」和「阿拉伯数字」、百度知道问答语料库、基于<br>知识图谱的问答系统、jieba_fast 加速版的jieba、正则表达式教程、中<br>文阅读理解数据集、基于BERT等最新语言模型的抽取式摘要提取、Python<br>利用深度学习进行文本摘要的综合指南、知识图谱深度学习相关资料整理<br>、维基大规模平行文本语料、StanfordNLP 0.2.0：纯Python版自然语言<br>处理包、NeuralNLP-NeuralClassifier：腾讯开源深度学习文本分类工具<br>、端到端的封闭域对话系统、中文命名实体识别：NeuroNER vs. BertNER<br>、新闻事件线索抽取、2019年百度的三元组抽取比赛：“科学空间队”源<br>码、基于依存句法的开放域文本知识三元组抽取和知识库构建、中文的GP<br>T2训练代码、ML-NLP - 机器学习(Machine Learning)NLP面试中常考到<br>的知识点和代码实现、nlp4han:中文自然语言处理工具集(断句/分词/词<br>性标注/组块/句法分析/语义分析/NER/N元语法/HMM/代词消解/情感分析/<br>拼写检查、XLM：Facebook的跨语言预训练语言模型、用基于BERT的微调<br>和特征提取方法来进行知识图谱百度百科人物词条属性抽取、中文自然语<br>言处理相关的开放任务-数据集-当前最佳结果、CoupletAI - 基于CNN+Bi<br>-LSTM+Attention 的自动对对联系统、抽象知识图谱、MiningZhiDaoQAC<br>orpus - 580万百度知道问答数据挖掘项目、brat rapid annotation to<br>ol: 序列标注工具、大规模中文知识图谱数据：1.4亿实体、数据增强在<br>机器翻译及其他nlp任务中的应用及效果、allennlp阅读理解:支持多种数<br>据和模型、PDF表格数据提取工具 、 Graphbrain：AI开源软件库和科研<br>工具，目的是促进自动意义提取和文本理解以及知识的探索和推断、简历<br>自动筛选系统、基于命名实体识别的简历自动摘要、中文语言理解测评基<br>准，包括代表性的数据集&基准模型&语料库&排行榜、树洞 OCR 文字识别<br> 、从包含表格的扫描图片中识别表格和文字、语声迁移、Python口语自<br>然语言处理工具集(英文)、 similarity：相似度计算工具包，java编写<br>、海量中文预训练ALBERT模型 、Transformers 2.0 、基于大规模音频数<br>据集Audioset的音频增强 、Poplar：网页版自然语言标注工具、图片文<br>字去除，可用于漫画翻译 、186种语言的数字叫法库、Amazon发布基于知<br>识的人-人开放领域对话数据集 、中文文本纠错模块代码、繁简体转换 <br>、 Python实现的多种文本可读性评价指标、类似于人名/地名/组织机构<br>名的命名体识别数据集 、东南大学《知识图谱》研究生课程(资料)、. <br>英文拼写检查库 、 wwsearch是企业微信后台自研的全文检索引擎、CHAM<br>ELEON：深度学习新闻推荐系统元架构 、 8篇论文梳理BERT相关模型进<br>展与反思、DocSearch：免费文档搜索引擎、 LIDA：轻量交互式对话标注<br>工具 、aili - the fastest in-memory index in the East 东半球最快<br>并发索引 、知识图谱车音工作项目、自然语言生成资源大全 、中日韩分<br>词库mecab的Python接口库、中文文本摘要/关键词提取、汉字字符特征提<br>取器 (featurizer)，提取汉字的特征（发音特征、字形特征）用做深度<br>学习的特征、中文生成任务基准测评 、中文缩写数据集、中文任务基准<br>测评 - 代表性的数据集-基准(预训练)模型-语料库-baseline-工具包-排<br>行榜、PySS3：面向可解释AI的SS3文本分类器机器可视化工具 、中文NLP<br>数据集列表、COPE - 格律诗编辑程序、doccano：基于网页的开源协同多<br>语言文本标注工具 、PreNLP：自然语言预处理库、简单的简历解析器，<br>用来从简历中提取关键信息、用于中文闲聊的GPT2模型：GPT2-chitchat<br>、基于检索聊天机器人多轮响应选择相关资源列表(Leaderboards、Datas<br>ets、Papers)、(Colab)抽象文本摘要实现集锦(教程 、词语拼音数据、<br>高效模糊搜索工具、NLP数据增广资源集、微软对话机器人框架 、 GitHu<br>b Typo Corpus：大规模GitHub多语言拼写错误/语法错误数据集、TextC<br>luster：短文本聚类预处理模块 Short text cluster、面向语音识别的<br>中文文本规范化、BLINK：最先进的实体链接库、BertPunc：基于BERT的<br>最先进标点修复模型、Tokenizer：快速、可定制的文本词条化库、中文<br>语言理解测评基准，包括代表性的数据集、基准(预训练)模型、语料库、<br>排行榜、spaCy 医学文本挖掘与信息提取 、 NLP任务示例项目代码集、 <br>python拼写检查库、chatbot-list - 行业内关于智能客服、聊天机器人<br>的应用和架构、算法分享和介绍、语音质量评价指标(MOSNet, BSSEval, <br>STOI, PESQ, SRMR)、 用138GB语料训练的法文RoBERTa预训练语言模型 <br>、BERT-NER-Pytorch：三种不同模式的BERT中文NER实验、无道词典 - 有<br>道词典的命令行版本，支持英汉互查和在线查询、2019年NLP亮点回顾、 <br>Chinese medical dialogue data 中文医疗对话数据集 、最好的汉字数<br>字(中文数字)-阿拉伯数字转换工具、 基于百科知识库的中文词语多词义<br>/义项获取与特定句子词语语义消歧、awesome-nlp-sentiment-analysis<br> - 情感分析、情绪原因识别、评价对象和评价词抽取、LineFlow：面向<br>所有深度学习框架的NLP数据高效加载器、中文医学NLP公开资源整理 、M<br>edQuAD：(英文)医学问答数据集、将自然语言数字串解析转换为整数和<br>浮点数、Transfer Learning in Natural Language Processing (NLP) <br>、面向语音识别的中文/英文发音辞典、Tokenizers：注重性能与多功能<br>性的最先进分词器、CLUENER 细粒度命名实体识别 Fine Grained Named <br>Entity Recognition、 基于BERT的中文命名实体识别、中文谣言数据库<br>、NLP数据集/基准任务大列表、nlp相关的一些论文及代码, 包括主题模<br>型、词向量(Word Embedding)、命名实体识别(NER)、文本分类(Text Cla<br>ssificatin)、文本生成(Text Generation)、文本相似性(Text Similar<br>ity)计算等，涉及到各种与nlp相关的算法，基于keras和tensorflow 、<br>Python文本挖掘/NLP实战示例、 Blackstone：面向非结构化法律文本的<br>spaCy pipeline和NLP模型通过同义词替换实现文本“变脸” 、中文 预<br>训练 ELECTREA 模型: 基于对抗学习 pretrain Chinese Model 、albert<br>-chinese-ner - 用预训练语言模型ALBERT做中文NER 、基于GPT2的特定<br>主题文本生成/文本增广、开源预训练语言模型合集、多语言句向量包、<br>编码、标记和实现：一种可控高效的文本生成方法、 英文脏话大列表 、<br>attnvis：GPT2、BERT等transformer语言模型注意力交互可视化、CoVoS<br>T：Facebook发布的多语种语音-文本翻译语料库，包括11种语言(法语、<br>德语、荷兰语、俄语、西班牙语、意大利语、土耳其语、波斯语、瑞典语<br>、蒙古语和中文)的语音、文字转录及英文译文、Jiagu自然语言处理工具<br> - 以BiLSTM等模型为基础，提供知识图谱关系抽取 中文分词 词性标注<br> 命名实体识别 情感分析 新词发现 关键词 文本摘要 文本聚类等功能<br>、用unet实现对文档表格的自动检测，表格重建、NLP事件提取文献资源<br>列表 、 金融领域自然语言处理研究资源大列表、CLUEDatasetSearch - <br>中英文NLP数据集：搜索所有中文NLP数据集，附常用英文NLP数据集 、me<br>dical_NER - 中文医学知识图谱命名实体识别 、(哈佛)讲因果推理的免<br>费书、知识图谱相关学习资料/数据集/工具资源大列表、Forte：灵活强<br>大的自然语言处理pipeline工具集 、Python字符串相似性算法库、PyLai<br>a：面向手写文档分析的深度学习工具包、TextFooler：针对文本分类/<br>推理的对抗文本生成模块、Haystack：灵活、强大的可扩展问答(QA)框架<br>、中文关键短语抽取工具 |
| [onedrive_user_enu<br>m](https://github.com/nyxgeek/onedrive_user_enum) |  | onedrive user enumeration - pentest tool to enumerate valid o3<br>65 users |
| [ShellcodeWrapper](https://github.com/Arno0x/ShellcodeWrapper) |  | Shellcode wrapper with encryption for multiple target language<br>s |
| [crawlergo](https://github.com/0Kee-Team/crawlergo) |  |  |
| [poc-cve-2018-1273](https://github.com/wearearima/poc-cve-2018-1273) |  | POC for CVE-2018-1273 |
| [Yara-rules](https://github.com/bartblaze/Yara-rules) |  | Collection of private Yara rules. |
| [ExchangeRelayX](https://github.com/quickbreach/ExchangeRelayX) |  | An NTLM relay tool to the EWS endpoint for on-premise exchange<br> servers. Provides an OWA for hackers. |
| [TongDa-OA](https://github.com/OA-HUNTER/TongDa-OA) |  | 通达OA一些漏洞点 |
| [tyton](https://github.com/nbulischeck/tyton) | v1.2 | Kernel-Mode Rootkit Hunter |
| [ja3](https://github.com/salesforce/ja3) |  | JA3 is a standard for creating SSL client fingerprints in an e<br>asy to produce and shareable way. |
| [RdpThief_tools](https://github.com/hmoytx/RdpThief_tools) |  |  窃取mstsc中的用户明文凭据 |
| [PRET](https://github.com/RUB-NDS/PRET) |  | Printer Exploitation Toolkit - The tool that made dumpster div<br>ing obsolete. |
| [VpsEnvInstall](https://github.com/fuzz-security/VpsEnvInstall) |  | 一键部署渗透VPS |
| [DangerousSpamWord<br>s](https://github.com/adlered/DangerousSpamWords) |  | :notes:超轻量的中文敏感字、敏感词库，字典词典，超低误识别率，<br>另提供API调用 |
| [golang-developer-<br>roadmap-cn](https://github.com/Quorafind/golang-developer-roadmap-cn) |  | 在 2019 成为一名 Go 开发者的路线图。为学习 Go 的人而准备。 |
| [pydictor](https://github.com/LandGrey/pydictor) | v2.0.5 | A powerful and useful hacker dictionary builder for a brute-fo<br>rce attack |
| [Alphalog](https://github.com/AlphabugX/Alphalog) | 1.0.0.R<br>elease | DNSLOG、httplog、rmilog、ldaplog、jndi 等都支持,完全匿名 产品(<br>fuzz.red)，Alphalog与传统DNSLog不同，更快、更安全。 |
| [CVE-2020-14756](https://github.com/Y4er/CVE-2020-14756) |  | WebLogic T3/IIOP RCE ExternalizableHelper.class of coherence.j<br>ar |
| [ruler](https://github.com/sensepost/ruler) | 2.4.1 | A tool to abuse Exchange services |
| [poc](https://github.com/tenable/poc) |  | Proof of Concepts |
| [CVE-2020-1350-DoS](https://github.com/maxpl0it/CVE-2020-1350-DoS) |  | A denial-of-service proof-of-concept for CVE-2020-1350 |
| [Diamorphine](https://github.com/m0nad/Diamorphine) |  | LKM rootkit for Linux Kernels 2.6.x/3.x/4.x/5.x/6.x (x86/x86_6<br>4 and ARM64) |
| [python-pinyin](https://github.com/mozillazg/python-pinyin) | v0.49.0 | 汉字转拼音(pypinyin) |
| [TLS-poison](https://github.com/ZeddYu/TLS-poison) |  |  |
| [VTSCAN](https://github.com/TheSecondSun/VTSCAN) |  |  |
| [batch_ping](https://github.com/caucy/batch_ping) |  | support multi ping |
| [sam-the-admin](https://github.com/WazeHell/sam-the-admin) |  |  |
| [qrazybox](https://github.com/Merricx/qrazybox) |  | QR Code Analysis and Recovery Toolkit |
| [clairvoyance](https://github.com/nikitastupin/clairvoyance) | v2.5.3 | Obtain GraphQL API schema even if the introspection is disable<br>d |
| [HandleKatz](https://github.com/codewhitesec/HandleKatz) |  | PIC lsass dumper using cloned handles |
| [Windows-Exploit-S<br>uggester](https://github.com/AonCyberLabs/Windows-Exploit-Suggester) |  | This tool compares a targets patch levels against the Microsof<br>t vulnerability database in order to detect potential missing p<br>atches on the target. It also notifies the user if there are pu<br>blic exploits and Metasploit modules available for the missing <br>bulletins. |
| [JSONP-Hunter](https://github.com/p1g3/JSONP-Hunter) |  | JSONP Hunter in burpsuite. |
| [httpx](https://github.com/projectdiscovery/httpx) | v1.3.7 | httpx is a fast and multi-purpose HTTP toolkit that allows run<br>ning multiple probes using the retryablehttp library. |
| [Exploit-Framework](https://github.com/WangYihang/Exploit-Framework) |  | :fire: An Exploit framework for Web Vulnerabilities written in<br> Python |
| [jwtcat](https://github.com/aress31/jwtcat) |  | A CPU-based JSON Web Token (JWT) cracker and - to some extent <br>- scanner. |
| [proxyshell-poc](https://github.com/dmaasland/proxyshell-poc) |  |  |
| [patator](https://github.com/lanjelot/patator) |  | Patator is a multi-purpose brute-forcer, with a modular design<br> and a flexible usage. |
| [S2-056-XStream](https://github.com/iBearcat/S2-056-XStream) |  |  |
| [GraphQLmap](https://github.com/swisskyrepo/GraphQLmap) |  | GraphQLmap is a scripting engine to interact with a graphql en<br>dpoint for pentesting purposes. - Do not use for illegal testin<br>g ;) |
| [CVE-2020-5902](https://github.com/jas502n/CVE-2020-5902) |  | CVE-2020-5902 BIG-IP |
| [SM2Java](https://github.com/PopezLotado/SM2Java) |  | 国密SM2,SM3 Java实现 |
| [CVE-2018-1111](https://github.com/kkirsche/CVE-2018-1111) |  | CVE-2018-1111 DynoRoot |
| [Malbox](https://github.com/G4rb3n/Malbox) |  | 恶意软件容器靶机 |
| [SaiDict](https://github.com/Stardustsky/SaiDict) |  | 弱口令,敏感目录,敏感文件等渗透测试常用攻击字典 |
| [john](https://github.com/openwall/john) |  | John the Ripper jumbo - advanced offline password cracker, whi<br>ch supports hundreds of hash and cipher types, and runs on many<br> operating systems, CPUs, GPUs, and even some FPGAs |
| [KodExplorer](https://github.com/kalcaddle/KodExplorer) | 4.51.03 | A web based file manager,web IDE / browser based code editor |
| [reverse-shell](https://github.com/lukechilds/reverse-shell) |  | Reverse Shell as a Service |
| [CVE-2020-17144-EX<br>P](https://github.com/Airboi/CVE-2020-17144-EXP) |  | Exchange2010 authorized RCE |
| [WSPIH](https://github.com/jerrychan807/WSPIH) |  | Website Sensitive Personal Information Hunter 网站个人敏感信息<br>文件扫描器 |
| [CVE-2020-36179](https://github.com/Al1ex/CVE-2020-36179) |  | CVE-2020-36179~82  Jackson-databind SSRF&RCE |
| [CVE-2020-6287-exp<br>loit](https://github.com/duc-nt/CVE-2020-6287-exploit) |  | PoC for CVE-2020-6287  The PoC in python for add user only, no<br> administrator permission set. Inspired by @zeroSteiner from me<br>tasploit. Original Metasploit PR module: https://github.com/rap<br>id7/metasploit-framework/pull/13852/commits/d1e2c75b3eafa7f62a6<br>aba9fbe6220c8da97baa8 This PoC only create user with unauthenti<br>cation permission and no more administrator permission set. Thi<br>s project is created only for educational purposes and cannot b<br>e used for law violation or personal gain. The author of this p<br>roject is not responsible for any possible harm caused by the m<br>aterials of this project. Original finding: CVE-2020-6287: Pabl<br>o Artuso CVE-2020-6286: Yvan 'iggy' G.  Usage: python sap-CVE-2<br>020-6287-add-user.py <HTTP(s)://IP:Port |
| [flashsploit](https://github.com/thewhiteh4t/flashsploit) |  | Exploitation Framework for ATtiny85 Based HID Attacks |
| [CVE-2017-12617](https://github.com/cyberheartmi9/CVE-2017-12617) |  | Apache Tomcat < 9.0.1 (Beta) / < 8.5.23 / < 8.0.47 / < 7.0.8 -<br> JSP Upload Bypass / Remote Code Execution  |
| [joomscan](https://github.com/rezasp/joomscan) |  |  |
| [jwt-fuzzer](https://github.com/andresriancho/jwt-fuzzer) |  | JWT fuzzer |
| [AssetScan](https://github.com/JE2Se/AssetScan) |  | 资产探测工具，检测存活，检测风险端口，常规端口，全端口探测等等<br>，对探测的端口的脆弱面进行安全分析进行 |
| [Starkiller](https://github.com/BC-SECURITY/Starkiller) | v2.6.1 | Starkiller is a Frontend for PowerShell Empire. |
| [go-strip](https://github.com/boy-hack/go-strip) | v3.0 | 清除Go编译时自带的信息 |
| [ripple20](https://github.com/corelight/ripple20) |  | A Zeek package for the passive detection of "Ripple20" vulnera<br>bilities in the Treck TCP/IP stack. |
| [BadDNS](https://github.com/joinsec/BadDNS) | v1.0.1 |  |
| [phuip-fpizdam](https://github.com/neex/phuip-fpizdam) |  | Exploit for CVE-2019-11043 |
| [python_code_audit](https://github.com/MisakiKata/python_code_audit) |  | python 代码审计项目 |
| [cryptovenom](https://github.com/lockedbyte/cryptovenom) |  |  |
| [hey](https://github.com/rakyll/hey) | v0.1.4 | HTTP load generator, ApacheBench (ab) replacement |
| [CobaltStrikeParse<br>r](https://github.com/Sentinel-One/CobaltStrikeParser) |  |  |
| [CVE-2020-35728](https://github.com/Al1ex/CVE-2020-35728) |  |  CVE-2020-35728 & Jackson-databind RCE |
| [slowloris](https://github.com/llaera/slowloris) |  |  |
| [test](https://github.com/3gstudent/test) | ysoseri<br>al-0.0.6<br>-SNAPSHO<br>T | just test |
| [springfox](https://github.com/springfox/springfox) | 3.0.0 | Automated JSON API documentation for API's built with Spring |
| [cobaltstrike-suri<br>cata-rules](https://github.com/ainrm/cobaltstrike-suricata-rules) |  | 17条检测cobaltstrike的suricata-ids规则 |
| [bypass-403](https://github.com/iamj0ker/bypass-403) |  | A simple script just made for self use for bypassing 403 |
| [shadow-tls](https://github.com/ihciah/shadow-tls) | v0.2.23 | A proxy to expose real tls handshake to the firewall |
| [metasploit-framew<br>ork](https://github.com/rapid7/metasploit-framework) |  | Metasploit Framework |
| [go-dork](https://github.com/dwisiswant0/go-dork) | v1.0.2 | The fastest dork scanner written in Go. |
| [Fofa-collect](https://github.com/FishM4n/Fofa-collect) |  |  |
| [kernel-exploit-fa<br>ctory](https://github.com/bsauce/kernel-exploit-factory) |  | Linux kernel CVE exploit analysis report and relative debug en<br>vironment. You don't need to compile Linux kernel and configure<br> your environment anymore.  |
| [druid_sessions](https://github.com/yuyan-sec/druid_sessions) | 1.2 | 获取 alibaba druid 一些 sessions , sql , urls |
| [GitGot](https://github.com/BishopFox/GitGot) |  | Semi-automated, feedback-driven tool to rapidly search through<br> troves of public data on GitHub for sensitive secrets. |
| [PowerUpSQL](https://github.com/NetSPI/PowerUpSQL) |  | PowerUpSQL: A PowerShell Toolkit for Attacking SQL Server |
| [http-request-smug<br>gler](https://github.com/PortSwigger/http-request-smuggler) |  |  |
| [Prowl](https://github.com/nettitude/Prowl) |  |  |
| [qsreplace](https://github.com/tomnomnom/qsreplace) | v0.0.3 | Accept URLs on stdin, replace all query string values with a u<br>ser-supplied value |
| [odoh-server-go](https://github.com/cloudflare/odoh-server-go) |  |  |
| [OSCP_note](https://github.com/Ondrik8/OSCP_note) |  |  |
| [CVE-2017-17562](https://github.com/ivanitlearning/CVE-2017-17562) |  | Standalone Python 3 exploit for CVE-2017-17562 |
| [vmware_vcenter_cv<br>e_2020_3952](https://github.com/guardicore/vmware_vcenter_cve_2020_3952) |  | Exploit for CVE-2020-3952 in vCenter 6.7 |
| [CVE-2019-2890](https://github.com/SukaraLin/CVE-2019-2890) |  |  |
| [rundeck](https://github.com/rundeck/rundeck) | v4.17.3 | Enable Self-Service Operations: Give specific users access to <br>your existing tools, services, and scripts |
| [nginx-ssl-ja3](https://github.com/fooinha/nginx-ssl-ja3) | v0.0.2 | nginx module for SSL/TLS ja3 fingerprint. |
| [BlueLotus_XSSRece<br>iver](https://github.com/firesunCN/BlueLotus_XSSReceiver) |  |  |
| [Serverless-Top-10<br>-Project](https://github.com/OWASP/Serverless-Top-10-Project) | 1.0 | OWASP Serverless Top 10 |
| [base100](https://github.com/AdamNiederer/base100) |  | base💯 - Encode your data into emoji |
| [smuggler](https://github.com/defparam/smuggler) |  | Smuggler - An HTTP Request Smuggling / Desync testing tool wri<br>tten in Python 3 |
| [security-research<br>-pocs](https://github.com/google/security-research-pocs) |  | Proof-of-concept codes created as part of security research do<br>ne by Google Security Team. |
| [kalitools](https://github.com/Jack-Liang/kalitools) |  | Kali Linux工具清单 |
| [instantbox](https://github.com/instantbox/instantbox) |  | 📦 Get a clean, ready-to-go Linux box in seconds. |
| [CVE-2021-21972](https://github.com/NS-Sp4ce/CVE-2021-21972) |  | CVE-2021-21972 Exploit |
| [SIET](https://github.com/frostbits-security/SIET) |  | Smart Install Exploitation Tool |
| [PoCs](https://github.com/ImageTragick/PoCs) |  | Proof of Concepts for CVE-2016–3714 |
| [jasypt-spring-boo<br>t](https://github.com/ulisesbocchio/jasypt-spring-boot) | jasypt-<br>spring-b<br>oot-pare<br>nt-3.0.5 | Jasypt integration for Spring boot |
| [lynis](https://github.com/CISOfy/lynis) | 3.0.9 | Lynis - Security auditing tool for Linux, macOS, and UNIX-base<br>d systems. Assists with compliance testing (HIPAA/ISO27001/PCI <br>DSS) and system hardening. Agentless, and installation optional<br>. |
| [gjson](https://github.com/tidwall/gjson) |  | Get JSON values quickly - JSON parser for Go |
| [static-analysis](https://github.com/analysis-tools-dev/static-analysis) |  | ⚙️ A curated list of static analysis (SAST) tools and linter<br>s for all programming languages, config files, build tools, and<br> more. The focus is on tools which improve code quality. |
| [CVE-2020-2551](https://github.com/Y4er/CVE-2020-2551) |  | Weblogic IIOP CVE-2020-2551 |
| [hsd-cipher-sm](https://github.com/gotoworld/hsd-cipher-sm) |  | 国产密码算法SM2，SM3，SM4 |
| [SharpToolsAggress<br>or](https://github.com/uknowsec/SharpToolsAggressor) |  | 内网渗透中常用的c#程序整合成cs脚本，直接内存加载。持续更新~ |
| [exploits](https://github.com/cfreal/exploits) |  | Some of my exploits. |
| [awvs-decode](https://github.com/gatlindada/awvs-decode) |  |  |
| [community](https://github.com/volatilityfoundation/community) |  | Volatility plugins developed and maintained by the community  |
| [toppwdhash](https://github.com/moyuwa/toppwdhash) |  | 常见密码哈希离线查询工具 , 包含算法类型'md5', 'md5x2', 'md5x3'<br>,'sha1', 'ntlm', 'mysql', 'mysql5','md5_sha1', 'sha1_sha1', 'sh<br>a1_md5', 'md5_base64','md5_middle','base64_md5', 'md5_sha256', <br>'sha256','sm3' |
| [CVEs](https://github.com/sT0wn-nl/CVEs) |  | The following is a list of my collected CVE's |
| [CTFCrackTools](https://github.com/Acmesec/CTFCrackTools) |  |  |
| [RW_Password](https://github.com/r35tart/RW_Password) |  | 此项目用来提取收集以往泄露的密码中符合条件的强弱密码 |
| [bkcrack](https://github.com/kimci86/bkcrack) | v1.5.0 | Crack legacy zip encryption with Biham and Kocher's known plai<br>ntext attack. |
| [CVE-2015-7547](https://github.com/fjserna/CVE-2015-7547) |  | Proof of concept for CVE-2015-7547 |
| [checkO365](https://github.com/vysecurity/checkO365) |  | checkO365 is a tool to check if a target domain is using O365 |
| [Veil](https://github.com/Veil-Framework/Veil) | 3.1.14 | Veil 3.1.X (Check version info in Veil at runtime) |
| [Nmap_Bypass_IDS](https://github.com/al0ne/Nmap_Bypass_IDS) |  | Nmap&Zmap特征识别，绕过IDS探测 |
| [S2-045](https://github.com/iBearcat/S2-045) |  |  |
| [CVE-2020-17518](https://github.com/QmF0c3UK/CVE-2020-17518) |  |  |
| [DotNetToJScript](https://github.com/tyranid/DotNetToJScript) | v1.0.4 | A tool to create a JScript file which loads a .NET v2 assembly<br> from memory. |
| [CVE-2020-11651](https://github.com/0xc0d/CVE-2020-11651) |  | CVE-2020-11651: Proof of Concept |
| [Pentest101](https://github.com/ffffffff0x/Pentest101) |  | 一些关于渗透测试的Tips |
| [sttr](https://github.com/abhimanyu003/sttr) | v0.2.18 | cross-platform, cli app to perform various operations on strin<br>g |
| [oss-browser](https://github.com/aliyun/oss-browser) | v1.17.0 | OSS Browser 提供类似windows资源管理器功能。用户可以很方便的浏<br>览文件，上传下载文件，支持断点续传等。 |
| [Thanos](https://github.com/hotvulcan/Thanos) |  |  |
| [Reptile](https://github.com/f0rb1dd3n/Reptile) | 2.0 | LKM Linux rootkit |
| [wifi_keylogger](https://github.com/spacehuhn/wifi_keylogger) |  | DIY Arduino Wi-Fi Keylogger (Proof of Concept) |
| [S3Scanner](https://github.com/sa7mon/S3Scanner) | v3.0.4 | Scan for misconfigured S3 buckets across S3-compatible APIs! |
| [Socks5](https://github.com/wyx176/Socks5) |  | Socks5代理服务器搭建脚本/Socks5 shortcut creation script |
| [WOTD](https://github.com/jaredestroud/WOTD) |  |  |
| [CVE-2017-11882](https://github.com/Ridter/CVE-2017-11882) |  | CVE-2017-11882 from https://github.com/embedi/CVE-2017-11882 |
| [BB-Tips](https://github.com/bilbomal/BB-Tips) |  | Collection of Bug Bounty Tips  |
| [CVE-2019-19781](https://github.com/jas502n/CVE-2019-19781) |  | Citrix ADC Remote Code Execution |
| [gotestwaf](https://github.com/wallarm/gotestwaf) |  | An open-source project in Golang to asess different API Securi<br>ty tools and WAF for detection logic and bypasses |
| [GmSSL](https://github.com/guanzhi/GmSSL) | v3.1.1-<br>pr1 | 支持国密SM2/SM3/SM4/SM9/SSL的密码工具箱 |
| [PTP-RAT](https://github.com/pentestpartners/PTP-RAT) |  | Exfiltrate data over screen interfaces |
| [hetty](https://github.com/dstotijn/hetty) | v0.7.0 | An HTTP toolkit for security research. |
| [javascript-malwar<br>e-collection](https://github.com/HynekPetrak/javascript-malware-collection) |  | Collection of almost 40.000 javascript malware samples |
| [blind-ssrf-chains](https://github.com/assetnote/blind-ssrf-chains) |  | An exhaustive list of all the possible ways you can chain your<br> Blind SSRF vulnerability |
| [cve-2020-0688](https://github.com/random-robbie/cve-2020-0688) |  | cve-2020-0688 |
| [LoggerPlusPlus](https://github.com/nccgroup/LoggerPlusPlus) | v3.20.0 | Advanced Burp Suite Logging Extension |
| [snort-rules](https://github.com/codecat007/snort-rules) |  |  |
| [hackbar2](https://github.com/HCTYMFF/hackbar2) |  |  |
| [SAP-Pentest](https://github.com/lazaars/SAP-Pentest) |  |  |
| [gmssl](https://github.com/duanhongyi/gmssl) | v3.2.2 | a python crypto for sm2/sm3/sm4 |
| [Nessus_Map](https://github.com/Ebryx/Nessus_Map) |  | Parse .nessus file(s) and shows output in interactive UI |
| [lime](https://github.com/504ensicslabs/lime) | v1.9.1 | LiME (formerly DMD) is a Loadable Kernel Module (LKM), which a<br>llows the acquisition of volatile memory from Linux and Linux-b<br>ased devices, such as those powered by Android. The tool suppor<br>ts acquiring memory either to the file system of the device or <br>over the network. LiME is unique in that it is the first tool t<br>hat allows full memory captures from Android devices. It also m<br>inimizes its interaction between user and kernel space processe<br>s during acquisition, which allows it to produce memory capture<br>s that are more forensically sound than those of other tools de<br>signed for Linux memory acquisition. |
| [Windows-AD-enviro<br>nment-related](https://github.com/incredibleindishell/Windows-AD-environment-related) |  | This Repository contains the stuff related to windows Active d<br>irectory environment exploitation |
| [Spring4Shell-POC](https://github.com/reznok/Spring4Shell-POC) |  | Dockerized Spring4Shell (CVE-2022-22965) PoC application and e<br>xploit |
| [CollaboratorPlusP<br>lus](https://github.com/nccgroup/CollaboratorPlusPlus) | v1.0.2 |  |
| [Bug-Report](https://github.com/Taiwan-Tech-WebSec/Bug-Report) |  |  |
| [DongTai](https://github.com/HXSecurity/DongTai) | v1.16.0 | Dongtai IAST is an open-source Interactive Application Securit<br>y Testing (IAST) tool that enables real-time detection of commo<br>n vulnerabilities in Java applications and third-party componen<br>ts through passive instrumentation. It is particularly suitable<br> for use in the testing phase of the development pipeline. |
| [SigFlip](https://github.com/med0x2e/SigFlip) |  | SigFlip is a tool for patching authenticode signed PE files (e<br>xe, dll, sys ..etc) without invalidating or breaking the existi<br>ng signature. |
| [pacu](https://github.com/RhinoSecurityLabs/pacu) | v1.4.2 | The AWS exploitation framework, designed for testing the secur<br>ity of Amazon Web Services environments. |
| [suricata-rules](https://github.com/al0ne/suricata-rules) |  | Suricata IDS rules 用来检测红队渗透/恶意行为等，支持检测Cobalt<br>Strike/MSF/Empire/DNS隧道/Weevely/菜刀/冰蝎/挖矿/反弹shell/ICMP<br>隧道等 |
| [secscan-authcheck](https://github.com/ztosec/secscan-authcheck) | v0.1 | 越权检测工具 |
| [CVE-2019-0232](https://github.com/pyn3rd/CVE-2019-0232) |  | Apache Tomcat Remote Code Execution on Windows |
| [APIKit](https://github.com/API-Security/APIKit) | v1.5.1 | APIKit：Discovery, Scan and Audit APIs Toolkit All In One. |
| [CVE-2021-1675](https://github.com/cube0x0/CVE-2021-1675) |  | C# and Impacket implementation of PrintNightmare CVE-2021-1675<br>/CVE-2021-34527 |
| [theZoo](https://github.com/ytisf/theZoo) | v0.60 | A repository of LIVE malwares for your own joy and pleasure. t<br>heZoo is a project created to make the possibility of malware a<br>nalysis open and available to the public. |
| [CVE-2017-10271](https://github.com/1337g/CVE-2017-10271) |  | CVE-2017-10271 WEBLOGIC RCE  (TESTED) |
| [Red-Baron](https://github.com/Coalfire-Research/Red-Baron) |  | Automate creating resilient, disposable, secure and agile infr<br>astructure for Red Teams. |
| [inSp3ctor](https://github.com/brianwarehime/inSp3ctor) |  | AWS S3 Bucket/Object Finder |
| [EventLogMaster](https://github.com/QAX-A-Team/EventLogMaster) |  | Cobalt Strike插件 - RDP日志取证&清除 |
| [scanning](https://github.com/GossiTheDog/scanning) |  |  |
| [bottleneckOsmosis](https://github.com/7dog7/bottleneckOsmosis) |  | 瓶颈渗透,web渗透,red红队,fuzz param,注释,js字典,ctf |
| [fail2ban](https://github.com/fail2ban/fail2ban) | 1.0.2 | Daemon to ban hosts that cause multiple authentication errors |
| [Rogue-MySql-Serve<br>r](https://github.com/Gifts/Rogue-MySql-Server) |  | Rogue MySql Server |
| [CVE-2017-12615](https://github.com/iBearcat/CVE-2017-12615) |  |  |
| [PPLGuard](https://github.com/elastic/PPLGuard) |  |  |
| [shiro_rce](https://github.com/wyzxxz/shiro_rce) |  |  |
| [Go-For-OSCP](https://github.com/pythonmaster41/Go-For-OSCP) |  |  |
| [VPS-web-hacking-t<br>ools](https://github.com/supr4s/VPS-web-hacking-tools) |  |  |
| [pypykatz](https://github.com/skelsec/pypykatz) | 0.6.9 | Mimikatz implementation in pure Python |
| [CrossC2](https://github.com/gloxec/CrossC2) | v3.2 | generate CobaltStrike's cross-platform payload |
| [proxyshell_payloa<br>d](https://github.com/Ridter/proxyshell_payload) |  | proxyshell payload generate |
| [snmp_fuzzer](https://github.com/dark-lbp/snmp_fuzzer) |  | snmp_fuzzer |
| [CVE-2022-0185](https://github.com/chenaotian/CVE-2022-0185) |  | CVE-2022-0185 POC and Docker and Analysis write up |
| [impacket](https://github.com/CoreSecurity/impacket) |  |  |
| [siphon](https://github.com/liamg/siphon) | v0.0.2 | :alembic: Intercept stdin/stdout/stderr for any process |
| [geacon](https://github.com/TheKingOfDuck/geacon) |  | 修改自geacon的多功能linux运维管理工具 |
| [EBurst](https://github.com/grayddq/EBurst) |  | 这个脚本主要提供对Exchange邮件服务器的账户爆破功能，集成了现有<br>主流接口的爆破方式。 |
| [wafw00f](https://github.com/EnableSecurity/wafw00f) | v2.2.0 | WAFW00F allows one to identify and fingerprint Web Application<br> Firewall (WAF) products protecting a website. |
| [me_cleaner](https://github.com/corna/me_cleaner) | v1.2 | Tool for partial deblobbing of Intel ME/TXE firmware images |
| [SCADAPASS](https://github.com/scadastrangelove/SCADAPASS) | 1.2 | SCADA StrangeLove Default/Hardcoded Passwords List |
| [SharpProxyLogon](https://github.com/Flangvik/SharpProxyLogon) |  | C# POC for CVE-2021-26855 aka ProxyLogon, supports the classic<br>ally semi-interactive web shell as well as shellcode injection  |
| [go-pinyin](https://github.com/mozillazg/go-pinyin) | v0.20.0 | 汉字转拼音 |
| [password_brute_di<br>ctionary](https://github.com/huyuanzhi2/password_brute_dictionary) |  |  |
| [LuWu](https://github.com/QAX-A-Team/LuWu) |  | 红队基础设施自动化部署工具 |
| [garble](https://github.com/burrowers/garble) | v0.10.1 | Obfuscate Go builds |
| [ListRDPConnection<br>s](https://github.com/Heart-Sky/ListRDPConnections) | 0.0.3 | C# 读取本机对外RDP连接记录和其他主机对该主机的连接记录，从而在<br>内网渗透中获取更多可通内网网段信息以及定位运维管理人员主机 |
| [aem-hacker](https://github.com/0ang3el/aem-hacker) |  |  |
| [InstallerFileTake<br>Over](https://github.com/klinix5/InstallerFileTakeOver) |  |  |
| [phpvuln](https://github.com/ecriminal/phpvuln) |  |  |
| [emp3r0r](https://github.com/jm33-m0/emp3r0r) | v1.32.2 | Linux/Windows post-exploitation framework made by linux user |
| [tongda-exp](https://github.com/kitezzzGrim/tongda-exp) | 1.0.1 | python编写的多个通达常见漏洞exp |
| [aws_public_ips](https://github.com/arkadiyt/aws_public_ips) | 1.0.7 | Fetch all public IP addresses tied to your AWS account. Works <br>with IPv4/IPv6, Classic/VPC networking, and across all AWS serv<br>ices |
| [PortBrute](https://github.com/awake1t/PortBrute) |  | 一款跨平台小巧的端口爆破工具，支持爆破FTP/SSH/SMB/MSSQL/MYSQL/<br>POSTGRESQL/MONGOD / A cross-platform compact port blasting tool<br> that supports blasting FTP/SSH/SMB/MSSQL/MYSQL/POSTGRESQL/MONG<br>OD |
| [android-malware](https://github.com/ashishb/android-malware) |  | Collection of android malware samples |
| [hack_postgres](https://github.com/T3st0r-Git/hack_postgres) |  | 便捷地使用PostgreSQL自定义函数来执行系统命令，适用于数据库管理<br>员知道postgres密码却不知道ssh或RDP密码的时候在服务器执行系统命令<br>。 |
| [CVE-2022-34918](https://github.com/veritas501/CVE-2022-34918) |  | CVE-2022-34918 netfilter nf_tables 本地提权 POC |
| [winlog](https://github.com/i11us0ry/winlog) |  | 一款基于go的windows信息收集工具，主要收集目标机器rdp端口、msts<br>c远程连接记录、mstsc密码和安全事件中4624、4625登录事件记录 |
| [photon](https://github.com/vmware/photon) | 5.0-GA | Minimal Linux container host |
| [CVE-2020-2551](https://github.com/jas502n/CVE-2020-2551) |  | Weblogic RCE with IIOP |
| [BountyHunterInChi<br>na](https://github.com/J0o1ey/BountyHunterInChina) |  | 重生之我是赏金猎人系列，分享自己和团队在SRC、项目实战漏洞测试<br>过程中的有趣案例 |
| [CVE-2021-4034](https://github.com/berdav/CVE-2021-4034) |  | CVE-2021-4034 1day |
| [Cisco-UCM-SQLi-sc<br>ripts](https://github.com/FSecureLABS/Cisco-UCM-SQLi-scripts) |  | Scripts that can be used to exploit CVE-2019-15972 which was a<br>n Authenticated SQLi issue in Cisco Unified Call Manager (UCM). |
| [sslscan](https://github.com/rbsec/sslscan) | 2.1.1 | sslscan tests SSL/TLS enabled services to discover supported c<br>ipher suites |
| [BaoTa](https://github.com/aaPanel/BaoTa) |  | 宝塔Linux面板 - 简单好用的服务器运维面板 |
| [BeaconEye](https://github.com/CCob/BeaconEye) |  | Hunts out CobaltStrike beacons and logs operator command outpu<br>t |
| [icmptunnel](https://github.com/DhavalKapil/icmptunnel) | v1.0.0 | Transparently tunnel your IP traffic through ICMP echo and rep<br>ly packets. |
| [OSCE-Exploit-Deve<br>lopment](https://github.com/areyou1or0/OSCE-Exploit-Development) |  |  |
| [mapcidr](https://github.com/projectdiscovery/mapcidr) | v1.1.15 | Utility program to perform multiple operations for a given sub<br>net/CIDR ranges. |
| [J2EEScan](https://github.com/ilmila/J2EEScan) | v2.0.0 | J2EEScan is a plugin for Burp Suite Proxy. The goal of this pl<br>ugin is to improve the test coverage during web application pen<br>etration tests on J2EE applications. |
| [CVE-2021-41653](https://github.com/ohnonoyesyes/CVE-2021-41653) |  |  |
| [BurpBounty](https://github.com/wagiro/BurpBounty) | BurpBou<br>nty_v4.0 | Burp Bounty (Scan Check Builder in BApp Store) is a extension <br>of Burp Suite that allows you, in a quick and simple way, to im<br>prove the active and passive scanner by means of personalized r<br>ules through a very intuitive graphical interface. |
| [big_screen](https://github.com/TurboWay/big_screen) |  | 数据大屏可视化 |
| [sast-scan](https://github.com/ShiftLeftSecurity/sast-scan) | v2.1.1 | Scan is a free & Open Source DevSecOps tool for performing sta<br>tic analysis based security testing of your applications and it<br>s dependencies. CI and Git friendly. |
| [CACTUSTORCH](https://github.com/mdsecactivebreach/CACTUSTORCH) |  | CACTUSTORCH: Payload Generation for Adversary Simulations |
| [aquatone](https://github.com/michenriksen/aquatone) | v1.7.0 | A Tool for Domain Flyovers |
| [yara](https://github.com/VirusTotal/yara) | v4.3.2 | The pattern matching swiss knife |
| [experiments](https://github.com/commial/experiments) |  | Expriments |
| [Mythic](https://github.com/its-a-feature/Mythic) | v3.1.0 | A collaborative, multi-platform, red teaming framework |
| [struts-pwn_CVE-20<br>18-11776](https://github.com/mazen160/struts-pwn_CVE-2018-11776) |  |  An exploit for Apache Struts CVE-2018-11776 |
| [CVE-2021-1675_RDL<br>_LPE](https://github.com/mstxq17/CVE-2021-1675_RDL_LPE) |  | PrintNightMare LPE提权漏洞的CS 反射加载插件。开箱即用、通过内<br>存加载、混淆加载的驱动名称来ByPass Defender/EDR。 |
| [CVE-2019-12384](https://github.com/jas502n/CVE-2019-12384) |  | Jackson Rce For CVE-2019-12384  |
| [CVE-2019-0232](https://github.com/jas502n/CVE-2019-0232) |  | Apache Tomcat Remote Code Execution on Windows - CGI-BIN |
| [wfuzz](https://github.com/xmendez/wfuzz) | v3.1.0 | Web application fuzzer |
| [fucking-algorithm](https://github.com/labuladong/fucking-algorithm) | plugin | 刷算法全靠套路，认准 labuladong 就够了！English version suppor<br>ted! Crack LeetCode, not only how, but also why.  |
| [ecapture](https://github.com/ehids/ecapture) |  |  |
| [sensinfor](https://github.com/donot-wong/sensinfor) | 1.6 | A chrome extension use to find leak file and backup file. |
| [mimipenguin](https://github.com/huntergregal/mimipenguin) | 2.0-rel<br>ease | A tool to dump the login password from the current linux user |
| [sm-crypto](https://github.com/JuneAndGreen/sm-crypto) |  | 国密算法js版 |
| [LinuxEelvation](https://github.com/Al1ex/LinuxEelvation) |  | Linux Eelvation(持续更新) |
| [CVE-2020-1938](https://github.com/0nise/CVE-2020-1938) |  |  |
| [Exchange_SSRF](https://github.com/Jumbo-WJB/Exchange_SSRF) |  | Some Attacks of Exchange SSRF ProxyLogon&ProxyShell |
| [ip2domain](https://github.com/Sma11New/ip2domain) | ip2doma<br>in_v0.2 | 批量查询ip对应域名及百度权重、备案信息；ip反查域名；ip查备案信<br>息；资产归属查询；百度权重查询 |
| [shhgit](https://github.com/eth0izzle/shhgit) |  | Ah shhgit! Find secrets in your code. Secrets detection for yo<br>ur GitHub, GitLab and Bitbucket repositories. |
| [Weblogic](https://github.com/black-mirror/Weblogic) |  | Weblogic CVE-2019-2725 CVE-2019-2729 Getshell 命令执行  |
| [armitage](https://github.com/rsmudge/armitage) |  | Automatically exported from code.google.com/p/armitage |
| [CapOS](https://github.com/lis912/CapOS) |  | 等级保护测评windows工具源码 |
| [SharpShooter](https://github.com/mdsecactivebreach/SharpShooter) |  | Payload Generation Framework |
| [jo](https://github.com/jpmens/jo) | 1.9 | JSON output from a shell |
| [c-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker) |  | JWT brute force cracker written in C |
| [wechat-export](https://github.com/sn00pyd0g3/wechat-export) |  |  |
| [zsteg](https://github.com/zed-0xff/zsteg) |  | detect stegano-hidden data in PNG & BMP |
| [fastadmin](https://github.com/karsonzhang/fastadmin) |  | 基于 ThinkPHP5 和 Bootstrap 的极速后台开发框架，一键生成 CRUD<br>，自动生成控制器、模型、视图、JS、语言包、菜单、回收站。 |
| [CVE-2022-25636-Pi<br>peVersion](https://github.com/veritas501/CVE-2022-25636-PipeVersion) |  | CVE-2022-25636 exploit rewritten with pipe primitive |
| [Spring4Shell-POC](https://github.com/lunasec-io/Spring4Shell-POC) |  | This is a dockerized application that is vulnerable to the Spr<br>ing4Shell vulnerability (CVE-2022-22965). |
| [MSSQL_SQL_BYPASS_<br>WIKI](https://github.com/aleenzz/MSSQL_SQL_BYPASS_WIKI) |  | MSSQL注入提权,bypass的一些总结 |
| [PE2HTML](https://github.com/OsandaMalith/PE2HTML) |  | Injects HTML/PHP/ASP to the PE |
| [Lsass-Shtinkering](https://github.com/deepinstinct/Lsass-Shtinkering) |  |  |
| [cs2modrewrite](https://github.com/threatexpress/cs2modrewrite) |  | Convert Cobalt Strike profiles to modrewrite scripts |
| [FirmAE](https://github.com/pr0v3rbs/FirmAE) | v1.0 | Towards Large-Scale Emulation of IoT Firmware for Dynamic Anal<br>ysis |
| [CORS_vulnerable_L<br>ab-Without_Databas<br>e](https://github.com/incredibleindishell/CORS_vulnerable_Lab-Without_Database) |  |  |
| [naive-hashcat](https://github.com/brannondorsey/naive-hashcat) |  | Crack password hashes without the fuss :cat2: |
| [showdoc](https://github.com/star7th/showdoc) | v3.2.2 | ShowDoc is a tool greatly applicable for an IT team to share d<br>ocuments online一个非常适合IT团队的在线API文档、技术文档工具 |
| [Penetration-Testi<br>ng-Tools](https://github.com/mgeeky/Penetration-Testing-Tools) |  | A collection of more than 170+ tools, scripts, cheatsheets and<br> other loots that I've developed over years for Red Teaming/Pen<br>testing/IT Security audits purposes. |
| [jsrsasign](https://github.com/kjur/jsrsasign) | 10.8.5 | The 'jsrsasign' (RSA-Sign JavaScript Library) is an opensource<br> free cryptography library supporting RSA/RSAPSS/ECDSA/DSA sign<br>ing/validation, ASN.1, PKCS#1/5/8 private/public key, X.509 cer<br>tificate, CRL, OCSP, CMS SignedData, TimeStamp, CAdES and JSON <br>Web Signature/Token in pure JavaScript. |
| [sangfor-edr-explo<br>it](https://github.com/A2gel/sangfor-edr-exploit) |  |  |
| [DirBrute](https://github.com/Xyntax/DirBrute) |  | 多线程WEB目录爆破工具 [Multi-thread WEB directory blasting too<br>l(with dics inside) ] |
| [VolUtility](https://github.com/kevthehermit/VolUtility) | v1.2 | Web App for Volatility framework |
| [wisper](https://github.com/krisleech/wisper) |  | A micro library providing Ruby objects with Publish-Subscribe <br>capabilities |
| [Xiaomi_Mi_WiFi_R3<br>G_Vulnerability_PO<br>C](https://github.com/UltramanGaia/Xiaomi_Mi_WiFi_R3G_Vulnerability_POC) |  | A login bypass(CVE-2019-18371) and a command injection vulnera<br>bility(CVE-2019-18370) in Xiaomi Router R3G up to version 2.28.<br>23. |
| [kernel-exploits](https://github.com/xairy/kernel-exploits) |  | My proof-of-concept exploits for the Linux kernel |
| [cloudscraper](https://github.com/VeNoMouS/cloudscraper) | 1.2.68 | A Python module to bypass Cloudflare's anti-bot page. |
| [top25-parameter](https://github.com/lutfumertceylan/top25-parameter) | v1.0.7 | For basic researches, top 25 vulnerability parameters that can<br> be used in automation tools or manual recon. 🛡️⚔️🧙 |
| [CVE-2020-8840](https://github.com/jas502n/CVE-2020-8840) |  |  |
| [Cloud-Pentesting](https://github.com/TROUBLE-1/Cloud-Pentesting) |  | This repository is in progress, it will keep updating as I com<br>e across to new learning materials. Feel free to contribute. |
| [SQL-Injection-Pay<br>loads](https://github.com/trietptm/SQL-Injection-Payloads) |  | SQL Injection Payloads for Burp Suite, OWASP Zed Attack Proxy,<br>... |
| [mquery](https://github.com/CERT-Polska/mquery) | v1.4.0 | YARA malware query accelerator (web frontend) |
| [Karta](https://github.com/CheckPointSW/Karta) | v2.1.0 | Karta - source code assisted fast binary matching plugin for I<br>DA |
| [rtcp](https://github.com/knownsec/rtcp) | v0.1.0 | 利用 Python 的 Socket 端口转发，用于远程维护 |
| [woodpecker-framwo<br>rk-release](https://github.com/woodpecker-framework/woodpecker-framwork-release) |  |  |
| [surferFTP](https://github.com/vp777/surferFTP) |  | SSRF to TCP Port Scanning, Banner and Private IP Disclosure by<br> abusing the FTP protocol/clients |
| [RedTeam-BCS](https://github.com/Mel0day/RedTeam-BCS) |  | BCS（北京网络安全大会）2019 红队行动会议重点内容 |
| [scan-backup-langz<br>i-](https://github.com/oscommonjs/scan-backup-langzi-) |  | 扫描备份文件和敏感信息泄漏的扫描器，速度快，器大活好 |
| [awesome-burp-exte<br>nsions](https://github.com/snoopysecurity/awesome-burp-extensions) |  | A curated list of amazingly awesome Burp Extensions |
| [poc-graphql](https://github.com/righettod/poc-graphql) | 1.0.0 | Research on GraphQL from an AppSec point of view. |
| [avList](https://github.com/gh0stkey/avList) |  | avList - 杀软进程对应杀软名称 |
| [Log4jAttackSurfac<br>e](https://github.com/YfryTchsGD/Log4jAttackSurface) |  |  |
| [ebpfkit-monitor](https://github.com/Gui774ume/ebpfkit-monitor) |  | ebpfkit-monitor is a tool that detects and protects against eB<br>PF powered rootkits |
| [textfilter](https://github.com/observerss/textfilter) |  | 敏感词过滤的几种实现+某1w词敏感词库 |
| [SpringShell](https://github.com/TheGejr/SpringShell) |  | Spring4Shell - Spring Core RCE - CVE-2022-22965 |
| [writeups](https://github.com/snowyyowl/writeups) |  |  |
| [MailSniper](https://github.com/dafthack/MailSniper) |  | MailSniper is a penetration testing tool for searching through<br> email in a Microsoft Exchange environment for specific terms (<br>passwords, insider intel, network architecture information, etc<br>.). It can be used as a non-administrative user to search their<br> own email, or by an administrator to search the mailboxes of e<br>very user in a domain. |
| [subjack](https://github.com/haccer/subjack) | 2.1 | Subdomain Takeover tool written in Go |
| [OSCE](https://github.com/dhn/OSCE) |  | Some exploits, which I’ve created during my OSCE preparation. |
| [tget](https://github.com/jeffjose/tget) |  | tget is wget for torrents |
| [SHIRO-721](https://github.com/jas502n/SHIRO-721) |  | RememberMe Padding Oracle Vulnerability RCE |
| [CVE-2020-13935](https://github.com/RedTeamPentesting/CVE-2020-13935) |  | Exploit for WebSocket Vulnerability in Apache Tomcat |
| [Firewall](https://github.com/wudimahua/Firewall) |  | 美国国家安全局NSA下属方程式黑客组织（Equation Group）被The Sha<br>dow Brokers（影子经纪人）hack出来的并免费分享的源码 |
| [fuzzdb](https://github.com/infosec-au/fuzzdb) |  | Automatically exported from code.google.com/p/fuzzdb |
| [safety](https://github.com/pyupio/safety) | 2.3.5 | Safety checks Python dependencies for known security vulnerabi<br>lities and suggests the proper remediations for vulnerabilities<br> detected. |
| [cloud-service-enu<br>m](https://github.com/NotSoSecure/cloud-service-enum) |  |  |
| [shellcode_launche<br>r](https://github.com/clinicallyinane/shellcode_launcher) |  | Shellcode launcher utility |
| [Bad-Pdf](https://github.com/deepzec/Bad-Pdf) | v1.1 | Steal Net-NTLM Hash using Bad-PDF |
| [CVE-2021-22005](https://github.com/rwincey/CVE-2021-22005) |  |  |
| [WindowsExploits](https://github.com/abatchy17/WindowsExploits) |  | Windows exploits, mostly precompiled. Not being updated. Check<br> https://github.com/SecWiki/windows-kernel-exploits instead. |
| [CTF-Mind-maps](https://github.com/M0cK1nG-b1Rd/CTF-Mind-maps) |  | 整合入门到中高级题目的思路，for new CTFers ! |
| [CVE-2020-11651-po<br>c](https://github.com/jasperla/CVE-2020-11651-poc) |  | PoC exploit of CVE-2020-11651 and CVE-2020-11652 |
| [VirusTotalC2](https://github.com/D1rkMtr/VirusTotalC2) |  |  |
| [Conveigh](https://github.com/Kevin-Robertson/Conveigh) |  | Conveigh is a Windows PowerShell LLMNR/NBNS spoofer detection <br>tool |
| [Hosts_scan](https://github.com/fofapro/Hosts_scan) |  | 这是一个用于IP和域名碰撞匹配访问的小工具，旨意用来匹配出渗透过<br>程中需要绑定hosts才能访问的弱主机或内部系统。 |
| [TPscan](https://github.com/Lucifer1993/TPscan) |  | 一键ThinkPHP漏洞检测 |
| [CVE-2022-2639-Pip<br>eVersion](https://github.com/veritas501/CVE-2022-2639-PipeVersion) |  |  |
| [color](https://github.com/gookit/color) | v1.5.4 | 🎨 Terminal color rendering library, support 8/16 colors, 256 <br>colors, RGB color rendering output, support Print/Sprintf metho<br>ds, compatible with Windows. GO CLI 控制台颜色渲染工具库，支持1<br>6色，256色，RGB色彩渲染输出，使用类似于 Print/Sprintf，兼容并支<br>持 Windows 环境的色彩渲染 |
| [onesixtyone](https://github.com/trailofbits/onesixtyone) | v0.3.4 | Fast SNMP Scanner |
| [CVE-2017-7269-Ech<br>o-PoC](https://github.com/lcatro/CVE-2017-7269-Echo-PoC) |  | CVE-2017-7269 回显PoC ,用于远程漏洞检测.. |
| [henggeFish](https://github.com/SkewwG/henggeFish) |  | 自动化批量发送钓鱼邮件（横戈安全团队出品） |
| [fastjson-blacklis<br>t](https://github.com/LeadroyaL/fastjson-blacklist) |  |  |
| [S2-053-CVE-2017-1<br>2611](https://github.com/brianwrf/S2-053-CVE-2017-12611) |  | A simple script for exploit RCE for Struts 2 S2-053(CVE-2017-1<br>2611) |
| [SharpMapExec](https://github.com/cube0x0/SharpMapExec) |  |  |
| [SpoolSample](https://github.com/leechristensen/SpoolSample) |  | PoC tool to coerce Windows hosts authenticate to other machine<br>s via the MS-RPRN RPC interface.  This is possible via other pr<br>otocols as well. |
| [crawlergo_x_XRAY](https://github.com/timwhitez/crawlergo_x_XRAY) |  | 360/0Kee-Team/crawlergo动态爬虫结合长亭XRAY扫描器的被动扫描功<br>能 |
| [jaeles](https://github.com/jaeles-project/jaeles) | beta-v0<br>.17.1 | The Swiss Army knife for automated Web Application Testing |
| [modbus-cli](https://github.com/tallakt/modbus-cli) |  | Modbus command line utility |
| [phpinfo_scanner](https://github.com/proudwind/phpinfo_scanner) |  | 一个抓取phpinfo重要信息的小工具 |
| [AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) | v0.107.<br>41 | Network-wide ads & trackers blocking DNS server |
| [dirtycow-docker-v<br>dso](https://github.com/gebl/dirtycow-docker-vdso) |  |  |
| [CVE-2020-1472](https://github.com/VoidSec/CVE-2020-1472) |  | Exploit Code for CVE-2020-1472 aka Zerologon |
| [KaTeX](https://github.com/KaTeX/KaTeX) | v0.16.9 | Fast math typesetting for the web. |
| [emergency-respons<br>e-checklist](https://github.com/theLSA/emergency-response-checklist) | 1.0 | 应急响应指南 / emergency response checklist |
| [telebot](https://github.com/tucnak/telebot) | v3.1.0 | Telebot is a Telegram bot framework in Go. |
| [CVE-2018-15473-Ex<br>ploit](https://github.com/Rhynorater/CVE-2018-15473-Exploit) |  | Exploit written in Python for CVE-2018-15473 with threading an<br>d export formats |
| [jira_scan](https://github.com/bcoles/jira_scan) | v0.0.6 | A simple remote scanner for Atlassian Jira |
| [xxl-job](https://github.com/jas502n/xxl-job) | 1.0 | xxl-job RESTful API RCE |
| [bigdata_practice](https://github.com/TurboWay/bigdata_practice) |  | 大数据分析可视化实践 |
| [struts-pwn](https://github.com/mazen160/struts-pwn) |  | An exploit for Apache Struts CVE-2017-5638 |
| [MITM-cheatsheet](https://github.com/Sab0tag3d/MITM-cheatsheet) |  |  |
| [2017-Security-ppt](https://github.com/lovesec/2017-Security-ppt) |  |  |
| [CVE-2021-3156](https://github.com/stong/CVE-2021-3156) |  | PoC for CVE-2021-3156 (sudo heap overflow) |
| [Pinyin2Hanzi](https://github.com/letiantian/Pinyin2Hanzi) |  | 拼音转汉字， 拼音输入法引擎， pin yin -> 拼音 |
| [spiderfoot](https://github.com/smicallef/spiderfoot) | v4.0 | SpiderFoot automates OSINT for threat intelligence and mapping<br> your attack surface. |
| [RoarCTF-Writeup-2<br>019](https://github.com/Carry955/RoarCTF-Writeup-2019) |  | https://github.com/berTrAM888/RoarCTF-Writeup-some-Source-Code<br>.git |
| [SensitiveWordFilt<br>er](https://github.com/bzvs1992/SensitiveWordFilter) |  | 机器学习实现敏感词过滤 |
| [OffensiveNotion](https://github.com/mttaggart/OffensiveNotion) | v1.5.0 | Notion as a platform for offensive operations |
| [CVE-2019-2725](https://github.com/lufeirider/CVE-2019-2725) |  | CVE-2019-2725 命令回显 |
| [CVE-2019-17558_So<br>lr_Vul_Tool](https://github.com/SDNDTeam/CVE-2019-17558_Solr_Vul_Tool) | 1.0 | CVE-2019-17558 Solr模板注入漏洞图形化一键检测工具。CVE-2019-17<br>558 Solr Velocity Template Vul POC Tool. |
| [NtlmRelayToEWS](https://github.com/Arno0x/NtlmRelayToEWS) |  | ntlm relay attack to Exchange Web Services |
| [CVE-2018-3245](https://github.com/pyn3rd/CVE-2018-3245) |  | CVE-2018-3245-PoC |
| [BurpCollaboratorD<br>NSTunnel](https://github.com/NetSPI/BurpCollaboratorDNSTunnel) |  | A DNS tunnel utilizing the Burp Collaborator |
| [Homework-of-Pytho<br>n](https://github.com/3gstudent/Homework-of-Python) |  | Python codes of my blog. |
| [how-does-Xmanager<br>-encrypt-password](https://github.com/HyperSine/how-does-Xmanager-encrypt-password) |  | This is a repo to tell you how Xmanager (XFtp, XShell) encrypt<br> password. Transferred from https://github.com/DoubleLabyrinth/<br>how-does-Xmanager-encrypt-password |
| [wenyan](https://github.com/wenyan-lang/wenyan) | v0.3.4 | 文言文編程語言 A programming language for the ancient Chinese. |
| [rdesktop](https://github.com/rdesktop/rdesktop) | v1.9.0 | 🚨 rdesktop is in need of a new maintainter. Please see the ho<br>me page for more details. 🚨 |
| [social-engineer-t<br>oolkit](https://github.com/trustedsec/social-engineer-toolkit) |  | The Social-Engineer Toolkit (SET) repository from TrustedSec -<br> All new versions of SET will be deployed here. |
| [Janus](https://github.com/echtdefault/Janus) |  |  |
| [java-file-ftp](https://github.com/samsbp/java-file-ftp) |  | POC for leaking java version through file and ftp protocols |
| [XAntiDebug](https://github.com/strivexjun/XAntiDebug) |  | VMProtect 3.x Anti-debug Method Improved |
| [as_bypass_php_dis<br>able_functions](https://github.com/Medicean/as_bypass_php_disable_functions) |  | antsword bypass PHP disable_functions |
| [hackingthe](https://github.com/Hacking-the-Cloud/hackingthe) |  |  |
| [CiscoSmartInstall<br>Exploit](https://github.com/ChristianPapathanasiou/CiscoSmartInstallExploit) |  |  |
| [espanso](https://github.com/espanso/espanso) | v2.1.8 | Cross-platform Text Expander written in Rust |
| [gmpy](https://github.com/aleaxit/gmpy) | gmpy2-2<br>.1.5 | General Multi-Precision arithmetic for Python 2.6+/3+ (GMP, MP<br>IR, MPFR, MPC) |
| [cve-2020-0688](https://github.com/Ridter/cve-2020-0688) |  | cve-2020-0688 |
| [oracleShell](https://github.com/jas502n/oracleShell) |  | oracle 数据库命令执行 |
| [awesome-honeypots](https://github.com/paralax/awesome-honeypots) |  | an awesome list of honeypot resources |
| [patching](https://github.com/gaasedelen/patching) | v0.1.2 | An Interactive Binary Patching Plugin for IDA Pro |
| [chainoffools](https://github.com/kudelskisecurity/chainoffools) |  | A PoC for CVE-2020-0601 |
| [awesome-pentest-n<br>ote](https://github.com/pen4uin/awesome-pentest-note) |  |  |
| [ida_python_extrac<br>tCode](https://github.com/hackflame/ida_python_extractCode) |  | ida提取特征码脚本 |
| [PeiQi-WIKI-POC](https://github.com/PeiQi0/PeiQi-WIKI-POC) |  |  |
| [smogcloud](https://github.com/BishopFox/smogcloud) |  | Find cloud assets that no one wants exposed 🔎 ☁️ |
| [CS-checklist](https://github.com/theLSA/CS-checklist) | v1.0 | PC客户端（C-S架构）渗透测试checklist / Client side(C-S) penetr<br>ation checklist |
| [ones](https://github.com/ffffffff0x/ones) | v1.0.4 | 可用于多个网络资产测绘引擎 API 的命令行查询工具 |
| [ioc](https://github.com/avast/ioc) |  | Threat Intel IoCs + bits and pieces of dark matter |
| [clash_for_windows<br>_pkg](https://github.com/Fndroid/clash_for_windows_pkg) |  |  |
| [github-search](https://github.com/gwen001/github-search) | v2.0.1 | A collection of tools to perform searches on GitHub. |
| [SCFProxy](https://github.com/shimmeris/SCFProxy) | v0.2.1 | A proxy tool based on cloud function. |
| [f8x](https://github.com/ffffffff0x/f8x) | 1.6.2 | 红/蓝队环境自动化部署工具 | Red/Blue team environment automati<br>on deployment tool |
| [AheadLib-x86-x64](https://github.com/strivexjun/AheadLib-x86-x64) | 1.2 | hijack dll Source Code Generator. support x86/x64  |
| [CVE-2019-11539](https://github.com/0xDezzy/CVE-2019-11539) |  | Exploit for the Post-Auth RCE vulnerability in Pulse Secure Co<br>nnect |
| [vlmcsd](https://github.com/Wind4/vlmcsd) | svn1113 | KMS Emulator in C (currently runs on Linux including Android, <br>FreeBSD, Solaris, Minix, Mac OS, iOS, Windows with or without C<br>ygwin) |
| [STS2G](https://github.com/x51/STS2G) |  |  |
| [kernel-exploits](https://github.com/lucyoa/kernel-exploits) |  |  |
| [Violation_Pnetest](https://github.com/EvilAnne/Violation_Pnetest) |  | 渗透红线Checklist |
| [cve-2020-1054](https://github.com/0xeb-bp/cve-2020-1054) |  | LPE for CVE-2020-1054 targeting Windows 7 x64 |
| [fingerprintx](https://github.com/praetorian-inc/fingerprintx) | v1.1.11 | Standalone utility for service discovery on open ports!  |
| [google_dork_list](https://github.com/BullsEye0/google_dork_list) |  | Google Dorks | Google helps you to find Vulnerable Websites th<br>at Indexed in Google Search Results. Here is the latest collect<br>ion of Google Dorks. A collection of 13.760 Dorks. Author: Jola<br>nda de Koff |
| [flask-session-coo<br>kie-manager](https://github.com/noraj/flask-session-cookie-manager) | v1.2.1.<br>1 | :cookie: Flask Session Cookie Decoder/Encoder |
| [dnscrypt-proxy-co<br>nfig](https://github.com/CNMan/dnscrypt-proxy-config) |  |  |
| [ICS-pcap](https://github.com/automayt/ICS-pcap) |  | A collection of ICS/SCADA PCAPs |
| [CVE-2019-15642](https://github.com/jas502n/CVE-2019-15642) |  | Webmin Remote Code Execution (authenticated)  |
| [CVE-2018-8174-msf](https://github.com/0x09AL/CVE-2018-8174-msf) |  | CVE-2018-8174 - VBScript memory corruption exploit. |
| [RDWArecon](https://github.com/p0dalirius/RDWArecon) |  |  |
| [blog-hugo](https://github.com/kylingit/blog-hugo) |  | 基于Hugo的静态博客 |
| [DVSA](https://github.com/OWASP/DVSA) |  | a Damn Vulnerable Serverless Application |
| [gendict](https://github.com/ffffffff0x/gendict) | v1.0.5 | 字典生成工具 |
| [microsoftSpider](https://github.com/tengzhangchao/microsoftSpider) |  |  |
| [noPac](https://github.com/cube0x0/noPac) |  | CVE-2021-42287/CVE-2021-42278 Scanner & Exploiter. |
| [JQShell](https://github.com/Stahlz/JQShell) |  | A weaponized version of CVE-2018-9206 |
| [spectre-meltdown-<br>checker](https://github.com/speed47/spectre-meltdown-checker) | v0.46 | Downfall, Zenbleed, ZombieLoad, RIDL, Fallout, Foreshadow, Spe<br>ctre, Meltdown vulnerability/mitigation checker for Linux & BSD |
| [shuji](https://github.com/paazmaya/shuji) |  | Reverse engineering JavaScript and CSS sources from sourcemaps |
| [CVE-2021-3156](https://github.com/worawit/CVE-2021-3156) |  | Sudo Baron Samedit Exploit |
| [CVE-2018-14729](https://github.com/FoolMitAh/CVE-2018-14729) |  |  |
| [can-utils](https://github.com/linux-can/can-utils) | v2023.0<br>3 | Linux-CAN / SocketCAN user space applications |
| [CVE-2017-0199](https://github.com/bhdresh/CVE-2017-0199) | v4.0.1 | Exploit toolkit CVE-2017-0199 - v4.0 is a handy python script <br>which provides pentesters and security researchers a quick and <br>effective way to test Microsoft Office RCE. It could generate a<br> malicious RTF/PPSX file and deliver metasploit / meterpreter /<br> other payload to victim without any complex configuration. |
| [Burp2Malleable](https://github.com/CodeXTF2/Burp2Malleable) |  | Quick python utility I wrote to turn HTTP requests from burp s<br>uite into Cobalt Strike Malleable C2 profiles |
| [Exploits](https://github.com/WindowsExploits/Exploits) |  | Windows Exploits |
| [shiroPoc](https://github.com/potats0/shiroPoc) | 0.0.05 |  |
| [CobaltStrikeDetec<br>ted](https://github.com/huoji120/CobaltStrikeDetected) |  | 40行代码检测到大部分CobaltStrike的shellcode |
| [CVE-2018-13382](https://github.com/milo2012/CVE-2018-13382) |  | CVE-2018-13382 |
| [Python-dsstore](https://github.com/gehaxelt/Python-dsstore) |  | A library for parsing .DS_Store files and extracting file name<br>s |
| [dive](https://github.com/wagoodman/dive) | v0.11.0 | A tool for exploring each layer in a docker image |
| [python-uncompyle6](https://github.com/rocky/python-uncompyle6) | 3.9.0 | A cross-version Python bytecode decompiler |
| [Cobalt_Strike_wik<br>i](https://github.com/aleenzz/Cobalt_Strike_wiki) |  | Cobalt Strike系列 |
| [write-ups-2015](https://github.com/ctfs/write-ups-2015) |  | Wiki-like CTF write-ups repository, maintained by the communit<br>y. 2015 |
| [autotimeliner](https://github.com/andreafortuna/autotimeliner) |  | Automagically extract forensic timeline from volatile memory d<br>ump |
| [git-tips](https://github.com/521xueweihan/git-tips) |  | :trollface:Git的奇技淫巧 |
| [choose](https://github.com/theryangeary/choose) | v1.3.4 | A human-friendly and fast alternative to cut and (sometimes) a<br>wk |
| [CobaltNotion](https://github.com/HuskyHacks/CobaltNotion) |  | A spin-off research project. Cobalt Strike x Notion collab 202<br>2 |
| [ctf-tools](https://github.com/zardus/ctf-tools) |  | Some setup scripts for security research tools. |
| [ExtractedDefender](https://github.com/HackingLZ/ExtractedDefender) |  |  |
| [DumpTheGit](https://github.com/Securityautomation/DumpTheGit) |  |  |
| [etl2pcapng](https://github.com/microsoft/etl2pcapng) | v1.11.0 | Utility that converts an .etl file containing a Windows networ<br>k packet capture into .pcapng format. |
| [CVE-2020-0787-EXP<br>-ALL-WINDOWS-VERSI<br>ON](https://github.com/cbwang505/CVE-2020-0787-EXP-ALL-WINDOWS-VERSION) | 1 | Support ALL Windows Version |
| [icsmaster](https://github.com/w3h/icsmaster) |  | ICS/SCADA Security Resource（整合工控安全相关资源） |
| [csprecon](https://github.com/edoardottt/csprecon) | v0.0.8 | Discover new target domains using Content Security Policy  |
| [Amass](https://github.com/OWASP/Amass) |  |  |
| [CVE-2021-21972](https://github.com/horizon3ai/CVE-2021-21972) |  | Proof of Concept Exploit for vCenter CVE-2021-21972 |
| [proxylogscan](https://github.com/dwisiswant0/proxylogscan) | v0.0.2 | A fast tool to mass scan for a vulnerability on Microsoft Exch<br>ange Server that allows an attacker bypassing the authenticatio<br>n and impersonating as the admin (CVE-2021-26855). |
| [blackboxprotobuf](https://github.com/nccgroup/blackboxprotobuf) |  | Blackbox protobuf is a Burp Suite extension for decoding and m<br>odifying arbitrary protobuf messages without the protobuf type <br>definition. |
| [clairctl](https://github.com/jgsqware/clairctl) | v1.2.8 | Tracking container vulnerabilities with Clair Control for Core<br>OS Clair |
| [ICS-Security-Tool<br>s](https://github.com/ITI/ICS-Security-Tools) |  | Tools, tips, tricks, and more for exploring ICS Security. |
| [weakfilescan](https://github.com/ring04h/weakfilescan) |  | 动态多线程敏感信息泄露检测工具 |
| [druid](https://github.com/alibaba/druid) | 1.2.20 | 阿里云计算平台DataWorks(https://help.aliyun.com/document_detai<br>l/137663.html) 团队出品，为监控而生的数据库连接池 |
| [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole) |  | get things from one computer to another, safely |
| [IIS_exploit](https://github.com/edwardz246003/IIS_exploit) |  |  |
| [exploitdb-bin-spl<br>oits](https://github.com/offensive-security/exploitdb-bin-sploits) |  | The legacy Exploit Database repository - New repo located at h<br>ttps://gitlab.com/exploit-database/exploitdb-bin-sploits |
| [Invoke-BuildAnony<br>mousSMBServer](https://github.com/3gstudent/Invoke-BuildAnonymousSMBServer) |  | Use to build an anonymous SMB file server. |
| [Vxscan](https://github.com/al0ne/Vxscan) |  | python3写的综合扫描工具，主要用来存活验证，敏感文件探测(目录扫<br>描/js泄露接口/html注释泄露)，WAF/CDN识别，端口扫描，指纹/服务识<br>别，操作系统识别，POC扫描，SQL注入，绕过CDN，查询旁站等功能，主<br>要用来甲方自测或乙方授权测试，请勿用来搞破坏。 |
| [ProxyShell](https://github.com/ktecv2000/ProxyShell) |  | ProxyShell POC Exploit : Exchange Server RCE (ACL Bypass + EoP<br> + Arbitrary File Write) |
| [anew](https://github.com/tomnomnom/anew) | v0.1.1 | A tool for adding new lines to files, skipping duplicates |
| [werkzeug](https://github.com/pallets/werkzeug) | 3.0.1 | The comprehensive WSGI web application library. |
| [Libra](https://github.com/rabbitmask/Libra) |  | Libra [ 天秤座 ] | 网站篡改、暗链、死链监测平台 |
| [danted](https://github.com/Lozy/danted) |  | Fast script for installing & configing Danted--Socks5 Proxy Se<br>rver. |
| [CVE-2018-8120](https://github.com/alpha1ab/CVE-2018-8120) |  | CVE-2018-8120 Exploit for Win2003 Win2008 WinXP Win7  |
| [FourEye](https://github.com/lengjibo/FourEye) | 1.8 | AV Evasion Tool For Red Team Ops |
| [ctf-wiki](https://github.com/ctf-wiki/ctf-wiki) |  | Come and join us, we need you! |
| [sec-interview](https://github.com/d1nfinite/sec-interview) |  | 信息安全面试题汇总 |
| [Inspur](https://github.com/NS-Sp4ce/Inspur) |  | Inspur vul repo |
| [BurpCollector](https://github.com/TEag1e/BurpCollector) |  | 通过BurpSuite来构建自己的爆破字典，可以通过字典爆破来发现隐藏<br>资产。 |
| [jarm_randomizer](https://github.com/netskopeoss/jarm_randomizer) |  | This tool was open sourced as part of JARM Randomizer: Evading<br> JARM Fingerprinting for HiTB Amsterdam 2021. |
| [harbor](https://github.com/goharbor/harbor) | v2.9.1 | An open source trusted cloud native registry project that stor<br>es, signs, and scans content. |
| [BT_Panel_Privileg<br>e_Escalation](https://github.com/Hzllaga/BT_Panel_Privilege_Escalation) |  | 宝塔面板Windows版提权方法 |
| [cve-2019-1003000-<br>jenkins-rce-poc](https://github.com/adamyordan/cve-2019-1003000-jenkins-rce-poc) |  | Jenkins RCE Proof-of-Concept: SECURITY-1266 / CVE-2019-1003000<br> (Script Security), CVE-2019-1003001 (Pipeline: Groovy), CVE-20<br>19-1003002 (Pipeline: Declarative) |
| [mscan](https://github.com/lele8/mscan) |  |  |
| [Eventlogedit-evt-<br>-General](https://github.com/3gstudent/Eventlogedit-evt--General) |  | Remove individual lines from Windows Event Viewer Log (EVT) fi<br>les |
| [DigistumpArduino](https://github.com/digistump/DigistumpArduino) | 1.6.7 | Files to add Digistump support (Digispark, Pro, DigiX) to Ardu<br>ino 1.6.X (1.6.5+) |
| [sensitive-stop-wo<br>rds](https://github.com/fwwdn/sensitive-stop-words) |  | 互联网常用敏感词、停止词词库 |
| [tomcat_nofile_web<br>shell](https://github.com/z1Ro0/tomcat_nofile_webshell) |  | Tomcat基于动态注册Filter的无文件Webshell |
| [PocCollect](https://github.com/cckuailong/PocCollect) |  | Poc Collected for study and develop |
| [base92](https://github.com/thenoviceoof/base92) |  | Implementations of base92 in various languages (C, python) |
| [x-crack](https://github.com/netxfly/x-crack) | 1.0.1 | x-crack - Weak password scanner, Support: FTP/SSH/SNMP/MSSQL/M<br>YSQL/PostGreSQL/REDIS/ElasticSearch/MONGODB |
| [nali](https://github.com/zu1k/nali) | v0.8.0 | An offline tool for querying IP geographic information and CDN<br> provider. 一个查询IP地理信息和CDN服务提供商的离线终端工具. |
| [jQuery-with-XSS](https://github.com/mahp/jQuery-with-XSS) |  | jQuery with XSS, Testing and Secure Version |
| [IoT_Sec_Tutorial](https://github.com/G4rb3n/IoT_Sec_Tutorial) |  | IoT安全教程 |
| [awesome-yara](https://github.com/InQuest/awesome-yara) |  | A curated list of awesome YARA rules, tools, and people. |
| [CVE-2020-9484](https://github.com/masahiro331/CVE-2020-9484) |  |  |
| [BurpSuiteSuite-co<br>llections](https://github.com/Mr-xn/BurpSuiteSuite-collections) |  |  |
| [hackerone-reports](https://github.com/reddelexc/hackerone-reports) |  | Top disclosed reports from HackerOne |
| [CVE-2022-0847-Dir<br>tyPipe-Exploit](https://github.com/Arinerron/CVE-2022-0847-DirtyPipe-Exploit) |  | A root exploit for CVE-2022-0847 (Dirty Pipe) |
| [UnblockNeteaseMus<br>ic](https://github.com/nondanee/UnblockNeteaseMusic) | v0.25.3 | Revive unavailable songs for Netease Cloud Music |
| [cve-2019-2618](https://github.com/jas502n/cve-2019-2618) |  | Weblogic Upload Vuln(Need  username password)-CVE-2019-2618 |
| [CotEditor](https://github.com/coteditor/CotEditor) | 4.6.5 | Lightweight Plain-Text Editor for macOS |
| [MSOLSpray](https://github.com/dafthack/MSOLSpray) |  | A password spraying tool for Microsoft Online accounts (Azure/<br>O365). The script logs if a user cred is valid, if MFA is enabl<br>ed on the account, if a tenant doesn't exist, if a user doesn't<br> exist, if the account is locked, or if the account is disabled<br>.  |
| [Jackson_RCE-CVE-2<br>019-12384](https://github.com/MagicZer0/Jackson_RCE-CVE-2019-12384) |  | CVE-2019-12384 漏洞测试环境 |
| [falco](https://github.com/falcosecurity/falco) | 0.36.2 | Cloud Native Runtime Security |
| [CS_fakesubmit](https://github.com/LiAoRJ/CS_fakesubmit) |  | 一个可以伪装上线Cobaltstrike的脚本 |
| [volatility-plugin<br>s](https://github.com/superponible/volatility-plugins) |  | Plugins I've written for Volatility |
| [Motrix](https://github.com/agalwood/Motrix) | v1.8.19 | A full-featured download manager. |
| [supervisor](https://github.com/Supervisor/supervisor) |  | Supervisor process control system for Unix (supervisord) |
| [bopscrk](https://github.com/r3nt0n/bopscrk) | v2.4.5 | Generate smart and powerful wordlists |
| [thc-ipv6](https://github.com/vanhauser-thc/thc-ipv6) | v3.8 | IPv6 attack toolkit |
| [ZhouYu](https://github.com/threedr3am/ZhouYu) |  | （周瑜）Java - SpringBoot 持久化 WebShell 学习demo（不仅仅是Sp<br>ringBoot，适合任何符合JavaEE规范的服务） |
| [F5-steganography](https://github.com/matthewgao/F5-steganography) |  | F5 steganography |
| [iconhash](https://github.com/Becivells/iconhash) | v0.4.3 | fofa shodan favicon.ico hash icon ico 计算器 |
| [MSSQL_BackDoor](https://github.com/evi1ox/MSSQL_BackDoor) |  |  |
| [rsdl](https://github.com/tismayil/rsdl) |  | Subdomain Scan With Ping Method. |
| [AntSword-Labs](https://github.com/AntSwordProject/AntSword-Labs) |  | Awesome environment for antsword tests |
| [naxsi](https://github.com/nbs-system/naxsi) | 1.3 | NAXSI is an open-source, high performance, low rules maintenan<br>ce WAF for NGINX |
| [profiles](https://github.com/volatilityfoundation/profiles) |  | Volatility profiles for Linux and Mac OS X |
| [DNSLog](https://github.com/BugScanTeam/DNSLog) |  | DNSLog 是一款监控 DNS 解析记录和 HTTP 访问记录的工具。 |
| [EventCleaner](https://github.com/QAX-A-Team/EventCleaner) |  | A tool mainly to erase specified records from Windows event lo<br>gs, with additional functionalities. |
| [exp](https://github.com/rootphantomer/exp) |  |  |
| [exploits](https://github.com/mm0r1/exploits) |  | Pwn stuff. |
| [api-firewall](https://github.com/wallarm/api-firewall) | v0.6.13 | Fast and light-weight API proxy firewall for request and respo<br>nse validation by OpenAPI specs.  |
| [tlslite-ng](https://github.com/glzjin/tlslite-ng) |  | New home of the TLS implementation in pure python |
| [Probable-Wordlist<br>s](https://github.com/berzerk0/Probable-Wordlists) | v2.0 | Version 2 is live! Wordlists sorted by probability originally <br>created for password generation and testing - make sure your pa<br>sswords aren't popular! |
| [OSCP](https://github.com/areyou1or0/OSCP) |  | OSCP  |
| [pdns](https://github.com/PowerDNS/pdns) |  | PowerDNS Authoritative, PowerDNS Recursor, dnsdist |
| [yq](https://github.com/mikefarah/yq) | v4.35.2 | yq is a portable command-line YAML, JSON, XML, CSV, TOML  and <br>properties processor |
| [Emergency](https://github.com/0x1997CN/Emergency) |  |  |
| [privilege-escalat<br>ion-awesome-script<br>s-suite](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite) |  |  |
| [cve-2019-0708](https://github.com/mekhalleh/cve-2019-0708) |  | Metasploit module for massive Denial of Service using #Bluekee<br>p vector. |
| [sensitive_words](https://github.com/qloog/sensitive_words) |  | 敏感词库整理 |
| [pingcastle](https://github.com/vletoux/pingcastle) | 3.1.0.1 | PingCastle - Get Active Directory Security at 80% in 20% of th<br>e time |
| [compose](https://github.com/docker/compose) | v2.23.0 | Define and run multi-container applications with Docker |
| [graphql-voyager](https://github.com/APIs-guru/graphql-voyager) |  |  |
| [logging-log4j2](https://github.com/apache/logging-log4j2) | rel/2.2<br>1.1 | Apache Log4j 2 is a versatile, feature-rich, efficient logging<br> API and backend for Java. |
| [wooyun-payload](https://github.com/boy-hack/wooyun-payload) | 1.0 | 从wooyun中提取的payload，以及burp插件 |
| [Responder](https://github.com/lgandx/Responder) |  | Responder is a LLMNR, NBT-NS and MDNS poisoner, with built-in <br>HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting <br>NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP au<br>thentication.  |
| [gmapsapiscanner](https://github.com/ozguralp/gmapsapiscanner) |  |  |
| [rules](https://github.com/Yara-Rules/rules) |  | Repository of yara rules |
| [fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts) |  | Web Pentesting Fuzz 字典,一个就够了。 |
| [CS_mock](https://github.com/jas502n/CS_mock) |  | 模拟cobalt strike beacon上线包. Simulation cobalt strike beaco<br>n connection packet. |
| [metarget](https://github.com/brant-ruan/metarget) |  |  |
| [gopsutil](https://github.com/shirou/gopsutil) | v3.23.1<br>0 | psutil for golang |
| [clashX](https://github.com/yichengchen/clashX) |  |  |
| [bro-pdns](https://github.com/JustinAzoff/bro-pdns) |  |  |
| [open-source-badge<br>s](https://github.com/ellerbrock/open-source-badges) |  | :octocat: Open Source & Licence Badges |
| [ShiroScan](https://github.com/sv3nbeast/ShiroScan) |  | Shiro<=1.2.4反序列化，一键检测工具 |
| [unfurl](https://github.com/tomnomnom/unfurl) | v0.4.3 | Pull out bits of URLs provided on stdin |
| [at-ps](https://github.com/specterops/at-ps) |  | Adversary Tactics - PowerShell Training |
| [31-days-of-API-Se<br>curity-Tips](https://github.com/inonshk/31-days-of-API-Security-Tips) |  | This challenge is Inon Shkedy's 31 days API Security Tips. |
| [cisco-snmp-rce](https://github.com/artkond/cisco-snmp-rce) |  | Cisco IOS SNMP RCE PoC |
| [taskcafe](https://github.com/JordanKnott/taskcafe) | 0.3.2 | An open source project management tool with Kanban boards |
| [pwndbg](https://github.com/pwndbg/pwndbg) | 2023.07<br>.17 | Exploit Development and Reverse Engineering with GDB Made Easy |
| [xvwa](https://github.com/s4n7h0/xvwa) |  | XVWA is a badly coded web application written in PHP/MySQL tha<br>t helps security enthusiasts to learn application security.   |
| [Win2016LPE](https://github.com/alpha1ab/Win2016LPE) |  | Windows10 & Windows Server 2016 LPE Exploit (use schedsvc!SchR<br>pcSetSecurity()) |
| [gin](https://github.com/gin-gonic/gin) | v1.9.1 | Gin is a HTTP web framework written in Go (Golang). It feature<br>s a Martini-like API with much better performance -- up to 40 t<br>imes faster. If you need smashing performance, get yourself som<br>e Gin. |
| [POC-T](https://github.com/Xyntax/POC-T) | 2.0.5 | 渗透测试插件化并发框架 / Open-sourced remote vulnerability PoC<br>/EXP framework |
| [CVE-2020-14882](https://github.com/jas502n/CVE-2020-14882) |  | CVE-2020–14882、CVE-2020–14883 |
| [hassh](https://github.com/salesforce/hassh) |  | HASSH is a network fingerprinting standard which can be used t<br>o identify specific Client and Server SSH implementations. The <br>fingerprints can be easily stored, searched and shared in the f<br>orm of a small MD5 fingerprint. |
| [CVE-2017-12615](https://github.com/breaktoprotect/CVE-2017-12615) |  | POC Exploit for Apache Tomcat 7.0.x CVE-2017-12615 PUT JSP vul<br>nerability. |
| [asnmap](https://github.com/projectdiscovery/asnmap) | v1.0.6 | Go CLI and Library for quickly mapping organization network ra<br>nges using ASN information. |
| [rsatool](https://github.com/ius/rsatool) |  | rsatool can be used to calculate RSA and RSA-CRT parameters |
| [web-log-parser](https://github.com/JeffXue/web-log-parser) |  | An open source analysis web log tool |
| [ddos-tools](https://github.com/licyun/ddos-tools) |  |  |
| [sas-top-10](https://github.com/puresec/sas-top-10) |  | Serverless Architectures Security Top 10 Guide |
| [CaptfEncoder](https://github.com/guyoung/CaptfEncoder) | 3.1.2 | Captfencoder is opensource a rapid cross platform network secu<br>rity tool suite, providing network security related code conver<br>sion, classical cryptography, cryptography, asymmetric encrypti<br>on, miscellaneous tools, and aggregating all kinds of online to<br>ols. |
| [pupy](https://github.com/n1nj4sec/pupy) |  | Pupy is an opensource, cross-platform (Windows, Linux, OSX, An<br>droid) C2 and post-exploitation framework written in python and<br> C |
| [XSStrike](https://github.com/s0md3v/XSStrike) | 3.1.5 | Most advanced XSS scanner. |
| [iprange](https://github.com/ffffffff0x/iprange) | v1.0.2 | 计算ip范围,支持 cidr,ip-range 格式的输入 |
| [CVE-2019-10392](https://github.com/jas502n/CVE-2019-10392) |  | CVE-2019-10392 RCE Jackson with Git Client Plugin 2.8.2 (Authe<br>nticated) |
| [corsair_scan](https://github.com/Santandersecurityresearch/corsair_scan) | v0.2.0 | Corsair_scan is a security tool to test Cross-Origin Resource <br>Sharing (CORS). |
| [SharpNetCheck](https://github.com/uknowsec/SharpNetCheck) |  |  |
| [Spray-AD](https://github.com/outflanknl/Spray-AD) |  | A Cobalt Strike tool to audit Active Directory user accounts f<br>or weak, well known or easy guessable passwords. |
| [CVE-2018-0296](https://github.com/yassineaboukir/CVE-2018-0296) |  | Script to test for Cisco ASA path traversal vulnerability (CVE<br>-2018-0296) and extract system information. |
| [pwcrack-framework](https://github.com/L-codes/pwcrack-framework) | 1.20.0 | Password Crack Framework |
| [glpi](https://github.com/glpi-project/glpi) | 10.0.10 | GLPI is a Free Asset and IT Management Software package, Data <br>center management, ITIL Service Desk, licenses tracking and sof<br>tware auditing. |
| [s3-buckets-finder](https://github.com/gwen001/s3-buckets-finder) | v1.2.0 | Find AWS S3 buckets and test their permissions. |
| [4-ZERO-3](https://github.com/Dheerajmadhukar/4-ZERO-3) |  | 403/401 Bypass Methods + Bash Automation + Your Support ;) |
| [CVE-2019-0803](https://github.com/ExpLife0011/CVE-2019-0803) |  | Win32k Elevation of Privilege Poc |
| [nmap-bootstrap-xs<br>l](https://github.com/honze-net/nmap-bootstrap-xsl) |  | A Nmap XSL implementation with Bootstrap. |
| [Administrative-di<br>visions-of-China](https://github.com/modood/Administrative-divisions-of-China) | 2.7.0 | 中华人民共和国行政区划：省级（省份）、 地级（城市）、 县级（区<br>县）、 乡级（乡镇街道）、 村级（村委会居委会） ，中国省市区镇村<br>二级三级四级五级联动地址数据。 |
| [BurpAuthzPlugin](https://github.com/wuntee/BurpAuthzPlugin) |  |  |
| [Spring-Boot-Vulne<br>rability](https://github.com/pyn3rd/Spring-Boot-Vulnerability) |  |  |
| [Adinfo](https://github.com/lzzbb/Adinfo) | v0.3 | 域信息收集工具 |
| [Exchange2domain](https://github.com/Ridter/Exchange2domain) |  | CVE-2018-8581 |
| [CVE-2021-4034](https://github.com/zhzyker/CVE-2021-4034) |  | polkit pkexec Local Privilege Vulnerability to Add custom comm<br>ands |
| [Fuzz_dic](https://github.com/SmithEcon/Fuzz_dic) |  |  |
| [Red-Team-Infrastr<br>ucture-Wiki](https://github.com/bluscreenofjeff/Red-Team-Infrastructure-Wiki) |  | Wiki to collect Red Team infrastructure hardening resources |
| [yakit](https://github.com/yaklang/yakit) | v1.2.7-<br>sp4 | Cyber Security ALL-IN-ONE Platform |
| [cobalt-arsenal](https://github.com/mgeeky/cobalt-arsenal) |  | My collection of battle-tested Aggressor Scripts for Cobalt St<br>rike 4.0+ |
| [pkcrack](https://github.com/keyunluo/pkcrack) |  | pkcrack with modern  building  tools |
| [Vulmap](https://github.com/vulmon/Vulmap) |  | Vulmap Online Local Vulnerability Scanners Project |
| [SysmonEnte](https://github.com/codewhitesec/SysmonEnte) |  |  |
| [CVE-2018-9206](https://github.com/Den1al/CVE-2018-9206) |  | A Python PoC for CVE-2018-9206 |
| [upload-scanner](https://github.com/PortSwigger/upload-scanner) |  | HTTP file upload scanner for Burp Proxy |
| [sec_tools](https://github.com/firebroo/sec_tools) |  |  |
| [SiteCopy](https://github.com/Threezh1/SiteCopy) |  | sitecopy is a tool that facilitates personal website backup an<br>d network data collection |
| [CVE-2020-15148-by<br>passes](https://github.com/Maskhe/CVE-2020-15148-bypasses) |  | 几条关于CVE-2020-15148（yii2反序列化）的绕过 |
| [factordb-python](https://github.com/ryosan-470/factordb-python) | 1.3.0 | FactorDB client library with Python |
| [Axis-1](https://github.com/KibodWapon/Axis-1) |  |  |
| [git-vuln-finder](https://github.com/cve-search/git-vuln-finder) | v1.4 | Finding potential software vulnerabilities from git commit mes<br>sages |
| [ThinkAdmin](https://github.com/zoujingli/ThinkAdmin) |  | 基于 ThinkPHP6 的极简后台管理系统，内置注解权限、异步多任务、<br>应用插件生态等，支持类 PaaS 更新公共模块和应用插件，插件可本地化<br>定制开发。 |
| [stegoVeritas](https://github.com/bannsec/stegoVeritas) |  | Yet another Stego Tool |
| [RCE-0-day-for-Gho<br>stScript-9](https://github.com/duc-nt/RCE-0-day-for-GhostScript-9) |  |  |
| [sourcemapper](https://github.com/denandz/sourcemapper) |  | Extract JavaScript source trees from Sourcemap files |
| [evilarc](https://github.com/ptoomey3/evilarc) |  | Create tar/zip archives that can exploit directory traversal v<br>ulnerabilities |
| [CVE-2019-0193](https://github.com/jas502n/CVE-2019-0193) |  | Apache Solr DataImport Handler RCE |
| [CVE-2021-26855](https://github.com/charlottelatest/CVE-2021-26855) |  |  |
| [python_sec](https://github.com/bit4woo/python_sec) |  | python安全和代码审计相关资料收集 resource collection of python<br> security and code review |
| [writeups](https://github.com/d3npa/writeups) |  | 昔書いたctfライトアップなど |
| [laravel-exploits](https://github.com/ambionics/laravel-exploits) |  | Exploit for CVE-2021-3129 |
| [notify](https://github.com/nikoksr/notify) | v0.41.0 | A dead simple Go library for sending notifications to various <br>messaging services. |
| [Apache-NiFi-Api-R<br>CE](https://github.com/imjdl/Apache-NiFi-Api-RCE) |  |  |
| [List-RDP-Connecti<br>ons-History](https://github.com/3gstudent/List-RDP-Connections-History) |  | Use powershell to list the RDP Connections History of logged-i<br>n users or all users |
| [CMS-Hunter](https://github.com/SecWiki/CMS-Hunter) |  | CMS漏洞测试用例集合 |
| [butterfly](https://github.com/paradoxxxzero/butterfly) |  | A web terminal based on websocket and tornado |
| [CVE-2019-1388](https://github.com/sv3nbeast/CVE-2019-1388) |  | guest→system（UAC手动提权） |
| [apache-](https://github.com/ianxtianxt/apache-) |  | apache权限维持后门 |
| [GetMail](https://github.com/b0bac/GetMail) |  | 利用NTLM Hash读取Exchange邮件 |
| [openrasp](https://github.com/baidu/openrasp) | v1.3.7 | 🔥Open source RASP solution |
| [scan4all](https://github.com/hktalent/scan4all) | 2.8.7 | Official repository  vuls Scan: 15000+PoCs; 23 kinds of applic<br>ation password crack; 7000+Web fingerprints; 146 protocols and <br>90000+ rules Port scanning; Fuzz, HW, awesome BugBounty( ͡° ͜ʖ <br>͡°)... |
| [ip2region](https://github.com/lionsoul2014/ip2region) |  | Ip2region (2.0 - xdb) is a offline IP address manager framewor<br>k and locator, support billions of data segments, ten microseco<br>nd searching performance. xdb engine implementation for many pr<br>ogramming languages |
| [PySQLTools](https://github.com/Ridter/PySQLTools) |  | Mssql利用工具 |
| [Shell_Script](https://github.com/xiaoyunjie/Shell_Script) | v0.1 | Linux系统的安全，通过脚本对Linux系统进行一键检测和一键加固 |
| [Nuitka](https://github.com/Nuitka/Nuitka) |  | Nuitka is a Python compiler written in Python.  It's fully com<br>patible with Python 2.6, 2.7, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.1<br>0, and 3.11. You feed it your Python app, it does a lot of clev<br>er things, and spits out an executable or extension module.  |
| [MITMf](https://github.com/byt3bl33d3r/MITMf) | v0.9.8 | Framework for Man-In-The-Middle attacks |
| [fastjson-check](https://github.com/bigsizeme/fastjson-check) | beta | fastjson 被动扫描、不出网payload生成 |
| [locust](https://github.com/locustio/locust) | 2.18.3 | Write scalable load tests in plain Python 🚗💨 |
| [wmi](https://github.com/StackExchange/wmi) | 1.1.0 | WMI for Go |
| [nanodump](https://github.com/helpsystems/nanodump) |  |  |
| [anti-AD](https://github.com/privacy-protection-tools/anti-AD) | v4.3 | 致力于成为中文区命中率最高的广告过滤列表，实现精确的广告屏蔽和<br>隐私保护。anti-AD现已支持AdGuardHome，dnsmasq， Surge，Pi-Hole，<br>smartdns等网络组件。完全兼容常见的广告过滤工具所支持的各种广告<br>过滤列表格式 |
| [iCULeak](https://github.com/llt4l/iCULeak) |  |  |
| [gmhelper](https://github.com/ZZMarquis/gmhelper) |  | 基于BC库：国密SM2/SM3/SM4算法简单封装；实现SM2 X509v3证书的签<br>发；实现SM2 pfx证书的签发 |
| [HijackLibs](https://github.com/wietze/HijackLibs) |  | Project for tracking publicly disclosed DLL Hijacking opportun<br>ities. |
| [synner](https://github.com/JuxhinDB/synner) |  | A TCP SYN flood client written in Rust, powered by libpnet |
| [interactsh](https://github.com/projectdiscovery/interactsh) | v1.1.7 | An OOB interaction gathering server and client library |
| [redis-ssrf](https://github.com/xmsec/redis-ssrf) |  | redis ssrf gopher generater & redis ssrf to rce by master-slav<br>e-sync |
| [RdpThief](https://github.com/0x09AL/RdpThief) |  | Extracting Clear Text Passwords from mstsc.exe using API Hooki<br>ng. |
| [nodejsscan](https://github.com/ajinabraham/nodejsscan) | v4.8 | nodejsscan is a static security code scanner for Node.js appli<br>cations. |
| [docker-vulnerabil<br>ity-environment](https://github.com/MyKings/docker-vulnerability-environment) |  | Use the docker to build a vulnerability environment |
| [ffmpeg-avi-m3u-xb<br>in](https://github.com/neex/ffmpeg-avi-m3u-xbin) |  |  |
| [BackdoorMan](https://github.com/cys3c/BackdoorMan) |  | BackdoorMan is a toolkit that helps you find malicious, hidden<br> and suspicious PHP scripts and shells in a chosen destination. |
| [CVE-2021-21972](https://github.com/TaroballzChen/CVE-2021-21972) |  | CVE-2021-21972 Unauthorized RCE in VMware vCenter metasploit e<br>xploit script |
| [spectre-attack](https://github.com/Eugnis/spectre-attack) |  | Example of using revealed "Spectre" exploit (CVE-2017-5753 and<br> CVE-2017-5715) |
| [fastjsonVul](https://github.com/Lonely-night/fastjsonVul) |  | fastjson 80 远程代码执行漏洞复现 |
| [jenkins-rce](https://github.com/petercunha/jenkins-rce) |  | :smiling_imp: Jenkins RCE PoC. From unauthenticated user to re<br>mote code execution, it's a hacker's dream! |
| [PPLdump](https://github.com/itm4n/PPLdump) |  | Dump the memory of a PPL with a userland exploit |
| [ssrf-king](https://github.com/ethicalhackingplayground/ssrf-king) | v1.12 | SSRF plugin for burp Automates SSRF Detection in all of the Re<br>quest |
| [AboutSecurity](https://github.com/No-Github/AboutSecurity) |  |  |
| [searx](https://github.com/asciimoo/searx) |  |  |
| [ttyd](https://github.com/tsl0922/ttyd) | 1.7.4 | Share your terminal over the web |
| [ThinkphpRCE](https://github.com/sukabuliet/ThinkphpRCE) |  | Thinkphp  rce扫描脚本，附带日志扫描 |
| [dompdf-rce](https://github.com/positive-security/dompdf-rce) |  | RCE exploit for dompdf |
| [Intensio-Obfuscat<br>or](https://github.com/Hnfull/Intensio-Obfuscator) |  | Obfuscate a python code 2.x and 3.x |
| [theHarvester](https://github.com/laramies/theHarvester) | 4.4.4 | E-mails, subdomains and names Harvester - OSINT  |
| [Chinese-Names-Cor<br>pus](https://github.com/wainshine/Chinese-Names-Corpus) | v2.2 | 中文人名语料库。人名生成器。中文姓名,姓氏,名字,称呼,日本人名,<br>翻译人名,英文人名。可用于中文分词、人名实体识别。 |
| [Diggy](https://github.com/s0md3v/Diggy) |  | Extract endpoints from apk files. |
| [RouterScan-consol<br>e](https://github.com/dilap54/RouterScan-console) |  |  |
| [Invoke-TheHash](https://github.com/Kevin-Robertson/Invoke-TheHash) |  | PowerShell Pass The Hash Utils |
| [30min_guides](https://github.com/qinjx/30min_guides) |  | 覃健祥的学习笔记，各种几十分钟入门的文档 |
| [MYSQL_SQL_BYPASS_<br>WIKI](https://github.com/aleenzz/MYSQL_SQL_BYPASS_WIKI) |  | mysql注入,bypass的一些心得 |
| [CVE-2022-2588](https://github.com/Markakd/CVE-2022-2588) |  | exploit for CVE-2022-2588 |
| [sec-dog](https://github.com/madneal/sec-dog) | v1.0.4 |  |
| [fapro](https://github.com/fofapro/fapro) | v0.65 | Fake Protocol Server |
| [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) | 2023.08 | PyInstaller Extractor |
| [focalboard](https://github.com/mattermost/focalboard) | v7.11.3 | Focalboard is an open source, self-hosted alternative to Trell<br>o, Notion, and Asana. |
| [apollo](https://github.com/apolloconfig/apollo) | v2.1.0 | Apollo is a reliable configuration management system suitable <br>for microservice configuration management scenarios. |
| [web-cve-tests](https://github.com/foospidy/web-cve-tests) |  | A simple framework for sending test payloads for known web CVE<br>s. |
| [linux-exploit-sug<br>gester](https://github.com/mzet-/linux-exploit-suggester) |  |  |
| [WerTrigger](https://github.com/sailay1996/WerTrigger) |  | Weaponizing for privileged file writes bugs with windows probl<br>em reporting |
| [yujianrdpcrack](https://github.com/foryujian/yujianrdpcrack) |  | 御剑RDP爆破工具 |
| [powerline-shell](https://github.com/b-ryan/powerline-shell) |  | A beautiful and useful prompt for your shell |
| [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) | v3.0.0 | PowerSploit - A PowerShell Post-Exploitation Framework |
| [wabt](https://github.com/WebAssembly/wabt) | 1.0.34 | The WebAssembly Binary Toolkit |
| [CVE-2022-39197-pa<br>tch](https://github.com/burpheart/CVE-2022-39197-patch) | patch-0<br>.2 | CVE-2022-39197 漏洞补丁. CVE-2022-39197 Vulnerability Patch.  |
| [ILSpy](https://github.com/icsharpcode/ILSpy) | v8.2 | .NET Decompiler with support for PDB generation, ReadyToRun, M<br>etadata (&more) - cross-platform! |
| [CVE-2018-3191](https://github.com/voidfyoo/CVE-2018-3191) |  |  |
| [bat](https://github.com/sharkdp/bat) | v0.24.0 | A cat(1) clone with wings. |
| [vlany](https://github.com/mempodippy/vlany) |  | Linux LD_PRELOAD rootkit (x86 and x86_64 architectures) |
| [spring-boot-start<br>er-swagger](https://github.com/SpringForAll/spring-boot-starter-swagger) | 2.0.2.R<br>ELEASE | 自制spring boot starter for swagger 2.x，来试试吧，很好用哦~ |
| [awesome-vehicle-s<br>ecurity](https://github.com/jaredthecoder/awesome-vehicle-security) |  | 🚗  A curated list of resources for learning about vehicle sec<br>urity and car hacking. |
| [CVE-2022-39197](https://github.com/its-arun/CVE-2022-39197) |  | CobaltStrike <= 4.7.1 RCE |
| [Middleware-Vulner<br>ability-detection](https://github.com/mai-lang-chai/Middleware-Vulnerability-detection) |  |  |
| [2022-HW-POC](https://github.com/sobinge/2022-HW-POC) |  |  |
| [pulumi](https://github.com/pulumi/pulumi) | v3.93.0 | Pulumi - Infrastructure as Code in any programming language. B<br>uild infrastructure intuitively on any cloud using familiar lan<br>guages 🚀 |
| [singularity](https://github.com/nccgroup/singularity) |  | A DNS rebinding attack framework. |
| [UsnJrnl2Csv](https://github.com/jschicht/UsnJrnl2Csv) | v1.0.0.<br>24 | Parser for $UsnJrnl on NTFS |
| [Kayak](https://github.com/dschanoeh/Kayak) | untagge<br>d-359703<br>9ad20ce9<br>798a99 | Kayak is a CAN bus analysis tool based on SocketCAN |
| [ripple20-poc](https://github.com/jiansiting/ripple20-poc) |  | Treck Network Stack Discovery Tool by JSOF |
| [spring-cloud-netf<br>lix-hystrix-dashbo<br>ard-cve-2021-22053](https://github.com/SecCoder-Security-Lab/spring-cloud-netflix-hystrix-dashboard-cve-2021-22053) |  | Spring Cloud Netflix Hystrix Dashboard template resolution vul<br>nerability CVE-2021-22053 |
| [SQLInjectionWiki](https://github.com/ning1022/SQLInjectionWiki) |  | 一个专注于聚合和记录各种SQL注入方法的wiki |
| [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) |  |  |
| [EgGateWayGetShell<br>_py](https://github.com/yumusb/EgGateWayGetShell_py) |  | EgGateWayGetShell py脚本 |
| [Log4j2-CVE-2021-4<br>4228](https://github.com/jas502n/Log4j2-CVE-2021-44228) |  | Remote Code Injection In Log4j |
| [UPnP-Pentest-Tool<br>kit](https://github.com/nccgroup/UPnP-Pentest-Toolkit) |  | UPnP Pentest Toolkit for Windows |
| [CVE-2019-1040-dcp<br>wn](https://github.com/Ridter/CVE-2019-1040-dcpwn) |  | CVE-2019-1040 with Kerberos delegation |
| [Threat-Intelligen<br>ce-Analyst](https://github.com/pandazheng/Threat-Intelligence-Analyst) |  | 威胁情报，恶意样本分析，开源Malware代码收集 |
| [VolDiff](https://github.com/aim4r/VolDiff) |  |  |
| [vulnerability-lis<br>t](https://github.com/1120362990/vulnerability-list) |  | 在渗透测试中快速检测常见中间件、组件的高危漏洞。 |
| [DahuaConsole](https://github.com/mcw0/DahuaConsole) |  | Dahua Console, access internal debug console and/or other rese<br>arched functions in Dahua devices. Feel free to contribute in t<br>his project. |
| [PowerShell-AD-Rec<br>on](https://github.com/PyroTek3/PowerShell-AD-Recon) |  | PowerShell Scripts I find useful |
| [ACLight](https://github.com/cyberark/ACLight) |  | A script for advanced discovery of Privileged Accounts - inclu<br>des Shadow Admins |
| [libesedb](https://github.com/libyal/libesedb) |  | Library and tools to access the Extensible Storage Engine (ESE<br>) Database File (EDB) format. |
| [pdfparser](https://github.com/smalot/pdfparser) | v2.7.0 | PdfParser, a standalone PHP library, provides various tools to<br> extract data from a PDF file. |
| [findomain](https://github.com/Edu4rdSHL/findomain) |  |  |
| [CVE-2021-24086](https://github.com/0vercl0k/CVE-2021-24086) |  | Proof of concept for CVE-2021-24086, a NULL dereference in tcp<br>ip.sys triggered remotely. |
| [IOCs-IDPS](https://github.com/SpiderLabs/IOCs-IDPS) |  | This repository will hold PCAP IOC data related with known mal<br>ware samples (owner: Bryant Smith) |
| [CVE-2018-2380](https://github.com/erpscanteam/CVE-2018-2380) |  | PoC of Remote Command Execution via Log injection on SAP NetWe<br>aver AS JAVA CRM |
| [base58](https://github.com/keis/base58) |  | Base58 and Base58Check implementation compatible with what is <br>used by the bitcoin network. |
| [go-shodan](https://github.com/ns3777k/go-shodan) | v2.0.4 | Shodan API client |
| [upx](https://github.com/upx/upx) | v4.2.1 | UPX - the Ultimate Packer for eXecutables |
| [CVE-2018-8420](https://github.com/Lz1y/CVE-2018-8420) |  | 原PoC甚至符号都打错了！太不走心了！ |
| [SuperMem](https://github.com/CrowdStrike/SuperMem) |  | A python script developed to process Windows memory images bas<br>ed on triage type. |
| [Fastjson-Scanner](https://github.com/p1g3/Fastjson-Scanner) |  | a burp extension to find where use fastjson |
| [Zoinks](https://github.com/trustedsec/Zoinks) |  | Manage Engine Decrypter |
| [wordpress-dos-poc](https://github.com/roddux/wordpress-dos-poc) |  | WordPress <= 5.3.? DoS |
| [HikariCP](https://github.com/brettwooldridge/HikariCP) |  | 光 HikariCP・A solid, high-performance, JDBC connection pool a<br>t last. |
| [nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) | v9.6.9 | Community curated list of templates for the nuclei engine to f<br>ind security vulnerabilities. |
| [as_scanwebshell](https://github.com/virink/as_scanwebshell) |  | An AntSword's plugin to scan webshell |
| [CVE-2019-7238](https://github.com/jas502n/CVE-2019-7238) |  | Nexus Repository Manager 3 Remote Code Execution without authe<br>ntication < 3.15.0 |
| [SimpleShellcodeIn<br>jector](https://github.com/DimopoulosElias/SimpleShellcodeInjector) |  | SimpleShellcodeInjector receives as an argument a shellcode in<br> hex and executes it.  It DOES NOT inject the shellcode in a th<br>ird party application. |
| [cve-2017-7269-too<br>l](https://github.com/zcgonvh/cve-2017-7269-tool) |  | CVE-2017-7269 to webshell or shellcode loader |
| [PowerDNS-Admin](https://github.com/ngoduykhanh/PowerDNS-Admin) |  |  |
| [Eventlogedit-evtx<br>--Evolution](https://github.com/3gstudent/Eventlogedit-evtx--Evolution) | v1.1.0 | Remove individual lines from Windows XML Event Log (EVTX) file<br>s |
| [CVE-2020-9547](https://github.com/fairyming/CVE-2020-9547) |  | CVE-2020-9547：FasterXML/jackson-databind 远程代码执行漏洞 |
| [CVE-2020-2555](https://github.com/Y4er/CVE-2020-2555) |  | Weblogic com.tangosol.util.extractor.ReflectionExtractor RCE |
| [PostgresApp](https://github.com/PostgresApp/PostgresApp) | v2.6.8 | The easiest way to get started with PostgreSQL on the Mac |
| [Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) |  | Information Protection & OSINT resources | 一个关于数字隐私搜<br>集、保护、清理集一体的方案,外加开源信息收集(OSINT)对抗 |
| [CaA](https://github.com/gh0stkey/CaA) | 0.5 | CaA - BurpSuite Collector and Analyzer |
| [WebAliveScan](https://github.com/broken5/WebAliveScan) |  | 对目标域名进行快速的存活扫描、简单的指纹识别、目录扫描 |
| [DS_Store_crawler_<br>parser](https://github.com/anantshri/DS_Store_crawler_parser) |  | a parser + crawler for .DS_Store files exposed publically |
| [docker-remote-api<br>-exp](https://github.com/netxfly/docker-remote-api-exp) |  | docker remote api未授权访问的利用代码 |
| [idea-project-fish<br>-exploit](https://github.com/CC11001100/idea-project-fish-exploit) |  |  |
| [CVE-2019-9810](https://github.com/0vercl0k/CVE-2019-9810) | 1 | Exploit for CVE-2019-9810 Firefox on Windows 64-bit. |
| [docker_mirror](https://github.com/silenceshell/docker_mirror) | v1.0 | 查找最快的docker镜像 |
| [ProxyLogon](https://github.com/hausec/ProxyLogon) |  |  |
| [PatchAMSI](https://github.com/D1rkMtr/PatchAMSI) |  |  |
| [sharry](https://github.com/eikek/sharry) | v1.12.1 | Sharry is a self-hosted file sharing web application. |
| [browser-dumpwd](https://github.com/wekillpeople/browser-dumpwd) |  | Dump browser passwords(chrome, firefox) with sqlite3 lib.  |
| [curl-impersonate](https://github.com/lwthiker/curl-impersonate) | v0.6.0-<br>alpha.1 | curl-impersonate: A special build of curl that can impersonate<br> Chrome & Firefox |
| [CVE-2019-11580](https://github.com/jas502n/CVE-2019-11580) |  | CVE-2019-11580 Atlassian Crowd and Crowd Data Center RCE |
| [masnmapscan-V1](https://github.com/hellogoldsnakeman/masnmapscan-V1) |  |  |
| [weevely3](https://github.com/epinna/weevely3) | v4.0.1 | Weaponized web shell |
| [CC-attack](https://github.com/Leeon123/CC-attack) | v3.7.1 | Using Socks4/5 or http proxies to make a multithreading Http-f<br>lood/Https-flood (cc) attack. |
| [pdf-export](https://github.com/HaberHe/pdf-export) |  |  |
| [rce-over-spark](https://github.com/aRe00t/rce-over-spark) |  | Remote Command Execution Over Spark |
| [outguess](https://github.com/resurrecting-open-source-projects/outguess) | 0.4 | Universal steganographic tool |
| [CVE-2019-0708](https://github.com/zerosum0x0/CVE-2019-0708) |  |  |
| [impacket-ghostpot<br>ato](https://github.com/Lz1y/impacket-ghostpotato) |  | impacket-ghostpotato Fork from https://shenaniganslabs.io/2019<br>/11/12/Ghost-Potato.html |
| [dontgo403](https://github.com/devploit/dontgo403) | 0.9.4 | Tool to bypass 40X response codes. |
| [volatility](https://github.com/volatilityfoundation/volatility) |  | An advanced memory forensics framework |
| [genpAss](https://github.com/RicterZ/genpAss) |  |  |
| [bash-insulter](https://github.com/No-Github/bash-insulter) |  | Insults the user when typing wrong command |
| [node-red](https://github.com/node-red/node-red) | 3.1.0 | Low-code programming for event-driven applications |
| [AggressorScript-C<br>reateCloneHiddenAc<br>count](https://github.com/Ch1ngg/AggressorScript-CreateCloneHiddenAccount) |  | 创建一个克隆隐藏的管理员账号/Create a Clone Hidden Administrat<br>or Account |
| [ActuatorExploit](https://github.com/LFYSec/ActuatorExploit) |  | SpringBoot Actuator未授权自动化利用，支持信息泄漏/RCE |
| [exploit-CVE-2017-<br>7494](https://github.com/opsxcq/exploit-CVE-2017-7494) |  | SambaCry exploit and vulnerable container (CVE-2017-7494) |
| [CVE-2021-27850_PO<br>C](https://github.com/kahla-sec/CVE-2021-27850_POC) |  | A Proof of concept for CVE-2021-27850 affecting Apache Tapestr<br>y and leading to unauthencticated remote code execution. |
| [NGLite](https://github.com/Maka8ka/NGLite) | V1.0.01 | A major platform RAT Tool based by Blockchain/P2P.Now support <br>Windows/Linux/MacOS |
| [how-does-MobaXter<br>m-encrypt-password](https://github.com/HyperSine/how-does-MobaXterm-encrypt-password) |  | This repo offers a tool to reveal password encrypted by MobaXt<br>erm. |
| [BurpSuite-Asset_D<br>iscover](https://github.com/redhuntlabs/BurpSuite-Asset_Discover) |  | Burp Suite extension to discover assets from HTTP response. |
| [al-khaser](https://github.com/LordNoteworthy/al-khaser) |  | Public malware techniques used in the wild: Virtual Machine, E<br>mulation, Debuggers, Sandbox detection.  |
| [AhMyth-Android-RA<br>T](https://github.com/AhMyth/AhMyth-Android-RAT) |  | Android Remote Administration Tool |
| [Luyten](https://github.com/deathmarine/Luyten) | v0.5.4_<br>Rebuilt_<br>with_Lat<br>est_depe<br>nencies | An Open Source Java Decompiler Gui for Procyon |
| [TextMining](https://github.com/lining0806/TextMining) |  | Python文本挖掘系统 Research of Text Mining System |
| [cuc-ns](https://github.com/c4pr1c3/cuc-ns) |  | 网络安全课本 |
| [jadx](https://github.com/skylot/jadx) | v1.4.7 | Dex to Java decompiler |
| [ssti-payload](https://github.com/VikasVarshney/ssti-payload) |  | SSTI Payload Generator |
| [shc](https://github.com/neurobin/shc) | 4.0.3 | Shell script compiler |
| [prowler](https://github.com/toniblyx/prowler) |  |  |
| [crowbar](https://github.com/galkan/crowbar) | v4.2 | Crowbar is brute forcing tool that can be used during penetrat<br>ion tests. It is developed to support protocols that are not cu<br>rrently supported by thc-hydra and other popular brute forcing <br>tools.  |
| [CVE-2022-40684](https://github.com/horizon3ai/CVE-2022-40684) |  | A proof of concept exploit for CVE-2022-40684 affecting Fortin<br>et FortiOS, FortiProxy, and FortiSwitchManager |
| [csrf-poc-generato<br>r](https://github.com/merttasci/csrf-poc-generator) |  | this html file creates a csrf poc form to any http request. |
| [NetUser](https://github.com/lengjibo/NetUser) | 2.0 | 使用windows api添加用户，可用于net无法使用时.分为nim版，c++版<br>本，RDI版，BOF版。 |
| [common-regex](https://github.com/cdoco/common-regex) |  | :jack_o_lantern: 常用正则表达式 - 收集一些在平时项目开发中经常<br>用到的正则表达式。 |
| [java-deserializat<br>ion-exploits](https://github.com/Coalfire-Research/java-deserialization-exploits) |  | A collection of curated Java Deserialization Exploits |
| [Extracted_WD_VDM](https://github.com/crisprss/Extracted_WD_VDM) |  | Windows Defender VDM lua collections |
| [swagger2markup](https://github.com/Swagger2Markup/swagger2markup) | v1.3.4 | A Swagger to AsciiDoc or Markdown converter to simplify the ge<br>neration of an up-to-date RESTful API documentation by combinin<br>g documentation that’s been hand-written with auto-generated A<br>PI documentation. |
| [CVE-2018-3252](https://github.com/pyn3rd/CVE-2018-3252) |  | CVE-2018-3252-PoC |
| [Registry-Recon](https://github.com/optiv/Registry-Recon) |  | Cobalt Strike Aggressor Script that Performs System/AV/EDR Rec<br>on |
| [monomorph](https://github.com/DavidBuchanan314/monomorph) | v1.0 | MD5-Monomorphic Shellcode Packer - all payloads have the same <br>MD5 hash |
| [SpoolerScanner](https://github.com/vletoux/SpoolerScanner) |  | Check if MS-RPRN is remotely available with powershell/c# |
| [nacos](https://github.com/alibaba/nacos) | 2.2.3 | an easy-to-use dynamic service discovery, configuration and se<br>rvice management platform for building cloud native application<br>s. |
| [filebrowser](https://github.com/filebrowser/filebrowser) | v2.26.0 | 📂 Web File Browser |
| [wait-for](https://github.com/eficode/wait-for) | v2.2.4 | ./wait-for is a script to wait for another service to become a<br>vailable. |
| [webmin_cve-2019-1<br>2840_poc](https://github.com/KrE80r/webmin_cve-2019-12840_poc) |  | A standalone POC for CVE-2019-12840 |
| [yougar0](https://github.com/yougar0/yougar0) |  |  |
| [ReflectiveDLLInje<br>ction](https://github.com/stephenfewer/ReflectiveDLLInjection) |  | Reflective DLL injection is a library injection technique in w<br>hich the concept of reflective programming is employed to perfo<br>rm the loading of a library from memory into a host process. |
| [turbo-intruder](https://github.com/portswigger/turbo-intruder) | 1.0.19 | Turbo Intruder is a Burp Suite extension for sending large num<br>bers of HTTP requests and analyzing the results. |
| [Spring-Cloud-Gate<br>way-CVE-2022-22947](https://github.com/lucksec/Spring-Cloud-Gateway-CVE-2022-22947) |  | CVE-2022-22947 |
| [CTF-RSA-tool](https://github.com/3summer/CTF-RSA-tool) |  |  |
| [REALITY_SMASHER](https://github.com/rabidwh0re/REALITY_SMASHER) |  | vRealize RCE + Privesc (CVE-2021-21975, CVE-2021-21983, CVE-0D<br>AY-?????) |
| [wekan](https://github.com/wekan/wekan) | v7.18 | The Open Source kanban (built with Meteor). Keep variable/tabl<br>e/field names camelCase. For translations, only add Pull Reques<br>t changes to wekan/i18n/en.i18n.json , other translations are d<br>one at https://app.transifex.com/wekan/ only. |
| [KPTI-PoC-Collecti<br>on](https://github.com/turbo/KPTI-PoC-Collection) |  | Meltdown/Spectre PoC src collection. |
| [cve-2019-1040-sca<br>nner](https://github.com/fox-it/cve-2019-1040-scanner) |  |  |
| [DVWA](https://github.com/ethicalhack3r/DVWA) |  |  |
| [gmsm](https://github.com/tjfoc/gmsm) | v1.4.1 | GM SM2/3/4 library based on Golang (基于Go语言的国密SM2/SM3/SM<br>4算法库) |
| [vcenter_saml_logi<br>n](https://github.com/horizon3ai/vcenter_saml_login) |  | A tool to extract the IdP cert from vCenter backups and log in<br> as Administrator |
| [CVE-2020-0796](https://github.com/danigargu/CVE-2020-0796) | v1.0 | CVE-2020-0796 - Windows SMBv3 LPE exploit #SMBGhost |
| [thc-pptp-bruter](https://github.com/BlackArch/thc-pptp-bruter) |  | [Mirror] thc.org uses a CA that is not trusted on a base Arch <br>system so we are mirroring some source here. |
| [HiveNightmare](https://github.com/GossiTheDog/HiveNightmare) | 0.6 | Exploit allowing you to read registry hives as non-admin on Wi<br>ndows 10 and 11 |
| [dnsx](https://github.com/projectdiscovery/dnsx) | v1.1.6 | dnsx is a fast and multi-purpose DNS toolkit allow to run mult<br>iple DNS queries of your choice with a list of user-supplied re<br>solvers. |
| [checkburp](https://github.com/TomAPU/checkburp) |  | Detect burp |
| [aSiagaming](https://github.com/vngkv123/aSiagaming) |  | My Chrome and Safari exploit code + write-up repo |
| [RDODecrypt](https://github.com/Hzllaga/RDODecrypt) |  | Remote Desktop Organizer 密码破解 |
| [aliyun-cli](https://github.com/aliyun/aliyun-cli) | v3.0.18<br>6 | Alibaba Cloud CLI |
| [RSA-ATTACK](https://github.com/findneo/RSA-ATTACK) |  | RSA加密应用常见缺陷的原理与实践 |
| [jmet](https://github.com/matthiaskaiser/jmet) | 0.1.0 | Java Message Exploitation Tool |
| [tomcat-cluster-se<br>ssion-sync-exp](https://github.com/threedr3am/tomcat-cluster-session-sync-exp) |  | tomcat使用了自带session同步功能时，不安全的配置（没有使用Encry<br>ptInterceptor）导致存在的反序列化漏洞，通过精心构造的数据包， <br>可以对使用了tomcat自带session同步功能的服务器进行攻击。PS:这个不<br>是CVE-2020-9484，9484是session持久化的洞，这个是session集群同步<br>的洞！ |
| [byp4xx](https://github.com/lobuhi/byp4xx) |  | 40X/HTTP bypasser in Go. Features: Verb tampering, headers, #b<br>ugbountytips, User-Agents, extensions, default credentials... |
| [CobaltSpam](https://github.com/hariomenkel/CobaltSpam) |  |  |
| [PasswordDic](https://github.com/k8gege/PasswordDic) |  | 2011-2019年Top100弱口令密码字典 Top1000密码字典 服务器SSH/VPS<br>密码字典 后台管理密码字典 数据库密码字典  子域名字典 |
| [inql](https://github.com/doyensec/inql) | v5.0.2 | InQL is a robust, open-source Burp Suite extension for advance<br>d GraphQL testing, offering intuitive vulnerability detection, <br>customizable scans, and seamless Burp integration. |
| [Subdomain-Takeove<br>r](https://github.com/Echocipher/Subdomain-Takeover) |  | 一个子域名接管检测工具 |
| [lsassy](https://github.com/Hackndo/lsassy) | v3.1.9 | Extract credentials from lsass remotely |
| [CVE-2017-3506](https://github.com/ianxtianxt/CVE-2017-3506) |  | CVE-2017-3506 |
| [memshell](https://github.com/ydnzol/memshell) | mxd_reb<br>ehinder_<br>v3_0_5 | Tomcat 冰蝎内存马。 |
| [csp_security_mist<br>akes](https://github.com/SummitRoute/csp_security_mistakes) |  | This repo has been replaced by https://www.cloudvulndb.org |
| [CVE-2019-5736-PoC](https://github.com/Frichetten/CVE-2019-5736-PoC) |  | PoC for CVE-2019-5736 |
| [bettercap](https://github.com/bettercap/bettercap) | v2.32.0 | The Swiss Army knife for 802.11, BLE, IPv4 and IPv6 networks r<br>econnaissance and MITM attacks. |
| [CVE-2021-42321](https://github.com/DarkSprings/CVE-2021-42321) |  | Microsoft Exchange Server Poc |
| [Vulnerability-goa<br>pp](https://github.com/Hardw01f/Vulnerability-goapp) |  | Web application build Golang with Vulnerability |
| [ini](https://github.com/go-ini/ini) | v1.67.0 | Package ini provides INI file read and write functionality in <br>Go |
| [BlueCommand](https://github.com/leeberg/BlueCommand) |  | Dashboarding and Tooling front-end for PowerShell Empire using<br> PowerShell Universal Dashboard |
| [jobber](https://github.com/dshearer/jobber) | v1.4.4 | An alternative to cron, with sophisticated status-reporting an<br>d error-handling |
| [ICSim](https://github.com/zombieCraig/ICSim) |  | Instrument Cluster Simulator |
| [APT_CyberCriminal<br>_Campagin_Collecti<br>ons](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections) |  | APT & CyberCriminal Campaign Collection |
| [CVE-2020-2883](https://github.com/Y4er/CVE-2020-2883) |  | Weblogic coherence.jar RCE |
| [exploits](https://github.com/r4j0x00/exploits) |  |  |
| [redis-rogue-serve<br>r](https://github.com/LoRexxar/redis-rogue-server) |  | Redis 4.x & 5.x RCE |
| [imcat](https://github.com/stolk/imcat) |  | Show any image in a terminal window. |
| [DLLSpy](https://github.com/cyberark/DLLSpy) | V1 | DLL Hijacking Detection Tool |
| [CVE-2021-4034](https://github.com/arthepsy/CVE-2021-4034) |  | PoC for PwnKit: Local Privilege Escalation Vulnerability in po<br>lkit’s pkexec (CVE-2021-4034) |
| [Git_Extract](https://github.com/gakki429/Git_Extract) |  | 提取远程 git 泄露或本地 git 的工具 |
| [CVE-2021-21985](https://github.com/r0ckysec/CVE-2021-21985) |  |  |
| [CVE-2019-1132](https://github.com/Vlad-tri/CVE-2019-1132) |  | EoP POC for CVE-2019-1132 |
| [Windows11_Hardeni<br>ng](https://github.com/beerisgood/Windows11_Hardening) |  | a collection about Windows 11 |
| [S2-055](https://github.com/iBearcat/S2-055) |  |  |
| [ispy](https://github.com/Cyb0r9/ispy) |  | ispy V1.0 - Eternalblue(ms17-010)/Bluekeep(CVE-2019-0708) Scan<br>ner and exploit ( Metasploit automation ) |
| [dwarf2json](https://github.com/volatilityfoundation/dwarf2json) |  | convert ELF/DWARF symbol and type information into vol3's inte<br>rmediate JSON |
| [pafish](https://github.com/a0rtega/pafish) | v0.6 | Pafish is a testing tool that uses different techniques to det<br>ect virtual machines and malware analysis environments in the s<br>ame way that malware families do |
| [WeblogicScan](https://github.com/dr0op/WeblogicScan) |  | 增强版WeblogicScan、检测结果更精确、插件化、添加CVE-2019-2618<br>，CVE-2019-2729检测，Python3支持 |
| [rdpwrap](https://github.com/stascorp/rdpwrap) | v1.6.2 | RDP Wrapper Library |
| [CTF_web](https://github.com/wonderkun/CTF_web) |  | a  project aim to collect CTF web practices . |
| [tomorrow-theme](https://github.com/chriskempson/tomorrow-theme) |  | Tomorrow Theme |
| [CVE-2020-0668](https://github.com/RedCursorSecurityConsulting/CVE-2020-0668) |  | Use CVE-2020-0668 to perform an arbitrary privileged file move<br> operation. |
| [msdt-follina](https://github.com/JohnHammond/msdt-follina) |  | Codebase to generate an msdt-follina payload |
| [Auto_proxy](https://github.com/Mustard404/Auto_proxy) |  | 利用IP地址池进行自动切换Http代理，防止IP封禁。 |
| [CVE-2018-8120](https://github.com/unamer/CVE-2018-8120) |  |  |
| [CVE-2017-7494](https://github.com/joxeankoret/CVE-2017-7494) |  | Remote root exploit for the SAMBA CVE-2017-7494 vulnerability |
| [emby_ssrf](https://github.com/btnz-k/emby_ssrf) |  |  |
| [Redpoint](https://github.com/digitalbond/Redpoint) |  | Digital Bond's ICS Enumeration Tools |
| [js-md5](https://github.com/emn178/js-md5) |  | A simple MD5 hash function for JavaScript supports UTF-8 encod<br>ing. |
| [Dictionary-Of-Pen<br>testing](https://github.com/insightglacier/Dictionary-Of-Pentesting) |  | Dictionary collection project such as Pentesing, Fuzzing, Brut<br>eforce and BugBounty. 渗透测试、SRC漏洞挖掘、爆破、Fuzzing等字<br>典收集项目。 |
| [wappalyzer](https://github.com/wappalyzer/wappalyzer) |  |  |
| [HealthChecker](https://github.com/dpaulson45/HealthChecker) |  |  |
| [RedisModules-Exec<br>uteCommand](https://github.com/n0b0dyCN/RedisModules-ExecuteCommand) |  | Tools, utilities and scripts to help you write redis modules! |
| [msbuild-inline-ta<br>sk](https://github.com/3gstudent/msbuild-inline-task) |  |  |
| [pcap_dnsproxy](https://github.com/chengr28/pcap_dnsproxy) |  |  |
| [croc](https://github.com/schollz/croc) | v9.6.6 | Easily and securely send things from one computer to another :<br>crocodile: :package: |
| [marshalsec](https://github.com/mbechler/marshalsec) |  |  |
| [hashcrack](https://github.com/nccgroup/hashcrack) |  | Guesses hash types, picks some sensible dictionaries and rules<br> for hashcat |
| [tsh](https://github.com/orangetw/tsh) |  | Tiny SHell is an open-source UNIX backdoor. |
| [CVE-2018-2893](https://github.com/pyn3rd/CVE-2018-2893) |  | CVE-2018-2893-PoC |
| [SMTP-NC](https://github.com/Rvn0xsy/SMTP-NC) | v0.1.1 | SMTP Netcat , test SMTP protocol |
| [Cipher_Encryption<br>_Type_Identificati<br>on](https://github.com/Snowming04/Cipher_Encryption_Type_Identification) |  | 对密文的加密类型进行判断的命令行工具。 |
| [knm](https://github.com/FzWjScJ/knm) |  | 鼠标键盘流量包取证 |
| [-Baseline-check](https://github.com/tangjie1/-Baseline-check) |  | windows和linux基线检查，配套自动化检查脚本。纯手打。 |
| [SharpDump](https://github.com/GhostPack/SharpDump) |  | SharpDump is a C# port of PowerSploit's Out-Minidump.ps1 funct<br>ionality. |
| [Struts2-048](https://github.com/dragoneeg/Struts2-048) |  | CVE-2017-9791 |
| [VMware_vCenter](https://github.com/l0ggg/VMware_vCenter) |  | VMware vCenter 7.0.2.00100 unauth Arbitrary File Read + SSRF +<br> Reflected XSS |
| [CVE-2018-7600](https://github.com/pimps/CVE-2018-7600) |  | Exploit for Drupal 7 <= 7.57 CVE-2018-7600 |
| [WDExtract](https://github.com/hfiref0x/WDExtract) |  | Extract Windows Defender database from vdm files and unpack it |
| [MassBleed](https://github.com/1N3/MassBleed) |  | MassBleed SSL Vulnerability Scanner |
| [usql](https://github.com/xo/usql) | v0.15.2 | Universal command-line interface for SQL databases |
| [AntSword-Loader](https://github.com/AntSwordProject/AntSword-Loader) | 4.0.3 | AntSword 加载器 |
| [spring-boot-actua<br>tor-h2-rce](https://github.com/spaceraccoon/spring-boot-actuator-h2-rce) |  | Sample Spring Boot App Demonstrating RCE via Exposed env Actua<br>tor and H2 Database |
| [Nessus_to_report](https://github.com/Bypass007/Nessus_to_report) |  | Nessus中文报告自动化脚本 |
| [PixelJihad](https://github.com/oakes/PixelJihad) |  | A JavaScript steganography tool |
| [DarkNet_ChineseTr<br>ading](https://github.com/s045pd/DarkNet_ChineseTrading) |  | 🚇暗网中文网监控爬虫(DEEPMIX) |
| [sandcastle](https://github.com/0xSearches/sandcastle) |  | 🏰 A Python script for AWS S3 bucket enumeration. |
| [CVE-2017-8759](https://github.com/Lz1y/CVE-2017-8759) |  | CVE-2017-8759 |
| [loginlog_windows](https://github.com/uknowsec/loginlog_windows) |  | 读取登录过本机的登录失败或登录成功的所有计算机信息，在内网渗透<br>中快速定位运维管理人员。  |
| [Cas_Exploit](https://github.com/nice0e3/Cas_Exploit) |  |  |
| [Struts2_045-Poc](https://github.com/tengzhangchao/Struts2_045-Poc) |  |  |
| [2020-Interview-ex<br>perience](https://github.com/Kit4y/2020-Interview-experience) |  |  |
| [PwnKit](https://github.com/ly4k/PwnKit) |  | Self-contained exploit for CVE-2021-4034 - Pkexec Local Privil<br>ege Escalation |
| [pics](https://github.com/corkami/pics) |  | File formats explanations, logos redrawing... |
| [CVE-2018-20250](https://github.com/WyAtu/CVE-2018-20250) |  | exp for https://research.checkpoint.com/extracting-code-execut<br>ion-from-winrar |
| [Thanks-Mirror](https://github.com/eryajf/Thanks-Mirror) |  | 整理记录各个包管理器，系统镜像，以及常用软件的好用镜像，Thanks<br> Mirror。     走过路过，如觉不错，麻烦点个赞👆🌟 |
| [aliyun-oss-python<br>-sdk](https://github.com/aliyun/aliyun-oss-python-sdk) | 2.18.3 | Aliyun OSS SDK for Python |
| [SqlKnife_0x727](https://github.com/0x727/SqlKnife_0x727) | 1.2 | 适合在命令行中使用的轻巧的SQL Server数据库安全检测工具 |
| [pspy](https://github.com/DominicBreuker/pspy) | v1.2.1 | Monitor linux processes without root permissions |
| [PetitPotam](https://github.com/topotam/PetitPotam) |  | PoC tool to coerce Windows hosts to authenticate to other mach<br>ines via MS-EFSRPC EfsRpcOpenFileRaw or other functions. |
| [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) | v5.4.0 | A swiss army knife for pentesting networks |
| [ncDecode](https://github.com/jas502n/ncDecode) |  |  |
| [rekall](https://github.com/google/rekall) | v1.7.1 | Rekall Memory Forensic Framework |
| [Xray_and_crwlergo<br>_in_server](https://github.com/ox01024/Xray_and_crwlergo_in_server) |  | 雇一位免费的360工程师和一位长亭工程师为你挖洞，还有听话的serve<br>r酱给你汇报 |
| [code-server](https://github.com/coder/code-server) | v4.18.0 | VS Code in the browser |
| [chineseocr_lite](https://github.com/ouyanghuiyu/chineseocr_lite) |  |  |
| [phpmyadmin](https://github.com/phpmyadmin/phpmyadmin) | RELEASE<br>_5_2_1 | A web interface for MySQL and MariaDB |
| [cve-2018-1002105](https://github.com/gravitational/cve-2018-1002105) |  | Test utility for cve-2018-1002105 |
| [awesome-adb](https://github.com/mzlogin/awesome-adb) |  | ADB Usage Complete / ADB 用法大全 |
| [PrintNightmare](https://github.com/outflanknl/PrintNightmare) |  |  |
| [winscppasswd](https://github.com/anoopengineer/winscppasswd) | 1.0 | WinSCP Password Extractor/Decrypter/Revealer written in go lan<br>guage |
| [log4jscanner](https://github.com/google/log4jscanner) | v0.5.0 | A log4j vulnerability filesystem scanner and Go package for an<br>alyzing JAR files. |
| [Kali-TX](https://github.com/M507/Kali-TX) |  | Customized Kali Linux - Ansible playbook |
| [webuploader](https://github.com/fex-team/webuploader) | 0.1.5 | It's a new file uploader solution!  |
| [Brida](https://github.com/federicodotta/Brida) | v0.6pre | The new bridge between Burp Suite and Frida! |
| [AttackDetection](https://github.com/ptresearch/AttackDetection) |  | Attack Detection |
| [cronsun](https://github.com/shunfei/cronsun) | v0.3.5 | A Distributed, Fault-Tolerant Cron-Style Job System. |
| [btrace](https://github.com/btraceio/btrace) | v2.2.4 | BTrace - a safe, dynamic tracing tool for the Java platform |
| [ja3box](https://github.com/Macr0phag3/ja3box) |  | extract ja3(s) when sniffing or from a pcap. |
| [CVE-2019-1215](https://github.com/bluefrostsecurity/CVE-2019-1215) |  |  |
| [burp-bounty](https://github.com/Sy3Omda/burp-bounty) |  | Burp Bounty profiles |
| [pentest-wiki](https://github.com/nixawk/pentest-wiki) |  | PENTEST-WIKI is a free online security knowledge library for p<br>entesters / researchers. If you have a good idea, please share <br>it with others. |
| [ProcessInjection](https://github.com/sud01oo/ProcessInjection) |  | Some ways to inject a DLL into a alive process |
| [CVE-2022-21882](https://github.com/KaLendsi/CVE-2022-21882) |  | win32k LPE  |
| [Archive2](https://github.com/No-Github/Archive2) | 1.3.4 |  |
| [Tencent_Yun_tools](https://github.com/freeFV/Tencent_Yun_tools) |  |  |
| [cs-ssl-gen](https://github.com/rmikehodges/cs-ssl-gen) |  |  |
| [sasquatch](https://github.com/devttys0/sasquatch) |  |  |
| [2021hvv_vul](https://github.com/YinWC/2021hvv_vul) |  | 2021hvv漏洞汇总 |
| [gitls](https://github.com/hahwul/gitls) | v1.0.4 | 🖇 Enumerate git repository URL from list of URL / User / Org.<br> Friendly to pipeline |
| [ssh-auditor](https://github.com/ncsa/ssh-auditor) | v0.18 | The best way to scan for weak ssh passwords on your network |
| [luaforwindows](https://github.com/rjpcomputing/luaforwindows) | v5.1.5-<br>52 | Lua for Windows is a 'batteries included environment' for the <br>Lua scripting language on Windows. NOTICE: Looking for maintain<br>er. |
| [zscan](https://github.com/zyylhn/zscan) | v2.0.1 | Zscan a scan blasting tool set |
| [sec-chart](https://github.com/SecWiki/sec-chart) |  | 安全思维导图集合 |
| [fzf](https://github.com/junegunn/fzf) | 0.44.0 | :cherry_blossom: A command-line fuzzy finder |
| [iscsicpl_bypassUA<br>C](https://github.com/zha0gongz1/iscsicpl_bypassUAC) | v1.0 | UAC bypass for x64 Windows 7 - 11（无弹窗版） |
| [bugcrowd-levelup-<br>subdomain-enumerat<br>ion](https://github.com/appsecco/bugcrowd-levelup-subdomain-enumeration) |  | This repository contains all the material from the talk "Esote<br>ric sub-domain enumeration techniques" given at Bugcrowd LevelU<br>p 2017 virtual conference |
| [CVE-2022-0778](https://github.com/drago-96/CVE-2022-0778) |  | Proof of concept for CVE-2022-0778, which triggers an infinite<br> loop in parsing X.509 certificates due to a bug in BN_mod_sqrt |
| [Security-PPT](https://github.com/FeeiCN/Security-PPT) |  | Security-related Slide Presentation & Security Research Report<br>（大安全各领域各公司各会议分享的PPT以及各类安全研究报告） |
| [duf](https://github.com/muesli/duf) | v0.8.1 | Disk Usage/Free Utility - a better 'df' alternative |
| [taborator](https://github.com/hackvertor/taborator) |  | A Burp extension to show the Collaborator client in a tab |
| [WaterDragon](https://github.com/sh3d0ww01f/WaterDragon) |  | WaterDragon:用GithubAction实现代理功能。红队,cve,代理池,隐匿,<br>攻防,对抗，hackone,src,proxy,CVE-2020,CVE-2021,CVE-2022 |
| [Sentinel](https://github.com/alibaba/Sentinel) | 1.8.6 | A powerful flow control component enabling reliability, resili<br>ence and monitoring for microservices. (面向云原生微服务的高可<br>用流控防护组件) |
| [CMS-Exploit-Frame<br>work](https://github.com/Q2h1Cg/CMS-Exploit-Framework) |  | CMS Exploit Framework |
| [SSRF_Vulnerable_L<br>ab](https://github.com/incredibleindishell/SSRF_Vulnerable_Lab) |  | This Lab contain the sample codes which are vulnerable to Serv<br>er-Side Request Forgery attack |
| [merlin](https://github.com/MythicAgents/merlin) |  | Cross-platform post-exploitation HTTP Command & Control agent <br>written in golang |
| [rdpscan](https://github.com/robertdavidgraham/rdpscan) |  | A quick scanner for the CVE-2019-0708 "BlueKeep" vulnerability<br>. |
| [fastjson_rce_tool](https://github.com/wyzxxz/fastjson_rce_tool) |  |  |
| [OddProxyDemo](https://github.com/CHYbeta/OddProxyDemo) |  |  |
| [CNVD-C-2019-48814](https://github.com/jas502n/CNVD-C-2019-48814) |  | WebLogic wls9-async反序列化远程命令执行漏洞 |
| [name-fuzz](https://github.com/ffffffff0x/name-fuzz) |  | 针对目标已知信息的字典生成工具 |
| [HexRaysCodeXplore<br>r](https://github.com/REhints/HexRaysCodeXplorer) | 2.1 | Hex-Rays Decompiler plugin for better code navigation |
| [dnscrypt-proxy](https://github.com/jedisct1/dnscrypt-proxy) |  |  |
| [commix](https://github.com/commixproject/commix) | v3.8 | Automated All-in-One OS Command Injection Exploitation Tool. |
| [WebLogicPasswordD<br>ecryptorUi](https://github.com/Ch1ngg/WebLogicPasswordDecryptorUi) | v2.0 | 解密weblogic AES或DES加密方法 |
| [dnsFookup](https://github.com/makuga01/dnsFookup) |  | DNS rebinding toolkit |
| [cub3](https://github.com/mempodippy/cub3) |  | Proof of concept for LD_PRELOAD malware that uses extended att<br>ributes to protect files. |
| [webshell](https://github.com/tennc/webshell) | v-2021-<br>01-05 | This is a webshell open source project |
| [PrivExchange](https://github.com/dirkjanm/PrivExchange) |  | Exchange your privileges for Domain Admin privs by abusing Exc<br>hange |
| [tabby](https://github.com/wh1t3p1g/tabby) | v1.2.0-<br>3 | A CAT called tabby ( Code Analysis Tool ) |
| [SSRF-Testing](https://github.com/cujanovic/SSRF-Testing) |  | SSRF (Server Side Request Forgery) testing resources |
| [rdpwrap](https://github.com/asmtron/rdpwrap) |  | RDP Wrapper Library |
| [HikPwn](https://github.com/4n4nk3/HikPwn) |  | HikPwn, a simple scanner for Hikvision devices with basic vuln<br>erability scanning capabilities written in Python 3.8. |
| [lolcat](https://github.com/busyloop/lolcat) |  | Rainbows and unicorns! |
| [StratosphereLinux<br>IPS](https://github.com/stratosphereips/StratosphereLinuxIPS) | v1.0.7 | Slips, a free software behavioral Python intrusion prevention <br>system (IDS/IPS) that uses machine learning to detect malicious<br> behaviors in the network traffic. Stratosphere Laboratory, AIC<br>, FEL, CVUT in Prague. |
| [KCon](https://github.com/knownsec/KCon) |  | KCon is a famous Hacker Con powered by Knownsec Team. |
| [tp5-getshell](https://github.com/theLSA/tp5-getshell) |  | thinkphp5 rce getshell |
| [geacon](https://github.com/darkr4y/geacon) |  | Practice Go programming and implement CobaltStrike's Beacon in<br> Go |
| [shadowsocks](https://github.com/edwardz246003/shadowsocks) |  |  |
| [payloads](https://github.com/foospidy/payloads) |  | Git All the Payloads! A collection of web attack payloads. |
| [3gstudent](https://github.com/3gstudent/3gstudent) |  |  |
| [telegram-bot-api](https://github.com/go-telegram-bot-api/telegram-bot-api) | v5.5.1 | Golang bindings for the Telegram Bot API |
| [smbmap](https://github.com/ShawnDEvans/smbmap) | v1.9.3.<br>1 | SMBMap is a handy SMB enumeration tool |
| [TerraformGoat](https://github.com/HXSecurity/TerraformGoat) | 0.0.7 | TerraformGoat is HXSecurity research lab's "Vulnerable by Desi<br>gn" multi cloud deployment tool. |
| [CNVD-C-2019-48814<br>-COMMON](https://github.com/skytina/CNVD-C-2019-48814-COMMON) |  | CNVD-C-2019-48814 poc work on linux and windows |
| [bitcracker](https://github.com/e-ago/bitcracker) |  | BitCracker is the first open source password cracking tool for<br> memory units encrypted with BitLocker |
| [CVE-2020-9484](https://github.com/IdealDreamLast/CVE-2020-9484) |  | 用Kali 2.0复现Apache Tomcat Session反序列化代码执行漏洞 |
| [python-small-exam<br>ples](https://github.com/jackzhenguo/python-small-examples) |  | 告别枯燥，致力于打造 Python 实用小例子，更多Python良心教程见 P<br>ython中文网 http://www.zglg.work |
| [jira-mobile-ssrf-<br>exploit](https://github.com/assetnote/jira-mobile-ssrf-exploit) |  | Exploit code for Jira Mobile Rest Plugin SSRF (CVE-2022-26135) |
| [MX1014](https://github.com/L-codes/MX1014) | v2.4.0 | MX1014 is a flexible, lightweight and fast port scanner. |
| [RabR](https://github.com/0671/RabR) | 0.6.2 | Redis-Attack By Replication (通过主从复制攻击Redis)    |
| [GPON](https://github.com/f3d0x0/GPON) |  | Exploit for Remote Code Execution on GPON home routers (CVE-20<br>18-10562) written in Python. Initially disclosed by VPNMentor (<br>https://www.vpnmentor.com/blog/critical-vulnerability-gpon-rout<br>er/), kudos for their work. |
| [volatility3](https://github.com/volatilityfoundation/volatility3) | v2.5.0 | Volatility 3.0 development |
| [mssqli-duet](https://github.com/Keramas/mssqli-duet) |  | SQL injection script for MSSQL that extracts domain users from<br> an Active Directory environment based on RID bruteforcing |
| [websocat](https://github.com/vi/websocat) | v1.12.0 | Command-line client for WebSockets, like netcat (or curl) for <br>ws:// with advanced socat-like functions |
| [QEMU](https://github.com/qemu/QEMU) |  | Official QEMU mirror. Please see https://www.qemu.org/contribu<br>te/ for how to submit changes to QEMU. Pull Requests are ignore<br>d. Please only use release tarballs from the QEMU website. |
| [KillDefender](https://github.com/pwn1sher/KillDefender) |  | A small POC to make defender useless by removing its token pri<br>vileges and lowering the token integrity   |
| [shiftleft-go-demo](https://github.com/ShiftLeftSecurity/shiftleft-go-demo) |  |  |
| [winshock-test](https://github.com/anexia-it/winshock-test) |  | Bash script that tests if a system is Winshock (MS14-066) vuln<br>erable |
| [yaml-payload-for-<br>ruoyi](https://github.com/lz2y/yaml-payload-for-ruoyi) |  | A memory shell for ruoyi |
| [Empire](https://github.com/BC-SECURITY/Empire) | v5.7.3 | Empire is a post-exploitation and adversary emulation framewor<br>k that is used to aid Red Teams and Penetration Testers. |
| [AwesomeEncoder](https://github.com/AntSwordProject/AwesomeEncoder) |  | AntSword 自定义编(解)码器分享 |
| [CS-Loader](https://github.com/Gality369/CS-Loader) |  | CS免杀 |
| [yari](https://github.com/avast/yari) |  | YARI is an interactive debugger for YARA Language. |
| [PortTran](https://github.com/k8gege/PortTran) |  | PortTran (.NET端口转发工具,支持任意权限) |
| [SB-Actuator](https://github.com/rabbitmask/SB-Actuator) |  | Spring Boot Actuator未授权访问【XXE、RCE】单/多目标检测 |
| [goblin](https://github.com/xiecat/goblin) | v0.4.6 | 一款适用于红蓝对抗中的仿真钓鱼系统 |
| [follina](https://github.com/chvancooten/follina) |  |  |
| [proxify](https://github.com/projectdiscovery/proxify) | v0.0.12 | A versatile and portable proxy for capturing, manipulating, an<br>d replaying HTTP/HTTPS traffic on the go. |
| [alt-tab-macos](https://github.com/lwouis/alt-tab-macos) | v6.64.0 | Windows alt-tab on macOS  |
| [trash-cli](https://github.com/andreafrancia/trash-cli) |  | Command line interface to the freedesktop.org trashcan. |
| [wydomain](https://github.com/ring04h/wydomain) |  | to discover subdomains of your target domain |
| [javaweb-vuln](https://github.com/javaweb-rasp/javaweb-vuln) |  | RASP测试靶场 |
| [BypassCaiDao](https://github.com/admintony/BypassCaiDao) |  | 过WAF菜刀 |
| [subzy](https://github.com/LukaSikic/subzy) |  |  |
| [CVE-2019-13272](https://github.com/jas502n/CVE-2019-13272) |  | Linux 4.10 < 5.1.17 PTRACE_TRACEME local root |
| [weird_proxies](https://github.com/GrrrDog/weird_proxies) |  | Reverse proxies cheatsheet |
| [CVE-2022-34918-LP<br>E-PoC](https://github.com/randorisec/CVE-2022-34918-LPE-PoC) |  |  |
| [gophish](https://github.com/gophish/gophish) | v0.12.1 | Open-Source Phishing Toolkit |
| [jumpserver](https://github.com/jumpserver/jumpserver) | v3.8.2 | JumpServer 是广受欢迎的开源堡垒机，是符合 4A 规范的专业运维安<br>全审计系统。 |
| [Logout4Shell](https://github.com/Cybereason/Logout4Shell) |  | Use Log4Shell vulnerability to vaccinate a victim server again<br>st Log4Shell |
| [AlphaGolang](https://github.com/SentineLabs/AlphaGolang) |  | IDApython Scripts for Analyzing Golang Binaries |
| [FBI-WARNING-in-co<br>nsole](https://github.com/Mithrilwoodrat/FBI-WARNING-in-console) |  | FBI-WARNING-in-console |
| [dfirtriage](https://github.com/travisfoley/dfirtriage) |  | Digital forensic acquisition tool for Windows based incident r<br>esponse. |
| [package-manager-p<br>roxy-settings](https://github.com/comwrg/package-manager-proxy-settings) |  | 记录各个包管理器代理设置坑点。 |
| [CVE-2019-8451](https://github.com/jas502n/CVE-2019-8451) |  | Jira未授权SSRF漏洞 |
| [MSSQL-SQLi-Labs](https://github.com/Larryxi/MSSQL-SQLi-Labs) |  |  |
| [IDA-Pro-tips](https://github.com/VulnTotal-Team/IDA-Pro-tips) |  | IDA Pro每周小技巧 |
| [idcard](https://github.com/naozibuhao/idcard) |  |  |
| [DSInternals](https://github.com/MichaelGrafnetter/DSInternals) | v4.12 |  Directory Services Internals (DSInternals) PowerShell Module <br>and Framework |
| [merlin-agent](https://github.com/Ne0nd0g/merlin-agent) | v2.0.0 | Post-exploitation agent for Merlin |
| [rules](https://github.com/webanalyzer/rules) |  | 通用的指纹识别规则 |
| [dirble](https://github.com/nccgroup/dirble) | v1.4.2 | Fast directory scanning and scraping tool |
| [aSYNcrone](https://github.com/fatih4842/aSYNcrone) |  |  |
| [dics](https://github.com/haiyangma/dics) |  |  |
| [ICS-Protocol-iden<br>tify](https://github.com/hi-KK/ICS-Protocol-identify) |  | Using nmap NSE scripts for  identifying common ICS protocols[<br>使用nmap的nse脚本对常见工控协议进行识别，附对应nse脚本，并记录pc<br>ap流量] |
| [XORpass](https://github.com/devploit/XORpass) |  | Encoder to bypass WAF filters using XOR operations. |
| [sslh](https://github.com/yrutschle/sslh) |  | Applicative Protocol Multiplexer (e.g. share SSH and HTTPS on <br>the same port) |
| [humre](https://github.com/asweigart/humre) |  | A human-readable regular expression module for Python. |
| [gron](https://github.com/TomNomNom/gron) | v0.7.1 | Make JSON greppable! |
| [WeblogicEnvironme<br>nt](https://github.com/QAX-A-Team/WeblogicEnvironment) |  | Weblogic环境搭建工具 |
| [kjackal](https://github.com/dgoulet/kjackal) |  | Linux Rootkit Scanner |
| [gobfuscate](https://github.com/unixpickle/gobfuscate) |  | Obfuscate Go binaries and packages |
| [Invoke-x64dbg-loa<br>ddll](https://github.com/Rvn0xsy/Invoke-x64dbg-loaddll) |  | 调用x64dbg中的loadll.exe白加黑示例代码 |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | 10.1.4 | An interactive TLS-capable intercepting HTTP proxy for penetra<br>tion testers and software developers. |
| [poc_and_exp](https://github.com/TomAPU/poc_and_exp) |  | 搜集的或者自己写的poc或者exp |
| [CVE-2022-36804](https://github.com/notdls/CVE-2022-36804) |  | A real exploit for BitBucket RCE CVE-2022-36804 |
| [suricata](https://github.com/OISF/suricata) | suricat<br>a-7.0.2 | Suricata is a network Intrusion Detection System, Intrusion Pr<br>evention System and Network Security Monitoring engine develope<br>d by the OISF and the Suricata community. |
| [uncover](https://github.com/projectdiscovery/uncover) | v1.0.7 | Quickly discover exposed hosts on the internet using multiple <br>search engines. |
| [cve-2021-3449](https://github.com/terorie/cve-2021-3449) |  | CVE-2021-3449 OpenSSL denial-of-service exploit 👨🏻‍💻 |
| [repo-security-sca<br>nner](https://github.com/UKHomeOffice/repo-security-scanner) |  |  |
| [Grafana-VulnTips](https://github.com/jas502n/Grafana-VulnTips) |  |  |
| [Bug-Hunting-Domai<br>ns](https://github.com/TSlayman/Bug-Hunting-Domains) |  |  |
| [HTTP-Smuggling-La<br>b](https://github.com/ZeddYu/HTTP-Smuggling-Lab) |  | Use HTTP Smuggling Lab to learn HTTP Smuggling. |
| [ruby](https://github.com/ruby/ruby) | v3_2_2 | The Ruby Programming Language |
| [mole](https://github.com/ztgrace/mole) | v0.1 | Mole is a framework for identifying and exploiting out-of-band<br> application vulnerabilities. |
| [Apache-Solr-RCE](https://github.com/Imanfeng/Apache-Solr-RCE) |  | Apache Solr Exploits  🌟 |
| [cve-2020-11651-ex<br>p-plus](https://github.com/lovelyjuice/cve-2020-11651-exp-plus) |  |  |
| [HugeDirtyCowPOC](https://github.com/bindecy/HugeDirtyCowPOC) |  | A POC for the Huge Dirty Cow vulnerability (CVE-2017-1000405) |
| [TREVORspray](https://github.com/blacklanternsecurity/TREVORspray) |  | TREVORspray is a modular password sprayer with threading, clev<br>er proxying, loot modules, and more! |
| [dnstwist](https://github.com/elceef/dnstwist) | 2023091<br>8 | Domain name permutation engine for detecting homograph phishin<br>g attacks, typo squatting, and brand impersonation |
| [awesome-burp-suit<br>e](https://github.com/alphaSeclab/awesome-burp-suite) |  | Awesome Burp Suite Resources. 400+ open source Burp plugins, 4<br>00+ posts and videos. |
| [cve-2018-1273](https://github.com/jas502n/cve-2018-1273) |  | Spring Data Commons RCE 远程命令执行漏洞 |
| [netdiscover](https://github.com/alexxy/netdiscover) |  | netdiscover |
| [XxlJob-Hessian-RC<br>E](https://github.com/OneSourceCat/XxlJob-Hessian-RCE) |  | XxlJob<=2.1.2配置不当情况下反序列化RCE |
| [WordPress_4](https://github.com/brianwrf/WordPress_4) |  |  |
| [webshell](https://github.com/JoyChou93/webshell) |  | 入侵分析时发现的Webshell后门 |
| [conpot](https://github.com/mushorg/conpot) | Release<br>_0.6.0 | ICS/SCADA honeypot |
| [XssPy](https://github.com/faizann24/XssPy) |  | XssPy - Web Application XSS Scanner |
| [phishing_catcher](https://github.com/x0rz/phishing_catcher) |  | Phishing catcher using Certstream |
| [wesng](https://github.com/bitsadmin/wesng) |  | Windows Exploit Suggester - Next Generation |
| [CVE-2020-1472](https://github.com/SecuraBV/CVE-2020-1472) |  | Test tool for CVE-2020-1472 |
| [JSP-Webshells](https://github.com/threedr3am/JSP-Webshells) |  | Collect JSP webshell of various implementation methods. 收集JS<br>P Webshell的各种姿势 |
| [SSRFire](https://github.com/ksharinarayanan/SSRFire) |  | An automated SSRF finder. Just give the domain name and your s<br>erver and chill! ;) Also has options to find XSS and open redir<br>ects |
| [Tools](https://github.com/chrisdee/Tools) |  | GitHub repository for sysadmin related tools |
| [LogonTracer](https://github.com/JPCERTCC/LogonTracer) | v1.6.0 | Investigate malicious Windows logon by visualizing and analyzi<br>ng Windows event log |
| [CVE-2021-3156](https://github.com/reverse-ex/CVE-2021-3156) |  | CVE-2021-3156 |
| [jd-gui](https://github.com/java-decompiler/jd-gui) | v1.6.6 | A standalone Java Decompiler GUI |
| [My-Shodan-Scripts](https://github.com/random-robbie/My-Shodan-Scripts) |  | Collection of Scripts for shodan searching stuff. |
| [403-fuzz](https://github.com/ffffffff0x/403-fuzz) |  | 针对 403 页面的 fuzz 脚本 |
| [xss](https://github.com/keyus/xss) |  | php写的个人研究测试用的  xss cookie 攻击管理平台,开源出来 |
| [UPGDSED](https://github.com/hfiref0x/UPGDSED) | v1.1.2 | Universal PatchGuard and Driver Signature Enforcement Disable |
| [wix3](https://github.com/wixtoolset/wix3) | wix3112<br>rtm | WiX Toolset v3.x |
| [Struts2Environmen<br>t](https://github.com/wh1t3p1g/Struts2Environment) |  | Struts2 历史版本的漏洞环境 |
| [CVE-2018-2628](https://github.com/shengqi158/CVE-2018-2628) |  | CVE-2018-2628 & CVE-2018-2893 |
| [testssl](https://github.com/drwetter/testssl) |  |  |
| [delve](https://github.com/go-delve/delve) | v1.21.2 | Delve is a debugger for the Go programming language. |
| [coremail-exp](https://github.com/yuxiaoyou123/coremail-exp) |  |  |
| [OSCE](https://github.com/ihack4falafel/OSCE) |  | Collection of things made during my preparation to take on OSC<br>E |
| [neofetch](https://github.com/dylanaraps/neofetch) | 7.1.0 | 🖼️  A command-line system information tool written in bash 3<br>.2+ |
| [AES-Killer](https://github.com/Ebryx/AES-Killer) | v4.0 | Burp Plugin to decrypt AES encrypted traffic on the fly |
| [fi6s](https://github.com/sfan5/fi6s) |  | IPv6 network scanner designed to be fast |
| [Impulse](https://github.com/LimerBoy/Impulse) |  | :bomb: Impulse Denial-of-service ToolKit |
| [h3c-pt-tools](https://github.com/grutz/h3c-pt-tools) |  | Huawei/H3C/HP Penetration Testing Tools |
| [S9MF-php-webshell<br>-bypass](https://github.com/S9MF/S9MF-php-webshell-bypass) |  | 为方便WAF入库的项目 | 分享PHP免杀大马 | 菜是原罪 | 多姿势(假的<br>就一个)  |
| [LeakLooker](https://github.com/woj-ciech/LeakLooker) |  | Find open databases - Powered by Binaryedge.io |
| [coremail-address-<br>book](https://github.com/dpu/coremail-address-book) | 0.0.2 | 📧Coremail邮件系统组织通讯录导出脚本 |
| [phantom-attack](https://github.com/rexguowork/phantom-attack) |  | POC for Phantom Attack |
| [linux-hardening-c<br>hecklist](https://github.com/trimstray/linux-hardening-checklist) |  | Simple checklist to help you deploying the most important area<br>s of the GNU/Linux production systems - work in progress. |
| [ProxyLogon](https://github.com/p0wershe11/ProxyLogon) |  | ProxyLogon(CVE-2021-26855+CVE-2021-27065) Exchange Server RCE(<br>SSRF->GetWebShell) |
| [Windows-Exploit-S<br>uggester](https://github.com/GDSSecurity/Windows-Exploit-Suggester) |  |  |
| [riscv-ida](https://github.com/lcq2/riscv-ida) |  | RISC-V ISA processor module for IDAPro 7.x |
| [CVE-2020-1472](https://github.com/dirkjanm/CVE-2020-1472) |  | PoC for Zerologon - all research credits go to Tom Tervoort of<br> Secura |
| [CAAC-CTF-2018-Pri<br>mary](https://github.com/wrlu/CAAC-CTF-2018-Primary) |  | 2018年民航网络安全职业技能竞赛-初赛 |
| [S2-055-PoC](https://github.com/shengqi158/S2-055-PoC) |  | S2-055的环境，基于rest-show-case改造 |
| [fierce](https://github.com/mschwager/fierce) |  | A DNS reconnaissance tool for locating non-contiguous IP space<br>. |
| [vncpwd](https://github.com/jeroennijhof/vncpwd) | v0.1 | VNC Password Decrypter |
| [Exploits](https://github.com/lcashdol/Exploits) |  | Exploits for various CVEs |
| [poshkatz](https://github.com/Stealthbits/poshkatz) |  |  |
| [awesome-industria<br>l-control-system-s<br>ecurity](https://github.com/hslatman/awesome-industrial-control-system-security) |  | A curated list of resources related to Industrial Control Syst<br>em (ICS) security. |
| [trufflehog](https://github.com/trufflesecurity/trufflehog) | v3.62.1 | Find and verify credentials |
| [CVE-2022-25636](https://github.com/Bonfee/CVE-2022-25636) |  | CVE-2022-25636 |
| [as_webshell_venom](https://github.com/yzddmr6/as_webshell_venom) |  | 免杀webshell无限生成工具蚁剑版 |
| [outguess](https://github.com/crorvick/outguess) |  | An unmaintained fork of the OutGuess steganographic tool.  Try<br> https://github.com/resurrecting-open-source-projects/outguess <br>for possibly a better option. |
| [A8-OA-seeyon-RCE](https://github.com/RayScri/A8-OA-seeyon-RCE) |  | A Zhiyuan OA Collaborative Office Remote Code Execution Vulner<br>ability on Windows |
| [htpwdScan](https://github.com/lijiejie/htpwdScan) |  | HTTP weak pass scanner |
| [distorm](https://github.com/gdabah/distorm) | 3.5.2b | Powerful Disassembler Library For x86/AMD64 |
| [ntlmv1-multi](https://github.com/evilmog/ntlmv1-multi) |  | NTLMv1 Multitool |
| [donut](https://github.com/TheWover/donut) | v1.0 | Generates x86, x64, or AMD64+x86 position-independent shellcod<br>e that loads .NET Assemblies, PE files, and other Windows paylo<br>ads from memory and runs them with parameters |
| [CVE-2020-14645](https://github.com/Y4er/CVE-2020-14645) |  | Weblogic CVE-2020-14645 UniversalExtractor JNDI injection getD<br>atabaseMetaData() |
| [acefile](https://github.com/Ridter/acefile) |  | POC of https://research.checkpoint.com/extracting-code-executi<br>on-from-winrar/ |
| [source-code-pro](https://github.com/adobe-fonts/source-code-pro) | 2.042R-<br>u/1.062R<br>-i/1.026<br>R-vf | Monospaced font family for user interface and coding environme<br>nts |
| [RGPerson](https://github.com/gh0stkey/RGPerson) |  | RGPerson - Randomly generate identity information |
| [asset](https://github.com/netsecli/asset) |  | NMAP扫描网络资产自动导入到Elasticstack进行展示 |
| [Halfrost-Field](https://github.com/halfrost/Halfrost-Field) |  | ✍🏻 这里是写博客的地方 —— Halfrost-Field 冰霜之地 |
| [LSB-Steganography](https://github.com/RobinDavid/LSB-Steganography) |  | Python program to steganography files into images using the Le<br>ast Significant Bit. |
| [SIGRed_RCE_PoC](https://github.com/chompie1337/SIGRed_RCE_PoC) |  |  |
| [Teemo](https://github.com/bit4woo/Teemo) |  | A Domain Name & Email Address Collection Tool |
| [Spring-Boot-Actua<br>tor-Exploit](https://github.com/mpgn/Spring-Boot-Actuator-Exploit) |  | Spring Boot Actuator (jolokia) XXE/RCE |
| [Tentacle](https://github.com/orleven/Tentacle) |  | Tentacle is a POC vulnerability verification and exploit frame<br>work. It supports free extension of exploits and uses POC scrip<br>ts. It supports calls to zoomeye, fofa, shodan and other APIs t<br>o perform bulk vulnerability verification for multiple targets. |
| [proxypool](https://github.com/zu1k/proxypool) | v0.3.1 | Automatically crawls proxy nodes on the public internet, de-du<br>plicates and tests for usability and then provides a list of no<br>des |
| [subjs](https://github.com/lc/subjs) | v1.0.1 | Fetches javascript file from a list of URLS or subdomains. |
| [beanstack](https://github.com/x41sec/beanstack) | v0.6.1 | X41 BeanStack - Stack Trace Fingerprinting BETA |
| [china-operator-ip](https://github.com/gaoyifan/china-operator-ip) |  | 中国运营商IPv4/IPv6地址库-每日更新 |
| [Sensitive-word](https://github.com/57ing/Sensitive-word) |  | 收集的一些敏感词汇，挺全的，还细分了暴恐词库、反动词库、民生词<br>库、色情词库、贪腐词库、其他词库等 |
| [nextnet](https://github.com/hdm/nextnet) | v0.0.2 | nextnet is a pivot point discovery tool written in Go. |
| [staffdb](https://github.com/Dc7User/staffdb) |  |  |
| [SharpCookieMonste<br>r](https://github.com/m0rv4i/SharpCookieMonster) |  |  |
| [CTF](https://github.com/L1nwatch/CTF) |  | 保存有关自己做的 CTF 题目 |
| [cloud-torrent](https://github.com/jpillora/cloud-torrent) | 0.8.25 | ☁️ Cloud Torrent: a self-hosted remote torrent client |
| [glances](https://github.com/nicolargo/glances) | v3.4.0.<br>2 | Glances an Eye on your system. A top/htop alternative for GNU/<br>Linux, BSD, Mac OS and Windows operating systems. |
| [cve-2020-14386](https://github.com/cgwalters/cve-2020-14386) |  |  |
| [HOUDINI](https://github.com/cybersecsi/HOUDINI) | v0.2.9 | Hundreds of Offensive and Useful Docker Images for Network Int<br>rusion. The name says it all. |
| [CVE-2020-0796-PoC](https://github.com/eerykitty/CVE-2020-0796-PoC) |  | PoC for triggering buffer overflow via CVE-2020-0796 |
| [JSPHorse](https://github.com/EmYiQing/JSPHorse) |  |  |
| [deepce](https://github.com/stealthcopter/deepce) |  | Docker Enumeration, Escalation of Privileges and Container Esc<br>apes (DEEPCE) |
| [luadec](https://github.com/viruscamp/luadec) |  | Lua Decompiler for lua 5.1 , 5.2 and 5.3 |