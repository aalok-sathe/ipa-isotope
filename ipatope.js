// external js: isotope.pkgd.js


// init Isotope
var $grid = $('.grid').isotope({
  itemSelector: '.phoneme-item',
  // layoutMode: 'fitRows',

  layoutMode: 'packery',
  packery: {
    gutter: 5
  },
  stamp: '.stamp',

  getSortData: {
    name: '[name]',
    symbol: '.symbol',
    number: '.number parseInt',
    sonority: '.sonority parseFloat',
    category: '[data-category]',
    weight: function(itemElem) {
      var weight = $(itemElem).find('.weight').text();
      return parseFloat(weight.replace(/[\(\)]/g, ''));
    }
  }
});

// filter functions
var filterFns = {
  // show if number is greater than 50
  numberGreaterThan50: function() {
    var number = $(this).find('.number').text();
    return parseInt(number, 10) > 50;
  },
  // show if sonority is greater than 3
  sonGreaterThan3: function() {
    var number = $(this).find('.sonority').text();
    return parseFloat(number, 10) > 3;
  },
  // show if name ends with -ium
  ium: function() {
    var name = $(this).find('.name').text();
    return name.match(/ium$/);
  }
};

// bind filter button click
$('#filters').on('click', 'button', function() {
  var filterValue = $(this).attr('data-filter');
  // use filterFn if matches value
  filterValue = filterFns[filterValue] || filterValue;
  $grid.isotope({
    filter: filterValue
  });
});

// bind sort button click
$('#sorts').on('click', 'button', function() {
  var sortByValue = $(this).attr('data-sort-by');
  $grid.isotope({
    sortBy: sortByValue
  });
});

// change is-checked class on buttons
$('.button-group').each(function(i, buttonGroup) {
  var $buttonGroup = $(buttonGroup);
  $buttonGroup.on('click', 'button', function() {
    $buttonGroup.find('.is-checked').removeClass('is-checked');
    $(this).addClass('is-checked');
  });
});