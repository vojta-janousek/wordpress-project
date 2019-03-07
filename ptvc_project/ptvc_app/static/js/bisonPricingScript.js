function infoBoxFunc(val) {
  if (val === 0) {
    window.alert("Some text");
  }
  else {
    window.alert("Some other text");
  }
}

function serverPriceChange() {
  var serverUserCount = document.getElementById("server-user-count").value;
  var serverPriceObject = document.getElementById("server-price");

  serverPriceObject.textContent = serverUserCount;
}

function dataCenterPriceChange() {
  var dataCenterUserCount = document.getElementById("data-center-user-count").value;
  var dataCenterPriceObject = document.getElementById("data-center-price");

  dataCenterPriceObject.textContent = dataCenterUserCount;
}
