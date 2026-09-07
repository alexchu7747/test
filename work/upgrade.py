from pathlib import Path
p=Path('/Users/chu/Documents/Codex/2026-05-30/new-chat/outputs/portuguese-study-tool/public/index.html')
s=p.read_text()
def replace(a,b):
    global s
    assert a in s, a[:100]
    s=s.replace(a,b)
replace('</head>', '  <meta name="description" content="葡语精听、沉浸精读与间隔复习。保存真实语料，逐句掌握葡萄牙语。">\n  <link rel="stylesheet" href="workbench.css">\n</head>')
replace('<div class="brand"><div class="mark">PT</div><span>葡语学习台</span></div>', '<div class="brand"><div class="mark">pt.</div><span>葡语学习台<small>MEU PORTUGUÊS</small></span></div>')
replace('<nav>', '<nav aria-label="主要导航">')
replace('<button data-view="settings"', '<button data-view="review" title="复习"><span class="nav-icon">↻</span><span class="nav-label">复习</span><span id="reviewBadge" class="nav-badge">0</span></button>\n        <button data-view="settings"')
replace('<strong>默认不花钱</strong><br>\n        YouTube / Spotify、字幕导入、清洗、隐藏、基础语料都在浏览器里完成。AI 功能只在你手动点击时调用.', '<strong>每天一点，慢慢听懂。</strong><br>\n        从真实语料出发，把不熟悉的表达变成自己的葡语。') if False else None
replace('<strong>默认不花钱</strong><br>\n        YouTube / Spotify、字幕导入、清洗、隐藏、基础语料都在浏览器里完成。AI 功能只在你手动点击时调用。', '<strong>每天一点，慢慢听懂。</strong><br>从真实语料出发，把不熟悉的表达变成自己的葡语。<br><span class="local-indicator">● 学习记录保存在此设备</span>')
replace('<h1 id="viewTitle">视频精听</h1>', '<div><div class="eyebrow">你的葡语练习室</div><h1 id="viewTitle">视频精听</h1></div>')
replace('<button id="clearBtn" class="danger">清空</button>', '<button id="restoreBtn">恢复备份</button><input id="restoreFile" type="file" accept=".json,application/json" class="hidden">')
replace('      <section id="listen"', '      <div id="studyRibbon" class="study-ribbon"><div><span class="status-dot"></span><strong id="sessionSummary">准备好开始今天的练习了吗？</strong><span id="sessionHint">导入一段语料，听懂一句，再学下一句。</span></div><button id="quickReviewBtn">今日复习 <b id="dueCount">0</b> →</button></div>\n      <section id="listen"')
replace('<div class="subtitle-list" id="sentenceList"></div>', '<div class="listen-progress"><span id="listenProgressText">尚未开始</span><progress id="listenProgress" value="0" max="1" aria-label="精听完成进度"></progress></div><div class="subtitle-list" id="sentenceList"></div>')
replace('<div class="reader-grid reader-setup" id="readerSetup">', '<div class="article-shelf"><div class="shelf-heading"><div><h2>我的阅读</h2><span class="small">接着读，或开始一篇新文章</span></div><button id="newArticleBtn">＋ 新文章</button></div><div id="articleShelf" class="shelf-items"></div></div>\n        <div class="reader-grid reader-setup" id="readerSetup">')
replace('      <section id="settings"', '''      <section id="review" class="view">
        <div class="review-layout"><div class="review-intro"><div class="eyebrow">RELEMBRAR</div><h2>把收藏，变成掌握。</h2><p>先回忆意思，再翻开答案。根据熟悉程度，安排下一次复习。</p><div id="reviewStats" class="review-stats"></div><p class="small">新语料与到期语料会自动进入今日复习。<br>空格翻面 · 1 再练 · 2 模糊 · 3 记住</p></div><div id="reviewWorkspace" aria-live="polite"></div></div>
      </section>
      <section id="settings"''')
replace('<button id="resetUsageBtn">重置本月估算</button>', '<button id="resetUsageBtn">重置本月估算</button><div class="data-management"><h3>学习数据</h3><p class="small">导出的备份包含学习内容和进度，不包含 API 密钥。恢复时会合并内容，并保留当前设备设置。</p><button id="clearBtn" class="danger">清空此设备的学习数据</button></div>')
replace('<div id="toast" class="toast"></div>', '<div id="toast" class="toast" role="status" aria-live="polite"></div>\n  <dialog id="contextDialog"><div class="shelf-heading"><h2>语料上下文</h2><button id="closeContextBtn" aria-label="关闭">×</button></div><div id="contextBody"></div></dialog>')
replace('        subtitles: [],', '        reader: { title: "", source: "", text: "", segments: [], activeIndex: 0, stage: "skim" },\n        activity: {},\n        subtitles: [],')
replace('      Object.keys(patch || {}).forEach((key) => {', '      Object.keys(patch || {}).forEach((key) => {\n        if (["__proto__", "constructor", "prototype"].includes(key)) return;')
replace('      localStorage.setItem(storeKey, JSON.stringify(state));', '      try { localStorage.setItem(storeKey, JSON.stringify(state)); }\n      catch { showToast("保存失败：设备存储空间不足，请先导出备份。"); }')
replace('          done: readSegments[index]?.done || false,\n          hard: readSegments[index]?.hard || false,\n          note: readSegments[index]?.note || ""', '          done: readSegments[index]?.text === text ? readSegments[index].done : false,\n          hard: readSegments[index]?.text === text ? readSegments[index].hard : false,\n          note: readSegments[index]?.text === text ? readSegments[index].note : ""')
replace('      activeReadIndex = 0;\n      renderArticle();', '      activeReadIndex = Math.min(activeReadIndex, Math.max(0, readSegments.length - 1));\n      renderArticle();')
replace('      if (["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) return;', '      if (["INPUT", "TEXTAREA", "SELECT", "BUTTON"].includes(document.activeElement.tagName) || document.activeElement.isContentEditable || event.ctrlKey || event.metaKey || event.altKey) return;\n      if (!$("listen").classList.contains("active") && !readImmersive) return;')
replace('corpus: "基础语料库", settings: "设置"', 'corpus: "我的语料", review: "间隔复习", settings: "偏好与数据"')
replace('这里先保持基础版。精听或精读时保存的词、短语、句子会出现在这里。', '还没有匹配的语料。精听或精读时点击保存，把值得记住的表达收集到这里。')
replace('      if (!term) return;\n      state.corpus.unshift({', '      if (!term) return;\n      if (state.corpus.some(existing => existing.term.toLocaleLowerCase("pt") === term.toLocaleLowerCase("pt") && existing.context === String(item.context || "").trim())) return showToast("这条语料已收藏，可到复习页练习。");\n      state.corpus.unshift({')
replace('      if (contextId) {\n        const item = state.corpus.find((x) => x.id === contextId);\n        if (item?.time != null) seekTo(item.time, true);\n      }', '      if (contextId) showCorpusContext(contextId);')
start=s.index('      const text = $("articleInput").value.trim();', s.index('$("saveArticleBtn").addEventListener'))
end=s.index('\n    });',start)
s=s[:start]+'      saveCurrentArticle();'+s[end:]
replace('      $("youtubeUrl").value = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";', '      if ((state.subtitles.length || $("articleInput").value.trim()) && !confirm("载入示例会替换当前字幕和阅读草稿。已收藏的语料和已保存的文章会保留，是否继续？")) return;\n      $("youtubeUrl").value = "";')
replace('      state.video.title = "YouTube 视频";\n      saveState();\n      showToast("示例已载入");', '      state.video = { title: "字幕练习示例（无配套音频）", url: "", youtubeId: "" };\n      if (player?.stopVideo) player.stopVideo();\n      saveState();\n      showToast("示例已载入：可体验查词和阅读，字幕无配套音频。");')
replace('      const blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });', '      persistReader();\n      const backup = JSON.parse(JSON.stringify(state));\n      delete backup.settings.openaiKey;\n      delete backup.settings.elevenLabsApiKey;\n      const blob = new Blob([JSON.stringify(backup, null, 2)], { type: "application/json" });')
replace('    renderArticle();\n    renderAll();\n  </script>', '    renderArticle();\n    renderAll();\n  </script>\n  <script src="workbench.js"></script>')
p.write_text(s)
