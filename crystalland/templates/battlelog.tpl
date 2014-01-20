{% extends "basic_inc.tpl" %}
{% block header_trail %}
<link rel="stylesheet" type="text/css" href="/static/style.css" />
{% endblock %}
{% block body_content %}
<div id="doc"> <div id="mainbold"> <div id="main"> <h2>战斗记录</h2> <table class="bl">
{% for l in log.rec %} <tr>
{% if "s" in l %} <td id="bc1">
{% ifequal l.s 2 %} </td><td class="bc2"> {% endifequal %}
{% ifequal l.type 1 %}
<div id="sl"> <span class="fname"> {{ l.name }} </span> 使用了 <span class="skill"> {{ l.skill }} </span> </div>
{% endifequal %} {% ifequal l.type 2 %} {% if l.pro %}
<span class="bname"> {{ l.name }} </span> 保护 <span class="bpname"> {{ l.pro }} </span> ，受到了 <span class="dmg"> {{ l.dam }} </span> 点伤害 {% ifequal l.cri 1 %} <span class="bcri">(暴击!)</span> {% endifequal %}.
{% else  %}
<span class="bname"> {{ l.name }} </span> 受到了 <span class="dmg"> {{ l.dam }} </span> 点伤害 {% ifequal l.cri 1 %} <span class="bcri">(暴击!)</span> {% endifequal %}.
{% endif %}
{% endifequal %}
{% ifequal l.type 3 %}
<span id="bname"> {{ l.name }} </span> 死掉了.
{% endifequal %}
{% ifequal l.type 4 %}
<div id="sl"> <span id="fname"> {{ l.name }} </span> 陷入了沉思. </div>
{% endifequal %}
{% ifequal l.type 5 %}
<div id="sl"> <span id="fname"> {{ l.name }} </span> 开始蓄力 <span> ({{l.barbe}}  &gt;&gt; {{l.baraf}}) </span> </div> 
{% endifequal %}
{% ifequal l.type 6 %}
<div id="sl"> <span id="fname"> {{ l.name }} </span> 开始咏唱 <span> ({{l.barbe}}  &gt;&gt; {{l.baraf}}) </span> </div> 
{% endifequal %}
{% ifequal l.s 1 %}
</td><td class="bc2">
{% endifequal %}
</td>
{% else %}
{% ifequal l.type 4 %}
<td class="bh" colspan="2"> <h3> 第 {{l.turn}} 回合 </h3> </td>
</tr><tr>
<td class="bc1 break">
<table id="bdc"><tr>
<td style="width:50%">{% for ch in l.t1bk %}<span class="bold">{{ch.name}}</span><div class="hpsp"><span class="hp">HP: {{ch.hp}}/{{ch.maxhp}} </span><br><span class="sp">SP: {{ch.sp}} / {{ch.maxsp}} </span></div>{% endfor %}</td>
<td style="width:50%">{% for ch in l.t1fr %}<span class="bold">{{ch.name}}</span><div class="hpsp"><span class="hp">HP: {{ch.hp}}/{{ch.maxhp}} </span><br><span class="sp">SP: {{ch.sp}} / {{ch.maxsp}} </span></div> {% endfor %} </td></tr></table> 
</td>
<td class="bc2 break">
<table id="bdc"><tr>
<td style="width:50%">{% for ch in l.t2fr %}<span class="bold">{{ch.name}}</span><div class="hpsp"><span class="hp">HP: {{ch.hp}}/{{ch.maxhp}} </span><br><span class="sp">SP: {{ch.sp}} / {{ch.maxsp}} </span> </div> {% endfor %}</td>
<td style="width:50%">{% for ch in l.t2bk %}<span class="bold">{{ch.name}}</span><div class="hpsp"><span class="hp">HP: {{ch.hp}}/{{ch.maxhp}} </span><br><span class="sp">SP: {{ch.sp}} / {{ch.maxsp}} </span> </div> {% endfor %} </td>
</tr></table>
</td>
{% else %}
<td>
<span> {{ l.msg }} </span>
</td>
{% endifequal %}
{% endif %}
</tr>
{% endfor %}
</table>
</div>
</div>
</div>
{% endblock %}
