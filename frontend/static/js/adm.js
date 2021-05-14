$(function () {
    $("#sidebar-wrapper").addClass("bg-light border-right");
    $("#sidebar-wrapper").load("/static/components/sidebarAdm.html");

    $("#navbar").addClass("navbar navbar-expand-lg navbar-light bg-light border-bottom");
    $("#navbar").load("/static/components/navbar.html");
});