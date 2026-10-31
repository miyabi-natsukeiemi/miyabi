// How to reach us, for the whole site (homepage #ask, services page). TODO: fill in the real values.
// A value that still starts with "TODO" is not linked: the name stays plain text.
window.MIYABI_CONTACTS = {
  telegram: 'TODO_TELEGRAM_HANDLE',   // user name without @  → https://t.me/<handle>
  whatsapp: 'TODO_WHATSAPP_NUMBER',   // international number, digits only, e.g. 819012345678 → https://wa.me/<number>
  email: 'TODO_EMAIL'                 // e.g. hello@example.com → mailto:
};
(function(){
  var C = window.MIYABI_CONTACTS, URL = {
    telegram: function(v){ return 'https://t.me/' + v.replace(/^@/, ''); },
    whatsapp: function(v){ return 'https://wa.me/' + v.replace(/\D/g, ''); },
    email: function(v){ return 'mailto:' + v; }
  };
  function fill(){
    document.querySelectorAll('a[data-contact]').forEach(function(a){
      var k = a.getAttribute('data-contact'), v = C[k];
      if (!v || /^TODO/.test(v) || !URL[k]) return;
      a.href = URL[k](v);
      if (k !== 'email') { a.target = '_blank'; a.rel = 'noopener'; }
    });
  }
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fill) : fill();
})();
