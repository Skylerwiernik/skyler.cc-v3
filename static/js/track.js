uid = ""
$.get("https://api.ipdata.co?api-key=06722f1da9b19b6777f415f32f465e0db4d123a1920e640e9f907b08", function (response) {
    if (JSON.stringify(response)["is_eu"] && !document.cookie.includes("eu_accept")) {

        if (window.confirm("Are cookies ok?")) {
            document.cookie += "eu_accept=true";
        }
        else {
            return;
        }
    }
    if (!document.cookie.includes("uid")) {
        document.cookie = "uid=" + Math.random() * Math.pow(10, 16);
    }
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());

    gtag('config', 'UA-178456740-1');

    const cookieSplit = document.cookie.split("=");
    uid = cookieSplit[cookieSplit.indexOf("uid") + 1];
    gtag('set', {'user_id': uid});
    $.getScript("https://www.googletagmanager.com/gtag/js?id=UA-178456740-1");
}, "jsonp");
