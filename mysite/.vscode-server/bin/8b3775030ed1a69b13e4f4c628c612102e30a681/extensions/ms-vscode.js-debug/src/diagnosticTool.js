"use strict";(()=>{var W,m,le,Ze,A,ce,ie,de,B={},fe=[],Xe=/acit|ex(?:s|g|n|p|$)|rph|grid|ows|mnc|ntw|ine[ch]|zoo|^ord|itera/i;function C(e,n){for(var t in n)e[t]=n[t];return e}function pe(e){var n=e.parentNode;n&&n.removeChild(e)}function i(e,n,t){var r,s,o,l={};for(o in n)o=="key"?r=n[o]:o=="ref"?s=n[o]:l[o]=n[o];if(arguments.length>2&&(l.children=arguments.length>3?W.call(arguments,2):t),typeof e=="function"&&e.defaultProps!=null)for(o in e.defaultProps)l[o]===void 0&&(l[o]=e.defaultProps[o]);return M(e,l,r,s,null)}function M(e,n,t,r,s){var o={type:e,props:n,key:t,ref:r,__k:null,__:null,__b:0,__e:null,__d:void 0,__c:null,__h:null,constructor:void 0,__v:s??++le};return s==null&&m.vnode!=null&&m.vnode(o),o}function w(e){return e.children}function P(e,n){this.props=e,this.context=n}function R(e,n){if(n==null)return e.__?R(e.__,e.__.__k.indexOf(e)+1):null;for(var t;n<e.__k.length;n++)if((t=e.__k[n])!=null&&t.__e!=null)return t.__e;return typeof e.type=="function"?R(e):null}function me(e){var n,t;if((e=e.__)!=null&&e.__c!=null){for(e.__e=e.__c.base=null,n=0;n<e.__k.length;n++)if((t=e.__k[n])!=null&&t.__e!=null){e.__e=e.__c.base=t.__e;break}return me(e)}}function Y(e){(!e.__d&&(e.__d=!0)&&A.push(e)&&!V.__r++||ie!==m.debounceRendering)&&((ie=m.debounceRendering)||ce)(V)}function V(){for(var e;V.__r=A.length;)e=A.sort(function(n,t){return n.__v.__b-t.__v.__b}),A=[],e.some(function(n){var t,r,s,o,l,u;n.__d&&(l=(o=(t=n).__v).__e,(u=t.__P)&&(r=[],(s=C({},o)).__v=o.__v+1,Z(u,o,s,t.__n,u.ownerSVGElement!==void 0,o.__h!=null?[l]:null,r,l??R(o),o.__h),ye(r,o),o.__e!=l&&me(o)))})}function _e(e,n,t,r,s,o,l,u,c,f){var a,g,p,d,_,y,v,h=r&&r.__k||fe,x=h.length;for(t.__k=[],a=0;a<n.length;a++)if((d=t.__k[a]=(d=n[a])==null||typeof d=="boolean"?null:typeof d=="string"||typeof d=="number"||typeof d=="bigint"?M(null,d,null,null,d):Array.isArray(d)?M(w,{children:d},null,null,null):d.__b>0?M(d.type,d.props,d.key,null,d.__v):d)!=null){if(d.__=t,d.__b=t.__b+1,(p=h[a])===null||p&&d.key==p.key&&d.type===p.type)h[a]=void 0;else for(g=0;g<x;g++){if((p=h[g])&&d.key==p.key&&d.type===p.type){h[g]=void 0;break}p=null}Z(e,d,p=p||B,s,o,l,u,c,f),_=d.__e,(g=d.ref)&&p.ref!=g&&(v||(v=[]),p.ref&&v.push(p.ref,null,d),v.push(g,d.__c||_,d)),_!=null?(y==null&&(y=_),typeof d.type=="function"&&d.__k===p.__k?d.__d=c=ge(d,c,e):c=ve(e,d,p,h,_,c),typeof t.type=="function"&&(t.__d=c)):c&&p.__e==c&&c.parentNode!=e&&(c=R(p))}for(t.__e=y,a=x;a--;)h[a]!=null&&(typeof t.type=="function"&&h[a].__e!=null&&h[a].__e==t.__d&&(t.__d=R(r,a+1)),xe(h[a],h[a]));if(v)for(a=0;a<v.length;a++)he(v[a],v[++a],v[++a])}function ge(e,n,t){for(var r,s=e.__k,o=0;s&&o<s.length;o++)(r=s[o])&&(r.__=e,n=typeof r.type=="function"?ge(r,n,t):ve(t,r,r,s,r.__e,n));return n}function ve(e,n,t,r,s,o){var l,u,c;if(n.__d!==void 0)l=n.__d,n.__d=void 0;else if(t==null||s!=o||s.parentNode==null)e:if(o==null||o.parentNode!==e)e.appendChild(s),l=null;else{for(u=o,c=0;(u=u.nextSibling)&&c<r.length;c+=2)if(u==s)break e;e.insertBefore(s,o),l=o}return l!==void 0?l:s.nextSibling}function Qe(e,n,t,r,s){var o;for(o in t)o==="children"||o==="key"||o in n||O(e,o,null,t[o],r);for(o in n)s&&typeof n[o]!="function"||o==="children"||o==="key"||o==="value"||o==="checked"||t[o]===n[o]||O(e,o,n[o],t[o],r)}function se(e,n,t){n[0]==="-"?e.setProperty(n,t):e[n]=t==null?"":typeof t!="number"||Xe.test(n)?t:t+"px"}function O(e,n,t,r,s){var o;e:if(n==="style")if(typeof t=="string")e.style.cssText=t;else{if(typeof r=="string"&&(e.style.cssText=r=""),r)for(n in r)t&&n in t||se(e.style,n,"");if(t)for(n in t)r&&t[n]===r[n]||se(e.style,n,t[n])}else if(n[0]==="o"&&n[1]==="n")o=n!==(n=n.replace(/Capture$/,"")),n=n.toLowerCase()in e?n.toLowerCase().slice(2):n.slice(2),e.l||(e.l={}),e.l[n+o]=t,t?r||e.addEventListener(n,o?ue:ae,o):e.removeEventListener(n,o?ue:ae,o);else if(n!=="dangerouslySetInnerHTML"){if(s)n=n.replace(/xlink[H:h]/,"h").replace(/sName$/,"s");else if(n!=="href"&&n!=="list"&&n!=="form"&&n!=="tabIndex"&&n!=="download"&&n in e)try{e[n]=t??"";break e}catch{}typeof t=="function"||(t!=null&&(t!==!1||n[0]==="a"&&n[1]==="r")?e.setAttribute(n,t):e.removeAttribute(n))}}function ae(e){this.l[e.type+!1](m.event?m.event(e):e)}function ue(e){this.l[e.type+!0](m.event?m.event(e):e)}function Z(e,n,t,r,s,o,l,u,c){var f,a,g,p,d,_,y,v,h,x,L,b=n.type;if(n.constructor!==void 0)return null;t.__h!=null&&(c=t.__h,u=n.__e=t.__e,n.__h=null,o=[u]),(f=m.__b)&&f(n);try{e:if(typeof b=="function"){if(v=n.props,h=(f=b.contextType)&&r[f.__c],x=f?h?h.props.value:f.__:r,t.__c?y=(a=n.__c=t.__c).__=a.__E:("prototype"in b&&b.prototype.render?n.__c=a=new b(v,x):(n.__c=a=new P(v,x),a.constructor=b,a.render=nn),h&&h.sub(a),a.props=v,a.state||(a.state={}),a.context=x,a.__n=r,g=a.__d=!0,a.__h=[]),a.__s==null&&(a.__s=a.state),b.getDerivedStateFromProps!=null&&(a.__s==a.state&&(a.__s=C({},a.__s)),C(a.__s,b.getDerivedStateFromProps(v,a.__s))),p=a.props,d=a.state,g)b.getDerivedStateFromProps==null&&a.componentWillMount!=null&&a.componentWillMount(),a.componentDidMount!=null&&a.__h.push(a.componentDidMount);else{if(b.getDerivedStateFromProps==null&&v!==p&&a.componentWillReceiveProps!=null&&a.componentWillReceiveProps(v,x),!a.__e&&a.shouldComponentUpdate!=null&&a.shouldComponentUpdate(v,a.__s,x)===!1||n.__v===t.__v){a.props=v,a.state=a.__s,n.__v!==t.__v&&(a.__d=!1),a.__v=n,n.__e=t.__e,n.__k=t.__k,n.__k.forEach(function(I){I&&(I.__=n)}),a.__h.length&&l.push(a);break e}a.componentWillUpdate!=null&&a.componentWillUpdate(v,a.__s,x),a.componentDidUpdate!=null&&a.__h.push(function(){a.componentDidUpdate(p,d,_)})}a.context=x,a.props=v,a.state=a.__s,(f=m.__r)&&f(n),a.__d=!1,a.__v=n,a.__P=e,f=a.render(a.props,a.state,a.context),a.state=a.__s,a.getChildContext!=null&&(r=C(C({},r),a.getChildContext())),g||a.getSnapshotBeforeUpdate==null||(_=a.getSnapshotBeforeUpdate(p,d)),L=f!=null&&f.type===w&&f.key==null?f.props.children:f,_e(e,Array.isArray(L)?L:[L],n,t,r,s,o,l,u,c),a.base=n.__e,n.__h=null,a.__h.length&&l.push(a),y&&(a.__E=a.__=null),a.__e=!1}else o==null&&n.__v===t.__v?(n.__k=t.__k,n.__e=t.__e):n.__e=en(t.__e,n,t,r,s,o,l,c);(f=m.diffed)&&f(n)}catch(I){n.__v=null,(c||o!=null)&&(n.__e=u,n.__h=!!c,o[o.indexOf(u)]=null),m.__e(I,n,t)}}function ye(e,n){m.__c&&m.__c(n,e),e.some(function(t){try{e=t.__h,t.__h=[],e.some(function(r){r.call(t)})}catch(r){m.__e(r,t.__v)}})}function en(e,n,t,r,s,o,l,u){var c,f,a,g=t.props,p=n.props,d=n.type,_=0;if(d==="svg"&&(s=!0),o!=null){for(;_<o.length;_++)if((c=o[_])&&"setAttribute"in c==!!d&&(d?c.localName===d:c.nodeType===3)){e=c,o[_]=null;break}}if(e==null){if(d===null)return document.createTextNode(p);e=s?document.createElementNS("http://www.w3.org/2000/svg",d):document.createElement(d,p.is&&p),o=null,u=!1}if(d===null)g===p||u&&e.data===p||(e.data=p);else{if(o=o&&W.call(e.childNodes),f=(g=t.props||B).dangerouslySetInnerHTML,a=p.dangerouslySetInnerHTML,!u){if(o!=null)for(g={},_=0;_<e.attributes.length;_++)g[e.attributes[_].name]=e.attributes[_].value;(a||f)&&(a&&(f&&a.__html==f.__html||a.__html===e.innerHTML)||(e.innerHTML=a&&a.__html||""))}if(Qe(e,p,g,s,u),a)n.__k=[];else if(_=n.props.children,_e(e,Array.isArray(_)?_:[_],n,t,r,s&&d!=="foreignObject",o,l,o?o[0]:t.__k&&R(t,0),u),o!=null)for(_=o.length;_--;)o[_]!=null&&pe(o[_]);u||("value"in p&&(_=p.value)!==void 0&&(_!==e.value||d==="progress"&&!_||d==="option"&&_!==g.value)&&O(e,"value",_,g.value,!1),"checked"in p&&(_=p.checked)!==void 0&&_!==e.checked&&O(e,"checked",_,g.checked,!1))}return e}function he(e,n,t){try{typeof e=="function"?e(n):e.current=n}catch(r){m.__e(r,t)}}function xe(e,n,t){var r,s;if(m.unmount&&m.unmount(e),(r=e.ref)&&(r.current&&r.current!==e.__e||he(r,null,n)),(r=e.__c)!=null){if(r.componentWillUnmount)try{r.componentWillUnmount()}catch(o){m.__e(o,n)}r.base=r.__P=null}if(r=e.__k)for(s=0;s<r.length;s++)r[s]&&xe(r[s],n,typeof e.type!="function");t||e.__e==null||pe(e.__e),e.__e=e.__d=void 0}function nn(e,n,t){return this.constructor(e,t)}function X(e,n,t){var r,s,o;m.__&&m.__(e,n),s=(r=typeof t=="function")?null:t&&t.__k||n.__k,o=[],Z(n,e=(!r&&t||n).__k=i(w,null,[e]),s||B,B,n.ownerSVGElement!==void 0,!r&&t?[t]:s?null:n.firstChild?W.call(n.childNodes):null,o,!r&&t?t:s?s.__e:n.firstChild,r),ye(o,e)}function we(e,n){var t={__c:n="__cC"+de++,__:e,Consumer:function(r,s){return r.children(s)},Provider:function(r){var s,o;return this.getChildContext||(s=[],(o={})[n]=this,this.getChildContext=function(){return o},this.shouldComponentUpdate=function(l){this.props.value!==l.value&&s.some(Y)},this.sub=function(l){s.push(l);var u=l.componentWillUnmount;l.componentWillUnmount=function(){s.splice(s.indexOf(l),1),u&&u.call(l)}}),r.children}};return t.Provider.__=t.Consumer.contextType=t}W=fe.slice,m={__e:function(e,n){for(var t,r,s;n=n.__;)if((t=n.__c)&&!t.__)try{if((r=t.constructor)&&r.getDerivedStateFromError!=null&&(t.setState(r.getDerivedStateFromError(e)),s=t.__d),t.componentDidCatch!=null&&(t.componentDidCatch(e),s=t.__d),s)return t.__E=t}catch(o){e=o}throw e}},le=0,Ze=function(e){return e!=null&&e.constructor===void 0},P.prototype.setState=function(e,n){var t;t=this.__s!=null&&this.__s!==this.state?this.__s:this.__s=C({},this.state),typeof e=="function"&&(e=e(C({},t),this.props)),e&&C(t,e),e!=null&&this.__v&&(n&&this.__h.push(n),Y(this))},P.prototype.forceUpdate=function(e){this.__v&&(this.__e=!0,e&&this.__h.push(e),Y(this))},P.prototype.render=w,A=[],ce=typeof Promise=="function"?Promise.prototype.then.bind(Promise.resolve()):setTimeout,V.__r=0,de=0;function S(){}S.prototype={diff:function(n,t){var r=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{},s=r.callback;typeof r=="function"&&(s=r,r={}),this.options=r;var o=this;function l(y){return s?(setTimeout(function(){s(void 0,y)},0),!0):y}n=this.castInput(n),t=this.castInput(t),n=this.removeEmpty(this.tokenize(n)),t=this.removeEmpty(this.tokenize(t));var u=t.length,c=n.length,f=1,a=u+c,g=[{newPos:-1,components:[]}],p=this.extractCommon(g[0],t,n,0);if(g[0].newPos+1>=u&&p+1>=c)return l([{value:this.join(t),count:t.length}]);function d(){for(var y=-1*f;y<=f;y+=2){var v=void 0,h=g[y-1],x=g[y+1],L=(x?x.newPos:0)-y;h&&(g[y-1]=void 0);var b=h&&h.newPos+1<u,I=x&&0<=L&&L<c;if(!b&&!I){g[y]=void 0;continue}if(!b||I&&h.newPos<x.newPos?(v=rn(x),o.pushComponent(v.components,void 0,!0)):(v=h,v.newPos++,o.pushComponent(v.components,!0,void 0)),L=o.extractCommon(v,t,n,y),v.newPos+1>=u&&L+1>=c)return l(tn(o,v.components,t,n,o.useLongestToken));g[y]=v}f++}if(s)(function y(){setTimeout(function(){if(f>a)return s();d()||y()},0)})();else for(;f<=a;){var _=d();if(_)return _}},pushComponent:function(n,t,r){var s=n[n.length-1];s&&s.added===t&&s.removed===r?n[n.length-1]={count:s.count+1,added:t,removed:r}:n.push({count:1,added:t,removed:r})},extractCommon:function(n,t,r,s){for(var o=t.length,l=r.length,u=n.newPos,c=u-s,f=0;u+1<o&&c+1<l&&this.equals(t[u+1],r[c+1]);)u++,c++,f++;return f&&n.components.push({count:f}),n.newPos=u,c},equals:function(n,t){return this.options.comparator?this.options.comparator(n,t):n===t||this.options.ignoreCase&&n.toLowerCase()===t.toLowerCase()},removeEmpty:function(n){for(var t=[],r=0;r<n.length;r++)n[r]&&t.push(n[r]);return t},castInput:function(n){return n},tokenize:function(n){return n.split("")},join:function(n){return n.join("")}};function tn(e,n,t,r,s){for(var o=0,l=n.length,u=0,c=0;o<l;o++){var f=n[o];if(f.removed){if(f.value=e.join(r.slice(c,c+f.count)),c+=f.count,o&&n[o-1].added){var g=n[o-1];n[o-1]=n[o],n[o]=g}}else{if(!f.added&&s){var a=t.slice(u,u+f.count);a=a.map(function(d,_){var y=r[c+_];return y.length>d.length?y:d}),f.value=e.join(a)}else f.value=e.join(t.slice(u,u+f.count));u+=f.count,f.added||(c+=f.count)}}var p=n[l-1];return l>1&&typeof p.value=="string"&&(p.added||p.removed)&&e.equals("",p.value)&&(n[l-2].value+=p.value,n.pop()),n}function rn(e){return{newPos:e.newPos,components:e.components.slice(0)}}var Hn=new S;var be=/^[A-Za-z\xC0-\u02C6\u02C8-\u02D7\u02DE-\u02FF\u1E00-\u1EFF]+$/,ke=/\S/,Te=new S;Te.equals=function(e,n){return this.options.ignoreCase&&(e=e.toLowerCase(),n=n.toLowerCase()),e===n||this.options.ignoreWhitespace&&!ke.test(e)&&!ke.test(n)};Te.tokenize=function(e){for(var n=e.split(/([^\S\r\n]+|[()[\]{}'"\r\n]|\b)/),t=0;t<n.length-1;t++)!n[t+1]&&n[t+2]&&be.test(n[t])&&be.test(n[t+2])&&(n[t]+=n[t+2],n.splice(t+1,2),t--);return n};var Le=new S;Le.tokenize=function(e){var n=[],t=e.split(/(\n|\r\n)/);t[t.length-1]||t.pop();for(var r=0;r<t.length;r++){var s=t[r];r%2&&!this.options.newlineIsToken?n[n.length-1]+=s:(this.options.ignoreWhitespace&&(s=s.trim()),n.push(s))}return n};var on=new S;on.tokenize=function(e){return e.split(/(\S.+?[.!?])(?=\s+|$)/)};var sn=new S;sn.tokenize=function(e){return e.split(/([{}:;,]|\s+)/)};function U(e){"@babel/helpers - typeof";return typeof Symbol=="function"&&typeof Symbol.iterator=="symbol"?U=function(n){return typeof n}:U=function(n){return n&&typeof Symbol=="function"&&n.constructor===Symbol&&n!==Symbol.prototype?"symbol":typeof n},U(e)}var an=Object.prototype.toString,E=new S;E.useLongestToken=!0;E.tokenize=Le.tokenize;E.castInput=function(e){var n=this.options,t=n.undefinedReplacement,r=n.stringifyReplacer,s=r===void 0?function(o,l){return typeof l>"u"?t:l}:r;return typeof e=="string"?e:JSON.stringify(Q(e,null,null,s),s,"  ")};E.equals=function(e,n){return S.prototype.equals.call(E,e.replace(/,([\r\n])/g,"$1"),n.replace(/,([\r\n])/g,"$1"))};function Q(e,n,t,r,s){n=n||[],t=t||[],r&&(e=r(s,e));var o;for(o=0;o<n.length;o+=1)if(n[o]===e)return t[o];var l;if(an.call(e)==="[object Array]"){for(n.push(e),l=new Array(e.length),t.push(l),o=0;o<e.length;o+=1)l[o]=Q(e[o],n,t,r,s);return n.pop(),t.pop(),l}if(e&&e.toJSON&&(e=e.toJSON()),U(e)==="object"&&e!==null){n.push(e),l={},t.push(l);var u=[],c;for(c in e)e.hasOwnProperty(c)&&u.push(c);for(u.sort(),o=0;o<u.length;o+=1)c=u[o],l[c]=Q(e[c],n,t,r,c);n.pop(),t.pop()}else l=e;return l}var z=new S;z.tokenize=function(e){return e.slice()};z.join=z.removeEmpty=function(e){return e};function Se(e,n,t){return z.diff(e,n,t)}var J,k,Ce,$=0,Ae=[],Fe=m.__b,Ie=m.__r,Ne=m.diffed,De=m.__c,Re=m.unmount;function ne(e,n){m.__h&&m.__h(k,e,$||n),$=0;var t=k.__H||(k.__H={__:[],__h:[]});return e>=t.__.length&&t.__.push({}),t.__[e]}function j(e){return $=1,un(Me,e)}function un(e,n,t){var r=ne(J++,2);return r.t=e,r.__c||(r.__=[t?t(n):Me(void 0,n),function(s){var o=r.t(r.__[0],s);r.__[0]!==o&&(r.__=[o,r.__[1]],r.__c.setState({}))}],r.__c=k),r.__}function H(e,n){var t=ne(J++,7);return cn(t.__H,n)&&(t.__=e(),t.__H=n,t.__h=e),t.__}function N(e,n){return $=8,H(function(){return e},n)}function Ee(e){var n=k.context[e.__c],t=ne(J++,9);return t.c=e,n?(t.__==null&&(t.__=!0,n.sub(k)),n.props.value):e.__}function ln(){for(var e;e=Ae.shift();)if(e.__P)try{e.__H.__h.forEach(q),e.__H.__h.forEach(ee),e.__H.__h=[]}catch(n){e.__H.__h=[],m.__e(n,e.__v)}}m.__b=function(e){k=null,Fe&&Fe(e)},m.__r=function(e){Ie&&Ie(e),J=0;var n=(k=e.__c).__H;n&&(n.__h.forEach(q),n.__h.forEach(ee),n.__h=[])},m.diffed=function(e){Ne&&Ne(e);var n=e.__c;n&&n.__H&&n.__H.__h.length&&(Ae.push(n)!==1&&Ce===m.requestAnimationFrame||((Ce=m.requestAnimationFrame)||function(t){var r,s=function(){clearTimeout(o),He&&cancelAnimationFrame(r),setTimeout(t)},o=setTimeout(s,100);He&&(r=requestAnimationFrame(s))})(ln)),k=null},m.__c=function(e,n){n.some(function(t){try{t.__h.forEach(q),t.__h=t.__h.filter(function(r){return!r.__||ee(r)})}catch(r){n.some(function(s){s.__h&&(s.__h=[])}),n=[],m.__e(r,t.__v)}}),De&&De(e,n)},m.unmount=function(e){Re&&Re(e);var n,t=e.__c;t&&t.__H&&(t.__H.__.forEach(function(r){try{q(r)}catch(s){n=s}}),n&&m.__e(n,t.__v))};var He=typeof requestAnimationFrame=="function";function q(e){var n=k,t=e.__c;typeof t=="function"&&(e.__c=void 0,t()),k=n}function ee(e){var n=k;e.__c=e.__(),k=n}function cn(e,n){return!e||e.length!==n.length||n.some(function(t,r){return t!==e[r]})}function Me(e,n){return typeof n=="function"?n(e):n}var Pe=e=>!!e;var Pn=Symbol("unset");function Be(e){let n=[];for(let t of e)n=n.concat(t);return n}var Bn=2**31-1;var Ve=e=>function({value:t,onChange:r}){return i("div",{className:"decision-buttons"},e.map(s=>i("button",{key:s,onClick:()=>r(s),className:t===s?"active":""},s)))};var ze="<node_internals>",qe="node:",$e=e=>e.config.type==="pwa-node"||e.config.type==="pwa-extensionHost"||e.config.type==="node-terminal",K=e=>e.config.type==="pwa-chrome"||e.config.type==="pwa-msedge",te=e=>e.absolutePath.startsWith(ze)||e.url.startsWith(qe)?2:e.absolutePath.includes("node_modules")?1:0,G=(e,n)=>e.url.startsWith(qe)?e.url:e.absolutePath.startsWith(ze)?e.absolutePath:dn(e.absolutePath)&&n.config.__workspaceFolder?pn(n.config.__workspaceFolder,e.absolutePath):e.absolutePath||e.url,D=e=>{let n=(e.prettyName||e.url).split(/\\|\//g);return n[n.length-1]},dn=e=>Je(e)||fn(e),Je=e=>e.startsWith("/"),fn=e=>/^[a-z]:/i.test(e),Oe=(e,n)=>{let t=e.split("/"),r=n.split("/");for(;t.length&&r[0]===t[0];)t.shift(),r.shift();return(t.length?new Array(t.length).fill(".."):["."]).concat(r).join("/")},pn=(e,n)=>Je(e)?Oe(e,n):Oe(We(Ue(e)),We(Ue(n))),We=e=>e.replace(/\\\//g,"/").replace(/\\/g,"/"),Ue=e=>e.slice(0,1).toUpperCase()+e.slice(1);var re=we(void 0),T=()=>Ee(re);var oe=acquireVsCodeApi(),mn=(e,n)=>{let t=oe.getState()?.componentState||{};return t.hasOwnProperty(e)?t[e]:n},_n=(e,n)=>{let t=oe.getState();oe.setState({...t,componentState:{...t?.componentState,[e]:n}})},F=(e,n)=>{let[t,r]=j(()=>mn(e,n)),s=N(o=>{_n(e,o),r(o)},[e,r]);return[t,s]};var je=()=>{let e=T();return i(w,null,e.breakpoints.map((n,t)=>i(hn,{bp:n,key:t})))},gn=(e,n)=>e.cdp.some(t=>{if("location"in t.args)return!0;if(t.args.url){let r=t.args.url;return n.sources.some(s=>s.url===r)}if(t.args.urlRegex){let r=new RegExp(t.args.urlRegex);return n.sources.some(s=>r.test(s.url))}return!1}),vn=(e,n)=>{let t=0,r=[i("li",{key:t++},i("p",null,"\u2705 This breakpoint was initially set in:"),i("p",null,i("code",null,e.source.path)," line ",e.params.line," column ",e.params.column||1))];if(!gn(e,n))return r.push(i(xn,{bp:e,key:t++})),r;r.push(i("li",{key:t++},i("p",null,"\u2705 In the runtime, the breakpoint was set in:"),i("p",null,i("ul",null,e.cdp.map((l,u)=>i(kn,{cdp:l,index:u,key:u}))))));let s=e.cdp.filter(l=>l.state===1),o=Be(s.map(l=>l.state===1?l.uiLocations:[]));return o.length?(r.push(i("li",{key:t++},i("p",null,"\u2705 The runtime acknowledged and adjusted the breakpoint, and it mapped back to the following locations:"),i("ul",null,o.map((l,u)=>i(bn,{loc:l,key:u})))),i("li",{key:t++},i("p",null,"If this is not right, your compiled code might be out of date with your sources. If you don't think this is the case and something else is wrong, please"," ",i("a",{href:"https://github.com/microsoft/vscode-js-debug/issues/new/choose"},"open an issue"),"!"))),r):(r.push(i("li",{key:t++},i(yn,null))),r)},yn=()=>{let e=T();return i("p",null,"\u2753 We sent the breakpoint, but it didn't bind to any locations. If this is unexpected:",i("ul",null,i("li",null,"Make sure that your program is loading or running this script. You can add a"," ",i("code",null,"debugger;")," statement to check this: your program will pause when it hits it."),i("li",null,"If your breakpoint is set in certain places, such as on the last empty line of a file, the runtime might not be able to find anywhere to place it."),$e(e)&&i("li",null,"Unless you"," ",i("a",{href:"https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_breakpoint-validation"},"run with --nolazy"),", Node.js might not resolve breakpoints for code it hasn't parsed yet."),i("li",null,"If necessary, make sure your compiled files are up-to-date with your source files.")))},hn=({bp:e})=>{if(!e.source.path)return null;let n=T();return i("div",{className:"content source-container"},i("h2",null,G({absolutePath:e.source.path,url:e.source.path},n),":",e.params.line,":",e.params.column||1),i("ul",{className:"bp-tracing"},vn(e,n)))},xn=({bp:e})=>{let n=T(),t=D({url:e.source.path}),r=n.sources.filter(s=>D(s).toLowerCase()===t.toLowerCase());return r.length?i("li",null,i("p",null,"\u2753 We couldn't find a corresponding source location, but found some other files with the same name:"),i("ul",null,r.map(s=>i("li",{key:s},i(wn,{original:e.source.path,updated:s.absolutePath||s.url})))),K(n)?i("p",null,"You may need to adjust the ",i("code",null,"webRoot")," in your ",i("code",null,"launch.json")," if you're building from a subfolder, or tweak your ",i("code",null,"sourceMapPathOverrides"),"."):i("p",null,"If this is the same file, you may need to adjust your build tool"," ",K(n)&&i(w,null,"or ",i("code",null,"webRoot")," in the launch.json")," ","to correct the paths.")):i("li",null,i("p",null,i(Sn,{basename:t})))},wn=({original:e,updated:n})=>i("span",{className:"text-diff"},Se(e.split(/[/\\]/g),n.split(/[/\\]/g),{ignoreCase:!0}).map((t,r)=>i("span",{className:t.added?"add":t.removed?"rm":"",key:r},r>0?"/":"",t.value.join("/")))),bn=({loc:e})=>{let t=T().sources.find(r=>r.sourceReference===e.sourceReference);return i(w,null,i("code",null,t?.absolutePath??t?.url??"unknown")," line ",e.lineNumber," column"," ",e.columnNumber)},kn=({cdp:e,index:n})=>{let t=T(),[r,s]=F(`showCdpBp${n}`,!1),{url:o,line:l,col:u,regex:c}="location"in e.args?{url:t.sources.find(f=>!f.compiledSourceRefToUrl&&f.scriptIds.includes(e.args.location.scriptId))?.url,regex:void 0,line:e.args.location.lineNumber+1,col:(e.args.location.columnNumber||0)+1}:{url:e.args.urlRegex?Tn(e.args.urlRegex):e.args.url,regex:e.args.urlRegex,line:e.args.lineNumber+1,col:(e.args.columnNumber||0)+1};return i("li",null,i("p",null,i("code",null,o)," line ",l," column ",u," ",c&&i("a",{onClick:()=>s(!r)},"via this regex")),r&&i("p",null,i("code",null,c)))},Tn=e=>e.replace(/\[([[a-z])[A-Z]\]/g,(n,t)=>t).replace(/\\\\/,"\\").replace(/\\\//g,"/").replace(/\|.+$/g,"").replace(/\\\./g,".");var Ln=Ve(["Loaded in directly","Be parsed from a sourcemap"]),Sn=({basename:e})=>{let n=T(),[t,r]=j(e.endsWith(".js")?void 0:"Be parsed from a sourcemap");return i(w,null,i("p",null,"\u2753 We couldn't find a corresponding source location, and didn't find any source with the name ",i("code",null,e),"."),i("p",null,"How did you expect this file to be loaded? (If you have a compilation step, you should pick 'sourcemap')",i(Ln,{onChange:r,value:t}),t==="Loaded in directly"&&(K(n)?i("p",null,"It looks like your webpage didn't load this script; breakpoints won't be bound until the file they're set in is loaded. Make sure your script is imported from the right location using a ",i("code",null,"<script>")," tag."):i("p",null,"It looks like your program didn't load this script; breakpoints won't be bound until the file they're set in is loaded. Make sure your script is imported with a"," ",i("code",null,"require()")," or ",i("code",null,"import")," statement, such as"," ",i("code",null,"require('./",e,"')"),".")),t==="Be parsed from a sourcemap"&&i("p",null,"Here's some hints that might help you:",i("ul",null,/\.tsx?$/.test(e)?i("li",null,"Make sure you have ",i("code",null,'"sourceMap": true')," in your tsconfig to generate sourcemaps."):i("li",null,"Make sure your build tool is set up to create sourcemaps."),!n.config.outFiles.includes("!**/node_modules/**")&&i("li",null,"It looks like you narrowed the ",i("code",null,"outFiles")," in your launch.json. Try removing this: it now defaults to the whole workspace, and overspecifying it can unnecessarily narrow places where we'll resolve sourcemaps.")))))};var Ke=({onPick:e})=>i("div",{className:"intro"},i("div",null,i("header",null,"Debug Doctor"),i("div",{className:"intro-content"},i("p",null,"What are you trying to find out?"),i("ul",null,i("li",null,i("a",{role:"button",onClick:()=>e(1)},"Why my breakpoints don't bind")),i("li",null,i("a",{role:"button",onClick:()=>e(2)},"What scripts and sourcemaps are loaded")),i("li",null,i("a",{href:"https://github.com/microsoft/vscode-js-debug/issues/new/choose"},"Something else..."))))));var Ge=()=>{let e=T(),n=H(()=>{let u=new Map;for(let c of e.sources)u.set(c.uniqueId,c);return u},[e.sources]),t=H(()=>e.sources.map(u=>[[u.url,u.absolutePath,u.prettyName].join(" ").toLowerCase(),u]).sort((u,c)=>te(u[1])-te(c[1])),[e.sources]),[r,s]=F("filter",""),o=H(()=>r?t.filter(([u])=>u.includes(r.toLowerCase())).map(([,u])=>u):t.map(u=>u[1]),[t,r]),l=N(u=>s(u.target.value),[]);return i(w,null,i("input",{placeholder:"Filter sources...",className:"source-filter",value:r,onChange:l,onKeyUp:l}),i("small",{style:{marginBottom:"1rem"}},"Showing ",o.length," of ",e.sources.length," sources..."),o.map(u=>i(Cn,{source:u,allSources:n,key:u.sourceReference})))},Cn=({source:e,allSources:n})=>{let[t,r]=F(`sourceBreadCrumbs${e.uniqueId}`,[e.uniqueId]),s=H(()=>t.map(f=>n.get(f)).filter(Pe),[n,t]),[o,l]=F(`sourceExpanded${e.uniqueId}`,!1),u=T(),c=N(()=>l(!o),[o]);return i("div",{className:`source-container ${o?" expanded":""}`},i("h2",{onClick:c},G(e,u)),o&&i(w,null,s.length>1&&i(Fn,{sources:s,update:r}),i(In,{source:s[s.length-1],open:f=>{let a=u.sources.find(g=>g.sourceReference===f);a&&r(t.concat(a.uniqueId))}})))},Fn=({sources:e,update:n})=>i("ol",{className:"source-breadcrumbs"},e.map((t,r)=>{let s=`${D(t)} (#${t.sourceReference})`;return r===e.length-1?i("li",null,s):i("li",{key:r},i("a",{key:r,onClick:()=>n(e.slice(0,r+1).map(o=>o.uniqueId))},s)," ","\xBB"," ")})),In=({source:e,open:n})=>i("dl",{className:"source-data-grid"},i("dt",null,"url"),i("dd",null,i("code",null,e.url)),i("dt",null,"sourceReference"),i("dd",null,i("code",null,e.sourceReference)),i("dt",null,"absolutePath"),i("dd",null,i("code",null,e.absolutePath)),i("dt",null,"absolutePath verified?"),i("dd",null,e.compiledSourceRefToUrl?"\u2705 From sourcemap, assumed correct":e.actualAbsolutePath?"\u2705 Verified on disk":"\u274C Disk verification failed (does not exist or different content)"),i("dt",null,"sourcemap children:"),i("dd",null,e.sourceMap?i("ul",null,Object.entries(e.sourceMap.sources).map(([t,r])=>i("li",{key:t},i(Nn,{url:t,sourceRef:r,pick:n})))):"None (does not have a sourcemap)"),i("dt",null,"referenced from sourcemap:"),i("dd",null,e.compiledSourceRefToUrl?i("ul",null,e.compiledSourceRefToUrl.map(([t,r])=>i("li",{key:r},i(Dn,{url:r,sourceRef:t,pick:n})))):"None (not from a sourcemap)")),Nn=({url:e,sourceRef:n,pick:t})=>{let s=T().sources.find(l=>l.sourceReference===n),o=N(()=>t(n),[n]);return i(w,null,e," \u2192 ",i("a",{onClick:o},s?`${D(s)} (#${n})`:"unknown"))},Dn=({url:e,sourceRef:n,pick:t})=>{let s=T().sources.find(l=>l.sourceReference===n),o=N(()=>t(n),[n]);return i(w,null,i("a",{onClick:o},s?`${D(s)} (#${n})`:"unknown")," as ",e," ","\u2192 this")};var Ye=({dump:e})=>{let[n,t]=F("experience",0);return i(re.Provider,{value:e},n===0?i(Ke,{onPick:t}):i(w,null,i("a",{role:"button",onClick:()=>t(0),className:"back"},"\u2190 Back"),n===1?i(je,null):i(Ge,null)))};typeof DUMP<"u"?X(i(Ye,{dump:DUMP}),document.body):fetch(document.location.search.slice(1)).then(e=>e.json()).then(e=>X(i(Ye,{dump:e}),document.body));})();
//# sourceMappingURL=diagnosticTool.js.map
