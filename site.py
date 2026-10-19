import os, re, shutil

OUT = os.path.expanduser(r'~/Desktop/siersz-website')
DOMAIN = 'https://www.siersz.com'
UPDATED = '2026-10-16'

# ---------- placeholders (edit these, then re-run) ----------
C = {
    'zh': dict(brand='Siersz', legal='思尔兹贸易有限公司（示例）', email='info@example.com', phone='+00 000 0000 0000（示例）',
               addr='示例省示例市示例路 123 号 示例大厦 8 层（示例地址）', country='示例国家/地区'),
    'en': dict(brand='Siersz', legal='Siersz Trading Co., Ltd. (sample)', email='info@example.com', phone='+00 000 0000 0000 (sample)',
               addr='Floor 8, Sample Tower, 123 Sample Road, Sample City (sample address)', country='Sample Country'),
}

NAV = {
    'zh': [('index', '首页'), ('about', '关于我们'), ('services', '我们的服务'), ('products', '产品与分级'), ('sustainability', '可持续发展'), ('why-us', '为什么选择我们'), ('contact', '联系我们')],
    'en': [('index', 'Home'), ('about', 'About Us'), ('services', 'What We Do'), ('products', 'Products'), ('sustainability', 'Sustainability'), ('why-us', 'Why Siersz'), ('contact', 'Contact Us')],
}
GROUP_URL = 'https://www.sunstrike.com'
LEGAL = {
    'zh': [('privacy', '隐私政策'), ('terms', '使用条款'), ('cookies', 'Cookie 政策')],
    'en': [('privacy', 'Privacy Policy'), ('terms', 'Terms of Use'), ('cookies', 'Cookie Policy')],
}
UI = {
    'zh': dict(skip='跳到正文', toggle='EN', toggle_title='Switch to English', lang='zh-CN', menu='菜单',
               cta='联系我们', rights='版权所有。', group='Siersz 是 Sunstrike 集团旗下的姊妹公司，为独立法人实体。', group_link='访问 Sunstrike',
               rights2='', draft='占位内容：正式上线前请替换所有标有黄色底色的文字。',
               ck_text='本网站使用 Cookie 以改善浏览体验。详情请见', ck_ok='接受', ck_no='拒绝', updated='最后更新：'),
    'en': dict(skip='Skip to content', toggle='中文', toggle_title='切换到中文', lang='en', menu='Menu',
               cta='Contact us', rights='All rights reserved.', group='Siersz is a sister company of the Sunstrike group and a separate legal entity.', group_link='Visit Sunstrike',
               rights2='', draft='Placeholder content: replace everything highlighted in yellow before launch.',
               ck_text='This site uses cookies to improve your experience. See our', ck_ok='Accept', ck_no='Decline', updated='Last updated: '),
}



import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from logo import logo_svg, NAVY, AMBER


def ph(t):
    return f'<span class="ph">{t}</span>'


def P(lang):
    c = C[lang]
    return {k: ph(v) for k, v in c.items() if k != 'brand'} | {'brand': c['brand']}


# ---------- page content ----------
def pages(lang):
    p = P(lang)
    if lang == 'zh':
        return {
            'index': dict(title='全球二手苹果设备 B2B 供应伙伴', desc='Siersz 专注于二手苹果设备（以 iPhone 为主）的 B2B 批发供应。', body=f'''
<section class="hero"><div class="wrap">
  <p class="eyebrow">B2B · 二手苹果设备 · SUNSTRIKE 集团成员</p>
  <h1>让每一台设备<br>拥有第二次生命</h1>
  <p class="lead">稳定货源 · 清晰分级 · 面向企业客户的二手 iPhone 供应伙伴。</p>
  <a class="btn" href="contact.html">申请开通贸易账户</a>
</div></section>
<section class="sec"><div class="wrap two">
  <div><h2>关于 {p['brand']}</h2></div>
  <div><p>{p['brand']} 专注于二手苹果设备的企业间批发供应，产品以 iPhone 为主。我们为运营商、零售商、电商平台和经销商提供稳定、透明、分级一致的货源。</p>
  <p>{p['brand']} 是 Sunstrike 集团的姊妹公司，依托集团遍布全球的供应网络，以中文为主要沟通语言，服务中文市场的企业买家。</p>
  {ph('[在此补充 Siersz 自身的成立时间、业务模式、服务对象]')}
  <p><a class="more" href="about.html">了解更多 →</a></p></div>
</div></section>
<section class="sec alt"><div class="wrap"><h2>我们的服务</h2>
<div class="cards">
  <article class="card"><h3>批发供应</h3><p>面向企业客户的二手 iPhone 批量供应，规格、成色与数量清晰明确。</p></article>
  <article class="card"><h3>分级与质检</h3><p>统一的成色分级标准，出货前逐台检测并记录。</p></article>
  <article class="card"><h3>物流与交付</h3><p>按订单安排发货与交付，订单进度可追踪。</p></article>
</div><p><a class="more" href="services.html">查看全部服务 →</a></p></div></section>
<section class="sec"><div class="wrap"><h2>合作流程</h2>
<ol class="steps">
<li><b>1</b><h3>货源</h3><p>通过集团网络获取设备。</p></li>
<li><b>2</b><h3>检测分级</h3><p>逐台检测、清除数据、统一分级。</p></li>
<li><b>3</b><h3>发货交付</h3><p>按订单发货并同步进度。</p></li>
<li><b>4</b><h3>售后跟进</h3><p>反馈与持续合作。{ph('[如有质保请补充]')}</p></li>
</ol></div></section>
<section class="sec alt"><div class="wrap"><h2>我们服务的客户</h2>
<ul class="ticks cols"><li>移动运营商</li><li>零售商与连锁渠道</li><li>电商平台</li><li>经销商与批发商</li><li>保险与设备更换服务商</li><li>企业与机构采购方</li></ul>
<p class="note">{ph('[按实际客户类型增删]')}</p></div></section>
<section class="sec"><div class="wrap"><h2>集团实力：Sunstrike</h2>
<p>以下为 Sunstrike International 集团的整体数据，Siersz 依托这一网络开展业务。</p>
<div class="stats">
  <div><b>1997</b><span>集团创立</span></div>
  <div><b>85</b><span>服务的国家和地区</span></div>
  <div><b>2,500+</b><span>全球合作伙伴</span></div>
  <div><b>1M+</b><span>每年处理设备（台）</span></div>
</div><p class="note">{ph('[上线前请与集团确认以上数据，并确保口径一致]')}</p></div></section>
<section class="sec alt"><div class="wrap"><h2>全球网络</h2>
<p>集团在五大洲布局，主要枢纽包括：</p>
<div class="stats net">
  <div><b>迈阿密</b><span>北美</span></div>
  <div><b>伦敦</b><span>欧洲</span></div>
  <div><b>迪拜</b><span>中东</span></div>
  <div><b>香港 · 印度</b><span>亚洲</span></div>
</div><p class="note">{ph('[请确认哪些枢纽可以公开，以及 Siersz 实际可使用的节点]')}</p></div></section>
<section class="cta"><div class="wrap"><h2>成为我们的合作伙伴</h2><p>告诉我们您的需求和业务规模，我们将为您准备合适的方案。</p><a class="btn light" href="contact.html">申请开通贸易账户</a></div></section>'''),
            'about': dict(title='关于我们', desc='了解 Siersz 的背景、愿景与价值观。', body=f'''
<section class="page-head"><div class="wrap"><h1>关于我们</h1><p class="lead">深耕二手苹果设备的企业间供应。</p></div></section>
<section class="sec"><div class="wrap two"><div><h2>公司简介</h2></div><div>
<p>{p['brand']} 是一家专注于二手苹果设备（以 iPhone 为主）的 B2B 供应商。二手设备市场分散、信息不透明、品质参差，企业买家常面临货源不稳、分级不一致的问题。我们希望用稳定的流程和清晰的沟通改善这一状况。</p>
{ph('[在此补充：公司成立时间、总部所在地、团队背景、主要合作对象]')}
</div></div></section>
<section class="sec alt"><div class="wrap two"><div><h2>愿景</h2></div><div>
<p>让每一台设备都有再次被使用的机会，让二手成为一种理性的选择，而不是退而求其次。</p>
{ph('[可根据公司实际定位修改愿景]')}</div></div></section>
<section class="sec"><div class="wrap"><h2>核心价值观</h2>
<div class="cards">
<article class="card"><h3>精准</h3><p>从收货到交付，每一步都有明确标准，可衡量、可追溯。</p></article>
<article class="card"><h3>循环</h3><p>延长设备使用寿命，减少电子废弃物。</p></article>
<article class="card"><h3>伙伴</h3><p>以稳定、透明和履约能力，与客户建立长期合作。</p></article>
</div></div></section>
<section class="sec alt"><div class="wrap two"><div><h2>Sunstrike 集团</h2></div><div>
<p>{p['brand']} 是 Sunstrike International Limited 的姊妹公司，两者为各自独立的法人实体。Sunstrike 成立于 1997 年，是专注“第二生命科技”的全球分销商，业务覆盖五大洲，主要枢纽位于迈阿密、伦敦、迪拜、香港和印度。</p>
<p><a class="more" href="{GROUP_URL}" target="_blank" rel="noopener">访问 Sunstrike 官网 →</a></p>
{ph('[请确认以上集团信息的措辞，并说明 Siersz 与集团之间的具体合作方式]')}</div></div></section>
<section class="sec"><div class="wrap two"><div><h2>业务布局</h2></div><div>
<p>{ph('[填写 Siersz 自身的所在地、仓库及办公地点；没有的内容请删除]')}</p></div></div></section>'''),
            'services': dict(title='我们的服务', desc='批发供应、分级质检、物流交付。', body=f'''
<section class="page-head"><div class="wrap"><h1>我们的服务</h1><p class="lead">覆盖二手苹果设备从货源到交付的关键环节。</p></div></section>
<section class="sec"><div class="wrap">
<div class="svc"><h2>01 批发供应</h2><p>向企业客户提供二手 iPhone 批量供应。可按型号、容量、颜色和成色等级下单，并提供清晰的报价与交货安排。</p>
<ul><li>型号覆盖：{ph('[例如 iPhone 12 至 iPhone 17 系列，按实际填写]')}</li><li>起订量：{ph('[填写起订量]')}</li><li>报价方式：{ph('[币种、含税/不含税、贸易条款]')}</li></ul></div>
<div class="svc"><h2>02 分级与质检</h2><p>采用统一的成色分级标准，出货前逐台检测、清除数据并记录结果，让买家清楚知道收到的是什么。</p>
<ul><li>分级标准：{ph('[如 A+ / A / B / C 的具体定义]')}</li><li>检测项目：{ph('[外观、屏幕、电池健康度、功能测试等]')}</li><li>数据清除：{ph('[说明采用的方式]')}</li></ul></div>
<div class="svc"><h2>03 物流与交付</h2><p>根据订单安排发货，并及时同步发货与到货信息。</p>
<ul><li>发货地：{ph('[仓库所在地]')}</li><li>交货周期：{ph('[填写常规周期]')}</li><li>售后与退换：{ph('[填写政策]')}</li></ul></div>
</div></section>
<section class="sec alt"><div class="wrap"><h2>合作模式</h2>
<p>根据采购规模与合作深度，提供三种合作方式。</p>
<div class="cards">
<article class="card"><h3>批发</h3><p>适合大批量采购的经销商：阶梯价格、库存管理、物流支持。</p><p>{ph('[起订量，如每月 XX 台]')}</p></article>
<article class="card"><h3>区域独家</h3><p>适合区域领先企业：区域合作权利、专属客户经理、定制物流。</p><p>{ph('[起订量与条件]')}</p></article>
<article class="card"><h3>战略合作</h3><p>适合成长型伙伴：联合拓展市场、系统对接、收益共享。</p><p>{ph('[起订量与条件]')}</p></article>
</div></div></section>
<section class="sec"><div class="wrap"><h2>合作流程</h2>
<div class="cards">
<article class="card"><h3>1 洽谈与签约</h3><p>沟通需求、确认条款并签署合同。</p></article>
<article class="card"><h3>2 对接与备货</h3><p>确认型号、数量与交付方式，安排库存。</p></article>
<article class="card"><h3>3 发货上线</h3><p>首批发货，持续跟踪交付与反馈。</p></article>
<article class="card"><h3>4 持续合作</h3><p>稳定供货，按需扩大规模。</p></article>
</div><p class="note">{ph('[请按实际周期补充各阶段所需时间，如第 1–4 周]')}</p></div></section>
<section class="cta"><div class="wrap"><h2>需要报价或样品？</h2><p>请发送您的型号、数量和交货地点。</p><a class="btn light" href="contact.html">联系我们</a></div></section>'''),
            'products': dict(title='产品与分级', desc='Siersz 提供的二手 iPhone 型号、成色分级与质检标准。', body=f'''
<section class="page-head"><div class="wrap"><h1>产品与分级</h1><p class="lead">以二手 iPhone 为主，统一的成色分级与质检标准。</p></div></section>
<section class="sec"><div class="wrap"><h2>产品范围</h2>
<p>主营二手 iPhone，可按型号、容量、颜色和成色下单。{ph('[列出实际可供的型号范围，如 iPhone 12–iPhone 17]')}</p>
<p>其他苹果产品（iPad、MacBook、Apple Watch、AirPods）可通过集团网络询价。{ph('[请确认是否对外提供]')}</p></div></section>
<section class="sec alt"><div class="wrap"><h2>成色分级</h2>
<div class="cards">
<article class="card"><h3>A+ 近乎全新</h3><p>{ph('[外观与功能的具体定义]')}</p></article>
<article class="card"><h3>A 轻微使用痕迹</h3><p>{ph('[外观与功能的具体定义]')}</p></article>
<article class="card"><h3>B 明显使用痕迹</h3><p>{ph('[外观与功能的具体定义]')}</p></article>
<article class="card"><h3>C 较多磨损</h3><p>{ph('[外观与功能的具体定义]')}</p></article>
</div><p class="note">{ph('[分级名称与定义仅为示例，请按实际标准修改]')}</p></div></section>
<section class="sec"><div class="wrap"><h2>质检与保障</h2>
<ul class="ticks"><li>逐台功能与外观检测</li><li>数据清除并记录</li><li>来源可追溯</li><li>质保与售后：{ph('[如有质保期限与条件请填写]')}</li></ul></div></section>
<section class="cta"><div class="wrap"><h2>需要最新库存与报价？</h2><p>请发送型号、成色和数量需求。</p><a class="btn light" href="contact.html">申请开通贸易账户</a></div></section>'''),
            'sustainability': dict(title='可持续发展', desc='循环经济：让设备被再次使用，减少电子废弃物。', body=f'''
<section class="page-head"><div class="wrap"><h1>可持续发展</h1><p class="lead">延长设备寿命，是对环境最直接的贡献。</p></div></section>
<section class="sec"><div class="wrap two"><div><h2>循环经济</h2></div><div>
<p>电子废弃物是增长最快的垃圾类型之一。让仍然可用的设备经过检测后再次流通，可以减少新设备生产带来的资源消耗和碳排放。</p>
{ph('[如需引用电子废弃物或碳排放数据，请注明权威来源与年份]')}</div></div></section>
<section class="sec alt"><div class="wrap"><h2>我们的做法</h2>
<div class="cards">
<article class="card"><h3>回收</h3><p>从企业渠道收集仍有使用价值的设备。</p></article>
<article class="card"><h3>检测</h3><p>逐台检测、清除数据并分级。</p></article>
<article class="card"><h3>再流通</h3><p>通过 B2B 渠道让设备进入下一段使用周期。</p></article>
</div></div></section>
<section class="sec"><div class="wrap two"><div><h2>集团的承诺</h2></div><div>
<p>Sunstrike 集团将可持续发展作为核心方向之一。{ph('[认证、减碳数据等仅可在有文件证明时填写，并注明属于集团还是 Siersz]')}</p>
<p><a class="more" href="{GROUP_URL}" target="_blank" rel="noopener">了解 Sunstrike →</a></p></div></div></section>'''),
            'why-us': dict(title='为什么选择我们', desc='选择 Siersz 作为二手苹果设备供应伙伴的理由。', body=f'''
<section class="page-head"><div class="wrap"><h1>为什么选择我们</h1><p class="lead">企业客户选择我们的几点理由。</p></div></section>
<section class="sec"><div class="wrap"><div class="cards big">
<article class="card"><h3>01 专注苹果设备</h3><p>只做苹果二手设备，资源、经验与市场判断都围绕这一领域积累。</p></article>
<article class="card"><h3>02 分级清晰一致</h3><p>统一的分级标准和检测记录，减少收货后的争议。</p></article>
<article class="card"><h3>03 集团支持的货源</h3><p>依托 Sunstrike 集团覆盖五大洲的供应网络获取货源。{ph('[说明具体货源渠道，仅填写真实情况]')}</p></article>
<article class="card"><h3>04 沟通高效</h3><p>订单、库存和交付进度清晰透明，响应及时。</p></article>
<article class="card"><h3>05 可长期合作</h3><p>重视履约与口碑，以长期稳定的合作为目标。</p></article>
</div><p class="note">以上为示例卖点，请根据公司实际能力修改或删减，避免未经证实的表述。</p></div></section>'''),
            'contact': dict(title='联系我们', desc='联系 Siersz，洽谈合作。', body=f'''
<section class="page-head"><div class="wrap"><h1>联系我们</h1><p class="lead">请告诉我们您的需求和业务规模，我们将尽快回复。</p></div></section>
<section class="sec"><div class="wrap two"><div><h2>联系方式</h2></div><div>
<dl class="contact">
<dt>邮箱</dt><dd>{p['email']}</dd>
<dt>电话</dt><dd>{p['phone']}</dd>
<dt>地址</dt><dd>{p['addr']}</dd>
<dt>工作时间</dt><dd>{ph('[例如 周一至周五 9:00–18:00（北京时间）]')}</dd>
</dl>
<h2>申请开通贸易账户</h2>
<p>请发邮件并注明：公司名称与所在国家/地区、所需型号与数量、预计月采购量、交货地点。我们的团队将尽快与您联系。</p>
<p><a class="btn" href="mailto:{C['zh']['email']}?subject=%E8%B4%B8%E6%98%93%E8%B4%A6%E6%88%B7%E7%94%B3%E8%AF%B7">申请开通贸易账户</a></p>
<p class="note">发布前请把按钮中的邮箱换成真实邮箱（在 site.py 顶部修改后重新生成）。</p></div></div></section>'''),
            'faq': dict(title='常见问题', desc='关于产品、分级、发货与合作方式的常见问题。', body=f'''
<section class="page-head"><div class="wrap"><h1>常见问题</h1><p class="lead">合作前最常被问到的问题。</p></div></section>
<section class="sec"><div class="wrap faqs">
<details class="faq"><summary>你们销售什么产品？</summary><div><p>主营面向企业客户的二手 iPhone，可按型号、容量、颜色和成色等级下单。其他苹果产品可通过集团网络询价。</p></div></details>
<details class="faq"><summary>最低起订量是多少？</summary><div><p>起订量视型号和合作模式而定。{ph('[填写起订量]')}</p></div></details>
<details class="faq"><summary>成色是如何分级的？</summary><div><p>我们使用统一的成色分级标准，详见“产品与分级”页面。</p></div></details>
<details class="faq"><summary>设备会经过检测并清除数据吗？</summary><div><p>是的，出货前逐台检测功能与外观，并清除数据、记录结果。{ph('[按实际流程核对]')}</p></div></details>
<details class="faq"><summary>有质保和退换政策吗？</summary><div><p>{ph('[填写质保期限、退换条件与流程]')}</p></div></details>
<details class="faq"><summary>如何发货？支持哪些贸易条款？</summary><div><p>按订单安排发货。{ph('[填写发货地、常用贸易条款（如 FOB/CIF）和交货周期]')}</p></div></details>
<details class="faq"><summary>支持哪些付款方式？</summary><div><p>{ph('[填写币种与付款方式]')}</p></div></details>
<details class="faq"><summary>如何开通贸易账户？</summary><div><p>请通过“联系我们”页面发送邮件，说明公司名称与所在国家/地区、需求型号与数量、预计月采购量和交货地点，我们的团队会尽快联系您。</p></div></details>
<details class="faq"><summary>你们是 Apple 授权经销商吗？</summary><div><p>我们是独立的二手设备供应商，与 Apple 无关联。Apple、iPhone 为 Apple Inc. 的商标。{ph('[请按实际授权情况核对此回答]')}</p></div></details>
<details class="faq"><summary>Siersz 与 Sunstrike 是什么关系？</summary><div><p>Siersz 是 Sunstrike 集团的姊妹公司，双方为各自独立的法人实体。我们依托集团的全球供应网络开展业务。</p></div></details>
</div></section>
<section class="cta"><div class="wrap"><h2>还有其他问题？</h2><p>欢迎直接联系我们。</p><a class="btn light" href="contact.html">联系我们</a></div></section>'''),
            'privacy': dict(title='隐私政策', desc='Siersz 隐私政策。', legal=True, body=f'''
<p>{p['legal']}（以下简称“我们”）重视您的隐私。本政策说明我们在您访问 www.siersz.com 及与我们联系时，如何收集、使用和保护您的个人信息。</p>
<h2>1. 我们收集的信息</h2><ul><li>您主动提供的信息：姓名、公司名称、邮箱、电话及您在邮件中提供的内容。</li><li>自动收集的信息：浏览器类型、设备信息、访问页面、访问时间和大致地区等（通过日志或 Cookie）。</li></ul>
<h2>2. 使用目的</h2><ul><li>回复您的咨询并洽谈业务合作；</li><li>改进网站内容与访问体验；</li><li>履行法律法规要求的义务。</li></ul>
<h2>3. 信息共享</h2><p>我们不会出售您的个人信息。仅在下列情况下共享：经您同意；为提供服务而委托的服务提供商（须承担保密义务）；法律法规要求或有权机关依法要求。</p>
<h2>4. 信息保存</h2><p>我们仅在实现上述目的所需期限内保存信息，法律另有要求的除外。{ph('[如有具体保存期限请填写]')}</p>
<h2>5. 信息安全</h2><p>我们采取合理的技术和管理措施保护信息，但互联网传输无法保证绝对安全。</p>
<h2>6. 您的权利</h2><p>您可以要求查阅、更正或删除您的个人信息，或撤回同意。请通过下方联系方式与我们联系。</p>
<h2>7. 跨境传输</h2><p>{ph('[如数据存储或处理涉及境外，请在此说明]')}</p>
<h2>8. 未成年人</h2><p>本网站面向企业用户，不面向未成年人。</p>
<h2>9. 政策更新</h2><p>我们可能不时更新本政策，更新后的版本将发布在本页面。</p>
<h2>10. 联系我们</h2><p>邮箱：{p['email']}<br>地址：{p['addr']}</p>'''),
            'terms': dict(title='使用条款', desc='Siersz 网站使用条款。', legal=True, body=f'''
<p>欢迎访问 www.siersz.com（“本网站”），由 {p['legal']}（“我们”）运营。访问或使用本网站即表示您同意本条款。</p>
<h2>1. 网站内容</h2><p>本网站仅提供公司及业务的一般性信息，不构成要约、报价或合同。具体交易以双方书面确认的订单或合同为准。</p>
<h2>2. 知识产权</h2><p>本网站的文字、图片、标识和设计归我们或相关权利人所有。未经书面许可，不得复制、修改或用于商业用途。</p>
<h2>3. 第三方商标</h2><p>网站中提及的 Apple、iPhone 等名称和商标归其各自所有者所有。我们与这些商标所有者之间的关系仅限于{ph('[如实说明，例如“独立的二手设备经销商，与 Apple 无关联”]')}。</p>
<p>{p['brand']} 是 Sunstrike International Limited 的姊妹公司，双方为各自独立的法人实体；除非另有说明，本网站关于一方的信息不代表另一方。</p>
<h2>4. 合理使用</h2><p>您不得利用本网站从事违法行为、干扰网站运行或试图未经授权访问系统。</p>
<h2>5. 免责声明</h2><p>网站内容按“现状”提供，我们不保证其完整、准确或持续可用。在法律允许范围内，我们不对因使用本网站产生的间接损失承担责任。</p>
<h2>6. 外部链接</h2><p>本网站可能包含第三方链接，我们对其内容不负责任。</p>
<h2>7. 条款变更</h2><p>我们可随时修改本条款，修改后继续使用即视为接受。</p>
<h2>8. 适用法律与争议解决</h2><p>本条款适用 {p['country']} 的法律。争议应先友好协商；协商不成的，提交 {ph('[管辖法院或仲裁机构]')} 解决。</p>
<h2>9. 联系我们</h2><p>邮箱：{p['email']}</p>'''),
            'cookies': dict(title='Cookie 政策', desc='Siersz Cookie 政策。', legal=True, body=f'''
<p>本政策说明 www.siersz.com 如何使用 Cookie 及类似技术。</p>
<h2>1. 什么是 Cookie</h2><p>Cookie 是网站存放在您设备上的小型文本文件，用于记住您的偏好并帮助我们了解网站使用情况。</p>
<h2>2. 我们使用的类型</h2><ul><li><b>必要型：</b>保证网站正常运行，例如记住您对本横幅的选择。</li><li><b>分析型：</b>统计访问量和页面表现（仅在您接受后启用）。{ph('[如未使用任何分析工具，请删除此项]')}</li></ul>
<h2>3. 如何管理</h2><p>您可以通过页面底部横幅接受或拒绝非必要 Cookie，也可在浏览器设置中删除或阻止 Cookie。阻止部分 Cookie 可能影响网站功能。</p>
<h2>4. 第三方</h2><p>{ph('[如使用第三方分析或嵌入内容，请列出名称和用途]')}</p>
<h2>5. 联系我们</h2><p>邮箱：{p['email']}</p>'''),
        }
    return {
        'index': dict(title='A reliable partner for pre-owned Apple devices', desc='Siersz supplies pre-owned Apple devices, mainly iPhone, to business buyers.', body=f'''
<section class="hero"><div class="wrap">
  <p class="eyebrow">B2B · Pre-owned Apple devices · A Sunstrike group company</p>
  <h1>Giving every device<br>a second life</h1>
  <p class="lead">Dependable supply · Clear grading · Pre-owned iPhone for business buyers.</p>
  <a class="btn" href="contact.html">Open a trade account</a>
</div></section>
<section class="sec"><div class="wrap two">
  <div><h2>About {p['brand']}</h2></div>
  <div><p>{p['brand']} supplies pre-owned Apple devices, mainly iPhone, to business customers. We work with carriers, retailers, e-commerce platforms and distributors that need consistent supply and transparent grading.</p>
  <p>{p['brand']} is a sister company of the Sunstrike group. We draw on the group's worldwide supply network and serve Chinese-speaking business buyers in their own language.</p>
  {ph("[Add Siersz's own details: year founded, business model, who you serve]")}
  <p><a class="more" href="about.html">Learn more →</a></p></div>
</div></section>
<section class="sec alt"><div class="wrap"><h2>What we do</h2>
<div class="cards">
  <article class="card"><h3>Wholesale supply</h3><p>Bulk pre-owned iPhone supply for business buyers, with clear model, capacity, grade and quantity.</p></article>
  <article class="card"><h3>Grading and inspection</h3><p>A consistent grading standard, with each device tested and recorded before shipment.</p></article>
  <article class="card"><h3>Logistics and delivery</h3><p>Shipping arranged per order, with order progress you can follow.</p></article>
</div><p><a class="more" href="services.html">See all services →</a></p></div></section>
<section class="sec"><div class="wrap"><h2>How we work</h2>
<ol class="steps">
<li><b>1</b><h3>Source</h3><p>Devices come in through the group network.</p></li>
<li><b>2</b><h3>Test and grade</h3><p>Each unit tested, data-erased and graded.</p></li>
<li><b>3</b><h3>Ship</h3><p>Dispatched per order, with progress shared.</p></li>
<li><b>4</b><h3>Support</h3><p>Feedback and ongoing cooperation. {ph('[Add warranty if any]')}</p></li>
</ol></div></section>
<section class="sec alt"><div class="wrap"><h2>Who we serve</h2>
<ul class="ticks cols"><li>Mobile network operators</li><li>Retailers and retail chains</li><li>E-commerce platforms</li><li>Distributors and wholesalers</li><li>Insurers and device-replacement providers</li><li>Enterprise and public-sector buyers</li></ul>
<p class="note">{ph('[Add or remove customer types to match reality]')}</p></div></section>
<section class="sec"><div class="wrap"><h2>Group strength: Sunstrike</h2>
<p>These figures describe the Sunstrike International group as a whole. Siersz operates on the strength of this network.</p>
<div class="stats">
  <div><b>1997</b><span>group founded</span></div>
  <div><b>85</b><span>countries served</span></div>
  <div><b>2,500+</b><span>global partners</span></div>
  <div><b>1M+</b><span>devices handled per year</span></div>
</div><p class="note">{ph('[Confirm these figures with the group before launch and keep them consistent]')}</p></div></section>
<section class="sec alt"><div class="wrap"><h2>Global network</h2>
<p>The group operates across five continents. Main hubs include:</p>
<div class="stats net">
  <div><b>Miami</b><span>North America</span></div>
  <div><b>London</b><span>Europe</span></div>
  <div><b>Dubai</b><span>Middle East</span></div>
  <div><b>Hong Kong · India</b><span>Asia</span></div>
</div><p class="note">{ph('[Confirm which hubs may be shown publicly and which ones Siersz can actually use]')}</p></div></section>
<section class="cta"><div class="wrap"><h2>Become a partner</h2><p>Tell us what you need and the scale of your business, and we will prepare a suitable proposal.</p><a class="btn light" href="contact.html">Open a trade account</a></div></section>'''),
        'about': dict(title='About Us', desc="Siersz's background, vision and values.", body=f'''
<section class="page-head"><div class="wrap"><h1>About Us</h1><p class="lead">Business-to-business supply of pre-owned Apple devices.</p></div></section>
<section class="sec"><div class="wrap two"><div><h2>Company profile</h2></div><div>
<p>{p['brand']} is a B2B supplier of pre-owned Apple devices, mainly iPhone. The pre-owned market is fragmented and inconsistent, and business buyers often face unreliable supply and uneven grading. We aim to improve that with dependable processes and clear communication.</p>
{ph('[Add: year founded, headquarters, team background, main customer types]')}
</div></div></section>
<section class="sec alt"><div class="wrap two"><div><h2>Vision</h2></div><div>
<p>To give every device the chance to be useful again, and to make pre-owned a sensible choice rather than a compromise.</p>
{ph('[Edit the vision to match the company]')}</div></div></section>
<section class="sec"><div class="wrap"><h2>Core values</h2>
<div class="cards">
<article class="card"><h3>Precision</h3><p>Every step from intake to delivery follows a defined standard that can be measured and traced.</p></article>
<article class="card"><h3>Circularity</h3><p>Extending device lifespans and reducing electronic waste.</p></article>
<article class="card"><h3>Partnership</h3><p>Long-term relationships built on consistency, transparency and delivery.</p></article>
</div></div></section>
<section class="sec alt"><div class="wrap two"><div><h2>The Sunstrike group</h2></div><div>
<p>{p['brand']} is a sister company of Sunstrike International Limited. The two are separate legal entities. Sunstrike was founded in 1997 and is a global distributor focused on second-life technology, with a presence on five continents and main hubs in Miami, London, Dubai, Hong Kong and India.</p>
<p><a class="more" href="{GROUP_URL}" target="_blank" rel="noopener">Visit the Sunstrike website →</a></p>
{ph("[Confirm the wording about the group and describe how Siersz and the group work together]")}</div></div></section>
<section class="sec"><div class="wrap two"><div><h2>Where we operate</h2></div><div>
<p>{ph("[List Siersz's own location, warehouses and offices. Delete anything that does not apply]")}</p></div></div></section>'''),
        'services': dict(title='What We Do', desc='Wholesale supply, grading and inspection, logistics.', body=f'''
<section class="page-head"><div class="wrap"><h1>What We Do</h1><p class="lead">The key steps from supply to delivery of pre-owned Apple devices.</p></div></section>
<section class="sec"><div class="wrap">
<div class="svc"><h2>01 Wholesale supply</h2><p>Bulk pre-owned iPhone supply for business customers. Order by model, capacity, colour and grade, with clear pricing and delivery arrangements.</p>
<ul><li>Models: {ph('[e.g. iPhone 12 to iPhone 17 series, as applicable]')}</li><li>Minimum order: {ph('[enter minimum order quantity]')}</li><li>Pricing: {ph('[currency, tax treatment, trade terms]')}</li></ul></div>
<div class="svc"><h2>02 Grading and inspection</h2><p>A consistent cosmetic grading standard. Each device is tested, data-erased and recorded before shipment, so buyers know what they receive.</p>
<ul><li>Grades: {ph('[define A+ / A / B / C]')}</li><li>Tests: {ph('[appearance, screen, battery health, function tests]')}</li><li>Data erasure: {ph('[describe the method]')}</li></ul></div>
<div class="svc"><h2>03 Logistics and delivery</h2><p>Shipping is arranged per order, with dispatch and arrival updates.</p>
<ul><li>Ships from: {ph('[warehouse location]')}</li><li>Typical lead time: {ph('[enter lead time]')}</li><li>Returns and after-sales: {ph('[enter policy]')}</li></ul></div>
</div></section>
<section class="sec alt"><div class="wrap"><h2>Partnership models</h2>
<p>Three ways to work with us, depending on your scale and the depth of cooperation.</p>
<div class="cards">
<article class="card"><h3>Wholesale</h3><p>For high-volume distributors: tiered pricing, inventory management and logistics support.</p><p>{ph('[minimum volume, e.g. XX units per month]')}</p></article>
<article class="card"><h3>Exclusive</h3><p>For regional leaders: territory rights, a dedicated account team and custom logistics.</p><p>{ph('[minimum volume and conditions]')}</p></article>
<article class="card"><h3>Strategic</h3><p>For growth partners: joint market expansion, system integration and revenue sharing.</p><p>{ph('[minimum volume and conditions]')}</p></article>
</div></div></section>
<section class="sec"><div class="wrap"><h2>How we start</h2>
<div class="cards">
<article class="card"><h3>1 Agree terms</h3><p>We discuss your needs, confirm terms and sign the contract.</p></article>
<article class="card"><h3>2 Set up and allocate</h3><p>We confirm models, quantities and delivery method, and allocate stock.</p></article>
<article class="card"><h3>3 Ship</h3><p>The first shipment goes out, with delivery and feedback followed closely.</p></article>
<article class="card"><h3>4 Grow</h3><p>Steady supply, scaled up as you need.</p></article>
</div><p class="note">{ph('[Add the real time for each stage, e.g. weeks 1–4]')}</p></div></section>
<section class="cta"><div class="wrap"><h2>Need a quote or samples?</h2><p>Send us your models, quantities and delivery location.</p><a class="btn light" href="contact.html">Contact us</a></div></section>'''),
        'products': dict(title='Products and Grades', desc='The pre-owned iPhone models, cosmetic grades and inspection standards Siersz supplies.', body=f'''
<section class="page-head"><div class="wrap"><h1>Products and Grades</h1><p class="lead">Mainly pre-owned iPhone, with one consistent grading and inspection standard.</p></div></section>
<section class="sec"><div class="wrap"><h2>Product range</h2>
<p>Mainly pre-owned iPhone, ordered by model, capacity, colour and grade. {ph('[List the models actually available, e.g. iPhone 12 to iPhone 17]')}</p>
<p>Other Apple products (iPad, MacBook, Apple Watch, AirPods) can be quoted through the group network. {ph('[Confirm whether to offer these publicly]')}</p></div></section>
<section class="sec alt"><div class="wrap"><h2>Cosmetic grades</h2>
<div class="cards">
<article class="card"><h3>A+ Like new</h3><p>{ph('[define appearance and function]')}</p></article>
<article class="card"><h3>A Light signs of use</h3><p>{ph('[define appearance and function]')}</p></article>
<article class="card"><h3>B Visible signs of use</h3><p>{ph('[define appearance and function]')}</p></article>
<article class="card"><h3>C Heavier wear</h3><p>{ph('[define appearance and function]')}</p></article>
</div><p class="note">{ph('[Grade names and definitions are examples. Replace them with your real standard]')}</p></div></section>
<section class="sec"><div class="wrap"><h2>Inspection and assurance</h2>
<ul class="ticks"><li>Each device tested for function and appearance</li><li>Data erased and recorded</li><li>Traceable source</li><li>Warranty and after-sales: {ph('[enter warranty period and conditions if any]')}</li></ul></div></section>
<section class="cta"><div class="wrap"><h2>Need current stock and prices?</h2><p>Send the models, grades and quantities you need.</p><a class="btn light" href="contact.html">Open a trade account</a></div></section>'''),
        'sustainability': dict(title='Sustainability', desc='A circular economy: giving devices another use and reducing electronic waste.', body=f'''
<section class="page-head"><div class="wrap"><h1>Sustainability</h1><p class="lead">The most direct environmental contribution is a longer device life.</p></div></section>
<section class="sec"><div class="wrap two"><div><h2>Circular economy</h2></div><div>
<p>Electronic waste is among the fastest-growing waste streams. Putting working devices back into use after inspection reduces the resources and carbon emissions that producing new devices requires.</p>
{ph('[If you quote e-waste or carbon figures, state the authoritative source and year]')}</div></div></section>
<section class="sec alt"><div class="wrap"><h2>How we do it</h2>
<div class="cards">
<article class="card"><h3>Collect</h3><p>Gather devices that still have working life from business channels.</p></article>
<article class="card"><h3>Test</h3><p>Inspect each device, erase its data and grade it.</p></article>
<article class="card"><h3>Redistribute</h3><p>Move devices into their next life through B2B channels.</p></article>
</div></div></section>
<section class="sec"><div class="wrap two"><div><h2>The group's commitment</h2></div><div>
<p>The Sunstrike group treats sustainability as a core direction. {ph('[Certifications and carbon figures belong here only with documents, and must say whether they belong to the group or to Siersz]')}</p>
<p><a class="more" href="{GROUP_URL}" target="_blank" rel="noopener">Learn about Sunstrike →</a></p></div></div></section>'''),
        'why-us': dict(title='Why Siersz', desc='Why businesses choose Siersz for pre-owned Apple devices.', body=f'''
<section class="page-head"><div class="wrap"><h1>Why Siersz</h1><p class="lead">What business customers can expect from us.</p></div></section>
<section class="sec"><div class="wrap"><div class="cards big">
<article class="card"><h3>01 Apple focus</h3><p>We work only with pre-owned Apple devices, so our sourcing, experience and market knowledge are built around one category.</p></article>
<article class="card"><h3>02 Clear, consistent grading</h3><p>One grading standard and test records reduce disputes after delivery.</p></article>
<article class="card"><h3>03 Group-backed supply</h3><p>We source through the Sunstrike group's supply network across five continents. {ph('[Describe the specific supply channels. State only what is true]')}</p></article>
<article class="card"><h3>04 Responsive communication</h3><p>Orders, stock and delivery progress are clear and answered promptly.</p></article>
<article class="card"><h3>05 Built for the long term</h3><p>We value delivery and reputation, and aim for lasting partnerships.</p></article>
</div><p class="note">These are sample selling points. Edit or remove them to match what the company can prove.</p></div></section>'''),
        'contact': dict(title='Contact Us', desc='Get in touch with Siersz.', body=f'''
<section class="page-head"><div class="wrap"><h1>Contact Us</h1><p class="lead">Tell us what you need and the scale of your business, and we will reply as soon as we can.</p></div></section>
<section class="sec"><div class="wrap two"><div><h2>Contact details</h2></div><div>
<dl class="contact">
<dt>Email</dt><dd>{p['email']}</dd>
<dt>Phone</dt><dd>{p['phone']}</dd>
<dt>Address</dt><dd>{p['addr']}</dd>
<dt>Hours</dt><dd>{ph('[e.g. Mon–Fri 9:00–18:00 China Standard Time]')}</dd>
</dl>
<h2>Open a trade account</h2>
<p>Email us with your company name and country, the models and quantities you need, your expected monthly volume and the delivery location. Our team will get back to you shortly.</p>
<p><a class="btn" href="mailto:{C['en']['email']}?subject=Trade%20account%20enquiry">Open a trade account</a></p>
<p class="note">Before launch, replace the email in this button with the real address (edit the top of site.py and regenerate).</p></div></div></section>'''),
        'faq': dict(title='FAQ', desc='Common questions about products, grading, shipping and how to work with Siersz.', body=f'''
<section class="page-head"><div class="wrap"><h1>FAQ</h1><p class="lead">The questions we are asked most before working together.</p></div></section>
<section class="sec"><div class="wrap faqs">
<details class="faq"><summary>What do you sell?</summary><div><p>Mainly pre-owned iPhone for business customers, ordered by model, capacity, colour and grade. Other Apple products can be quoted through the group network.</p></div></details>
<details class="faq"><summary>What is the minimum order?</summary><div><p>The minimum depends on the model and the partnership model. {ph('[enter minimum order quantity]')}</p></div></details>
<details class="faq"><summary>How are devices graded?</summary><div><p>We use one consistent cosmetic grading standard. See the Products page for the grades.</p></div></details>
<details class="faq"><summary>Are devices tested and data-erased?</summary><div><p>Yes. Each device is tested for function and appearance, data-erased and recorded before shipment. {ph('[check against your real process]')}</p></div></details>
<details class="faq"><summary>Is there a warranty or returns policy?</summary><div><p>{ph('[enter warranty period, return conditions and process]')}</p></div></details>
<details class="faq"><summary>How do you ship, and on what trade terms?</summary><div><p>Shipping is arranged per order. {ph('[enter ship-from location, usual trade terms such as FOB/CIF, and lead time]')}</p></div></details>
<details class="faq"><summary>Which payment methods do you accept?</summary><div><p>{ph('[enter currencies and payment methods]')}</p></div></details>
<details class="faq"><summary>How do I open a trade account?</summary><div><p>Email us from the Contact page with your company name and country, the models and quantities you need, your expected monthly volume and the delivery location. Our team will get back to you shortly.</p></div></details>
<details class="faq"><summary>Are you an authorised Apple reseller?</summary><div><p>We are an independent supplier of pre-owned devices and are not affiliated with Apple. Apple and iPhone are trademarks of Apple Inc. {ph('[check this answer against your real authorisation status]')}</p></div></details>
<details class="faq"><summary>How is Siersz related to Sunstrike?</summary><div><p>Siersz is a sister company of the Sunstrike group. The two are separate legal entities, and Siersz draws on the group's global supply network.</p></div></details>
</div></section>
<section class="cta"><div class="wrap"><h2>Another question?</h2><p>Get in touch with us directly.</p><a class="btn light" href="contact.html">Contact us</a></div></section>'''),
        'privacy': dict(title='Privacy Policy', desc='Siersz privacy policy.', legal=True, body=f'''
<p>{p['legal']} ("we", "us") respects your privacy. This policy explains how we collect, use and protect personal information when you visit www.siersz.com or contact us.</p>
<h2>1. Information we collect</h2><ul><li>Information you give us: name, company, email, phone number and anything you include in your messages.</li><li>Information collected automatically: browser type, device information, pages visited, visit times and approximate location, through logs or cookies.</li></ul>
<h2>2. How we use it</h2><ul><li>To reply to enquiries and discuss business cooperation;</li><li>To improve site content and user experience;</li><li>To meet legal obligations.</li></ul>
<h2>3. Sharing</h2><p>We do not sell personal information. We share it only with your consent, with service providers who act on our behalf under confidentiality duties, or where the law or a competent authority requires it.</p>
<h2>4. Retention</h2><p>We keep information only as long as needed for the purposes above, unless the law requires longer. {ph('[Add specific retention periods if any]')}</p>
<h2>5. Security</h2><p>We use reasonable technical and organisational measures to protect information, but no transmission over the internet is completely secure.</p>
<h2>6. Your rights</h2><p>You may ask to access, correct or delete your personal information, or withdraw consent. Contact us using the details below.</p>
<h2>7. International transfers</h2><p>{ph('[If data is stored or processed outside your country, explain here]')}</p>
<h2>8. Children</h2><p>This site is for business users and is not directed at children.</p>
<h2>9. Changes</h2><p>We may update this policy from time to time. The latest version will be posted on this page.</p>
<h2>10. Contact</h2><p>Email: {p['email']}<br>Address: {p['addr']}</p>'''),
        'terms': dict(title='Terms of Use', desc='Siersz website terms of use.', legal=True, body=f'''
<p>Welcome to www.siersz.com (the "Site"), operated by {p['legal']} ("we", "us"). By using the Site you agree to these terms.</p>
<h2>1. Site content</h2><p>The Site gives general information about the company and its business. It is not an offer, quotation or contract. Any transaction is governed by an order or contract confirmed in writing by both parties.</p>
<h2>2. Intellectual property</h2><p>The text, images, logos and design on the Site belong to us or their owners. You may not copy, modify or use them commercially without written permission.</p>
<h2>3. Third-party trademarks</h2><p>Apple, iPhone and other names are trademarks of their respective owners. Our relationship with those owners is limited to: {ph('[state accurately, e.g. "an independent reseller of pre-owned devices, not affiliated with Apple"]')}.</p>
<p>{p['brand']} is a sister company of Sunstrike International Limited. The two are separate legal entities, and unless stated otherwise information on this Site about one does not describe the other.</p>
<h2>4. Acceptable use</h2><p>You must not use the Site for unlawful purposes, interfere with its operation, or try to gain unauthorised access to our systems.</p>
<h2>5. Disclaimer</h2><p>The Site is provided "as is". We do not guarantee that it is complete, accurate or always available. To the extent the law allows, we are not liable for indirect loss arising from use of the Site.</p>
<h2>6. External links</h2><p>The Site may link to third-party sites. We are not responsible for their content.</p>
<h2>7. Changes</h2><p>We may change these terms at any time. Continued use means you accept the changes.</p>
<h2>8. Governing law and disputes</h2><p>These terms are governed by the laws of {p['country']}. Disputes should first be resolved through friendly negotiation; if that fails, they will be submitted to {ph('[court or arbitration body]')}.</p>
<h2>9. Contact</h2><p>Email: {p['email']}</p>'''),
        'cookies': dict(title='Cookie Policy', desc='Siersz cookie policy.', legal=True, body=f'''
<p>This policy explains how www.siersz.com uses cookies and similar technologies.</p>
<h2>1. What cookies are</h2><p>Cookies are small text files that a site stores on your device to remember preferences and help us understand how the site is used.</p>
<h2>2. Types we use</h2><ul><li><b>Necessary:</b> keep the site working, for example remembering your choice on the cookie banner.</li><li><b>Analytics:</b> measure visits and page performance (only after you accept). {ph('[Delete this item if no analytics tool is used]')}</li></ul>
<h2>3. Managing cookies</h2><p>You can accept or decline non-essential cookies in the banner at the bottom of the page, or delete or block cookies in your browser settings. Blocking some cookies may affect how the site works.</p>
<h2>4. Third parties</h2><p>{ph('[If you use third-party analytics or embedded content, list the name and purpose]')}</p>
<h2>5. Contact</h2><p>Email: {p['email']}</p>'''),
    }


def _i(d):
    return ('<svg class="ico" viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + '</svg>')


ICONS = {
    'package': _i('<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/>'),
    'shield': _i('<path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5L15.5 10"/>'),
    'truck': _i('<path d="M2 6h11v10H2z"/><path d="M13 9h4l4 4v3h-8z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>'),
    'target': _i('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>'),
    'recycle': _i('<path d="M4 12a8 8 0 0 1 13.5-5.8L20 8.5"/><path d="M20 4v4.5h-4.5"/><path d="M20 12a8 8 0 0 1-13.5 5.8L4 15.5"/><path d="M4 20v-4.5h4.5"/>'),
    'handshake': _i('<path d="M2 12l4-4 4 1 3-2 4 2 5 3"/><path d="M6 8v8l4 3 3-2 4 1 4-4"/><path d="M10 14l2 2"/>'),
    'globe': _i('<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3 3 15 0 18"/><path d="M12 3c-3 3-3 15 0 18"/>'),
    'chat': _i('<path d="M4 5h16v11H9l-5 4V5z"/><path d="M8 9h8M8 12h5"/>'),
    'phone': _i('<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 19h2"/>'),
}


def _phone(x, y, rot, c1, c2, tag):
    return f'''<g transform="translate({x} {y}) rotate({rot})">
<defs><linearGradient id="g{tag}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
<rect x="-70" y="-140" width="140" height="280" rx="26" fill="#0b1220" stroke="#ffffff" stroke-opacity=".25" stroke-width="2"/>
<rect x="-61" y="-131" width="122" height="262" rx="19" fill="url(#g{tag})"/>
<rect x="-18" y="-124" width="36" height="9" rx="4.5" fill="#0b1220"/>
<rect x="-40" y="-70" width="80" height="10" rx="5" fill="#fff" fill-opacity=".75"/>
<rect x="-40" y="-50" width="52" height="7" rx="3.5" fill="#fff" fill-opacity=".45"/>
<rect x="-40" y="0" width="80" height="52" rx="10" fill="#fff" fill-opacity=".22"/>
<rect x="-40" y="64" width="80" height="34" rx="10" fill="#fff" fill-opacity=".16"/></g>'''


def _back(x, y, rot, c1, c2, tag, lens=3, s=1.0):
    """generic smartphone, seen from the back (no brand marks)"""
    cam = ''
    if lens == 3:
        pos = [(-33, -97), (-33, -65), (-7, -81)]
    elif lens == 2:
        pos = [(-33, -97), (-33, -65)]
    else:
        pos = [(-33, -97)]
    for cx, cy in pos:
        cam += f'<circle cx="{cx}" cy="{cy}" r="10" fill="#0b1220" stroke="#cbd5e1" stroke-width="2.5"/><circle cx="{cx}" cy="{cy}" r="4" fill="#334155"/><circle cx="{cx-2}" cy="{cy-2}" r="1.5" fill="#fff" fill-opacity=".7"/>'
    cam += '<circle cx="14" cy="-100" r="4" fill="#fde68a" stroke="#cbd5e1" stroke-width="1.5"/>'
    plate_h = 78 if lens >= 2 else 46
    return f'''<g transform="translate({x} {y}) rotate({rot}) scale({s})">
<defs><linearGradient id="b{tag}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
<rect x="-70" y="-140" width="140" height="280" rx="26" fill="url(#b{tag})" stroke="#0b1220" stroke-opacity=".35" stroke-width="2"/>
<rect x="-70" y="-140" width="140" height="280" rx="26" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="3"/>
<rect x="-53" y="-115" width="{82 if lens==3 else 60}" height="{plate_h+14}" rx="18" fill="#fff" fill-opacity=".22" stroke="#fff" stroke-opacity=".5" stroke-width="1.5"/>
{cam}
<rect x="-70" y="-60" width="3" height="26" rx="1.5" fill="#0b1220" fill-opacity=".35"/><rect x="67" y="-50" width="3" height="40" rx="1.5" fill="#0b1220" fill-opacity=".35"/>
<path d="M-62 120Q0 90 62 120" fill="none" stroke="#fff" stroke-opacity=".25" stroke-width="10" stroke-linecap="round"/></g>'''


ART = {
    'hero-phones': f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 440" role="img" aria-label="">
<circle cx="260" cy="220" r="190" fill="#ffffff" fill-opacity=".08"/><circle cx="260" cy="220" r="130" fill="#ffffff" fill-opacity=".07"/>
<g class="fl1">{_back(120, 245, -14, '#475569', '#0f172a', 'a', 3, .88)}</g>
<g class="fl2">{_back(405, 235, 12, '#fbcfe8', '#ec4899', 'c', 2, .88)}</g>
<g class="fl3">{_back(262, 215, 0, '#93c5fd', '#2563eb', 'b', 3, 1)}</g>
<circle cx="60" cy="70" r="7" fill="#fff" fill-opacity=".5"/><circle cx="470" cy="380" r="10" fill="#fff" fill-opacity=".35"/><circle cx="445" cy="60" r="5" fill="#fff" fill-opacity=".6"/>
</svg>''',
    'lineup': f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" role="img" aria-label="">
<ellipse cx="450" cy="318" rx="400" ry="14" fill="#14284b" fill-opacity=".12"/>
{_back(95, 170, 0, '#64748b', '#0f172a', 'l1', 1, .95)}
{_back(280, 170, 0, '#93c5fd', '#2563eb', 'l2', 2, .95)}
{_back(450, 160, 0, '#6ee7b7', '#059669', 'l3', 3, 1)}
{_back(620, 170, 0, '#fde68a', '#f59e0b', 'l4', 2, .95)}
{_back(805, 170, 0, '#fbcfe8', '#ec4899', 'l5', 1, .95)}
</svg>''',
    'globe': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" role="img" aria-label="">
<defs><linearGradient id="gg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3b82f6"/><stop offset="1" stop-color="#14284b"/></linearGradient></defs>
<circle cx="160" cy="160" r="130" fill="url(#gg)"/>
<g fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"><ellipse cx="160" cy="160" rx="130" ry="50"/><ellipse cx="160" cy="160" rx="60" ry="130"/><path d="M30 160h260M160 30v260"/></g>
<g stroke="#fde68a" stroke-width="2.5" fill="none"><path d="M95 120Q160 60 225 110"/><path d="M110 210Q170 260 235 200"/><path d="M95 120Q80 170 110 210"/></g>
<g fill="#fde68a"><circle cx="95" cy="120" r="8"/><circle cx="225" cy="110" r="8"/><circle cx="110" cy="210" r="8"/><circle cx="235" cy="200" r="8"/></g>
</svg>''',
    'boxes': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 260" role="img" aria-label="">
<g stroke="#14284b" stroke-width="2" stroke-linejoin="round">
<path d="M70 150l55-28 55 28-55 28z" fill="#93c5fd"/><path d="M70 150v50l55 28v-50z" fill="#3b82f6"/><path d="M180 150v50l-55 28v-50z" fill="#1d4ed8"/>
<path d="M150 90l55-28 55 28-55 28z" fill="#fde68a"/><path d="M150 90v50l55 28v-50z" fill="#f59e0b"/><path d="M260 90v50l-55 28v-50z" fill="#b45309"/>
<path d="M175 185l45-23 45 23-45 23z" fill="#a7f3d0"/><path d="M175 185v38l45 23v-38z" fill="#10b981"/><path d="M265 185v38l-45 23v-38z" fill="#047857"/></g>
<path d="M30 238h260" stroke="#14284b" stroke-opacity=".2" stroke-width="3" stroke-linecap="round"/>
</svg>''',
    'shield': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 300" role="img" aria-label="">
<defs><linearGradient id="gs" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#60a5fa"/><stop offset="1" stop-color="#14284b"/></linearGradient></defs>
<path d="M140 20l100 38v80c0 62-42 108-100 126C82 246 40 200 40 138V58z" fill="url(#gs)"/>
<path d="M140 44l78 30v64c0 48-31 86-78 101-47-15-78-53-78-101V74z" fill="#fff" fill-opacity=".12"/>
<path d="M92 148l33 33 63-70" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',
    'chat': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 260" role="img" aria-label="">
<rect x="20" y="30" width="190" height="110" rx="22" fill="#3b82f6"/><path d="M60 140v38l40-38z" fill="#3b82f6"/>
<rect x="110" y="110" width="190" height="100" rx="22" fill="#fde68a"/><path d="M265 210v32l-36-32z" fill="#fde68a"/>
<g fill="#fff"><rect x="48" y="62" width="120" height="10" rx="5"/><rect x="48" y="86" width="90" height="10" rx="5"/></g>
<g fill="#92400e"><rect x="138" y="140" width="120" height="10" rx="5"/><rect x="138" y="164" width="76" height="10" rx="5"/></g>
</svg>''',
}

PAGE_ART = {'about': 'globe', 'services': 'boxes', 'why-us': 'shield', 'contact': 'chat', 'products': 'boxes', 'sustainability': 'globe', 'faq': 'chat'}
ICON_SEQ = {
    'index': ['package', 'shield', 'truck'],
    'about': ['target', 'recycle', 'handshake'],
    'why-us': ['phone', 'shield', 'package', 'chat', 'handshake'],
    'services': ['package', 'shield', 'truck'],
}


def decorate(lang, key, body):
    """add icons, hero art and page-head art to a page body"""
    pre = '' if lang == 'zh' else '../'
    seq = list(ICON_SEQ.get(key, []))
    if key == 'services':
        body = re.sub(r'<div class="svc"><h2>', lambda m: '<div class="svc reveal"><span class="icobox">' + ICONS[seq.pop(0)] + '</span><h2>', body)
    else:
        body = re.sub(r'<article class="card"><h3>', lambda m: '<article class="card reveal"><span class="icobox">' + ICONS[seq.pop(0)] + '</span><h3>' if seq else m.group(0), body)
    if key == 'index':
        body = body.replace('<section class="hero"><div class="wrap">', '<section class="hero"><div class="wrap hero-grid"><div class="hero-text">', 1)
        body = body.replace('</div></section>', f'</div><img class="hero-img" src="{pre}images/photos/hero-phone.jpg" alt="" width="760" height="950"></div></section>', 1)
    if key in PAGE_ART:
        body = body.replace('<section class="page-head"><div class="wrap">', f'<section class="page-head"><div class="wrap ph-flex"><div>', 1)
        body = body.replace('</div></section>', f'</div><img class="head-img" src="{pre}images/{PAGE_ART[key]}.svg" alt="" width="220" height="190"></div></section>', 1)
    if key == 'index':
        h, t = (('产品范围', '提供多种型号、容量与颜色，具体库存请联系我们确认。') if lang == 'zh'
                else ('Device range', 'Multiple models, capacities and colours. Contact us to confirm current stock.'))
        note = ph('[在此补充主要型号和成色等级]' if lang == 'zh' else '[List your main models and grades here]')
        band = (f'<section class="sec lineup"><div class="wrap"><h2>{h}</h2><p>{t} {note}</p>'
                f'<figure class="photo wide reveal"><img src="{pre}images/photos/range.jpg" alt="" width="1400" height="788" loading="lazy"></figure></div></section>\n')
        body = body.replace('<section class="sec alt">', band + '<section class="sec alt">', 1)
    if key == 'index':
        if lang == 'zh':
            qh, qp, qs = '逐台检测，成色清晰', '每台设备出货前经过检测与分级，让买家清楚知道收到的是什么。', ['外观与屏幕检查', '电池与功能测试', '数据清除与记录', '统一的成色分级']
            qph = '[按实际流程修改以上要点]'
        else:
            qh, qp, qs = 'Every device checked, every grade clear', 'Each device is inspected and graded before it ships, so buyers know exactly what they receive.', ['Cosmetic and screen check', 'Battery and function tests', 'Data erasure and records', 'One consistent grading scale']
            qph = '[Edit these points to match your real process]'
        lis = ''.join(f'<li>{s}</li>' for s in qs)
        quality = (f'<section class="sec quality"><div class="wrap two-photo"><figure class="photo reveal"><img src="{pre}images/photos/quality.jpg" alt="" width="1000" height="667" loading="lazy"></figure>'
                   f'<div><h2>{qh}</h2><p>{qp}</p><ul class="ticks">{lis}</ul><p class="note">{ph(qph)}</p></div></div></section>\n')
        body = body.replace('<section class="cta">', quality + '<section class="cta">', 1)
    if key == 'about':
        body = body.replace('</section>', f'</section>\n<div class="wrap"><figure class="photo strip reveal"><img src="{pre}images/photos/aisle.jpg" alt="" width="1400" height="700" loading="lazy"></figure></div>', 1)
    if key == 'services':
        body = body.replace('</section>', f'</section>\n<div class="wrap"><figure class="photo strip reveal"><img src="{pre}images/photos/boxes.jpg" alt="" width="1200" height="900" loading="lazy" style="object-position:center 45%"></figure></div>', 1)
    if key == 'why-us':
        body = body.replace('</section>', f'</section>\n<div class="wrap"><figure class="photo strip reveal"><img src="{pre}images/photos/showcase.jpg" alt="" width="1400" height="788" loading="lazy" style="object-position:center 40%"></figure></div>', 1)
    body = body.replace('<div class="stats">', '<div class="stats reveal">')
    return body


EXTRA_CSS = r'''
.icobox{display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:14px;background:var(--alt);color:var(--blue);margin-bottom:12px}
.alt .icobox{background:var(--bg)}
.svc{position:relative;padding-left:76px}.svc .icobox{position:absolute;left:0;top:30px}
.card{transition:transform .25s,box-shadow .25s}.card:hover{transform:translateY(-4px);box-shadow:0 10px 28px rgba(20,40,75,.12)}
.hero-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:32px;align-items:center}
.hero-img{width:100%;height:auto;max-width:520px;justify-self:end}
.fl1{animation:fl 6s ease-in-out infinite}.fl2{animation:fl 7s ease-in-out infinite reverse}.fl3{animation:fl 5s ease-in-out infinite .5s}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.ph-flex{display:flex;align-items:center;justify-content:space-between;gap:24px}
.head-img{width:220px;height:auto;flex:none}
@media(max-width:820px){.hero-grid{grid-template-columns:1fr}.hero-img{max-width:340px;justify-self:center}.head-img{display:none}.hero{padding:56px 0}.svc{padding-left:0}.svc .icobox{position:static}}
:root{--amber:#f5a524}
.hero{background:radial-gradient(circle at 80% 40%,rgba(236,72,153,.28),transparent 45%),radial-gradient(circle at 15% 90%,rgba(245,165,36,.18),transparent 40%),linear-gradient(120deg,#0b1220,#14284b 55%,#1f4e9c);padding:110px 0 150px;clip-path:polygon(0 0,100% 0,100% 88%,0 100%)}
.hero:before{display:none}
.hero h1{font-size:clamp(2.2rem,5.4vw,3.8rem);letter-spacing:-.01em}
.hero h1:after{content:"";display:block;width:84px;height:5px;border-radius:3px;background:var(--amber);margin-top:18px}
.hero .btn{background:var(--amber);color:#1a1200;box-shadow:0 8px 24px rgba(245,165,36,.35)}
.hero .btn:hover{filter:brightness(1.07)}
.btn{transition:transform .2s,filter .2s}.btn:hover{transform:translateY(-2px)}
.cta{background:linear-gradient(rgba(11,18,32,.88),rgba(20,40,75,.9)),url(../images/photos/aisle.jpg) center/cover;padding:96px 0;clip-path:polygon(0 8%,100% 0,100% 100%,0 100%);margin-top:-30px}
.cta .btn.light{background:var(--amber);color:#1a1200}
.photo{margin:0;position:relative}
.photo img{display:block;width:100%;height:auto;border-radius:18px;box-shadow:0 18px 44px rgba(11,18,32,.25)}
.photo:before{content:"";position:absolute;inset:18px -18px -18px 18px;border:3px solid var(--amber);border-radius:18px;z-index:-1}
.hero-img{width:100%;max-width:360px;height:auto;aspect-ratio:4/5;object-fit:cover;border-radius:26px;box-shadow:0 30px 70px rgba(0,0,0,.5),0 0 0 6px rgba(255,255,255,.08);animation:fl 7s ease-in-out infinite;justify-self:center}
.photo.wide{margin:20px 18px 0 0}
.photo.strip{margin:8px 18px 48px 0}.photo.strip img{height:300px;object-fit:cover}
.two-photo{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
@media(max-width:820px){.two-photo{grid-template-columns:1fr;gap:36px}.photo:before{inset:12px -10px -12px 12px}.photo.strip img{height:200px}.hero{padding:64px 0 110px}}
.ticks{list-style:none;padding:0;margin:16px 0}.ticks li{position:relative;padding-left:32px;margin:10px 0;font-weight:500}
.ticks li:before{content:"";position:absolute;left:0;top:.35em;width:20px;height:20px;border-radius:50%;background:var(--amber) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M5 10.5l3.2 3.2L15 7' fill='none' stroke='%231a1200' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/20px no-repeat}
.stats b{background:linear-gradient(90deg,var(--blue),var(--amber));-webkit-background-clip:text;background-clip:text;color:transparent}
.stats div{border-left-color:var(--amber)}
.card{border-top:3px solid transparent}.card:hover{border-top-color:var(--amber)}
.page-head{background:linear-gradient(120deg,var(--alt),var(--bg));position:relative}
.page-head:after{content:"";position:absolute;left:0;bottom:0;width:100%;height:4px;background:linear-gradient(90deg,var(--blue),var(--amber))}
.logo-img{height:38px;width:auto;display:block;color:var(--navy)}
.logo-img.foot{height:34px;margin-bottom:10px}
.grp{font-size:.85rem;max-width:260px}.grp a{font-weight:600;color:var(--amber)}
.wrap.bar{max-width:1180px}
.steps{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:28px}
.steps li{position:relative;padding-top:8px}
.steps li b{display:flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:50%;background:var(--amber);color:#1a1200;font-size:1.1rem;margin-bottom:14px;position:relative;z-index:1}
.steps li:not(:last-child):after{content:"";position:absolute;top:30px;left:52px;right:-18px;height:2px;background:repeating-linear-gradient(90deg,var(--amber) 0 6px,transparent 6px 12px);opacity:.6}
.steps h3{margin:0 0 .3em;font-size:1.1rem}.steps p{margin:0;color:var(--mute)}
@media(max-width:820px){.steps li:not(:last-child):after{display:none}}
.faqs{max-width:820px}
.faq{border:1px solid var(--line);border-radius:12px;margin:12px 0;background:var(--bg);transition:border-color .2s}
.faq[open]{border-color:var(--amber)}
.faq summary{cursor:pointer;padding:16px 48px 16px 20px;font-weight:600;list-style:none;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";position:absolute;right:20px;top:50%;transform:translateY(-50%);font-size:1.4rem;color:var(--amber);line-height:1}
.faq[open] summary:after{content:"\2212"}
.faq div{padding:0 20px 16px;color:var(--mute)}.faq p{margin:0}
.hero-grid{grid-template-columns:1.4fr 1fr}
.net b{font-size:1.5rem;line-height:1.3}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0 32px}
@media(max-width:1080px){.menu-btn{display:block}nav{display:none;position:absolute;left:0;right:0;top:100%;background:var(--bg);border-bottom:1px solid var(--line);padding:8px 20px 16px}nav.open{display:block}nav ul{flex-direction:column;align-items:stretch}}
@media(prefers-color-scheme:dark){.logo-img:not(.foot){color:#fff}}
.lineup{text-align:center}.lineup p{color:var(--mute)}.lineup img{width:100%;height:auto;max-width:900px;margin-top:16px}
.hero{position:relative;overflow:hidden}
.hero:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 85% 20%,rgba(255,255,255,.14),transparent 45%),radial-gradient(circle at 10% 90%,rgba(251,191,36,.18),transparent 40%)}
.hero .wrap{position:relative}
.cta{background:linear-gradient(135deg,#0b1220,#1f4e9c)}
.js .reveal{opacity:0;transform:translateY(18px);transition:opacity .6s,transform .6s}
.js .reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.fl1,.fl2,.fl3{animation:none}.js .reveal{opacity:1;transform:none;transition:none}.card{transition:none}}
'''

EXTRA_JS = r'''(function(){
var els=document.querySelectorAll('.reveal');
if(!('IntersectionObserver' in window)||!els.length){return}
document.documentElement.classList.add('js');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
els.forEach(function(el){io.observe(el)});
})();'''

CSS = r'''
:root{--navy:#14284b;--blue:#1f5fbf;--ink:#1c2430;--mute:#5b6675;--line:#e3e8ef;--bg:#fff;--alt:#f5f8fc;--ph:#fff3a8}
@media(prefers-color-scheme:dark){:root{--ink:#e7ecf3;--mute:#a4b0c0;--line:#2a3547;--bg:#0f1622;--alt:#141d2c;--navy:#0b1220;--blue:#6fa3f5;--ph:#5a4d00}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.7;font-size:16px}
a{color:var(--blue)}img{max-width:100%}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;color:#000;padding:8px;z-index:99}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);z-index:20}
.bar{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:64px}
.logo{font-weight:800;letter-spacing:.14em;font-size:1.25rem;color:var(--navy);text-decoration:none}
@media(prefers-color-scheme:dark){.logo{color:#fff}}
nav ul{display:flex;gap:6px;list-style:none;margin:0;padding:0;align-items:center}
nav a{display:block;padding:8px 9px;white-space:nowrap;color:var(--ink);text-decoration:none;border-radius:6px;font-size:.95rem}
nav a:hover,nav a[aria-current=page]{background:var(--alt);color:var(--blue)}
.lang{border:1px solid var(--line);font-weight:600}
.menu-btn{display:none;background:none;border:1px solid var(--line);color:var(--ink);padding:8px 12px;border-radius:6px;font-size:.95rem}
@media(max-width:820px){.menu-btn{display:block}nav{display:none;position:absolute;left:0;right:0;top:100%;background:var(--bg);border-bottom:1px solid var(--line);padding:8px 20px 16px}nav.open{display:block}nav ul{flex-direction:column;align-items:stretch}}
.hero{background:linear-gradient(135deg,#0f2147,#1f5fbf);color:#fff;padding:96px 0}
.hero h1{font-size:clamp(2rem,5vw,3.2rem);line-height:1.2;margin:.2em 0}
.eyebrow{letter-spacing:.12em;text-transform:uppercase;font-size:.85rem;opacity:.85;margin:0}
.lead{font-size:1.15rem;opacity:.95;margin:0 0 1.6em}
.btn{display:inline-block;background:var(--blue);color:#fff;padding:12px 26px;border-radius:8px;text-decoration:none;font-weight:600}
.hero .btn,.btn.light{background:#fff;color:#14284b}
.page-head{background:var(--alt);padding:56px 0 40px;border-bottom:1px solid var(--line)}
.page-head h1{margin:0 0 .2em;font-size:2.1rem}.page-head .lead{color:var(--mute);margin:0}
.sec{padding:64px 0}.alt{background:var(--alt)}
h2{font-size:1.5rem;margin:0 0 .6em;line-height:1.3}
.two{display:grid;grid-template-columns:1fr 2fr;gap:32px}
@media(max-width:820px){.two{grid-template-columns:1fr;gap:8px}}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin:24px 0}
.card{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:24px}
.card h3{margin:0 0 .4em;font-size:1.1rem}.card p{margin:0;color:var(--mute)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;margin-top:20px}
.stats div{border-left:3px solid var(--blue);padding-left:16px}.stats b{display:block;font-size:2rem;color:var(--navy)}
@media(prefers-color-scheme:dark){.stats b{color:#fff}}
.stats span{color:var(--mute);font-size:.95rem}
.cta{background:var(--navy);color:#fff;text-align:center;padding:64px 0}.cta p{opacity:.9}
.svc{padding:28px 0;border-bottom:1px solid var(--line)}.svc:last-child{border:0}
.contact{display:grid;grid-template-columns:110px 1fr;gap:10px 16px;margin:0 0 20px}.contact dt{font-weight:600;color:var(--mute)}.contact dd{margin:0}
.more{font-weight:600;text-decoration:none}
.note{color:var(--mute);font-size:.85rem}
.ph{background:var(--ph);padding:0 4px;border-radius:3px}
.legal{max-width:780px;padding:40px 20px 72px}.legal h2{font-size:1.2rem;margin-top:1.8em}
footer{background:var(--navy);color:#c9d3e3;padding:40px 0 28px;font-size:.9rem}
footer a{color:#c9d3e3;text-decoration:none}footer a:hover{text-decoration:underline}
.fcols{display:flex;flex-wrap:wrap;gap:24px 48px;justify-content:space-between}
footer ul{list-style:none;margin:0;padding:0}footer li{margin:4px 0}
.draft{background:#fff3a8;color:#333;text-align:center;font-size:.8rem;padding:4px 10px}
#ck{position:fixed;left:12px;right:12px;bottom:12px;max-width:560px;background:var(--bg);color:var(--ink);border:1px solid var(--line);box-shadow:0 6px 24px rgba(0,0,0,.2);border-radius:10px;padding:14px 16px;z-index:50;display:none;font-size:.9rem}
#ck.show{display:block}#ck button{margin:8px 8px 0 0;padding:6px 16px;border-radius:6px;border:1px solid var(--blue);cursor:pointer;font:inherit}
#ck .y{background:var(--blue);color:#fff}#ck .n{background:none;color:var(--blue)}
'''

JS = r'''(function(){
var b=document.querySelector('.menu-btn'),n=document.getElementById('site-nav');
if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)})}
var ck=document.getElementById('ck');
function get(){try{return localStorage.getItem('siersz_cookie')}catch(e){return null}}
function set(v){try{localStorage.setItem('siersz_cookie',v)}catch(e){}}
if(ck&&!get()){ck.classList.add('show')}
if(ck){ck.addEventListener('click',function(e){var t=e.target;if(t.dataset&&t.dataset.v){set(t.dataset.v);ck.classList.remove('show')}})}
})();'''


def render(lang, key, pg):
    u = UI[lang]; other = 'en' if lang == 'zh' else 'zh'
    pre = '' if lang == 'zh' else '../'
    outfile = key + '.html'
    # path to same page in other language
    sw = ('en/' + outfile) if lang == 'zh' else ('../' + outfile)
    nav = ''.join(f'<li><a href="{k}.html"{" aria-current=\"page\"" if k == key else ""}>{t}</a></li>' for k, t in NAV[lang])
    nav += f'<li><a class="lang" href="{sw}" hreflang="{"en" if lang == "zh" else "zh-CN"}" lang="{"en" if lang == "zh" else "zh-CN"}" title="{u["toggle_title"]}">{u["toggle"]}</a></li>'
    fl = ''.join(f'<li><a href="{k}.html">{t}</a></li>' for k, t in NAV[lang] + [('faq', '常见问题' if lang == 'zh' else 'FAQ')])
    ll = ''.join(f'<li><a href="{k}.html">{t}</a></li>' for k, t in LEGAL[lang])
    brand = C[lang]['brand']
    title = f'{pg["title"]} | {brand}' if key != 'index' else f'{brand} | {pg["title"]}'
    if pg.get('legal'):
        body = f'<main id="main"><section class="page-head"><div class="wrap"><h1>{pg["title"]}</h1><p class="note">{u["updated"]}{UPDATED}</p></div></section><div class="wrap legal">{pg["body"]}</div></main>'
    else:
        body = f'<main id="main">{decorate(lang, key, pg["body"])}</main>'
    zh_url = f'{DOMAIN}/{outfile}'; en_url = f'{DOMAIN}/en/{outfile}'
    self_url = zh_url if lang == 'zh' else en_url
    ck_link = f'<a href="cookies.html">{LEGAL[lang][2][1]}</a>'
    ck_end = '。' if lang == 'zh' else '.'
    return f'''<!doctype html>
<html lang="{u["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{pg["desc"]}">
<link rel="canonical" href="{self_url}">
<link rel="alternate" hreflang="zh-CN" href="{zh_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{zh_url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{pg["desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{self_url}">
<link rel="icon" href="{pre}images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{pre}css/style.css">
</head>
<body>
<a class="skip" href="#main">{u["skip"]}</a>
<div class="draft">{u["draft"]}</div>
<header><div class="wrap bar">
<a class="logo" href="index.html" aria-label="{brand}">{logo_svg("logo-img")}</a>
<button class="menu-btn" aria-expanded="false" aria-controls="site-nav">{u["menu"]}</button>
<nav id="site-nav" aria-label="main"><ul>{nav}</ul></nav>
</div></header>
{body}
<footer><div class="wrap"><div class="fcols">
<div>{logo_svg("logo-img foot", top="#ffffff", word="#ffffff")}<p>{C[lang]["legal"]}</p><p class="grp">{u["group"]}<br><a href="{GROUP_URL}" target="_blank" rel="noopener">{u["group_link"]} →</a></p></div>
<ul>{fl}</ul><ul>{ll}</ul></div>
<p style="margin-top:28px">&copy; 2026 {brand}. {u["rights"]}</p></div></footer>
<div id="ck" role="dialog" aria-label="cookies"><span>{u["ck_text"]} {ck_link}{ck_end}</span><br><button class="y" data-v="yes">{u["ck_ok"]}</button><button class="n" data-v="no">{u["ck_no"]}</button></div>
<script src="{pre}js/main.js"></script>
</body>
</html>
'''


def main():
    for d in ('css', 'js', 'images', 'en'):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
    for lang in ('zh', 'en'):
        base = OUT if lang == 'zh' else os.path.join(OUT, 'en')
        for key, pg in pages(lang).items():
            with open(os.path.join(base, key + '.html'), 'w', encoding='utf-8') as f:
                f.write(render(lang, key, pg))
    open(os.path.join(OUT, 'css/style.css'), 'w', encoding='utf-8').write(CSS.strip() + '\n' + EXTRA_CSS.strip() + '\n')
    open(os.path.join(OUT, 'js/main.js'), 'w', encoding='utf-8').write(JS + '\n' + EXTRA_JS + '\n')
    for name, svg in ART.items():
        open(os.path.join(OUT, 'images', name + '.svg'), 'w', encoding='utf-8').write(svg + '\n')
    L = os.path.join(OUT, 'images')
    def wr(name, svg):
        open(os.path.join(L, name), 'w', encoding='utf-8').write(svg + chr(10))
    wr('favicon.svg', logo_svg(top='#ffffff', mark_only=True, tile=NAVY))
    wr('logo-mark.svg', logo_svg(top=NAVY, mark_only=True))
    wr('logo-app-icon.svg', logo_svg(top='#ffffff', mark_only=True, tile=NAVY))
    wr('logo.svg', logo_svg(top=NAVY, word=NAVY))
    wr('logo-white.svg', logo_svg(top='#ffffff', word='#ffffff'))
    keys = list(pages('zh'))
    urls = ''.join(f'<url><loc>{DOMAIN}/{k}.html</loc><xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/en/{k}.html"/></url>\n<url><loc>{DOMAIN}/en/{k}.html</loc><xhtml:link rel="alternate" hreflang="zh-CN" href="{DOMAIN}/{k}.html"/></url>\n' for k in keys)
    open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + '</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    open(os.path.join(OUT, 'README.txt'), 'w', encoding='utf-8').write(
        'Siersz website (static)\n\n'
        'Chinese (main) pages are in this folder; English pages are in en/.\n'
        'Every [bracketed] item shown with a yellow background is a placeholder.\n'
        'Edit the settings at the top of site.py (company name, email, phone, address) and re-run: python site.py\n'
        'Open index.html in a browser to preview. To publish, upload the whole folder to the web host for siersz.com.\n'
        'The yellow "placeholder" bar at the top of each page is controlled by the "draft" text in site.py; remove it before launch.\n'
        'Legal pages are drafts: have them reviewed by a lawyer before launch.\n'
        'Photos in images/photos come from Unsplash (free licence, see unsplash.com/license). Replace them with your own photos when you have them.\n'
        'The iPhone photos show real Apple devices and logos (stock photos). State in the Terms of Use that you are an independent reseller with no Apple affiliation, and replace them with photos of your own stock when available.\n')
    shutil.copy(os.path.abspath(__file__), os.path.join(OUT, 'site.py'))
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo.py'), os.path.join(OUT, 'logo.py'))
    print('built', OUT)


main()
