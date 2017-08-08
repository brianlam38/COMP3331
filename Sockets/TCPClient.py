
<!doctype html>
<html prefix="og: http://ogp.me/ns#">
<head>
    <meta charset="UTF-8"><script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={xpid:"XA8AWVNaGwICXFVVAgkA"};window.NREUM||(NREUM={}),__nr_require=function(t,n,e){function r(e){if(!n[e]){var o=n[e]={exports:{}};t[e][0].call(o.exports,function(n){var o=t[e][1][n];return r(o||n)},o,o.exports)}return n[e].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<e.length;o++)r(e[o]);return r}({1:[function(t,n,e){function r(t){try{s.console&&console.log(t)}catch(n){}}var o,i=t("ee"),a=t(15),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,n,e){r(e.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,n){return t}).join(", ")))},{}],2:[function(t,n,e){function r(t,n,e,r,o){try{d?d-=1:i("err",[o||new UncaughtException(t,n,e)])}catch(s){try{i("ierr",[s,c.now(),!0])}catch(u){}}return"function"==typeof f&&f.apply(this,a(arguments))}function UncaughtException(t,n,e){this.message=t||"Uncaught error with no additional information",this.sourceURL=n,this.line=e}function o(t){i("err",[t,c.now()])}var i=t("handle"),a=t(16),s=t("ee"),c=t("loader"),f=window.onerror,u=!1,d=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(l){"stack"in l&&(t(8),t(7),"addEventListener"in window&&t(5),c.xhrWrappable&&t(9),u=!0)}s.on("fn-start",function(t,n,e){u&&(d+=1)}),s.on("fn-err",function(t,n,e){u&&(this.thrown=!0,o(e))}),s.on("fn-end",function(){u&&!this.thrown&&d>0&&(d-=1)}),s.on("internal-error",function(t){i("ierr",[t,c.now(),!0])})},{}],3:[function(t,n,e){t("loader").features.ins=!0},{}],4:[function(t,n,e){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(8),s=t(7),c="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",l="resource",p="-start",h="-end",m="fn"+p,w="fn"+h,v="bstTimer",y="pushState",g=t("loader");g.features.stn=!0,t(6);var b=NREUM.o.EV;o.on(m,function(t,n){var e=t[0];e instanceof b&&(this.bstStart=g.now())}),o.on(w,function(t,n){var e=t[0];e instanceof b&&i("bst",[e,n,this.bstStart,g.now()])}),a.on(m,function(t,n,e){this.bstStart=g.now(),this.bstType=e}),a.on(w,function(t,n){i(v,[n,this.bstStart,g.now(),this.bstType])}),s.on(m,function(){this.bstStart=g.now()}),s.on(w,function(t,n){i(v,[n,this.bstStart,g.now(),"requestAnimationFrame"])}),o.on(y+p,function(t){this.time=g.now(),this.startPath=location.pathname+location.hash}),o.on(y+h,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+c]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["c"+c]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["webkitC"+c]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],5:[function(t,n,e){function r(t){for(var n=t;n&&!n.hasOwnProperty(u);)n=Object.getPrototypeOf(n);n&&o(n)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,n){return t[1]}var a=t("ee").get("events"),s=t(18)(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";n.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,n){var e=t[1],r=c(e,"nr@wrapped",function(){function t(){if("function"==typeof e.handleEvent)return e.handleEvent.apply(e,arguments)}var n={object:t,"function":e}[typeof e];return n?s(n,"fn-",null,n.name||"anonymous"):e});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],6:[function(t,n,e){var r=t("ee").get("history"),o=t(18)(r);n.exports=r,o.inPlace(window.history,["pushState","replaceState"],"-")},{}],7:[function(t,n,e){var r=t("ee").get("raf"),o=t(18)(r),i="equestAnimationFrame";n.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],8:[function(t,n,e){function r(t,n,e){t[0]=a(t[0],"fn-",null,e)}function o(t,n,e){this.method=e,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,e)}var i=t("ee").get("timer"),a=t(18)(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";n.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],9:[function(t,n,e){function r(t,n){d.inPlace(n,["onreadystatechange"],"fn-",s)}function o(){var t=this,n=u.context(t);t.readyState>3&&!n.resolved&&(n.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,y,"fn-",s)}function i(t){g.push(t),h&&(x?x.then(a):w?w(a):(E=-E,O.data=E))}function a(){for(var t=0;t<g.length;t++)r([],g[t]);g.length&&(g=[])}function s(t,n){return n}function c(t,n){for(var e in t)n[e]=t[e];return n}t(5);var f=t("ee"),u=f.get("xhr"),d=t(18)(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,w=l.SI,v="readystatechange",y=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],g=[];n.exports=u;var b=window.XMLHttpRequest=function(t){var n=new p(t);try{u.emit("new-xhr",[n],n),n.addEventListener(v,o,!1)}catch(e){try{u.emit("internal-error",[e])}catch(r){}}return n};if(c(p,b),b.prototype=p.prototype,d.inPlace(b.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,n){r(t,n),i(n)}),u.on("open-xhr-start",r),h){var x=m&&m.resolve();if(!w&&!m){var E=1,O=document.createTextNode(E);new h(a).observe(O,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===v||a()})},{}],10:[function(t,n,e){function r(t){var n=this.params,e=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!n.aborted){if(e.duration=a.now()-this.startTime,4===t.readyState){n.status=t.status;var i=o(t,this.lastSize);if(i&&(e.rxSize=i),this.sameOrigin){var c=t.getResponseHeader("X-NewRelic-App-Data");c&&(n.cat=c.split(", ").pop())}}else n.status=0;e.cbTime=this.cbTime,f.emit("xhr-done",[t],t),s("xhr",[n,e,this.startTime])}}}function o(t,n){var e=t.responseType;if("json"===e&&null!==n)return n;var r="arraybuffer"===e||"blob"===e||"json"===e?t.response:t.responseText;return h(r)}function i(t,n){var e=c(n),r=t.params;r.host=e.hostname+":"+e.port,r.pathname=e.pathname,t.sameOrigin=e.sameOrigin}var a=t("loader");if(a.xhrWrappable){var s=t("handle"),c=t(11),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,l=t("id"),p=t(14),h=t(13),m=window.XMLHttpRequest;a.features.xhr=!0,t(9),f.on("new-xhr",function(t){var n=this;n.totalCbs=0,n.called=0,n.cbTime=0,n.end=r,n.ended=!1,n.xhrGuids={},n.lastSize=null,p&&(p>34||p<10)||window.opera||t.addEventListener("progress",function(t){n.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,n){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&n.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,n){var e=this.metrics,r=t[0],o=this;if(e&&r){var i=h(r);i&&(e.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof n.onload))&&o.end(n)}catch(e){try{f.emit("internal-error",[e])}catch(r){}}};for(var s=0;s<d;s++)n.addEventListener(u[s],this.listener,!1)}),f.on("xhr-cb-time",function(t,n,e){this.cbTime+=t,n?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof e.onload||this.end(e)}),f.on("xhr-load-added",function(t,n){var e=""+l(t)+!!n;this.xhrGuids&&!this.xhrGuids[e]&&(this.xhrGuids[e]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,n){var e=""+l(t)+!!n;this.xhrGuids&&this.xhrGuids[e]&&(delete this.xhrGuids[e],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,n){n instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],n)}),f.on("removeEventListener-end",function(t,n){n instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],n)}),f.on("fn-start",function(t,n,e){n instanceof m&&("onload"===e&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),f.on("fn-end",function(t,n){this.xhrCbStart&&f.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,n],n)})}},{}],11:[function(t,n,e){n.exports=function(t){var n=document.createElement("a"),e=window.location,r={};n.href=t,r.port=n.port;var o=n.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=n.hostname||e.hostname,r.pathname=n.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!n.protocol||":"===n.protocol||n.protocol===e.protocol,a=n.hostname===document.domain&&n.port===e.port;return r.sameOrigin=i&&(!n.hostname||a),r}},{}],12:[function(t,n,e){function r(){}function o(t,n,e){return function(){return i(t,[f.now()].concat(s(arguments)),n?null:this,e),n?void 0:this}}var i=t("handle"),a=t(15),s=t(16),c=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,n){u[n]=o(l+n,!0,"api")}),u.addPageAction=o(l+"addPageAction",!0),u.setCurrentRouteName=o(l+"routeName",!0),n.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,n){var e={},r=this,o="function"==typeof n;return i(p+"tracer",[f.now(),t,e],r),function(){if(c.emit((o?"":"no-")+"fn-start",[f.now(),r,o],e),o)try{return n.apply(this,arguments)}finally{c.emit("fn-end",[f.now()],e)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,n){h[n]=o(p+n)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now()])}},{}],13:[function(t,n,e){n.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(n){return}}}},{}],14:[function(t,n,e){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),n.exports=r},{}],15:[function(t,n,e){function r(t,n){var e=[],r="",i=0;for(r in t)o.call(t,r)&&(e[i]=n(r,t[r]),i+=1);return e}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],16:[function(t,n,e){function r(t,n,e){n||(n=0),"undefined"==typeof e&&(e=t?t.length:0);for(var r=-1,o=e-n||0,i=Array(o<0?0:o);++r<o;)i[r]=t[n+r];return i}n.exports=r},{}],17:[function(t,n,e){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],18:[function(t,n,e){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(16),a="nr@original",s=Object.prototype.hasOwnProperty,c=!1;n.exports=function(t,n){function e(t,n,e,o){function nrWrapper(){var r,a,s,c;try{a=this,r=i(arguments),s="function"==typeof e?e(r,a):e||{}}catch(f){l([f,"",[r,a,o],s])}u(n+"start",[r,a,o],s);try{return c=t.apply(a,r)}catch(d){throw u(n+"err",[r,a,d],s),d}finally{u(n+"end",[r,a,c],s)}}return r(t)?t:(n||(n=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,n,o,i){o||(o="");var a,s,c,f="-"===o.charAt(0);for(c=0;c<n.length;c++)s=n[c],a=t[s],r(a)||(t[s]=e(a,f?s+o:o,i,s))}function u(e,r,o){if(!c||n){var i=c;c=!0;try{t.emit(e,r,o,n)}catch(a){l([a,e,r,o])}c=i}}function d(t,n){if(Object.defineProperty&&Object.keys)try{var e=Object.keys(t);return e.forEach(function(e){Object.defineProperty(n,e,{get:function(){return t[e]},set:function(n){return t[e]=n,n}})}),n}catch(r){l([r])}for(var o in t)s.call(t,o)&&(n[o]=t[o]);return n}function l(n){try{t.emit("internal-error",n)}catch(e){}}return t||(t=o),e.inPlace=f,e.flag=a,e}},{}],ee:[function(t,n,e){function r(){}function o(t){function n(t){return t&&t instanceof r?t:t?c(t,s,i):i()}function e(e,r,o,i){if(!l.aborted||i){t&&t(e,r,o);for(var a=n(o),s=h(e),c=s.length,f=0;f<c;f++)s[f].apply(a,r);var d=u[y[e]];return d&&d.push([g,e,r,a]),a}}function p(t,n){v[t]=h(t).concat(n)}function h(t){return v[t]||[]}function m(t){return d[t]=d[t]||o(e)}function w(t,n){f(t,function(t,e){n=n||"feature",y[e]=n,n in u||(u[n]=[])})}var v={},y={},g={on:p,emit:e,get:m,listeners:h,context:n,buffer:w,abort:a,aborted:!1};return g}function i(){return new r}function a(){(u.api||u.feature)&&(l.aborted=!0,u=l.backlog={})}var s="nr@context",c=t("gos"),f=t(15),u={},d={},l=n.exports=o();l.backlog=u},{}],gos:[function(t,n,e){function r(t,n,e){if(o.call(t,n))return t[n];var r=e();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(t,n,e){function r(t,n,e,r){o.buffer([t],r),o.emit(t,n,e)}var o=t("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(t,n,e){function r(t){var n=typeof t;return!t||"object"!==n&&"function"!==n?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");n.exports=r},{}],loader:[function(t,n,e){function r(){if(!x++){var t=b.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&n))return u.abort();f(y,function(n,e){t[n]||(t[n]=e)}),c("mark",["onload",a()+b.offset],null,"api");var e=l.createElement("script");e.src="https://"+t.agent,n.parentNode.insertBefore(e,n)}}function o(){"complete"===l.readyState&&i()}function i(){c("mark",["domContent",a()+b.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(s=Math.max((new Date).getTime(),s))-b.offset}var s=(new Date).getTime(),c=t("handle"),f=t(15),u=t("ee"),d=window,l=d.document,p="addEventListener",h="attachEvent",m=d.XMLHttpRequest,w=m&&m.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:m,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var v=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1044.min.js"},g=m&&w&&w[p]&&!/CriOS/.test(navigator.userAgent),b=n.exports={offset:s,now:a,origin:v,features:{},xhrWrappable:g};t(12),l[p]?(l[p]("DOMContentLoaded",i,!1),d[p]("load",r,!1)):(l[h]("onreadystatechange",o),d[h]("onload",r)),c("mark",["firstbyte",s],null,"api");var x=0,E=t(17)},{}]},{},["loader",2,10,4,3]);</script><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","queueTime":0,"licenseKey":"ea97b07fc4","agent":"","transactionName":"YgdQZ0YEDBdSBxVQWFtNYlJTADIWVhcEV0NQEB1DVQIHO0UNBE4NVAFGWlsLWBJaARY=","applicationID":"12847587","errorBeacon":"bam.nr-data.net","applicationTime":673}</script>
    <script type="text/javascript">
      !function(){var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","page","once","off","on"];analytics.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);analytics.push(e);return analytics}};for(var t=0;t<analytics.methods.length;t++){var e=analytics.methods[t];analytics[e]=analytics.factory(e)}analytics.load=function(t){var e=document.createElement("script");e.type="text/javascript";e.async=!0;e.src=("https:"===document.location.protocol?"https://":"http://")+"cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)};analytics.SNIPPET_VERSION="3.1.0";
      analytics.load("gZUJfCaNLAI624oQBIqhDeM4i96M6Bbx");
      analytics.page()
      }}();
    </script>
    <script type="text/x-mathjax-config">
      MathJax.Hub.Config({
        showProcessingMessages: false,
        tex2jax: { inlineMath: [['$','$'],['\\(','\\)']] }
      });
    </script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML,Safe"></script>
    <script type="text/javascript">
        window.loadTimestamp = Date.now();
        window.addEventListener("load", function() {
            window.loadEndTimestamp = Date.now();
        }, false);
    </script>
    
        <link rel="icon" type="image/png" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon.png?v=2">
    

    <meta name="author" content="Open Learning Global Pty Ltd.">
    <meta name="apple-itunes-app" content="app-id=981790180">
    <meta name="google-play-app" content="app-id=openlearning.com.openlearning">

    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="viewport" content="minimal-ui, width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    
        
            <!-- ****** faviconit.com favicons ****** -->
            <link rel="shortcut icon" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/favicon.png?v=2">
            <link rel="icon" sizes="16x16 32x32 96x96" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/favicon.png?v=2">

            <link rel="icon" type="image/png" sizes="36x36" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/android-icon-36x36.png?v=2">
            <link rel="icon" type="image/png" sizes="48x48" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/android-icon-48x48.png?v=2">
            <link rel="icon" type="image/png" sizes="72x72" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/android-icon-72x72.png?v=2">
            <link rel="icon" type="image/png" sizes="96x96" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/android-icon-96x96.png?v=2">
            <link rel="icon" type="image/png" sizes="144x144" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/android-icon-144x144.png?v=2">
            <link rel="icon" type="image/png" sizes="192x192" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/android-icon-192x192.png?v=2">

            <link rel="apple-touch-icon" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon.png?v=2">
            <link rel="apple-touch-icon" sizes="57x57" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-57x57.png?v=2">
            <link rel="apple-touch-icon" sizes="60x60" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-60x60.png?v=2">
            <link rel="apple-touch-icon" sizes="72x72" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-72x72.png?v=2">
            <link rel="apple-touch-icon" sizes="76x76" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-76x76.png?v=2">
            <link rel="apple-touch-icon" sizes="114x114" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-114x114.png?v=2">
            <link rel="apple-touch-icon" sizes="120x120" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-120x120.png?v=2">
            <link rel="apple-touch-icon" sizes="144x144" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-144x144.png?v=2">
            <link rel="apple-touch-icon" sizes="152x152" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-152x152.png?v=2">
            <link rel="apple-touch-icon" sizes="180x180" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-180x180.png?v=2">
            <link rel="apple-touch-icon" sizes="180x180" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/apple-icon-precomposed.png?v=2">

            <meta name="msapplication-TileColor" content="#FFFFFF">
            <meta name="msapplication-TileImage" content="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/ms-icon-144x144.png?v=2">
            <meta name="msapplication-config" content="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/favicon/browserconfig.xml">
            <!-- ****** faviconit.com favicons ****** -->
        
    

    
        <meta property="og:image"
              content="https://openlearning-cdn.s3.amazonaws.com/course__unswcourses_courses_COMP9331__course-promo-image-1481673142.39.jpg">
        <meta property="og:type" content="website">
        <meta property="og:title" content="COMP9331 Computer Networks &amp; Applications">
    

    

<script type="application/json" id="standalone-blockpage-data">
    {
        "siteURL": "https://www.openlearning.com",
        "mediaURL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/",
        "chunkURL": "https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/",
        "chunkURLS": {"testimonialLoder": ["testimonialLoder.ca8871bd18f1408df6dd.js", "testimonialLoder.ca8871bd18f1408df6dd.js.map"], "chunkIDs": ["chunkIDs.1a4eb3d364e2d263ce9a.js", "chunkIDs.1a4eb3d364e2d263ce9a.js.map"], "metrics": ["metrics.1ac90add601cd07fbbf4.js", "metrics.1ac90add601cd07fbbf4.js.map"], "chat": ["chat.d7e6a720441568d82138.js", "chat.d7e6a720441568d82138.js.map"], "portalInstitutionPageLoader": ["portalInstitutionPageLoader.6d878b41a080f394f4be.js", "portalInstitutionPageLoader.6d878b41a080f394f4be.js.map"], "courseOnBoarding": ["courseOnBoarding.25e51c0b668dd590f4b9.js", "courseOnBoarding.25e51c0b668dd590f4b9.js.map"], "tinymce": ["tinymce.14d84e414ae27d4fd55d.js", "tinymce.14d84e414ae27d4fd55d.js.map"], "teachPageLoader": ["teachPageLoader.df638fde31816b67110d.js", "teachPageLoader.df638fde31816b67110d.js.map"], "portalCoursePageLoader": ["portalCoursePageLoader.9b4616450073ba43c78d.js", "portalCoursePageLoader.9b4616450073ba43c78d.js.map"], "portalUserCommon": ["portalUserCommon.4c603735e40680d9f3cd.js", "portalUserCommon.4c603735e40680d9f3cd.js.map"], "analytics": ["analytics.153ffd405e9411149d16.js", "analytics.153ffd405e9411149d16.js.map"], "courseWalkThrough": ["courseWalkThrough.92cf1068621a725ed8d7.js", "courseWalkThrough.92cf1068621a725ed8d7.js.map"], "molpayLoader": ["molpayLoader.e5b8a4a72d999d6fb3a5.js", "molpayLoader.e5b8a4a72d999d6fb3a5.js.map"], "imagetools": ["imagetools.c8b0f6a2aaecbbb9a327.js", "imagetools.c8b0f6a2aaecbbb9a327.js.map"], "reduxStorage": ["reduxStorage.635f2131f41599dba089.js", "reduxStorage.635f2131f41599dba089.js.map"], "thankYouPageLoader": ["thankYouPageLoader.d6e028b07ec880fd3749.js", "thankYouPageLoader.d6e028b07ec880fd3749.js.map"], "teach": ["teach.b3a4964d910d1bc49719.js", "teach.b3a4964d910d1bc49719.js.map"], "portalAdminInstitutionGeneralSettingsPageLoader": ["portalAdminInstitutionGeneralSettingsPageLoader.ca542e107bb6158053b6.js", "portalAdminInstitutionGeneralSettingsPageLoader.ca542e107bb6158053b6.js.map"], "malaysiaHomepage": ["malaysiaHomepage.26a269f1fd9dcab4c801.js", "malaysiaHomepage.26a269f1fd9dcab4c801.js.map"], "aboutPageLoader": ["aboutPageLoader.68c2129459f91fe63a81.js", "aboutPageLoader.68c2129459f91fe63a81.js.map"], "overlay": ["overlay.d58cef201dee4071db06.js", "overlay.d58cef201dee4071db06.js.map"], "blockPage": ["blockPage.c8edde01f1a3b9dac69a.js", "blockPage.c8edde01f1a3b9dac69a.js.map"], "teamPageLoader": ["teamPageLoader.9a6204b70612bde57b08.js", "teamPageLoader.9a6204b70612bde57b08.js.map"], "linkedNotificationLoader": ["linkedNotificationLoader.9ae6f75e052ed7d084a1.js", "linkedNotificationLoader.9ae6f75e052ed7d084a1.js.map"], "courseGroupsLoader": ["courseGroupsLoader.b98d0f5221be6a8b5e28.js", "courseGroupsLoader.b98d0f5221be6a8b5e28.js.map"], "courseCertificationSetupLoader": ["courseCertificationSetupLoader.4b28d2362931559788ed.js", "courseCertificationSetupLoader.4b28d2362931559788ed.js.map"], "clearCourseCache": ["clearCourseCache.85e7d9a72b3cdb25de73.js", "clearCourseCache.85e7d9a72b3cdb25de73.js.map"], "portalAdminInstitutionBrandingPageLoader": ["portalAdminInstitutionBrandingPageLoader.3daf5edd46f1715eef66.js", "portalAdminInstitutionBrandingPageLoader.3daf5edd46f1715eef66.js.map"], "OLexports": ["OLexports.ec44c85cfe806a912c1c.js", "OLexports.ec44c85cfe806a912c1c.js.map"], "online": ["online.48a87c93a4036b611cab.js", "online.48a87c93a4036b611cab.js.map"], "landingPageSetupLoader": ["landingPageSetupLoader.1a2dac38ab96bfbd4eff.js", "landingPageSetupLoader.1a2dac38ab96bfbd4eff.js.map"], "portalAdminQualificationsPageLoader": ["portalAdminQualificationsPageLoader.70aac01d04e1ba066b37.js", "portalAdminQualificationsPageLoader.70aac01d04e1ba066b37.js.map"], "richTextDisplay": ["richTextDisplay.c1c54a76016ce53b13b0.js", "richTextDisplay.c1c54a76016ce53b13b0.js.map"], "assessment": ["assessment.efea02d665fc1585aa3a.js", "assessment.efea02d665fc1585aa3a.js.map"], "pricingPageLoader": ["pricingPageLoader.107d8b1256f0b10e9180.js", "pricingPageLoader.107d8b1256f0b10e9180.js.map"], "courseRoles": ["courseRoles.19b795b1c99a91c52428.js", "courseRoles.19b795b1c99a91c52428.js.map"], "cohortScheduleAdmin": ["cohortScheduleAdmin.8dfafd241fa6e015218c.js", "cohortScheduleAdmin.8dfafd241fa6e015218c.js.map"], "homepageLoader": ["homepageLoader.9ca6288ed47f2a326058.js", "homepageLoader.9ca6288ed47f2a326058.js.map"], "jobs": ["jobs.a8f8ae6ca6ef39f87ed6.js", "jobs.a8f8ae6ca6ef39f87ed6.js.map"], "moment": ["moment.a8f0e7b81b24ee2e57ba.js", "moment.a8f0e7b81b24ee2e57ba.js.map"], "paymentPageLoader": ["paymentPageLoader.93751e36b1d0b2e72735.js", "paymentPageLoader.93751e36b1d0b2e72735.js.map"], "notificationHistory": ["notificationHistory.c329c10c2df4761d750f.js", "notificationHistory.c329c10c2df4761d750f.js.map"], "portalQualificationPageLoader": ["portalQualificationPageLoader.27fa607e34a52b702362.js", "portalQualificationPageLoader.27fa607e34a52b702362.js.map"], "portalAdminInstitutionPageSectionsPageLoader": ["portalAdminInstitutionPageSectionsPageLoader.01f83927a602a76681c8.js", "portalAdminInstitutionPageSectionsPageLoader.01f83927a602a76681c8.js.map"], "portalTinyMCECommon": ["portalTinyMCECommon.e2cf21fc501d1baa93ea.js", "portalTinyMCECommon.e2cf21fc501d1baa93ea.js.map"], "courseOutcomes": ["courseOutcomes.33397ad684cba030a126.js", "courseOutcomes.33397ad684cba030a126.js.map"], "previewFeedPageLoader": ["previewFeedPageLoader.d88dc53d701ef4f9269d.js", "previewFeedPageLoader.d88dc53d701ef4f9269d.js.map"], "portalAdminQualificationsLandingPageLoader": ["portalAdminQualificationsLandingPageLoader.c77c07bcb0d96820b1ef.js", "portalAdminQualificationsLandingPageLoader.c77c07bcb0d96820b1ef.js.map"], "OLTopBar": ["OLTopBar.4b6bd068627d0603d8db.js", "OLTopBar.4b6bd068627d0603d8db.js.map"], "pieChart": ["pieChart.b615abd5f28e984edd51.js", "pieChart.b615abd5f28e984edd51.js.map"], "certificateVerificationLoader": ["certificateVerificationLoader.930e053139e5ecfcd531.js", "certificateVerificationLoader.930e053139e5ecfcd531.js.map"], "molpayResponsePageLoader": ["molpayResponsePageLoader.cf57eb2def32283237b8.js", "molpayResponsePageLoader.cf57eb2def32283237b8.js.map"], "smartAppBanner": ["smartAppBanner.5e7afc702aba4dea27b6.js", "smartAppBanner.5e7afc702aba4dea27b6.js.map"], "navigationSetup": ["navigationSetup.452aa9738a3f120178cf.js", "navigationSetup.452aa9738a3f120178cf.js.map"], "courseCertificationAppearanceLoader": ["courseCertificationAppearanceLoader.1bcc30a711bf9d1bf10c.js", "courseCertificationAppearanceLoader.1bcc30a711bf9d1bf10c.js.map"], "courselandingpage": ["courselandingpage.218162e9696ee983fd71.js", "courselandingpage.218162e9696ee983fd71.js.map"], "teachathon": ["teachathon.b3d78ff66bbdb629c7a2.js", "teachathon.b3d78ff66bbdb629c7a2.js.map"], "react": ["react.aa313b8d33224d84aa7f.js", "react.aa313b8d33224d84aa7f.js.map"], "notificationRedirect": ["notificationRedirect.5079f109218b68fc0e9e.js", "notificationRedirect.5079f109218b68fc0e9e.js.map"], "portalAdminInstitutionFaqsPageLoader": ["portalAdminInstitutionFaqsPageLoader.3b8eb3763e828bdfa00c.js", "portalAdminInstitutionFaqsPageLoader.3b8eb3763e828bdfa00c.js.map"], "portalAdminInstitutionSellingPointsPageLoader": ["portalAdminInstitutionSellingPointsPageLoader.d2b8ae0c06ad53f559cf.js", "portalAdminInstitutionSellingPointsPageLoader.d2b8ae0c06ad53f559cf.js.map"], "course": ["course.348fb35c7dfc6e1eef04.js", "course.348fb35c7dfc6e1eef04.js.map"], "institutionProgress": ["institutionProgress.ce4814e85ba5a9bfe085.js", "institutionProgress.ce4814e85ba5a9bfe085.js.map"], "patternLibraryLoader": ["patternLibraryLoader.da227661060d1c99bab2.js", "patternLibraryLoader.da227661060d1c99bab2.js.map"], "footer": ["footer.a9027b34201af7fb3cf6.js", "footer.a9027b34201af7fb3cf6.js.map"], "publicProgress": ["publicProgress.e3b8c84dc96f99c2e9c1.js", "publicProgress.e3b8c84dc96f99c2e9c1.js.map"], "sso": ["sso.07bc101089ff42fd717d.js", "sso.07bc101089ff42fd717d.js.map"], "coursesPageLoader": ["coursesPageLoader.3e90dde227f2bd0ac234.js", "coursesPageLoader.3e90dde227f2bd0ac234.js.map"], "chatHistory": ["chatHistory.9c4a905c1a630a65ad40.js", "chatHistory.9c4a905c1a630a65ad40.js.map"], "anon": ["anon.30874ae92a7a948d6790.js", "anon.30874ae92a7a948d6790.js.map"], "classCertificationLoader": ["classCertificationLoader.91fc8e0522565725fc40.js", "classCertificationLoader.91fc8e0522565725fc40.js.map"], "progressPage": ["progressPage.2cec720f4ba68a7de96e.js", "progressPage.2cec720f4ba68a7de96e.js.map"], "moduleEditor": ["moduleEditor.e2c8a8a9ea28988c17bf.js", "moduleEditor.e2c8a8a9ea28988c17bf.js.map"], "portalAdminInstitutionFooterPageLoader": ["portalAdminInstitutionFooterPageLoader.8cd5a5ed915f280fdec6.js", "portalAdminInstitutionFooterPageLoader.8cd5a5ed915f280fdec6.js.map"], "raven": ["raven.2e27564d0070108f74e5.js", "raven.2e27564d0070108f74e5.js.map"], "ssoProvisioningLoader": ["ssoProvisioningLoader.b1129d8ab9d5c15a5a1b.js", "ssoProvisioningLoader.b1129d8ab9d5c15a5a1b.js.map"]},
        "profileName": "",
        "isAdmin": false,
        "isSuper": false,
        "isAnon": false
    }
</script>

<script type="application/json" id="site-url-data">
    {
        "baseMedia": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/",
        "transformURL": "https://live-assets.scdn5.secure.raxcdn.com/transform",
        "siteURL": "https://www.openlearning.com",
        "socketcluster": {
            "host": "auweb11.openlearning.com",
            "port": 443
        },
        "iframelyKey": "d84fd7201524f3ea0333c77b9a3dc776"

    }
</script>


<!-- DATA PROVIDERS -->

<!-- OpenLearning User Messaging -->

<script type="application/json" id="user-messaging-data">
    {
        "userMessaging": {
            "myFullName": "Brian Lam",
            "myProfileName": "brian.lam",
            "myAvatar": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-48-ts1476971072.jpg",
            "mediaURL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/",
            "emoticonPath": "images/emoticons/"
        },
        "desktopChat": {
            "profileName": "brian.lam"
        }
    }
</script>
<script type="application/json" id="initial-users-data">
    {"brian.lam": {"externalIds": {"institution:unswcourses": "z5035087", "cohort:unswcourses/courses/comp9331-s2/cohorts/classof2017": "z5035087"}, "userId": "504caba4bbddbd3726000000", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-48-ts1476971072.jpg", "groups": ["unswcourses/courses/comp9331-s2/Cohorts/ClassOf2017", "courses/COMP1927-14s2/Cohorts/ClassOf2014", "courses/Comp1917Rag/Cohorts/ClassOf2016"], "profileName": "brian.lam", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-120-ts1476971077.jpg", "fullName": "Brian Lam", "id": "504caba4bbddbd3726000000", "smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-24-ts1476971074.jpg", "standardAvatarPath": "brian.lam-avatar-48-ts1476971072.jpg", "privacyOptions": {}, "profileLink": "https://www.openlearning.com/u/brian.lam"}}
</script>
<script type="application/json" id="current-user-data">
    "brian.lam"
</script>
<script type="application/json" class="redux-users">
    [{"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-24-ts1476971074.jpg", "externalIds": {"institution:unswcourses": "z5035087", "cohort:unswcourses/courses/comp9331-s2/cohorts/classof2017": "z5035087"}, "standardAvatarPath": "brian.lam-avatar-48-ts1476971072.jpg", "userId": "504caba4bbddbd3726000000", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-48-ts1476971072.jpg", "privacyOptions": {}, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-120-ts1476971077.jpg", "profileLink": "https://www.openlearning.com/u/brian.lam", "profileName": "brian.lam", "fullName": "Brian Lam", "id": "504caba4bbddbd3726000000"}]
</script>
<script type="application/json" id="current-user-id-data">
    "504caba4bbddbd3726000000"
</script>

<script type="application/json" id="initial-cohorts-data">
    {"unswcourses/courses/comp9331-s2/Cohorts/ClassOf2017": {"cohortTitle": "Class of 17s2", "path": "unswcourses/courses/comp9331-s2/cohorts/classof2017", "courseTitle": "COMP9331 - Semester 2 Computer Networks and Applications", "title": "COMP9331 - Semester 2 Computer Networks and Applications (Class of 17s2) "}, "courses/Comp1917Rag/Cohorts/ClassOf2016": {"cohortTitle": "Class of 2016", "path": "courses/comp1917rag/cohorts/classof2016", "courseTitle": "The Art of Computing 1", "title": "The Art of Computing 1 (Class of 2016) "}, "courses/COMP1927-14s2/Cohorts/ClassOf2014": {"cohortTitle": "COMP1927-14s2", "path": "courses/comp1927-14s2/cohorts/classof2014", "courseTitle": "COMP1927-14s2 - Computing 2", "title": "COMP1927-14s2 - Computing 2 (COMP1927-14s2) "}}
</script>
<script type="application/json" id="initial-notifications-data">
    ""
</script>
<script type="application/json" id="initial-notifications-seen-time-data">
    "2017-05-14T14:00:02.304Z"
</script>
















<!-- end User Messaging -->

<!-- end User Messaging -->

<!-- TODO: consolidate this to retrieve from a single data-source and have more signed fields -->
<script type="application/json" id="class-data-loader">
{
    
        "user-id":  "504caba4bbddbd3726000000",
        "isSuperUser": false,
        
            
                "isCourseAdmin": false, 
            
                "isCourseStaff": false,
        
       
    
    "_token": "a8a5a25c19ac2bba7d043acfe13b21e2c4529627",
    

    "remote-address": "110.20.162.5, 10.189.254.6",
    "id-type": "legacy",
    "page-id": "58293794c57691021ca4bfe1",
    "page-path": "",
    "notifications": {
        "num-unread": "0",
        "num-messages": 0
    },



    
        "cohort-type": "course-unenrolled",
        "cohort": "unswcourses/courses/COMP9331",
    

    "progress": {
        "percentage": 0,
        "num-completed": 0,
        "completion-message": "You are Awesome!"
    },
    "kudos": 0,
    "comments": {
        "num-posts": null,
        "num-image-posts": null,
        "num-replies": null,
        "num-posts-liked": null,
        "num-likes-received": null
    },
    "affect": null,
    "badges": {
        "num-received": null
    },
    "courses": {
        "num-enrolled": 0
    },
    "sharing": {
        "num-posts": null,
        "num-favourites": null,
        "num-blog-posts": null
    },
    "pages": {
        "num-edits": null,
        "num-subscribed-to": null
    },
    "is-course": true,
    "is-new-layout": true,
    "module-editor-enabled": true
    
}
</script>

<!-- END DATA -->

<script type="text/javascript">
window.olFuture = {};
</script>




    <meta property="og:title" content="COMP9331 Computer Networks &amp; Applications on openlearning.com"/>
    <meta property="og:type" content="website"/>
    <meta property="og:image" content="https://www.openlearning.comhttps://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/redesign/openlearning_icon_small.jpg"/>
    <meta property="og:url" content="https://www.openlearning.com/unswcourses/courses/COMP9331"/>
    <meta property="og:site_name" content="openlearning.com"/>
    <meta property="fb:app_id" content="203356799790933"/>
    <meta property="og:description" content="A brief summary of the course..." />
    <meta name="description" content="A brief summary of the course...">


    <title>


    COMP9331 Computer Networks &amp; Applications on openlearning.com


    </title>

    <link href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/new/css/style.css" rel="stylesheet" type="text/css">
    <link href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/lib/bootstrap-modal/bootstrap-modal.css" rel="stylesheet" type="text/css">


    



    

    <link rel="stylesheet" type="text/css" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/new/css/pages/courseTheme2.css">
    <link rel="stylesheet" type="text/css" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/new/css/iconhover-component.css" />
    <link rel="stylesheet" type="text/css" href="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/lib/font-awesome-4.5/css/font-awesome.css" />

    <style>
        
        body {
            
            background-image: url(https://openlearning-cdn.s3.amazonaws.com/course__unswcourses_courses_COMP9331__course-background-image-1479360836.77.jpg);
            
            background-color: #eeeeee;
            
            background-repeat: repeat-all;
            
            background-attachment: fixed;
            background-position: left center;
        }

        #site-container {
            background: inherit;
        }
        .page-section {
            background: none;
        }
        

        #course-banner {
            
                
            background-image: url(https://openlearning-cdn.s3.amazonaws.com/course__unswcourses_courses_COMP9331__course-banner-image-1485733864.53.jpg);
            filter: none;
                
            

            

            background-repeat: no-repeat;
            background-size: cover;
        }

        

        #non-course-page-content {
            margin: 0;
        }

        .course-banner-container.tall-banner {
            height: 0;
            padding-bottom: 14.52991452991453%;
        }

        .course-banner-container .banner-title {
            line-height: normal;
            display: flex;
            align-items: center;
            height: 100%;
        }

        .course-banner-container .banner-title .banner-title-text {
            width: 100%;
        }

        .course-banner-container.tall-banner .banner-title {
            line-height: normal;
            display: flex;
            align-items: center;
            height: 100%;
        }

        .course-banner-container.tall-banner .banner-title .banner-title-text {
            width: 100%;
        }

        @media (max-width: 480px) {
            .course-banner-container .banner-title, .course-banner-container.tall-banner .banner-title {
                line-height: normal;
                display: flex;
                align-items: center;
                height: 100%;
            }

            .course-banner-container .banner-title .banner-title-text,
            .course-banner-container.tall-banner .banner-title .banner-title-text {
                width: 100%;
            }
        }

        @media (max-width: 344px) {
            .course-banner-container.tall-banner {
                height: 50px;
                padding-bottom: 0;
            }
        }

        .course-banner-container > a {
            display: block;
            height: 100%;
        }

        .course-banner-container > a .ribbonwrapper {
            display: block;
            position: absolute;
            width: 100%;
            height: 100%;
        }
    </style>

    <style type="text/css">
        @font-face {
            font-family: Evenfall Upright;
            src: url("https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0//font/evenfall-upright.otf") format("opentype");
        }

        @font-face {
            font-family: Evenfall Upright;
            src: url("https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0//font/evenfall-upright.ttf") format("truetype");
        }
    </style>

    <link href="//fonts.googleapis.com/css?family=Open+Sans:300,400,600,700" rel="stylesheet" type="text/css">

    <!-- External Service Scripts -->
    <script type="text/javascript" src="//api.filepicker.io/v1/filepicker.js"></script>
    <script charset="utf-8">
        var currentCourseName = 'COMP9331 Computer Networks &amp; Applications';
        var currentCourse = 'unswcourses/courses/COMP9331';
        var currentCohort = '';
        window.OpenLearningUserData = {
            
                courseAdmin: false,
                isMyProfilePage: 'false' == 'true',
                profileName: 'brian.lam',
                fullName: 'Brian Lam',
                avatar24: 'https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-24-ts1476971074.jpg',
                avatar48: 'https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-48-ts1476971072.jpg',
                initialUsers: {"brian.lam": {"externalIds": {"institution:unswcourses": "z5035087", "cohort:unswcourses/courses/comp9331-s2/cohorts/classof2017": "z5035087"}, "userId": "504caba4bbddbd3726000000", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-48-ts1476971072.jpg", "groups": ["unswcourses/courses/comp9331-s2/Cohorts/ClassOf2017", "courses/COMP1927-14s2/Cohorts/ClassOf2014", "courses/Comp1917Rag/Cohorts/ClassOf2016"], "profileName": "brian.lam", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-120-ts1476971077.jpg", "fullName": "Brian Lam", "id": "504caba4bbddbd3726000000", "smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-24-ts1476971074.jpg", "standardAvatarPath": "brian.lam-avatar-48-ts1476971072.jpg", "privacyOptions": {}, "profileLink": "https://www.openlearning.com/u/brian.lam"}},
                profileImageFilename: '27cc7abdaefcf08cb093a0b049349599.jpg',
                id: '504caba4bbddbd3726000000',
                timezoneOffset: 600.0,
                timezone: "Australia/Brisbane",
                currentCohort: currentCohort,
                pageAccess: {
                    read: false,
                    write: false,
                    admin: false
                }
            
        };
        var absoluteURI = 'https://www.openlearning.com/unswcourses/courses/comp9331?redirectTo=https%3A%2F%2Fwww.openlearning.com%2Funswcourses%2Fcourses%2Fcomp9331%2Flab_exercise_2_socket_programming%2Fsample_client_server_programs_and_networking_resources%2F588a9390117bd057c84aa0cb%2FTCPClient.py';
        var baseMedia = 'https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/';
        var siteURL = 'https://www.openlearning.com';
        
    </script>



<!-- START CHUNK chunkIDs -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/chunkIDs.1a4eb3d364e2d263ce9a.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK chunkIDs -->




<!-- START CHUNK anon -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/anon.30874ae92a7a948d6790.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK anon -->





<!-- START CHUNK imagetools -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/imagetools.c8b0f6a2aaecbbb9a327.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK imagetools -->













    <script src="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/scripts/min/ol-anon.min.js"></script>




<!-- end OpenLearning Metrics -->
<script charset="utf-8">
    JS.require('OpenLearning', 'jQuery.ui', 'Utilities', function() {
        
        var isNewAccount = !!Utilities.getCookie("OL-NewAccount");
        if (isNewAccount) {
            Utilities.deleteCookie("OL-NewAccount");
        }
        
    });
 </script>
 <!--[if lte IE 8]>
<style>
  input {
    font-family: Arial;
  }
</style>
<![endif]-->






</head>
<body class=" courseTheme2">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script src="//static.tapfiliate.com/tapfiliate.js" type="text/javascript" async></script>
<script type="text/javascript">
    window['TapfiliateObject'] = i = 'tap';
    window[i] = window[i] || function () {
                (window[i].q = window[i].q || []).push(arguments);
            };
    tap('create', '2627-89fd0d');
</script>



<!-- START CHUNK smartAppBanner -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/smartAppBanner.5e7afc702aba4dea27b6.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK smartAppBanner -->



    
<div id="site-header-bar">
    <header id="site-header-bar-header" class="header small-header stickyheader logged-in"
            style="min-height: 35px; max-height: 35px;">
        <div class="container">
            <div class="row visible-phone mobile-header-row" id="mobile-header-row">
                
                    <button type="button" id="mobile-nav-menu-btn"
                            class="mobile-heading-item pull-left mobile-heading-button"><i class="icon-reorder"></i>
                    </button>

                    <div id="mobile-online-toggle" class="toggle-light" style="display:none;"></div>
                   
                    <div  class="mobile-heading-item mobile-heading-button pull-right" riot-tag="notifications-dropdown" browser="mobile"></div>
                    
                    
                
            </div>

            <div class="row hidden-phone" id="desktop-header-row">
                <section class="logo pull-left">
                    
                        <a class="pull-left" href="https://www.openlearning.com/" title="OpenLearning">
                            <style type="text/css">
                                header .header-logo-image {
                                    background-image: url(https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/OpenLearning-Logo-Regular.png);
                                    background-size: 176px 44px;
                                    width: 176px;
                                    height: 44px;
                                    position: relative;
                                    top: 7px;
                                }

                                header.small-header .header-logo-image {
                                    background-image: url(https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/OpenLearning-Logo-Small.png);
                                    background-size: 140px 35px;
                                    width: 140px;
                                    height: 35px;
                                    top: 0px;
                                }

                                /* This hides the OpenLearning logo's text so the content of the header bar does not wrap. */
                                @media (max-width: 850px) {
                                    header .header-logo-image {
                                        width: 40px;
                                    }

                                    header.small-header .header-logo-image {
                                        width: 32px;
                                    }
                                }
                            </style>
                            <div class="header-logo-image" alt="OpenLearning" id="header-logo"></div>
                        </a>
                    
                    <span>
                        <div id="search-container" class="pull-left">
                            <form id="search-container-form" style="margin-top: 3px;" class="small-search-form" action="https://www.openlearning.com/search/" method="get" accept-charset="utf-8">
                                <input type="text" name="q" value=""
                                       placeholder="Search">
                                <input type="hidden" name="course" value="unswcourses/courses/COMP9331">
                            </form>
                        </div>
                    </span>
                </section>

                <section class="pull-right" style="margin-top: 0;">
                    <nav id="main_menu_sticky">
                        <div id="headerbar-nav-container" class="nav-collapse collapse">
                            
                                <ul class="nav nav-pills pull-right">
                                    <!-- Notifications -->
                                    <li class="dropdown" riot-tag="notifications-dropdown" browser="desktop"></li>
                                    <!-- Courses -->
                                    
                                    <li class="dropdown">
                                        <a class="dropdown-toggle menu-item-link" data-toggle="dropdown" href="#">
                                            <span class="menu-item-text">
                                                <img src="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0//images/Graphics/Icons/Icon_Globe.png">
                                                Courses
                                            </span>
                                        </a>
                                        <ul class="courses-dropdown-menu dropdown-menu" role="menu" id="courses-dropdown">
                                            <li class="courseDropdownItem course-dropdown-loading"><span class="loader-placeholder loader-icon" style="margin: 10px auto; float:none;"></span></li>

                                            
                                            <li class="divider"></li>
                                            <li>
                                                <a href="https://www.openlearning.com/courses/my/">
                                                    View all my courses
                                                </a>
                                            </li>
                                            
                                                <li>
                                                    <a href="https://www.openlearning.com/courses/">
                                                        Find new courses
                                                    </a>
                                                </li>
                                            
                                            <li>
                                                <a href="https://www.openlearning.com/courses/create/">
                                                    Create a course
                                                </a>
                                            </li>
                                            
                                        </ul>
                                    </li>


                                    <!-- User Profile -->
                                    <li class="dropdown">
                                        <a id="profile-dropdown" class="dropdown-toggle menu-item-link" data-toggle="dropdown" data-target="#"
                                           href="#">
                                            
                                            <span class="menu-item-text">
                                            <img id="header-profile-image" src="https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-24-ts1476971074.jpg" alt="" border="0"
                                                 class="profile-image" align="absmiddle" id="myAvatar24">
                                            
                                                <span class="profile-name">Brian Lam</span>
                                            
                                        </span>


                                            
                                        </a>
                                        <ul class="dropdown-menu profile-image-dropdown-menu">
                                            <li class="launch-change-profile-picture-modal upload-profile-picture-container no-profile-picture-header-list-item" style="display: none;">
                                                <a class="upload-profile-picture" href="javascript:;">
                                                    <span class="icon-star-full"></span>
                                                    <span class="text">Change profile picture</span>
                                                </a>
                                            </li>
                                            <li class="launch-change-profile-picture-modal upload-profile-picture-container has-profile-picture-header-list-item">
                                                <a class="upload-profile-picture" href="javascript:;">
                                                    Change profile picture
                                                </a>
                                            </li>
                                            <li class="divider has-profile-picture-header-list-item"></li>
                                            <script type="text/javascript">
                                                (function () {
                                                    var noProfilePicLiElements = Array.prototype.slice.call(document.getElementsByClassName('no-profile-picture-header-list-item'));
                                                    var hasProfilePicLiElements = Array.prototype.slice.call(document.getElementsByClassName('has-profile-picture-header-list-item'));
                                                    if (window.OpenLearningUserData.profileImageFilename) {
                                                        noProfilePicLiElements.forEach(function (elem) {
                                                            elem.style.display = 'none';
                                                        });
                                                        hasProfilePicLiElements.forEach(function (elem) {
                                                            elem.style.display = '';
                                                        });
                                                    } else {
                                                        noProfilePicLiElements.forEach(function (elem) {
                                                            elem.style.display = '';
                                                        });
                                                        hasProfilePicLiElements.forEach(function (elem) {
                                                            elem.style.display = 'none';
                                                        });
                                                    }
                                                })();
                                            </script>
                                            <li>
                                                <a href="https://www.openlearning.com/u/brian.lam">
                                                    My Profile Page
                                                </a>
                                            </li>
                                            
                                                <li>
                                                    <a href="https://www.openlearning.com/accounts/conversations">
                                                        Chat History
                                                    </a>
                                                </li>
                                            
                                            <li class="divider"></li>
                                            <li>
                                                <a href="https://www.openlearning.com/accounts/account-settings/">
                                                    Account Settings
                                                </a>
                                            </li>
                                            <li>
                                                <a href="https://www.openlearning.com/accounts/notifications/#settings">
                                                    Notification Settings
                                                </a>
                                            </li>
                                            <li class="divider"></li>
                                            
                                            
                                            <li>
                                                <form action="/accounts/logout/" id="logout-form" class="logout-form"
                                                      method="post" accept-charset="utf-8">
                                                    <div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='CQZYT9b5LfYbfz4SvmvLRLtYN8CEOJpe' /></div>
                                                    <input type="submit" name="logout" class="logout-button"
                                                           id="logout-button" value="Logout"/>
                                                </form>
                                            </li>
                                        </ul>
                                    </li>

                                    <!-- Help -->
                                    <!--                             <li>
                                    <a class="menu-item-link" href="https://www.openlearning.com/help">
                                        <span class="menu-item-text">
                                            Help
                                        </span>
                                    </a>
                                </li> -->
                                <!-- hack for fullamark -->
                                
                                    <li>
                                        <a class="menu-item-link" href="
                                                https://www.openlearning.com/help">
                                            <span class="menu-item-text">
                                                Help
                                            </span>
                                        </a>
                                    </li>
                                    
                                
                                </ul>
                            
                        </div>
                    </nav>
                </section>
            </div>
        </div>
        <div class="header-sharing-backdrop hide"></div>
        <div class="container">
            <div id="header-sharing-bar-container" class="hide"></div>
            <div id="shared-feedback" class="shared-feedback-item hide">
                Thanks for sharing. Your post can be found in - <a href="" class="sharedLink"></a>
            </div>
        </div>
        
            
                
                    
                        
                    
                    
                
            

            
        
    </header>
    <div class="mobile-header-hack"></div> 
</div>



<!-- jQuery 2 does not work with IE<=8, so we need this alternative way of displaying our browser update warning. -->
<table id="very-old-ie-browser-warning" style="display: none; height: 100%; width: 100%; top: 0; left: 0; position: fixed; z-index: 9999;">
    <tr>
        <td style="vertical-align: middle;">
            <div style="line-height: 20px; background-color: white; width: 500px; margin-left: auto; margin-right: auto; padding: 20px; border: 1px solid black;">
                <div style="margin-bottom: 10px; color: #e74c3c; font-weight: bold;">
                    Please upgrade your browser
                </div>
                <div style="margin-bottom: 10px;">
                    Your browser is out of date, and may not be compatible with our website.
                </div>
                <div style="margin-bottom: 10px;">
                    For the best experience with OpenLearning, please click on one of the links below to download the
                    latest version of Chrome or Firefox:
                </div>
                <div>
                    <table style="margin-left: auto; margin-right: auto;">
                        <tr>
                            <td style="padding-right: 30px;">
                                <a style="background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAABBCAMAAABSHoJ0AAADAFBMVEVJo9fUHSrdpCcCgLzw1Gvi4uOr0Knz5a/zxBa5urvCw8RWp9ntkZTwalr96+r9/f3pSz1Lo0W21+niHSvb3NxRq0X41DfrUkP1rKqTYTTlsSLsbWdlu1ettCcom9JWuEbw8PCcmpz80gn5+fntW0rrzI3mOjP6zg7H3un0yBMCerfhqiX90QH++upYukfjKC3lMzGbyuVWtUbVni5krN3tuxyCg4XP6MzjIy329/bu1qX32dcyndOJio3qtR4SlM721Ux5izypqqyjo6UbmNCJuow5i0Hp6emSkpUAaafxthjtxRjer7LkLjBBk0Lu7u4Pkcz35JV7qzNrqXCZxJlInURVskbivnrk7fP++/X6493J2ciowH09oNXn8ufW1tewsbK33LWtxtX70QrnRDjnQDYLi8ZnnT58fYB5en3prB/68dnNzs+Hts8+i7cHhsGxsrPF0tz1+fXZxBhFmEP71B33ysalpqiyPC/a5OiLx4L60AxSwkjp8PUOj8mEhYjIyMrxwBiMjZDR0dLsx8mDvuL++f/267/zn5n+/fvy7vJdvE3432p5wW71yhv1+vx0rMnrfHjs4eaVlpgEc69dtFFasdjW3NXaqEVaqVMEjctzlED6//60tbfEKyzGxsisra++vsDKy8zzygXmSFS2trhWvkju5une7d5dsUb79v6cnZ8Vi8LT09RPp0XqTj+TzonlNjr+9/Z1u9v6+/onfK5Rl1vHFyTOz9DoRzoCiMXsVUb80g7jLybuX0/jIieztLWvsLF/gIP4yxDy8/NTr0br6+yHiIvU1NXLzM2YmJuoqKrm5udrv1338+ud1ZPP1t9Yp8ygoKL8+P7/+/3f3+D6xhOAqGbdFCWRwdzjMCuPkJPx9/H17/D28/r28/X71AzsWEhUmGDtvw3XR1HCbVtNjk5MlFIObaZhm770vLhGkU9Fm09IlE5Ts0O3uLlOm0zz08Nhpj9osdPqwCXovhTxxAfyzBLg6O7x6uzjtWPxiYbovU5QoUx3eHv///+f0uIBAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB98GFgkUNaJC0UAAABEOSURBVFgJAQMR/O4A////////////////////////////////////////////////////////////////////////////////////////AP///////////////////////////////////////////////////////////////////////////////////////wD///////////////////////////////+yWuqI+5ENDQ0NDQ2R+4jqWrL///////////////////////////////8A////////////////////////////snaIG76+vr6+vr6+vr6+vr4kJCQbDHay////////////////////////////AP////////////////////////8OGBvhJCQkvr6+vr6+vr6+vr4kJOHhuxcXDRgO/////////////////////////wD//////////////////////w6Ivhe7u+HhJCQkvr6+vr6+JCQk4eG7uxcXF68Qu4gO//////////////////////8A////////////////////1Bi+r68XF7u74eHhJCQkJCQkJCTh4bu7uxcXF68QELm54RjU////////////////////AP//////////////////WpG5EBCvrxcXF7u7u+Hh4eHh4eHhu7u7FxcXr68QELm5ZGRlG1r//////////////////wD/////////////////6hdkubkQEK+vrxcXFxcXu7u7u7u7FxcXFxevrxAQELm5ZGRlZSZk6v////////////////8A////////////////iGVlZGS5ubkQEK+vr68XFxcXFxcXFxcXr6+vEBAQubm5ZGRlZSYmMDCI////////////////AP////////////+J+yYmJmVlZLm5ubkQEBCvr6+vr6+vr6+vrxAQEBC5ublkZGVlJiYmMDBNTfv//////////////wD/////////////+zAwJiYmZWVlZGS5ubm5EBAQEBAQEBAQEBC5ubm5uWRkZWUmJiYwMDBNTS8v+/////////////8A////////////DE1NMDAwJiYmZWVlZGRkZLm5ubm5ubm5ubm5uWRkZGVlZSYmJiYwMDBNTS8vODgM////////////AP//////////GC8vTU1NMDAwJiYmJmVlZWVkZGRkZGRkZGRkZGVlZWUmJiYmJjAwME1NLy8vODgTExj//////////wD/////////O004Ly9NTU1NMDAwJiYmJiYmZWVlZWVlZWVlZWUmJiYmJiYwMDAwTU1NLy84OBMTExMvO/////////8A////////tOXYODg4Ly8vTU1NMDAwMDAmJiYmJiYmJiYmJiYmJiYwMDAwME1NTS8vLzg4ExMTExMTE6Sy////////AP///////2GbAQETODg4Ly8vTU1NTU0wMDAwMDAwMDAwMDAwMDAwME1NTU1NLy8vODg4ExMTExMTExMTDP///////wD//////16LfBnYARMTODg4OC8vL01NTU1NTU1NTU1NTU1NTU1NTS8vLy8vODg4OBMTExMTExMTExMTEy9a//////8A//////+wLqbyngEBExMTEzg4ODgvLy8vLy9NL7+/L7GxsbHavb3aTU1NTS8vLy8vLy8vLy8vLy8vLy8vkf//////AP////+oiy4ufBnYAQETExMTExMTODg4ODg4E00biHY7Ozs78SX6KwICKysrampqampqaj5KSkpKSkpKSjVr/////wD/////zx8uLqYueNgBARMTExMTExMTExPYOJE7tP9ZOTk5I4n/D2sE9PX0S0tLS0tLKSn39/f39/cne+DgjP////8A////3BwuLi4ufJsBAQEBExMTExMTExPYpIScD1gSMYWFhdkxEn3/D4dA40tLSwgIKSkpKSnDJ3tjIiIiInUt////AP///2EfLi4uLi58GdgBAQETExMTExPYG4r/WDE0CzQ0NDQ0NAs0MX3/3wT2KSkpKSnDJydjIiIiIiIiIiJjUf///wD///96Hy4uLi4upqme2AEBARMTExPYG8SJKDQACzQ0NDQ0NDQ0CwA0KA85BKPDJ3tjIiIiIiIiIiIiIiIiY0D///8A//9yHB8uLi4uLi58QdgBAQEBExPYpPm0EgAACwsLNDQ0NDQ0CwsLAAAS1M4WLCIiIiIiIiIiIiIiIiIiImN1Lf//AP//NzIfLi4uLi4uLh942AEBARMTE4ScEl1dAAALCwsLCwsLCwsLAABdXSjUhyIiIiIiIiIiIiIiIiIiIiJje4f//wD//wYyHy4uLi4uLi58mwEBAQEB2BuP+AA8XV0AAAALCwsLCwsAAABdXTwLfY+MLCIiIiIiIiIiIiIiIiIiY3tR//8A//+wMh8uLi4uLi4uLnwZtwEBAQGEtIVEPDxdXV0AAAAAAAAAAABdXTw8RNnUhyIiIiIiIiIiIiIiIiIiImN7jP//AP//jTIfLi4uLi4uLi6m8p63AbfkT/g8RB48PDxdXV1dXV1dXV1dXTw8HkRdfd8WLCIiIiIiIiIiIiIiImNjJ0CJ/wD//80yHy4uLi4uLi4uLnwZt7e3kSMSUEREHh48PDw8XV1dXTw8PDweHkREPxLTjCwiIiIiIiIiIiIiIiJjYycWWf8A//+VMh8fLi4uLi4uLi6mMni3t4i0s5o/REREHh4eHjw8PDweHh4eREREP36FhlEsIiIiIiIiIiIiIiIiY3snji3/AP//lTIyHy4uLi4uLi4uLnxBt7dMOZaaPz8/REREREQeHh4eHkREREQ/Pz+aloYHLCIiIiIiIiIiIiIiImN7J44t/wD//5VWMh8uLi4uLi4uLi4uphm3TCALmj8/Pz8/Pz9EREREREQ/Pz8/Pz9QmpbTBywiIiIiIiIiIiIiIiJje8OOLf8A//+VVjIfHy4uLi4uLi4uLnxnnkzEC5pQUFA/Pz8/Pz8/Pz8/Pz8/P1BQUJqWqgcsIiIiIiIiIiIiIiJjeyfDji3/AP//lcUyMh8uLi4uLi4uLi4ufBkMOfO6fn5QUFBQUFA/Pz8/UFBQUFBQUH66s6pRLCIiIiIiIiIiIiIiY3snw44t/wD//xzFVjIfLi4uLi4uLi4uLqbyId3ZumZ+fn5+UFBQUFBQUFBQUFB+fn5mujHejCwiIiIiIiIiIiIiY2MnwykWWf8A//+NxVYyHx8uLi4uLi4uLi4uH9eSKKxvZmZmfn5+fn5+fn5+fn5+ZmZmb6x5TxYsIiIiIiIiIiIiImN7J8MpQIn/AP//ehXFVjIfLi4uLi4uLi4uLi4uW/nRA29vb2ZmZmZmZmZmZmZmZm9vbwPz34e8IiIiIiIiIiIiImNjJ8MpCAT//wD//wYVxVYyHx8uLi4uLi4uLi4u7rD5cW8qAwNvb29vb29vb29vb28DAwOsKIqMLCIiIiIiIiIiIiJjeyfDKQhR//8A//83rhXFMjIfLi4uLi4uLi4uLh+LW/ltlCoqAwMDAwMDAwMDAwMDKioq2YoHvCIiIiIiIiIiIiJjeyfDKQiBh///AP//cpkVxVYyMh8uLi4uLi4uLi4uH43Vp5CUlCoqKioqKioqKioqKpSUkIrMFiwiIiIiIiIiIiJjY3snwykI9C3//wD///96rhXFVjIfHy4uLi4uLi4uLi7uegWnkJRJlJSUlJSUlJSUlEmUbfn4BCwiIiIiIiIiIiIiY3snwykIgQT///8A////YREVxVYyMh8uLi4uLi4uLi4uLu561adibklJSUlJSUlJSUluYt15XKMiIiIiIiIiIiIiY3snwykpgTUH////AP///9yZrhXFVjIyHy4uLi4uLi4uLi4uH41bpwVi6bXo6OjoteliR4pbUx0iIiIiIiIiIiJjY3snJ8MpCIH0Lf///wD/////VBGuFcVWMh8fHy4uLi4uLi4uLi4fi1SXp6fV0HFx0AX5+ZdU7FIiIiIiIiIiIiJjY3snJ8MpCIE1BP////8A/////6j9ERUVxVYyMh8fLi4uLi4uLi4uLh8fHHoGW5cUFJdbBkWZTnRzIiIiIiIiIiJjY3snJ8MpCIE1Pmv/////AP//////RVURFRXFVjIyHy4uLi4uLi4uLi4uLh8fHy4czc0cxa4RVXQdIiIiIiIiIiJjY3snJ8MpCIE1PgT//////wD//////6j9Ea4VFcVWMjIfHy4uLi4uLi4uLi4uLi4uHx8f7hUVrlXy9yIiIiIiIiJjY3snw8MpCIE1Phpr//////8A////////BlURrhUVxVYyMh8fLi4uLi4uLi4uLi4uLi4uLlbFFRFVHSIiIiIiImNjYycnw8MpCIE1Pho6////////AP///////7RTVRGuFRXFVjIyHx8fLi4uLi4uLi4uLi4uLh/FxRURUiIiIiIiY2NjeycnwykpCIE1Phr8Wf///////wD/////////qPBVEa6uFcXFVjIyHx8fLi4uLi4uLi4uLi4yxcWurnMiIiJjY2N7eyfDwykICIE1Phoaa/////////8A//////////9hdHRVEa4VFcVWMjIyHx8fLi4uLi4uLi4uVsXFER0iY2NjY3snJyfDKSkIgYE1PhorB///////////AP///////////1ROdFURrhUVxcVWMjIyMh8fHx8uLi4uH1bFFfL3Int7eycnw8MpKQgIgTU1PhorJf///////////wD/////////////VE50VRERrhUVxcVWVjIyMjIfHx8fHzLFxa4dIicnJ8PDwykpCAiBgTU+GhorJf////////////8A/////////////w9UTnR0VRGurhUVxcVWVlYyMjIyMjLFxRVSwyfDw8MpKSkICIGBNT4+GisCJf//////////////AP///////////////1ROTnRVVRGurhUVFcXFxVZWVlZWFRUVc8MpKSkICAiBgTU1Pj4aGisCJf///////////////wD/////////////////Ye1OTnRVVRERrq4VFRUVFRXFFa4RHdYICAiBgYGBNTU+PhoaKwICB/////////////////8A//////////////////+oU0ZOTnR0VVURERGurq6uFa4R8vWBgYE1NTU1Pj4aGisrAgL6a///////////////////AP///////////////////w8G50ZOTnR0dFVVVRERERFVVR01NT4+Pj4+GhoaKysCApg6if///////////////////wD//////////////////////15F60ZGTk5OdHR0dFVVdGcaGhoaGhorKysCAgIzMyXO//////////////////////8A/////////////////////////15UtkZGRk5OTk5OTk4daisrKwICAgICMzOYJc7/////////////////////////AP///////////////////////////3JbRbZGRkZGRkabAgICAjMzMzMzmFcHWf///////////////////////////wD///////////////////////////////9yqAZFU+LmMzMzMzOY+lc6a1n///////////////////////////////8A////////////////////////////////////////////////////////////////////////////////////////AP////////////////////////////////////////////////////////////////////////////////////////J/Sybzr0cBAAAAAElFTkSuQmCC); position: relative; background-position: center top; background-repeat: no-repeat; display: inline-block; width: 70px; height: 105px; chrome-link"
                                   href="https://www.google.com/chrome/browser/desktop/index.html" target="_Blank">
                                    <span style="text-align: center; position: absolute; bottom: 0; color: #3498db; line-height: 15px;">Download Chrome</span>
                                </a>
                            </td>
                            <td>
                                <a style="background-image: url(data:image/png;base64,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/f39AP7//wD///8AAQAAAAAAAAACAgIAAgICAAQEBAAEBAQABAQEAAUFBQAGBgYABgYGAAUFBQAGBgYABgYGAAUFBQAFBQUABAQEAAQEBAAEBAQABAQEAAICAgABAQEAAQEBAAEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH/////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD+/v4A/v7+AP7+/gD8/PwA/f39AP39/QD9/f0A/f39APz8/AD9/f0A/v7+AP39/QD+/v4A/v7+AP///wAAAAAAAAAAAAAAAAABAQEAAgICAAICAgACAgIAAwMDAAMDAwADAwMAAwMDAAMDAwAEBAQAAwMDAAMDAwADAwMAAgICAAICAgABAQEAAQEBAAEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH/////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD+/v4A/v7+AP///wD///8A/v7+AP///wD///8A////AP///wAAAAAAAAAAAAAAAAABAQEAAAAAAAICAgAAAAAAAgICAAICAgABAQEAAgICAAEBAQACAgIAAQEBAAEBAQABAQEAAQEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH/////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8AAAAAAP///wAAAAAAAAAAAP///wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBAQAAAAAAAQEBAAAAAAABAQEAAAAAAAEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH/////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMUsKOsP0Cm6AAAAAElFTkSuQmCC); position: relative; background-position: center top; background-repeat: no-repeat; display: inline-block; width: 70px; height: 105px; firefox-link" href="https://www.mozilla.com/firefox" target="_Blank">
                                    <span style="text-align: center; position: absolute; bottom: 0; color: #3498db; line-height: 15px;">Download Firefox</span>
                                </a>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </td>
    </tr>
</table>
<script type="text/javascript">
    /**
     * Internet Explorer browser of versions 10 and older can be detected in JavaScript by checking existence of the
     * nonstandard document.all object available only in IE10 and older.
     *
     * document.addEventListener() was first implemented in IE9.
     *
     * Therefore document.all && !document.addEventListener checks whether we are in IE < 9.
     */
    if (document.all && !document.addEventListener) {
        document.getElementById('very-old-ie-browser-warning').style.display = 'table';
    }
</script>

<!--Non mobile site content-->
<div id="site-container" class="small-header">
    <div class="mobile-selection" id="mobile-courses-selection"></div>
    <div class="mobile-selection" id="mobile-notifications-selection"></div>
    
        

        

        
            <!-- Scripts for Modals -->

<script type="text/javascript" charset="utf-8">
	var ListSubscribers = {
		openModal: function() {
			$('#list-subscribers-modal .modal-content').text('Loading list of subscribers...')
													   .load('?action=listSubscribers', {}, function() {
														$(window).trigger('resize');
													});

			$('#list-subscribers-modal').modal({
				show: true
			});
			
		},
		closeModal: function() {
			$('#list-subscribers-modal').modal('hide');
		}
	};

	var ListSubpages = {
		openModal: function() {
			$('#list-subpages-modal .modal-content').text('Loading list of sub-pages...')
													.load('?action=listSubpages', {}, function() {
														$(window).trigger('resize');
													});

			$('#list-subpages-modal').modal({
				show: true
			});
			
		},
		closeModal: function() {
			$('#list-subpages-modal').modal('hide');
		}
	};

	var AddThumbnail = {
		openModal: function() {
			$('#add-thumbnail-modal').modal({
				show: true
			});
		},
		closeModal: function() {
			$('#add-thumbnail-modal').modal('hide');
		}
	}
	var AddSubpage = {
		currentPage: 'https://www.openlearning.com/unswcourses/courses/COMP9331/',
		pageToCreate: '',
		openModal: function() {
			$('#add-subpage-modal').modal({
				show: true
			});

			// Highlight the input box upon modal open -- cause clicking sucks
			$('#add-subpage-modal').on('shown', function() {
				$('#addSubpageName').focus()
			});
		},
		closeModal: function() {
			$('#add-subpage-modal').modal('hide');
		},

		// Context: the textbox
		updateUrlPreview: function() {
			var pageTitle = $(this).val();

			var capitalizedPageTitle = pageTitle.toLowerCase().replace(/\b([a-z])/gi,function( word ){ return word.toUpperCase() });

			var unspacedPageTitle = capitalizedPageTitle.replace(/[^A-Za-z0-9]+/g, '');

			AddSubpage.pageToCreate = AddSubpage.currentPage + unspacedPageTitle;
			$('#addSubpageDynamicURL').text( unspacedPageTitle );
		},
		addSubpage: function() {
			document.location.href = AddSubpage.pageToCreate + '?title=' + $('#addSubpageName').val();
		}
	};

	
	JS.require( '$.fn.modal', function() {
		$(document).ready( function() {
			// Define references to the modals and their buttons.
			var listSubscribersModal = $('#list-subscribers-modal');
			var listSubpagesModal = $('#list-subpages-modal');
			var addSubpageModal = $('#add-subpage-modal');
			var listSubscribersModalButton = $('#listSubscribers');
			var listSubpagesModalButton = $('#listSubpages');
			var addSubpageModalButton = $('#addSubpage');
			var addThumbnailModalButton = $('#addThumbnail');
			var addSubpageForm = $('#addSubpageForm');

			// Attach handlers to the buttons
			listSubscribersModal.find('.btn-danger, .close').click(ListSubscribers.closeModal);
			listSubscribersModalButton.click(ListSubscribers.openModal);

			listSubpagesModal.find('.btn-danger, .close').click(ListSubpages.closeModal);
			listSubpagesModalButton.click(ListSubpages.openModal);

			addSubpageModal.find('.btn-danger, .close').click(AddSubpage.closeModal);
			addSubpageModal.find('.btn-primary').click(AddSubpage.addSubpage);
			addSubpageModal.find('#addSubpageName').on('keyup', AddSubpage.updateUrlPreview);
			addSubpageForm.submit(function(e) { e.preventDefault(); AddSubpage.addSubpage(); });
			addSubpageModalButton.click(AddSubpage.openModal);
			addThumbnailModalButton.click(AddThumbnail.openModal);

	
		} );
	} );
</script>

<!-- List Subscribers Modal -->
<div id="list-subscribers-modal" class="modal hide fade">
	<div class="modal-header">
		<a href="#" class="close">&times;</a>
		<h3>List of Subscribers</h3>
	</div>
	<div class="modal-body">
		<p class="modal-content">
			
		</p>
	</div>
	<div class="modal-footer">
		<a href="#" class="btn btn-inverse" data-dismiss="modal">Close</a>
	</div>
</div>

<!-- List Subpages Modal -->
<div id="list-subpages-modal" class="modal hide fade">
	<div class="modal-header">
		<a href="#" class="close">&times;</a>
		<h3>Pages under COMP9331 Computer Networks &amp; Applications</h3>
	</div>
	<div class="modal-body">
		<p class="modal-content">
			
		</p>
	</div>
	<div class="modal-footer">
		<a href="#" class="btn btn-inverse" data-dismiss="modal">Close</a>
	</div>
</div>

<!-- Add Thumbnail Modal -->
<div id="add-thumbnail-modal" class="modal hide fade">
	<form enctype="multipart/form-data" method="post" action="?action=addThumbnail">
	<div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='CQZYT9b5LfYbfz4SvmvLRLtYN8CEOJpe' /></div>
	<div class="modal-header">
		<a href="#" class="close">&times;</a>
		<h3>Add Thumbnail</h3>
	</div>
	<div class="modal-body">
		<p class="modal-content">
			<label>Choose a thumbnail</label>
			<input type="file" id="thumbnailFile" name="thumbnailFile">
			<input type="hidden" name="pagePath" value="https://www.openlearning.com/unswcourses/courses/COMP9331">
		</p>
	</div>
	<div class="modal-footer">
		<a href="#" class="btn btn-inverse" data-dismiss="modal">Cancel</a>
		<input type="submit" class="btn btn-primary" value="Save Thumbnail">
	</div>
	</form>
</div>

<!-- Add Subpage Modal -->
<div id="add-subpage-modal" class="modal hide fade">
	<div class="modal-header">
		<a href="#" class="close">&times;</a>
		<h3>Add Subpage</h3>
	</div>
	<div class="modal-body">
		<p class="modal-content">
			<form id="addSubpageForm">
				<label>Subpage Name</label>
				<input type="text" id="addSubpageName" name="addSubpageName">
				<br><br>
				<label>URL Preview</label>
				<div id="addSubpageURLPreview">https://www.openlearning.com/unswcourses/courses/COMP9331/<span id="addSubpageDynamicURL" style="color: #00a;"></span></div>
			</form>
		</p>
	</div>
	<div class="modal-footer">

		<a href="#" class="btn btn-inverse" data-dismiss="modal">Cancel</a>
		<a href="#" class="btn btn-primary">Add Sub-page</a>
	</div>
</div>

<!-- Revert Revision Modal -->
<div id="revert-page-modal" class="modal hide">
	<div class="modal-header">
		<a href="#" class="close">&times;</a>
		<h3>Revert Changes</h3>
	</div>
	<div class="modal-body">
		<p class="modal-content">
			This will set this old revision of the page as the latest revision. Do you wish to proceed?
		</p>
	</div>
	<div class="modal-footer">
		<a class="btn btn-primary">Proceed with revert</a>
		<a class="btn btn-danger">Cancel</a>
	</div>
</div>

        

        
        <style>
	.macro-embedly {
		display: block;
	}

	.macro-math {
		display: inline-block;
	}

	.macro-video {
		display: block;
	}

	.responsive-object {
		position: relative;
		padding-bottom: 56.25%;
		height: 0;
		margin: 10px 0;
		overflow: hidden;
	}

	.responsive-object iframe,
	.responsive-object object,
	.responsive-object embed {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	}

	.iframely-responsive {
		top: 0;
		left: 0;
		width: 100%;
		height: 0;
		position: relative;
		padding-bottom: 56.25%;
	}
	.iframely-responsive>* {
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		position: absolute;
		border: 0;
	}

	@media only screen and (min-width: 1200px) {
		.page-content > .macro-embedly > .responsive-object,
		.comment-media > .embedly-link > .responsive-object {
			padding-bottom: 43.35%;
		}
	}

	@media only screen and (max-width: 667px) {
		.audiojs {
			width: 100%;

		}
		.audiojs .scrubber {
			width: 160px;
		}
	}

	@media only screen and (max-width: 320px) {
		.audiojs .scrubber {
			width: 100px;
		}
	}
</style>

<script type="text/javascript" src="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/lib/audiojs/audio.min.js"></script>

<script type="text/javascript">
	var initMacros;

JS.require( 'jQuery', 'API', 'Utilities', function() {
	initMacros = function( ) {
		// check if iframely is loaded
		var omitScript = window.iframely ? '&omit_script=1' : '';

		$('.macro-embedly').each(function() {
			var $this = $(this);
			var url = $(this).data('url');
			var link = $('<a/>').attr('href', url).text(url);

			$this.html(link);
			$.ajax({
				dataType: 'json',
				// MD5 hash of the iframely API KEY
				url: 'https://iframe.ly/api/oembed?iframe=1&lazy=1&omit_css=1' + omitScript + '&maxwidth=700&url=' + encodeURIComponent(url) + '&key=d84fd7201524f3ea0333c77b9a3dc776'
			}).done(function(obj) {
				// wrapper for setting max width/height
				var div = $('<div></div>');
				var css = {
					'max-width': '700px'
					// 'height': obj.type === 'video' ? '394px' : '100%',
				};
				div.css(css);
				div.html(obj.html);
				$this.replaceWith(div);
				if (window.iframely) {
					window.iframely.load();
				}
			});
		});

		$('.macro-math').each(function() {
			var latex = $(this).data('latex');
			var link = $('<img/>').attr('src', 'http://latex.codecogs.com/gif.latex?' + latex);
			$(this).html(link);
		});

		$('.macro-pozible').each(function() {
			var collectionId = $(this).data('collectionId');
			var url = $(this).data('url');
			var width = $(this).data('width');
			var height = $(this).data('height');
			if (url.lastIndexOf('https://www.pozible.com/widget/collection/') === 0) {
				var $newContents = $('<iframe/>').attr('frameborder', 0).attr('scrolling', 'no').attr('width', width).attr('height', height).attr('src', url);
				$(this).replaceWith($newContents);
			}
		});

		$('.macro-externallink').each(function() {
			var url = encodeURIComponent($(this).data('url'));
			var $that = $(this);
			API.get('macro/external/', { 'url': url }).done(function(result) {
				if (result.success) {
					$that.html(result.content);
				} else {
					$that.html($('<div/>').html('This content is not available. Please try the link directly: ' + url));
				}
			}).fail(function() {
				$that.html($('<div/>').html('This content is not available. Please try the link directly: ' + url));
			});
		});

		$('.macro-video').each(function() {
			var url = encodeURIComponent($(this).data('url'));
			var width = $(this).data('width');
			var height = $(this).data('height');
			var $that = $(this);
			var ratio = ((height/Math.max($('#course-page-content').width(), width))*100).toPrecision(4) + '%';

			API.get('macro/video/', { 'width': width, 'height': height, 'videoUrl': url }).done(function(result) {
				$that.html(result.embedVideoHTML);
				$that.find('.responsive-object').css('padding-bottom',ratio);
			}).fail(function() {
				$that.html($('<div/>').html('This video is not available.'));
			});

		});

		$('.macro-container').each(function() {
			var $container = $(this);
			var containerType = $container.data('type') || 'container-rounded';
			var $contents = $container.contents();

			var $newContents = $('<div/>').addClass(containerType).append($contents.clone());

			$contents.replaceWith($newContents);
		});

		$('.macro-audio').each(function() {
			var $audio = $(this);
			var url = $audio.data('url');
			if (!/^(f|ht)tps?:\/\//i.test(url)) {
				url = 'https://www.openlearning.com/' + $audio.data('url') + '?action=download';
			}

			var $audioElement = $('<div>').append($('<audio>').attr('src', url).attr('preload', 'none'));
			$audioElement.append($('<a/>').attr('href', url).text('Download this audio file.'));
			$audio.append($audioElement);
		});
		audiojs.events.ready(function() { var as = audiojs.createAll(); });

		$('.macro-user-content').each(function() {
			var $element = $(this);
			var url = $element.attr('data-url');
			var elementType = $element.attr('data-element');
			var keyPath = $element.attr('data-path');
			var scheme = $element.attr('data-scheme');
			var content = $element.attr('data-content');

			$element.css({
				'display': 'inline'
			});

			var getData = {};

			if (keyPath) {
				getData.path = keyPath;
			}

			if (scheme) {
				getData.scheme = scheme;
			}

			API.get('page/userToken/', getData).done(function(response) {
				var token, cohort, dashedCohort;

				token = response.token;
				cohort = response.cohort;

				if (!token) {
					token = 'default';
				}

				if (!cohort) {
					cohort = 'default';
				}

				dashedCohort = cohort.replace(/\//g, '-');

				if (!url) {
					url = '#';
				} else {
					url = url.replace(/\~token\~/g, token);
					url = url.replace(/\~class\~/g, cohort);
					url = url.replace(/\~classdashed\~/g, dashedCohort);
				}

				if (!content) {
					content = url;
				} else {
					content = content.replace(/\~token\~/g, token);
					content = content.replace(/\~class\~/g, cohort);
					content = content.replace(/\~classdashed\~/g, dashedCohort);
				}

				var $replacement;
				if (elementType == 'image') {
					$replacement = $('<img>')
						.attr({
							'src': url,
							'alt': content
						});
				} else if (elementType == 'hyperlink') {
					$replacement = $('<a>')
						.attr({
							'href': url,
							'target': '_blank'
						})
						.text(content);
				} else {
					$replacement = $('<span>')
						.text(content);
				}

				$element.html($replacement);
			});
		});

		$('.macro-subpages').each(function() {

			var $subpages = $(this);
			var path = $subpages.data('path');
			var sort = $subpages.data('sort');

			if (sort != null && sort.length > 0) {
				sort = '?sort=' + sort;
			} else {
				sort = '';
			}

			API.get('page/' + path + '/subpages' + sort).done(function(res) {
				var $subpageTable = $('<table class="table table-hover table-condensed subpages-table"><thead><tr><th>Page</th><th class="last-update">Last Updated</th></tr></thead><tbody></tbody></table>');

				for (var i = 0; i < res.subpages.length; i++) {
					var lastUpdate = res.subpages[i].lastUpdate;
					if (lastUpdate) {
						lastUpdate = Utilities.formatTimestamp(lastUpdate, "%d %b %Y, %H:%M:%S");
					} else {
						lastUpdate = "N/A";
					}
					$subpageTable.append(
						$('<tr/>').append(
							$('<td/>').append(
								$('<a/>').attr('href', res.subpages[i].url).text(res.subpages[i].title)
							),
							$('<td/>').addClass('last-update').text(lastUpdate)
						)
					);
				}

				$subpages.append($subpageTable);
			});
		});

		var revealToggle = function( ) {
			var $spoiler = $(this).parents('.macro-spoiler');
			$spoiler.find('.spoiler-tag').toggleClass('spoiler-tag-displayed');
			$spoiler.find('.spoiler-reveal').toggle();
			$spoiler.find('.spoiler-content').slideToggle( "fast" );
			$spoiler.toggleClass('spoiler-displayed');
			$spoiler.find('.spoiler-tag-hide').toggle();
			return false;
		};

		$('.macro-spoiler').each(function() {
			var $spoiler = $(this);
			var title = $spoiler.data('title') || "Spoiler!";
			var $contents = $spoiler.contents();
			var $newContents = $(document.createDocumentFragment());

			$newContents.append($('<div class="spoiler-reveal"></div>').append($('<a href="#"><i>Click to Reveal</i></a>')).click(revealToggle));
			$newContents.append($('<div>').attr('class', 'spoiler-content').append($contents.clone()));
			$newContents.append($('<div>').attr('class', 'spoiler-tag').append(title).click(revealToggle));
			$newContents.append($('<div class="spoiler-tag-hide hide"><a href="#"><i class="icon-caret-up"></i></a></div>').click(revealToggle));

			if ($contents.length) {
				$contents.replaceWith($newContents);
			} else {
				$spoiler.append($newContents);
			}
		});
	};

	$(document).ready(initMacros);

});
</script>

        

        <script type="text/javascript">
        JS.require('PageMetricsOverlay', 'jQuery', function() {
            $(function() {
                var pageMetrics = new PageMetricsOverlay();
                $('#overlayPageMetrics').click(function() {
                    if (pageMetrics.visible) {
                        pageMetrics.hide();
                    } else {
                        pageMetrics.load();
                    }
                    return false;
                });
            });
        });
        </script>
        <script type="text/javascript">
        JS.require( 'jQuery', function( ) {
            $(document).ready( function( ) {
                // check if iframely is loaded
                var omitScript = window.iframely ? '&omit_script=1' : '';
                $('.embedLink a').each(function() {
                    var $this = $(this);
                    var url = $this.attr('href');
                    $.ajax({
                        dataType: 'json',
                        // MD5 hash of the iframely API KEY
                        url: 'https://iframe.ly/api/oembed?iframe=1&lazy=1&omit_css=1' + omitScript + '&maxwidth=700&url=' + encodeURIComponent(url) + '&key=d84fd7201524f3ea0333c77b9a3dc776'
                    }).done(function(obj) {
                        // wrapper for setting max width/height
                        var div = $('<div></div>');
                        var css = {
                            'max-width': '700px'
                            // 'height': obj.type === 'video' ? '394px' : '100%',
                        };
                        div.css(css);
                        div.html(obj.html);
                        $this.replaceWith(div);
                        if (window.iframely) {
                          window.iframely.load();
                        }
                    });
                });
            });
        });
        </script>
    

    

    
 
    <style>
	.macro-embedly {
		display: block;
	}

	.macro-math {
		display: inline-block;
	}

	.macro-video {
		display: block;
	}

	.responsive-object {
		position: relative;
		padding-bottom: 56.25%;
		height: 0;
		margin: 10px 0;
		overflow: hidden;
	}

	.responsive-object iframe,
	.responsive-object object,
	.responsive-object embed {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	}

	.iframely-responsive {
		top: 0;
		left: 0;
		width: 100%;
		height: 0;
		position: relative;
		padding-bottom: 56.25%;
	}
	.iframely-responsive>* {
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		position: absolute;
		border: 0;
	}

	@media only screen and (min-width: 1200px) {
		.page-content > .macro-embedly > .responsive-object,
		.comment-media > .embedly-link > .responsive-object {
			padding-bottom: 43.35%;
		}
	}

	@media only screen and (max-width: 667px) {
		.audiojs {
			width: 100%;

		}
		.audiojs .scrubber {
			width: 160px;
		}
	}

	@media only screen and (max-width: 320px) {
		.audiojs .scrubber {
			width: 100px;
		}
	}
</style>

<script type="text/javascript" src="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/lib/audiojs/audio.min.js"></script>

<script type="text/javascript">
	var initMacros;

JS.require( 'jQuery', 'API', 'Utilities', function() {
	initMacros = function( ) {
		// check if iframely is loaded
		var omitScript = window.iframely ? '&omit_script=1' : '';

		$('.macro-embedly').each(function() {
			var $this = $(this);
			var url = $(this).data('url');
			var link = $('<a/>').attr('href', url).text(url);

			$this.html(link);
			$.ajax({
				dataType: 'json',
				// MD5 hash of the iframely API KEY
				url: 'https://iframe.ly/api/oembed?iframe=1&lazy=1&omit_css=1' + omitScript + '&maxwidth=700&url=' + encodeURIComponent(url) + '&key=d84fd7201524f3ea0333c77b9a3dc776'
			}).done(function(obj) {
				// wrapper for setting max width/height
				var div = $('<div></div>');
				var css = {
					'max-width': '700px'
					// 'height': obj.type === 'video' ? '394px' : '100%',
				};
				div.css(css);
				div.html(obj.html);
				$this.replaceWith(div);
				if (window.iframely) {
					window.iframely.load();
				}
			});
		});

		$('.macro-math').each(function() {
			var latex = $(this).data('latex');
			var link = $('<img/>').attr('src', 'http://latex.codecogs.com/gif.latex?' + latex);
			$(this).html(link);
		});

		$('.macro-pozible').each(function() {
			var collectionId = $(this).data('collectionId');
			var url = $(this).data('url');
			var width = $(this).data('width');
			var height = $(this).data('height');
			if (url.lastIndexOf('https://www.pozible.com/widget/collection/') === 0) {
				var $newContents = $('<iframe/>').attr('frameborder', 0).attr('scrolling', 'no').attr('width', width).attr('height', height).attr('src', url);
				$(this).replaceWith($newContents);
			}
		});

		$('.macro-externallink').each(function() {
			var url = encodeURIComponent($(this).data('url'));
			var $that = $(this);
			API.get('macro/external/', { 'url': url }).done(function(result) {
				if (result.success) {
					$that.html(result.content);
				} else {
					$that.html($('<div/>').html('This content is not available. Please try the link directly: ' + url));
				}
			}).fail(function() {
				$that.html($('<div/>').html('This content is not available. Please try the link directly: ' + url));
			});
		});

		$('.macro-video').each(function() {
			var url = encodeURIComponent($(this).data('url'));
			var width = $(this).data('width');
			var height = $(this).data('height');
			var $that = $(this);
			var ratio = ((height/Math.max($('#course-page-content').width(), width))*100).toPrecision(4) + '%';

			API.get('macro/video/', { 'width': width, 'height': height, 'videoUrl': url }).done(function(result) {
				$that.html(result.embedVideoHTML);
				$that.find('.responsive-object').css('padding-bottom',ratio);
			}).fail(function() {
				$that.html($('<div/>').html('This video is not available.'));
			});

		});

		$('.macro-container').each(function() {
			var $container = $(this);
			var containerType = $container.data('type') || 'container-rounded';
			var $contents = $container.contents();

			var $newContents = $('<div/>').addClass(containerType).append($contents.clone());

			$contents.replaceWith($newContents);
		});

		$('.macro-audio').each(function() {
			var $audio = $(this);
			var url = $audio.data('url');
			if (!/^(f|ht)tps?:\/\//i.test(url)) {
				url = 'https://www.openlearning.com/' + $audio.data('url') + '?action=download';
			}

			var $audioElement = $('<div>').append($('<audio>').attr('src', url).attr('preload', 'none'));
			$audioElement.append($('<a/>').attr('href', url).text('Download this audio file.'));
			$audio.append($audioElement);
		});
		audiojs.events.ready(function() { var as = audiojs.createAll(); });

		$('.macro-user-content').each(function() {
			var $element = $(this);
			var url = $element.attr('data-url');
			var elementType = $element.attr('data-element');
			var keyPath = $element.attr('data-path');
			var scheme = $element.attr('data-scheme');
			var content = $element.attr('data-content');

			$element.css({
				'display': 'inline'
			});

			var getData = {};

			if (keyPath) {
				getData.path = keyPath;
			}

			if (scheme) {
				getData.scheme = scheme;
			}

			API.get('page/userToken/', getData).done(function(response) {
				var token, cohort, dashedCohort;

				token = response.token;
				cohort = response.cohort;

				if (!token) {
					token = 'default';
				}

				if (!cohort) {
					cohort = 'default';
				}

				dashedCohort = cohort.replace(/\//g, '-');

				if (!url) {
					url = '#';
				} else {
					url = url.replace(/\~token\~/g, token);
					url = url.replace(/\~class\~/g, cohort);
					url = url.replace(/\~classdashed\~/g, dashedCohort);
				}

				if (!content) {
					content = url;
				} else {
					content = content.replace(/\~token\~/g, token);
					content = content.replace(/\~class\~/g, cohort);
					content = content.replace(/\~classdashed\~/g, dashedCohort);
				}

				var $replacement;
				if (elementType == 'image') {
					$replacement = $('<img>')
						.attr({
							'src': url,
							'alt': content
						});
				} else if (elementType == 'hyperlink') {
					$replacement = $('<a>')
						.attr({
							'href': url,
							'target': '_blank'
						})
						.text(content);
				} else {
					$replacement = $('<span>')
						.text(content);
				}

				$element.html($replacement);
			});
		});

		$('.macro-subpages').each(function() {

			var $subpages = $(this);
			var path = $subpages.data('path');
			var sort = $subpages.data('sort');

			if (sort != null && sort.length > 0) {
				sort = '?sort=' + sort;
			} else {
				sort = '';
			}

			API.get('page/' + path + '/subpages' + sort).done(function(res) {
				var $subpageTable = $('<table class="table table-hover table-condensed subpages-table"><thead><tr><th>Page</th><th class="last-update">Last Updated</th></tr></thead><tbody></tbody></table>');

				for (var i = 0; i < res.subpages.length; i++) {
					var lastUpdate = res.subpages[i].lastUpdate;
					if (lastUpdate) {
						lastUpdate = Utilities.formatTimestamp(lastUpdate, "%d %b %Y, %H:%M:%S");
					} else {
						lastUpdate = "N/A";
					}
					$subpageTable.append(
						$('<tr/>').append(
							$('<td/>').append(
								$('<a/>').attr('href', res.subpages[i].url).text(res.subpages[i].title)
							),
							$('<td/>').addClass('last-update').text(lastUpdate)
						)
					);
				}

				$subpages.append($subpageTable);
			});
		});

		var revealToggle = function( ) {
			var $spoiler = $(this).parents('.macro-spoiler');
			$spoiler.find('.spoiler-tag').toggleClass('spoiler-tag-displayed');
			$spoiler.find('.spoiler-reveal').toggle();
			$spoiler.find('.spoiler-content').slideToggle( "fast" );
			$spoiler.toggleClass('spoiler-displayed');
			$spoiler.find('.spoiler-tag-hide').toggle();
			return false;
		};

		$('.macro-spoiler').each(function() {
			var $spoiler = $(this);
			var title = $spoiler.data('title') || "Spoiler!";
			var $contents = $spoiler.contents();
			var $newContents = $(document.createDocumentFragment());

			$newContents.append($('<div class="spoiler-reveal"></div>').append($('<a href="#"><i>Click to Reveal</i></a>')).click(revealToggle));
			$newContents.append($('<div>').attr('class', 'spoiler-content').append($contents.clone()));
			$newContents.append($('<div>').attr('class', 'spoiler-tag').append(title).click(revealToggle));
			$newContents.append($('<div class="spoiler-tag-hide hide"><a href="#"><i class="icon-caret-up"></i></a></div>').click(revealToggle));

			if ($contents.length) {
				$contents.replaceWith($newContents);
			} else {
				$spoiler.append($newContents);
			}
		});
	};

	$(document).ready(initMacros);

});
</script>


    <script charset="utf-8">
        JS.require('Facebook', function(Facebook) {
            Facebook.load();
        });
    </script>

    <section class="page-section first-page-section">
        <div class="container">
            <div class="row">
                <div class="span12">
                    <div id="non-course-page-content" style="padding:0px;"><a name="overview"></a>
                        <div id="page-header-container">
                            <div class="course-banner-container teamimagewrap tall-banner" style="position: relative;">
                                <a href="https://www.openlearning.com/unswcourses/courses/COMP9331">
                                    <div class="ribbonwrapper">
                                    <div class="ribbon-wrapper-blue" style="z-index: 10;">
                                        
                                    </div>
                                    <div id="course-banner-link" style="cursor: pointer; width: 100%; height: 100%; position: absolute;">
                                        <div id="course-banner">
                                        
                                        </div>
                                    </div>
                                    </div>
                                </a>
                                
                            </div>
                        </div>
                        <div id="landing-page-content-area">
                        
                            <div class="row-fluid">
                                <div id="content-area-column1" class="span9">
                                
                                    
                                    <img alt="Image for COMP9331 Computer Networks &amp; Applications" src="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/images/default_promo_still.jpg" style="width:100%">
                                    
                                
                                    <div class="row-fluid pad30">
                                        <div class="span12"><a name="video"></a>
                                        
                                            <div class="course-summary">
                                                <p>A brief summary of the course...</p>
                                            </div>
                                            <br><br>
                                        </div>
                                    </div>
                                    
                                    <div class="clearfix"></div><a name="team"></a>
                                    <div class="pad30" style="overflow:hidden">
                                        <h1 class="heading"><span>The Team</span></h1>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/salil.kanhere"><img src="https://openlearning-cdn.s3.amazonaws.com/salil.kanhere-avatar-48-ts1481861925.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/salil.kanhere">salil kanhere</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">1124 kudos</span></p>
                                            <blockquote>I have taught a variety of computing subjects in my 10+ years at UNSW. I love to work on cool research related to the Internet of Things, pervasive and mobile c...</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/altuz.nicholas"><img src="https://openlearning-cdn.s3.amazonaws.com/altuz.nicholas-avatar-48-ts1488023733.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/altuz.nicholas">Nicholas Mulianto</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">95 kudos</span></p>
                                            <blockquote>Full time student, part time nerd and tutor....</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/arashsh"><img src="https://openlearning-cdn.s3.amazonaws.com/arashsh-avatar-48-ts1456965804.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/arashsh">Arash Shaghaghi</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">71 kudos</span></p>
                                            <blockquote>Current Role:
I'm the course administrator for Comp3331/9331 in S2, 2017.
 
Brief Bio:
I’m a PhD Candidate at Networked Systems and Security Group (NetSyS) and...</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/alidorri"><img src="https://openlearning-cdn.s3.amazonaws.com/alidorri-avatar-48-ts1482974187.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/alidorri">Ali Dorri</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">66 kudos</span></p>
                                            <blockquote>I am a Ph.D. student in the school  of computer science and engineering. Currently, I am working on Blockchain and Internet of Things for my research. I am also...</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/nurulhusniyah"><img src="https://openlearning-cdn.s3.amazonaws.com/nurulhusniyah-avatar-48-ts1473755261.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/nurulhusniyah">Nurul Husniyah</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">61 kudos</span></p>
                                            <blockquote>Hye,just call me Niya....</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/posadaedtech"><img src="https://openlearning-cdn.s3.amazonaws.com/posadaedtech-avatar-48-ts1435805857.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/posadaedtech">John Paul Posada</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">32 kudos</span></p>
                                            <blockquote>Hello everyone, I'm a teacher for this course and I can't wait to learn with all of you.</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/s.a.hoseini"><img src="https://openlearning-cdn.s3.amazonaws.com/s.a.hoseini-avatar-48-ts1488183410.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/s.a.hoseini">sahoseini</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">15 kudos</span></p>
                                            <blockquote>I am third year Ph.D. student in computer science and engineering. My research area is wireless networking (currently focused on cellular network and 5G) under...</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/a.fotouhi"><img src="https://openlearning-cdn.s3.amazonaws.com/a.fotouhi-avatar-48-ts1487897666.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/a.fotouhi">Azade</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">12 kudos</span></p>
                                            <blockquote>I am a PhD student at University of New South Wales, school of computer science and engineering. Currently I am working on Mobile communication and next generat...</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/lyncollins"><img src="https://openlearning-cdn.s3.amazonaws.com/lyncollins-avatar-48-ts1448250035.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/lyncollins">Lyn Collins</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">3 kudos</span></p>
                                            <blockquote>Hello everyone, I'm a teacher for this course and I can't wait to learn with all of you.</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/sidraa.malik"><img src="https://openlearning-cdn.s3.amazonaws.com/sidraa.malik-avatar-48-ts1489037953.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/sidraa.malik">Sidra Malik</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">3 kudos</span></p>
                                            <blockquote>Hello everyone, I'm a teacher for this course and I can't wait to learn with all of you.</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/sanjay.jha"><img src="https://openlearning-cdn.s3.amazonaws.com/sanjay.jha-avatar-48-ts1500813395.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/sanjay.jha">sanjayjha</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">2 kudos</span></p>
                                            <blockquote>I am a full professor in CSE  bringing over 25 years of teaching  experience. I am an active researcher in the areas of networking and cybersecurity. You can fi...</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/jin.zhang1"><img src="https://openlearning-cdn.s3.amazonaws.com/jin.zhang1-avatar-48-ts1488279858.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/jin.zhang1">Jin Zhang</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">0 kudos</span></p>
                                            <blockquote>Jin Zhang is currently pursuing Postgraduate Research(PhD) in Wireless Networking domain under the supervision of Salil Kanhere and Wen Hu, in the School of Com...</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/lilaazouz"><img src="https://openlearning-cdn.s3.amazonaws.com/lilaazouz-avatar-48-ts1488248837.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/lilaazouz">Lila Azouz</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">0 kudos</span></p>
                                            <blockquote>Hello everyone, I'm a teacher for this course and I can't wait to learn with all of you.</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/hui.huang"><img src="https://openlearning-cdn.s3.amazonaws.com/hui.huang-avatar-48-ts1488245493.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/hui.huang">huihuang</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">0 kudos</span></p>
                                            <blockquote>Hui Huang was graduated form Beijing University of Technology in 2010, he then received the MSc in computing science from the University of Glasgow, UK in 2013....</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/minjie.shen"><img src="https://openlearning-cdn.s3.amazonaws.com/minjie.shen-avatar-48-ts1487908620.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/minjie.shen">minjieshen</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">0 kudos</span></p>
                                            <blockquote>Hello everyone, I'm a teacher for this course and I can't wait to learn with all of you.</blockquote>
                                            </div>
                                        </div>
                                        
                                        <div class="span5 niceProfileDisplay">
                                            <a href="/u/s.mumtaz"><img src="https://openlearning-cdn.s3.amazonaws.com/s.mumtaz-avatar-48-ts1487899640.jpg" align="left" style="top:0;" class="img-polaroid"></a>
                                            <div style="margin-left: 70px;height: 128px;"><p><a href="/u/s.mumtaz">smumtaz</a> &nbsp; &nbsp; &nbsp; <span class="icon-star"></span> <span style="color: #666;">0 kudos</span></p>
                                            <blockquote>Hello everyone, I'm a teacher for this course and I can't wait to learn with all of you.</blockquote>
                                            </div>
                                        </div>
                                        
                                    </div>
                                    
                                    
                                    <div class="clearfix"></div><a name="community"></a>
                                    <div class="pad30" style="overflow:hidden">
                                        <h1 class="heading"><span>The Community</span></h1>
                                        <div style="text-align:center">
                                            <h4 class="soft-title"><span class="icon icon-user"></span> 272 Students &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="icon icon-comments"></span> 2000 Comments</h4>
                                        </div>
                                        <div id="studentsList" class="follower-list"></div>
                                        
                                    </div>
                                    
                                    
                                    <div class="clearfix"></div><a name="reviews"></a>
                                    <div class="pad30">
                                        <div id="ct-read-review-widget" data-course="https://www.openlearning.com/unswcourses/courses/COMP9331"></div><script src="https://coursetalk-cdn.s3.amazonaws.com/s/js/widgets/read-review-widget-openlearning.js"></script>
                                    </div>
                                    
                                    <div class="clearfix"></div><a name="information"></a>
                                    <div class="pad30" style="overflow:hidden">
                                        <h1 class="heading"><span>More Information</span></h1>
                                        
                                        <p>Any further information you wish to show non-enrolled visitors...</p>
                                    </div>
                                    
                                    <div class="clearfix"></div><a name="related"></a>
                                    <div class="pad30" style="overflow:hidden">
                                        <h1 class="heading"><span>Related Courses</span></h1>
                                        <div id="relatedCoursesList"></div>
                                    </div>
                                    
                                    
                                    <div id="jointhecourse" class="modal hide" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="background-color: rgba(0,0,0,0.7);">
                                        <div class="modal-header">
                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                                            <h3 id="myModalLabel">Join COMP9331 Computer Networks &amp; Applications</h3>
                                        </div>
                                        <div class="modal-body">
                                            

<script type="text/javascript" charset="utf-8">
    JS.require( 'jQuery', '$.fn.tooltip', function() {
        $(document).ready( function() {
            // this will send a postMessage to parent in case this is shown in an iframe which means the user is not logged in
            var targetDomain = 'https://www.openlearning.com';
            var message = {
                method: 'register'
            };
            window.parent.postMessage(JSON.stringify(message), targetDomain);

            function makeName( full_name ) {
                return full_name.toLowerCase( ).replace( /[^a-zA-Z ]/g, "" ).replace( / /g, "" );
            }

            function autoUsername( ) {
                $("#profileName").val( makeName( $("#fullName").val( ) ) );
            }

            $("#fullName").keyup( function ( event ) {
                if ( !$("#profileName").data( "touched" ) ) {
                    autoUsername( );
                    $('#profileNameContainer').show();
                }
            } );

            $("#profileName").keyup( function ( event ) {
                if ( $(this).val( ).length == 0 || $(this).val( ) == makeName( $("#fullName").val( ) ) ) {
                    $(this).data( "touched", false );
                } else {
                    $(this).data( "touched", true );
                }
                $('#profileName').val(makeName($('#profileName').val()));
            } );

            $("#profileName").focus( function ( event ) {
                if ( !$(this).data( "touched" ) ) {
                }
            } );

            $("#profileName").focusout( function ( event ) {
                if ( $(this).val( ).length == 0 ) {
                    autoUsername( );
                }
            } );
        });
    });
</script>




    <div>
        <div class="row-fluid">
            
            <div class="span6 signup-area">
                <form action="https://www.openlearning.com/accounts/register/" method="post" accept-charset="utf-8" class="form-horizontal" id="registrationForm" style="margin-bottom:0;">

                <input type="hidden" name="redirectTo" value="">
                <div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='CQZYT9b5LfYbfz4SvmvLRLtYN8CEOJpe' /></div>
                
                <input type="text" id="fullName" name="fullName" value="" placeholder="Your full name" style="width: 100%;border-top-left-radius: 2px !important;border-top-right-radius: 2px !important;" class="largeInput"  data-placement="right">
                

                
                   <input type="text" id="profileName" name="profileName" value="" placeholder="Your profile name" style="width: 100%;" class="largeInput"  data-placement="right">
                
                   
                
                         
                             <input type="email" id="emailAddress" name="emailAddress" value="" placeholder="Your email address" style="width: 100%;" class="largeInput"  data-placement="right">
                           
                
                         
                             <input type="password" id="password" name="password" placeholder="Your password" style="width: 100%;" class="largeInput"  data-placement="right">
                          
                
                <div class="registerInfo" style="border-bottom-left-radius: 2px !important;border-bottom-right-radius: 2px !important;">
                    <label for="acceptTerms">
                        <input type="checkbox" name="acceptTerms" id="acceptTerms" value="1"> &nbsp; Accept our <a href="https://www.openlearning.com/PrivacyPolicy">Privacy Policy</a> and <a href="https://www.openlearning.com/TermsOfService">Terms</a>
                    </label>
                </div>                
                
                
                <input type="submit" class="btn btn-success" id="registrationButton" style="margin:20px 0 0 0;box-sizing:border-box;padding:10px 0;font-size: 18px;border-radius: 2px; width:100%; box-shadow: none; text-transform: inherit" value="Join the course &raquo;">
                </form>
            </div>
            
            
            
        </div>
        
    </div>



                                        </div>
                                    </div>

                                    

                                    <div id="landing-bottom"></div>
                                </div>
                                <div class="span3">
                                    <div id="landing-top" style="position:relative">
                                        <div id="course-enrol-bar">
                                            <div class="course-information">
                                                <div class="row-fluid">
                                                    <div class="span12">
                                                        
                                                        <h2 class="heading">COMP9331 Computer Networks &amp; Applications</h2>
                                                    
                                                        <div>
                                                            <p>
                                                            
                                                                
                                                                <span class="icon-calendar-empty icon"></span> Status: On now
                                                                
                                                            
                                                            </p>
                                                            
                                                            
                                                            <p>
                                                                <span class="icon-user icon"></span> Students: 272
                                                            </p>
                                                            
                                                            
                                                            
                                                        </div>
                                                        
                                                        
                                                        <form action="https://www.openlearning.com/courses/enrol/" id="enrol-course-form" method="post" accept-charset="utf-8" style="z-index: 100;">
                                                            
                                                                <div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='CQZYT9b5LfYbfz4SvmvLRLtYN8CEOJpe' /></div>
                                                                <input type="hidden" name="course" value="unswcourses/courses/COMP9331">
                                                                <input type="hidden" name="enrol" value="1">
                                                                
                                                            
                                                            <div>
                                                            
                                                                <button type="submit" class="btn join-course-btn ripple">Join the course</button>
                                                            
                                                            </div>
                                                        </form>
                                                        
                                                    
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script type="application/json" id="course-landing-page-data">
        {
            "mediaURL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/",
            "coursePath": "unswcourses/courses/COMP9331",
            "showLanding": true,
            "previewMode": false,
            "randomUsers": [{"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/sanjay.jha-avatar-24-ts1500813397.jpg", "standardAvatarPath": "sanjay.jha-avatar-48-ts1500813395.jpg", "userId": "5955bc18044f851a0eaed324", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/sanjay.jha-avatar-48-ts1500813395.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/sanjay.jha-avatar-120-ts1500813399.jpg", "profileName": "sanjay.jha", "fullName": "sanjayjha"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/xiangyuzhu-avatar-24-ts1490951464.jpg", "standardAvatarPath": "xiangyuzhu-avatar-48-ts1490951461.jpg", "userId": "58bc9fee5aa80a35d0a48c50", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/xiangyuzhu-avatar-48-ts1490951461.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/xiangyuzhu-avatar-120-ts1490951466.jpg", "profileName": "xiangyuzhu", "fullName": "Xiangyu Zhu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/mohamadismailibrahim-avatar-24-ts1488757149.jpg", "standardAvatarPath": "mohamadismailibrahim-avatar-48-ts1488757139.jpg", "userId": "58bc07509279a1093dff77b0", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/mohamadismailibrahim-avatar-48-ts1488757139.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/mohamadismailibrahim-avatar-120-ts1488757153.jpg", "profileName": "mohamadismailibrahim", "fullName": "Mohamad Ismail Ibrahim"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/yiminghe-avatar-24-ts1495637137.jpg", "standardAvatarPath": "yiminghe-avatar-48-ts1495637125.jpg", "userId": "58bba61d9279a14cc6ff77e5", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/yiminghe-avatar-48-ts1495637125.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/yiminghe-avatar-120-ts1495637141.jpg", "profileName": "yiminghe", "fullName": "Yiming He"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/ethan.xu-avatar-24-ts1488845965.jpg", "standardAvatarPath": "ethan.xu-avatar-48-ts1488845956.jpg", "userId": "58b8a9ce5aa80a1841fbe193", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/ethan.xu-avatar-48-ts1488845956.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/ethan.xu-avatar-120-ts1488845969.jpg", "profileName": "ethan.xu", "fullName": "Ethan Xu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/michellphan-avatar-24-ts1489753569.jpg", "standardAvatarPath": "michellphan-avatar-48-ts1489753560.jpg", "userId": "58b7d23aba5e65610dc788b7", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/michellphan-avatar-48-ts1489753560.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/michellphan-avatar-120-ts1489753574.jpg", "profileName": "michellphan", "fullName": "Michelle Phan"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/rongfachen-avatar-24-ts1488521053.jpg", "standardAvatarPath": "rongfachen-avatar-48-ts1488521051.jpg", "userId": "58b7c9fc117bd04611b7b8d7", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/rongfachen-avatar-48-ts1488521051.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/rongfachen-avatar-120-ts1488521056.jpg", "profileName": "rongfachen", "fullName": "rongfa"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/chenweihuang-avatar-24-ts1488887686.jpg", "standardAvatarPath": "chenweihuang-avatar-48-ts1488887676.jpg", "userId": "58b6aec326f81b21943d74de", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/chenweihuang-avatar-48-ts1488887676.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/chenweihuang-avatar-120-ts1488887691.jpg", "profileName": "chenweihuang", "fullName": "Chenwei Huang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/brontekalebic-avatar-24-ts1489405025.jpg", "standardAvatarPath": "brontekalebic-avatar-48-ts1489405015.jpg", "userId": "58b6addecc50f83bba18e2ba", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/brontekalebic-avatar-48-ts1489405015.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/brontekalebic-avatar-120-ts1489405030.jpg", "profileName": "brontekalebic", "fullName": "Bronte Kalebic"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/xingshizhang-avatar-24-ts1488588320.jpg", "standardAvatarPath": "xingshizhang-avatar-48-ts1488588311.jpg", "userId": "58b69fe8cc50f817f718e2a2", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/xingshizhang-avatar-48-ts1488588311.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/xingshizhang-avatar-120-ts1488588325.jpg", "profileName": "xingshizhang", "fullName": "Xingshi Zhang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/tysonchan-avatar-24-ts1488330628.jpg", "standardAvatarPath": "tysonchan-avatar-48-ts1488330620.jpg", "userId": "58b618b9cc50f850e7c9f8e2", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/tysonchan-avatar-48-ts1488330620.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/tysonchan-avatar-120-ts1488330633.jpg", "profileName": "tysonchan", "fullName": "Tyson Chan"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/meisili-avatar-24-ts1488340309.jpg", "standardAvatarPath": "meisili-avatar-48-ts1488340299.jpg", "userId": "58b613a2044f85374ab521e7", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/meisili-avatar-48-ts1488340299.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/meisili-avatar-120-ts1488340314.jpg", "profileName": "meisili", "fullName": "Meisi Li"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/reidkyla-avatar-24-ts1488325662.jpg", "standardAvatarPath": "reidkyla-avatar-48-ts1488325652.jpg", "userId": "58b6084b9279a1751a7a4a72", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/reidkyla-avatar-48-ts1488325652.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/reidkyla-avatar-120-ts1488325667.jpg", "profileName": "reidkyla", "fullName": "Kyla Reid"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/elevnlee-avatar-24-ts1488285546.jpg", "standardAvatarPath": "elevnlee-avatar-48-ts1488285537.jpg", "userId": "58b515adba5e656dd8b616a9", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/elevnlee-avatar-48-ts1488285537.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/elevnlee-avatar-120-ts1488285551.jpg", "profileName": "elevnlee", "fullName": "Elevn Li"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/xianglii-avatar-24-ts1496539338.jpg", "standardAvatarPath": "xianglii-avatar-48-ts1496539336.jpg", "userId": "58b50b57ba5e6548a220c174", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/xianglii-avatar-48-ts1496539336.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/xianglii-avatar-120-ts1496539340.jpg", "profileName": "xianglii", "fullName": "Xiang Li"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/shaochizhou-avatar-24-ts1488598538.jpg", "standardAvatarPath": "shaochizhou-avatar-48-ts1488598529.jpg", "userId": "58b50795ba5e653c0e20c166", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/shaochizhou-avatar-48-ts1488598529.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/shaochizhou-avatar-120-ts1488598544.jpg", "profileName": "shaochizhou", "fullName": "Shaochi Zhou"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/yufeizhang-avatar-24-ts1488440138.jpg", "standardAvatarPath": "yufeizhang-avatar-48-ts1488440129.jpg", "userId": "58b507219279a1411476b649", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/yufeizhang-avatar-48-ts1488440129.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/yufeizhang-avatar-120-ts1488440143.jpg", "profileName": "yufeizhang", "fullName": "Yufei Zhang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/hoikichow-avatar-24-ts1488510474.jpg", "standardAvatarPath": "hoikichow-avatar-48-ts1488510470.jpg", "userId": "58b4e83e9279a149cc400048", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/hoikichow-avatar-48-ts1488510470.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/hoikichow-avatar-120-ts1488510479.jpg", "profileName": "hoikichow", "fullName": "Hoi Ki Chow"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/yirongchen-avatar-24-ts1488712427.jpg", "standardAvatarPath": "yirongchen-avatar-48-ts1488712425.jpg", "userId": "58b4dafc5aa80a4c16bd6b0c", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/yirongchen-avatar-48-ts1488712425.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/yirongchen-avatar-120-ts1488712432.jpg", "profileName": "yirongchen", "fullName": "Yirong Chen"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/qiuyang57-avatar-24-ts1488335334.jpg", "standardAvatarPath": "qiuyang57-avatar-48-ts1488335321.jpg", "userId": "58b4da335aa80a486ebd6b3e", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/qiuyang57-avatar-48-ts1488335321.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/qiuyang57-avatar-120-ts1488335340.jpg", "profileName": "qiuyang57", "fullName": "Yang Qiu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/yanshengliu-avatar-24-ts1488765076.jpg", "standardAvatarPath": "yanshengliu-avatar-48-ts1488765066.jpg", "userId": "58b4d68426f81b146474f27c", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/yanshengliu-avatar-48-ts1488765066.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/yanshengliu-avatar-120-ts1488765079.jpg", "profileName": "yanshengliu", "fullName": "Yansheng Liu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/openlearner17s1-avatar-24-ts1490011046.jpg", "standardAvatarPath": "openlearner17s1-avatar-48-ts1490011037.jpg", "userId": "58b4befacc50f85b1a58a9bf", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/openlearner17s1-avatar-48-ts1490011037.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/openlearner17s1-avatar-120-ts1490011050.jpg", "profileName": "openlearner17s1", "fullName": "Clinton Huynh"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/yuanjieyang-avatar-24-ts1488713028.jpg", "standardAvatarPath": "yuanjieyang-avatar-48-ts1488713017.jpg", "userId": "58b4be09ba5e6574005b4c9f", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/yuanjieyang-avatar-48-ts1488713017.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/yuanjieyang-avatar-120-ts1488713033.jpg", "profileName": "yuanjieyang", "fullName": "Yuanjie Yang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/batchat-avatar-24-ts1488277890.jpg", "standardAvatarPath": "batchat-avatar-48-ts1488277880.jpg", "userId": "58b4b35826f81b2305545384", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/batchat-avatar-48-ts1488277880.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/batchat-avatar-120-ts1488277895.jpg", "profileName": "batchat", "fullName": "Tony Bao"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/natashawai-avatar-24-ts1488367679.jpg", "standardAvatarPath": "natashawai-avatar-48-ts1488367676.jpg", "userId": "58b4b029117bd07d3ae100a2", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/natashawai-avatar-48-ts1488367676.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/natashawai-avatar-120-ts1488367683.jpg", "profileName": "natashawai", "fullName": "Natasha Wai"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/chenjianniu-avatar-24-ts1488333798.jpg", "standardAvatarPath": "chenjianniu-avatar-48-ts1488333789.jpg", "userId": "58b4af88ba5e65451fd558a3", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/chenjianniu-avatar-48-ts1488333789.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/chenjianniu-avatar-120-ts1488333802.jpg", "profileName": "chenjianniu", "fullName": "Chenjian Niu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/awsum-avatar-24-ts1488388653.jpg", "standardAvatarPath": "awsum-avatar-48-ts1488388650.jpg", "userId": "58b46dcd26f81b501e545394", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/awsum-avatar-48-ts1488388650.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/awsum-avatar-120-ts1488388657.jpg", "profileName": "awsum", "fullName": "Henry Sihavong"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/kundong-avatar-24-ts1488198616.jpg", "standardAvatarPath": "kundong-avatar-48-ts1488198607.jpg", "userId": "58b3f67bcc50f80e580088b5", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/kundong-avatar-48-ts1488198607.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/kundong-avatar-120-ts1488198621.jpg", "profileName": "kundong", "fullName": "KUN DONG"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/tingmei-avatar-24-ts1488772904.jpg", "standardAvatarPath": "tingmei-avatar-48-ts1488772895.jpg", "userId": "58b3e64d5aa80a4935fa2b44", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/tingmei-avatar-48-ts1488772895.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/tingmei-avatar-120-ts1488772909.jpg", "profileName": "tingmei", "fullName": "Ting Mei"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/ajayprakash-avatar-24-ts1488329044.jpg", "standardAvatarPath": "ajayprakash-avatar-48-ts1488329034.jpg", "userId": "58b3d996ba5e653b35d55883", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/ajayprakash-avatar-48-ts1488329034.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/ajayprakash-avatar-120-ts1488329050.jpg", "profileName": "ajayprakash", "fullName": "Ajay Prakash"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/adrian-so-avatar-24-ts1488619677.jpg", "standardAvatarPath": "adrian-so-avatar-48-ts1488619674.jpg", "userId": "58b3c975044f850aced59c6f", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/adrian-so-avatar-48-ts1488619674.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/adrian-so-avatar-120-ts1488619682.jpg", "profileName": "adrian-so", "fullName": "Adrian So"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/guangyuanyao-avatar-24-ts1488237484.jpg", "standardAvatarPath": "guangyuanyao-avatar-48-ts1488237474.jpg", "userId": "58b3abd0044f852364d59c6c", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/guangyuanyao-avatar-48-ts1488237474.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/guangyuanyao-avatar-120-ts1488237489.jpg", "profileName": "guangyuanyao", "fullName": "Gary Yao"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/shuxiangzhang-avatar-24-ts1488157076.jpg", "standardAvatarPath": "shuxiangzhang-avatar-48-ts1488157073.jpg", "userId": "58b3785bcc50f8519400893b", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/shuxiangzhang-avatar-48-ts1488157073.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/shuxiangzhang-avatar-120-ts1488157080.jpg", "profileName": "shuxiangzhang", "fullName": "Shuxiang Zhang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/jordanfodera-avatar-24-ts1488155376.jpg", "standardAvatarPath": "jordanfodera-avatar-48-ts1488155367.jpg", "userId": "58b37133117bd02bc3e10089", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/jordanfodera-avatar-48-ts1488155367.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/jordanfodera-avatar-120-ts1488155381.jpg", "profileName": "jordanfodera", "fullName": "Jordan Fodera"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/weisong-avatar-24-ts1488327213.jpg", "standardAvatarPath": "weisong-avatar-48-ts1488327204.jpg", "userId": "58b35adfba5e65705da43ad3", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/weisong-avatar-48-ts1488327204.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/weisong-avatar-120-ts1488327218.jpg", "profileName": "weisong", "fullName": "Wei Song"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/megankurz-avatar-24-ts1488325805.jpg", "standardAvatarPath": "megankurz-avatar-48-ts1488325795.jpg", "userId": "58b356fd9279a1022e5dfa68", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/megankurz-avatar-48-ts1488325795.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/megankurz-avatar-120-ts1488325810.jpg", "profileName": "megankurz", "fullName": "Megan Kurz"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/jieyanliang-avatar-24-ts1496812862.jpg", "standardAvatarPath": "jieyanliang-avatar-48-ts1496812860.jpg", "userId": "58b2b444cc50f804db912319", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/jieyanliang-avatar-48-ts1496812860.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/jieyanliang-avatar-120-ts1496812864.jpg", "profileName": "jieyanliang", "fullName": "Jieyan Liang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/andrewxu-avatar-24-ts1492967739.jpg", "standardAvatarPath": "andrewxu-avatar-48-ts1492967737.jpg", "userId": "58b2b04c5aa80a5fe7b151ef", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/andrewxu-avatar-48-ts1492967737.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/andrewxu-avatar-120-ts1492967742.jpg", "profileName": "andrewxu", "fullName": "Andrew Xu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/xuecongzang-avatar-24-ts1488932223.jpg", "standardAvatarPath": "xuecongzang-avatar-48-ts1488932221.jpg", "userId": "58b2a20bba5e654b56a43af4", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/xuecongzang-avatar-48-ts1488932221.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/xuecongzang-avatar-120-ts1488932227.jpg", "profileName": "xuecongzang", "fullName": "Xuecong Zang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/lyl123-avatar-24-ts1488092589.jpg", "standardAvatarPath": "lyl123-avatar-48-ts1488092579.jpg", "userId": "58b27816044f853d354af40d", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/lyl123-avatar-48-ts1488092579.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/lyl123-avatar-120-ts1488092594.jpg", "profileName": "lyl123", "fullName": "Xingyu Li"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/ruchiang-avatar-24-ts1488288318.jpg", "standardAvatarPath": "ruchiang-avatar-48-ts1488288308.jpg", "userId": "58b238a39279a1186d5dfa44", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/ruchiang-avatar-48-ts1488288308.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/ruchiang-avatar-120-ts1488288323.jpg", "profileName": "ruchiang", "fullName": "Cheng Ru Chiang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/chenguo-avatar-24-ts1493840784.jpg", "standardAvatarPath": "chenguo-avatar-48-ts1493840782.jpg", "userId": "58b214a5044f857ec2e08c78", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/chenguo-avatar-48-ts1493840782.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/chenguo-avatar-120-ts1493840787.jpg", "profileName": "chenguo", "fullName": "Chen Guo"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/chinkymutreja-avatar-24-ts1488595560.jpg", "standardAvatarPath": "chinkymutreja-avatar-48-ts1488595558.jpg", "userId": "58b1759bcc50f828b58e641c", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/chinkymutreja-avatar-48-ts1488595558.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/chinkymutreja-avatar-120-ts1488595566.jpg", "profileName": "chinkymutreja", "fullName": "Chinky Mutreja"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/zhuochenn-avatar-24-ts1488702822.jpg", "standardAvatarPath": "zhuochenn-avatar-48-ts1488702820.jpg", "userId": "58b17494117bd079aea6c6ac", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/zhuochenn-avatar-48-ts1488702820.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/zhuochenn-avatar-120-ts1488702827.jpg", "profileName": "zhuochenn", "fullName": "Zhuo Chen"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/yimingwang-avatar-24-ts1488237020.jpg", "standardAvatarPath": "yimingwang-avatar-48-ts1488237011.jpg", "userId": "58b162e75aa80a6b8a93651b", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/yimingwang-avatar-48-ts1488237011.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/yimingwang-avatar-120-ts1488237022.jpg", "profileName": "yimingwang", "fullName": "Yiming Wang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/jinchengliu-avatar-24-ts1488238523.jpg", "standardAvatarPath": "jinchengliu-avatar-48-ts1488238513.jpg", "userId": "58b160e29279a10bc5ab8546", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/jinchengliu-avatar-48-ts1488238513.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/jinchengliu-avatar-120-ts1488238528.jpg", "profileName": "jinchengliu", "fullName": "Jincheng Liu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/eternalthinker-avatar-24-ts1488286713.jpg", "standardAvatarPath": "eternalthinker-avatar-48-ts1488286702.jpg", "userId": "58b1605bba5e656e4191a0d8", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/eternalthinker-avatar-48-ts1488286702.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/eternalthinker-avatar-120-ts1488286718.jpg", "profileName": "eternalthinker", "fullName": "Rahul Anand"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/danielnguyen13189-avatar-24-ts1493874778.jpg", "standardAvatarPath": "danielnguyen13189-avatar-48-ts1493874775.jpg", "userId": "58b13f7426f81b4e45b0c839", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/danielnguyen13189-avatar-48-ts1493874775.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/danielnguyen13189-avatar-120-ts1493874780.jpg", "profileName": "danielnguyen13189", "fullName": "Daniel Nguyen"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/wuzongheng-avatar-24-ts1494257346.jpg", "standardAvatarPath": "wuzongheng-avatar-48-ts1494257344.jpg", "userId": "58b126ff5aa80a3bcf936513", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/wuzongheng-avatar-48-ts1494257344.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/wuzongheng-avatar-120-ts1494257349.jpg", "profileName": "wuzongheng", "fullName": "Wu Zongheng"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/nurfaizuddinnordin-avatar-24-ts1496900455.jpg", "standardAvatarPath": "nurfaizuddinnordin-avatar-48-ts1496900453.jpg", "userId": "58b126bcba5e65530b91a0a2", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/nurfaizuddinnordin-avatar-48-ts1496900453.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/nurfaizuddinnordin-avatar-120-ts1496900457.jpg", "profileName": "nurfaizuddinnordin", "fullName": "Nur Faizuddin Nordin"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/jeremyfu1-avatar-24-ts1489128129.jpg", "standardAvatarPath": "jeremyfu1-avatar-48-ts1489128125.jpg", "userId": "58b113895aa80a025b936509", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/jeremyfu1-avatar-48-ts1489128125.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/jeremyfu1-avatar-120-ts1489128134.jpg", "profileName": "jeremyfu1", "fullName": "Jeremy Fu"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/saurabhdanielsamuel-avatar-24-ts1488410004.jpg", "standardAvatarPath": "saurabhdanielsamuel-avatar-48-ts1488409995.jpg", "userId": "58b10c94044f855fd4e08bd0", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/saurabhdanielsamuel-avatar-48-ts1488409995.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/saurabhdanielsamuel-avatar-120-ts1488410009.jpg", "profileName": "saurabhdanielsamuel", "fullName": "Saurabh Daniel Samuel"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/mengqizhang-avatar-24-ts1488340545.jpg", "standardAvatarPath": "mengqizhang-avatar-48-ts1488340542.jpg", "userId": "58b10549117bd02db5a6c6bb", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/mengqizhang-avatar-48-ts1488340542.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/mengqizhang-avatar-120-ts1488340550.jpg", "profileName": "mengqizhang", "fullName": "Mengqi Zhang"}, {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/xiaochenhan-avatar-24-ts1488594712.jpg", "standardAvatarPath": "xiaochenhan-avatar-48-ts1488594703.jpg", "userId": "58b103b8cc50f86f298e6409", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/xiaochenhan-avatar-48-ts1488594703.jpg", "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/xiaochenhan-avatar-120-ts1488594716.jpg", "profileName": "xiaochenhan", "fullName": "Xiaochen Han"}],
            "relatedCourses": [{"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/kutay-avatar-24-ts1447294923.jpg", "standardAvatarPath": "kutay-avatar-48-ts1447294922.jpg", "userId": "5643f7cacc50f81bce9edf27", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/kutay-avatar-48-ts1447294922.jpg", "karma": 0, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/kutay-avatar-120-ts1447294925.jpg", "profileName": "kutay", "fullName": "Cat"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__courses_allysupport__course-promo-image-1467610843.06.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "OL", "title": "Other"}, "courseSummary": "ALLY@UNSW is a network that promotes understanding and inclusive practice around\u00a0sex and gender diversity at UNSW.\nThis module introduces the role of an ALLY in", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/courses/allysupport", "students": null, "startDateISO": null, "path": "courses/allysupport", "landingPage": {"show": "video", "image": "course__courses_allysupport__course-landing-image-1449205765.23.jpg", "summary": "<p>ALLY@UNSW is a network that promotes understanding and inclusive practice around\u00a0sex and gender diversity at UNSW.</p>\n<p>This module introduces the role of an ALLY in providing support for students and staff</p>\n<p>It will focus on the frameworks of legislative protections and anti-discrimination issues around sex and gender diversity, and provide stories from around Australia and the Univeristy to present the LGBTQI experience.</p>", "content": "<p>For more information about ALLY@UNSW;\u00a0ALLY contacts ,online resources and\u00a0face to face training dates to become an ALLY</p>\n<p>visit: \u00a0<a href=\"http://www.ally.unsw.edu.au\" target=\"_blank\">www.ally.unsw.edu.au</a></p>\n<p>Please like our <a href=\"https://www.facebook.com/ally.unsw.edu.au\" target=\"_blank\">ALLY page on Facebook</a></p>", "video": "https://www.youtube.com/watch?v=xn6ubm1IHys", "commentsEnabled": false, "still": "course__courses_allysupport__course-landing-still-1449206646.04.jpg"}, "relatedCourseItem": true, "categoryIcon": ["icon-star", "#ffffff", "#000000"], "homeFeatured": false, "name": "ALLY@UNSW Introduction to LGBTIQ diversity and protections", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/catkutay-avatar-24-ts1476569260.jpg", "standardAvatarPath": "catkutay-avatar-48-ts1476569257.jpg", "userId": "528df05ab919662b177d8ba2", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/catkutay-avatar-48-ts1476569257.jpg", "karma": 1, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/catkutay-avatar-120-ts1476569262.jpg", "profileName": "catkutay", "fullName": "Cat Kutay"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__courses_culturalintelligence__course-promo-image-1462858100.71.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "LANG", "title": "Language and Communication"}, "courseSummary": "Acknowledgement of this country\nThe Open Minds: Don't Assume course, as a public meeting and training space, acknowledges the traditional owners and Elders past", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/courses/culturalintelligence", "students": null, "startDateISO": null, "path": "courses/culturalintelligence", "landingPage": {"content": "<p><strong>Why do this course?</strong></p>\n<p>In line with the UNSW 2025 Strategy of Internationally engaged education, the University is developing courses to engage staff and students with the cultural diversity of our University and prepare them for the global working environment.\u00a0The aim of cultural intelligence training is to provide the tools and discussions to enable you\u00a0to:</p>\n<ul>\n<li>Develop awareness and respect for others</li>\n<li>Understand how cultural biases frame all of our interactions</li>\n<li>Improve communication</li>\n<li>Appreciate the value of diversity and difference</li>\n<li>Develop self-awareness and skills to identify your own cultural biases and institutional cultural gaps</li>\n<li>Improve responsiveness to others\u00a0within your role at the university as a staff member or student</li>\n<li>Learn how to develop culturally sensitive practice and apply the skills to your life, work and learning</li>\n<li>Improve your value and flexibility in a global learning and workplace context</li>\n</ul>\n<p>We hope you enjoy the exercises, videos from our contributors and the material we have collected and developed for you.\u00a0</p>\n<p>But first we want you to understand that an\u00a0understanding of culture is something you can develop at any age, by understanding yourself and how your own culture and\u00a0values develop.</p>", "commentsEnabled": true, "still": "course__courses_culturalintelligence__course-landing-still-1449928676.98.jpg", "show": "still", "summary": "<p><strong>Acknowledgement of this country</strong></p>\n<p>The Open Minds: Don't Assume course, as a public meeting and training space, acknowledges the traditional owners and Elders past and present across Australia, with particular acknowledgment to the\u00a0<a href=\"https://en.wikipedia.org/wiki/Cadigal\" style=\"color:rgb(42, 93, 176);\" target=\"_blank\">Gadigal</a>,\u00a0<a href=\"https://en.wikipedia.org/wiki/Tharawal\" style=\"color:rgb(42, 93, 176);\" target=\"_blank\">Dharawal</a>,\u00a0<a href=\"https://en.wikipedia.org/wiki/Bidjigal\" style=\"color:rgb(42, 93, 176);\" target=\"_blank\">Bidjigal</a>,\u00a0<a href=\"https://en.wikipedia.org/wiki/Wangal\" style=\"color:rgb(42, 93, 176);\" target=\"_blank\">Wangal</a>\u00a0and\u00a0<a href=\"https://en.wikipedia.org/wiki/Darug\" style=\"color:rgb(42, 93, 176);\" target=\"_blank\">Dharug</a>\u00a0Nations, the traditional owners of the lands around Sydney where our offices are located.</p>\n<p><strong>Welcome to Open Minds Don't Assume\u00a0</strong>- this is the\u00a0<strong>Cultural Intelligence Course</strong></p>"}, "relatedCourseItem": true, "categoryIcon": ["icon-comments", "#000000", "#cc0000"], "homeFeatured": false, "name": "Culture Matters", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/catkutay-avatar-24-ts1476569260.jpg", "standardAvatarPath": "catkutay-avatar-48-ts1476569257.jpg", "userId": "528df05ab919662b177d8ba2", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/catkutay-avatar-48-ts1476569257.jpg", "karma": 1, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/catkutay-avatar-120-ts1476569262.jpg", "profileName": "catkutay", "fullName": "Cat Kutay"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__courses_diversityandracism__course-promo-image-1448497946.18.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "OL", "title": "Other"}, "courseSummary": "How do we train people in Cultural Intelligence or Awareness to reduce racism and improve understanding of diversity?\nThere are many different factors to be con", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/courses/diversityandracism", "students": null, "startDateISO": null, "path": "courses/diversityandracism", "landingPage": {"content": "<p>Any further information you wish to show non-enrolled visitors...</p>", "commentsEnabled": true, "still": "course__courses_diversityandracism__course-landing-still-1448497971.58.jpg", "summary": "<p>How do we train people in Cultural Intelligence or Awareness to reduce racism and improve understanding of diversity?</p>\n<p>There are many different factors to be considered in diversity. Racism, gender identity and disability are some aspects we will deal with.</p>\n<p>We have collected interviews from people who work with Culutral Awareness training, Racism and Diversity and ALLY programs.</p>\n<p>These terms have a lot of different meanings to people, so we will start by defining each of these concepts.</p>\n<p>Here are some of the questions we will be dealing with in this course:</p>\n<p>What is cultural intelligence and how is this represented in people's behaviour?</p>\n<p>Racism ? What is racism about really? Is there such a thing as race? What are we referring to?</p>\n<p>And how can we deal with racism in its many forms?</p>\n<p>To fully understand diversity what are the issues we need to consider for LGBTIQA people?</p>", "show": "still"}, "relatedCourseItem": true, "categoryIcon": ["icon-star", "#ffffff", "#000000"], "homeFeatured": false, "name": "Open Minds Don't Assume: Racism Matters", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/clareellisally-studentequity-avatar-24-ts1442970419.jpg", "standardAvatarPath": "clareellisally-studentequity-avatar-48-ts1442970416.jpg", "userId": "5601fb27cc50f82ca0262e0c", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/clareellisally-studentequity-avatar-48-ts1442970416.jpg", "karma": 0, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/clareellisally-studentequity-avatar-120-ts1442970423.jpg", "profileName": "clareellisally-studentequity", "fullName": "Clare Ellis Ally-studentequity"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__courses_openmindsdontassume__course-promo-image-1487139071.34.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "OL", "title": "Other"}, "courseSummary": "Racism has a lot of different meanings to people, so we will start by defining this concept. We have collected some interviews from people who work with Racism", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/courses/openmindsdontassume", "students": null, "startDateISO": null, "path": "courses/openmindsdontassume", "landingPage": {"show": "video", "image": "course__courses_openmindsdontassume__course-landing-image-1447292798.7.jpg", "summary": "<p>Racism has a lot of different meanings to people, so we will start by defining this concept. We have collected some interviews from people who work with Racism and Diversity.</p>\n<p>Here are some of the questions we will be dealing with in this course:</p>\n<p>Racism ? What is racism about really? Is there such a thing as race? What are we referring to?</p>\n<p>And how can we deal with racism in its many forms?</p>\n<p>How do we train people in Cultural Intelligence or Awareness to reduce racism and improve understanding of diversity?</p>\n<p>To fully understand diversity what are the issues we need to consider for LGBTIQA people?</p>", "content": "<p>Any further information you wish to show non-enrolled visitors...</p>", "video": "https://youtu.be/tXT16qgjtWE", "commentsEnabled": true, "still": "course__courses_openmindsdontassume__course-landing-still-1442970794.85.jpg"}, "relatedCourseItem": true, "categoryIcon": ["icon-star", "#ffffff", "#000000"], "homeFeatured": false, "name": "Open Minds: Don't Assume", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/abrimo-avatar-24-ts1364188160.jpg", "standardAvatarPath": "abrimo-avatar-48-ts1364188159.jpg", "userId": "4eb20e92759b741acf000000", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/abrimo-avatar-48-ts1364188159.jpg", "karma": 991, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/abrimo-avatar-120-ts1435115963.jpg", "profileName": "abrimo", "fullName": "Adam Brimo"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__unswcourses_courses_2017HS1917__course-promo-image-1487676065.49.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "ENG", "title": "Engineering"}, "courseSummary": "Welcome to UNSW HS1917 for 2017!\u00a0\n\u00a0\n\u00a0\nTo start the course enter the activation code you were given in lectures.", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/unswcourses/courses/2017HS1917", "students": null, "startDateISO": null, "path": "unswcourses/courses/2017HS1917", "landingPage": {"content": "<p>Any further information you wish to show non-enrolled visitors...</p>", "still": "course__unswcourses_courses_2017HS1917__course-landing-still-1487676099.69.jpg", "show": "still", "summary": "<p>Welcome to UNSW HS1917 for 2017!\u00a0</p>\n<p>\u00a0</p>\n<p>\u00a0</p>\n<p>To start the course enter the activation code you were given in lectures.</p>"}, "relatedCourseItem": true, "categoryIcon": ["icon-cogs", "#000000", "#76cf67"], "homeFeatured": false, "name": "HS1917 Enhanced Computing", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-24-ts1443419680.jpg", "standardAvatarPath": "melinda.garcia-avatar-48-ts1443419678.jpg", "userId": "50c12d1b78f2f25e95000030", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-48-ts1443419678.jpg", "karma": 189, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-120-ts1443419682.jpg", "profileName": "melinda.garcia", "fullName": "Melinda Garcia"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__unswcourses_courses_acct3303__course-promo-image-1498452457.63.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "BUS", "title": "Business and Economics"}, "courseSummary": "A brief summary of the course...", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/unswcourses/courses/acct3303", "students": null, "startDateISO": null, "path": "unswcourses/courses/acct3303", "landingPage": {"content": "<p>Any further information you wish to show non-enrolled visitors...</p>", "still": "course__unswcourses_courses_acct3303__course-landing-still-1498451975.67.jpg", "summary": "<p>A brief summary of the course...</p>", "show": "still"}, "relatedCourseItem": true, "categoryIcon": ["icon-dollar", "#000000", "#cc0000"], "homeFeatured": false, "name": "ACCT3303 Industry Placement 3", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/john.shepherd-avatar-24-ts1350266212.jpg", "standardAvatarPath": "john.shepherd-avatar-48-ts1350266212.jpg", "userId": "4f3d89d7e694aa0e69000003", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/john.shepherd-avatar-48-ts1350266212.jpg", "karma": 474, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/john.shepherd-avatar-120-ts1435116489.jpg", "profileName": "john.shepherd", "fullName": "John Shepherd"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__unswcourses_courses_COMP9311__course-promo-image-1481672863.18.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "TECH", "title": "Computers and Technology"}, "courseSummary": "A brief summary of the course...", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/unswcourses/courses/COMP9311", "students": null, "startDateISO": null, "path": "unswcourses/courses/COMP9311", "landingPage": {"content": "<p>Any further information you wish to show non-enrolled visitors...</p>", "show": "still", "summary": "<p>A brief summary of the course...</p>"}, "relatedCourseItem": true, "categoryIcon": ["icon-rocket", "#000000", "#ffd700"], "homeFeatured": false, "name": "COMP9311 Database Systems", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-24-ts1443419680.jpg", "standardAvatarPath": "melinda.garcia-avatar-48-ts1443419678.jpg", "userId": "50c12d1b78f2f25e95000030", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-48-ts1443419678.jpg", "karma": 189, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-120-ts1443419682.jpg", "profileName": "melinda.garcia", "fullName": "Melinda Garcia"}, "studentPrice": null, "image": "https://openlearning-cdn.s3.amazonaws.com/course__unswcourses_courses_COMP9311_2__course-promo-image-1488253829.04.jpg", "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "ENG", "title": "Engineering"}, "courseSummary": "A brief summary of the course...", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/unswcourses/courses/COMP9311_2", "students": null, "startDateISO": null, "path": "unswcourses/courses/COMP9311_2", "landingPage": {"content": "<p>Any further information you wish to show non-enrolled visitors...</p>", "summary": "<p>A brief summary of the course...</p>", "show": "still"}, "relatedCourseItem": true, "categoryIcon": ["icon-cogs", "#000000", "#76cf67"], "homeFeatured": false, "name": "COMP9311 Database Systems", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}, {"startDate": null, "randomStudents": [], "alreadyStarted": true, "creator": {"smallAvatar": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-24-ts1443419680.jpg", "standardAvatarPath": "melinda.garcia-avatar-48-ts1443419678.jpg", "userId": "50c12d1b78f2f25e95000030", "standardAvatar": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-48-ts1443419678.jpg", "karma": 189, "avatar@3x": "https://openlearning-cdn.s3.amazonaws.com/melinda.garcia-avatar-120-ts1443419682.jpg", "profileName": "melinda.garcia", "fullName": "Melinda Garcia"}, "studentPrice": null, "image": null, "currency": null, "paidCohort": false, "duration": null, "showPrivate": "", "category": {"code": "ENG", "title": "Engineering"}, "courseSummary": "A brief summary of the course...", "progress": null, "selfPaced": null, "courseUrl": "https://www.openlearning.com/unswcourses/courses/comp9331-s2", "students": null, "startDateISO": null, "path": "unswcourses/courses/comp9331-s2", "landingPage": {"content": "<p>Any further information you wish to show non-enrolled visitors...</p>", "summary": "<p>A brief summary of the course...</p>", "show": "still"}, "relatedCourseItem": true, "categoryIcon": ["icon-cogs", "#000000", "#76cf67"], "homeFeatured": false, "name": "COMP9331 - Semester 2 Computer Networks and Applications", "karma": null, "MEDIA_URL": "https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/"}],
            "totalStudents": 272,
            "showType": "still",
            "sharingWidget": "",
            "sharingPageWidget": "",
            "referredBy": null,
            "enrolled": false,
            "invitePoints": "",
            "inviteUserFans": "",
            "imageIndex": ""
        }
    </script>
    

<!-- START CHUNK moment -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/moment.a8f0e7b81b24ee2e57ba.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK moment -->

    

<!-- START CHUNK courselandingpage -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/courselandingpage.218162e9696ee983fd71.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK courselandingpage -->

    

    
        
            
        <footer class="footer">
            <section class="footerwidgetarea">
                <div class="footerwidgetcontainer">
                    <div class="footerwidgetinnercontainer">
                        <div class="footerwidget">
                            <h3>About Us</h3>
                            <ul>
                                <li>
                                    <a href="https://www.openlearning.com/About">What is OpenLearning?</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/Team">The Team</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/Pedagogy">Pedagogy</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/blog">Blog</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/press">Press</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/contact">Contact</a>
                                </li>
                            </ul>
                        </div>

                        <div class="footerwidget">
                            <h3>FAQs</h3>
                             <ul>
                                <li>
                                    <a href="https://www.openlearning.com/help">Help &amp; Support</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/help/technical/api">
                                        <span style="display: inline-block;">Developers</span>
                                        /
                                        <span style="display: inline-block;">APIs</span>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/pricing">Pricing</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/TermsOfService">Terms of Service</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/PrivacyPolicy">Privacy Policy</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/jobs">Jobs</a>
                                </li>
                            </ul>
                        </div>

                        <div class="footerwidget">
                            <h3>Explore</h3>
                             <ul>
                                <li>
                                    <a href="https://www.openlearning.com/courses/">All Courses</a>
                                </li>
                                <li>
                                    <a href="/courses/type/highereducation">University Courses</a>
                                </li>
                                <li>
                                    <a href="/courses/type/professionaldevelopment">Skills-based Courses</a>
                                </li>
                                <li>
                                    <a href="/courses/type/lifestyle">Lifestyle Courses</a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/teach"><b>Teach a Course</b></a>
                                </li>
                                <li>
                                    <a href="https://www.openlearning.com/institution/create">Create an Institution</a>
                                </li>
                            </ul>
                        </div>
                        <div class="footerwidget" style="margin-bottom: 0;">
                            <h3>Stay in Touch</h3>
                            <ul>
                                <li>
                                    <a href="https://www.openlearning.com/thankyou">Your Stories</a>
                                </li>
                                <li><a href="https://facebook.com/OpenLearning" target="_Blank" title="Follow us on Facebook"><span style="display:inline-block;width: 20px;"><i class="icon-facebook"></i></span> Facebook</a>
                                </li>
                                <li>
                                    <a href="https://twitter.com/openlrning" target="_Blank" title="Follow us on Twitter"><span style="display:inline-block;width: 20px;"><i class="icon-twitter"></i></span> Twitter</a>
                                </li>
                                <li>
                                    <a href="http://www.weibo.com/OpenLearningAu" target="_Blank" title="Be concerned about us on Weibo"><span style="display:inline-block;width: 20px;"><i class="icon-weibo"></i></span> Weibo</a>
                                </li>
                                <li>
                                    <a href="http://au.linkedin.com/company/open-learning" target="_Blank" title="Follow us on Linked In"><span style="display:inline-block;width: 20px;"><i class="icon-linkedin"></i></span> LinkedIn</a>
                                </li>
                                <li>
                                    <a href="https://www.instagram.com/openlearning_global" target="_Blank" title="Follow us on Instagram"><span style="display:inline-block;width: 20px;"><i class="icon-instagram"></i></span> Instagram</a>
                                </li>
                                <li>
                                    <!-- <a href="#">Newsletter</a> -->
                                    <form method="post" action="https://openlearningcom.createsend.com/t/i/s/aykr/" id="subscribe-form" style="margin-bottom: 0; margin-top: 0;">
                                        <input name="cm-aykr-aykr" id="aykr-aykr" type="email" placeholder="Your Email" style="font-size: 14px; height: 34px; border: 1px solid #ccc;margin-bottom:10px;" class="largeInput">
                                        <input type="hidden" name="cm-fo-qaid" value="243954">
                                        <input type="hidden" name="cm-fo-qaih" value="243956">
                                        <input type="submit" class="btn btn-success ripple" value="Subscribe">
                                    </form>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>
            <!-- Widget Area -->
            <div class="container">
                <!-- Copyright & Social Area -->
                <div class="row">
                    <div class="span12 text-center copyright">
                        <p>&copy;2012-2017 Open Learning Global Pty Ltd. </p>
                        
                    </div>
                </div>
                <!-- Copyright & Social Area -->
            </div>
        </footer>
        

<!-- START CHUNK footer -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/footer.a9027b34201af7fb3cf6.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK footer -->

        
        
    

    
    <script>

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-27113294-1']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>
    


    <script src="https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/new/js/custom.js"></script>
    <script type="text/javascript">
    JS.require('jQuery', 'API', 'dust_helpers', function() {
        var HEADER_BAR_HEIGHT = 35;
        var $window = $(window);
        var $coursesDropdownMenu = $('#courses-dropdown');
        function resizeCoursesMenu() {
            $coursesDropdownMenu.css('max-height', $window.height() - HEADER_BAR_HEIGHT - 20); // arbitrary padding from bottom
        }
        var $coursesDropdown = $coursesDropdownMenu.parent();
        $coursesDropdown.on('click', function() {
            if (!$coursesDropdown.hasClass('open')) {
                olFuture.collapseFutureDropdowns();
            }
            if (!$coursesDropdown.hasClass('dropdownDataLoaded')) {
                $coursesDropdown.addClass('dropdownDataLoaded');
                $.ajaxSetup({ 'cache': true });
                $.getScript('https://openlearning.scdn5.secure.raxcdn.com/media-46c79b0/lib/dust/compiled_templates/page.dust').done(function() {
                    API.get('users/enrolledCourseListing').done(function(res) {
                        var courseDropdownData = {
                            'myCourses': res.myCourses,
                            'myInstitutions': res.myInstitutions,
                            'hasCourses': (res.myCourses.length > 0),
                            'hasInstitutions': (res.myInstitutions.length > 0)
                        };
                        dust.render('courseDropdownMenu', courseDropdownData, function(err, html) {
                            $('#courses-dropdown').prepend($(html));
                            $('.courseHeadMenu').click(function (e) {
                                e.preventDefault();
                                e.stopPropagation();

                                var $this = $(this);

                                $('.courseHeadMenu').not($this).removeClass('highlight');
                                $this.toggleClass('highlight');
                                console.log($(this).attr('data-course'));
                                $('.courseCohortDropdownItem').not('[data-course="' + $(this).attr('data-course') + '"]').removeClass('expanded');
                                $('.courseCohortDropdownItem[data-course="' + $(this).attr('data-course') + '"]').toggleClass('expanded');
                            });
                            $coursesDropdown.find('.course-dropdown-loading').addClass('hide');
                        });
                    }).fail(function() {
                        $coursesDropdown.removeClass('dropdownDataLoaded');
                        $coursesDropdown.find('.course-dropdown-loading').text("Please reload the page and try again.");
                    });
                });
            }

        });

        var $profileDropdown = $('#profile-dropdown').parent();
        $profileDropdown.on('click', function() {
            if (!$profileDropdown.hasClass('open')) {
                olFuture.collapseFutureDropdowns();
            }
        });

        $(window).on('resize', resizeCoursesMenu);
        resizeCoursesMenu();
    });
    </script>

    

    
        <script type="text/javascript">
            JS.require('jQuery', '$.pnotify', 'jstz', 'API', function($) {
                $(function() {
                    var settingsURL = 'https://www.openlearning.com/accounts/account-settings/';

                    var timezonesMismatch = (OpenLearningUserData.timezoneOffset !== -(new Date().getTimezoneOffset()));
                    var newTimezone = jstz.determine().name();

                    var shouldWarn;
                    try {
                        shouldWarn = (sessionStorage.getItem('hushTimezoneWarning') != '1');
                    } catch (err) {
                        shouldWarn = false;
                    }

                    if (location.href !== settingsURL && timezonesMismatch) {
                        API.post('users/timezone', {timezone: newTimezone}).done(function(result) {
                            if (!result.isSaved && shouldWarn) {
                                $.pnotify({
                                    title: "Timezone has changed.",
                                    text: "\nYour current timezone is set to:\n" + OpenLearningUserData.timezone + " but you are now in " + newTimezone + ".\n" +
                                            "You can change timezone settings in your <a href='" + settingsURL + "' target='_blank'>account settings</a>\n",
                                    before_open: function($pnotify) {
                                        $pnotify.css('top', 45);
                                    },
                                    after_close: function($pnotify) {
                                        try {
                                            sessionStorage.setItem('hushTimezoneWarning', '1');
                                        } catch (err) {
                                            // no session storage or out of space
                                        }
                                    }
                                });
                            }
                        });
                    }
                });
            });
        </script>
    
</div>


    <div id="desktop-chat">
        <div id="desktop-chat-container"></div>
    </div>
    
        

<!-- START CHUNK chat -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/chat.d7e6a720441568d82138.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK chat -->

    



    <div id="mobile-left-panel" class="mobile-slide-panel visible-phone">
        <ul class="mobile-user-menu">
        
            <li class="mobile-nav-search">
                <form action="https://www.openlearning.com/search/" method="get" accept-charset="utf-8">
                    <input type="text" name="q" value="" placeholder="Search...">
                    <input type="hidden" name="course" value="unswcourses/courses/COMP9331">
                </form>
            </li>

            <!--Contextual navigation-->
            
                <!--Contextual nav available in courseBase.html and profile/main.html-->
            


            <!--Global nav - Profile-->
            <li class="mobile-nav-heading">My Profile</li>
            <li>
                <a class="mobile-nav-link" href="https://www.openlearning.com/u/brian.lam">
                    <img src="https://openlearning-cdn.s3.amazonaws.com/brian.lam-avatar-48-ts1476971072.jpg">
                    Brian Lam
                </a>
            </li>

            <!--Global nav - Links to courses-->
            <li class="mobile-nav-heading" id="mobile-coursedropdown-menu">My Courses</li>
            <li class="course-dropdown-loading"><span class="loader-placeholder loader-icon" style="margin: 10px auto; float:none;"></span></li>
            
            <li>
                <a class="mobile-nav-link" href="https://www.openlearning.com/courses/my/">
                    View all my courses
                </a>
            </li>

            
                <li>
                    <a class="mobile-nav-link" href="https://www.openlearning.com/courses/">
                        Find new courses
                    </a>
                </li>
            
            


            <!--Global nav - Misc-->
            <li class="mobile-nav-heading">Misc</li>
            <li>
                <a class="mobile-nav-link" href="https://www.openlearning.com/accounts/account-settings/">
                    Account Settings
                </a>
            </li>
            <li>
                <a class="mobile-nav-link" href="https://www.openlearning.com/accounts/notifications/#settings">
                    Notification Settings
                </a>
            </li>
            <li>
                <a class="mobile-nav-link" href="https://www.openlearning.com/help">

                    Help / Report a Problem
                </a>
            </li>

            
            

            <!--Global nav - Logout-->
            <li class="mobile-nav-form">
                <form action="/accounts/logout/" id="logout-form" class="logout-form" method="post" accept-charset="utf-8">
                    <div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='CQZYT9b5LfYbfz4SvmvLRLtYN8CEOJpe' /></div>
                    <input type="submit" name="logout" id="mobile-logout-button" value="Logout"/>
                </form>
            </li>
        
            <li class="mobile-nav-end"></li>
        </ul>
    </div>
    <script type="text/javascript">
        JS.require('OpenLearning_mobile', function() {
            OpenLearning_mobile.init();
        });
    </script>



<script type="text/javascript">
    JS.require('dust', function() {
        
            dust.debugLevel = 'ERROR';
        
    });
</script>

<script type="text/javascript">
    JS.require('Placeholders', function() {
    });
</script>



<script type="json" id="user-metrics-data">
    {
        "institutionDomainPath": "",
        "remoteAddr": "110.20.162.5, 10.189.254.6"
    }
</script>


<!-- START CHUNK metrics -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/metrics.1ac90add601cd07fbbf4.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK metrics -->


    

<!-- START CHUNK online -->
<script src="https://709d46f74041f979bbed-0078dfde91f1026e77c6f80bb37dbaa2.ssl.cf4.rackcdn.com/chunks/online.48a87c93a4036b611cab.js" type="text/javascript" crossorigin="anonymous"></script>
<!-- END CHUNK online -->



</body>
</html>
