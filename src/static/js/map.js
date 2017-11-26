// $.getJSON('eatwhat.json', function(json) {
//     var data_size = json.eatwhat.length;
//     var randon_seed = Math.floor(Math.random() * data_size);
//     document.getElementById("address").value = json.eatwhat[randon_seed].address;
//     var show_strisng = "今天吃" + json.eatwhat[randon_seed].address + "的" + json.eatwhat[randon_seed].storeName;
//     document.getElementById('store').innerHTML = show_string;
// });

//google map js
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 19,
        center: {
            lat: 25.034007,
            lng: 121.559811
        }
    });
    var geocoder = new google.maps.Geocoder();
    document.getElementById('submit').addEventListener('click', function() {
        geocodeAddress(geocoder, map);
    });
    window.onload = function() {
        geocodeAddress(geocoder, map);
    }
}

function geocodeAddress(geocoder, resultsMap) {
    var address = document.getElementById('address').value;
    geocoder.geocode({
        'address': address
    }, function(results, status) {
        if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: resultsMap,
                position: results[0].geometry.location
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}

document.getElementById('next').addEventListener('click', function() {
    window.location.reload();
});
