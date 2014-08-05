{% extends "play/common_play_inc.tpl" %}

{% block main_content %}
<script>navhilight('mercenaries');</script>
<script class="tpl-data" type="text/html" data-tpl="msg-dialog" data-title="创建社团" data-height=180 data-width=400 data-enable-close="disable">
  <div class='main-panel'>
    <form action='/play/guild/create/do' onsubmit='return false;'>
      {% csrf_token %}
      <div class='notice-fb'></div>
      <div class='user-input-panel'>
        <div class='form-sep-panel fullw'>
          <div class='label c1'> 名称：</div>
          <input type='text' class='bc1' width='200px' name='guildname'/> 
          <div class='hint'> 请给你的社团起个好听的名字(不要超过32个字符) </div>
        </div>
      </div>
      <div class='input-btn-panel'>
        <div class='btn'> <div class='btn-inner' onclick='createguildsubmit(this);'> 确定 </div> </div>
        <div class='btn'> <div class='btn-inner' onclick='resetform(this);'> 重置 </div> </div>
      </div>
    </form>
  </div>
</script>
<script type='text/javascript'>showdialog('msg-dialog');</script>
{% endblock %}
