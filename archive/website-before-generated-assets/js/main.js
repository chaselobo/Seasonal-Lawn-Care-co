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

  // Image placeholders: if the real photo exists at data-src, show it.
  // Drop a file with the matching name into images/photos/ and it appears.
  document.querySelectorAll('.asset[data-src]').forEach(function (fig) {
    var img = new Image();
    img.onload = function () {
      img.alt = fig.getAttribute('data-alt') || '';
      img.loading = 'lazy';
      fig.innerHTML = '';
      fig.appendChild(img);
      fig.classList.add('has-image');
    };
    img.src = fig.getAttribute('data-src');
  });

  // "Copy prompt" buttons on placeholders
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.asset__copy');
    if (!btn) return;
    var text = btn.parentElement.querySelector('.asset__prompt').innerText.replace(/^Prompt:\s*/i, '');
    var done = function () {
      btn.textContent = 'Copied ✓';
      setTimeout(function () { btn.textContent = 'Copy prompt'; }, 1600);
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, fallback);
    } else {
      fallback();
    }
    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); done(); } catch (err) {}
      ta.remove();
    }
  });

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
