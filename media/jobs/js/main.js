$(document).ready(function() {
	console.log('main.js script loaded') // sanity check

	// hide / show invoiced jobs
	$('#show-invoiced').on('click', function() {
		$('.unpaid-invoice-row').toggle("slow", function() {
			console.log('Show/Hide row');
		});
	});

	// event listener for showing open issues
	$('.open-issue-box').on('click', function() {
		console.log('Open issues clicked');
		$(this).children('.open-issues').toggle("slow");
	});


	// change colors for client background	
	$('.client').each(function() {
		var text = $(this).text();
		//console.log(text);
		if (text == "Charter") {
			$(this).addClass("charter");
		} else {
			$(this).addClass("other-client");
		} 
	});

	// check where city, change background color accordingly
	$('.city').each(function() {
		var city = $(this).text();
		//check if in phoenix area
		if (isInArray(phoenixList, city)) {
			$(this).addClass("phoenix");
		} else {
			$(this).addClass("tucson");
		}
	});

	// get aging invoice days and append to 
	$('.aging').each(function() {
		var date = $(this).parent().siblings('.invoice-line').children('.date-invoiced').text();
		date = moment(new Date(date));
		console.log(date) //sanity check
		var days = daysAgo(date);
		console.log(days) //sanity check
		$(this).children().append(days);
	});

	// append 'due now' to card if due soon or past due
	$('.days-left').each(function() {
		var timeText = $(this).text();
		console.log(timeText);
		if (timeText.toLowerCase().indexOf("minutes") >= 0 ) {
			$(this).text('NOW').addClass('due');
		}
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
	"tempe",
	"surprise",
	"queen creek",
	"goodyear",
	"glendale"
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