document.addEventListener("DOMContentLoaded", function () {
  const hourSelect = document.getElementById("res-hour");
  const minuteSelect = document.getElementById("res-minute");

  // hour options 16:00 to 02:00
  for (let i = 16; i <= 26; i++) {
    const option = document.createElement("option");
    option.value = i;
    option.textContent = (i > 24 ? i - 24 : i) + ":00";
    hourSelect.appendChild(option);
  }

  // event listener to the hour select
  hourSelect.addEventListener("change", function () {
    const selectedHour = parseInt(hourSelect.value);
    minuteSelect.innerHTML = "";

    // minute options (00, 05, 10, ..., 55)
    for (let minute = 0; minute < 60; minute += 5) {
      const option = document.createElement("option");
      option.value = minute < 10 ? "0" + minute : minute;
      option.textContent = option.value;
      minuteSelect.appendChild(option);
    }

    if (selectedHour === 26) {
      // 02:00
      minuteSelect.innerHTML = "";
      for (let minute = 0; minute < 60; minute += 5) {
        if (minute <= 55) {
          const option = document.createElement("option");
          option.value = minute < 10 ? "0" + minute : minute;
          option.textContent = option.value;
          minuteSelect.appendChild(option);
        }
      }
    }
  });

  // validate reservation time
  function validateReservationTime() {
    const currentHour = new Date().getHours();
    const currentMinute = new Date().getMinutes();

    hourSelect.addEventListener("change", function () {
      checkFutureTime();
    });

    minuteSelect.addEventListener("change", function () {
      checkFutureTime();
    });

    function checkFutureTime() {
      const selectedHour = parseInt(hourSelect.value);
      const selectedMinute = parseInt(minuteSelect.value);
      if (
        selectedHour < currentHour ||
        (selectedHour === currentHour && selectedMinute < currentMinute)
      ) {
        alert("Please select a future time for your reservation.");
        hourSelect.value = "";
        minuteSelect.value = "";
      }
    }
  }

  validateReservationTime();
});
