document.addEventListener("DOMContentLoaded", function () {
  const hourSelect = document.getElementById("res-hour");
  const minuteSelect = document.getElementById("res-minute");

  // Hour options from 16:00 to 02:00
  for (let i = 16; i <= 26; i++) {
    const option = document.createElement("option");
    option.value = i > 24 ? i - 24 : i; // 02:00 being 26 in the loop
    option.textContent = (i > 24 ? i - 24 : i) + ":00";
    hourSelect.appendChild(option);
  }

  hourSelect.addEventListener("change", function () {
    const selectedHour = parseInt(hourSelect.value);
    minuteSelect.innerHTML = "";

    for (let minute = 0; minute < 60; minute += 5) {
      const option = document.createElement("option");
      option.value = minute < 10 ? "0" + minute : minute;
      option.textContent = option.value;
      minuteSelect.appendChild(option);
    }

    if (selectedHour === 2) {
      minuteSelect.innerHTML = "";
      for (let minute = 0; minute < 60; minute += 5) {
        const option = document.createElement("option");
        option.value = minute < 10 ? "0" + minute : minute;
        option.textContent = option.value;
        minuteSelect.appendChild(option);
      }
    }
  });

  // Validate reservation time - must be future time
  function validateReservationTime() {
    const currentHour = new Date().getHours();
    const currentMinute = new Date().getMinutes();

    hourSelect.addEventListener("change", checkFutureTime);
    minuteSelect.addEventListener("change", checkFutureTime);

    function checkFutureTime() {
      const selectedHour = parseInt(hourSelect.value);
      const selectedMinute = parseInt(minuteSelect.value);

      let isPastTime = false;

      // Current time is between 00:00 and 02:00 (next day)
      if (selectedHour < 16) {
        isPastTime =
          selectedHour + 24 < currentHour ||
          (selectedHour + 24 === currentHour && selectedMinute < currentMinute);
      } else {
        isPastTime =
          selectedHour < currentHour ||
          (selectedHour === currentHour && selectedMinute < currentMinute);
      }

      if (isPastTime) {
        alert("Please select a future time for your reservation.");
        hourSelect.value = "";
        minuteSelect.value = "";
      }
    }
  }

  validateReservationTime();
});
