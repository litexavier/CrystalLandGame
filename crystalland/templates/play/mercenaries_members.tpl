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
<script class='tpl-data' type='text/html' data-tpl='msg-dialog' data-enable-title='disable' data-height='auto' data-width=600 data-enable-close='enable'>
  <div class='mercenary-detail foldable'>
    <div class='fold'>
      <div class='fold-t title-banner mercenary-name bgtitle c0'>##name##</div>
      <div class='fold-c'>
        <div class='title-banner bg1 c0'> 基本信息 </div>
        <div class='banner bg3 c0'> 职业 </div>
        <div class='value bg2 c0'> ##cls## </div>
        <div class='banner bg3 c0'> 等级 </div>
        <div class='value bg4 c0'> ##lv## </div>
        <div class='banner bg3 c0'> 经验 </div>
        <div class='value bg2 c0'> ##exp## </div>
        <div class='title-banner bg1 c0'> 人物属性 </div>
        <div class='half'>
          <div class='banner bg3 c0'> HP </div>
          <div class='value'>
            <div class='bghp' style='height:100%;width:70%;padding:0;margin-left:5px;'>&nbsp;</div>
            <div class='hpval' style='padding:0;'> ##hp## </div>
          </div>
          <div class='banner bg3 c0'> 攻击 </div>
          <div class='value bg2 c0'> ##atk## </div>
          <div class='banner bg3 c0'> 魔攻 </div>
          <div class='value bg4 c0'> ##matk## </div>
          <div class='banner bg3 c0'> 速度 </div>
          <div class='value bg2 c0'> ##speed## </div>
        </div>
        <div class='half'>
          <div class='banner bg3 c0'> SP </div>
          <div class='value'>
            <div class='bgsp' style='height:100%;width:70%;padding:0;margin-left:5px;'>&nbsp;</div>
            <div class='spval' style='padding:0;'> ##sp## </div>
          </div>
          <div class='banner bg3 c0'> 防御 </div>
          <div class='value bg2 c0'> ##def## </div>
          <div class='banner bg3 c0'> 魔防 </div>
          <div class='value bg4 c0'> ##mdef## </div>
        </div>
        <div class='title-banner bg1 c0'><span> 可用点数：</span><span> ##apts## </span></div>
        <div class='banner bg3 c0'> STR </div>
        <div class='value'> ##str## </div>
        <div class='banner bg3 c0'> VIT </div>
        <div class='value'> ##vit## </div>
        <div class='banner bg3 c0'> INT </div>
        <div class='value'> ##int## </div>
      </div>
    </div>
    <div class='fold'>
      <div class='fold-t title-banner bgtitle c0'> 装备 </div>
      <div class='fold-c'>
        <div class='test' style='height:100px;'></div>
      </div>
    </div>
    <div class='fold'>
      <div class='fold-t title-banner bgtitle c0'> 技能 </div>
      <div class='fold-c'> </div>
    </div>
    <div class='fold'>
      <div class='fold-t title-banner bgtitle c0'> AI设置 </div>
      <div class='fold-c'> </div>
    </div>
  </div>
</script>
