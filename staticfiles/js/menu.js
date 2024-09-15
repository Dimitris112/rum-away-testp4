document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript file loaded.");

  const itemsPerPage = 4; // Number of items per page
  let currentPage = 1;
  let drinksData = [];

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
        drinksData = data[category] || [];
        if (drinksData.length > 0) {
          currentPage = 1; // Reset to the first page
          updateModal(category);
        } else {
          console.error("No drinks data found for category:", category);
        }
      })
      .catch((error) => console.error("Error fetching drinks data:", error));
  }

  // Update modal with drinks data and pagination
  function updateModal(category) {
    const modalTitle = document.querySelector("#drinksModalLabel");
    const modalDescription = document.querySelector("#modal-description");
    const drinksContainer = document.querySelector("#drinks-container");
    const pageInfo = document.querySelector("#page-info");
    const prevContainer = document.querySelector("#prev-container");
    const nextContainer = document.querySelector("#next-container");

    modalTitle.textContent = category;
    modalDescription.textContent = `Explore our exquisite selection of ${category}.`;

    // Pagination logic
    const totalPages = Math.ceil(drinksData.length / itemsPerPage);
    pageInfo.innerHTML = `<span class="page-number">${currentPage}</span> of <span class="page-total">${totalPages}</span>`;

    drinksContainer.innerHTML = "";

    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const currentDrinks = drinksData.slice(start, end);

    currentDrinks.forEach((drink) => {
      const drinkCard = createDrinkCard(drink);
      drinksContainer.appendChild(drinkCard);
    });

    // Show-hide pagination buttons
    prevContainer.style.display = currentPage > 1 ? "inline-block" : "none";
    nextContainer.style.display =
      currentPage < totalPages ? "inline-block" : "none";

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

  // Event listeners for pagination
  document.querySelector("#prev").addEventListener("click", function () {
    if (currentPage > 1) {
      currentPage--;
      updateModal(document.querySelector("#drinksModalLabel").textContent);
    }
  });

  document.querySelector("#next").addEventListener("click", function () {
    const totalPages = Math.ceil(drinksData.length / itemsPerPage);
    if (currentPage < totalPages) {
      currentPage++;
      updateModal(document.querySelector("#drinksModalLabel").textContent);
    }
  });
});
