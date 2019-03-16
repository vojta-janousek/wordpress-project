function infoBoxFunc(val) {
  if (val === 0) {
    window.alert("On-premise software is installed locally, on a company's own computers and servers.");
  }
  else {
    window.alert("Cloud-based software is hosted on the vendor's servers and accessed through a web browser.");
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
