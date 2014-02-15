{% extends "play/common_play_inc.tpl" %}

{% block content %}
<script> $(function($) {navhilightid="nav-login";}) </script>
<div class="panel panel-default style-play-main-login">
	<div class="panel-heading">登录：</div>
	<div class="panel-body">
		<form role="form" id="login-form" method="post" action="javascript:LoginAction()">
			{% csrf_token %}
			<div class="form-group">
				<label for="UserName">用户名：</label>
				<input type="text" class="form-control" id="UserName" name="username" placeholder="请输入用户名"/>
			</div>
			<div class="form-group">
				<label for="Password">密码：</label>
				<input type="password" class="form-control" id="Password" name="password" placeholder="请输入密码"/>
			</div>
			<div class="alert" id="LoginFeedback" style="display:none"></div>
			<button type="submit" class="btn btn-default">登录</button>
		</form>
	</div>
</div>
{% endblock %}
