var searchbar = document.querySelector(".search");

function slide(){
    if(searchbar.classList.contains("hide")){
        searchbar.classList.remove("hide");
    }
    else{
        searchbar.classList.add("hide");
    }
}

function initMap(){
    var location = {lat: 24.903561, lng: 91.873611};
    var map = new google.maps.Map(document.getElementById("map"),{
        zoom: 4,
        center: location
    })
}