// js/api.js
const API_URL = "https://wine-catalog-wle0.onrender.com"; // Substitua pela URL do seu backend

async function getWines() {
  const res = await fetch(`${API_URL}/wines`);
  return res.json();
}

async function createWine({name, grape, description, image_url}) {
  const res = await fetch(`${API_URL}/wines`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({name, grape, description, image_url})
  });
  return res.json();
}

async function getWineById(wine_id) {
  const res = await fetch(`${API_URL}/wines/${wine_id}`);
  if (!res.ok) {
    throw new Error('Wine not found');
  }
  return res.json();
}

async function createMoment(wine_id, {name, description, images}) {
  const res = await fetch(`${API_URL}/wines/${wine_id}/moments`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({name, description, images})
  });
  return res.json();
}
