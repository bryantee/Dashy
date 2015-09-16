$(document).ready(function() {
	console.log('main.js script loaded')
	$('#show-invoiced').on('click', function() {
		$('.unpaid-invoice-row').toggle("slow", function() {
			console.log('Show/Hide row');
		});
	}) ;
});