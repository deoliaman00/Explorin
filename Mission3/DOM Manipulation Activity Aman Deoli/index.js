var a = true;

function presser() {
  if (a == true) {
    document.getElementById("h1-header").style.color = "transparent";
    a = false;
  } else {
    document.getElementById("h1-header").style.color = "black";
    a = true;
  }
}
