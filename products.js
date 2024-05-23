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
    // // BEGIN CODE HERE
    // const name = document.getElementById("product-name").value;
    // const year = document.getElementById("product-year").value;
    // const price = document.getElementById("product-price").value;
    // const color = document.getElementById("product-color").value;
    // const size = document.getElementById("product-size").value;
    
    
    // if (!name || !price || !year || !color || !size){
    //     alert('Please fill all the fields');
    //     return;
    // }
    // const data = {name: name, year: year, price: price, color: color, size: size};
    // const response = fetch(api+"/add-product")
    // if (response.ok){
    //     alert('Added');
    //     document.getElementById("product-name").value = '';
    //     document.getElementById("product-year").value = '';
    //     document.getElementById("product-price").value = '';
    //     document.getElementById("product-color").value = '';
    //     document.getElementById("product-size").value = '';
    // }else{
    //     alert ('Error');
    // }
        // BEGIN CODE HERE
        const getName = document.getElementById("product-name");
        const getYear = document.getElementById("product-year");
        const getPrice = document.getElementById("product-price");
        const getColor = document.getElementById("product-color");
        const getSize = document.getElementById("product-size");
    
        const res = new XMLHttpRequest();
        res.open("POST", `http://127.0.0.1:5000/add-product`);
        res.onreadystatechange = () => {
            if (res.readyState == 4) {
                if (res.status == 200) {
                    alert(res.responseText);
                    getName.value="";
                    getYear.value="";
                    getPrice.value="";
                    getColor.value="";
                    getSize.value="";
                }
            }
        };
        res.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        res.send(JSON.stringify({
            name: getName.value,
            production_year: parseInt(getYear.value),
                price: parseInt(getPrice.value),
                color: parseInt(getColor.value),
                size: parseInt(getSize.value)
         }))



    
    // END CODE HERE
}
