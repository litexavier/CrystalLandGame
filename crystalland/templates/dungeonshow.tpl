{% extends "basic_inc.tpl" %}
{% block header_trail %}
<link href="/static/style2.css" rel="stylesheet">
<script src="/static/jquery-1.10.2.min.js"></script>
{% endblock %}

{% block body_content %}
<div class="section">
<h3>已有副本</h3>
<div class="sectbody">
<table style="width:100%">
<tr>
<th> ID </th> <th> 名称 </th> <th> 怪物 </th> <th> 战斗重置 </th> <th style="width:30px"></th> <th style="width:30px"></th>
</tr>
{% for i in dlist %}
<tr>
<td> {{ i.id }} </td>
<td> {{ i.name }} </td>
<td> {{ i.monsters }} </td>
<td> {% ifequal i.resetby 1 %} 是 {% else %} 否  {% endifequal %} </td>
<td> <a href="/dungeon/mod/{{i.id}}"> 更改 </a> </td>
<td> <a href="/dungeon/del/{{i.id}}"> 删除 </a> </td>
</tr>
{% endfor %}
</table>
</div>
</div>
<div class="section">
<h3>
添加副本
</h3>
<div class="sectbody">
<form action="/dungeon/add/" method="post">
{% csrf_token %}
<span>副本名称：</span><input type="text" name="dname"/><br>
<span>每次战斗是否刷新：</span>
<input type="radio" name="rbb" value="yes" selected/>是
<input type="radio" name="rbb" value="no"/>否
<br>
<input type="submit"/>
</form>
</div>
</div>
{% endblock %}
