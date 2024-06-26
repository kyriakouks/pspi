const api = "http://127.0.0.1:5000";

window.onload = () => {
  // You can add any initialization logic here if needed
};

searchButtonOnClick = (event) => {
  event.preventDefault();
  const name = document.getElementById("searchProduct").value;

  var x = document.getElementById("hiddenDiv");
  let request = new XMLHttpRequest();
  request.open("GET", api + "/search?name=" + encodeURIComponent(name));

  request.onreadystatechange = function () {
    if (request.readyState === XMLHttpRequest.DONE) {
      if (request.status === 200) {
        var data = JSON.parse(request.responseText);
        const table = document.getElementById("table-body-names");
        while (table.firstChild) {
          table.removeChild(table.firstChild);
        }
        data.forEach(result => {
          const row = table.insertRow();

          const td0 = row.insertCell(0);
          const td1 = row.insertCell(1);
          const td2 = row.insertCell(2);
          const td3 = row.insertCell(3);
          const td4 = row.insertCell(4);
          const td5 = row.insertCell(5);

          td0.innerText = result.id;
          td1.innerText = result.name;
          td2.innerText = result.production_year;
          td3.innerText = result.price;
          td4.innerText = result.color;
          td5.innerText = result.size;
        });

        // Show the result table
        x.style.display = "block";
      } else {
        console.error("Error");
      }
    }
  };

  request.send();
};



productFormOnSubmit = (event) => {
  const getName = document.getElementById("product-name").value;
  const getYear = document.getElementById("product-year").value;
  const getPrice = document.getElementById("product-price").value;
  const getColor = document.getElementById("product-color").value;
  const getSize = document.getElementById("product-size").value;

  if (!getName || !getPrice || !getYear || !getColor || !getSize) {
    return;
  }

  if (getColor < 1 || getColor > 3 || getSize < 1 || getSize > 4) {
    return;
  }

  const request = new XMLHttpRequest();
  request.open("POST", api + "/add-product");
  request.setRequestHeader("Content-Type", "application/json");
  const data = JSON.stringify({
    name: getName,
    production_year: parseInt(getYear),
    price: parseInt(getPrice),
    color: parseInt(getColor),
    size: parseInt(getSize),
  });

  request.onreadystatechange = function () {
    if (request.readyState === XMLHttpRequest.DONE) {
      if (request.status === 200) {
        document.getElementById("product-name").value = "";
        document.getElementById("product-year").value = "";
        document.getElementById("product-price").value = "";
        document.getElementById("product-color").value = "";
        document.getElementById("product-size").value = "";
      }
    }
  };
  request.send(data);
  alert("OK");
};
