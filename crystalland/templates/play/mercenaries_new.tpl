{% extends "play/common_play_inc.tpl" %}

{% block content %}
<script> $(function($) {navhilightid="nav-mercenaries";}) </script>
<form role="form" action="javascript:SubmitNewGuild()">
{% csrf_token %}
<div class="modal show dialog-top-margin" id="guild-create-step1">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<h4 class="modal-title">创建一个公会（1/2）</h4>
			</div>
			<div class="modal-body">
				<p>你还没有自己的公会，点击<b style="color:blue">下一步</b>开始创建公会</p>	
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-primary" onclick="$('#guild-create-step1').removeClass('show');$('#guild-create-step2').addClass('show');">下一步</button>
			</div>
		</div>
	</div>
</div>
<div class="modal dialog-top-margin" id="guild-create-step2">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<h4 class="modal-title">创建一个公会（2/2）</h4>
			</div>
			<div class="modal-body">
				<div class="form-group">
					<label for="GuildName">请输入公会名：</label>
					<span class="control-label form-control-feedback" id="GuildSubmitFeedback"></span>
					<input type="text" class="form-control" id="GuildName" name="GuildName" placeholder="公会名"/>
				</div>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-default" disabled="disabled">上一步</button>
				<input type="submit" class="btn btn-primary" value="下一步" />
			</div>
		</div>
	</div>
</div>
<div class="modal dialog-top-margin" id="guild-create-succ">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<h4 class="modal-title">创建完成</h4>
			</div>
			<div class="modal-body">
				<p> 恭喜，你已经创建完公会，点击 <b style="color:blue">完成</b> 按钮进入公会界面 </p>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-primary" onclick="javascript:window.location.href='/play/mercenaries'">完成</button>
			</div>
		</div>
	</div>
</div>
</form>
{% endblock %}
