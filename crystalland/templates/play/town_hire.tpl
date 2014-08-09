<div class='hire-form'>
  <form method='post' action='/play/town/hire/do' onsubmit='return false;'>
    {% csrf_token %}
    <div class='hire-class-title'>
      请问你要雇佣谁呢？
    </div> 
    <div class='notice-fb'></div>
    <div class='hire-class-list'>
    <lu id='class-choose'>
      <li class='hire-title'>
        <span class='name'> 职业名称 </span>
        <span class='describe'> 职业描述 </span>
        <span class='price'> 价格 </span>
      </li>
      {% for item in hire_item %}
      <li class='hire-item list-item' data-id= {{ item.id }} > 
        <span class='name'> {{ item.classname }} </span>
        <span class='describe'> {{ item.describe }} </span>
        <span class='price'> {{ item.price }} G </span>
      </li>
      {% endfor %}
    </lu>
    </div>
    <div class='hire-phase-2 fullw' style='display:none'>
      <div class='form-sep-panel'>
        <span class='label c1'> 名称： </span>
        <input type='text' class='bc1' width='300px' name='hirename'/><br>
        <span class='hint'> 请给你的佣兵起个名字（不要超过32个字符) </span>
      </div>

      <div class='input-btn-panel'>
        <div class='btn'> <div class='btn-inner' onclick='hiresubmit(this);'> 雇佣 </div> </div>
        <div class='btn'> <div class='btn-inner' onclick='cl.reset();resetform(this);'> 重置 </div> </div>
      </div>
    </div>
  </form>
  <script type='text/javascript'>cl=new ClickableList('class-choose');cl.act(function(){$('.hire-phase-2').css('display', 'block')}).disact(function(){$('.hire-phase-2').css('display', 'none')});</script>
</div>
