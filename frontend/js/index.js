// js/index.js
document.addEventListener('DOMContentLoaded', async () => {
  const wineList = document.getElementById('wine-list');
  const form = document.getElementById('add-wine-form');

  // Carrega vinhos
  const wines = await getWines();
  wines.forEach(wine => {
    const li = document.createElement('li');
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    li.innerHTML = `
      <span>${wine.name}</span>
      <a class="btn btn-sm btn-primary" href="wine_detail.html?id=${wine.id}">Detalhes</a>
    `;
    wineList.appendChild(li);
  });

  // Formulário de adicionar vinho
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('wineName').value;
    const grape = document.getElementById('wineGrape').value || null;
    const description = document.getElementById('wineDescription').value || null;
    const image_url = document.getElementById('wineImageUrl').value || null;

    const newWine = await createWine({name, grape, description, image_url});
    
    // Atualizar a lista
    const li = document.createElement('li');
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    li.innerHTML = `
      <span>${newWine.name}</span>
      <a class="btn btn-sm btn-primary" href="wine_detail.html?id=${newWine.id}">Detalhes</a>
    `;
    wineList.appendChild(li);

    // Limpa o formulário
    form.reset();
  });
});
