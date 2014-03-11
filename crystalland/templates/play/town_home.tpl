{% extends "play/common_play_inc.tpl" %}

{% block content %}
<script> $(function($) {navhilightid="nav-town";}) </script>
<div class="row">
	<div class="panel panel-default">
		<div class="panel-heading">酒馆</div>
		<div class="panel-body">
			<button class="btn btn-primary" data-toggle="modal" data-target="#HireStep1"> 雇佣佣兵 </button>
		</div>
	</div>
</div>
<form role="form" action="javascript:HireMercenary()">
	{% csrf_token %}
	<div class="modal dialog-top-margin" id="HireStep1">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
					<h4 class="modal-title">雇佣佣兵 (1/3)</h4>
				</div>
				<div class="modal-body">
					<p> 请选择要招募的佣兵： </p>
					<div class="radio">
						<input type="radio" name="hirecls" value="warrior" checked/> <span> 见习战士 </span> <span style="margin-left:20px;" class="style-gold"> 100G </span>
 						<br>
						<input type="radio" name="hirecls" value="magician"/> <span> 魔法学徒 </span> <span style="margin-left:20px" class="style-gold"> 150G </span>  
					</div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" disabled="disabled">上一步</button>
					<button type="button" class="btn btn-primary" onclick="$('#HireStep1').modal('hide');$('#HireStep2').modal('show');">下一步</button>	
				</div>
			</div>
		</div>
	</div>
	<div class="modal dialog-top-margin" id="HireStep2">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
					<h4 class="modal-title">雇佣佣兵 (2/3)</h4>
				</div>
				<div class="modal-body">
					<div class="form-group">
						<label> 请输入佣兵名字： </label>
						<span class="control-label form-control-feedback" id="MercenaryPreSubFB"></span>
						<input type="text" name="mercname" id="MerName" class="form-control"/>
					</div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" onclick="$('#HireStep2').modal('hide');$('#HireStep1').modal('show');">上一步</button>
					<input type="submit" class="btn btn-primary" value="下一步"/>	
				</div>
			</div>
		</div>
	</div>
	<div class="modal dialog-top-margin" id="HireStep3">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
					<h4 class="modal-title">雇佣佣兵 (3/3)</h4>
				</div>
				<div class="modal-body">
					<div id="HireMerFB"></div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-primary" onclick="javascript:window.location.href='/play/mercenaries'">完成</button>
				</div>
			</div>
		</div>
	</div>
</form>
{% endblock %}
