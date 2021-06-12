function searchUrl() {
    var search = document.getElementById("search").value;
    var searchLower = search.toLowerCase();
    console.log("SEARCHING : " + searchLower);
    switch (searchLower) {
        case "login":
            window.location.href = '/login'
            break;
        case "projects":
            window.location.href = '/#projects';
            break;
        case "home":
            window.location.href = '/';
            break;
        case "faculty":
            window.location.href = '/faculty';
            break;
        case "alumni":
            window.location.href = '/alumni';
            break;
        case "who made this":
            window.alert("Search The Royal Flush on LinkedIn ;)");
            break;
        case ":)":
            window.alert(":)");
            break;
        case "create account":
            window.location.href = '/login';
            break;
        default:
            window.alert("Search not found :(");
            break;
    }
}