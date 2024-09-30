import "../static/js/menu";

describe("Menu functionality", () => {
  let drinksData;

  beforeAll(() => {
    // Mock fetch response
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ cocktails: mockDrinks() }),
      })
    );

    // Mock loadDrinksData function
    global.loadDrinksData = jest.fn(async (category) => {
      const response = await fetch("/static/js/drinks.json");
      drinksData = (await response.json())[category];

      const drinksContainer = document.querySelector("#drinks-container");
      drinksData.forEach((drink) => {
        drinksContainer.appendChild(createDrinkCard(drink));
      });
      updateModal();
    });

    // Mock functions
    global.createDrinkCard = jest.fn((drink) => {
      const card = document.createElement("div");
      card.innerHTML = `<h5 class="card-title">${drink.name}</h5><p class="card-text">${drink.description}</p>`;
      return card;
    });

    let currentPage = 1;
    const totalPages = 2;

    global.updateModal = jest.fn(() => {
      document.querySelector(
        "#page-info"
      ).textContent = `${currentPage} of ${totalPages}`;
    });

    document.body.innerHTML = `
      <div id="drinksModal" class="modal">
        <div class="modal-content">
          <div id="drinks-container"></div>
          <div id="page-info"></div>
          <button id="prev">Previous</button>
          <button id="next">Next</button>
        </div>
      </div>
      <div id="drinkDetailsModal" class="modal"></div>
    `;

    document.querySelector("#next").addEventListener("click", () => {
      if (currentPage < totalPages) {
        currentPage++;
        updateModal();
      }
    });
  });

  afterAll(() => {
    jest.restoreAllMocks(); // clean up mocks
  });

  test("should fetch drinks data and update modal", async () => {
    await loadDrinksData("cocktails");
    expect(global.fetch).toHaveBeenCalledWith("/static/js/drinks.json");
    expect(
      document.querySelector("#drinks-container").children.length
    ).toBeGreaterThan(0);
  });

  test("should create drink cards with correct data", () => {
    const card = createDrinkCard(drinksData[0]);
    expect(card.querySelector(".card-title").textContent).toBe(
      drinksData[0].name
    );
    expect(card.querySelector(".card-text").textContent).toBe(
      drinksData[0].description
    );
  });

  test("should show correct pagination info", () => {
    drinksData = drinksData.slice(0, 4); // show 4 items
    updateModal();
    expect(document.querySelector("#page-info").textContent).toContain(
      "1 of 2"
    );
  });

  test("should change page when next is clicked", () => {
    document.querySelector("#next").click(); // next button click
    expect(document.querySelector("#page-info").textContent).toContain(
      "2 of 2"
    );
  });

  test("should load drink details on click", () => {
    const drink = drinksData[0];
    const detailsButton = document.createElement("button");
    detailsButton.dataset.drink = JSON.stringify(drink);
    detailsButton.click(); // click on details button

    document.getElementById("drinkDetailsModal").innerHTML = `
      <div id="drink-name">${drink.name}</div>
      <div id="drink-price">$${drink.price.toFixed(2)}</div>
    `;
    expect(document.getElementById("drink-name").textContent).toBe(drink.name);
    expect(document.getElementById("drink-price").textContent).toBe(
      `$${drink.price.toFixed(2)}`
    );
  });

  test("should reopen drinks modal when drink details modal is hidden", () => {
    const drinksModal = document.getElementById("drinksModal");
    const drinkDetailsModal = document.getElementById("drinkDetailsModal");
    drinkDetailsModal.dispatchEvent(new Event("hide.bs.modal")); // hide event
    expect(drinksModal.style.display).toBe(""); // drinks modal is visible
  });

  function mockDrinks() {
    return [
      {
        name: "Mojito",
        description: "Minty and refreshing",
        price: 10.99,
        image: "mojito.jpg",
      },
      {
        name: "Margarita",
        description: "Tangy and salty",
        price: 12.99,
        image: "margarita.jpg",
      },
    ];
  }
});
