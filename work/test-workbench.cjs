const fs=require('fs');const vm=require('vm');const assert=require('node:assert/strict');
const {parseHTML}=require('./test-tools/node_modules/linkedom');
const root='/Users/chu/Documents/Codex/2026-05-30/new-chat/outputs/portuguese-study-tool';
const html=fs.readFileSync(root+'/public/index.html','utf8');
const inline=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const addon=fs.readFileSync(root+'/public/workbench.js','utf8');
function app(seed){
 const {window}=parseHTML(html),{document}=window;let persisted=seed||null;
 // DOM-only integration harness; no browser, media, network, or live services.
 Object.defineProperty(window.HTMLSelectElement.prototype,'value',{configurable:true,get(){return this._value??this.querySelector('option')?.getAttribute('value')??''},set(v){this._value=String(v)}});
 document.querySelectorAll('input,textarea').forEach(el=>{if(el.value==null)el.value=''});
 document.querySelectorAll('audio').forEach(el=>{el.pause=()=>{};el.play=()=>Promise.resolve();el.load=()=>{}});
 document.querySelectorAll('*').forEach(el=>{el.scrollIntoView=()=>{};el.focus=()=>{}});
 document.getElementById('contextDialog').showModal=()=>{};document.getElementById('contextDialog').close=()=>{};
 const context={document,console,URL,Blob,Date,Math,JSON,Set,Map,Uint16Array,Number,String,Array,Object,RegExp,Error,SyntaxError,Promise,
 localStorage:{getItem:()=>persisted,setItem:(k,v)=>{persisted=v},removeItem:()=>{persisted=null}},
 navigator:{},location:{reload:()=>{}},confirm:()=>true,
 setTimeout:()=>0,clearTimeout:()=>{},setInterval:()=>0,requestAnimationFrame:()=>{},fetch:()=>Promise.reject(new Error('Network disabled in tests')),
 addEventListener:()=>{},getSelection:()=>({toString:()=>''})};
 context.window=context;const ctx=vm.createContext(context);
 vm.runInContext(inline,ctx,{filename:'index-inline.js'});vm.runInContext(addon,ctx,{filename:'workbench.js'});
 return {ctx,document,run:code=>vm.runInContext(code,ctx),saved:()=>persisted};
}
const a=app();
assert.equal(a.document.querySelectorAll('nav button').length,5);
assert.equal(a.run('state.corpus.length'),0);
assert.match(a.document.getElementById('reviewWorkspace').textContent,/第一条语料/);
assert.equal(a.run('compareDictation("Olá, tudo bem?", "olá tudo bem").score'),100);
assert.equal(a.run('compareDictation("Eu gosto muito de café", "Eu gosto de café").score'),89);
assert(a.run('compareDictation("avó", "avo").score')<100);
assert.equal(a.run('scheduleReview(null,"again",100).due'),600100);
assert.equal(a.run('scheduleReview(null,"good",0).interval'),3);
assert.equal(a.run('scheduleReview({interval:3},"good",0).interval'),7);
assert.throws(()=>a.run('validateStudyBackup({corpus:[{id:"bad\\\"",term:"x"}],articles:[],subtitles:[]})'));
a.run('addCorpus({term:"bom dia",meaning:"早上好"});addCorpus({term:"bom dia",meaning:"早上好"})');
assert.equal(a.run('state.corpus.length'),1,'duplicate collection prevented');
a.document.querySelector('[data-view="review"]').click();
assert.match(a.document.getElementById('reviewWorkspace').textContent,/bom dia/);
assert(!a.document.getElementById('reviewWorkspace').textContent.includes('早上好'));
a.document.querySelector('[data-review-action="reveal"]').click();
assert.match(a.document.getElementById('reviewWorkspace').textContent,/早上好/);
a.document.querySelector('[data-grade="good"]').click();
assert.equal(a.run('state.corpus[0].review.interval'),3);
assert.match(a.document.getElementById('reviewWorkspace').textContent,/完成了/);
a.run('$("articleTitle").value="Teste";$("articleInput").value="Primeiro parágrafo.\\n\\nSegundo parágrafo.";renderArticle();startReadSession();updateActiveReadSegment({note:"记住搭配",done:true});saveCurrentArticle();');
assert.equal(a.run('state.articles.length'),1);
a.run('saveCurrentArticle()');assert.equal(a.run('state.articles.length'),1,'update saved article rather than duplicate');
const b=app(a.saved());
assert.equal(b.run('readSegments[0].note'),'记住搭配','notes survive reload');
assert.equal(b.run('readSegments[0].done'),true);
assert.equal(b.document.getElementById('articleTitle').value,'Teste');
b.run('setReadStage("recall")');
assert(b.document.getElementById('articleView').classList.contains('hidden'));
assert(!b.document.getElementById('activeReadUnit').textContent.includes('Primeiro parágrafo.'));
b.document.getElementById('revealRecallBtn').click();
assert(b.document.getElementById('activeReadUnit').textContent.includes('Primeiro'));
b.run('readSegments[0].recall="Eu lembro";renderArticle();persistReader()');
assert.equal(b.run('state.reader.segments[0].recall'),'Eu lembro','recall draft preserved');
b.run('$("articleInput").value="Conteúdo diferente.";renderArticle()');
assert.equal(b.run('readSegments[0].note'),'','new paragraph does not inherit old notes');
assert.equal(b.run('readSegments[0].done'),false);
b.document.querySelector('[data-view="corpus"]').click();b.document.querySelector('[data-load-context]').click();
assert.match(b.document.getElementById('contextBody').textContent,/bom dia/);
const ids=[...b.document.querySelectorAll('[id]')].map(x=>x.id);assert.equal(new Set(ids).size,ids.length,'unique element IDs');
console.log('PASS: boot, navigation, review grading and reveal, dictation alignment, duplicate prevention, article upsert, note/recall persistence, paragraph reset, context, backup validation, unique IDs.');
