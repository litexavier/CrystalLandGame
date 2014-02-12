{% extends "play/common_play_inc.tpl" %}

{% block content %}
<script> $(function($) {navhilightid="";}) </script>
<div class="panel panel-default style-play-main-login">
	<div class="panel-heading">注册新用户：</div>
	<div class="panel-body">
		<form role="form" method="post" action="/register/">
			<div class="form-group">
				<label for="UserName">用户名：</label>
				<input type="text" class="form-control" id="UserName" placeholder="请输入用户名"/>
			</div>
			<div class="form-group">
				<label for="Password">密码：</label>
				<input type="password" class="form-control" id="Password" placeholder="请输入密码"/>
			</div>
			<div class="form-group">
				<label for="RepeatPassword">重复密码：</label>
				<input type="password" class="form-control" id="RepeatPassword" placeholder="请输入密码"/>
			</div>
			<button type="submit" class="btn btn-default">提交</button>
		</form>
	</div>
</div>
{% endblock %}
