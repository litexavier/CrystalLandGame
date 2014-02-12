function hilight_nav(hi_id) {
	if (hi_id == "") return;
	$(".navbar-collapse #"+hi_id).addClass("active");
}
