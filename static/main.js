function getCookie(c_name) {
  var i,
    x,
    y,
    ARRcookies = document.cookie.split(";");
  for (i = 0; i < ARRcookies.length; i++) {
    x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
    y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
    x = x.replace(/^\s+|\s+$/g, "");
    if (x == c_name) {
      return unescape(y);
    }
  }
}

function setCookie(c_name, value, exdays) {
  var exdate = new Date();
  exdate.setDate(exdate.getDate() + exdays);
  var c_value =
    escape(value) + (exdays == null ? "" : ";expires=" + exdate.toUTCString());
  document.cookie = c_name + "=" + c_value;
}

function checkForm() {
  console.log(document.getElementById("id_city_search").value.length);
  if (
    document.getElementById("id_city_search").value.length == 0 &&
    document.getElementById("id_state_search").value.length == 0
  ) {
    alert("Please enter a search term");
    return false;
  }
  let city = document.getElementById("id_city_search").value;
  let normalizedCity = city.toLowerCase();
  let state = document.getElementById("id_state_search").value;
  let normalizedState = state.toLowerCase();
  if (normalizedCity == "elon musk" || normalizedState == "elon musk") {
    alert("He's not here");
    return false;
  }
}

function checkCookie() {
  if (getCookie("first_visit") == 1) {
    window.location.href = "/rides";
  } else {
    setCookie("first_visit", 1, 90);
  }
}
