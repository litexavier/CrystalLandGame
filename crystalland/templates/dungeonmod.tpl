{% extends "basic_inc.tpl" %}
{% block header_trail %}
<link href="/static/style2.css" rel="stylesheet">
<link href="/static/jquery-ui-1.10.4.custom.min.css" rel="stylesheet">
<script src="/static/jquery-1.10.2.min.js"></script>
<script src="/static/jquery-ui-1.10.4.custom.min.js"></script>
<script src="/static/custom.js"></script>
	<script>
	$(function() {
		$( "#tabs" ).tabs();
		// Hover states on the static widgets
		$( "#dialog-link, #icons li" ).hover(
			function() {
				$( this ).addClass( "ui-state-hover" );
			},
			function() {
				$( this ).removeClass( "ui-state-hover" );
			}
		);
	});
	</script>
	<style>
	body{
		font: 62.5% "Trebuchet MS", sans-serif;
		margin: 50px;
	}
	.demoHeaders {
		margin-top: 2em;
	}
	#dialog-link {
		padding: .4em 1em .4em 20px;
		text-decoration: none;
		position: relative;
	}
	#dialog-link span.ui-icon {
		margin: 0 5px 0 0;
		position: absolute;
		left: .2em;
		top: 50%;
		margin-top: -8px;
	}
	#icons {
		margin: 0;
		padding: 0;
	}
	#icons li {
		margin: 2px;
		position: relative;
		padding: 4px 0;
		cursor: pointer;
		float: left;
		list-style: none;
	}
	#icons span.ui-icon {
		float: left;
		margin: 0 4px;
	}
	.fakewindowcontain .ui-widget-overlay {
		position: absolute;
	}
	</style>
{% endblock %}

{% block body_content %}
{% include "dungeonmod_basic.tpl" %}
{% endblock %}
