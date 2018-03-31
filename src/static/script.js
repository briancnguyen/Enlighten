$(document).ready(function() {
    setTimeout(function() { 
        $(window).scrollTop(0); 
    }, 150);
    $('.dropdown-trigger').dropdown();
    $(".button-collapse").sideNav();
    $("a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 500, function(){
                window.location.hash = hash;
            });
        } 
    });
});