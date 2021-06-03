function searchUrl() {
  var search = document.getElementById("search").value;
  switch (search) {
    case "login":
    window.location.href='login.html'  
        break;
    case "projects":
    window.location.href='index.html#projects';
        break;
    case "login":
    window.location.href='';
        break;
    case "login":
    window.location.href='';
        break;
    default:
        window.alert("Search not found :(")
      break;
  }
}
