//we are not using this file atm

function myMap() {
var mapProp= {
  center:new google.maps.LatLng(51.508742,-0.120850),
  zoom:5,
};
var map = new google.maps.Map(document.getElementById("map"),mapProp);
}


function initMap() {
  const uluru = {
      lat: -25.344,
      lng: 131.036
  };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: uluru,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
      position: uluru,
      map: map,
  });
}


function sendName() {
  return function() {
      var data = '';
      data = getInputValue();
      console.log(data);

      $.ajax({
          method: "GET",
          url: 'http://localhost:5000/' + data,
          data: JSON.stringify(data),
          headers: {
              "Accept": "application/json"
          }
      }).done(function(result) {});
  }
}