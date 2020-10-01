window.onresize = function () {
    resize()
}
window.onload = function () {
    resize()
    $(".project-content").show()
}

function resize() {
    if(window.innerWidth > innerHeight) {
        $("p").addClass("desktop-paragraph").removeClass("mobile-paragraph");
        $("#head").addClass("desktop-head").removeClass("mobile-head");
        $(".projects-nav").show()
        $(".project-content").css("margin-left", "200px")
        $(".side-badge").show()
        $("#side-badge-mobile").hide()
    }
    else {
        $("p").addClass("mobile-paragraph").removeClass("desktop-paragraph");
        $("#head").addClass("mobile-head").removeClass("desktop-head");
        $(".projects-nav").hide()
        $(".project-content").css("margin-left", "5px")
        $(".side-badge").hide()
        $("#side-badge-mobile").show()


    }
}