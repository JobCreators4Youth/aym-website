(function () {
  var el = document.getElementById("aym-map");
  if (!el || !window.L) return;

  var map = L.map(el, { center: [22, -25], zoom: 2, minZoom: 2, maxZoom: 6, scrollWheelZoom: false, worldCopyJump: true, attributionControl: false });
  L.control.attribution({ prefix: false }).addTo(map).addAttribution("Map data: Johan Sundström / Leaflet");

  fetch("https://cdn.jsdelivr.net/gh/johan/world.geo.json@master/countries.geo.json")
    .then(function (r) { return r.json(); })
    .then(function (data) {
      L.geoJSON(data, { interactive: false, style: { fillColor: "#315640", fillOpacity: 1, color: "#173c2e", weight: 1 } }).addTo(map);
    }).catch(function () {});

  var dot = L.divIcon({ className: "map-pin", html: "<span></span>", iconSize: [22, 22], iconAnchor: [11, 11], popupAnchor: [0, -12] });
  var places = [
    { at: [7.6, -11.8], tag: "Operational base", name: "Sierra Leone", text: "Community programs, youth enterprise, and locally led development.", href: "where-sierra-leone.html" },
    { at: [43.1, -89.5], tag: "Coordination &amp; partnerships", name: "United States", text: "Partnerships and resources supporting AYM’s work across communities.", href: "where-usa.html" }
  ];

  places.forEach(function (p) {
    var m = L.marker(p.at, { icon: dot, title: p.name }).addTo(map);
    m.bindPopup('<span class="map-pop__tag">' + p.tag + '</span><strong>' + p.name + '</strong><p>' + p.text + '</p><a class="btn btn--link" href="' + p.href + '">Learn more</a>', { closeButton: false, offset: [0, -4] });
    m.on("mouseover", function () { m.openPopup(); });
  });
})();