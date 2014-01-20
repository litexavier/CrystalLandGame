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

function unicode(str){
    var a = [], i = 0;
    for (; i < str.length;) {
        var strr = str[i];
        if(check(strr)){
            a[i] = "\\u"+("00" + str.charCodeAt(i).toString(16)).slice( - 4);
            //alert(a[i]);
        }
        else{
            a[i] = strr;
        }
        i++;
    }
    return (a.join(""));
}

function AddAILine(box) {
	c = $("#"+box+" ul li");
	t = c.size()+1;
	n = c.last().clone();
	n.children(".skill").attr("name", "skill"+t);
	n.children(".aival").attr("name", "aival"+t);
	n.children(".aimode").attr("name", "aimode"+t);
	n.appendTo($("#"+box+" ul"));
}

function DelAILine(box) {
	s = $("#"+box+" ul li").size();
	if(s>1){
		$("#"+box+" ul li").last().remove();
	}
}

function SubmitNewMonster () {
	aimodelist = new Array();
	c = $("#new-monster-form #ai-control-box ul li");
	b = c.children(".aimode").find("option:selected");
	for(i=0;i<b.length;i++) {
		aimodelist.push(b[i].value);
	}
	aivallist = new Array();
	b = c.children(".aival");
	for(i=0;i<b.length;i++) {
		aivallist.push(b[i].value);
	}
	skilllist = new Array();
	b = c.children(".skill").find("option:selected");
	for(i=0;i<b.length;i++) {
		skilllist.push(b[i].value);
	}
	ps = $("#new-monster-form").children(".pos").find("option:selected").val();
	prt = $("#new-monster-form").children(".protrate").val();
	m = $("#new-monster-form").children(".mid").find("option:selected").val();
	mn = $("#new-monster-form").children(".mname").val();
	d = document.getElementById("dungeon-id").value;
	tai = new Array;
	for(i=0;i<aimodelist.length;i++) {
		tai.push({
			mode : aimodelist[i],
			val  : aivallist[i],
			skill: skilllist[i]
		});
	}
	var ret = $.toJSON({ ai:tai, mid:m, mname:mn, pos:ps, protrate:prt });
	$.post("/dungeon/mod/monadd/", {"did":d, "data":ret, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value})
	.done(function(data) {
    		$( ".section" ).empty().append(data);
		$( "#tabs" ).tabs();
		// Hover states on the static widgets
		$( "#dialog-link, #icons li" ).hover(
			function() {
				$( this ).addClass( "ui-state-hover" );
			},
			function() {
				$( this ).removeClass( "ui-state-hover" );
			}
		);
	});
}

function ModifyMonster(mid)
{
	aimodelist = new Array();
	c = $("#mod-monster-form"+mid+" #ai-control-box-m"+mid+" ul li");
	b = c.children(".aimode").find("option:selected");
	for(i=0;i<b.length;i++) {
		aimodelist.push(b[i].value);
	}
	aivallist = new Array();
	b = c.children(".aival");
	for(i=0;i<b.length;i++) {
		aivallist.push(b[i].value);
	}
	skilllist = new Array();
	b = c.children(".skill").find("option:selected");
	for(i=0;i<b.length;i++) {
		skilllist.push(b[i].value);
	}
	ps = $("#mod-monster-form"+mid).children(".pos").find("option:selected").val();
	prt = $("#mod-monster-form"+mid).children(".protrate").val();
	m = $("#mod-monster-form"+mid).children(".mid").find("option:selected").val();
	mn = $("#mod-monster-form"+mid).children(".mname").val();
	d = document.getElementById("dungeon-id").value;
	tai = new Array;
	for(i=0;i<aimodelist.length;i++) {
		tai.push({
			mode : aimodelist[i],
			val  : aivallist[i],
			skill: skilllist[i]
		});
	}
	var ret = $.toJSON({ ai:tai, mid:m, mname:mn, pos:ps, protrate:prt });
	$.post("/dungeon/mod/monmod/", {"did":d, "mid":mid, "data":ret, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value})
	.done(function(data) {
    		$( ".section" ).empty().append(data);
		$( "#tabs" ).tabs();
		// Hover states on the static widgets
		$( "#dialog-link, #icons li" ).hover(
			function() {
				$( this ).addClass( "ui-state-hover" );
			},
			function() {
				$( this ).removeClass( "ui-state-hover" );
			}
		);
	});
}

function DelMonster(mid)
{
	d = document.getElementById("dungeon-id").value;
	$.post("/dungeon/mod/mondel/", {"did":d, "mid":mid, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value})
	.done(function(data) {
    		$( ".section" ).empty().append(data);
		$( "#tabs" ).tabs();
		// Hover states on the static widgets
		$( "#dialog-link, #icons li" ).hover(
			function() {
				$( this ).addClass( "ui-state-hover" );
			},
			function() {
				$( this ).removeClass( "ui-state-hover" );
			}
		);
	});
}

function ClearSubmit()
{
}
