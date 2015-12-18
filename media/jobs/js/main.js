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

	// check where city, change background color accordingly
	$('.city').each(function() {
		var city = $(this).text();
		//check if in phoenix area
		if (isInArray(phoenixList, city)) {
			$(this).css('background-color', '#A81A5B');
		} else {
			$(this).css("background-color", "#3F358C");
		}
	});

	// get aging invoice days and append to 
	$('.aging').each(function() {
		var date = $(this).parent().siblings('.invoice-line').children('.date-invoiced').text();
		date = moment(date);
		console.log(date) //sanity check
		var days = daysAgo(date);
		console.log(days) //sanity check
		$(this).children().append(days);
		});
});

// Set lists for each major city area
var phoenixList = 
[
	"phoenix",
	"fountain hills",
	"peoria",
	"mesa",
	"scottsdale",
	"gilbert",
	"buckeye",
	"tempe"
]

var tucsonList = 
[
	"tucson",
	"sahuarita",
	"marana",
	"green valley"
]

function isInArray(cities, city) {
	return cities.indexOf(city.toLowerCase()) > -1;
}

function daysAgo(date) {
	var now = moment();
	return now.diff(date, 'days');
}