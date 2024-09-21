document.addEventListener("DOMContentLoaded", function () {
  const hourSelect = document.getElementById("res-hour");
  const minuteSelect = document.getElementById("res-minute");
  const hallSelect = document.getElementById("res-location");
  const guestsInput = document.getElementById("res-guests");
  const availableSpotsDisplay = document.getElementById("available-spots");

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
  });

  hallSelect.addEventListener("change", updateAvailableSpots);
  guestsInput.addEventListener("input", updateAvailableSpots);
  hourSelect.addEventListener("change", updateAvailableSpots);
  minuteSelect.addEventListener("change", updateAvailableSpots);

  // Update available spots
  async function updateAvailableSpots() {
    const hall = hallSelect.value;
    const hour = hourSelect.value;
    const minute = minuteSelect.value;
    const reservationTime = `${
      new Date().toISOString().split("T")[0]
    }T${hour}:${minute}`;

    if (hall && hour && minute) {
      try {
        const response = await fetch(
          `/get-availability?hall=${hall}&reservation_time=${reservationTime}`
        );
        const data = await response.json();

        const numGuests = parseInt(guestsInput.value) || 0;
        const spotsLeft = data.spots_left - numGuests;

        availableSpotsDisplay.textContent = `Available spots: ${spotsLeft} (Max: ${data.max_capacity})`;
      } catch (error) {
        console.error("Error fetching availability:", error);
      }
    }
  }

  // Validate reservation time - must be future time
  function validateReservationTime() {
    const currentHour = new Date().getHours();
    const currentMinute = new Date().getMinutes();

    hourSelect.addEventListener("change", checkFutureTime);
    minuteSelect.addEventListener("change", checkFutureTime);
    document
      .getElementById("res-date")
      .addEventListener("change", checkFutureTime);

    function checkFutureTime() {
      const selectedHour = parseInt(hourSelect.value);
      const selectedMinute = parseInt(minuteSelect.value);
      const selectedDate = new Date(document.getElementById("res-date").value);
      const currentDate = new Date();

      // If selected date is in the future allow any time
      if (selectedDate > currentDate) {
        return;
      }

      let isPastTime = false;

      //  Time is between 00:00 and 02:00 next day
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
