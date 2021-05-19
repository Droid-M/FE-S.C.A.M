$(function () {
    $("#sidebar-wrapper").addClass("bg-light border-right");
    $("#sidebar-wrapper").load("./templates/sidebarAdm.html");

    $("#navbar").addClass("navbar navbar-expand-lg navbar-light bg-light border-bottom");
    $("#navbar").load("./templates/navbar.html");
});