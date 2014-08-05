{% extends "play/common_play_inc.tpl" %}

{% block main_content %}
<script class="tpl-data" type="text/html" data-tpl="msg-dialog" data-title="注册" data-height=270 data-width=400 data-enable-close="disable">
  <div class='main-panel'>
    <form method="post" action="/play/register/do" onsubmit="return false;">
      {% csrf_token %}
      <div class='user-input-panel'>
        <div class='notice-fb'></div>
        <div class='form-sep-panel fullw'>
          <span class='c1 label'> 用户名： </span> 
	      	<input class='bc1' name="username" type="text" style='width: 200px'/> <br>
          <span class='hint'> 由1到32个字符组成 </span>
        </div>
        <div class='form-sep-panel fullw'>
          <span class='c1 label'> 密码： </span>
          <input class='bc1' name="password" type="password" style='width: 200px'/> <br>
          <span class='hint'> 由6到16个字符组成 </span>
        </div>
        <div class='form-sep-panel fullw'>
          <span class='c1 label'> 重复密码： </span>
          <input class='bc1' name="reppass" type="password" style='width: 200px'/> <br>
          <span class='hint'> 重复上面的密码 </span>
        </div>
      </div>
      <div class='input-btn-panel'>
        <div class='btn' onclick='userregsubmit(this);'> <div class='btn-inner'> 确定 </div> </div>
        <div class='btn' onclick='resetform(this);'> <div class='btn-inner'>重置 </div> </div>
      </div>
    </form>
  </div>
</script>
<script type="text/javascript"> showdialog('msg-dialog'); </script>
{% endblock %}
