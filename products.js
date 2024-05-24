const api = "http://127.0.0.1:5000";

window.onload = () => {
  // You can add any initialization logic here if needed
};

searchButtonOnClick = () => {
  const name = document.getElementById("searchProduct").value;
  var x = document.getElementById("hiddenDiv");
  fetch(api + "/search?name=" + encodeURIComponent(name))
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // Parse JSON response
    })
    .then((data) => {
        if (data.results.length < 1) {
            x.style.display = "none";
            return;
        }
      const existingTable = document.getElementsByClassName("result-table");
      console.log(existingTable)
      if (existingTable.length > 0) {
        existingTable.remove();
      }
      const table = document.getElementById("table-body-names");
      table.classList.add("result-table");
      for (result of data.results) {
        const row = table.insertRow();

        const td0 = row.insertCell(0);
        const td1 = row.insertCell(1);
        const td2 = row.insertCell(2);
        const td3 = row.insertCell(3);
        const td4 = row.insertCell(4);
        const td5 = row.insertCell(5);

        td0.innerText = result._id.$oid;
        td1.innerText = result.name;
        td2.innerText = result.year;
        td3.innerText = result.price;
        td4.innerText = result.color;
        td5.innerText = result.size;
        x.style.display = "block";
      }
      // You can update your UI or process the data here
    })
    .catch((error) => {
      console.error("An unexpected error occurred:", error);
    });

};

productFormOnSubmit = (event) => {
  const name = document.getElementById("product-name").value;
  const year = document.getElementById("product-year").value;
  const price = document.getElementById("product-price").value;
  const color = document.getElementById("product-color").value;
  const size = document.getElementById("product-size").value;

  if (!name || !price || !year || !color || !size) {
    alert("Please fill all the fields");
    return;
  }

  const data = {
    name: name,
    year: year,
    price: price,
    color: color,
    size: size,
  };

  fetch(api + "/add-product", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      alert("Added");
      document.getElementById("product-name").value = "";
      document.getElementById("product-year").value = "";
      document.getElementById("product-price").value = "";
      document.getElementById("product-color").value = "";
      document.getElementById("product-size").value = "";
    })
    .catch((error) => {
      console.error("Error adding product:", error);
      alert("Error adding product");
    });
};
