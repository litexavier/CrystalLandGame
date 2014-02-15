function hilight_nav(hi_id) {
	if (hi_id == "") return;
	$(".navbar-collapse #"+hi_id).addClass("active");
}

function LoginAction() {
	un = document.getElementById("UserName").value;
	up = document.getElementById("Password").value;
	if(un == "")
	{
		$("#LoginFeedback").addClass("alert-danger");
		$("#LoginFeedback").show();
		$("#LoginFeedback").empty().append("错误：用户名不能为空");
		return;
	}
	$.post("/play/login/do", {"username":un, "password":up, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}, 
		function(data) {
			if(data.flag=="succ")
			{
				window.location.href='/play/mercenaries';
			}
			else
			{
				$("#LoginFeedback").addClass("alert-danger");
				$("#LoginFeedback").show();
				$("#LoginFeedback").empty().append("错误："+data.msg);
			}
		},
		"json");
}

function SubmitNewGuild() {
	d = document.getElementById("GuildName").value;
	if(d == "")
	{
		$("#GuildSubmitFeedback").parent().addClass("has-error");
		$("#GuildSubmitFeedback").empty().append("公会名不能为空");
		return;
	}
	$.getJSON("/play/guild/create/do", {"name":d, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}).done(
		function(data) {
			if(data.flag=="succ")
			{
				$("#guild-create-step2").removeClass("show");
				$("#guild-create-succ").addClass("show");
			}
			else
			{
				$("#GuildSubmitFeedback").parent().addClass("has-error");
				$("#GuildSubmitFeedback").empty().append(data.msg);
			}	
		});
}
