<div class='member-list' id='member-list'>
  <lu>
    <li class='member-list-title'>
      <span class='name'> 名称 </span>
      <span class='lv'> 等级 </span>
      <span class='cls'> 职业 </span>
      <span class='disp'> 空闲 </span>
      <span class='hpsp'> HP/SP </span>
      <span class='op'></span>
    </li> 
    {% for it in member_list %}
    <li class='member-list-item list-item' id={{it.id}}>
      <span class='name'> {{it.name}} </span>
      <span class='lv'> {{it.lv}} </span>
      <span class='cls'> {{it.cls}} </span>
      {% if it.disp %}
      <span class='disp yes'> 是 </span>
      {% else %}
      <span class='disp no'> 否 </span>
      {% endif %}
      <span class='hpsp'> <span class='hp'>{{it.hp}} </span>/ <span class='sp'>{{it.sp}} </span></span>
      <span class='span-btn mag20 icon-enter' style='display:none' onclick='showmerdetail(this.parentNode.getAttribute("id"))'></span>
    </li>
    {% endfor %}
  </lu>
</div>
<script type='text/javascript'> cl=new ClickableList('member-list'); cl.act(function(e){$(e).find('.span-btn').css('display', 'inline-block');}).disact(function(e){$(e).find('.span-btn').css('display', 'none');});</script>
<script class='tpl-data' type='text/html' data-tpl='msg-dialog' data-title='佣兵详情' data-height=300 data-width=400 data-enable-close='enable'>
  <div class='mercenary-detail'>
    <div class='mercenary-name'>
      <span class='name'> ##name## </span>
    </div>
    <div class='mercenary-class'>
      <span class='cls'> ##cls## </span>
    </div>
    <div class='mercenary-level'>
      <span class='lvl'> ##lv## </span>
    </div>
  </div>
</script>
