
const findcity = () => {
    const status = document.querySelector('.status');

    const success = (position) => {
      console.log(position);
       const  latitude = position.coords.latitude;
       const  longitude = position.coords.longitude;
       let x = latitude.toFixed(10);
       let y = longitude.toFixed(10);




      const geoApiUrl = 'https://nominatim.openstreetmap.org/reverse?format=geojson&lat=${x}&lon=${y}'


      fetch(geoApiUrl)
      .then(res => res.json())
      .then(data =>{
        console.log(data)
        status.textContent = data.city
      })
  }








  const error = () => {
    status.textContent = 'Unable to find location';
  }


  var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  };



  navigator.geolocation.getCurrentPosition(success, error, [options]);
}



document.querySelector('.find-city').addEventListener('click',findcity);
