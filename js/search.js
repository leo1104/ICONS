function searchUrl() {
    var search = document.getElementById("search").value;
    var searchLower = search.toLowerCase();
    console.log("SEARCHING : " + searchLower);
    switch (searchLower) {
        case "login":
            window.location.href = 'login.html'
            break;
        case "projects":
            window.location.href = 'index.html#projects';
            break;
        case "home":
            window.location.href = 'index.html';
            break;
        case "login":
            window.location.href = '';
            break;
        default:
            window.alert("Search not found :(")
            break;
    }
}