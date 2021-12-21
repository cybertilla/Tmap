function myMap() {
var mapProp= {
  center:new google.maps.LatLng(51.508742,-0.120850),
  zoom:5,
};
var map = new google.maps.Map(document.getElementById("map"),mapProp);
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