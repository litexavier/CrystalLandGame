﻿{% extends "play/common_play_inc.tpl" %}

{% block main_content %}
<script> navhilight('town'); </script>
<div id='town-slide' class='slide-content'>
  <div class='sidenav'>
    <div class='sidenavitem' data-content='/play/town/hire/'> <div class='side-navitem-inner'> 雇佣 </div> </div>
    <div class='sidenavitem'> <div class='side-navitem-inner'> 竞技场 </div> </div>
    <div class='sidenavitem'> <div class='side-navitem-inner'> 商店 </div> </div>
    <div class='sideblank'> </div>
  </div>
  <div class='sidenavcontent'>
  </div>
</div>
<script type='text/javascript'> sv=new Sidenav('town-slide'); sv.setDefault(0); </script>
{% endblock %}
