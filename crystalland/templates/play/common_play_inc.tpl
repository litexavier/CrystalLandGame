{% extends "basic_inc.tpl" %}
{% block header_trail %} 
<link rel="stylesheet" href="/static/bootstrap.min.css">
<link rel="stylesheet" href="/static/style-play.css">
<script src="/static/jquery-1.10.2.min.js"></script>
<script src="/static/bootstrap.min.js"></script>
<script src="/static/js-play.js"></script>
<title> 水晶大陆 </title>
{% endblock %}

{% block body_content %}
<div class="navbar navbar-default navbar-fixed-top" role="navigation">
	<div class="container">
		<div class="navbar-header">
			<a class="navbar-brand" href="#">水晶大陆</a>
		</div>
		<div class="navbar-collapse collapse">
			<ul class="nav navbar-nav">
				<li id="nav-mercenaries"><a href="#">佣兵团</a></li>
				<li id="nav-battles"><a href="#">战斗</a></li>
				<li id="nav-cities"><a href="#">城镇</a></li>
				<li id="nav-maps"><a href="#">地图</a></li>
				<li id="nav-help"><a href="#">帮助</a></li>
			</ul>
			<ul class="nav navbar-nav navbar-right">
				{% if user.is_authenticated %}
				<li id="nav-logname"><a>{{user.username}} </a></li>
				<li id="nav-logout"><a href="/play/logout/do">登出</a></li>
				{% else %}
				<li id="nav-login"><a href="/play/login/">登录</a></li>
				<li id="nav-register"><a href="/play/register/">注册</a></li>
				{% endif %}
			</ul>
		</div>
	</div>
</div>
<div class="container style-play-main">
	{% block content %}
	{% endblock %}
</div>
<script> $(function ($) { hilight_nav(navhilightid); }) </script>
{% endblock %}
