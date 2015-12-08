$(document).ready(function() {
	console.log('main.js script loaded') // sanity check

	// hide / show invoiced jobs
	$('#show-invoiced').on('click', function() {
		$('.unpaid-invoice-row').toggle("slow", function() {
			console.log('Show/Hide row');
		});
	});

	// change colors for client background
	$('.client').each(function() {
		var text = $(this).text();
		//console.log(text);
		if (text == "Charter") {
			$(this).css("background-color", "#4F9CD4");
		} else {
			$(this).css("background-color", "#4CAE4C");
		} 
	});
});