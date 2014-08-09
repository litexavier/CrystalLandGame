(function($){
    // the code of this function is from 
    // http://lucassmith.name/pub/typeof.html
    $.type = function(o){
        var _toS = Object.prototype.toString;
        var _types = {
            'undefined': 'undefined',
            'number': 'number',
            'boolean': 'boolean',
            'string': 'string',
            '[object Function]': 'function',
            '[object RegExp]': 'regexp',
            '[object Array]': 'array',
            '[object Date]': 'date',
            '[object Error]': 'error'
        };
        return _types[typeof o] || _types[_toS.call(o)] || (o ? 'object' : 'null');
    };
    // the code of these two functions is from mootools
    // http://mootools.net
    var $specialChars = {
        '\b': '\\b',
        '\t': '\\t',
        '\n': '\\n',
        '\f': '\\f',
        '\r': '\\r',
        '"': '\\"',
        '\\': '\\\\'
    };
    var $replaceChars = function(chr){
        return $specialChars[chr] || '\\u00' + Math.floor(chr.charCodeAt() / 16).toString(16) + (chr.charCodeAt() % 16).toString(16);
    };
    $.toJSON = function(o){
        var s = [];
        switch ($.type(o)) {
        case 'undefined':
            return 'undefined';
            break;
        case 'null':
            return 'null';
            break;
        case 'number':
        case 'boolean':
        case 'date':
        case 'function':
            return o.toString();
            break;
        case 'string':
            return '"' + o.replace(/[\x00-\x1f\\"]/g, $replaceChars) + '"';
            break;
        case 'array':
            for (var i = 0, l = o.length; i < l; i++) {
                s.push($.toJSON(o[i]));
            }
            return '[' + s.join(',') + ']';
            break;
        case 'error':
        case 'object':
            for (var p in o) {
                s.push('\"' + p + '\"' + ':' + $.toJSON(o[p]));
            }
            return '{' + s.join(',') + '}';
            break;
        default:
            return '';
            break;
        }
    };
    $.evalJSON = function(s){
        if ($.type(s) != 'string' || !s.length) 
            return null;
        return eval('(' + s + ')');
    };
})(jQuery);
$(function(){init();});
function init() { datahrefinit(); }
function footerloc() {var h=$('.main-content')[0].offsetHeight; h=550-h-25; $('.footer').css('margin-top', h + 'px');}
function navhilight(e) {$('#'+e).addClass('active');}
function datahrefinit() {$('[data-href]').click(function(e){window.location.href=this.getAttribute('data-href');});}
function Dialog() {
    this.dlgtxt=""; this.dlgtitle=""; this.w = 0; this.h = 0; this.dc=false;
    Dialog.prototype.setWH=function(w,h) {this.w=w;this.h=h;}
    Dialog.prototype.setdlg=function(dlg) {this.dlgtxt=dlg;}
    Dialog.prototype.setTitle=function(t) {this.dlgtitle=t;}
    Dialog.prototype.disableClose=function() {this.dc=true;}
    Dialog.prototype.show=function() {
        var mfx = $('.play-main-frame')[0].offsetLeft;
	      var mfy = $('.play-main-frame')[0].offsetTop;
	      var mr = (800 - this.w)/2;
	      var dt = this.dlgtxt;
	      dt = "<div class='dialog-title'>" + "<div class='dialog-title-text'>" + this.dlgtitle + "</div><div class='dialog-title-close-bt'><span class='icon-close'></span></div></div>" + dt;
	      dt = "<div class='dialog'>" + dt + "</div>";
	      this.dlg=$(dt);
	      this.dlg.css("width", this.w);
	      if(this.h != 0) this.dlg.css("height", this.h);
	      this.dlg.css("top", (mfy + 100) + "px");
        this.dlg.css("left", (mr + mfx) +"px");
        if(!this.dc) this.attach('dialog-title-close-bt', 'click', function(e){e.data.close();});
	      $(document.body).append(this.dlg);
    }
    Dialog.prototype.attach=function(g,a,e){this.dlg.find('.'+g).bind(a,this,e);}
    Dialog.prototype.close=function() {this.dlg.remove();}
    return this;
}
function Sidenav (e) {
    this.items = [];
    this.data = document.getElementById(e);
    var its = $(this.data).find('.sidenavitem');
    var cont= $(this.data).find('.sidenavcontent');
    for(i=0;i<its.length;i++) {
        $(its[i]).click(this, function(e){e.data.doclick(this)});
        this.items.push(its[i]);
        }
    Sidenav.prototype.setDefault = function(l) {
        this.doclick(this.items[l])
    }
    Sidenav.prototype.doclick = function(it){
        for(i=0;i<this.items.length;i++) $(this.items[i]).removeClass('active');
        $(it).addClass('active');
        if(it.hasAttribute('data-content'))
        {
            var cp=it.getAttribute('data-content')
            $.get(cp, function(e){
                if(e['status'] == 'ok') {
                    cont.empty().append(e['msg']);
                }
            }, 'json')
        } else {
            cont.empty();
        }
    }
    return this;
}
function ClickableList(e) {
    this.data = document.getElementById(e);
    this.active = null;
    $(this.data).find('.list-item').click(this, function(e){e.data.doclick(this)});
    ClickableList.prototype.doclick = function(it) {
        this.reset();
        this.active = it; if('actcb' in this)this.actcb(it);
        $(it).addClass('active'); 
    }
    ClickableList.prototype.reset = function () {
        if(this.active != null) $(this.active).removeClass('active');
        if('disactcb' in this)this.disactcb(this.active);
        this.active=null;
    }
    ClickableList.prototype.getActiveId = function() {
        if(this.active == null)return "";
        return this.active.getAttribute('data-id');
    }
    ClickableList.prototype.act = function(e) {
        this.actcb = e;
        return this;
    }
    ClickableList.prototype.disact = function(e) {
        this.disactcb = e;
        return this;
    }
    return this;
}
function userloginsubmit(e) {
    var fm=getpar(e, "FORM");
    clearmsg(fm);
    var un=$(fm).find('input[name="username"]').val();
    var up=$(fm).find('input[name="password"]').val();
    if(un.length==0||un.length>32) {showerrmsg(fm, "用户名不应为空或者长度大于32"); return false;}
    if(up.length<6||up.length>16) {showerrmsg(fm, "密码不应小于6个字符或多于16个字符"); return false;}
    return msgasyncpost(fm, {'username': un, 'password': up});
}
function userregsubmit(e) {
    var fm=getpar(e, "FORM");
    clearmsg(fm);
    var un=$(fm).find('input[name="username"]').val();
    var up=$(fm).find('input[name="password"]').val();
    var rpup=$(fm).find('input[name="reppass"]').val();
    if(un.length==0||un.length>32) {showerrmsg(fm, "用户名不应为空或者长度大于32"); return false;}
    if(up.length<6||up.length>16) {showerrmsg(fm, "密码不应小于6个字符或多于16个字符"); return false;}
    if(up != rpup) {showerrmsg(fm, "两次输入的密码不匹配"); return false;}
    return msgasyncpost(fm, {'username': un, 'password': up});
}
function hiresubmit(e) {
    var fm=getpar(e, "FORM");
    clearmsg(fm);
    var un=$(fm).find('input[name="hirename"]').val();
    if(un.length==0||un.length>32) {showerrmsg(fm, "佣兵名称不应为空或者长度大于32"); return false;}
    return msgasyncpost(fm, {'clsname':cl.getActiveId(), 'pname':un});
}
function createguildsubmit(e) {
    var fm=getpar(e, "FORM");
    clearmsg(fm);
    var un=$(fm).find('input[name="guildname"]').val();
    if(un.length==0||un.length>32) {showerrmsg(fm, "社团名不应为空或者长度大于32"); return false;}
    return msgasyncpost(fm, {'name':un});
}
function dohire(e) {}
function resetform(e) {
    var fm=e;
    while(fm.nodeName != "FORM") fm=fm.parentNode;
    clearmsg(fm);
    $(fm).find('input:text').text("").val("");
    $(fm).find('input:password').text("").val("");
    $(fm).find('textarea').text("").val("");
}
function msgasyncpost(d,da) {
    var t=d.getAttribute('action');
    da['csrfmiddlewaretoken']=document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.post(t, da,
	         function(e){
	             if(e['status']=='ok') {
		               if('msg' in e && e['msg'] != '') showmsg(d, e['msg']);
		               if('redirect' in e && e['redirect']!='') window.location.href=e['redirect'];
	             } else {
		               showerrmsg(d, e['msg']);
	             }
	         },
	         'json').fail(function(e){showerrmsg(d,"操作超时")});
}
function clearmsg(d) {$(d).find('.notice-fb').empty();}
function showerrmsg(d, da) {
    var s=$(d).find('.notice-fb');
    s.empty();
    s.append('<span class="notice-error"><span class="icon-warning"></span>' + da + '</span>');
}
function showmsg(d, da) {
    var s=$(d).find('.notice-fb');
    s.empty();
    s.append('<span class="notice-succ"><span class="icon-success"></span>' + da + '</span');
}
function showdialog(e) {
    var p=$('script[data-tpl='+e+']')[0];
    d=new Dialog();
    d.setTitle(p.getAttribute('data-title'));
    d.setWH(p.getAttribute('data-width'), p.getAttribute('data-height'));
    d.setdlg(p.innerText);
    var x=p.getAttribute('data-enable-close');
    if(x=='disable') d.disableClose();
    return d.show();
}
function getpar(e,t) {
    var r=e;
    while(r.nodeName != t) r=r.parentNode;
    return r;
}
