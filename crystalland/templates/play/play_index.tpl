{% extends "play/common_play_inc.tpl" %}

{% block main_content %}
<div class='mainc'>
     <div class='box-container' style='width:100%'>
     	  <div class='box-container-inner'>
     	       <div class='box-container-header'> 新闻 </div>
	  </div>
     </div>
</div>
<div class='sidec'>
     <div class='box-container fast-login-con'>
     	  <div class='box-container-inner'>
	       <div class='box-container-header'> 快速登录 </div>
	       <div class='box-container-body'>
	       	    <form id='userloginform' method='post' action='/play/login/do' onsubmit='return false'>
		    	{% csrf_token %}
		        <div class='notice-fb'></div>
			<div class='user-input-panel'>
			     <span class='label'>用户名：</span>
			     <input class='bc1' type='text' name='username' style='width:120px'/> <br>
			     <span class='label'>密码：</span> 
			     <input class='bc1' type='password' name='password' style='width:120px'/>
			</div>
			<div class='input-btn-panel'>
			     <div class='btn' onclick='userloginsubmit(this);'> <div class='btn-inner'> 确认 </div> </div>
			     <div class='btn' onclick='resetform(this);'><div class='btn-inner'>重置</div> </div>
			</div>
		    </form>
	       </div>
	  </div>
     </div>
     <div class='box-container ranking-con'>
     	  <div class='box-container-inner'>
	       <div class='box-container-header'> 排行榜 </div>
	  </div>
     </div>
</div>
{% endblock %}
