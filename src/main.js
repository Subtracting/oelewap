import './style.css';
import politicians from './politicians.json';
import { pickNextProfile } from './profile-picker.js';

const historyKey = 'oelewappers-recent-v1';
const params = new URLSearchParams(window.location.search);
const requestedId = params.get('id');
let recent = [];

try {
  const saved = JSON.parse(sessionStorage.getItem(historyKey) || '[]');
  if (Array.isArray(saved)) recent = saved.filter(id => politicians.some(person => person.name === id));
} catch {
  recent = [];
}

const profile = requestedId
  ? politicians.find(person => person.name.toLocaleLowerCase('nl') === requestedId.toLocaleLowerCase('nl')) || pickNextProfile(politicians, recent)
  : pickNextProfile(politicians, recent);

if (profile) {
  recent = [...recent.filter(id => id !== profile.name), profile.name].slice(-politicians.length);
  try { sessionStorage.setItem(historyKey, JSON.stringify(recent)); } catch { /* A private browsing session may disable storage. */ }
}

const app = document.querySelector('#app');

if (!profile) {
  app.innerHTML = '<main class="page"><p>Geen profielen beschikbaar.</p></main>';
} else {
  app.innerHTML = `
    <main class="page">
      <header class="topbar">
        <a class="wordmark" href="/" aria-label="Oelewappers, ververs voor een ander gezicht">Oelewappers<span class="wordmark-dot">.</span></a>
        <span class="top-note"><span class="live-dot"></span> De Haagse editie</span>
      </header>

      <section class="feature" aria-labelledby="person-name">
        <div class="photo-wrap">
          <div class="photo-meta"><span>UIT HET BINNENHOF</span><span class="issue">№ 001 — NL</span></div>
          <img class="portrait" src="${profile.image}" alt="Portret van ${profile.name}" fetchpriority="high" />
          <div class="photo-caption"><span>Een gezicht. Een verhaal.</span><span>DEN HAAG&nbsp; / &nbsp;NEDERLAND</span></div>
        </div>

        <div class="profile-info">
          <div class="kicker"><span class="kicker-line"></span> DE POLITIEK, VANDAAG</div>
          <h1 id="person-name">${profile.name}</h1>
          <p class="role">${profile.role}</p>
          <div class="rule"></div>
          <p class="description">${profile.roast}</p>
          <div class="actions">
            <a class="button" href="/" aria-label="Bekijk een andere politicus" title="Een ander gezicht, ook met spatie"><span>Volgende wapper</span><span class="arrow" aria-hidden="true">↗</span></a>
            <span class="refresh-hint"><kbd>↻</kbd> of ververs de pagina</span>
          </div>
          <div class="source"><span class="source-label">KAMERPROFIEL</span><a href="${profile.tweedekamer}" target="_blank" rel="noreferrer">${profile.credit}<span aria-hidden="true"> ↗</span></a></div>
        </div>
      </section>

      <footer class="footer"><span>Een klein beetje Haagse drukte.</span><span>GEMAAKT MET <span class="heart">♥</span> IN NEDERLAND</span></footer>
    </main>
  `;

  const portrait = app.querySelector('.portrait');
  portrait.addEventListener('error', () => {
    portrait.classList.add('image-error');
    portrait.alt = `Portret niet beschikbaar voor ${profile.name}`;
    portrait.removeAttribute('src');
  }, { once: true });
}
