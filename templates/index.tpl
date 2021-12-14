<!DOCTYPE html>
<html>

<body>

<h1>My First Google Map</h1>

<div id="googleMap" style="width:100%;height:400px;"></div>

<script>
function initMap() {
var mapProp= {
  center:new google.maps.LatLng({{ lat }}, {{ long }}),
  zoom:5,
};
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
}
</script>

<script
  src="https://maps.googleapis.com/maps/api/js?key={{ key }}&callback=initMap&v=weekly"
  async></script>

<form name="newLoc" id="newLoc">
  <input type="hidden" name="id">
  <label for="name">Search new location</label>
  <input type="text">
  {% print(input) %}
  <button type="button" id="requestNewLoc">Send</button>
</form>

</body>
</html>
