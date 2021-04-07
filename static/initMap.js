let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 16,
    center: new google.maps.LatLng(-33.91722, 151.23064),
    mapTypeId: "roadmap",
  });
  const iconBase = "https://maps.google.com/mapfiles/kml/paddle/";
  const icons = {
    bank: {
      name: "Food Bank",
      icon: iconBase + "B.png",
    },
    distribution: {
      name: "Distribution Location",
      icon: iconBase + "D.png",
    },
    partner: {
      name: "Partners",
      icon: iconBase + "P.png",
    },
  };
  const features = [
    {
      position: new google.maps.LatLng(-33.91721, 151.2263),
      type: "bank",
    },
    {
      position: new google.maps.LatLng(-33.91665018901448, 151.2282474695587),
      type: "partner",
    },
    {
      position: new google.maps.LatLng(-33.91727341958453, 151.23348314155578),
      type: "distribution",
    },
  ];
  features.forEach((feature) => {
    new google.maps.Marker({
      position: feature.position,
      icon: icons[feature.type].icon,
      map: map,
    });
  });
  const legend = document.getElementById("legend");

  for (const key in icons) {
    const type = icons[key];
    const name = type.name;
    const icon = type.icon;
    const div = document.createElement("div");
    div.innerHTML = '<img src="' + icon + '"> ' + name;
    legend.appendChild(div);
  }
  map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
}