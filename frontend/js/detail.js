// js/detail.js
document.addEventListener('DOMContentLoaded', async () => {
  const params = new URLSearchParams(window.location.search);
  const wine_id = params.get('id');

  const wineNameEl = document.getElementById('wine-name');
  const wineDescriptionEl = document.getElementById('wine-description');
  const wineImageEl = document.getElementById('wine-image');
  const momentList = document.getElementById('moment-list');
  const momentForm = document.getElementById('add-moment-form');

  try {
    const wine = await getWineById(wine_id);
    wineNameEl.textContent = wine.name;
    wineDescriptionEl.textContent = wine.description || '';
    if (wine.image_url) {
      wineImageEl.src = wine.image_url;
      wineImageEl.alt = `Imagem do vinho ${wine.name}`;
    } else {
      wineImageEl.style.display = 'none';
    }

    // Listar momentos
    wine.moments.forEach(m => {
      const li = document.createElement('li');
      li.className = "list-group-item";
      li.innerHTML = `
        <h5>${m.name}</h5>
        <p>${m.description || ''}</p>
        <div class="d-flex flex-wrap">
          ${m.images.map(img => `<img src="${img.image_url}" class="img-fluid me-2 mb-2" style="max-width:100px;">`).join('')}
        </div>
      `;
      momentList.appendChild(li);
    });

  } catch (err) {
    console.error(err);
    alert('Erro ao carregar dados do vinho');
  }

  // Adicionar momento
  momentForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('momentName').value;
    const description = document.getElementById('momentDescription').value || null;
    const imagesRaw = document.getElementById('momentImages').value.trim();
    
    let images = [];
    if (imagesRaw) {
      images = imagesRaw.split('\n').map(url => url.trim()).filter(url => url.length > 0);
    }

    const newMoment = await createMoment(wine_id, {name, description, images});

    // Atualiza a lista de momentos
    const li = document.createElement('li');
    li.className = "list-group-item";
    li.innerHTML = `
      <h5>${newMoment.name}</h5>
      <p>${newMoment.description || ''}</p>
      <div class="d-flex flex-wrap">
        ${newMoment.images.map(img => `<img src="${img.image_url}" class="img-fluid me-2 mb-2" style="max-width:100px;">`).join('')}
      </div>
    `;
    momentList.appendChild(li);

    // Limpa o formulário
    momentForm.reset();
  });
});
