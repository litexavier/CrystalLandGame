﻿<div class="section">
<h3> 副本 {{ name }} </h3>
<div class="sectbody">
<input type="hidden" value={{did}} id="dungeon-id" />
<div id="tabs">
<ul>
{% for i in data %}
<li><a href="#tab-monster{{forloop.counter}}">{{i.mname}}</a><li>
{% endfor %}
<li><a href="#tab-add">添加怪物</a></li>
</ul>
{% for d in data %}
<div id="tab-monster{{forloop.counter}}">
<form method="post" id="mod-monster-form{{forloop.counter}}" action="javascript:ClearSubmit()">
{% csrf_token %}
<span>怪物类型：</span>
<select class="mid">
{% for i in minfo %}
<option value={{i.id}} {% ifequal i.id d.mid %} selected {% endifequal %} > {{i.name}} </option>
{% endfor %}
</select><br>
<span>怪物名称：</span>
<input type="text" class="mname" value="{{d.mname}}"/> <br>
<span>位置：</span>
<select class="pos">
<option value="0" {% ifequal d.pos "0" %} selected {% endifequal %}> 前排 </option>
<option value="1" {% ifequal d.pos "1" %} selected {% endifequal %}> 后排 </option>
</select>
<span>保护：</span>
<input type="text" class="protrate" value="{{d.protrate}}" style="width:30px"/> <span> % </span>
<div id="ai-control-box-m{{forloop.counter}}">
<p> AI设置：</p>
<ul>
{% for a in d.ai %}
<li>
<select name="aimode1" class="aimode">
{% for i in ailist %}
<option value={{i.id}} {% ifequal i.id a.mode %} selected {% endifequal %}> {{i.name}} </option>
{% endfor %}
</select>
<span> 值： </span>
<input type=text" name="aival1" class="aival" style="width:40px" value="{{a.val}}"/>
<span> 技能：</span>
<select name="skill1" class="skill">
{% for i in sk %}
<option value={{i.id}} {% ifequal i.id a.skill %} selected {% endifequal %}> {{i.name}} </option>
{% endfor %}
</select>
</li>
{% endfor %}
</ul>
</div>
<a href="javascript:AddAILine('ai-control-box-m{{forloop.counter}}');"> 增加一行 </a> <span> | </span>
<a href="javascript:DelAILine('ai-control-box-m{{forloop.counter}}');"> 减少一行 </a> <br>
<input type="submit" onclick="javascript:ModifyMonster({{forloop.counter}})" value="修改"/>
<input type="submit" onclick="javascript:DelMonster({{forloop.counter}})" value="删除"/>
</form>
</div>
{% endfor %}
<div id="tab-add">
<form action="javascript:SubmitNewMonster()" method="post" id="new-monster-form">
{% csrf_token %}
<span>怪物类型：</span>
<select class="mid">
{% for i in minfo %}
<option value={{i.id}}> {{i.name}} </option>
{% endfor %}
</select><br>
<span>怪物名称：</span>
<input type="text" class="mname"/> <br>
<span>位置：</span>
<select class="pos">
<option value="0"> 前排 </option>
<option value="1"> 后排 </option>
</select>
<span>保护：</span>
<input type="text" class="protrate" style="width:30px"/> <span> % </span>
<div id="ai-control-box">
<p> AI设置：</p>
<ul>
<li>
<select name="aimode1" class="aimode">
{% for i in ailist %}
<option value={{i.id}}> {{i.name}} </option>
{% endfor %}
</select>
<span> 值： </span>
<input type=text" name="aival1" class="aival" style="width:40px"/>
<span> 技能：</span>
<select name="skill1" class="skill">
{% for i in sk %}
<option value={{i.id}}> {{i.name}} </option>
{% endfor %}
</select>
</li>
</ul>
</div>
<a href="javascript:AddAILine('ai-control-box');"> 增加一行 </a> <span> | </span>
<a href="javascript:DelAILine('ai-control-box');"> 减少一行 </a> <br>
<input type="submit" value="添加"/>
</form> 
</div>
</div>
</div>
<br><a href="/dungeon/show/">返回</a>
</div>
