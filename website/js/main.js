// Monroe Seasonal Co. — small site behaviors
(function () {
  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var links = document.getElementById('nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Estimate form — not connected to a backend yet (see README.md)
  var form = document.getElementById('estimate-form');
  if (form && !form.getAttribute('action')) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = document.getElementById('form-status');
      status.classList.add('show');
      status.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }

  // Pre-check services when arriving from a "Quote ..." link (contact.html?service=fall)
  var season = new URLSearchParams(location.search).get('service');
  if (season) {
    document.querySelectorAll('input[data-season="' + season + '"]').forEach(function (box) {
      box.checked = true;
    });
  }

  // Footer year
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
