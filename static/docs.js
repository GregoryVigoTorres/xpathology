'use-strict'

// show hide long lists
var hiddenSiblings = document.getElementsByClassName('show-hide-siblings');

for (i=0; i < hiddenSiblings.length; i++) {
  hiddenSiblings[i].addEventListener('click', (event) => showHideList(event));
};

var hiddenTableRows = document.getElementsByClassName('show-hide-rows');
for (i=0; i<hiddenTableRows.length; i++) {
  hiddenTableRows[i].addEventListener('click', (event) => showHideRow(event));
};

var showHideRow = function(eve) {
  // this is for tables .show-hide-rows
  var getTable = function(elem) {
    // gets the parent table for event.target
    while (elem && elem.tagName.toLowerCase() != 'table') {
      elem = elem.parentElement;
    };
    return elem;
  };
  var table = getTable(eve.target);
  var rows = table.querySelectorAll('tbody tr');

  for (i=0; i<rows.length; i++) {
    rows[i].classList.toggle('hidden');
  };
};

var showHideList = function(eve) {
  // this only works with lists
  // siblings of .show-hide-siblings elements
  // inside a show-hide container
  var parElem = eve.target.parentElement;
  var hiddenElems = parElem.getElementsByClassName('show-hide');

  for (i=0; i<hiddenElems.length; i++) {
    hiddenElems[i].classList.toggle('hidden');
  };
};
