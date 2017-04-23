var $animation_elements = $('.animation-element');
var $window = $(window);
var istransition = false;
function check_if_in_view() {
    var window_height = $window.height();
    var window_top_position = $window.scrollTop();
    var window_bottom_position = (window_top_position + window_height);

    $.each($animation_elements, function () {
        var $element = $(this);
        var element_height = $element.outerHeight();
        var element_top_position = $element.offset().top;
        var element_bottom_position = (element_top_position + element_height);

        if (istransition == true) {
            $animation_elements = null
        }
        //check to see if this current container is within viewport
        if ((element_bottom_position >= window_top_position) &&
            (element_top_position <= window_bottom_position)) {
            $element.addClass('in-view');
            istransition = true;
        } else {
            $element.removeClass('in-view');
        }


    });
}

$window.on('scroll resize', check_if_in_view);
$window.trigger('scroll');


window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Chrome, Safari and Opera
    document.documentElement.scrollTop = 0; // For IE and Firefox
}

var images = [
    "/static/homepage/images/background-image1.jpg",
    "/static/homepage/images/background-image2.jpg",
    "/static/homepage/images/background-image3.jpg",
    "/static/homepage/images/homepage.jpg",
]


var imageHead = document.getElementById("scroll-div");
var i = 0;

setInterval(function () {

     $("#scroll-div").css("background-image", "url(" + images[i] + ")");
    i = i + 1;
    if (i == images.length) {
        i = 0;
    }

        $(this).css("background-image", "url(" + images[i] + ")");

}, 3000);


$(document).ready(function() {
    var $lightbox = $('#lightbox');

    $('[data-target="#lightbox"]').on('click', function(event) {
        var $img = $(this).find('img'),
            src = $img.attr('src'),
            alt = $img.attr('alt'),
            css = {
                'maxWidth': $(window).width() - 100,
                'maxHeight': $(window).height() - 100
            };

        $lightbox.find('.close').addClass('hidden');
        $lightbox.find('img').attr('src', src);
        $lightbox.find('img').attr('alt', alt);
        $lightbox.find('img').css(css);
    });

    $lightbox.on('shown.bs.modal', function (e) {
        var $img = $lightbox.find('img');

        $lightbox.find('.modal-dialog').css({'width': $img.width()});
        $lightbox.find('.close').removeClass('hidden');
    });
});

$(document).ready(function() {
	// get current URL path and assign 'active' class
	var pathname = window.location.pathname;
	debugger;
	$('.nav > li > a[href="'+pathname+'"]').parent().addClass('active');
	$('.nav > li > a[href!="'+pathname+'"]').parent().removeClass('active');
})