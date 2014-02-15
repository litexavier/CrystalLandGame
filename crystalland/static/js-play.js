function hilight_nav(hi_id) {
	if (hi_id == "") return;
	$(".navbar-collapse #"+hi_id).addClass("active");
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
