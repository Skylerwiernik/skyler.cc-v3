
function resize() {
    if (window.innerHeight > window.innerWidth || window.innerWidth < 1200) {
        $(".contact-form, .info-box, .social-box").css("margin-left", ((window.innerWidth - 260) / 2).toString() + "px");
        $(".contact-form").removeClass("contact-form-desktop");
        $(".info-box").removeClass("info-box-desktop")
        $(".social-box").removeClass("social-box-desktop").css("left", "0px")
    }
    else {
        $(".contact-form").addClass("contact-form-desktop");
        $(".info-box").addClass("info-box-desktop");
        $(".contact-form, .info-box, .social-box").css("margin-left","20px")
        $(".social-box").addClass("social-box-desktop").css("left", (($(".contact-form").width() + $(".info-box").width()) * 1.2).toString() + "px");
    }
    console.log(window.innerHeight)
    if (window.innerWidth < 1200 && window.innerHeight > 665 && window.innerHeight / window.innerWidth < 1.5) {
        $(".contact-form, .info-box, .social-box").addClass("tablet")
    }
    else {
        $(".contact-form, .info-box, .social-box").removeClass("tablet")
    }
}

window.onload = function (e) {
    $(".contact-form, .info-box, .social-box").show()
    resize()
    $("#uid").value = uid
}

window.onresize = function () {
    resize()

}


function socialClick(platform) {
    window.location = "/out/" + platform;
}

function recaptchaCallback(token) {
    $("#contactForm").submit();

}
