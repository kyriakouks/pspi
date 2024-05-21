const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE
    
    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE
    try {
        const response = fetch(api+"/search");    
    } catch (error) {
        console.log("you  fucked  up");
    }
    
    var x = document.getElementById("hiddenDiv");
    const input = document.getElementById("searchProduct").value;
    
    if (input != ""){
        x.style.display = "block"; //shows the results-table only when we search
    }else{
        x.style.display = "none";  //hides the table when input is null
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
    
    
    if (!name || !price || !year || !color || !size){
        alert('Please fill all the fields');
        return;
    }
    const data = {name: name, year: year, price: price, color: color, size: size};
    const response = fetch('http://127.0.0.1:5500/products.html/add-product', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)});
    if (response.ok){
        alert('Added');
        document.getElementById("product-name").value = '';
        document.getElementById("product-year").value = '';
        document.getElementById("product-price").value = '';
        document.getElementById("product-color").value = '';
        document.getElementById("product-size").value = '';
    }else{
        alert ('Error');
    }
    
    // END CODE HERE
}
