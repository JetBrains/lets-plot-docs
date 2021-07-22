document.addEventListener("DOMContentLoaded", function () {
  addLinkToPyPI();
  addLinkToGitHub();
  handlePreviewsSliders();
  handlePreviewsPickers();
  fixPanels();
  addTargetToExternalReferences();
  handlePreviewGallery();
});

function addLinkToPyPI() {
  const versionElem = document.querySelector("#navbar .navbar-version b");
  const versionParentElem = versionElem.parentElement;
  const linkElem = document.createElement("a");
  linkElem.href = "https://pypi.org/project/lets-plot";
  linkElem.classList.add("reference", "external");
  linkElem.appendChild(versionElem);
  versionParentElem.appendChild(linkElem);
}

function addLinkToGitHub() {
  const logoSize = document.getElementsByClassName('navbar-version')[0].clientHeight;
  const logoElem = document.createElement("div");
  logoElem.classList.add("github-logo");
  logoElem.style.display = "block";
  logoElem.style.width = logoSize + "px";
  logoElem.style.height = logoSize + "px";
  const linkElem = document.createElement("a");
  linkElem.href = "https://github.com/JetBrains/lets-plot";
  linkElem.classList.add("navbar-brand", "reference", "external");
  linkElem.appendChild(logoElem);
  document.querySelector("#navbar .navbar-header").appendChild(linkElem);
}

function handlePreviewsSliders() {
  if (document.getElementsByClassName('previews-slider-window').length == 0) return;
  const psWindows = document.getElementsByClassName('previews-slider-window');
  for (let i = 0; i < psWindows.length; i++) {
    const psWindow = psWindows[i];
    const psId = Array.from(psWindow.classList).find((className) => className.indexOf("id-") == 0);
    const psContent = document.getElementsByClassName(`previews-slider-content ${psId}`)[0];
    handlePreviewsSlider(psWindow, psContent);
  }
}

function handlePreviewsSlider(psWindow, psContent) {
  if (psWindow.getElementsByClassName('reference').length < 3) return;
  const btnLeft = psWindow.getElementsByClassName('reference')[0];
  const nbLinkElem = psWindow.getElementsByClassName('reference')[1];
  const nbImgElem = nbLinkElem.getElementsByTagName('img')[0];
  const btnRight = psWindow.getElementsByClassName('reference')[2];
  const previews = psContent.getElementsByClassName('d-flex');
  const previewsCount = previews.length;
  let currentPreviewId = 0;
  const onClick = function (event, direction) {
    event.preventDefault();
    if (previewsCount < 2) return;
    currentPreviewId = (previewsCount + currentPreviewId + direction) % previewsCount;
    const previewLinkElem = previews[currentPreviewId].getElementsByClassName('reference')[0];
    const previewImgElem = previewLinkElem.getElementsByTagName('img')[0];
    nbImgElem.setAttribute('src', previewImgElem.getAttribute('src').replace('.png', '_4x3.png'));
    nbLinkElem.setAttribute('href', previewLinkElem.getAttribute('href'));
  }
  btnLeft.onclick = (event) => onClick(event, -1);
  btnRight.onclick = (event) => onClick(event, 1);
}

function handlePreviewsPickers() {
  if (document.getElementsByClassName('previews-picker-window').length == 0) return;
  const ppWindows = document.getElementsByClassName('previews-picker-window');
  for (let i = 0; i < ppWindows.length; i++) {
    const ppWindow = ppWindows[i];
    const ppId = Array.from(ppWindow.classList).find((className) => className.indexOf("id-") == 0);
    const ppContent = document.getElementsByClassName(`previews-picker-content ${ppId}`)[0];
    handlePreviewsPicker(ppWindow, ppContent);
  }
}

function handlePreviewsPicker(ppWindow, ppContent) {
  const replaces = {
    "one_variable.png": "geom_bar.png",
    "two_variables.png": "geom_jitter_cc.png",
    "three_variables.png": "geom_contour.png",
    "functions.png": "geom_area.png",
    "error_bars.png": "geom_crossbar.png",
    "graphical_primitives.png": "geom_segment.png",
    "stats.png": "correlation.png",
    "general_purpose_scales.png": "identity_scales.png",
    "color_and_fill_scales.png": "grey_scale.png",
    "x_and_y_location_scales.png": "reversed_scale.png",
    "shape_scales.png": "shape_scale.png",
    "size_scales.png": "size_scale.png",
    "coordinate_systems.png": "map_coordinates.png",
    "faceting.png": "facet_grid.png",
    "position_adjustments.png": "dodge_position.png",
    "labels.png": "xlab_ylab.png",
    "legends.png": "scale_way.png",
    "themes.png": "default_theme.png",
    "zooming.png": "with_clipping.png",
  };
  const replacesNames = Object.keys(replaces);
  const nbLinkElem = ppWindow.getElementsByClassName('reference')[0];
  const nbImgElem = nbLinkElem.getElementsByTagName('img')[0];
  const previewsLinkElems = ppContent.getElementsByClassName('reference');
  const onClick = function (event) {
    event.preventDefault();
    // Place for changing image from preview to big size
    let src = event.target.getAttribute('src');
    for (let i = 0; i < replacesNames.length; i++)
      if (src.indexOf(replacesNames[i]) != -1)
        src = src.replace(replacesNames[i], replaces[replacesNames[i]]);
    nbImgElem.setAttribute('src', src);
    nbLinkElem.setAttribute('href', event.currentTarget.getAttribute('href'));
  }
  for (let i = 0; i < previewsLinkElems.length; i++)
    previewsLinkElems[i].onclick = onClick;
}

function fixPanels() {
  const cards = document.getElementsByClassName('card docutils');
  for (let i = 0; i < cards.length; i++)
    cards[i].classList.remove('shadow');
}

function addTargetToExternalReferences() {
  const links = document.getElementsByClassName('reference external');
  for (let i = 0; i < links.length; i++)
    links[i].setAttribute('target', '_blank');
}

function handlePreviewGallery() {
  if (document.getElementsByClassName('preview-gallery').length == 0) return;
  const previewsPerRow = 4;
  const previews = document.getElementsByClassName('preview-gallery')[0].getElementsByClassName('d-flex');
  const updatePreviewGallery = function (currentHiddenRowId) {
    for (let i = 0; i < previews.length; i++)
      if (i < currentHiddenRowId * previewsPerRow) {
        previews[i].classList.remove('hidden');
        previews[i].style.height = String(previews[i].offsetWidth) + 'px';
      } else
        previews[i].classList.add('hidden');
  }
  const thereIsMorePreviews = function () {
    return !![...previews].find(elem => elem.classList.contains('hidden'));
  }
  let hiddenRowId = 1;
  const loadMoreOnClick = function (event) {
    if (thereIsMorePreviews()) {
      event.preventDefault();
      hiddenRowId++;
      updatePreviewGallery(hiddenRowId);
      if (thereIsMorePreviews()) return;
      event.target.innerHTML = "Go to Gallery";
    }
  }
  updatePreviewGallery(hiddenRowId);
  document.getElementById('preview-gallery-more').getElementsByTagName('a')[0].onclick = loadMoreOnClick;
}