document.addEventListener("DOMContentLoaded", function () {
  const hourSelect = document.getElementById("res-hour");
  const minuteSelect = document.getElementById("res-minute");
  const hallSelect = document.getElementById("res-location");
  const guestsInput = document.getElementById("res-guests");
  const availableSpotsDisplay = document.getElementById("available-spots");
  const reservationDateInput = document.getElementById("res-date");

  // Hour options
  function populateHourOptions() {
    hourSelect.innerHTML = "";
    for (let i = 16; i <= 26; i++) {
      const option = document.createElement("option");
      const hourValue = i > 24 ? i - 24 : i; // Adjust for 24 hour format
      option.value = hourValue;
      option.textContent = (hourValue < 10 ? "0" : "") + hourValue + ":00"; // Format for display
      hourSelect.appendChild(option);
    }
  }

  // Minute options
  function populateMinuteOptions() {
    minuteSelect.innerHTML = "";
    for (let minute = 0; minute < 60; minute += 5) {
      const option = document.createElement("option");
      option.value = minute;
      option.textContent = minute < 10 ? "0" + minute : minute;
      minuteSelect.appendChild(option);
    }
  }

  populateHourOptions();
  populateMinuteOptions();

  // Event listeners for updates
  hourSelect.addEventListener("change", updateAvailableSpots);
  minuteSelect.addEventListener("change", updateAvailableSpots);
  hallSelect.addEventListener("change", updateAvailableSpots);
  guestsInput.addEventListener("input", updateAvailableSpots);
  reservationDateInput.addEventListener("change", updateAvailableSpots);

  async function updateAvailableSpots() {
    const hall = hallSelect.value;
    const hour = parseInt(hourSelect.value);
    const minute = parseInt(minuteSelect.value);
    const reservationDate = reservationDateInput.value;

    if (hall && !isNaN(hour) && !isNaN(minute) && reservationDate) {
      const reservationTime = new Date(reservationDate);
      reservationTime.setHours(hour, minute, 0); // Set hours and minutes

      try {
        const response = await fetch(
          `/get-availability?hall=${hall}&reservation_time=${reservationTime.toISOString()}`
        );

        if (!response.ok) throw new Error("Network response was not ok");

        const data = await response.json();
        const numGuests = parseInt(guestsInput.value) || 0;
        const spotsLeft =
          (data.spots_left ? parseInt(data.spots_left) : 0) - numGuests;

        availableSpotsDisplay.textContent = `Available spots: ${spotsLeft} (Total: ${data.max_capacity})`;

        if (spotsLeft < 0) {
          showAlert(
            `You can only reserve up to ${data.spots_left} spots.`,
            "danger"
          );
        }
      } catch (error) {
        console.error("Error fetching availability:", error);
        showAlert("Error fetching availability. Please try again.", "danger");
      }
    }
  }

  function validateReservationTime() {
    const currentDate = new Date();
    const maxReservationDate = new Date(currentDate);
    maxReservationDate.setMonth(currentDate.getMonth() + 6); // Max 6 months in advance

    function checkFutureTime() {
      const selectedHour = parseInt(hourSelect.value);
      const selectedMinute = parseInt(minuteSelect.value);
      const selectedDate = new Date(reservationDateInput.value);

      if (selectedDate < currentDate) {
        showAlert(
          "Please select a future date for your reservation.",
          "danger"
        );
        hourSelect.value = "";
        minuteSelect.value = "";
        return;
      }

      if (selectedDate > maxReservationDate) {
        showAlert(
          "Reservations can only be made up to 6 months in advance.",
          "danger"
        );
        hourSelect.value = "";
        minuteSelect.value = "";
        return;
      }

      // Set reservation time
      const reservationDateTime = new Date(selectedDate);
      reservationDateTime.setHours(selectedHour, selectedMinute, 0);

      if (reservationDateTime < currentDate) {
        showAlert(
          "Please select a future time for your reservation.",
          "danger"
        );
        hourSelect.value = "";
        minuteSelect.value = "";
      }
    }

    hourSelect.addEventListener("change", checkFutureTime);
    minuteSelect.addEventListener("change", checkFutureTime);
    reservationDateInput.addEventListener("change", checkFutureTime);
  }

  function showAlert(message, type) {
    const alertContainer = document.getElementById("alert-container");
    const alertElement = document.createElement("div");
    alertElement.className = `alert alert-${type} alert-dismissible fade show`;
    alertElement.role = "alert";
    alertElement.innerHTML =
      message +
      '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>';
    alertContainer.appendChild(alertElement);
  }

  validateReservationTime();
});
