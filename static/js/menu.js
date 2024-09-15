document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript file loaded.");

  const itemsPerPage = 4;
  let currentPage = 1;
  let currentCategory = null;
  let drinksData = [];
  let lastState = { page: 1, category: null }; // stores last state

  // Click listener for category buttons
  const categoryButtons = document.querySelectorAll(".btn-category");
  categoryButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const category = this.getAttribute("data-category");
      currentCategory = category;
      lastState.category = category;
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
          currentPage = 1;
          updateModal();
        } else {
          console.error("No drinks data found for category:", category);
        }
      })
      .catch((error) => console.error("Error fetching drinks data:", error));
  }

  function updateModal() {
    const modalTitle = document.querySelector("#drinksModalLabel");
    const modalDescription = document.querySelector("#modal-description");
    const drinksContainer = document.querySelector("#drinks-container");
    const pageInfo = document.querySelector("#page-info");
    const prevContainer = document.querySelector("#prev-container");
    const nextContainer = document.querySelector("#next-container");

    modalTitle.textContent = currentCategory;
    modalDescription.textContent = `Explore our exquisite selection of ${currentCategory}.`;

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

    const detailsButton = document.createElement("button");
    detailsButton.classList.add("btn", "btn-info");
    detailsButton.textContent = "View Details";
    detailsButton.setAttribute("data-drink", JSON.stringify(drink));
    detailsButton.setAttribute("data-bs-toggle", "modal");
    detailsButton.setAttribute("data-bs-target", "#drinkDetailsModal");

    cardBodyDiv.appendChild(title);
    cardBodyDiv.appendChild(description);
    cardBodyDiv.appendChild(price);
    cardBodyDiv.appendChild(detailsButton);

    cardDiv.appendChild(img);
    cardDiv.appendChild(cardBodyDiv);

    colDiv.appendChild(cardDiv);

    return colDiv;
  }

  // Event listeners for pagination
  document.querySelector("#prev").addEventListener("click", function () {
    if (currentPage > 1) {
      currentPage--;
      updateModal();
    }
  });

  document.querySelector("#next").addEventListener("click", function () {
    const totalPages = Math.ceil(drinksData.length / itemsPerPage);
    if (currentPage < totalPages) {
      currentPage++;
      updateModal();
    }
  });

  // Event listener for drink details
  document.addEventListener("click", function (event) {
    if (event.target.dataset.drink) {
      const drink = JSON.parse(event.target.dataset.drink);
      document.getElementById("drink-name").textContent = drink.name;
      document.getElementById("drink-description").textContent = drink.details;
      document.getElementById(
        "drink-price"
      ).textContent = `$${drink.price.toFixed(2)}`;
      document.getElementById(
        "drink-image"
      ).src = `/static/images/menu/${drink.image}`;
    }
  });

  // Keep the drinks modal open when drink details modal is shown
  const drinkDetailsModal = document.getElementById("drinkDetailsModal");
  drinkDetailsModal.addEventListener("show.bs.modal", function () {
    const drinksModal = document.getElementById("drinksModal");
    const drinksModalInstance = bootstrap.Modal.getInstance(drinksModal);
    if (drinksModalInstance && drinksModalInstance._isShown) {
      drinksModalInstance._backdrop.classList.add("show");
    }
  });

  // When drink details modal is hidden, make sure drinks modal stays open
  drinkDetailsModal.addEventListener("hide.bs.modal", function () {
    setTimeout(() => {
      const drinksModal = document.getElementById("drinksModal");
      const drinksModalInstance = bootstrap.Modal.getInstance(drinksModal);
      if (drinksModalInstance && !drinksModalInstance._isShown) {
        drinksModalInstance.show();
      }
    }, 200);
  });

  // Drinks modal reopens
  const drinksModal = document.getElementById("drinksModal");
  drinksModal.addEventListener("shown.bs.modal", function () {
    updateModal();
  });
});
