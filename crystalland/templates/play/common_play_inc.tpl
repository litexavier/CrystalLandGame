{% extends "basic_inc.tpl" %}
{% block header_trail %} 
<link rel="stylesheet" href="/static/style-iconfont.css">
<link rel="stylesheet" href="/static/style-play.css">
<script src="/static/jquery-1.10.2.min.js"></script>
<script src="/static/js-play.js"></script>
<title> 水晶大陆 </title>
{% endblock %}
{% block body_content %}
<div class='play-main-frame'>
    <div class='title-nav'>
    	 <div class='title' data-href='/play/'><div class='maintitle'>水晶大陆</div><div class='subtitle'>ALPHA</div></div>
	 <div class='navs'>
		<div class='navitem' id='mercenaries' data-href='/play/mercenaries/'> <span> 社团 </span> </div>
		<div class='navitem' id='town' data-href='/play/town/'> <span> 城镇 </span> </div>
		<div class='navitem' id='fights' data-href='/play/fights/'> <span> 战斗 </span> </div>
	 </div>
	 <div class='nav-info'>
	      {% if user.username %}
	      	 <span> 欢迎您, {{ user.username }} </span>
		 <span class='nav-info-person-btn' data-href='/play/person/'>[个人]</span>
		 <span class='nav-info-logout-btn' data-href='/play/logout/do'>[登出]</span>
	      {% else %}
	      	 <span class='nav-info-login-btn' data-href='/play/login/'>[登入]</span>
		 <span class='nav-info-register-btn' data-href='/play/register'>[注册]</span>
	      {% endif %}
	 </div>
    </div>
    <div class='main-content'>
    	 {% block main_content %}
	 {% endblock %}
    </div>
    <div class='footer'>
    	 <span> Author By <a href='mailto:xavier_lt@163.com'>@Xavier.Lite</a>, 2013-2014 </span>
    </div>
</div>
{% endblock %}
