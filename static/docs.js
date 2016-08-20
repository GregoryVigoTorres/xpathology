'use-strict'

// show hide long lists
var hiddenSiblings = document.getElementsByClassName('show-hide-siblings');

for (i=0; i < hiddenSiblings.length; i++) {
    hiddenSiblings[i].addEventListener('click', (event) => showHideList(event));
};

var showHideList = function(eve) {
    var parElem = eve.target.parentElement;
    var hiddenElems = parElem.getElementsByClassName('show-hide');

    for (i=0; i<hiddenElems.length; i++) {
        hiddenElems[i].classList.toggle('hidden');
    };
};
