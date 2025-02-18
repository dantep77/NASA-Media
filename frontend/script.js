const API_URL = "https://nasa-media-production.up.railway.app/search";
let page = 1;
let maxPage;

async function searchNASA() {
  const query = document.getElementById("searchQuery").value;
  if (!query) return (document.getElementById("results").innerHTML = "");

  const response = await fetch(
    `${API_URL}?q=${encodeURIComponent(query)}&page=${page}`
  );
  const data = await response.json();

  maxPage = Math.floor(data.count / 12);
  if (data.count % 12 !== 0) maxPage += 1;

  console.log(data.count);
  console.log(data.items);
  displayResults(data);
  if (!query) return (document.getElementById("results").innerHTML = "");
  updateArrows();
}

function displayResults(data) {
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  if (
    data.error === "Failed to fetch data from NASA API" ||
    data.length === 0
  ) {
    resultsDiv.innerHTML = "Failed to fetch data from NASA API";
    return;
  }

  data.items.forEach(async (item) => {
    const card = document.createElement("div");
    card.classList.add("card");
    const img = document.createElement("img");
    const imgLink = document.createElement("a");
    const title = document.createElement("h3");

    // Assign image attributes
    img.src = item.links[0].href;
    img.alt = item.data[0].title;
    img.title = item.data[0].title;
    imgLink.href = img.src;
    imgLink.target = "_blank";
    img.loading = "lazy";

    title.innerHTML = img.title;
    title.classList.add("details");

    imgLink.appendChild(img);
    card.append(imgLink);
    card.append(title);
    resultsDiv.appendChild(card);
  });
}

function updateArrows() {
  if (page > 1) {
    document.getElementById("prevPage").disabled = false;
  } else {
    document.getElementById("prevPage").disabled = true;
  }

  if (page >= maxPage) {
    document.getElementById("nextPage").disabled = true;
  } else {
    document.getElementById("nextPage").disabled = false;
  }
  document.getElementById("pageNumber").innerText = "Page " + page;
}

function changePage(change) {
  page += change;
  console.log(maxPage);
  console.log(page);
  window.scrollTo({ top: 0, behavior: "smooth"});
  updateArrows();
  searchNASA();
}

function resetPage() {
  page = 1;
}
