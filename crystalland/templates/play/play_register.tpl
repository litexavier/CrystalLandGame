{% extends "play/common_play_inc.tpl" %}

{% block content %}
<script> $(function($) {navhilightid="nav-register";}) </script>
<div class="panel panel-default style-play-main-login">
	<div class="panel-heading">注册新用户：</div>
	<div class="panel-body">
		<form role="form" id="register-form" method="post" action="/play/register/do">
			{% csrf_token %}
			<div class="form-group">
				<label for="UserName">用户名：</label>
				<span class="control-label form-control-feedback" id="UserNameInfo"></span>
				<input type="text" class="form-control" id="UserName" name="UserName" placeholder="请输入用户名"/>
			</div>
			<div class="form-group">
				<label for="Password">密码：</label>
				<span class="control-label form-control-feedback" id="PasswordInfo"></span>
				<input type="password" class="form-control" id="Password" name="Password" placeholder="请输入密码"/>
			</div>
			<div class="form-group">
				<label for="RepeatPassword">重复密码：</label>
				<span class="control-label form-control-feedback" id="RepeatPassInfo"></span>
				<input type="password" class="form-control" id="RepeatPassword" placeholder="请输入密码"/>
			</div>
			<button type="submit" class="btn btn-default">注册</button>
		</form>
	</div>
</div>
<script>
$("#register-form").submit(function(e){
	ufm = $("#UserName");
	ret = true;
	if( ufm.val() == "" ) {
		ufm.parent().addClass("has-error");
		$("#UserNameInfo").empty().append("用户名不能为空");
		ret = false;
	} else {
		ufm.parent().removeClass("has-error");
		$("#UserNameInfo").empty();
	};
	ufm = $("#Password");
	pwd = ufm.val();
	if( pwd == "" ) {
		ufm.parent().addClass("has-error");
		$("#PasswordInfo").empty().append("密码不能为空");
		ret = false;
	} else {
		ufm.parent().removeClass("has-error");
		$("#PasswordInfo").empty();
	};
	ufm = $("#RepeatPassword");
	if( ufm.val() != pwd ) {
		ufm.parent().addClass("has-error");
		$("#RepeatPassInfo").empty().append("重复密码和原密码不一致");
		ret = false;
	} else {
		ufm.parent().removeClass("has-error");
		$("#RepeatPassInfo").empty();
	};
	if(!ret) {
		e.preventDefault();
	}
});
</script>
{% endblock %}
