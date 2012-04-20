/* Main javascript */

jQuery(document).ready(function() {
	$("answer").bind("click", function(event) {
		console.log(this);
		$(this).toggleClass("active");
	});
});
