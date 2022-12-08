(function(){if(!window.cadesplugin){var pluginObject,plugin_resolved=0,plugin_reject,plugin_resolve,isOpera=0,isFireFox=0,isEdge=0,isSafari=0,failed_extensions=0,canPromise=!!window.Promise,cadesplugin;cadesplugin=canPromise?new Promise((function(n,i){plugin_resolve=n,plugin_reject=i})):{};var browserSpecs=check_browser(),ru_cryptopro_npcades_10_native_bridge={callbacksCount:1,callbacks:{},resultForCallback:function resultForCallback(n,i){var t=ru_cryptopro_npcades_10_native_bridge.callbacks[n];t&&t.apply(null,i)},call:function call(n,i,t){var a=t&&"function"===typeof t,s=a?ru_cryptopro_npcades_10_native_bridge.callbacksCount++:0;a&&(ru_cryptopro_npcades_10_native_bridge.callbacks[s]=t);var l=document.createElement("IFRAME"),_=new Array("_CPNP_handle");try{l.setAttribute("src","cpnp-js-call:"+n+":"+s+":"+encodeURIComponent(JSON.stringify(i,_)))}catch(n){alert(n)}document.documentElement.appendChild(l),l.parentNode.removeChild(l),l=null}};cadesplugin.JSModuleVersion="2.1.2",cadesplugin.async_spawn=async_spawn,cadesplugin.set=set_pluginObject,cadesplugin.set_log_level=set_log_level,cadesplugin.getLastError=getLastError,cadesplugin.is_capilite_enabled=is_capilite_enabled,isNativeMessageSupported()&&(cadesplugin.CreateObjectAsync=CreateObjectAsync,cadesplugin.ReleasePluginObjects=ReleasePluginObjects),isNativeMessageSupported()||(cadesplugin.CreateObject=CreateObject),window.cadesplugin_load_timeout?setTimeout(check_load_timeout,window.cadesplugin_load_timeout):setTimeout(check_load_timeout,2e4),set_constantValues(),cadesplugin.current_log_level=cadesplugin.LOG_LEVEL_ERROR,window.cadesplugin=cadesplugin,check_plugin_working()}function check_browser(){var n,i=navigator.userAgent,t=i.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i)||[];return/trident/i.test(t[1])?(n=/\brv[ :]+(\d+)/g.exec(i)||[],{name:"IE",version:n[1]||""}):"Chrome"===t[1]&&(n=i.match(/\b(OPR|Edge)\/(\d+)/),null!=n)?{name:n[1].replace("OPR","Opera"),version:n[2]}:(t=t[2]?[t[1],t[2]]:[navigator.appName,navigator.appVersion,"-?"],null!=(n=i.match(/version\/(\d+)/i))&&t.splice(1,1,n[1]),{name:t[0],version:t[1]})}function cpcsp_console_log(n,i){if("undefined"!==typeof console)return n<=cadesplugin.current_log_level?(n===cadesplugin.LOG_LEVEL_DEBUG&&console.log("DEBUG: %s",i),n===cadesplugin.LOG_LEVEL_INFO&&console.info("INFO: %s",i),void(n===cadesplugin.LOG_LEVEL_ERROR&&console.error("ERROR: %s",i))):void 0}function set_log_level(n){n===cadesplugin.LOG_LEVEL_DEBUG||n===cadesplugin.LOG_LEVEL_INFO||n===cadesplugin.LOG_LEVEL_ERROR?(cadesplugin.current_log_level=n,cadesplugin.current_log_level===cadesplugin.LOG_LEVEL_DEBUG&&cpcsp_console_log(cadesplugin.LOG_LEVEL_INFO,"cadesplugin_api.js: log_level = DEBUG"),cadesplugin.current_log_level===cadesplugin.LOG_LEVEL_INFO&&cpcsp_console_log(cadesplugin.LOG_LEVEL_INFO,"cadesplugin_api.js: log_level = INFO"),cadesplugin.current_log_level===cadesplugin.LOG_LEVEL_ERROR&&cpcsp_console_log(cadesplugin.LOG_LEVEL_INFO,"cadesplugin_api.js: log_level = ERROR"),isNativeMessageSupported()&&(cadesplugin.current_log_level===cadesplugin.LOG_LEVEL_DEBUG&&window.postMessage("set_log_level=debug","*"),cadesplugin.current_log_level===cadesplugin.LOG_LEVEL_INFO&&window.postMessage("set_log_level=info","*"),cadesplugin.current_log_level===cadesplugin.LOG_LEVEL_ERROR&&window.postMessage("set_log_level=error","*"))):cpcsp_console_log(cadesplugin.LOG_LEVEL_ERROR,"cadesplugin_api.js: Incorrect log_level: "+n)}function set_constantValues(){cadesplugin.CAPICOM_LOCAL_MACHINE_STORE=1,cadesplugin.CAPICOM_CURRENT_USER_STORE=2,cadesplugin.CADESCOM_LOCAL_MACHINE_STORE=1,cadesplugin.CADESCOM_CURRENT_USER_STORE=2,cadesplugin.CADESCOM_CONTAINER_STORE=100,cadesplugin.CAPICOM_MY_STORE="My",cadesplugin.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED=2,cadesplugin.CAPICOM_CERTIFICATE_FIND_SUBJECT_NAME=1,cadesplugin.CADESCOM_XML_SIGNATURE_TYPE_ENVELOPED=0,cadesplugin.CADESCOM_XML_SIGNATURE_TYPE_ENVELOPING=1,cadesplugin.CADESCOM_XML_SIGNATURE_TYPE_TEMPLATE=2,cadesplugin.XmlDsigGost3410UrlObsolete="http://www.w3.org/2001/04/xmldsig-more#gostr34102001-gostr3411",cadesplugin.XmlDsigGost3411UrlObsolete="http://www.w3.org/2001/04/xmldsig-more#gostr3411",cadesplugin.XmlDsigGost3410Url="urn:ietf:params:xml:ns:cpxmlsec:algorithms:gostr34102001-gostr3411",cadesplugin.XmlDsigGost3411Url="urn:ietf:params:xml:ns:cpxmlsec:algorithms:gostr3411",cadesplugin.CADESCOM_CADES_DEFAULT=0,cadesplugin.CADESCOM_CADES_BES=1,cadesplugin.CADESCOM_CADES_T=5,cadesplugin.CADESCOM_CADES_X_LONG_TYPE_1=93,cadesplugin.CADESCOM_PKCS7_TYPE=65535,cadesplugin.CADESCOM_ENCODE_BASE64=0,cadesplugin.CADESCOM_ENCODE_BINARY=1,cadesplugin.CADESCOM_ENCODE_ANY=-1,cadesplugin.CAPICOM_CERTIFICATE_INCLUDE_CHAIN_EXCEPT_ROOT=0,cadesplugin.CAPICOM_CERTIFICATE_INCLUDE_WHOLE_CHAIN=1,cadesplugin.CAPICOM_CERTIFICATE_INCLUDE_END_ENTITY_ONLY=2,cadesplugin.CAPICOM_CERT_INFO_SUBJECT_SIMPLE_NAME=0,cadesplugin.CAPICOM_CERT_INFO_ISSUER_SIMPLE_NAME=1,cadesplugin.CAPICOM_CERTIFICATE_FIND_SHA1_HASH=0,cadesplugin.CAPICOM_CERTIFICATE_FIND_SUBJECT_NAME=1,cadesplugin.CAPICOM_CERTIFICATE_FIND_ISSUER_NAME=2,cadesplugin.CAPICOM_CERTIFICATE_FIND_ROOT_NAME=3,cadesplugin.CAPICOM_CERTIFICATE_FIND_TEMPLATE_NAME=4,cadesplugin.CAPICOM_CERTIFICATE_FIND_EXTENSION=5,cadesplugin.CAPICOM_CERTIFICATE_FIND_EXTENDED_PROPERTY=6,cadesplugin.CAPICOM_CERTIFICATE_FIND_APPLICATION_POLICY=7,cadesplugin.CAPICOM_CERTIFICATE_FIND_CERTIFICATE_POLICY=8,cadesplugin.CAPICOM_CERTIFICATE_FIND_TIME_VALID=9,cadesplugin.CAPICOM_CERTIFICATE_FIND_TIME_NOT_YET_VALID=10,cadesplugin.CAPICOM_CERTIFICATE_FIND_TIME_EXPIRED=11,cadesplugin.CAPICOM_CERTIFICATE_FIND_KEY_USAGE=12,cadesplugin.CAPICOM_DIGITAL_SIGNATURE_KEY_USAGE=128,cadesplugin.CAPICOM_PROPID_ENHKEY_USAGE=9,cadesplugin.CAPICOM_OID_OTHER=0,cadesplugin.CAPICOM_OID_KEY_USAGE_EXTENSION=10,cadesplugin.CAPICOM_EKU_CLIENT_AUTH=2,cadesplugin.CAPICOM_EKU_SMARTCARD_LOGON=5,cadesplugin.CAPICOM_EKU_OTHER=0,cadesplugin.CAPICOM_AUTHENTICATED_ATTRIBUTE_SIGNING_TIME=0,cadesplugin.CAPICOM_AUTHENTICATED_ATTRIBUTE_DOCUMENT_NAME=1,cadesplugin.CAPICOM_AUTHENTICATED_ATTRIBUTE_DOCUMENT_DESCRIPTION=2,cadesplugin.CADESCOM_AUTHENTICATED_ATTRIBUTE_SIGNING_TIME=0,cadesplugin.CADESCOM_AUTHENTICATED_ATTRIBUTE_DOCUMENT_NAME=1,cadesplugin.CADESCOM_AUTHENTICATED_ATTRIBUTE_DOCUMENT_DESCRIPTION=2,cadesplugin.CADESCOM_ATTRIBUTE_OTHER=-1,cadesplugin.CADESCOM_STRING_TO_UCS2LE=0,cadesplugin.CADESCOM_BASE64_TO_BINARY=1,cadesplugin.CADESCOM_DISPLAY_DATA_NONE=0,cadesplugin.CADESCOM_DISPLAY_DATA_CONTENT=1,cadesplugin.CADESCOM_DISPLAY_DATA_ATTRIBUTE=2,cadesplugin.CADESCOM_ENCRYPTION_ALGORITHM_RC2=0,cadesplugin.CADESCOM_ENCRYPTION_ALGORITHM_RC4=1,cadesplugin.CADESCOM_ENCRYPTION_ALGORITHM_DES=2,cadesplugin.CADESCOM_ENCRYPTION_ALGORITHM_3DES=3,cadesplugin.CADESCOM_ENCRYPTION_ALGORITHM_AES=4,cadesplugin.CADESCOM_ENCRYPTION_ALGORITHM_GOST_28147_89=25,cadesplugin.CADESCOM_HASH_ALGORITHM_SHA1=0,cadesplugin.CADESCOM_HASH_ALGORITHM_MD2=1,cadesplugin.CADESCOM_HASH_ALGORITHM_MD4=2,cadesplugin.CADESCOM_HASH_ALGORITHM_MD5=3,cadesplugin.CADESCOM_HASH_ALGORITHM_SHA_256=4,cadesplugin.CADESCOM_HASH_ALGORITHM_SHA_384=5,cadesplugin.CADESCOM_HASH_ALGORITHM_SHA_512=6,cadesplugin.CADESCOM_HASH_ALGORITHM_CP_GOST_3411=100,cadesplugin.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256=101,cadesplugin.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512=102,cadesplugin.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_HMAC=110,cadesplugin.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256_HMAC=111,cadesplugin.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_512_HMAC=112,cadesplugin.LOG_LEVEL_DEBUG=4,cadesplugin.LOG_LEVEL_INFO=2,cadesplugin.LOG_LEVEL_ERROR=1,cadesplugin.CADESCOM_AllowNone=0,cadesplugin.CADESCOM_AllowNoOutstandingRequest=1,cadesplugin.CADESCOM_AllowUntrustedCertificate=2,cadesplugin.CADESCOM_AllowUntrustedRoot=4,cadesplugin.CADESCOM_SkipInstallToStore=268435456}function async_spawn(n){function continuer(n,s){var l;try{l=i[n](s)}catch(n){return Promise.reject(n)}return l.done?l.value:Promise.resolve(l.value).then(t,a)}var i=n(Array.prototype.slice.call(arguments,1)),t=continuer.bind(continuer,"next"),a=continuer.bind(continuer,"throw");return t()}function isIE(){return"IE"===browserSpecs.name||"MSIE"===browserSpecs.name}function isIOS(){return navigator.userAgent.match(/ipod/i)||navigator.userAgent.match(/ipad/i)||navigator.userAgent.match(/iphone/i)}function isNativeMessageSupported(){return!isIE()&&("Edge"===browserSpecs.name?(isEdge=!0,!0):"Opera"===browserSpecs.name?(isOpera=!0,browserSpecs.version>=33):"Firefox"===browserSpecs.name?(isFireFox=!0,browserSpecs.version>=52):"Chrome"===browserSpecs.name?browserSpecs.version>=42:"Safari"===browserSpecs.name?(isSafari=!0,browserSpecs.version>=12):void 0)}function CreateObject(n){if(isIOS())return call_ru_cryptopro_npcades_10_native_bridge("CreateObject",[n]);if(isIE()){if(n.match(/X509Enrollment/i))try{var i=document.getElementById("webClassFactory");return i.CreateObject(n)}catch(i){try{var t=document.getElementById("certEnrollClassFactory");return t.CreateObject(n)}catch(n){throw"Для создания обьектов X509Enrollment следует настроить веб-узел на использование проверки подлинности по протоколу HTTPS"}}try{t=document.getElementById("webClassFactory");return t.CreateObject(n)}catch(i){return new ActiveXObject(n)}}return pluginObject.CreateObject(n)}function decimalToHexString(n){return n<0&&(n=4294967295+n+1),n.toString(16).toUpperCase()}function GetMessageFromException(n){var i=n.message;return i?n.number&&(i+=" (0x"+decimalToHexString(n.number)+")"):i=n,i}function getLastError(n){if(isNativeMessageSupported()||isIE()||isIOS())return GetMessageFromException(n);try{return pluginObject.getLastError()}catch(i){return GetMessageFromException(n)}}function ReleasePluginObjects(){return cpcsp_chrome_nmcades.ReleasePluginObjects()}function CreateObjectAsync(n){return pluginObject.CreateObjectAsync(n)}function call_ru_cryptopro_npcades_10_native_bridge(functionName,array){var tmpobj,ex;if(ru_cryptopro_npcades_10_native_bridge.call(functionName,array,(function(e,response){ex=e;var str="tmpobj="+response;eval(str),"string"===typeof tmpobj&&(tmpobj=tmpobj.replace(/\\\n/gm,"\n"),tmpobj=tmpobj.replace(/\\\r/gm,"\r"))})),ex)throw ex;return tmpobj}function show_firefox_missing_extension_dialog(){if(!window.cadesplugin_skip_extension_install){var n=document.createElement("div");n.id="cadesplugin_ovr",n.style="visibility: hidden; position: fixed; left: 0px; top: 0px; width:100%; height:100%; background-color: rgba(0,0,0,0.7)",n.innerHTML="<div id='cadesplugin_ovr_item' style='position:relative; width:400px; margin:100px auto; background-color:#fff; border:2px solid #000; padding:10px; text-align:center; opacity: 1; z-index: 1500'><button id='cadesplugin_close_install' style='float: right; font-size: 10px; background: transparent; border: 1; margin: -5px'>X</button><p>Для работы КриптоПро ЭЦП Browser plugin на данном сайте необходимо расширение для браузера. Убедитесь, что оно у Вас включено или установите его.<p><a href='https://www.cryptopro.ru/sites/default/files/products/cades/extensions/firefox_cryptopro_extension_latest.xpi'>Скачать расширение</a></p></div>",document.getElementsByTagName("Body")[0].appendChild(n),document.getElementById("cadesplugin_close_install").addEventListener("click",(function(){plugin_loaded_error("Плагин недоступен"),document.getElementById("cadesplugin_ovr").style.visibility="hidden"})),n.addEventListener("click",(function(){plugin_loaded_error("Плагин недоступен"),document.getElementById("cadesplugin_ovr").style.visibility="hidden"})),n.style.visibility="visible"}}function install_opera_extension(){window.cadesplugin_skip_extension_install?plugin_loaded_error("Плагин недоступен"):document.addEventListener("DOMContentLoaded",(function(){var n=document.createElement("div");n.id="cadesplugin_ovr",n.style="visibility: hidden; position: fixed; left: 0px; top: 0px; width:100%; height:100%; background-color: rgba(0,0,0,0.7)",n.innerHTML="<div id='cadesplugin_ovr_item' style='position:relative; width:400px; margin:100px auto; background-color:#fff; border:2px solid #000; padding:10px; text-align:center; opacity: 1; z-index: 1500'><button id='cadesplugin_close_install' style='float: right; font-size: 10px; background: transparent; border: 1; margin: -5px'>X</button><p>Для работы КриптоПро ЭЦП Browser plugin на данном сайте необходимо установить расширение из каталога дополнений Opera.<p><button id='cadesplugin_install' style='font:12px Arial'>Установить расширение</button></p></div>",document.getElementsByTagName("Body")[0].appendChild(n);var i=document.getElementById("cadesplugin_install");i.addEventListener("click",(function(n){opr.addons.installExtension("epebfcehmdedogndhlcacafjaacknbcm",(function(){document.getElementById("cadesplugin_ovr").style.visibility="hidden",location.reload()}),(function(){}))})),document.getElementById("cadesplugin_close_install").addEventListener("click",(function(){plugin_loaded_error("Плагин недоступен"),document.getElementById("cadesplugin_ovr").style.visibility="hidden"})),n.addEventListener("click",(function(){plugin_loaded_error("Плагин недоступен"),document.getElementById("cadesplugin_ovr").style.visibility="hidden"})),n.style.visibility="visible",document.getElementById("cadesplugin_ovr_item").addEventListener("click",(function(n){n.stopPropagation()}))}))}function firefox_or_edge_nmcades_onload(){cpcsp_chrome_nmcades.check_chrome_plugin(plugin_loaded,plugin_loaded_error)}function nmcades_api_onload(){window.postMessage("cadesplugin_echo_request","*"),window.addEventListener("message",(function(n){if("string"===typeof n.data&&n.data.match("cadesplugin_loaded"))if(isFireFox||isEdge||isSafari){var i=n.data.substring(n.data.indexOf("url:")+4),t=document.createElement("script");t.setAttribute("type","text/javascript"),t.setAttribute("src",i),t.onerror=plugin_loaded_error,t.onload=firefox_or_edge_nmcades_onload,document.getElementsByTagName("head")[0].appendChild(t),failed_extensions++}else cpcsp_chrome_nmcades.check_chrome_plugin(plugin_loaded,plugin_loaded_error)}),!1)}function load_extension(){if(isFireFox||isEdge||isSafari)nmcades_api_onload();else{var n=document.createElement("script");n.setAttribute("type","text/javascript"),n.setAttribute("src","chrome-extension://iifchhfnnmpdbibifmljnfjhpififfog/nmcades_plugin_api.js"),n.onerror=plugin_loaded_error,n.onload=nmcades_api_onload,document.getElementsByTagName("head")[0].appendChild(n),n=document.createElement("script"),n.setAttribute("type","text/javascript"),n.setAttribute("src","chrome-extension://epebfcehmdedogndhlcacafjaacknbcm/nmcades_plugin_api.js"),n.onerror=plugin_loaded_error,n.onload=nmcades_api_onload,document.getElementsByTagName("head")[0].appendChild(n)}}function load_npapi_plugin(){var n=document.createElement("object");if(n.setAttribute("id","cadesplugin_object"),n.setAttribute("type","application/x-cades"),n.setAttribute("style","visibility: hidden"),document.getElementsByTagName("body")[0].appendChild(n),pluginObject=document.getElementById("cadesplugin_object"),isIE()){var i=document.createElement("object");i.setAttribute("id","certEnrollClassFactory"),i.setAttribute("classid","clsid:884e2049-217d-11da-b2a4-000e7bbb2b09"),i.setAttribute("style","visibility: hidden"),document.getElementsByTagName("body")[0].appendChild(i);var t=document.createElement("object");t.setAttribute("id","webClassFactory"),t.setAttribute("classid","clsid:B04C8637-10BD-484E-B0DA-B8A039F60024"),t.setAttribute("style","visibility: hidden"),document.getElementsByTagName("body")[0].appendChild(t)}}function plugin_loaded(){plugin_resolved=1,canPromise?plugin_resolve():window.postMessage("cadesplugin_loaded","*")}function plugin_loaded_error(n){if(isNativeMessageSupported()){if(failed_extensions++,failed_extensions<2)return;if(isOpera&&("undefined"===typeof n||"object"===typeof n))return void install_opera_extension()}"undefined"!==typeof n&&"object"!==typeof n||(n="Плагин недоступен"),plugin_resolved=1,canPromise?plugin_reject(n):window.postMessage("cadesplugin_load_error","*")}function check_load_timeout(){1!==plugin_resolved&&(isFireFox&&show_firefox_missing_extension_dialog(),plugin_resolved=1,canPromise?plugin_reject("Истекло время ожидания загрузки плагина"):window.postMessage("cadesplugin_load_error","*"))}function createPromise(n){return new Promise(n)}function check_npapi_plugin(){try{CreateObject("CAdESCOM.About");plugin_loaded()}catch(t){document.getElementById("cadesplugin_object").style.display="none";var n=navigator.mimeTypes["application/x-cades"];if(n){var i=n.enabledPlugin;plugin_loaded_error(i?"Плагин загружен, но не создаются обьекты":"Ошибка при загрузке плагина")}else plugin_loaded_error("Плагин недоступен")}}function check_plugin_working(){var n=document.createElement("div");n.innerHTML="\x3c!--[if lt IE 9]><i></i><![endif]--\x3e";var i=1===n.getElementsByTagName("i").length;i?plugin_loaded_error("Internet Explorer версии 8 и ниже не поддерживается"):isNativeMessageSupported()?load_extension():canPromise?"complete"===document.readyState?(load_npapi_plugin(),check_npapi_plugin()):window.addEventListener("load",(function(n){load_npapi_plugin(),check_npapi_plugin()}),!1):window.addEventListener("message",(function(n){"cadesplugin_echo_request"===n.data&&(load_npapi_plugin(),check_npapi_plugin())}),!1)}function set_pluginObject(n){pluginObject=n}function is_capilite_enabled(){return!("undefined"===typeof cadesplugin.EnableInternalCSP||!cadesplugin.EnableInternalCSP)}})();