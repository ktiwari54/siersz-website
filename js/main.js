(function(){
var b=document.querySelector('.menu-btn'),n=document.getElementById('site-nav');
if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)})}
var ck=document.getElementById('ck');
function get(){try{return localStorage.getItem('siersz_cookie')}catch(e){return null}}
function set(v){try{localStorage.setItem('siersz_cookie',v)}catch(e){}}
if(ck&&!get()){ck.classList.add('show')}
if(ck){ck.addEventListener('click',function(e){var t=e.target;if(t.dataset&&t.dataset.v){set(t.dataset.v);ck.classList.remove('show')}})}
})();
(function(){
var els=document.querySelectorAll('.reveal');
if(!('IntersectionObserver' in window)||!els.length){return}
document.documentElement.classList.add('js');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
els.forEach(function(el){io.observe(el)});
})();
