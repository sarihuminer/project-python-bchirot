define((function(){return function(e){var r={};function t(n){if(r[n])return r[n].exports;var o=r[n]={i:n,l:!1,exports:{}};return e[n].call(o.exports,o,o.exports,t),o.l=!0,o.exports}return t.m=e,t.c=r,t.d=function(e,r,n){t.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:n})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,r){if(1&r&&(e=t(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(t.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var o in e)t.d(n,o,function(r){return e[r]}.bind(null,o));return n},t.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(r,"a",r),r},t.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},t.p="",t(t.s=0)}([function(e,r,t){var n=t(1),o=t(4)(n);t.p=document.querySelector("body").getAttribute("data-base-url")+"nbextensions/arcgis-map-ipywidget";var i;window.require&&(i=n.CdnUrl,new Promise((e,r)=>{fetch(i,{mode:"cors"}).then(t=>{t.status>=200&&t.status<300?t.text().then(r=>{e(r)}).catch(e=>{r(e)}):r("HTTP request on "+i+" returned code "+status)}).catch(e=>{r(e)})})).then(e=>{o.setRequireJSConfig(n.BaseRequireJSConfig),console.log("Initializing esriLoader for quicker load times..."),o.loadModules(["esri/Map","esri/views/MapView","esri/views/SceneView","esri/layers/Layer"],n.EsriLoaderOptions).then(([e,r,t,n])=>{console.log("esriLoader initialization completed successfully!")}).catch(e=>{console.log("esriLoader initialization ran into an error:"),console.log(e)})}).catch(e=>{console.log("Cannot reach "+n.CdnUrl+": Not pre-loading, waiting for user to specify the proper CDN path")}),e.exports={load_ipython_extension:function(){}}},function(e,r,t){var n=t(2),o=t(3),i="/";if(/\/[0-9A-Fa-f]{32}\/notebooks\//.test(location.pathname))try{i=location.pathname.match(/.*\/[0-9A-Fa-f]{32}\/(?=notebooks\/)/)[0]}catch(e){}var a=i+"nbextensions/arcgis/";console.log("nbextension path = "+a),n.JupyterTarget="notebook",n.BaseRequireJSConfig={map:{"*":{"arcgis-map-ipywidget":a+"arcgis-map-ipywidget.js","legacy-mapview":a+"legacy-mapview.js"}},config:{has:{"esri-featurelayer-webgl":1},geotext:{useXhr:function(e){return!0},openXhr:!1,onXhr:function(e,r){var t="undefined"!=typeof XMLHttpRequest&&"withCredentials"in new XMLHttpRequest;e.open("GET",t?r:proxyUrl+"?"+r,!0)}}}},o(n,n.CdnUrl),e.exports=n},function(e,r){var t="//js.arcgis.com/4.13/",n={CdnUrl:t,CdnMainCssUrl:"https://js.arcgis.com/4.13/esri/css/main.css",EsriLoaderOptions:{url:t,dojoConfig:{has:{"esri-featurelayer-webgl":1}}},minJSAPIVersion:"4.13"};e.exports=n},function(e,r){e.exports=function(e,r){if(e.CdnUrl=r,e.EsriLoaderOptions.url=e.CdnUrl,"notebook"===e.JupyterTarget)e.BaseRequireJSConfig.packages=[{name:"esri",location:e.CdnUrl+"esri"},{name:"dojo",location:e.CdnUrl+"dojo"},{name:"dojox",location:e.CdnUrl+"dojox"},{name:"dijit",location:e.CdnUrl+"dijit"},{name:"dstore",location:e.CdnUrl+"dstore"},{name:"moment",location:e.CdnUrl+"moment"},{name:"@dojo",location:e.CdnUrl+"@dojo"},{name:"cldrjs",location:e.CdnUrl+"cldrjs",main:"dist/cldr"},{name:"globalize",location:e.CdnUrl+"globalize",main:"dist/globalize"},{name:"maquette",location:e.CdnUrl+"maquette",main:"dist/maquette.umd"},{name:"maquette-css-transitions",location:e.CdnUrl+"maquette-css-transitions",main:"dist/maquette-css-transitions.umd"},{name:"maquette-jsx",location:e.CdnUrl+"maquette-jsx",main:"dist/maquette-jsx.umd"},{name:"tslib",location:e.CdnUrl+"tslib",main:"tslib"}],window.require&&(window.customRequire=window.require.config(e.BaseRequireJSConfig));else if("lab"===e.JupyterTarget){var t=document.querySelector("script[data-esri-loader]");null!=t&&t.parentNode.removeChild(t)}}},function(e,r,t){var n=t(5),o=t(6);e.exports=function(e){if(e.JupyterTarget){if("lab"===e.JupyterTarget)return n;if("notebook"===e.JupyterTarget)return o;throw"Misconfigured config file! Failing"}throw"config does not specify 'JupyterTarget'! Failing"}},function(e,r,t){!function(e){"use strict";var r="4.13",t="next";function n(e){if(e.toLowerCase()===t)return t;var r=e&&e.match(/^(\d)\.(\d+)/);return r&&{major:parseInt(r[1],10),minor:parseInt(r[2],10)}}function o(e){return void 0===e&&(e=r),"https://js.arcgis.com/"+e+"/"}function i(e){return!e||n(e)?function(e){void 0===e&&(e=r);var i=o(e),a=n(e);return a!==t&&3===a.major?i+(a.minor<=10?"js/":"")+"esri/css/esri.css":i+"esri/themes/light/main.css"}(e):e}function a(e,r){var t=i(e),n=function(e){return document.querySelector('link[href*="'+e+'"]')}(t);return n||function(e,r){if(r){var t=document.querySelector(r);t.parentNode.insertBefore(e,t)}else document.head.appendChild(e)}(n=function(e){var r=document.createElement("link");return r.rel="stylesheet",r.href=e,r}(t),r),n}var s={Promise:"undefined"!=typeof window?window.Promise:void 0},u={};function c(e,r,t){var n;t&&(n=function(e,r){var t=function(n){r(n.error||new Error("There was an error attempting to load "+e.src)),e.removeEventListener("error",t,!1)};return e.addEventListener("error",t,!1),t}(e,t));var o=function(){r(e),e.removeEventListener("load",o,!1),n&&e.removeEventListener("error",n,!1)};e.addEventListener("load",o,!1)}function d(e){void 0===e&&(e={}),u=e}function l(){return document.querySelector("script[data-esri-loader]")}function f(){var e=window.require;return e&&e.on}function p(e){void 0===e&&(e={});var r={};[u,e].forEach((function(e){for(var t in e)Object.prototype.hasOwnProperty.call(e,t)&&(r[t]=e[t])}));var t=r.version,n=r.url||o(t);return new s.Promise((function(e,o){var i=l();if(i){var s=i.getAttribute("src");s!==n?o(new Error("The ArcGIS API for JavaScript is already loaded ("+s+").")):f()?e(i):c(i,e,o)}else if(f())o(new Error("The ArcGIS API for JavaScript is already loaded."));else{var u=r.css;u&&a(!0===u?t:u,r.insertCssBefore),r.dojoConfig&&(window.dojoConfig=r.dojoConfig),c(i=function(e){var r=document.createElement("script");return r.type="text/javascript",r.src=e,r.setAttribute("data-esri-loader","loading"),r}(n),(function(){i.setAttribute("data-esri-loader","loaded"),e(i)}),o),document.body.appendChild(i)}}))}function m(e){return new s.Promise((function(r,t){var n=window.require.on("error",t);window.require(e,(function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t];n.remove(),r(e)}))}))}function v(e,r){if(void 0===r&&(r={}),f())return m(e);var t=l(),n=t&&t.getAttribute("src");return!r.url&&n&&(r.url=n),p(r).then((function(){return m(e)}))}var g={getScript:l,isLoaded:f,loadModules:v,loadScript:p,loadCss:a,setDefaultOptions:d,utils:s};e.getScript=l,e.isLoaded=f,e.loadModules=v,e.loadScript=p,e.loadCss=a,e.setDefaultOptions=d,e.utils=s,e.default=g,Object.defineProperty(e,"__esModule",{value:!0})}(r)},function(e,r,t){"use strict";r.__esModule=!0;function n(e){var r=function(e){return document.querySelector('link[href*="'+e+'"]')}(e);return r||(r=function(e){var r=document.createElement("link");return r.rel="stylesheet",r.href=e,r}(e),document.head.appendChild(r)),r}r.loadCss=n;var o="undefined"!=typeof window,i="https://js.arcgis.com/4.7/";function a(e,r,t){var n;t&&(n=function(e,r){var t=function(n){r(n.error||new Error("There was an error attempting to load "+e.src)),e.removeEventListener("error",t,!1)};return e.addEventListener("error",t,!1),t}(e,t));var o=function(){r(e),e.removeEventListener("load",o,!1),n&&e.removeEventListener("error",n,!1)};e.addEventListener("load",o,!1)}function s(){return document.querySelector("script[data-esri-loader]")}function u(){return window.require&&window.requirejs}function c(e){return void 0===e&&(e={}),e.url||(e.url=i),new r.utils.Promise((function(r,t){var o=s();if(o){var i=o.getAttribute("src");i!==e.url?t(new Error("The ArcGIS API for JavaScript is already loaded ("+i+").")):u()?r(o):a(o,r,t)}else u()?t(new Error("The ArcGIS API for JavaScript is already loaded.")):(e.css&&n(e.css),e.requirejsConfig&&window.require.config(e.requirejsConfig),o=function(e){var r=document.createElement("script");return r.type="text/javascript",r.src=e,r.setAttribute("data-esri-loader","loading"),r}(e.url),e.url,a(o,(function(){o.setAttribute("data-esri-loader","loaded"),r(o)}),t),document.body.appendChild(o))}))}function d(e,t){return void 0===t&&(t={}),function(e){return new r.utils.Promise((function(r,t){null==window.activeRequireFunction?t("esriLoader.setRequireJSConfig() has not been called: You MUST call this function before using esriLoader"):window.activeRequireFunction(["require"],(function(n){n(e,(function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t];r(e)}),t)}))}))}(e)}function l(e){console.log("Setting requirejs-esri-loader's config:"),console.log(e),window.activeRequireFunction=window.require.config(e)}r.utils={Promise:o?window.Promise:void 0},r.getScript=s,r.isLoaded=u,r.loadScript=c,r.loadModules=d,r.setRequireJSConfig=l,r.default={setRequireJSConfig:l,getScript:s,isLoaded:u,loadModules:d,loadScript:c,loadCss:n,utils:r.utils}}])}));
//# sourceMappingURL=extension.js.map