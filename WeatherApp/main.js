async function getWeather() {
  const city = document.getElementById('city').value;
  if (!city) {
    alert('Please Enter a city!!');
    return;
  }

  try {
    const response = await fetch(`http://127.0.0.1:5000/weather?city=${city}`);
    const data = await response.json();

    if (data.error || data.Error) {
      document.getElementById('result').innerHTML = `<p>${data.error || data.Error}</p>`;
    } else {
      document.getElementById('result').innerHTML =
        `<h3>${data.city}</h3>` +
        `<p>Temperature: ${data.temperature}</p>` +
        `<p>Weather: ${data.description}</p>` +
        `<p>Humidity: ${data.humidity}</p>`;
    }
  } catch (error) {
    document.getElementById('result').innerHTML = `<p>Could not fetch weather data.</p>`;
  }
}