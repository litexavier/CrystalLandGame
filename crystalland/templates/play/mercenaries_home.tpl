{% extends "play/common_play_inc.tpl" %}

{% block main_content %}
{% include "play/guild_status_bar.tpl" %}
<div class='mercenary-slide'>
  <div id='mercenaries-slide' class='slide-content'>
    <div class='sidenav'>
      <div class='sidenavitem' data-content='/play/mercenaries/members/'> <div class='side-navitem-inner'> 成员 </div> </div>
      <div class='sidenavitem'> <div class='side-navitem-inner'> 队伍 </div> </div>
      <div class='sidenavitem'> <div class='side-navitem-inner'> 道具 </div> </div>
      <div class='sideblank'> </div>
    </div>
    <div class='sidenavcontent'>
    </div>
  </div>
</div>
<script type='text/javascript'> navhilight('mercenaries'); sv=new Sidenav('mercenaries-slide'); sv.setDefault(0); </script>
{% endblock %}
