{% extends "play/common_play_inc.tpl" %}

{% block content %}
<script> $(function($) {navhilightid="nav-town";}) </script>
<div class="shop-frame">
<table class="shop-table"> <tr>
	<td class="shop-tab-left"> 
		<div>
			<ul class="shop-item-list">
				<li>
					<div class="pic"> <img src="/static/images/items/Sword.png"></img></div>
					<div class="name"> 木剑 </div>
					<div class="price"> 20 G </div>		
				</li>
				<li>
					<div class="pic"> <img src="/static/images/items/Staff.png"></img></div>
					<div class="name"> 木杖 </div>
					<div class="price"> 20 G </div>
				</li>
				<li>
					<div class="pic"> <img src="/static/images/items/Hat.png"></img></div>
					<div class="name"> 铁质头盔 </div>
					<div class="price"> 20 G </div>
				</li>
				<li>
					<div class="pic"> <img src="/static/images/items/Shield.png"></img></div>
					<div class="name"> 木质盾牌 </div>
					<div class="price"> 20 G </div>
				</li>
			</ul>
		</div>
	</td>
	<td class="shop-tab-right">
		<div> </div>
	</td>
</tr></table>
</div>
{% endblock %}
