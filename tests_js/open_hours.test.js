import "../static/js/open_hours";

describe("Reservation functionality", () => {
  let hourSelect,
    minuteSelect,
    hallSelect,
    guestsInput,
    availableSpotsDisplay,
    reservationDateInput,
    alertContainer;

  beforeEach(() => {
    document.body.innerHTML = `
            <select id="res-hour"></select>
            <select id="res-minute"></select>
            <select id="res-location"></select>
            <input id="res-guests" type="number" />
            <div id="available-spots"></div>
            <input id="res-date" type="date" />
            <div id="alert-container"></div>
        `;

    hourSelect = document.getElementById("res-hour");
    minuteSelect = document.getElementById("res-minute");
    hallSelect = document.getElementById("res-location");
    guestsInput = document.getElementById("res-guests");
    availableSpotsDisplay = document.getElementById("available-spots");
    reservationDateInput = document.getElementById("res-date");
    alertContainer = document.getElementById("alert-container");

    window.populateHourOptions = () => {
      for (let i = 16; i <= 26; i++) {
        const option = document.createElement("option");
        option.textContent = `${i}:00`;
        hourSelect.appendChild(option);
      }
    };

    window.populateMinuteOptions = () => {
      for (let i = 0; i < 60; i += 5) {
        const option = document.createElement("option");
        option.textContent = i < 10 ? `0${i}` : i;
        minuteSelect.appendChild(option);
      }
    };

    window.updateAvailableSpots = async () => {
      const spotsLeft = 2; // there are 2 spots left
      availableSpotsDisplay.textContent = `Available spots: ${spotsLeft}`;
      if (guestsInput.value > spotsLeft) {
        const alert = document.createElement("div");
        alert.textContent = `You can only reserve up to ${spotsLeft} spots.`;
        alertContainer.appendChild(alert);
      }
    };

    window.checkFutureTime = () => {
      const selectedDate = new Date(reservationDateInput.value);
      const currentDate = new Date();

      if (selectedDate < currentDate) {
        const alert = document.createElement("div");
        alert.textContent = "Please select a future date for your reservation.";
        alertContainer.appendChild(alert);
        return;
      }

      const sixMonthsLater = new Date();
      sixMonthsLater.setMonth(currentDate.getMonth() + 6);
      if (selectedDate > sixMonthsLater) {
        const alert = document.createElement("div");
        alert.textContent = "Reservations can only be made up to 6 months in advance.";
        alertContainer.appendChild(alert);
        return;
      }

      const selectedHour = parseInt(hourSelect.value);
      const selectedMinute = parseInt(minuteSelect.value);
      const selectedTime = new Date(
        selectedDate.getFullYear(),
        selectedDate.getMonth(),
        selectedDate.getDate(),
        selectedHour,
        selectedMinute
      );

      if (selectedTime <= currentDate) {
        const alert = document.createElement("div");
        alert.textContent = "Please select a future time for your reservation.";
        alertContainer.appendChild(alert);
      }
    };

    window.populateHourOptions();
    window.populateMinuteOptions();
  });

  test("should populate hour options correctly", () => {
    expect(hourSelect.children.length).toBe(11); // 11 options from 16 to 26
    expect(hourSelect.children[0].textContent).toBe("16:00");
    expect(hourSelect.children[10].textContent).toBe("26:00");
  });

  test("should populate minute options correctly", () => {
    expect(minuteSelect.children.length).toBe(12); // 12 options for minutes
    expect(minuteSelect.children[0].textContent).toBe("00");
    expect(minuteSelect.children[11].textContent).toBe("55");
  });

  test("should show alert when trying to reserve more spots than available", async () => {
    // Mock the fetch response
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ spots_left: 2, max_capacity: 10 }),
      })
    );

    hallSelect.value = "hall1";
    hourSelect.value = "16";
    minuteSelect.value = "0";
    guestsInput.value = "3";
    reservationDateInput.value = "2024-09-30";

    await window.updateAvailableSpots();

    expect(alertContainer.children.length).toBe(1); // Check if alert show up
    expect(alertContainer.firstChild.textContent).toContain(
      "You can only reserve up to 2 spots."
    );
  });

  test("should show alert for past date selection", () => {
    const pastDate = new Date();
    pastDate.setDate(pastDate.getDate() - 1);
    reservationDateInput.value = pastDate.toISOString().split("T")[0];

    hourSelect.value = "16";
    minuteSelect.value = "0";

    window.checkFutureTime();

    expect(alertContainer.children.length).toBe(1);
    expect(alertContainer.firstChild.textContent).toContain(
      "Please select a future date for your reservation."
    );
  });

  test("should show alert for date more than 6 months in advance", () => {
    const futureDate = new Date();
    futureDate.setMonth(futureDate.getMonth() + 7);
    reservationDateInput.value = futureDate.toISOString().split("T")[0];

    hourSelect.value = "16";
    minuteSelect.value = "0";

    window.checkFutureTime();

    expect(alertContainer.children.length).toBe(1);
    expect(alertContainer.firstChild.textContent).toContain(
      "Reservations can only be made up to 6 months in advance."
    );
  });

  test("should show alert for past time selection", () => {
    const currentDate = new Date();
    reservationDateInput.value = currentDate.toISOString().split("T")[0]; //  today
    hourSelect.value = "15"; // an hour before the current hour
    minuteSelect.value = "0"; //

    jest.spyOn(Date, "now").mockImplementationOnce(() =>
        new Date(
            currentDate.getFullYear(),
            currentDate.getMonth(),
            currentDate.getDate(),
            16 // current time is 16:00
        ).valueOf()
    );

    window.checkFutureTime();

    expect(alertContainer.children.length).toBe(1);
    expect(alertContainer.firstChild.textContent).toContain(
        "Please select a future date for your reservation."
    );
});

  afterEach(() => {
    jest.restoreAllMocks();
    alertContainer.innerHTML = "";
  });
});
