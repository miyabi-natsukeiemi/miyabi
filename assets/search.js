/* Site search (the map on the top page and /search/). Data: assets/search-index.json, made by tools/search_build.py.
   window.OmSearch.load() fetches the index once; .find(query, {pref, cat, limit}) returns matching items, best first.
   Spelling variants match each other: both the index and the query go through norm(), which folds the usual ways of
   writing Japanese names in Russian and in Latin letters into one form (Нисеко = Нисэко = Niseko, Киото = Kyoto,
   Сибуя = Шибуя = Shibuya, Дзёдо = Джодо, Хоккайдо = Hokkaido). */
(function () {
  'use strict';
  var LAT = [['shi', 'си'], ['sh', 'с'], ['chi', 'ти'], ['ch', 'т'], ['tsu', 'цу'], ['ts', 'ц'], ['ji', 'дзи'], ['ja', 'дзя'],
    ['ju', 'дзю'], ['jo', 'дзё'], ['je', 'дзэ'], ['j', 'дз'], ['kh', 'х'], ['ya', 'я'], ['yu', 'ю'], ['yo', 'ё'], ['ye', 'е'],
    ['a', 'а'], ['b', 'б'], ['c', 'к'], ['d', 'д'], ['e', 'э'], ['f', 'ф'], ['g', 'г'], ['h', 'х'], ['i', 'и'], ['k', 'к'],
    ['l', 'р'], ['m', 'м'], ['n', 'н'], ['o', 'о'], ['p', 'п'], ['q', 'к'], ['r', 'р'], ['s', 'с'], ['t', 'т'], ['u', 'у'],
    ['v', 'в'], ['w', 'в'], ['x', 'кс'], ['y', 'й'], ['z', 'дз']];
  // after Latin letters became Cyrillic: fold the Russian spellings of Japanese sounds (order matters)
  var CYR = [[/ё/g, 'е'], [/[шщ]и/g, 'си'], [/[шщ]/g, 'с'], [/чи/g, 'ти'], [/ч/g, 'т'], [/дж/g, 'дз'], [/ж/g, 'дз'],
    [/дз/g, 'з'], [/тс/g, 'ц'], [/э/g, 'е'], [/й/g, 'и'], [/ы/g, 'и'], [/[ъь]/g, ''], [/ю/g, 'у'], [/я/g, 'а'],
    [/(^|[^а-я])кио/g, '$1ке'], [/кио/g, 'ке'], [/ио(?=[^а-я]|$)/g, 'е'], [/(.)\1+/g, '$1']];

  function norm(s) {
    s = String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');  // ō → o, й stays (NFD keeps it composed below)
    s = s.normalize('NFC');
    var out = '', i = 0;
    while (i < s.length) {
      var c = s[i], hit = null;
      if (c >= 'a' && c <= 'z') {
        for (var k = 0; k < LAT.length; k++) if (s.substr(i, LAT[k][0].length) === LAT[k][0]) { hit = LAT[k]; break; }
      }
      if (hit) { out += hit[1]; i += hit[0].length; } else { out += c; i++; }
    }
    for (var j = 0; j < CYR.length; j++) out = out.replace(CYR[j][0], CYR[j][1]);
    return out.replace(/[^0-9a-zа-я]+/g, ' ').trim();
  }

  var data = null, loading = null;
  function base() {
    var s = document.currentScript || document.querySelector('script[src*="assets/search.js"]');
    return s ? s.src.replace(/assets\/search\.js.*$/, '') : '/';
  }
  var BASE = base();

  function prep(d) {
    var pn = {};
    d.prefs.forEach(function (p) { pn[p.p] = p.n; });
    d.prefName = pn;
    d.items.forEach(function (e) {
      e.pn = pn[e.p] || '';
      e._t = ' ' + norm(e.t);
      e._x = ' ' + norm((e.x || []).join(' '));
      e._m = ' ' + norm(e.pn + ' ' + (e.g || '') + ' ' + (e.c || []).map(function (c) { return d.cats[c] || ''; }).join(' '));
      e._l = ' ' + norm(e.l || '');
    });
    return d;
  }

  function load() {
    if (data) return Promise.resolve(data);
    if (!loading) loading = fetch(BASE + 'assets/search-index.json').then(function (r) {
      if (!r.ok) throw new Error('search index: ' + r.status);
      return r.json();
    }).then(function (d) { data = prep(d); return data; });
    return loading;
  }

  // every word of the query must start a word somewhere in the item (title, places, prefecture/group/theme, lead);
  // the score prefers title, then places, then the rest
  function find(q, opt) {
    opt = opt || {};
    if (!data) return [];
    var words = norm(q).split(' ').filter(Boolean);
    var res = [];
    data.items.forEach(function (e) {
      if (opt.pref && e.p !== +opt.pref) return;
      if (opt.cat && (e.c || []).indexOf(opt.cat) < 0) return;
      if (opt.kind && e.k !== opt.kind) return;
      var score = 0;
      for (var i = 0; i < words.length; i++) {
        var w = ' ' + words[i];
        if (e._t.indexOf(w) >= 0) score += 10;
        else if (e._x.indexOf(w) >= 0) score += 6;
        else if (e._m.indexOf(w) >= 0) score += 4;
        else if (e._l.indexOf(w) >= 0) score += 1;
        else return;
      }
      if (!words.length) score = 1;
      if (e.k === 'g') score += words.length ? 3 : 0;
      res.push({ e: e, s: score });
    });
    res.sort(function (a, b) { return b.s - a.s || a.e.p - b.e.p; });
    var out = res.map(function (r) { return r.e; });
    return opt.limit ? out.slice(0, opt.limit) : out;
  }

  window.OmSearch = { norm: norm, load: load, find: find, base: BASE, get data() { return data; } };
})();
