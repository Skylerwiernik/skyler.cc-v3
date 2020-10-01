window.onload = function (e) {
    if(window.innerWidth > innerHeight) {
        $(".d-block").addClass("desktop-head w-25").removeClass("w-100");
        $(".mobile-paragraph").addClass("desktop-paragraph").removeClass("mobile-paragraph")
    }
    document.getElementById("page-head").hidden = false;
}

