const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE
    var x = document.getElementById("hiddenDiv");
    const input = document.getElementById("searchProduct").value;
    
    if (input != ""){
        x.style.display = "block"; //shows the results-table only when we search
    }
    // END CODE HERE
}

productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    const name = document.getElementById("product-name").value;
    const year = document.getElementById("product-year").value;
    const price = document.getElementById("product-price").value;
    const color = document.getElementById("product-color").value;
    const size = document.getElementById("product-size").value;

    // END CODE HERE
}
