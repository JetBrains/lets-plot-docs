document.addEventListener("DOMContentLoaded", function () {
  fixNavLinks();
  fixSearchResults();
  removeEmptySecondarySidebar();
  removeCardShadows();
  addTargetToExternalReferences();
});

function fixNavLinks() {
  const navItems = document.getElementsByClassName("navbar-nav")[0].getElementsByClassName("nav-item");
  for (let i = 0; i < navItems.length; i++) {
    const navLink = getNavLinkOrNull(navItems[i]);
    if (navLink === null) continue;
    navLink.classList.remove("nav-external");
    navLink.classList.add("nav-internal");
  }
}

function fixSearchResults() {
  const searchResultRoot = document.getElementById("search-results");
  if (searchResultRoot == null) return;
  const observerConfig = { attributes: false, childList: true, subtree: false };
  const observerCallback = (mutationList, observer) => {
    for (const mutation of mutationList) {
      if (mutation.type !== "childList") continue;
      const searchResultContainers = searchResultRoot.querySelectorAll("ul.search");
      if (searchResultContainers.length == 0) continue;
      removeSearchItemsWithoutTitle(searchResultContainers[searchResultContainers.length - 1]);
    }
  };
  const observer = new MutationObserver(observerCallback);
  observer.observe(searchResultRoot, observerConfig);
}

function removeSearchItemsWithoutTitle(searchResultContainer) {
  function removeSearchItemWithoutTitle(searchItem) {
    const linkElement = searchItem.getElementsByTagName("a")[0];
    if (linkElement.textContent.trim() == "<no title>") {
      searchItem.remove();
    }
  }
  const observerConfig = { attributes: false, childList: true, subtree: false };
  const observerCallback = (mutationList, observer) => {
    for (const mutation of mutationList) {
      if (mutation.type !== "childList") continue;
      Array.from(searchResultContainer.querySelectorAll("li")).forEach(function (searchResultElement) {
        removeSearchItemWithoutTitle(searchResultElement);
      });
    }
  };
  const observer = new MutationObserver(observerCallback);
  observer.observe(searchResultContainer, observerConfig);
}

function removeEmptySecondarySidebar() {
  const sidebarElements = document.getElementsByClassName("bd-sidebar-secondary bd-toc");
  for (let i = 0; i < sidebarElements.length; i++) {
    const sidebarElement = sidebarElements[i];
    if (sidebarElement.hasChildNodes()) continue;
    sidebarElement.style.display = "none";
  }
}

function removeCardShadows() {
  const cards = document.getElementsByClassName('sd-card docutils');
  for (let i = 0; i < cards.length; i++)
    cards[i].classList.remove('sd-shadow-sm');
}

function addTargetToExternalReferences() {
  const exceptions = [
    "pages/charts.html",
    "pages/maps.html",
    "pages/geocoding.html",
  ];
  Array.from(document.getElementsByClassName("reference external")).forEach(function (linkElement) {
    if (exceptions.indexOf(linkElement.getAttribute("href")) == -1) {
        linkElement.setAttribute('target', '_blank');
    } else {
        linkElement.classList.remove("external");
        linkElement.classList.add("internal");
    }
  });
}

function isLandingPage() {
  return document.getElementsByClassName("bd-breadcrumbs").length == 0;
}

function getNavLinkOrNull(navItem) {
  const navLinks = navItem.getElementsByClassName("nav-link");
  return navLinks.length != 0 ? navLinks[0] : null;
}