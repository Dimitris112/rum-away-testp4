document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript file loaded.");

  // Click listener for category buttons
  const categoryButtons = document.querySelectorAll(".btn-category");
  categoryButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const category = this.getAttribute("data-category");
      loadDrinksData(category);
    });

    button.addEventListener("mouseover", function () {
      this.classList.add("animate__animated", "animate__rubberBand");
    });

    button.addEventListener("mouseout", function () {
      this.classList.remove("animate__animated", "animate__rubberBand");
    });
  });

  function loadDrinksData(category) {
    fetch("/static/js/drinks.json")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Data fetched:", data);
        const drinksData = data[category];
        if (drinksData) {
          updateModal(category, drinksData);
        } else {
          console.error("No drinks data found for category:", category);
        }
      })
      .catch((error) => console.error("Error fetching drinks data:", error));
  }

  // Update modal with drinks data
  function updateModal(category, drinksData) {
    const modalTitle = document.querySelector("#drinksModalLabel");
    const modalDescription = document.querySelector("#modal-description");
    const drinksContainer = document.querySelector("#drinks-container");

    modalTitle.textContent = category;
    modalDescription.textContent = `Explore our exquisite selection of ${category}.`;

    drinksContainer.innerHTML = "";

    drinksData.forEach((drink) => {
      const drinkCard = createDrinkCard(drink);
      drinksContainer.appendChild(drinkCard);
    });

    const modalContent = document.querySelector(".modal-content");
    modalContent.classList.add("animate__animated", "animate__fadeIn");
  }

  // Card for each drink
  function createDrinkCard(drink) {
    const colDiv = document.createElement("div");
    colDiv.classList.add(
      "col-md-6",
      "mb-4",
      "animate__animated",
      "animate__fadeInUp"
    );

    const cardDiv = document.createElement("div");
    cardDiv.classList.add("card", "border-light", "shadow-lg", "rounded");

    const img = document.createElement("img");
    img.src = `/static/images/menu/${drink.image}`;
    img.classList.add("card-img-top");
    img.alt = drink.name;

    const cardBodyDiv = document.createElement("div");
    cardBodyDiv.classList.add("card-body", "text-center");

    const title = document.createElement("h5");
    title.classList.add("card-title", "text-primary");
    title.textContent = drink.name;

    const description = document.createElement("p");
    description.classList.add("card-text");
    description.textContent = drink.description;

    const price = document.createElement("p");
    price.classList.add("text-muted");
    price.textContent = `$${drink.price.toFixed(2)}`;

    cardBodyDiv.appendChild(title);
    cardBodyDiv.appendChild(description);
    cardBodyDiv.appendChild(price);

    cardDiv.appendChild(img);
    cardDiv.appendChild(cardBodyDiv);

    colDiv.appendChild(cardDiv);

    return colDiv;
  }
});
